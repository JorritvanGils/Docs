from pathlib import Path

# Paths
yolo_root = Path(__file__).resolve().parent.parent
dataset_path = yolo_root / "datasets" / "eu_cls"
train_dir = dataset_path / "train"

# Get all folder names and sort them alphabetically (YOLO's default behavior)
classes = sorted([f.name for f in train_dir.iterdir() if f.is_dir()])

# Create the YAML content
yaml_content = f"""# EU Moth Classification
path: {dataset_path}
train: train
val: val

names:
"""

for i, cls_name in enumerate(classes):
    yaml_content += f"  {i}: {cls_name}\n"

# Save it to your configs folder
config_file = Path(__file__).resolve().parent.parent / "configs" / "eu_cls.yaml"
config_file.parent.mkdir(exist_ok=True)
config_file.write_text(yaml_content)

print(f"✅ Generated config with {len(classes)} classes at {config_file}")