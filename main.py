import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import urllib3
from datetime import datetime as dt

# 忽略 SSL 警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 配置重试机制
retry_strategy = Retry(
    total=5,
    status_forcelist=[429, 500, 502, 503, 504],
    allowed_methods=["HEAD", "GET", "OPTIONS"]  # 替换 method_whitelist
)
adapter = HTTPAdapter(max_retries=retry_strategy)
http = requests.Session()
http.mount("https://", adapter)
http.mount("http://", adapter)


# 初始化 m3u8 文件头
m3u8_file = "#EXTM3U x-tvg-url=\"https://live.fanmingming.com/e.xml\"\n"

# 添加更新时间
current_time = dt.now().strftime("%Y-%m-%d %H:%M:%S")
m3u8_file += f"#EXTINF:-1 tvg-name=\"{current_time}\" tvg-logo=\"https://live.fanmingming.com/tv/{current_time.replace(' ', '%20')}.png\" group-title=\"更新时间\",{current_time}\nurl\n"

# 获取频道信息
channel_list_url = "https://app.ymedium.top/web/v1/channels"
channel_response = requests.get(channel_list_url).json()
channelGroups = channel_response['data']['channelGroups']

# 遍历每个频道组
for channelGroup in channelGroups:
    group_name = channelGroup["name"]
    for channel in channelGroup["channels"]:
        channel_name = channel["name"]
        channel_logo = channel["img"]
        channel_url = channel["url"]
        channel_info_url = f"https://hlove.tv/_next/data/rvXZUIAlaCnCKIyqQZng7/live/{channel_url}.json?id={channel_url}"

        try:
            response = http.get(channel_info_url, verify=False)
            channel_info = response.json()
            m3u8_url = channel_info["pageProps"]["purl"]
            m3u8_file += f"#EXTINF:-1 tvg-name=\"{channel_name}\" tvg-logo=\"{channel_logo}\" group-title=\"{group_name}\",{channel_name}\n{m3u8_url}\n"
            print(f"成功添加频道：{channel_name}")
        except requests.exceptions.RequestException as e:
            print(f"请求错误：{e}")
        except Exception as e:
            print(f"其他错误：{e}")

# 输出到文件
output_path = "./output/hlove.m3u"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(m3u8_file)

print(f"已生成 m3u 文件，保存路径：{output_path}")
