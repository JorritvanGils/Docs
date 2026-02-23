import os
from ultralytics import YOLO

from pathlib import Path

yaml_file = "nid_det.yaml" # nid_det.yaml or eu_cls.yaml

def main():
    yolo_root = Path(__file__).resolve().parent.parent
    project_dir = yolo_root / "runs" / "runs_cpu"

    model = YOLO("yolov8n.pt")

    model.train(
        data=yolo_root / "configs" / yaml_file,
        epochs=1,
        imgsz=640,
        batch=8,
        device="cpu",
        workers=2,
        project=project_dir,
        name="test_run",
        exist_ok=True
    )

if __name__ == "__main__":
    main()
