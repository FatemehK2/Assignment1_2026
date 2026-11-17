import numpy as np

def calculate_average(students):
  grades = [student["grade"] for student in students]
  return np.mean(grades)