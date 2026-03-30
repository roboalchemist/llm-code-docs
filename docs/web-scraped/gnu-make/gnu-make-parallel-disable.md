# Source: https://devdocs.io/gnu_make/parallel-disable

Title: Disabling Parallel Execution — DevDocs

URL Source: https://devdocs.io/gnu_make/parallel-disable

Markdown Content:
If a makefile completely and accurately defines the dependency relationships between all of its targets, then `make` will correctly build the goals regardless of whether parallel execution is enabled or not. This is the ideal way to write makefiles.

However, sometimes some or all of the targets in a makefile cannot be executed in parallel and it’s not feasible to add the prerequisites needed to inform `make`. In that case the makefile can use various methods to disable parallel execution.

If the `.NOTPARALLEL` special target with no prerequisites is specified anywhere then the entire instance of `make` will be run serially, regardless of the parallel setting. For example:

all: one two three
one two three: ; @sleep 1; echo $@

.NOTPARALLEL:

Regardless of how `make` is invoked, the targets one, two, and three will be run serially.

If the `.NOTPARALLEL` special target has prerequisites, then each of those prerequisites will be considered a target and all prerequisites of these targets will be run serially. Note that only when building this target will the prerequisites be run serially: if some other target lists the same prerequisites and is not in `.NOTPARALLEL` then these prerequisites may be run in parallel. For example:

all: base notparallel

base: one two three
notparallel: one two three

one two three: ; @sleep 1; echo $@

.NOTPARALLEL: notparallel

Here ‘make -j base’ will run the targets one, two, and three in parallel, while ‘make -j notparallel’ will run them serially. If you run ‘make -j all’ then they _will_ be run in parallel since base lists them as prerequisites and is not serialized.

The `.NOTPARALLEL` target should not have commands.

Finally you can control the serialization of specific prerequisites in a fine-grained way using the `.WAIT` special target. When this target appears in a prerequisite list and parallel execution is enabled, `make` will not build any of the prerequisites to the _right_ of `.WAIT` until all prerequisites to the _left_ of `.WAIT` have completed. For example:

all: one two .WAIT three
one two three: ; @sleep 1; echo $@

If parallel execution is enabled, `make` will try to build one and two in parallel but will not try to build three until both are complete.

As with targets provided to `.NOTPARALLEL`, `.WAIT` takes effect only when building the target in whose prerequisite list it appears. If the same prerequisites are present in other targets, without `.WAIT`, then they may still be run in parallel. Because of this, neither `.NOTPARALLEL` with targets nor `.WAIT` are as reliable for controlling parallel execution as defining a prerequisite relationship. However they are easy to use and may be sufficient in less complex situations.

The `.WAIT` prerequisite will not be present in any of the automatic variables for the rule.

You can create an actual target `.WAIT` in your makefile for portability but this is not required to use this feature. If a `.WAIT` target is created it should not have prerequisites or commands.

The `.WAIT` feature is also implemented in other versions of `make` and it’s specified in the POSIX standard for `make`.

Copyright © 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022 Free Software Foundation, Inc. 

Licensed under the GNU Free Documentation License.

[https://www.gnu.org/software/make/manual/html_node/Parallel-Disable.html](https://www.gnu.org/software/make/manual/html_node/Parallel-Disable.html)
