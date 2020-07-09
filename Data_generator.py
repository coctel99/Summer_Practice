import pandas as pd
import numpy as np
import random
import csv

objects = ['0.0', '1.0', '2.0', '3.0', '6.0', '7.0']

with open('dataset2.csv', mode='w', newline='') as data_file:
    data_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    # data_writer.writerow(['Frame', 'Bbox', 'Class', 'Confidence'])

    for i in range(20):
        rand_range_length = random.randint(10, 50)
        frames_range = np.arange(rand_range_length) + int((50 - rand_range_length) * random.uniform(0, 1))
        for j in frames_range:
            frame = j
            x_min = random.uniform(0, 0.6)
            y_min = random.uniform(0, 0.6)
            x_max = x_min + random.uniform(0.1, 0.4)
            y_max = y_min + random.uniform(0.1, 0.4)
            confidence = random.uniform(0.7, 1)
            frame_load_time = random.uniform(0, 1) + random.randint(1, 4)

            data_writer.writerow([frame, [x_min, y_min, x_max, y_max], random.choice(objects), confidence, frame_load_time])
