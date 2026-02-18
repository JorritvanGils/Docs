from ultralytics import YOLO

def main():
    model = YOLO("yolov8n.pt")

    model.train(
        data="data.yaml",
        epochs=1,
        imgsz=640,
        batch=8,
        device="cpu",
        workers=2,
        project="runs_cpu",
        name="test_run",
        exist_ok=True
    )

if __name__ == "__main__":
    main()
