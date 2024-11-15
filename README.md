## 项目简介

`hlove` 是一个用于定时从 [hlove.tv/live](https://hlove.tv/live) 获取全部直播频道的直播源信息，并将这些信息整合到一个标准的 `m3u8` 文件中的工具。  
该项目旨在方便用户快速获取和整理网络直播资源，支持定时任务的自动化运行。

---

## 功能特性

- **定时采集**：自动从指定网站抓取最新的直播频道信息。
- **标准输出**：将抓取到的直播源整合成符合 `m3u8` 格式的文件，便于播放器使用。
- **易于扩展**：代码结构清晰，方便添加更多功能。

---

## 使用方法

### 1. 克隆项目

```bash
git clone https://github.com/NB-XX/hlove.git
cd hlove
```

### 2. 安装依赖

项目依赖 Python 3 和 requests 库。

```bash
pip install -r requirements.txt
```

### 3. 运行项目

直接运行脚本：

```bash
python main.py
```

或配置定时任务，定时抓取最新直播源。

---

## 文件说明

- `main.py`：主程序，用于抓取直播数据并生成 `m3u8` 文件。
- `requirements.txt`：项目依赖库。
- `output/`：存放生成的 `m3u8` 文件。

---

## 待办事项 (To-Do List)

1. **增加直播源可用性测试**：在生成 `m3u8` 文件之前，检测直播源的可用性，过滤掉无效的链接。

---

## 许可证

本项目采用 MIT 许可证，详见 [LICENSE](./LICENSE) 文件。

---

## 联系方式

如有任何问题或建议，请提交 [Issues](https://github.com/NB-XX/hlove/issues)。