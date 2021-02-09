class Clock:

    def __init__(self, hour, minute):
        self.hour, self.minute = self._fix_time(hour, minute)

    def __repr__(self):
        hour, minute = str(self.hour), str(self.minute)
        if len(hour) < 2:
            hour = '0' + hour
        if len(minute) < 2:
            minute = '0' + minute            

        return hour + ':' + minute
        
    def __eq__(self, other):
        return self.hour == other.hour and self.minute == other.minute

    def __add__(self, minutes):
        return Clock(self.hour, self.minute + minutes)

    def __sub__(self, minutes):
        return Clock(self.hour, self.minute - minutes)
    
    def _fix_time(self, hour, minute):
        hour += minute//60
        minute = minute % 60
        hour %= 24
        return hour, minute
