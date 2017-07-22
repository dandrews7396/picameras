#!/usr/bin/python3,4

import time
import io
import picamera

# Create in-memory byte-stream
my_stream = io.BytesIO()
with picamera.PiCamera() as camera:
    camera.start_preview()
    # Camera warm-up time
    time.sleep(2)
    camera.capture(my_stream, 'jpeg')
