# Source: https://devdocs.io/gnu_make/recipes_002fsearch

Title: Writing Recipes with Directory Search — DevDocs

URL Source: https://devdocs.io/gnu_make/recipes_002fsearch

Markdown Content:
GNU Make / Writing Recipes with Directory Search — DevDocs
===============

You're browsing the GNU Make documentation. To browse all docs, go to [devdocs.io](https://devdocs.io/) (or press `esc`).

Clear search
[DevDocs](https://devdocs.io/)
==============================

[Preferences](https://devdocs.io/settings)[Offline Data](https://devdocs.io/offline)[Changelog](https://devdocs.io/news)[Guide](https://devdocs.io/help)[About](https://devdocs.io/about)[Report a bug](https://github.com/freeCodeCamp/devdocs/issues/new/choose)

[4.4 GNU Make](https://devdocs.io/gnu_make/ "GNU Make")

[156 Manual](https://devdocs.io/gnu_make-manual/)

Show more… (100)[Recursively Expanded Variable Assignment](https://devdocs.io/gnu_make/recursive-assignment)[Rule Example](https://devdocs.io/gnu_make/rule-example)[Rule Syntax](https://devdocs.io/gnu_make/rule-syntax)[Rules for Cleaning the Directory](https://devdocs.io/gnu_make/cleanup)[Rules without Recipes or Prerequisites](https://devdocs.io/gnu_make/force-targets)[Searching Directories for Prerequisites](https://devdocs.io/gnu_make/directory-search)[Secondary Expansion](https://devdocs.io/gnu_make/secondary-expansion)[Setting Variables](https://devdocs.io/gnu_make/setting)[Sharing Job Slots with GNU make](https://devdocs.io/gnu_make/job-slots)[Simply Expanded Variable Assignment](https://devdocs.io/gnu_make/simple-assignment)[Special Built-in Target Names](https://devdocs.io/gnu_make/special-targets)[Splitting Long Lines](https://devdocs.io/gnu_make/splitting-lines)[Splitting Recipe Lines](https://devdocs.io/gnu_make/splitting-recipe-lines)[Standard Targets for Users](https://devdocs.io/gnu_make/standard-targets)[Static Pattern Rules](https://devdocs.io/gnu_make/static-pattern)[Static Pattern Rules versus Implicit Rules](https://devdocs.io/gnu_make/static-versus-implicit)[Substitution References](https://devdocs.io/gnu_make/substitution-refs)[Suffix Rules for Archive Files](https://devdocs.io/gnu_make/archive-suffix-rules)[Summary of Options](https://devdocs.io/gnu_make/options-summary)[Suppressing Inheritance](https://devdocs.io/gnu_make/suppressing-inheritance)[Synchronized Terminal Output](https://devdocs.io/gnu_make/terminal-output)[Syntax of Conditionals](https://devdocs.io/gnu_make/conditional-syntax)[Syntax of Static Pattern Rules](https://devdocs.io/gnu_make/static-usage)[Target-specific Variable Values](https://devdocs.io/gnu_make/target_002dspecific)[Temporary Files](https://devdocs.io/gnu_make/temporary-files)[Testing the Compilation of a Program](https://devdocs.io/gnu_make/testing)[The Function wildcard](https://devdocs.io/gnu_make/wildcard-function)[The Two Flavors of Variables](https://devdocs.io/gnu_make/flavors)[The Variable MAKEFILES](https://devdocs.io/gnu_make/makefiles-variable)[The ‘--print-directory’ Option](https://devdocs.io/gnu_make/_002dw-option)[Types of Prerequisites](https://devdocs.io/gnu_make/prerequisite-types)[Undefining Variables](https://devdocs.io/gnu_make/undefine-directive)[Updating Archive Symbol Directories](https://devdocs.io/gnu_make/archive-symbols)[Using Empty Recipes](https://devdocs.io/gnu_make/empty-recipes)[Using Implicit Rules](https://devdocs.io/gnu_make/using-implicit)[Using Implicit Rules](https://devdocs.io/gnu_make/implicit-rules)[Using make to Update Archive Files](https://devdocs.io/gnu_make/archives)[Using One Shell](https://devdocs.io/gnu_make/one-shell)[Using Variables in Recipes](https://devdocs.io/gnu_make/variables-in-recipes)[Using Wildcard Characters in File Names](https://devdocs.io/gnu_make/wildcards)[Utilities in Makefiles](https://devdocs.io/gnu_make/utilities-in-makefiles)[Variables for Installation Directories](https://devdocs.io/gnu_make/directory-variables)[Variables for Specifying Commands](https://devdocs.io/gnu_make/command-variables)[Variables from the Environment](https://devdocs.io/gnu_make/environment)[Variables Make Makefiles Simpler](https://devdocs.io/gnu_make/variables-simplify)[Variables Used by Implicit Rules](https://devdocs.io/gnu_make/implicit-variables)[VPATH: Search Path for All Prerequisites](https://devdocs.io/gnu_make/general-search)[What a Rule Looks Like](https://devdocs.io/gnu_make/rule-introduction)[What Makefiles Contain](https://devdocs.io/gnu_make/makefile-contents)[What Name to Give Your Makefile](https://devdocs.io/gnu_make/makefile-names)[Wildcard Examples](https://devdocs.io/gnu_make/wildcard-examples)[Windows Jobserver Interaction](https://devdocs.io/gnu_make/windows-jobserver)[Writing Makefiles](https://devdocs.io/gnu_make/makefiles)[Writing Recipes in Rules](https://devdocs.io/gnu_make/recipes)[Writing Recipes with Directory Search](https://devdocs.io/gnu_make/recipes_002fsearch)[Writing Rules](https://devdocs.io/gnu_make/rules)

[68 Automatic Variables](https://devdocs.io/gnu_make-automatic-variables/)[16 Built-in targets](https://devdocs.io/gnu_make-built-in-targets/)[4 Conditionals Functions](https://devdocs.io/gnu_make-conditionals-functions/)[12 Conditionals Syntax](https://devdocs.io/gnu_make-conditionals-syntax/)[3 Directives](https://devdocs.io/gnu_make-directives/)[10 File Names Functions](https://devdocs.io/gnu_make-file-names-functions/)[68 Make Cli Options](https://devdocs.io/gnu_make-make-cli-options/)[3 Make Control Functions](https://devdocs.io/gnu_make-make-control-functions/)[12 String Substitution and Analysis Functions](https://devdocs.io/gnu_make-string-substitution-and-analysis-functions/)[10 Transforming text functions](https://devdocs.io/gnu_make-transforming-text-functions/)

Writing Recipes with Directory Search
=====================================

When a prerequisite is found in another directory through directory search, this cannot change the recipe of the rule; they will execute as written. Therefore, you must write the recipe with care so that it will look for the prerequisite in the directory where `make` finds it.

This is done with the _automatic variables_ such as ‘$^’ (see [Automatic Variables](https://devdocs.io/gnu_make/automatic-variables)). For instance, the value of ‘$^’ is a list of all the prerequisites of the rule, including the names of the directories in which they were found, and the value of ‘$@’ is the target. Thus:

foo.o : foo.c
        cc -c $(CFLAGS) $^ -o $@

(The variable `CFLAGS` exists so you can specify flags for C compilation by implicit rules; we use it here for consistency so it will affect all C compilations uniformly; see [Variables Used by Implicit Rules](https://devdocs.io/gnu_make/implicit-variables).)

Often the prerequisites include header files as well, which you do not want to mention in the recipe. The automatic variable ‘$<’ is just the first prerequisite:

VPATH = src:../headers
foo.o : foo.c defs.h hack.h
        cc -c $(CFLAGS) $< -o $@

Copyright © 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022 Free Software Foundation, Inc. 

Licensed under the GNU Free Documentation License.

[https://www.gnu.org/software/make/manual/html_node/Recipes_002fSearch.html](https://www.gnu.org/software/make/manual/html_node/Recipes_002fSearch.html)

 Back  Apply Docs Settings

##### Tracking cookies

We would like to gather usage data about how DevDocs is used through Google Analytics and Gauges. We only collect anonymous traffic information. Please confirm if you accept our tracking cookies. You can always change your decision in the settings. 

[Accept](https://devdocs.io/gnu_make/recipes_002fsearch#) or [Decline](https://devdocs.io/gnu_make/recipes_002fsearch#)Close
