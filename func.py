from . import list
from . import linker
def check(word):
    if word not in list.badword:
        return False
    else:
        if word in list.whitelist:
            return False
        else:
            return True

def add_b(word):
    if word not in list.badword:
        if linker.send_admin(word):
            return True
        else:
            print("Error")