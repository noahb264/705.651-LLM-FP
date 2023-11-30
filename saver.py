import os
import datetime
from render import display_level_with_labels
import imageio
import glob
import time
import matplotlib.pyplot as plt

class Saver():

    base_path = None
    i = None
    start_time = None

    def __init__(self):
        self.i = 0
        self.start_time = time.time()

        timestamp = datetime.datetime.today().strftime('%Y-%m-%d %H-%M-%S')
        dir_name = f"run_{timestamp}"
        base_path = "./runs/" + dir_name
        self.base_path = base_path

        if not os.path.exists(base_path):
            os.mkdir(base_path)

        print()
        
    def update(self, current_lvl):
        plt_fig = display_level_with_labels(current_lvl)
        plt_fig.axes[0].set_title(f"Iteration {self.i:03}")
        plt_fig.savefig(f"{self.base_path}/{self.i:03}.jpg")
        plt.close(plt_fig)

        elapsed_time = round(time.time() - self.start_time, 2)
        print(f"Current iteration: {self.i} | Time elapsed: {elapsed_time}", end="\r")
        self.i += 1

    def finalize(self, final_state):
        print()
        with imageio.get_writer(f"{self.base_path}/final.gif", mode='I', fps=1) as writer:
            for filename in sorted(glob.glob(f"{self.base_path}/*.jpg")):
                image = imageio.imread(filename)
                writer.append_data(image)

        with open(f"{self.base_path}/report.txt", "w") as f:
            f.write(f"Total iterations: {self.i}\n")
            f.write(f"Total time: {round(time.time() - self.start_time, 2)}\n")
            f.write(f"Success? {'G' not in final_state}")
