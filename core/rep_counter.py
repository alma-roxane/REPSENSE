THRESHOLDS = {
    'bicep_curl': {
        'down': 160,  # arm straight
        'up':   50,   # arm curled
    },
    'squat': {
        'down': 160,  # legs straight
        'up':   90,   # legs bent
    },
    'pushup': {
        'down': 160,  # arms straight
        'up':   90,   # arms bent
    },
}


class RepCounter:
    def __init__(self, exercise):
        self.exercise = exercise
        self.rep_count = 0
        self.state = 'waiting'
        
    def count(self, angle):
        if angle is None:
            return self.rep_count

        threshold_down = THRESHOLDS[self.exercise]['down']
        threshold_up = THRESHOLDS[self.exercise]['up']

        if self.state == 'waiting':
            if angle > threshold_down:
                self.state = 'down'

        elif self.state == 'down':
            if angle < threshold_up:
                self.state = 'up'

        elif self.state == 'up':
            if angle > threshold_down:
                self.state = 'down'
                self.rep_count += 1

        return self.rep_count
    
    def reset(self):
        self.rep_count = 0
        self.state = 'waiting'

    def get_state(self):
        return self.state