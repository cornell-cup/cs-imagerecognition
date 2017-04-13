from R2Protocol import encode, decode

encoded = encode("Pi", "NUC", "12", "33143")
params = decode(encoded)

for key, value in params.items():
	print(key)
	print (value)

