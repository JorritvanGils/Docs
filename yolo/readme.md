# YOLO Object Detection with NID Dataset

This repository contains scripts and instructions for training YOLO models on the NID (Noisy Image Dataset) dataset.

## Setup Instructions

### 0. Clone Repository
```bash
git clone git@github.com:JorritvanGils/Docs.git
cd Docs/yolo
```

### 1. Download NID Dataset
```bash
git clone git@github.com:cvjena/nid-dataset.git
```

### 2. Create Virtual Environment
```bash
# Install Python 3.10 and venv
sudo apt update && sudo apt upgrade -y
sudo apt install python3-venv software-properties-common -y
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt install python3.10 python3.10-venv -y

# Create and activate environment
python3.10 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install ultralytics
```

### 3. Convert Dataset to YOLO Format
First, verify the `root` and `yolo_root` paths in `scripts/convert_to_yolo.py`, then run:
```bash
python scripts/convert_to_yolo.py
```

**Expected output structure:**
```
yolo/
 ├── images/
 │    ├── train/
 │    └── val/
 ├── labels/
 │    ├── train/
 │    └── val/
 └── data.yaml
```

### 4. Run Inference
```bash
# Choose between pre-trained or custom model (if trained)
python scripts/inference.py
```

### 5. Training Options

#### CPU / Laptop Training
```bash
python scripts/train_cpu.py
```

#### GPU Training (using Vast.ai)
1. Rent a GPU instance on [Vast.ai](https://vast.ai)
2. Connect to the instance:
```bash
ssh -A -p [PORT] root@[IP_ADDRESS] -L 8080:localhost:8080
```
3. Repeat steps 0-3 on the remote instance
4. Update the data.yaml path:
```bash
sed -i "s|/media/jorrit/ssd/career|$(pwd)|g" data.yaml
```
5. Run GPU training:
```bash
python scripts/train_gpu.py
```

## Notes
- Make sure to verify paths in configuration files before running scripts
- The data.yaml file contains dataset paths and class information
- For GPU training, ensure you have compatible CUDA drivers installed

## License
[Add your license information here]