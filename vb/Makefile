
install:
	sudo apt update && sudo apt install python3 python3-pip python3-venv -y
	pip3 install -U pip
	pip3 install setuptools
	pip3 install -r requirements.txt

run:
	cd vb && python3 -m vb

test:
	python3 -m pytest