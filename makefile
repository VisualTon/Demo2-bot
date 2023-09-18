install:
	apt-get install python3.10
	pip3 install --upgrade pip
	pip3 install -r requirements.txt
run:
	python3 channelBot.py