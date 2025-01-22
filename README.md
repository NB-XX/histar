## 项目简介

`hlove` 是一个用于定时从 [hlove.tv/live](https://hlove.tv/live) 获取全部直播频道的直播源信息，并将这些信息整合到一个标准的 `m3u8` 文件中的工具。  
该项目旨在方便用户快速获取和整理网络直播资源，支持定时任务的自动化运行。

---

> [!CAUTION]
> 原网站新增`JWT token`校验登录用户，在方案成熟之前仅支持[直播源](./output/hlove.m3u8)可用，不保证脚本可正常运行。

---

## 文件说明

- `main.py`：主程序，用于抓取直播数据并生成 `m3u8` 文件。
- `test.py`：`main.py`的测试版本。
- `requirements.txt`：项目依赖库。
- `output/`：存放生成的 `m3u8` 文件。

---

## 待办事项 (To-Do List)

1. **增加直播源可用性测试**：在生成 `m3u8` 文件之前，检测直播源的可用性，过滤掉无效的链接。
2. **增加APP侧接口提取**：使用权限和优先级更高的 [APP](https://hlove.tv/download) 替代网页版抓取。

---

## 许可证

本项目采用 MIT 许可证，详见 [LICENSE](./LICENSE) 文件。

---

## 联系方式

如有任何问题或建议，请提交 [Issues](https://github.com/NB-XX/hlove/issues)。