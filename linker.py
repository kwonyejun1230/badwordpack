def send_admin(word):
    try:
        f = open("badwordcheck.txt", "w")
        f.write(f"{word}\n")
        f.close()
        return 1
    except Exception as e:
        return 0