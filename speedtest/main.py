import speedtest as st

# Set best server
server = st.Speedtest()
server.get_best_server()

# Test download speed
down = server.download()
down = down / 1000000
print(f"Download speed: {down} Mb/s")

# Test upload speed
up = server.upload()
up = up / 1000000
print(f"Upload speed: {up} Mb/s")

# Test ping
ping = server.results.ping
print(f"Ping speed: {ping}")