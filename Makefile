all: deploy

deploy:
	rsync -avz --exclude=Makefile --exclude=.git --exclude=*.swp --exclude=*.pyc --exclude=README.md /Users/rsivaranjan/Documents/Code/carcosa/ ramanan@funkaoshi.com:/home/ramanan/carcosa.totalpartykill.ca/
	ssh ramanan@funkaoshi.com 'touch carcosa.totalpartykill.ca/tmp/restart.txt'

clean:
	rm *.pyc


