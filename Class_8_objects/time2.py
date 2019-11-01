# Time2.py
#
# Rewrite the "__str__" method used to print the time.the routines 
# that Downey provides that would have to change to keep hours less than 24
# Usage:
#      % python Time2.py 
#
# Himanshu Mohan, Oct 29, 2019
"""

Code example from Think Python, by Allen B. Downey.
Available from http://thinkpython.com

Copyright 2012 Allen B. Downey.
Distributed under the GNU General Public License at gnu.org/licenses/gpl.html.

"""

class Time(object):
    """Represents the time of day.
       
    attributes: hour, minute, second
    """
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        if self.hour>12 :
            return '%.2d:%.2d' ' PM' % (self.hour-12, self.minute)
        elif self.hour==12:
            return '%.2d:%.2d' ' PM' % (self.hour, self.minute)
        else:
            return '%.2d:%.2d' ' AM' % (self.hour, self.minute)
        

    def print_time(self):
        print(str(self))

    def time_to_int(self):
        """Computes the number of seconds since midnight."""
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def is_after(self, other):
        """Returns True if t1 is after t2; false otherwise."""
        return self.time_to_int() > other.time_to_int()

    def __add__(self, other):
        """Adds two Time objects or a Time object and a number.

        other: Time object or number of seconds
        """
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)

    def __radd__(self, other):
        """Adds two Time objects or a Time object and a number."""
        return self.__add__(other)

    def add_time(self, other):
        """Adds two time objects."""
        assert self.is_valid() and other.is_valid()
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)

    def increment(self, seconds):
        """Returns a new Time that is the sum of this time and seconds."""
        seconds += self.time_to_int()
        return int_to_time(seconds)

    def is_valid(self):
        """Checks whether a Time object satisfies the invariants."""
        if self.hour < 0 or self.minute < 0 or self.second < 0:
            return False
        if self.minute >= 60 or self.second >= 60:
            return False
        return True


def int_to_time(seconds):
    """Makes a new Time object.

    seconds: int seconds since midnight.
    """
    minutes, second = divmod(seconds, 60)
    hour, minute = divmod(minutes, 60)
    hour_d, hour_m=divmod(hour, 24)
        
    time = Time(hour_m, minute, second)
    return time


def main():
    
    start = Time(49, 70, 80)
    sec= start.time_to_int()
    final=int_to_time(sec)
    final.print_time()

if __name__ == '__main__':
    main()