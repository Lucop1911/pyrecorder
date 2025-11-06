import argparse
import cv2
import numpy as np
import mss
import time

def record_screen(filename: str, duration: int, fps: float):
    with mss.mss() as sct:
        monitor = sct.monitors[1]
        width, height = monitor["width"], monitor["height"]

        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        out = cv2.VideoWriter(filename, fourcc, fps, (width, height))

        print(f"Recording {duration} seconds of screen to '{filename}' at {fps} FPS...")
        start_time = time.time()

        try:
            while (time.time() - start_time) < duration:
                frame = np.array(sct.grab(monitor))
                frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
                out.write(frame)
                time.sleep(1 / fps)
        except KeyboardInterrupt:
            print("\nRecording stopped manually.")
        finally:
            out.release()
            print(f"Saved recording to '{filename}'.")

def main():
    parser = argparse.ArgumentParser(description="Simple screen recorder using OpenCV and MSS.")
    parser.add_argument("duration", type=int, help="Duration of the recording in seconds")
    parser.add_argument(
        "-o", "--output", default="record.mp4", help="Output filename (default: record.mp4)"
    )
    parser.add_argument(
        "-f", "--fps", type=float, default=20.0, help="Frames per second (default: 20)"
    )

    args = parser.parse_args()
    record_screen(args.output, args.duration, args.fps)

if __name__ == "__main__":
    main()
