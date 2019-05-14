import sys
import time
import os

import cv2

def main():
    face_cascade = cv2.CascadeClassifier('face_model.xml')
    video_capture = cv2.VideoCapture(0)

    #calibrate
    calibration_time = 2 #seconds
    proper_face_area = calibrate(face_cascade, 
                                video_capture, 
                                calibration_time)

    #track
    track(face_cascade, 
        proper_face_area, 
        video_capture, 
        display_feed=True)    

def process_frame(frame, face_cascade):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)
    max_area_face = find_max_area_face(faces)

    return max_area_face

def calibrate(face_cascade, video_capture, calibration_time):
    start = time.time()
    face_areas = []
    while True:
        if time.time() - start > calibration_time:
            break
        
        ret, frame = video_capture.read()
        max_area_face = process_frame(frame, face_cascade)
        
        if max_area_face is None:
            print("Could not recognize a face")
            continue

        x, y, w, h = max_area_face
        area = w * h
        face_areas.append(area)

    return sum(face_areas) / len(face_areas)

def is_posture_changed(proper_face_area, current_face):
    x, y, w, h = current_face
    current_face_area = w * h
    return abs(proper_face_area - current_face_area) > 0.2 * proper_face_area

def track(face_cascade, proper_face_area, video_capture, display_feed=False):
    while True:
        ret, frame = video_capture.read()
        max_area_face = process_frame(frame, face_cascade)
        
        if max_area_face is None:
            print("Could not recognize a face")
            continue

        if display_feed:
            # Draw a rectangle around the faces
            draw_face_rectangle(max_area_face, frame)
            
            # Display the resulting frame
            cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        if is_posture_changed(proper_face_area, max_area_face):
            os.system("say 'Fix your posture!'")
        else:
            os.system("say 'Keep up the good work!'")

        time.sleep(10)


    # When everything is done, release the capture
    video_capture.release()
    cv2.destroyAllWindows()

def draw_eye_rectangle(eye, frame):
    x, y, w, h = eye
    top_left_corner = (x, y)
    bottom_right_corner = (x+w, y+h)
    color = (0, 0, 255)
    width = 2
    cv2.rectangle(frame, top_left_corner, bottom_right_corner, color, width)

def draw_face_rectangle(face, frame):
    x, y, w, h = face
    top_left_corner = (x, y)
    bottom_right_corner = (x+w, y+h)
    color = (0, 255, 0)
    width = 5
    area = w * h
    print(f"Face area: {area}")
    cv2.rectangle(frame, top_left_corner, bottom_right_corner, color, width)

def find_max_area_face(faces):
    max_area = -1
    max_face = None
    if len(faces) == 0:
        return None

    for face in faces:
        x, y, w, h = face
        area = w * h
        if area > max_area:
            max_area = area
            max_face = face

    return max_face

main()
