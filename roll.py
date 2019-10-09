import random, sys, keyboard
# pip install keyboard

def roll(rolls, sides):
    total = 0
    message = ""
    values = [None] * rolls
    for i in range(rolls):
        values[i] = random.randint(1, sides)
        natCheck = lambda x: "nat 20" if x == 20 else x
        message += f"Die {i+1} ({natCheck(values[i])}) "
        total += values[i]

    return total, message

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("usage:")
        print("    python roll.py [number of rolls] [sides of dice]")
        exit()
    while True:
        total, message = roll(int(sys.argv[1]), int(sys.argv[2]))
        print(f"You: {message} \n    Total Score: {total}")

        totalCPU, messageCPU = roll(int(sys.argv[1]), int(sys.argv[2]))
        print(f"Opponent: {messageCPU} \n    Total Score: {totalCPU}")

        if total > totalCPU:
            print("\nYou Win!")
        elif total < totalCPU:
            print("\nYou Loss!")
        else:
            print("\nDraw better luck next time")

        print("\nPlay again? Press space to continue. Press any key to stop...\n")
        if keyboard.read_hotkey() == 'space':
            continue
        print("Thanks for playing!")
        exit()
            
            
