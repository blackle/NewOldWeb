import cgi, sys

print("Content-Type: text/html")

form = cgi.FieldStorage()
password = form.getvalue('password')

print("\n")

real_password = "1234"
if password == real_password:
	print("password correct!")
	sys.exit()

if len(real_password) != len(password):
	if len(real_password) < len(password):
		print("password is shorter")
	else:
		print("password is longer")
	sys.exit()

corrections = "".join(a if a == b else '.' for a, b in zip(password, real_password))
print(corrections)