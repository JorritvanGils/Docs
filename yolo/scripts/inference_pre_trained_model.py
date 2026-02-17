from ultralytics import YOLO
import os

yolo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

image_path = os.path.join(yolo_root, "inference_images", "2020_08_08_Lichtfang_Hahnengrund_6729.JPG")
# image_path = os.path.join(yolo_root, "inference_images", "car.jpg")

use_pretrained = False
conf = 0.1 # 0.01 , 0.1, 0.25, 0.5, 0.75

if use_pretrained:
    model = YOLO('yolo8n.pt')  # Load the pretrained YOLOv8n model
    save_name = "inf/pretrained"
else:
    trained_model_path = os.path.join(
        yolo_root,
        "runs/detect/runs_cpu/test_run/weights/best.pt"  # pick best.pt or last.pt
    )
    model = YOLO(trained_model_path)
    save_name = "inf/finetuned"

model_name = os.path.basename(trained_model_path)

results = model.predict(
    image_path,
    conf=conf,
    iou=0.3,     # increase results in more detections (boxes have to overlap more to be considered the same object)
    save=True,
    project=os.path.join(yolo_root, "runs"),
    name=save_name,
    exist_ok=True
)

