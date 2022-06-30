
install:
	sudo apt update && sudo apt install python3 python3-pip python3-venv -y
	pip3 install setuptools

run:
	cd vb && python3 -m vb