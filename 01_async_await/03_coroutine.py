# coroutine

def grep(pattern: str):
    print("Start grep")
    try:
        while True:
            line = yield
            if pattern in line:
                print(line)
    except GeneratorExit:
        print("Stop grep")

g = grep("python")
next(g) # start coroutine
g.send("Slow python") # send data to the line 7 (yield)
g.send("Fast C++")
g.close() # triggers exception GeneratorExit
