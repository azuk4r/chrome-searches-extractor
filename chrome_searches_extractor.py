from re import sub, split, findall
from urllib.parse import unquote
from os.path import expanduser

user = expanduser('~')
path = user + r'\AppData\Local\Google\Chrome\User Data\Default\Favicons'
with open(path, 'rb') as file:
	content = file.read()
content_str = content.decode('utf-8', errors='ignore')
filtered_content = findall(r'http[s]?://[^\s]+', content_str)
for url in filtered_content:
	clean_url = unquote(url)
	cleaned_url = sub(r'[^a-zA-Z0-9\s,?&=:/._+-]', '', clean_url).strip()  
	possible_urls = split(r'(http[s]?://)', cleaned_url)
	for i in range(1, len(possible_urls), 2):
		final_url = possible_urls[i] + possible_urls[i + 1]
		print(final_url)
# by azuk4r
