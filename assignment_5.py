
import os

os.system("pip install -qr requirements.txt")
os.system("python train.py --epochs 3 --img 640 --cfg yolov5s.yaml --batch 64 --data ballPerson.yaml --weights weights/best.pt --hyp data/hyp.scale-3.yaml --name yolo_ballPerson_3")
os.system("python train.py --epochs 3 --img 640 --cfg yolov5s.yaml --batch 64 --data ballPerson.yaml --weights weights/best.pt --hyp data/hyp.scale-5.yaml --name yolo_ballPerson_5")
os.system("!python train.py --epochs 3 --img 640 --cfg yolov5s.yaml --batch 64 --data ballPerson.yaml --weights weights/best.pt --hyp data/hyp.scale-9.yaml --name yolo_ballPerson_9")
