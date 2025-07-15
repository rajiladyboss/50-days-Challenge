import time

print("Countdown starts!")

for i in range(10, -1, -1):
    print(i)
    time.sleep(1)  # waits for 1 second before printing next number

print("Countdown finished! 🚀")
