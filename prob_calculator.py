import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.contents = []
    for k, v in kwargs.items():
      self.contents += v * [k]

  def draw(self, num):
    balls_list = []
    
    if num > len(self.contents):
      balls_list = copy.deepcopy(self.contents)
    
    else:
      while (num > 0):
        balls = random.randint(0, len(self.contents) - 1)
        balls_list.append(self.contents[balls])
        self.contents.remove(self.contents[balls])
        num -= 1

    return balls_list
    

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  M = 0
  for i in range(num_experiments):
    hat_copy = copy.deepcopy(hat)
    balls = hat_copy.draw
    balls_list = balls(num_balls_drawn)

    eb_list = []
    for k, v in expected_balls.items():
      eb_list += v * [k]

    if contains_balls(eb_list, balls_list):
      M += 1

  probability = M / num_experiments

  return probability


def contains_balls(expected_balls, actual_balls):
  for item in expected_balls:
    if item in actual_balls:
      actual_balls.remove(item)
    else:
      return False
  return True
