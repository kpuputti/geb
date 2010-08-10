CC=gcc
CFLAGS=-std=c99 -g -pedantic -Wall -Wextra

quine: quine.c
	$(CC) -o quine $(CFLAGS) quine.c

clean:
	rm -f *~ quine
