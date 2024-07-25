# 6s red
# 3s green
# 1s orange

import time as t

while True:
    print("------------------------------")
    print("\t Road1 \t Road2")
    print("------------------------------")

    # Red
    red_start_time = t.time()
    print("\t Red \t Green")
    t.sleep(6)

    # Orange
    orange_start_time = t.time()
    print("\t Orange \t Orange")
    t.sleep(1)

    # Green
    green_start_time = t.time()
    print("\t Green \t Red")
    t.sleep(3)
