
f = open("AppData.yaml", "a")
f.close()

close = False

def appData():
    while close == False:
        f = open("AppData.yaml", "r")
        if close.find("close = True") > -1:
            close = True
            return close
        f.close()
