try:
	from googlesearch import search
except ImportError:
	print("Google nie znalazł tego")

query = "siema"

for j in search(query, tld="co.in", num=20, stop=20, pause=2):
	print(j)
