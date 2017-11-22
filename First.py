import urllib
response = urllib.urlopen("http://www.fishc.com")
html = response.read()
print (html)