while True:
    try:
        a=int(input("What's your age?\n"))
        print(a)
        break
    except ValueError:
        print("Please enter a number")
    except:
        break
    finally:
        print("I am getting Interest")