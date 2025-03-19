import pywhatkit as kit
import time

# Define recipient numbers
numbers = ["+237678931432"]

# Define the message
message = "Hello! This is an automated message from Python."

# Send messages one by one
for number in numbers:
    kit.sendwhatmsg_instantly(number, message, wait_time=15)
    time.sleep(10)  # Pause to avoid spam detection

print("Messages sent successfully!")
