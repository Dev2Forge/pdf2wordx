# pdf2docx 

![python-version](https://img.shields.io/badge/python->=3.6-green.svg)
<a target="_blank" href="https://codecov.io/gh/dothinking/pdf2docx"><img src="https://codecov.io/gh/dothinking/pdf2docx/branch/master/graph/badge.svg" alt="codecov"/></a>
<a target="_blank" href="https://pypi.python.org/pypi/pdf2docx/"><img src="https://img.shields.io/pypi/v/pdf2docx.svg" alt="pypi-version"/></a>
<img src="https://img.shields.io/pypi/l/pdf2docx.svg" alt="license"/>
<img src="https://img.shields.io/pypi/dm/pdf2docx" alt="downloads-pypi"/>

- 从PDF中提取数据，使用 `PyMuPDF`，例如文本、图像和绘图
- 使用规则分析布局，例如章节、段落、图像和表格
- 使用 `python-docx` 生成 docx

## 特性

- 分析并重建页面布局
    - 页面边距
    - 部分和列（仅 1 或 2 列）
    - 页眉和页脚 [待完成]

- 分析并重建段落
    - OCR 文本 [待完成]
    - 文本方向水平/垂直：从左到右，从下到上
    - 字体样式，例如字体名称、大小、粗细、斜体和颜色
    - 文本格式，例如高亮、下划线、删除线
    - 列表样式 [待完成]
    - 外部超链接
    - 段落的水平对齐（左/右/中心/两端对齐）和垂直间距
    
- 分析并重建图像
    - 内联图像
    - 灰度/RGB/CMYK 模式图像
    - 透明图像
    - 浮动图像，即文本后面的图像

- 分析并重建表格
    - 边框样式，例如宽度、颜色
    - 阴影样式，即背景颜色
    - 合并单元格
    - 垂直单元格方向
    - 部分隐藏边框的表格
    - 嵌套表格

- 使用并行处理进行页面分析

*也可以用作提取表格内容的工具，因为表格内容和格式/样式都会被分析。*

## 限制

- 基于文本的 PDF 文件
- 从左到右的语言
- 正常阅读方向，无需单词转换/旋转
- 基于规则的方法不能完全转换 PDF 布局

## 文档

- <a target="_blank" href="https://pdf2docx.readthedocs.io/en/latest/installation.html">安装</a>
- <a target="_blank" href="https://pdf2docx.readthedocs.io/en/latest/quickstart.html">快速开始</a>
    - <a target="_blank" href="https://pdf2docx.readthedocs.io/en/latest/quickstart.convert.html">转换 PDF</a>
    - <a target="_blank" href="https://pdf2docx.readthedocs.io/en/latest/quickstart.table.html">提取表格</a>
    - <a target="_blank" href="https://pdf2docx.readthedocs.io/en/latest/quickstart.cli.html">命令行界面</a>
    - <a target="_blank" href="https://pdf2docx.readthedocs.io/en/latest/quickstart.gui.html">图形用户界面</a>
- <a target="_blank" href="https://pdf2docx.readthedocs.io/en/latest/techdoc.html">技术文档（中文）</a>
- <a target="_blank" href="https://pdf2docx.readthedocs.io/en/latest/modules.html">API 文档</a>

## 示例

<div style="" class="centered">
    <img style="filter: drop-shadow(5px 5px 4px var(--body-color))" width=80% src="https://github.com/tutosrivegamerLQ/images-projects-srm-trg/raw/main/pdf2docx/sample-pdf2docx.png">
</div>