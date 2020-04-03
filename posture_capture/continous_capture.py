import cv2
import argparse
import time

def capture(posture_status):
    # f = 1/T. Write an image every 1 second
    write_period = 1
    
    # acquire webcam
    cam = cv2.VideoCapture(0)
    
    num_images = 0

    start = time.time()

    while True:
        is_succesful_read, frame = cam.read()
                
        cv2.imshow("test", frame)

        keystroke = cv2.waitKey(1)

        if keystroke % 256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break

        if time.time() - start < write_period:
            continue

        start = time.time()
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
