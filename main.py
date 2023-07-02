import sys
from botz.hello.index import call as call_hello

# TODO: Add the bot name -> call bot entry when new botz are added
botzNameRunMap = {
    "hello": call_hello,
}

allBotz = ", ".join(list(botzNameRunMap.keys()))

botzName = sys.argv[1]

if __name__ == "__main__":
    if botzNameRunMap.get(botzName):
        botzNameRunMap[botzName]()
    else:
        print(f"Unknown botz: {botzName}. Valid botz are: {allBotz}")
