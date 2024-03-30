import os
from PIL import Image
import sys


def convert_images_to_jpeg(source_folder, target_folder):
    # ターゲットフォルダが存在しない場合は作成
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    # サポートされる画像の拡張子
    supported_extensions = ['.jpg', '.jpeg', '.png', '.gif']
    # 連番を初期化
    num = 1

    # ソースフォルダ内のファイル一覧を取得
    for file in os.listdir(source_folder):
        # ファイルの拡張子を取得
        extension = os.path.splitext(file)[1].lower()
        # 拡張子がサポートされているかチェック
        if extension in supported_extensions:
            # 元の画像を開く
            with Image.open(os.path.join(source_folder, file)) as img:
                # 新しいファイル名を生成（連番 + ".jpg"）
                new_name = f"{num}.jpg"
                # 画像をJPEG形式で保存
                img.save(os.path.join(target_folder, new_name), "JPG")
                print(f"Saved {file} as {new_name} in JPG format.")
                # 連番を更新
                num += 1


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python convert_images_to_jpeg.py source_folder target_folder")
    else:
        source_folder = sys.argv[1]
        target_folder = sys.argv[2]
        convert_images_to_jpeg(source_folder, target_folder)
