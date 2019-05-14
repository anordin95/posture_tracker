import sys
import time
import os

import cv2

class PostureTracker:

    def __init__(self, face_model_filepath, calibration_time, check_peridicity, display_feed):
        self.face_cascade = cv2.CascadeClassifier(face_model_filepath)
        self.video_capture = cv2.VideoCapture(0)
        self.calibration_time = calibration_time #seconds
        self.check_periodicity = check_peridicity #seconds
        self.display_feed = display_feed
        self.proper_face_area = None

    def calibrate(self):
        start = time.time()
        face_areas = []
        while True:
            if time.time() - start > self.calibration_time:
                break
            
            ret, frame = self.video_capture.read()
            max_area_face = self.process_frame(frame)
            
            if max_area_face is None:
                print("Could not recognize a face")
                continue

            x, y, w, h = max_area_face
            area = w * h
            face_areas.append(area)

        self.proper_face_area = sum(face_areas) / len(face_areas)

    def process_frame(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray)
        max_area_face = PostureTracker.find_max_area_face(faces)

        return max_area_face    

    def is_posture_changed(self, current_face):
        if self.proper_face_area is None:
            raise ValueError("Cannot track posture unless the tracker is calibrated. ")

        x, y, w, h = current_face
        current_face_area = w * h
        return abs(self.proper_face_area - current_face_area) > 0.2 * self.proper_face_area

    def track(self):
        while True:
            ret, frame = self.video_capture.read()
            max_area_face = self.process_frame(frame)
            
            if max_area_face is None:
                print("Could not recognize a face")
                continue

            if self.display_feed:
                # Draw a rectangle around the faces
                PostureTracker.draw_face_rectangle(max_area_face, frame)
                
                # Display the resulting frame
                cv2.imshow('Video', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            if self.is_posture_changed(max_area_face):
                os.system("say 'Fix your posture!'")
            else:
                os.system("say 'Keep up the good work!'")

            time.sleep(self.check_periodicity)


        # When everything is done, release the capture
        video_capture.release()
        cv2.destroyAllWindows()

    @staticmethod
    def draw_face_rectangle(face, frame):
        x, y, w, h = face
        top_left_corner = (x, y)
        bottom_right_corner = (x+w, y+h)
        color = (0, 255, 0)
        width = 5
        area = w * h
        print(f"Face area: {area}")
        cv2.rectangle(frame, top_left_corner, bottom_right_corner, color, width)

    @staticmethod
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
