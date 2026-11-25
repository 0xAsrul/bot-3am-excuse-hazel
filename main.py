#!/usr/bin/env python3
"""Off the Clock - a hardware wallet's 3 AM excuse.

make.fun competition: The 3 AM Excuse
(u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)
"""

import os

LINE = "3 AM? My secure element is asleep, my screen is dark - your 'urgent' swap can wait for sunrise."


def main():
    print(LINE)
    try:
        os.makedirs("/output", exist_ok=True)
        with open("/output/entry.txt", "w", encoding="utf-8") as f:
            f.write(LINE + "\n")
    except OSError:
        pass


if __name__ == "__main__":
    main()
