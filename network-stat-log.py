#!/usr/bin/python3
import os
import signal
import argparse
import subprocess
from datetime import datetime, timedelta

import pandas as pd
import matplotlib.pyplot as plt

############################### PARSER ################################

parser = argparse.ArgumentParser(
        prog="Network Statistics Logger and Visualizer",
        description= "Men-log statistik jaringan dan membuat plot",
    )
parser.add_argument(
        '--plot_title',
        help="Judul Plot",
    )
args = parser.parse_args()

############################## KONSTANTA ##############################

# Overhead 2 detik
CURRENT_TIME    = (datetime.now() + timedelta(seconds=2)).strftime("%H-%M-%S")
CURRENT_DIR     = os.path.dirname(os.path.realpath(__file__))
OUTPUT_FOLDER   = "output"
LOG_OUTPUT      = f"{OUTPUT_FOLDER}/{CURRENT_TIME}/log.txt"
FIG_OUTPUT      = f"{OUTPUT_FOLDER}/{CURRENT_TIME}/fig.png"

SCRIPT_NAME     = "network-stat-log.sh"
NET_INTERFACE   = "eth0"

############################### SCRIPT ################################
# Pastikan folder ada
os.makedirs(f"{OUTPUT_FOLDER}/{CURRENT_TIME}", exist_ok=True)
# Jalanin Script
P1 = subprocess.Popen(
        ["./" + SCRIPT_NAME, NET_INTERFACE, LOG_OUTPUT], 
        cwd=CURRENT_DIR, 
        stdin=subprocess.PIPE
    )
# Bunuh Script kalau ada SIGINT / CTRL-C
signal.signal(signal.SIGINT, lambda *_: P1.send_signal(signal.SIGINT))
# Blocking
P1.wait()

############################## PLOTTING ###############################
# Baca Hasil
df = pd.read_csv(
        LOG_OUTPUT, 
        delim_whitespace=True
    )

fig, ax = plt.subplots()
cols_idx = [
        (4, "Download Speed"),
        (5, "Upload Speed")
    ]
for col_idx, col_name in cols_idx:
    print(f"Plotting {col_name}...")
    ax.plot(df.index, df.iloc[:, col_idx], label=col_name)

if args.plot_title is not None:
    ax.set_title(args.plot_title)
ax.legend(loc="upper right")
ax.set_xlim(left=0)
ax.set_ylim(bottom=0)
ax.set_xlabel("Time (second)")
ax.set_ylabel(f"Speed ({df.columns[cols_idx[0][0]][2:]})")

fig.savefig(FIG_OUTPUT)
print(f"Plot saved at {FIG_OUTPUT}")
