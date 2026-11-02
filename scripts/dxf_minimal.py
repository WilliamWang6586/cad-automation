# -*- coding: utf-8 -*-
"""无 AutoCAD 环境的 ezdxf 最小可跑示例：画一块板件轮廓并标注宽度

pip install ezdxf
python dxf_minimal.py out.dxf
"""
import sys

import ezdxf


def build(path, w=40.0, h=40.0):
    """画 w×h 板件轮廓并标注宽度

    圆角交给 AutoCAD 侧的后续命令处理（ezdxf 没有 fillet），
    这里只给能跑通的最小件。
    """
    doc = ezdxf.new("R2010", setup=True)
    doc.layers.add("OUTLINE", color=7)
    doc.layers.add("DIM", color=3)
    msp = doc.modelspace()
    msp.add_lwpolyline([(0, 0), (w, 0), (w, h), (0, h)], close=True,
                       dxfattribs={"layer": "OUTLINE"})
    msp.add_linear_dim(base=(0, -10), p1=(0, 0), p2=(w, 0),
                       dimstyle="EZDXF", dxfattribs={"layer": "DIM"}).render()
    doc.saveas(path)
    return path


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "out.dxf"
    build(out)
    # 自检：读回来必须能解析，且有两个实体
    d = ezdxf.readfile(out)
    n = len(list(d.modelspace()))
    assert n >= 2, "实体数不对: %d" % n
    print("ok", out, "entities=", n)
