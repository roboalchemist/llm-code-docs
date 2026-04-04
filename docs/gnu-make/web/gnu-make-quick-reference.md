# Source: https://devdocs.io/gnu_make/quick-reference

Title: GNU Make / Quick Reference — DevDocs

URL Source: https://devdocs.io/gnu_make/quick-reference

Markdown Content:
This appendix summarizes the directives, text manipulation functions, and special variables which GNU `make` understands. See [Special Targets](https://devdocs.io/gnu_make/special-targets), [Catalogue of Built-In Rules](https://devdocs.io/gnu_make/catalogue-of-rules), and [Summary of Options](https://devdocs.io/gnu_make/options-summary), for other summaries.

Here is a summary of the directives GNU `make` recognizes:

`define variable``define variable =``define variable :=``define variable ::=``define variable :::=``define variable +=``define variable ?=``endef`
Define multi-line variables. See [Multi-Line](https://devdocs.io/gnu_make/multi_002dline).

`undefine variable`
Undefining variables. See [Undefine Directive](https://devdocs.io/gnu_make/undefine-directive).

`ifdef variable``ifndef variable``ifeq (a,b)``ifeq "a" "b"``ifeq 'a' 'b'``ifneq (a,b)``ifneq "a" "b"``ifneq 'a' 'b'``else``endif`
Conditionally evaluate part of the makefile. See [Conditionals](https://devdocs.io/gnu_make/conditionals).

`include file``-include file``sinclude file`
Include another makefile. See [Including Other Makefiles](https://devdocs.io/gnu_make/include).

`override variable-assignment`
Define a variable, overriding any previous definition, even one from the command line. See [The `override` Directive](https://devdocs.io/gnu_make/override-directive).

`export`
Tell `make` to export all variables to child processes by default. See [Communicating Variables to a Sub-`make`](https://devdocs.io/gnu_make/variables_002frecursion).

`export variable``export variable-assignment``unexport variable`
Tell `make` whether or not to export a particular variable to child processes. See [Communicating Variables to a Sub-`make`](https://devdocs.io/gnu_make/variables_002frecursion).

`private variable-assignment`
Do not allow this variable assignment to be inherited by prerequisites. See [Suppressing Inheritance](https://devdocs.io/gnu_make/suppressing-inheritance).

`vpath pattern path`
Specify a search path for files matching a ‘%’ pattern. See [The `vpath` Directive](https://devdocs.io/gnu_make/selective-search).

`vpath pattern`
Remove all search paths previously specified for pattern.

`vpath`
Remove all search paths previously specified in any `vpath` directive.

Here is a summary of the built-in functions (see [Functions](https://devdocs.io/gnu_make/functions)):

`$(subst from,to,text)`
Replace from with to in text. See [Functions for String Substitution and Analysis](https://devdocs.io/gnu_make/text-functions).

`$(patsubst pattern,replacement,text)`
Replace words matching pattern with replacement in text. See [Functions for String Substitution and Analysis](https://devdocs.io/gnu_make/text-functions).

`$(strip string)`
Remove excess whitespace characters from string. See [Functions for String Substitution and Analysis](https://devdocs.io/gnu_make/text-functions).

`$(findstring find,text)`
Locate find in text. See [Functions for String Substitution and Analysis](https://devdocs.io/gnu_make/text-functions).

`$(filter pattern…,text)`
Select words in text that match one of the pattern words. See [Functions for String Substitution and Analysis](https://devdocs.io/gnu_make/text-functions).

`$(filter-out pattern…,text)`
Select words in text that _do not_ match any of the pattern words. See [Functions for String Substitution and Analysis](https://devdocs.io/gnu_make/text-functions).

`$(sort list)`
Sort the words in list lexicographically, removing duplicates. See [Functions for String Substitution and Analysis](https://devdocs.io/gnu_make/text-functions).

`$(word n,text)`
Extract the n th word (one-origin) of text. See [Functions for String Substitution and Analysis](https://devdocs.io/gnu_make/text-functions).

`$(words text)`
Count the number of words in text. See [Functions for String Substitution and Analysis](https://devdocs.io/gnu_make/text-functions).

`$(wordlist s,e,text)`
Returns the list of words in text from s to e. See [Functions for String Substitution and Analysis](https://devdocs.io/gnu_make/text-functions).

`$(firstword names…)`
Extract the first word of names. See [Functions for String Substitution and Analysis](https://devdocs.io/gnu_make/text-functions).

`$(lastword names…)`
Extract the last word of names. See [Functions for String Substitution and Analysis](https://devdocs.io/gnu_make/text-functions).

`$(dir names…)`
Extract the directory part of each file name. See [Functions for File Names](https://devdocs.io/gnu_make/file-name-functions).

`$(notdir names…)`
Extract the non-directory part of each file name. See [Functions for File Names](https://devdocs.io/gnu_make/file-name-functions).

`$(suffix names…)`
Extract the suffix (the last ‘.’ and following characters) of each file name. See [Functions for File Names](https://devdocs.io/gnu_make/file-name-functions).

`$(basename names…)`
Extract the base name (name without suffix) of each file name. See [Functions for File Names](https://devdocs.io/gnu_make/file-name-functions).

`$(addsuffix suffix,names…)`
Append suffix to each word in names. See [Functions for File Names](https://devdocs.io/gnu_make/file-name-functions).

`$(addprefix prefix,names…)`
Prepend prefix to each word in names. See [Functions for File Names](https://devdocs.io/gnu_make/file-name-functions).

`$(join list1,list2)`
Join two parallel lists of words. See [Functions for File Names](https://devdocs.io/gnu_make/file-name-functions).

`$(wildcard pattern…)`
Find file names matching a shell file name pattern (_not_ a ‘%’ pattern). See [The Function `wildcard`](https://devdocs.io/gnu_make/wildcard-function).

`$(realpath names…)`
For each file name in names, expand to an absolute name that does not contain any `.`, `..`, nor symlinks. See [Functions for File Names](https://devdocs.io/gnu_make/file-name-functions).

`$(abspath names…)`
For each file name in names, expand to an absolute name that does not contain any `.` or `..` components, but preserves symlinks. See [Functions for File Names](https://devdocs.io/gnu_make/file-name-functions).

`$(error text…)`
When this function is evaluated, `make` generates a fatal error with the message text. See [Functions That Control Make](https://devdocs.io/gnu_make/make-control-functions).

`$(warning text…)`
When this function is evaluated, `make` generates a warning with the message text. See [Functions That Control Make](https://devdocs.io/gnu_make/make-control-functions).

`$(shell command)`
Execute a shell command and return its output. See [The `shell` Function](https://devdocs.io/gnu_make/shell-function).

`$(origin variable)`
Return a string describing how the `make` variable variable was defined. See [The `origin` Function](https://devdocs.io/gnu_make/origin-function).

`$(flavor variable)`
Return a string describing the flavor of the `make` variable variable. See [The `flavor` Function](https://devdocs.io/gnu_make/flavor-function).

`$(let var [var ...],words,text)`
Evaluate text with the var s bound to the words in words. See [The `let` Function](https://devdocs.io/gnu_make/let-function).

`$(foreach var,words,text)`
Evaluate text with var bound to each word in words, and concatenate the results. See [The `foreach` Function](https://devdocs.io/gnu_make/foreach-function).

`$(if condition,then-part[,else-part])`
Evaluate the condition condition; if it’s non-empty substitute the expansion of the then-part otherwise substitute the expansion of the else-part. See [Functions for Conditionals](https://devdocs.io/gnu_make/conditional-functions).

`$(or condition1[,condition2[,condition3…]])`
Evaluate each condition conditionN one at a time; substitute the first non-empty expansion. If all expansions are empty, substitute the empty string. See [Functions for Conditionals](https://devdocs.io/gnu_make/conditional-functions).

`$(and condition1[,condition2[,condition3…]])`
Evaluate each condition conditionN one at a time; if any expansion results in the empty string substitute the empty string. If all expansions result in a non-empty string, substitute the expansion of the last condition. See [Functions for Conditionals](https://devdocs.io/gnu_make/conditional-functions).

`$(intcmp lhs,rhs[,lt-part[,eq-part[,gt-part]]])`
Compare lhs and rhs numerically; substitute the expansion of lt-part, eq-part, or gt-part depending on whether the left-hand side is less-than, equal-to, or greater-than the right-hand side, respectively. See [Functions for Conditionals](https://devdocs.io/gnu_make/conditional-functions).

`$(call var,param,…)`
Evaluate the variable var replacing any references to `$(1)`, `$(2)` with the first, second, etc. param values. See [The `call` Function](https://devdocs.io/gnu_make/call-function).

`$(eval text)`
Evaluate text then read the results as makefile commands. Expands to the empty string. See [The `eval` Function](https://devdocs.io/gnu_make/eval-function).

`$(file op filename,text)`
Expand the arguments, then open the file filename using mode op and write text to that file. See [The `file` Function](https://devdocs.io/gnu_make/file-function).

`$(value var)`
Evaluates to the contents of the variable var, with no expansion performed on it. See [The `value` Function](https://devdocs.io/gnu_make/value-function).

Here is a summary of the automatic variables. See [Automatic Variables](https://devdocs.io/gnu_make/automatic-variables), for full information.

`$@`
The file name of the target.

`$%`
The target member name, when the target is an archive member.

`$<`
The name of the first prerequisite.

`$?`
The names of all the prerequisites that are newer than the target, with spaces between them. For prerequisites which are archive members, only the named member is used (see [Archives](https://devdocs.io/gnu_make/archives)).

`$^``$+`
The names of all the prerequisites, with spaces between them. For prerequisites which are archive members, only the named member is used (see [Archives](https://devdocs.io/gnu_make/archives)). The value of `$^` omits duplicate prerequisites, while `$+` retains them and preserves their order.

`$*`
The stem with which an implicit rule matches (see [How Patterns Match](https://devdocs.io/gnu_make/pattern-match)).

`$(@D)``$(@F)`
The directory part and the file-within-directory part of `$@`.

`$(*D)``$(*F)`
The directory part and the file-within-directory part of `$*`.

`$(%D)``$(%F)`
The directory part and the file-within-directory part of `$%`.

`$(<D)``$(<F)`
The directory part and the file-within-directory part of `$<`.

`$(^D)``$(^F)`
The directory part and the file-within-directory part of `$^`.

`$(+D)``$(+F)`
The directory part and the file-within-directory part of `$+`.

`$(?D)``$(?F)`
The directory part and the file-within-directory part of `$?`.

These variables are used specially by GNU `make`:

`MAKEFILES`
Makefiles to be read on every invocation of `make`. See [The Variable `MAKEFILES`](https://devdocs.io/gnu_make/makefiles-variable).

`VPATH`
Directory search path for files not found in the current directory. See [`VPATH` Search Path for All Prerequisites](https://devdocs.io/gnu_make/general-search).

`SHELL`
The name of the system default command interpreter, usually /bin/sh. You can set `SHELL` in the makefile to change the shell used to run recipes. See [Recipe Execution](https://devdocs.io/gnu_make/execution). The `SHELL` variable is handled specially when importing from and exporting to the environment. See [Choosing the Shell](https://devdocs.io/gnu_make/choosing-the-shell).

`MAKESHELL`
On MS-DOS only, the name of the command interpreter that is to be used by `make`. This value takes precedence over the value of `SHELL`. See [MAKESHELL variable](https://devdocs.io/gnu_make/execution).

`MAKE`
The name with which `make` was invoked. Using this variable in recipes has special meaning. See [How the `MAKE` Variable Works](https://devdocs.io/gnu_make/make-variable).

`MAKE_VERSION`
The built-in variable ‘MAKE_VERSION’ expands to the version number of the GNU `make` program.

`MAKE_HOST`
The built-in variable ‘MAKE_HOST’ expands to a string representing the host that GNU `make` was built to run on.

`MAKELEVEL`
The number of levels of recursion (sub-`make`s). See [Variables/Recursion](https://devdocs.io/gnu_make/variables_002frecursion).

`MAKEFLAGS`
The flags given to `make`. You can set this in the environment or a makefile to set flags. See [Communicating Options to a Sub-`make`](https://devdocs.io/gnu_make/options_002frecursion).

It is _never_ appropriate to use `MAKEFLAGS` directly in a recipe line: its contents may not be quoted correctly for use in the shell. Always allow recursive `make`’s to obtain these values through the environment from its parent.

`GNUMAKEFLAGS`
Other flags parsed by `make`. You can set this in the environment or a makefile to set `make` command-line flags. GNU `make` never sets this variable itself. This variable is only needed if you’d like to set GNU `make`-specific flags in a POSIX-compliant makefile. This variable will be seen by GNU `make` and ignored by other `make` implementations. It’s not needed if you only use GNU `make`; just use `MAKEFLAGS` directly. See [Communicating Options to a Sub-`make`](https://devdocs.io/gnu_make/options_002frecursion).

`MAKECMDGOALS`
The targets given to `make` on the command line. Setting this variable has no effect on the operation of `make`. See [Arguments to Specify the Goals](https://devdocs.io/gnu_make/goals).

`CURDIR`
Set to the absolute pathname of the current working directory (after all `-C` options are processed, if any). Setting this variable has no effect on the operation of `make`. See [Recursive Use of `make`](https://devdocs.io/gnu_make/recursion).

`SUFFIXES`
The default list of suffixes before `make` reads any makefiles.

`.LIBPATTERNS`
Defines the naming of the libraries `make` searches for, and their order. See [Directory Search for Link Libraries](https://devdocs.io/gnu_make/libraries_002fsearch).

Copyright © 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022 Free Software Foundation, Inc. 

Licensed under the GNU Free Documentation License.

[https://www.gnu.org/software/make/manual/html_node/Quick-Reference.html](https://www.gnu.org/software/make/manual/html_node/Quick-Reference.html)
