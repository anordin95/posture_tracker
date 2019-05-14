from posture_tracker import PostureTracker
from performance_tracker import PerformanceTracker

calibration_time = 2
check_periodicity = 10
positive_reinforcement_periodicity = 300
display_feed = False
face_model_filepath = 'models/face_model.xml'

storage_filename = 'historical_performance.json'
performance_tracker = PerformanceTracker(storage_filename)

posture_tracker = PostureTracker(face_model_filepath,
						calibration_time,
						check_periodicity,
						positive_reinforcement_periodicity,
						display_feed,
						performance_tracker)



print("\nTracker calibrating...")
posture_tracker.calibrate()
print("\nTracker calibrated!")

print("\nTracking posture...")
posture_tracker.track()