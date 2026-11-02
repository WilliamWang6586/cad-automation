# CAD 自动化绘图 Skill（优化版）

> AutoCAD 二次开发知识库：COM/ActiveX 接口调用、图层与标注样式批量操作、DXF 文件读写（ezdxf）、脚本调试与批处理。附带最小可跑示例，不装 AutoCAD 也能先生成 DXF 验证思路。

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

把本目录整个复制到你的 agent 技能目录（如 `~/.agent/skills/` 或所用工具的 skills 目录）：

```bash
git clone https://github.com/WilliamWang6586/cad-automation.git
cp -r cad-automation "<你的技能目录>/"
```

放进去后，agent 读到 `SKILL.md` 即可按其中的触发条件调用。

## 文件

- `ATTRIBUTION.md`
- `SKILL.md`
- `scripts/dxf_minimal.py`

## 说明

