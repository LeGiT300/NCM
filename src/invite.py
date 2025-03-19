import pywhatkit as kit
import time

numbers = ["+237678931432"]

message = "https://docs.expo.dev/router/advanced/stack/"

try:
    for number in numbers:
        kit.sendwhatmsg_instantly(number, message, wait_time=15)
        time.sleep(10)

    print("Messages sent successfully!")

except Exception as e:
    print('Error{}'.format(e))