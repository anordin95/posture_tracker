import time
import json
import os

class PerformanceTracker:

	def __init__(self, storage_filename):
		self.storage_filename = storage_filename
		self.posture_checkins = {}
		self.last_save_time = time.time()

	def should_save(self):
		cur_time = time.time()
		if cur_time - self.last_save_time > 600:
			self.save()
			self.last_save_time = cur_time

	def bad_posture_checkin(self):
		self.should_save()
		self.posture_checkins[time.time()] = 'bad'

	def good_posture_checkin(self):
		self.should_save()
		self.posture_checkins[time.time()] = 'good'

	def save(self):
		if os.path.isfile(self.storage_filename):
			with open(self.storage_filename, 'r') as f:
				past_posture_info = json.load(f)
		else:
			past_posture_info = {}

		past_posture_info.update(self.posture_checkins)
		
		with open(self.storage_filename, 'w') as f:
			json.dump(past_posture_info, f)