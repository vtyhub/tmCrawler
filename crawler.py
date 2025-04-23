import requests
from os import path

url = 'https://livenging.alicdn.com/mediaplatform/55e2b9fe-3ee5-4adb-a245-c204ee95b206/'
filepath = path.join(path.expanduser("~"), 'Desktop') + '\\test2.mp4'

def main():
	with open(filepath, 'ab') as f:
		for cur in range(1, 1054):
			# 第1次循环 1-1054
			print(cur)
			currentUrl = url + str(cur) + '.ts'
			response = requests.get(currentUrl)
			# 第1次循环没有404
			f.write(response.content)
		
		for cur in range(10000000, 10003000):
			# 第2次循环 貌似是10000000-10002497
			print(cur)
			currentUrl = url + str(cur) + '.ts'
			response = requests.get(currentUrl)
			# 第2次循环遇到404结束
			if response.status_code == 404:
				break
			f.write(response.content)

if __name__ == '__main__':
	main()