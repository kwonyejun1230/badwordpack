from . import list

def check(word):
    if word not in list.badword:
        return False
    else:
        if word in list.whitelist:
            return False
        else:
            return True