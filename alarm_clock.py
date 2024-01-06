from playsound import playsound
import time

CLEAR = '\033[2J'
CLEAR_AND_RETURN = '\033'

def alarm(seconds):
  time_elapsed = 0

  while time_elapsed < seconds:
    time.sleep(1)
    time_elapsed += 1

    time_left = seconds - time_elapsed
    minutes_left = time_left // 60
    seconds_left = time_left % 60
    
    print(f'{minutes_left:02d}:{seconds_left:02d}')

alarm(10)

