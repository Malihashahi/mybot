import requests as req

soal=input("soal:")

out = req.get("http://5.161.91.18/chat?text="+soal)
print(out.json())
