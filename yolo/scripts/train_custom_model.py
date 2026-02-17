from ultralytics import YOLO

def main():
    print("YOLOv8 Training Template")
    print("You can customize: model type (n/s/m/l/x), batch size, image size, epochs, augmentations")

    model_choice = input("Choose model (nano=n, small=s, medium=m, large=l, x-large=x) [default n]: ") or "n"
    model_file = f"yolov8{model_choice}.pt"

    batch_size = input("Batch size [default 16]: ") or 16
    batch_size = int(batch_size)

    epochs = input("Epochs [default 50]: ") or 50
    epochs = int(epochs)

    augment_input = input("Use augmentations? (y/n) [default y]: ") or "y"
    augment = True if augment_input.lower() == "y" else False

    model = YOLO(model_file)

    model.train(
        data="data.yaml",
        epochs=epochs,
        imgsz=640,
        batch=batch_size,
        device="0",
        workers=4,
        augment=augment,
        project="runs_gpu",
        name=f"train_{model_choice}",
        exist_ok=True
    )

    # Optional: validate and export
    results = model.val(data="data.yaml")
    print("Validation results:", results)
    model.export(format="onnx", imgsz=640)
    print("Model exported to ONNX format")

if __name__ == "__main__":
    main()
