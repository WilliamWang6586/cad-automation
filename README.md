# CAD 自动化绘图 Skill（优化版）

> `cad-automation` —— Hermes Agent 技能。

**版本** 1.0.0 ｜ **技能名** `cad-automation`

﻿--- name: cad-automation description: CAD自动化绘图skill，内置完整的AutoCAD二次开发知识体系。支持通过Python(pyautocad/win32com)/AutoLISP/C#/VBA连接AutoCAD进行自动化绘图、编辑、图层管理、标注、块与属性、三维建模、批量处理、文件转换等。也涵盖国产中望CAD/浩辰CAD的兼容性。 category: engineering-cad version: 1.1.0 author: Delancy ---

## 用法

```
AutoCAD.Application
├── ActiveDocument (Document)
│   ├── ModelSpace        (模型空间)
│   ├── PaperSpace        (图纸空间)
│   ├── Layers            (图层集合)
│   ├── Linetypes         (线型集合)
│   ├── TextStyles        (文字样式)
│   ├── DimStyles         (标注样式)
│   ├── Blocks            (块集合)
│   ├── SelectionSets     (选择集)
│   ├── Groups            (组集合)
│   └── Utility           (角度/距离/坐标工具)
├── Documents
├── Preferences           (系统配置)
└── MenuGroups            (菜单组)
```

## 安装

```bash
# 方式一：直接链接安装（Hermes Agent）
hermes skills install https://github.com/WilliamWang6586/hermes-skills/tree/main/cad-automation

# 方式二：手动拷贝
git clone https://github.com/WilliamWang6586/hermes-skills.git && cp -r hermes-skills/cad-automation ~/AppData/Local/hermes-home/skills/
```

## 文件

- `ATTRIBUTION.md`
- `SKILL.md`
- `scripts/dxf_minimal.py`

## 说明

本技能收录于 [hermes-skills](https://github.com/WilliamWang6586/hermes-skills)，每个技能独立成目录、独立维护。内容若参考第三方项目，见本目录 `ATTRIBUTION.md`。
