PYTHON=python3
LN=ln
LNFLAGS=-s
CHMOD=chmod
PERMS=+x
MAIN=src/main.py
EXECUTABLE=jakeandamir

all:
	$(LN) $(LNFLAGS) $(MAIN) $(EXECUTABLE)
	$(CHMOD) $(PERMS) $(EXECUTABLE)
