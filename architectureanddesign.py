import json

print("Started Reading JSON file")
with open("sample-json.json", "r") as read_file:
	print("Converting JSON encoded data into Python dictionary")
	developer = json.load(read_file)

	print("Decoded JSON Data From File")

	for d in developer:
		for key, value in d.items():
			dev = (d.get('taggable image', {}))
		y = ([sub['points'] for sub in dev])
import matplotlib.pyplot as plt

for points in [y]:
	plt.plot(*zip(*(points + points[:1])), marker = 'o')

	automin, automax = plt.xlim()
	plt.xlim(automin - 0.5, automax + 0.5)
	automin, automax = plt.ylim()
	plt.ylim(automin - 0.5, automax + 0.5)

	plt.show()
print("Done reading json file")
