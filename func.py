from list import badword, whitelist
import linker
def check(word):
    if word not in badword:
        return False
    else:
        if word in whitelist:
            return False
        else:
            return True

def add_b(word):
    if word not in badword:
        if linker.send_admin(word):
            return True
        else:
            print("Error")