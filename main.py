import requests

m3u8_file ="#EXTM3U\n"

channel_list_url = "https://app.ymedium.top/web/v1/channels"
channel_response = requests.get(channel_list_url).json()
channelGroups = channel_response['data']['channelGroups']
for channelGroup in channelGroups:
    channel_list = channelGroup["channels"]
    group_name = channelGroup["name"]
    for i in channel_list:
        channel_name = i["name"]
        channel_logo = i["img"]
        channel_url = i["url"]
        channel_info_url = f"https://hlove.tv/_next/data/7Qm62oGR1Y6qugvX0IHh_/live/{channel_url}.json?id={channel_url}"
        channel_info_response = requests.get(channel_info_url).json()
        m3u8_url = channel_info_response["pageProps"]["purl"]
        m3u8_file += f"#EXTINF:-1 tvg-logo=\"{channel_logo}\" group-title=\"{group_name}\",{channel_name}\n{m3u8_url}\n"
        print(f"频道：{channel_name} 已添加")

with open("./output/hlove.m3u8", "w") as f:
    f.write(m3u8_file)
print("已生成m3u8文件")