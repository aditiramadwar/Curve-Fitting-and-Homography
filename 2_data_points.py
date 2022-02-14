# @file 2_data_points.py
# @author Aditi Ramadwar (adiram@umd.edu)
# @brief Extract data points from the video
# @date 2022-02-04
import cv2
from numpy import where 
import matplotlib.pyplot as plt

def process_video(vid_name):
    cap = cv2.VideoCapture("data/"+vid_name+'.mp4')
    # Check if video was accessed or not
    if (cap.isOpened()== False):
        print("Error opening video stream or file")
    # Create a file to write the data points on
    f = open("results/"+vid_name+".txt", "w")

    # Read until video is completed
    while(cap.isOpened()):
      # Capture frame-by-frame
      ret, frame = cap.read()
      if ret == True:
        # Make the frame gray
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Apply thereshold to the pixels
        b = where(gray<200)
        # Get the maximum and minimum coordinates of the ball in each frame
        y_max = max(b[0])
        y_min = min(b[0])
        x_max = max(b[1])
        x_min = min(b[1])
        # Get the centroid of the ball in each frame
        x_mid=int((x_min+x_max)/2) 
        y_mid=int((y_min+y_max)/2)
        # Write the centroid coordinates in a file
        row = '{0} {1}'.format(x_mid, y_mid)
        f.write('{0}\n'.format(row))
        # cv2.imshow('Frame',image)
        # cv2.waitKey(0)
        # Press Q on keyboard to  exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
          break
      # Break the loop
      else: 
        break

    print('Done analysing '+ vid_name+'!')
    
    # When everything done, release the video capture object
    cap.release()

    # Closes all the frames
    cv2.destroyAllWindows()
    
# Load the video and create object
process_video('Ball_travel_10fps')
process_video('Ball_travel_2_updated')


