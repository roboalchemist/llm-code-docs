# Source: https://devdocs.io/gnu_make/multiple-targets

Title: Multiple Targets in a Rule — DevDocs

URL Source: https://devdocs.io/gnu_make/multiple-targets

Markdown Content:
When an explicit rule has multiple targets they can be treated in one of two possible ways: as independent targets or as grouped targets. The manner in which they are treated is determined by the separator that appears after the list of targets.

#### Rules with Independent Targets

Rules that use the standard target separator, `:`, define independent targets. This is equivalent to writing the same rule once for each target, with duplicated prerequisites and recipes. Typically, the recipe would use automatic variables such as ‘$@’ to specify which target is being built.

Rules with independent targets are useful in two cases:

*    You want just prerequisites, no recipe. For example: kbd.o command.o files.o: command.h 
gives an additional prerequisite to each of the three object files mentioned. It is equivalent to writing:

kbd.o: command.h
command.o: command.h
files.o: command.h 
*    Similar recipes work for all the targets. The automatic variable ‘$@’ can be used to substitute the particular target to be remade into the commands (see [Automatic Variables](https://devdocs.io/gnu_make/automatic-variables)). For example: bigoutput littleoutput : text.g
        generate text.g -$(subst output,,$@) > $@ 
is equivalent to

bigoutput : text.g
        generate text.g -big > bigoutput
littleoutput : text.g
        generate text.g -little > littleoutput 
Here we assume the hypothetical program `generate` makes two types of output, one if given ‘-big’ and one if given ‘-little’. See [Functions for String Substitution and Analysis](https://devdocs.io/gnu_make/text-functions), for an explanation of the `subst` function.

Suppose you would like to vary the prerequisites according to the target, much as the variable ‘$@’ allows you to vary the recipe. You cannot do this with multiple targets in an ordinary rule, but you can do it with a _static pattern rule_. See [Static Pattern Rules](https://devdocs.io/gnu_make/static-pattern).

#### Rules with Grouped Targets

If instead of independent targets you have a recipe that generates multiple files from a single invocation, you can express that relationship by declaring your rule to use _grouped targets_. A grouped target rule uses the separator `&:` (the ‘&’ here is used to imply “all”).

When `make` builds any one of the grouped targets, it understands that all the other targets in the group are also updated as a result of the invocation of the recipe. Furthermore, if only some of the grouped targets are out of date or missing `make` will realize that running the recipe will update all of the targets. Finally, if any of the grouped targets are out of date, all the grouped targets are considered out of date.

As an example, this rule defines a grouped target:

foo bar biz &: baz boz
        echo $^ > foo
        echo $^ > bar
        echo $^ > biz

During the execution of a grouped target’s recipe, the automatic variable ‘$@’ is set to the name of the particular target in the group which triggered the rule. Caution must be used if relying on this variable in the recipe of a grouped target rule.

Unlike independent targets, a grouped target rule _must_ include a recipe. However, targets that are members of a grouped target may also appear in independent target rule definitions that do not have recipes.

Each target may have only one recipe associated with it. If a grouped target appears in either an independent target rule or in another grouped target rule with a recipe, you will get a warning and the latter recipe will replace the former recipe. Additionally the target will be removed from the previous group and appear only in the new group.

If you would like a target to appear in multiple groups, then you must use the double-colon grouped target separator, `&::` when declaring all of the groups containing that target. Grouped double-colon targets are each considered independently, and each grouped double-colon rule’s recipe is executed at most once, if at least one of its multiple targets requires updating.

Copyright © 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022 Free Software Foundation, Inc. 

Licensed under the GNU Free Documentation License.

[https://www.gnu.org/software/make/manual/html_node/Multiple-Targets.html](https://www.gnu.org/software/make/manual/html_node/Multiple-Targets.html)
