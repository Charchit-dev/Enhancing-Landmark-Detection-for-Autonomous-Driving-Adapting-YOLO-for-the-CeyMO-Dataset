```python
from ultralytics import YOLO
import cv2
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--weights', type=str, required=True)
parser.add_argument('--source', type=str, required=True)
args = parser.parse_args()

model = YOLO(args.weights)
cap = cv2.VideoCapture(args.source)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)
    annotated = results[0].plot()

    cv2.imshow("Detection", annotated)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```
