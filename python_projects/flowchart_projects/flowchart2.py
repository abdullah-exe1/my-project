num = int(input("inter a num"))

while True:
    try:
        if num > 1:
            print("done your num is bigger then 1")
            break

        elif num <= 1:
            num = num + 1
            print("your num incresd by 1")
            print(num)

    except:
        print("num isn't a int")