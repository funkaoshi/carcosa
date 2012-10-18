all: deploy

deploy:
	rsync -avz --exclude=Makefile --exclude=.git --exclude=*.swp --exclude=*.pyc --exclude=README.md /Users/ramanan/Sites/carcosa/ funkaoshi.com:/home/ramanan/carcosa.totalpartykill.ca/
	ssh funkaoshi.com 'touch carcosa.totalpartykill.ca/tmp/restart.txt'

clean:
	rm *.pyc


