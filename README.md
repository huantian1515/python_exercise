# 💰 个人记账本

一个命令行记账工具，支持收支记录、分类筛选、数据持久化。

## 功能

- 记一笔账：记录收入或支出，包含金额、分类、备注
- 查看所有记录：按日期排序展示，汇总总收入/总支出/结余
- 按分类筛选：按指定分类过滤记录并查看汇总
- 数据自动存盘：记录保存到 `data.json`，重启不丢失

## 如何运行

```bash
# 1. 克隆仓库
git clone https://github.com/huantian1515/python_exercise.git
cd python_exercise

# 2. 创建虚拟环境（可选）
python -m venv venv
venv\Scripts\activate

# 3. 运行（无需安装依赖，仅使用标准库）
python main.py
```

## 技术栈

- Python 3.12+
- 标准库（json、datetime、pathlib）

## 项目结构

```
├── main.py          # 入口，命令行交互菜单
├── tracker.py       # 记账核心逻辑（添加/查看/筛选）
├── storage.py       # 数据持久化（JSON 读写）
├── utils.py         # 工具函数（格式化输出、统计汇总）
├── data.json        # 账本数据文件
└── requirements.txt # 完整 Python 环境依赖（项目核心仅用标准库）
```