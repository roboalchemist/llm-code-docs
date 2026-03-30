# Source: https://devdocs.io/gnu_make/automatic-prerequisites

Title: Generating Prerequisites Automatically — DevDocs

URL Source: https://devdocs.io/gnu_make/automatic-prerequisites

Markdown Content:
In the makefile for a program, many of the rules you need to write often say only that some object file depends on some header file. For example, if main.c uses defs.h via an `#include`, you would write:

main.o: defs.h

You need this rule so that `make` knows that it must remake main.o whenever defs.h changes. You can see that for a large program you would have to write dozens of such rules in your makefile. And, you must always be very careful to update the makefile every time you add or remove an `#include`.

To avoid this hassle, most modern C compilers can write these rules for you, by looking at the `#include` lines in the source files. Usually this is done with the ‘-M’ option to the compiler. For example, the command:

cc -M main.c

generates the output:

main.o : main.c defs.h

Thus you no longer have to write all those rules yourself. The compiler will do it for you.

Note that such a rule constitutes mentioning main.o in a makefile, so it can never be considered an intermediate file by implicit rule search. This means that `make` won’t ever remove the file after using it; see [Chains of Implicit Rules](https://devdocs.io/gnu_make/chained-rules).

With old `make` programs, it was traditional practice to use this compiler feature to generate prerequisites on demand with a command like ‘make depend’. That command would create a file depend containing all the automatically-generated prerequisites; then the makefile could use `include` to read them in (see [Include](https://devdocs.io/gnu_make/include)).

In GNU `make`, the feature of remaking makefiles makes this practice obsolete—you need never tell `make` explicitly to regenerate the prerequisites, because it always regenerates any makefile that is out of date. See [Remaking Makefiles](https://devdocs.io/gnu_make/remaking-makefiles).

The practice we recommend for automatic prerequisite generation is to have one makefile corresponding to each source file. For each source file name.c there is a makefile name.d which lists what files the object file name.o depends on. That way only the source files that have changed need to be rescanned to produce the new prerequisites.

Here is the pattern rule to generate a file of prerequisites (i.e., a makefile) called name.d from a C source file called name.c:

%.d: %.c
        @set -e; rm -f $@; \
         $(CC) -M $(CPPFLAGS) $< > $@.$$$$; \
         sed 's,\($*\)\.o[ :]*,\1.o $@ : ,g' < $@.$$$$ > $@; \
         rm -f $@.$$$$

See [Pattern Rules](https://devdocs.io/gnu_make/pattern-rules), for information on defining pattern rules. The ‘-e’ flag to the shell causes it to exit immediately if the `$(CC)` command (or any other command) fails (exits with a nonzero status).

With the GNU C compiler, you may wish to use the ‘-MM’ flag instead of ‘-M’. This omits prerequisites on system header files. See [Options Controlling the Preprocessor](https://gcc.gnu.org/onlinedocs/gcc/Preprocessor-Options.html#Preprocessor-Options) in Using GNU CC, for details.

The purpose of the `sed` command is to translate (for example):

main.o : main.c defs.h

into:

main.o main.d : main.c defs.h

This makes each ‘.d’ file depend on all the source and header files that the corresponding ‘.o’ file depends on. `make` then knows it must regenerate the prerequisites whenever any of the source or header files changes.

Once you’ve defined the rule to remake the ‘.d’ files, you then use the `include` directive to read them all in. See [Include](https://devdocs.io/gnu_make/include). For example:

sources = foo.c bar.c

include $(sources:.c=.d)

(This example uses a substitution variable reference to translate the list of source files ‘foo.c bar.c’ into a list of prerequisite makefiles, ‘foo.d bar.d’. See [Substitution Refs](https://devdocs.io/gnu_make/substitution-refs), for full information on substitution references.) Since the ‘.d’ files are makefiles like any others, `make` will remake them as necessary with no further work from you. See [Remaking Makefiles](https://devdocs.io/gnu_make/remaking-makefiles).

Note that the ‘.d’ files contain target definitions; you should be sure to place the `include` directive _after_ the first, default goal in your makefiles or run the risk of having a random object file become the default goal. See [How Make Works](https://devdocs.io/gnu_make/how-make-works).

Copyright © 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022 Free Software Foundation, Inc. 

Licensed under the GNU Free Documentation License.

[https://www.gnu.org/software/make/manual/html_node/Automatic-Prerequisites.html](https://www.gnu.org/software/make/manual/html_node/Automatic-Prerequisites.html)
