from __future__ import print_function
import numpy as np
import cv2
import os
import shutil
import sys
print(cv2.__version__)
vidName = raw_input("Enter video file: ")
dirname = os.path.join("frames", vidName)

# Check to see if frames folder already exists, if it does.. remove it
if os.path.exists(dirname):
  print ("Removing existing files in " + dirname + " directory")
  shutil.rmtree(dirname)

# make sure to install open-cv through pip install opencv-python
# it will install opencv 3.2
vidcap = cv2.VideoCapture(vidName)
success,image = vidcap.read() # 2-tuple, boolean, image

count = 0
diffs = []

fc = vidcap.get(cv2.CAP_PROP_FRAME_COUNT)
fps = vidcap.get(cv2.CAP_PROP_FPS)
print('Frame count: %d' % fc)
print('FPS: %d' % fps)

# If vidcap.read() was successful, start slicing frames
if success:
  print("Slicing frames...")
  os.mkdir(dirname)
# Else, exit
else:
  print("Unsuccessful. Check to see if video exists")
  sys.exit()
  
while success:
    if count > 0 and count < (fc-10):
        diff = sum(sum(sum(abs(image-previmage))))
        diffs.append(diff)
        if diff > (370 * 1.5):
            cv2.imwrite(os.path.join(dirname, "frame%06d.jpg" % count), image)     # save frame as JPEG file
    previmage = image
    #print image.shape
    #print 'Read a new frame: ', success
    count += 1
    success,image = vidcap.read()

diffa = np.asarray(diffs)
print(np.min(diffa))
print(np.max(diffa))
print(np.mean(diffa))
print(np.median(diffa))
print('Total frames: %d' % count)
