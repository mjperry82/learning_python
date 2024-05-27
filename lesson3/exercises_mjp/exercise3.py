import time

start_time = time.time()

while time.time() - 5 <= start_time:
    time.sleep(1)
else:
    print("While loop exited.")


