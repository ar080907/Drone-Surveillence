from ultralytics import YOLO
import numpy as np
import cv2
from datetime import datetime
cam=cv2.VideoCapture(0)
model=YOLO("models/detector.pt")

intrusion=False
counter=0
points = []
ret, frame = cam.read()
def draw_zone(event, x, y, flags, param):
    global points
    if event == cv2.EVENT_LBUTTONDOWN:
            points.append((x, y))
cv2.namedWindow("Zone")
cv2.setMouseCallback("Zone", draw_zone)
while True:
    display=frame.copy()
    for point in points:
        cv2.circle(display, point, 5, (0,255,255), -1)
    cv2.imshow("Zone", display)
    key=cv2.waitKey(1)
    if len(points) == 4:
        break
    if key == ord('q'):
        break
cv2.destroyAllWindows()
zone = np.array([points], np.int32)
cam.set(cv2.CAP_PROP_POS_FRAMES, 0)
while True:
    ret,frame=cam.read()        
    if not ret:
        break
    results=model.predict(frame,conf=0.1,save=False)
    anotatedframe = frame.copy()
    for box in results[0].boxes:
        x1,y1,x2,y2=box.xyxy[0]
        x1 =int(x1)
        y1 =int(y1) 
        x2=int(x2)
        y2=int(y2)
        yc = (y2 + y1)//2
        xc = (x2 + x1)//2
    if len(results[0].boxes) > 0:
        inside = cv2.pointPolygonTest(zone, (float(xc), float(yc)), False)
        if inside >= 0:
         color = (0, 0, 255)
         if intrusion==False:
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            cv2.imwrite(f"intrusion/intrusion_{timestamp}.jpg", anotatedframe)
            counter+=1
         intrusion=True
        else:
            print(f"Drone is outside the zone: (xc: {xc}, yc: {yc})")
            color = (0, 255, 0)
            intrusion=False
        cv2.rectangle(anotatedframe, (x1,y1), (x2,y2), color, 2)
        conf = float(box.conf)
        label = f"Drone {conf*100:.1f}%"
        cv2.putText(
        anotatedframe,
        label,
        (x1, y1 - 10),
        cv2.FONT_HERSHEY_DUPLEX,
        0.6,
        color,
        2
        )
    else:
        color = (0, 255, 0)
        intrusion=False
    for point in points:
     cv2.circle(anotatedframe, point, 5, (0,255,255), -1)
    cv2.rectangle(
    anotatedframe,
    (10, 10),       
    (350, 170),      
    (40, 40, 40),    
    -1              
)
    cv2.rectangle(
    anotatedframe,
    (10,10),
    (350,170),
    (0,255,255),
    2
)
    cv2.putText(
    anotatedframe,
    "AI DRONE SURVEILLANCE",
    (20,35),
    cv2.FONT_HERSHEY_DUPLEX,
    0.7,
    (255,255,255),
    2
)
    cv2.putText(
    anotatedframe,
    f"Intrusions: {counter}",
    (20, 65),
    cv2.FONT_HERSHEY_DUPLEX,
    0.7,
    (255, 255, 255),
    2
)
    
    cv2.putText(
    anotatedframe,
    "Zone: Restricted",
    (20, 115),
    cv2.FONT_HERSHEY_DUPLEX,
    0.7,
    (0, 0, 255),
    2
)
    cv2.putText(
    anotatedframe,
    "Detection: Active",
    (20, 140),
    cv2.FONT_HERSHEY_DUPLEX,
    0.7,
    (255, 255, 0),
    2
)
   
    
    cv2.putText(
    anotatedframe,
    f"Status: {'Intrusion Detected' if intrusion else 'No Intrusion'}",
    (20, 90),
    cv2.FONT_HERSHEY_DUPLEX,
    0.7,
    color,
    2
)
    cv2.polylines(anotatedframe, [zone], True, color, 2)
    
    cv2.imshow("Drone Detection", anotatedframe)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()