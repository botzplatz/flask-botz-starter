import sys
from botz.hello.index import call as call_hello

# TODO: Add the bot name -> call bot entry when new botz are added
botz_call_map = {
    "hello": call_hello,
}

all_botz = ", ".join(list(botz_call_map.keys()))

bot_name = sys.argv[1]

if __name__ == "__main__":
    if botz_call_map.get(bot_name):
        botz_call_map[bot_name]()
    else:
        print(f"Unknown botz: {bot_name}. Valid botz are: {all_botz}")
