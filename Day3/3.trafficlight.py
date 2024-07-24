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
    t.sleep(3)
    # print(t.time() - red_start_time)
    t.sleep(3)
    # print(t.time() - red_start_time)

    # Orange
    orange_start_time = t.time()
    print("\t Orange \t Orange")
    t.sleep(1)
    # print(t.time() - orange_start_time)

    # Green
    green_start_time = t.time()
    print("\t Green \t Red")
    t.sleep(1.5)
    # print(t.time() - green_start_time)
    t.sleep(1.5)
    # print(t.time()-green_start_time)
