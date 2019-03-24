import urllib.request
import os

extensions = { ".jpg", ".png", ".gif" }

if not os.path.isdir("banners"):
	os.mkdir("banners")

for i in range(0,300):
	for e in extensions:
		ex = str(i) + e
		url = "https://s.4cdn.org/image/title/" + ex
		
		if os.path.isfile("banners/" + ex):
			print("[ERROR]: " + ex + " exists, skipping.")
		else:
			try:
				print("[INFO]: Downloading " + ex)
				urllib.request.urlretrieve(url, "banners/" + ex)
				print("[INFO]: Downloaded " + ex + " successfully.")
			except:
				print("[ERROR]: " + ex + " returned 404, skipping.")
