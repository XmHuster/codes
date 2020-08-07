CC=gcc
CFLAGS=-I.
DEPS = add.h multi.h
OBJ = add.o multi.o main.o

%.o: %.c $(DEPS)
	$(CC) -c -o $@ $< $(CFLAGS)

main: $(OBJ)
	$(CC) -o $@ $^ $(CFLAGS)

clean:
	rm *.o main