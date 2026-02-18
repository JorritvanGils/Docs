import os
from ultralytics import YOLO

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.join(base_dir, "..", "runs_cpu")

    model = YOLO("yolov8n.pt")

    model.train(
        data="data.yaml",
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
