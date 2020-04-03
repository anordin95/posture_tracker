import cv2
import argparse

def capture(posture_status):
    
    # acquire webcam
    cam = cv2.VideoCapture(0)

    num_images = 0

    while True:
        is_succesful_read, frame = cam.read()
        
        cv2.imshow("test", frame)
        
        if not is_succesful_read:
            break
        
        keystroke = cv2.waitKey(1)

        if keystroke % 256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        
        elif keystroke % 256 == 32:
            # SPACE pressed
            filename = f"{posture_status}_{num_images}.png"
            cv2.imwrite(filename, frame)
            print(f"{filename} written!")
            num_images += 1
    
    cam.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('posture_status', help="recordings are for good or bad posture?")
    args = parser.parse_args()
    posture_status = args.posture_status

    capture(posture_status)
