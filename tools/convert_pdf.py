import sys
from marker.convert import convert_single_pdf
from marker.models import load_all_models

def main():
    if len(sys.argv) < 3:
        print("Usage: python convert_pdf.py <input_pdf> <output_md>")
        return

    input_pdf = sys.argv[1]
    output_md = sys.argv[2]

    # モデルのロード
    model_lst = load_all_models()

    # Markerによる変換
    full_text, images, out_meta = convert_single_pdf(input_pdf, model_lst)

    # Markdownとして保存
    with open(output_md, 'w', encoding='utf-8') as f:
        f.write(full_text)

if __name__ == "__main__":
    main()