import pyshorteners

# Get the long URL from the user
long_url = input("Enter a long URL: ")

# Shorten the URL using pyshorteners
s = pyshorteners.Shortener()
short_url = s.tinyurl.short(long_url)

print(short_url)