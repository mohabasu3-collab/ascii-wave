import os
import math
import time

chars = " .:-=+*#%@"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def generate_frame(t, width=80, height=24):
    output = ""
    for y in range(height):
        for x in range(width):
            nx = (x - width / 2) / (width / 2)
            ny = (y - height / 2) / (height / 2)
            value = math.sin(10 * (nx**2 + ny**2) - t)
            index = int((value + 1) / 2 * (len(chars) - 1))
            output += chars[index]
        output += "\n"
    return output

def animate(frames=1000, fps=15):
    t = 0
    delay = 1 / fps
    try:
        for _ in range(frames):
            clear()
            frame = generate_frame(t)
            print(frame)
            t += 0.1
            time.sleep(delay)
    except KeyboardInterrupt:
        print("\n[Animación terminada]")

if __name__ == "__main__":
    animate()
