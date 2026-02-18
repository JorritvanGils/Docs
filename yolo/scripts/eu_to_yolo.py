import os
import shutil

yolo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
root = os.path.join(yolo_root, "datasets", "raw", "eu-moths-dataset")

# Load metadata
with open(os.path.join(root, "images.txt")) as f:
    images = [line.strip().split(" ", 1)[1] for line in f]

with open(os.path.join(root, "labels.txt")) as f:
    labels = [int(line.strip()) for line in f]

with open(os.path.join(root, "tr_ID.txt")) as f:
    splits = [int(line.strip()) for line in f]

with open(os.path.join(root, "class_names.txt")) as f:
    class_names = [line.strip() for line in f]

for img_rel, label, split in zip(images, labels, splits):

    subset = "train" if split != 0 else "val"
    class_name = class_names[label]

    img_src = os.path.join(root, "images", img_rel)
    img_name = os.path.basename(img_rel)

    img_dst = os.path.join(
        yolo_root,
        "datasets",
        "eu_cls",
        subset,
        class_name,
        img_name
    )

    os.makedirs(os.path.dirname(img_dst), exist_ok=True)
    shutil.copy(img_src, img_dst)

print("EU dataset conversion finished.")
