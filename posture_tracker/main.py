from posture_tracker import PostureTracker

calibration_time = 2
check_periodicity = 10
display_feed = False
face_model_filepath = 'models/face_model.xml'

tracker = PostureTracker(face_model_filepath,
						calibration_time,
						check_periodicity,
						display_feed)

print("\nTracker calibrating...")
tracker.calibrate()
print("\nTracker calibrated!")

print("\nTracking posture...")
tracker.track()