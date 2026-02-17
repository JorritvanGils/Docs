from ultralytics import YOLO
import os

yolo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

image_path = os.path.join(yolo_root, "inference_images", "2020_08_08_Lichtfang_Hahnengrund_6729.JPG")
# image_path = os.path.join(yolo_root, "inference_images", "car.jpg")

model = YOLO("yolov8n.pt")

results = model.predict(
    image_path,
    # conf=0.25,
    conf=0.01,  # Extremely low confidence threshold
    # iou=0.5,      
    save=True,
    project=os.path.join(yolo_root, "runs"),
    name="pretrained_inference",
    exist_ok=True
)

