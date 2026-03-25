# Source: https://devdocs.io/gnu_make/canned-recipes

Title: Defining Canned Recipes — DevDocs

URL Source: https://devdocs.io/gnu_make/canned-recipes

Markdown Content:
When the same sequence of commands is useful in making various targets, you can define it as a canned sequence with the `define` directive, and refer to the canned sequence from the recipes for those targets. The canned sequence is actually a variable, so the name must not conflict with other variable names.

Here is an example of defining a canned recipe:

define run-yacc =
yacc $(firstword $^)
mv y.tab.c $@
endef

Here `run-yacc` is the name of the variable being defined; `endef` marks the end of the definition; the lines in between are the commands. The `define` directive does not expand variable references and function calls in the canned sequence; the ‘$’ characters, parentheses, variable names, and so on, all become part of the value of the variable you are defining. See [Defining Multi-Line Variables](https://devdocs.io/gnu_make/multi_002dline), for a complete explanation of `define`.

The first command in this example runs Yacc on the first prerequisite of whichever rule uses the canned sequence. The output file from Yacc is always named y.tab.c. The second command moves the output to the rule’s target file name.

To use the canned sequence, substitute the variable into the recipe of a rule. You can substitute it like any other variable (see [Basics of Variable References](https://devdocs.io/gnu_make/reference)). Because variables defined by `define` are recursively expanded variables, all the variable references you wrote inside the `define` are expanded now. For example:

foo.c : foo.y
        $(run-yacc)

‘foo.y’ will be substituted for the variable ‘$^’ when it occurs in `run-yacc`’s value, and ‘foo.c’ for ‘$@’.

This is a realistic example, but this particular one is not needed in practice because `make` has an implicit rule to figure out these commands based on the file names involved (see [Using Implicit Rules](https://devdocs.io/gnu_make/implicit-rules)).

In recipe execution, each line of a canned sequence is treated just as if the line appeared on its own in the rule, preceded by a tab. In particular, `make` invokes a separate sub-shell for each line. You can use the special prefix characters that affect command lines (‘@’, ‘-’, and ‘+’) on each line of a canned sequence. See [Writing Recipes in Rules](https://devdocs.io/gnu_make/recipes). For example, using this canned sequence:

define frobnicate =
@echo "frobnicating target $@"
frob-step-1 $< -o $@-step-1
frob-step-2 $@-step-1 -o $@
endef

`make` will not echo the first line, the `echo` command. But it _will_ echo the following two recipe lines.

On the other hand, prefix characters on the recipe line that refers to a canned sequence apply to every line in the sequence. So the rule:

frob.out: frob.in
        @$(frobnicate)

does not echo _any_ recipe lines. (See [Recipe Echoing](https://devdocs.io/gnu_make/echoing), for a full explanation of ‘@’.)

Copyright © 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022 Free Software Foundation, Inc. 

Licensed under the GNU Free Documentation License.

[https://www.gnu.org/software/make/manual/html_node/Canned-Recipes.html](https://www.gnu.org/software/make/manual/html_node/Canned-Recipes.html)
