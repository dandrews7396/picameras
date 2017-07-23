#!/usr/bin/python3.4

import picamera
import picamera.array
import cv2
import numpy

camera = picamera.PiCamera()
camera.rotation = 180
