import fitz  # PyMuPDF
import cairosvg

def pdf_to_svg(input_pdf, output_svg):
    # 打开 PDF 文件
    doc = fitz.open(input_pdf)
    
    # 获取第一页
    page = doc.load_page(0)
    
    # 将页面渲染为图像（pixmap）
    pix = page.get_pixmap()
    
    # 保存为 PNG 文件
    pix.save('page.png')
    
    # 使用 cairosvg 将 PNG 转换为 SVG
    cairosvg.svg2png(url='page.png', write_to=output_svg)

# 示例
input_pdf = 'D:/Document/github/EgoVisionGroup/Exo2Ego.github.io/assets/pdf/modelv3.pdf'
output_svg = 'modelv3.svg'
pdf_to_svg(input_pdf, output_svg)