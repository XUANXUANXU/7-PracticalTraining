import time

def run_sing():
    while True:
        action = '我在唱歌'
        print(action)
        yield
        # time.sleep(5)
        
def run_dance():
    while True:
        action = '我在跳舞'
        print(action)
        yield
        # time.sleep(5)


if __name__ == '__main__':
    sing =  run_sing()
    dance = run_dance()

    while True:
        next(sing)
        next(dance)

    # next(sing)
    # next(dance)
    # next(sing)
    # next(dance)
    # next(sing)
    # next(dance)
    # next(sing)
    # next(dance)



    
