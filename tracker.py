import cv2 as cv
import numpy


# https://stackoverflow.com/questions/36521449/how-to-load-a-video-in-opencvpython
def load_video(video):
    # Load video file 
    cap = cv.VideoCapture(video)
    # TODO Make something to check if the video is able to open
    return cap

def load_and_play_video(video):
    # https://docs.opencv.org/4.x/dd/d43/tutorial_py_video_display.html
    cap = cv.VideoCapture(video)
     
    while cap.isOpened():
        ret, frame = cap.read()
    
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        cv.imshow('frame', frame) # Can change frame to grey if grey scaled video is wanted 
        if cv.waitKey(25) == ord('q'):
            break
    
    cap.release()
    cv.destroyAllWindows()



def extract_file():
    pass

def main():
    video_path = "temp_vid/Ace.mp4"
    load_and_play_video(video_path)


if __name__ == "__main__":
    main()
    