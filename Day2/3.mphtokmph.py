def mphtokmph(mphspeed):
    kmph = mphspeed * 1.60934
    return kmph


def main():
    mphspeed = float(input("Enter your speed in MPH: "))
    kmph = mphtokmph(mphspeed)
    print("You are travelling at:", kmph,"Kmph")

main()