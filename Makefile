LD = -lopendmarc
CC = -I/usr/include/opendmarc
PROJECT = dmarc2csv

.PHONY = all $(PROJECT) clean

all: $(PROJECT)

$(PROJECT): $(PROJECT).c
	gcc -o $@ $< $(CC) $(LD)

clean: 
	rm $(PROJECT)
