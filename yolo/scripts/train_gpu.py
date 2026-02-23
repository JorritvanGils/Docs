from pathlib import Path
from ultralytics import YOLO

# Model options: 'n', 's', 'm', 'l', 'x'
MODEL_SIZE = "n"
BATCH_SIZE = 16
EPOCHS = 1
AUGMENT = False

def main():
    yolo_root = Path(__file__).resolve().parent.parent
    
    yaml_file = "nid_det.yaml" # nid_det.yaml or eu_cls.yaml
    dataset_name = Path(yaml_file).stem
    model_path = yolo_root / f"yolov8{MODEL_SIZE}.pt"
    data_path = yolo_root / "configs" / yaml_file
    project_dir = yolo_root / "runs" / dataset_name / "runs_gpu"

    print(f"Working directory: {Path.cwd()}")
    print(f"Saving to: {project_dir}")

    model = YOLO(model_path)

    model.train(
        data=data_path,
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

    results = model.val(data=data_path)
    print(f"Validation results: {results}")

    export_path = model.export(format="onnx", imgsz=640)
    print(f"ONNX exported to: {export_path}")

if __name__ == "__main__":
    main()