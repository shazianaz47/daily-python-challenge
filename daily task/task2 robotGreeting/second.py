import time


def robot_greeting():
    name=input(" Enter your name:")
    print("/n processing...")
    time.sleep(1) 
    print(f"Name detected: {name}")
    time.sleep(1)
    print(f" Aceess granted! welcome,Agent {name}.Your mission awaits!")
robot_greeting()
