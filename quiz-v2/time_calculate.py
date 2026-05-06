import time

class QuizTimer:
    def __init__(self):
        self.start_time = None
        self.running = False

    def start(self):
# start the countdown
        self.start_time = time.time()
        self.running = True

    def stop(self):
# stop the countdown
        self.running = False

    def get_elapsed_time(self):
# calculate total time
        if self.start_time is None:
            return 0
        return int(time.time() - self.start_time)