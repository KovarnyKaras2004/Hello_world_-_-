f = open("output.txt", "w", encoding="utf-8")
print("kokkdasksaksdakfgdkgfd", file=f)
f = open("output.txt", "r", encoding="utf-8")
s = f.read()
print(s)

