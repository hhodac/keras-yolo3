import argparse
import os

from keras.models import load_model

import torch
import torchvision
import torchvision.transforms.functional as TF
import PIL

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

argparser = argparse.ArgumentParser(
    description='my pre-converted yolov3 wwith weights'
)

argparser.add_argument(
    '-w',
    '--weights',
    help='path to weights file'
)

argparser.add_argument(
    '-i',
    '--image',
    help='path to image file'
)

class my_yolov3:

    def __init__(self, weight_file):
        super().__init__()
        self.model = load_model(weight_file)
        self.input_w = 416
        self.input_h = 416
        self.anchors = [[116,90, 156,198, 373,326], [30,61, 62,45, 59,119], [10,13, 16,30, 33,23]]
        self.class_threshold = 0.6
        self.labels = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck",
            "boat", "traffic light", "fire hydrant", "stop sign", "parking meter", "bench",
            "bird", "cat", "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe",
            "backpack", "umbrella", "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard",
            "sports ball", "kite", "baseball bat", "baseball glove", "skateboard", "surfboard",
            "tennis racket", "bottle", "wine glass", "cup", "fork", "knife", "spoon", "bowl", "banana",
            "apple", "sandwich", "orange", "broccoli", "carrot", "hot dog", "pizza", "donut", "cake",
            "chair", "sofa", "pottedplant", "bed", "diningtable", "toilet", "tvmonitor", "laptop", "mouse",
            "remote", "keyboard", "cell phone", "microwave", "oven", "toaster", "sink", "refrigerator",
            "book", "clock", "vase", "scissors", "teddy bear", "hair drier", "toothbrush"]

    def get_model(self):
        return self.model