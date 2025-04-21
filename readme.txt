# 📁 README.md

# YOLOv8 Landmark Detection on CeyMO Dataset

This project enhances landmark detection for autonomous driving by applying YOLOv8 to the [CeyMO dataset](https://github.com/SeeMoreOnRoads/CeyMo). It includes training, evaluation, and comparison with prior CNN models.

## Demo

<p float="left">
  <img src="results/predictions/bus_lane_example.png" width="45%" />
  <img src="results/predictions/night_arrow.png" width="45%" />
</p>

---

## 🔧 Features

- Custom object detection with YOLOv8
- Real-time inference on urban driving videos
- Model evaluation using mAP, Precision, Recall, F1-Score
- Bird-eye transformation preprocessing
- Comparison with other models (e.g. R-CNN, SSD)

---

## 📂 Dataset

Dataset used: **CeyMO Dataset**  
Contains 2887 high-res road marking images with polygon/box/segmentation annotations.

### Classes

`['Right Arrow', 'Diamond', 'Pedestrian Crossing', 'Cycle Lane', 'Left Arrow', 'Junction Box', 'Slow', 'Straight Arrow', 'Straight-Left Arrow', 'Straight-Right Arrow', 'Bus Lane']`

> Download from: [CeyMO GitHub](https://github.com/SeeMoreOnRoads/CeyMo)

---

## 🚀 Installation

```bash
git clone https://github.com/yourusername/landmark-detection-yolov8-ceymo.git
cd landmark-detection-yolov8-ceymo

conda create -n yolov8_env python=3.11
conda activate yolov8_env

pip install -r requirements.txt
```

---

## 🏋️‍♂️ Training

```bash
yolo task=detect mode=train epochs=100 data=dataset/data_custom.yaml model=yolov8m.pt imgsz=640
```

---

## 📹 Inference on Video

```bash
python scripts/test_video.py --weights weights/yolov8_best.pt --source dataset/test/test_video.mp4
```

---
### 🔹 Training Graphs

<p float="left">
  <img src="results/graphs/loss_curve.png" width="45%" />
  <img src="results/graphs/mAP_curve.png" width="45%" />
</p>

### 🔹 Test Scenarios Evaluated:
- Daylight and night
- Rain and dazzle lighting
- Crowded intersections
- Urban traffic flow

### 🔹 Detected Elements:
- Arrows (Straight, Left, Right, Combo)
- Pedestrian Crossings
- Junction Boxes
- Bus Lanes
- Slow Markings

### 🔹 Performance Comparison:

| Model             | F1 Score | FPS | Comments                             |
|------------------|----------|-----|--------------------------------------|
| YOLOv8           | 1.00     | 91  | Highest accuracy and speed           |
| SSD-MobileNet-v2 | 0.84     | 72  | Fast, but struggles in poor lighting |
| Mask R-CNN       | 0.90     | 45  | Accurate but slower and heavier      |

📈 Results visualized in `results/graphs/` and predictions saved in `results/predictions/`

---

## 🔮 Future Work

- Dataset expansion to fog/snow scenarios
- LiDAR/Radar sensor fusion
- Optimized deployment on edge devices


## 📊 Results

| Model         | F1 Score | FPS | Robustness |
|---------------|----------|-----|------------|
| YOLOv8        | 1.00     | 91  | Excellent  |
| SSD-MobileNet | 0.84     | 72  | Fair       |
| Mask R-CNN    | 0.90     | 45  | Good       |

---

## 🔮 Future Work

- Dataset expansion to fog/snow scenarios
- LiDAR/Radar sensor fusion
- Optimized deployment on edge devices

---

## 👨‍💼 Author

**Charchit Devkota**  
Constructor University Bremen  
**Supervisor:** Prof. Dr. Jakob Suchan

---

## 📄 License

MIT License
