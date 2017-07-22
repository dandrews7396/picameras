#!/usr/bin/python3.4

##################################################################
##          test.py:- The test of the picamera                  ##
##                      using the opencv module                 ##
##################################################################

# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
 
### initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (320, 160)
with PiRGBArray(camera) as output:  
    #grab an image from the camera
    camera.capture(output, format="rgb")
    print("Captured {} x {} image".format(output.array.shape[1],
                                          output.array.shape[0],))
    output.truncate(0)
    image = output.array

### display the image on screen and wait for a keypress
print(image)
cv2.imshow("Image", image)
cv2.waitKey(0)



