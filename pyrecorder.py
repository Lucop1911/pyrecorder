import cv2
import numpy as np
import mss
import time

filename = "record.mp4"
record_seconds = 10
fps = 20.0

with mss.mss() as sct:
    monitor = sct.monitors[1]
    width, height = monitor["width"], monitor["height"]

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(filename, fourcc, fps, (width, height))

    print(f"Recording {record_seconds}s of screen to {filename}...")
    start_time = time.time()

    while (time.time() - start_time) < record_seconds:
        frame = np.array(sct.grab(monitor))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
        out.write(frame)
        time.sleep(1 / fps)

    out.release()
    print("Done. Saved to", filename)
