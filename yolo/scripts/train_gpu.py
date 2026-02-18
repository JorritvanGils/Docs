from ultralytics import YOLO

# Model options: 'n' (nano), 's' (small), 'm' (medium), 'l' (large), 'x' (x-large)
MODEL_SIZE = "n"
BATCH_SIZE = 16
EPOCHS = 1
AUGMENT = False

def main():
    model_file = f"yolov8{MODEL_SIZE}.pt"
    model = YOLO(model_file)

    model.train(
        data="data.yaml",
        epochs=EPOCHS,
        imgsz=640,
        batch=BATCH_SIZE,
        device="0",
        workers=4,
        augment=AUGMENT,
        project="runs_gpu",
        name=f"train_{MODEL_SIZE}",
        exist_ok=True
    )

    results = model.val(data="data.yaml")
    print("Validation results:", results)

    model.export(format="onnx", imgsz=640)
    print("Model exported to ONNX format")

if __name__ == "__main__":
    main()
