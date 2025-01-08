https = "https"
url = b''
url = [42, 6, 68, 64, 7]
bytes_https = https.encode()
xored = b''
for i in range(len(bytes_https)):
    xored += (int(bytes_https[i]) ^ url[i]).to_bytes()

print(xored.decode())
