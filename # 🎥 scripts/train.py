```python
from ultralytics import YOLO

model = YOLO('yolov8m.pt')
model.train(data='dataset/data_custom.yaml', epochs=100, imgsz=640)
```
