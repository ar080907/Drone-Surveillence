# Drone-Surveillence

An AI-powered drone surveillance system built using **YOLO11**, **OpenCV**, and **Python** for real-time drone detection and restricted zone monitoring.

The system allows users to define a custom restricted zone, detects drones in real time, and automatically generates alerts when a drone enters the protected area.

---

##  Features

*  Fine-tuned YOLO11 model for drone detection
*  Real-time object detection using OpenCV
*  Interactive restricted zone selection with mouse clicks
*  Automatic intrusion detection
*  Automatic evidence capture when an intrusion occurs
*  Live surveillance dashboard
*  Intrusion counter
*  Color-coded detection boxes and alerts
*  Supports webcam, IP camera, or video files

---


##  Project Structure

```
drone-surveillance-yolo/
│
├── models/
│   └── best.pt
│
├── src/
│   └── surv.py
│
├── screenshots/
│
├── intrusions/
│
├── train.py
├── requirements.txt
├── README.md

```

---

##  Installation

Clone the repository:

```bash
git clone https://github.com/ar080907/Drone-Surveillence.git
cd Drone-Surveillence
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

##  Model

The repository includes a fine-tuned **YOLOv8n** model trained for drone detection.

Classes:

* Drone


---

##  Training

To train the model on your own dataset:

```bash
python train.py
```

Make sure your dataset follows the Ultralytics YOLO format and update the dataset path in `data.yaml`.

---

##  Running the Surveillance System

Run:

```bash
python src/surv.py
```

### Workflow

1. Select four points to create the restricted zone.
2. The surveillance system starts automatically.
3. Every detected drone is checked against the restricted zone.
4. If a drone enters the zone:

   * A warning is displayed.
   * The intrusion counter increases.
   * A screenshot is saved inside the `intrusions/` folder.

---

##  Technologies Used

* Python
* Ultralytics YOLO
* OpenCV
* NumPy

---

##  Future Improvements

* Kalman Filter based tracking
* Drone speed estimation
* Distance estimation
* Multi-camera surveillance
* ROS 2 integration
* Real-time notifications
* Web dashboard

---

##  Example Output

The system displays:

* Detection confidence
* Restricted zone visualization
* Live system status
* Intrusion counter
* Automatic intrusion screenshots

---

##  Contributing

Contributions, suggestions, and improvements are welcome.

Feel free to fork the repository and submit a pull request.

---
GitHub: https://github.com/YOUR_USERNAME

