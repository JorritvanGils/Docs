import os
from ultralytics import YOLO

# Model options: 'n', 's', 'm', 'l', 'x'
MODEL_SIZE = "n"
BATCH_SIZE = 16
EPOCHS = 1
AUGMENT = False

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    yolo_root = os.path.abspath(os.path.join(base_dir, ".."))

    model_file = os.path.join(yolo_root, f"yolov8{MODEL_SIZE}.pt")
    data_file = os.path.join(yolo_root, "data.yaml")
    project_dir = os.path.join(yolo_root, "runs_gpu")

    print("Working directory:", os.getcwd())
    print("Saving to:", project_dir)

    model = YOLO(model_file)

    model.train(
        data=data_file,
        epochs=EPOCHS,
        imgsz=640,
        batch=BATCH_SIZE,
        device="0",  # GPU 0
        workers=4,
        augment=AUGMENT,
        project=project_dir,
        name=f"train_{MODEL_SIZE}",
        exist_ok=True
    )

    results = model.val(data=data_file)
    print("Validation results:", results)

    export_path = model.export(format="onnx", imgsz=640)
    print("ONNX exported to:", export_path)

if __name__ == "__main__":
    main()
