#Liliana O'Sullivan 13/02/2021

CC=g++
CFLAGS= -std=c++11 -fopenmp
UNAME := $(shell uname -s)

ALL:
ifeq ($(UNAME) , Linux)
	$(CC) main.cpp $(CFLAGS) -o main
endif
ifeq ($(UNAME),Darwin)
	clang++ -Xpreprocessor -fopenmp -I/usr/local/include -L/usr/local/lib -lomp main.cpp -std=c++11 -o main
endif

DOXY:
	doxygen Doxyfile
