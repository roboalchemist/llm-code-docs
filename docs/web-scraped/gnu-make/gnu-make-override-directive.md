# Source: https://devdocs.io/gnu_make/override-directive

Title: The override Directive — DevDocs

URL Source: https://devdocs.io/gnu_make/override-directive

Markdown Content:
If a variable has been set with a command argument (see [Overriding Variables](https://devdocs.io/gnu_make/overriding)), then ordinary assignments in the makefile are ignored. If you want to set the variable in the makefile even though it was set with a command argument, you can use an `override` directive, which is a line that looks like this:

override variable = value

or

override variable := value

To append more text to a variable defined on the command line, use:

override variable += more text

See [Appending More Text to Variables](https://devdocs.io/gnu_make/appending).

Variable assignments marked with the `override` flag have a higher priority than all other assignments, except another `override`. Subsequent assignments or appends to this variable which are not marked `override` will be ignored.

The `override` directive was not invented for escalation in the war between makefiles and command arguments. It was invented so you can alter and add to values that the user specifies with command arguments.

For example, suppose you always want the ‘-g’ switch when you run the C compiler, but you would like to allow the user to specify the other switches with a command argument just as usual. You could use this `override` directive:

override CFLAGS += -g

You can also use `override` directives with `define` directives. This is done as you might expect:

override define foo =
bar
endef

See [Defining Multi-Line Variables](https://devdocs.io/gnu_make/multi_002dline).

Copyright © 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022 Free Software Foundation, Inc. 

Licensed under the GNU Free Documentation License.

[https://www.gnu.org/software/make/manual/html_node/Override-Directive.html](https://www.gnu.org/software/make/manual/html_node/Override-Directive.html)
