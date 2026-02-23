import os
from ultralytics import YOLO

from pathlib import Path


def main():
    yolo_root = Path(__file__).resolve().parent.parent

    yaml_file = "eu_cls.yaml" # nid_det.yaml or eu_cls.yaml
    dataset_name = Path(yaml_file).stem
    project_dir = yolo_root / "runs" / dataset_name / "runs_cpu"
    is_classifier = "_cls" in yaml_file
    model_name = "yolov8n-cls.pt" if is_classifier else "yolov8n.pt"
    model = YOLO(model_name)
    dataset_dir = yolo_root / "datasets" / dataset_name

    model.train(
        data=str(dataset_dir),
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
