# Source: https://devdocs.io/gnu_make/static-usage

Title: Syntax of Static Pattern Rules — DevDocs

URL Source: https://devdocs.io/gnu_make/static-usage

Markdown Content:
GNU Make / Syntax of Static Pattern Rules — DevDocs
===============

You're browsing the GNU Make documentation. To browse all docs, go to [devdocs.io](https://devdocs.io/) (or press `esc`).

Clear search
[DevDocs](https://devdocs.io/)
==============================

[Preferences](https://devdocs.io/settings)[Offline Data](https://devdocs.io/offline)[Changelog](https://devdocs.io/news)[Guide](https://devdocs.io/help)[About](https://devdocs.io/about)[Report a bug](https://github.com/freeCodeCamp/devdocs/issues/new/choose)

[4.4 GNU Make](https://devdocs.io/gnu_make/ "GNU Make")

[156 Manual](https://devdocs.io/gnu_make-manual/)

Show more… (50)[How Directory Searches are Performed](https://devdocs.io/gnu_make/search-algorithm)[How Loaded Objects Are Remade](https://devdocs.io/gnu_make/remaking-loaded-objects)[How make Processes a Makefile](https://devdocs.io/gnu_make/how-make-works)[How make Reads a Makefile](https://devdocs.io/gnu_make/reading-makefiles)[How Makefiles Are Parsed](https://devdocs.io/gnu_make/parsing-makefiles)[How Makefiles Are Remade](https://devdocs.io/gnu_make/remaking-makefiles)[How Patterns Match](https://devdocs.io/gnu_make/pattern-match)[How the MAKE Variable Works](https://devdocs.io/gnu_make/make-variable)[How to Read This Manual](https://devdocs.io/gnu_make/reading)[How to Run make](https://devdocs.io/gnu_make/running)[How to Use Variables](https://devdocs.io/gnu_make/using-variables)[How Variables Get Their Values](https://devdocs.io/gnu_make/values)[Immediately Expanded Variable Assignment](https://devdocs.io/gnu_make/immediate-assignment)[Implicit Rule for Archive Member Targets](https://devdocs.io/gnu_make/archive-update)[Implicit Rule Search Algorithm](https://devdocs.io/gnu_make/implicit-rule-search)[Including Other Makefiles](https://devdocs.io/gnu_make/include)[Incompatibilities and Missing Features](https://devdocs.io/gnu_make/missing)[Input During Parallel Execution](https://devdocs.io/gnu_make/parallel-input)[Install Command Categories](https://devdocs.io/gnu_make/install-command-categories)[Instead of Executing Recipes](https://devdocs.io/gnu_make/instead-of-execution)[Integrating GNU make](https://devdocs.io/gnu_make/integrating-make)[Interfaces from Guile to make](https://devdocs.io/gnu_make/guile-interface)[Interrupting or Killing make](https://devdocs.io/gnu_make/interrupts)[Introduction to Pattern Rules](https://devdocs.io/gnu_make/pattern-intro)[Letting make Deduce the Recipes](https://devdocs.io/gnu_make/make-deduces)[Loaded Object Interface](https://devdocs.io/gnu_make/loaded-object-api)[Loading Dynamic Objects](https://devdocs.io/gnu_make/loading-objects)[Makefile Conventions](https://devdocs.io/gnu_make/makefile-conventions)[Match-Anything Pattern Rules](https://devdocs.io/gnu_make/match_002danything-rules)[Multiple Rules for One Target](https://devdocs.io/gnu_make/multiple-rules)[Multiple Targets in a Rule](https://devdocs.io/gnu_make/multiple-targets)[Old-Fashioned Suffix Rules](https://devdocs.io/gnu_make/suffix-rules)[Other Special Variables](https://devdocs.io/gnu_make/special-variables)[Output During Parallel Execution](https://devdocs.io/gnu_make/parallel-output)[Overriding Part of Another Makefile](https://devdocs.io/gnu_make/overriding-makefiles)[Overriding Variables](https://devdocs.io/gnu_make/overriding)[Overview of make](https://devdocs.io/gnu_make/overview)[Parallel Execution](https://devdocs.io/gnu_make/parallel)[Pattern Rule Examples](https://devdocs.io/gnu_make/pattern-examples)[Pattern-specific Variable Values](https://devdocs.io/gnu_make/pattern_002dspecific)[Phony Targets](https://devdocs.io/gnu_make/phony-targets)[Pitfalls of Using Wildcards](https://devdocs.io/gnu_make/wildcard-pitfall)[POSIX Jobserver Interaction](https://devdocs.io/gnu_make/posix-jobserver)[Preparing and Running Make](https://devdocs.io/gnu_make/preparing)[Problems and Bugs](https://devdocs.io/gnu_make/bugs)[Quick Reference](https://devdocs.io/gnu_make/quick-reference)[Recipe Echoing](https://devdocs.io/gnu_make/echoing)[Recipe Execution](https://devdocs.io/gnu_make/execution)[Recipe Syntax](https://devdocs.io/gnu_make/recipe-syntax)[Recursive Use of make](https://devdocs.io/gnu_make/recursion)[Recursively Expanded Variable Assignment](https://devdocs.io/gnu_make/recursive-assignment)[Rule Example](https://devdocs.io/gnu_make/rule-example)[Rule Syntax](https://devdocs.io/gnu_make/rule-syntax)[Rules for Cleaning the Directory](https://devdocs.io/gnu_make/cleanup)[Rules without Recipes or Prerequisites](https://devdocs.io/gnu_make/force-targets)[Searching Directories for Prerequisites](https://devdocs.io/gnu_make/directory-search)[Secondary Expansion](https://devdocs.io/gnu_make/secondary-expansion)[Setting Variables](https://devdocs.io/gnu_make/setting)[Sharing Job Slots with GNU make](https://devdocs.io/gnu_make/job-slots)[Simply Expanded Variable Assignment](https://devdocs.io/gnu_make/simple-assignment)[Special Built-in Target Names](https://devdocs.io/gnu_make/special-targets)[Splitting Long Lines](https://devdocs.io/gnu_make/splitting-lines)[Splitting Recipe Lines](https://devdocs.io/gnu_make/splitting-recipe-lines)[Standard Targets for Users](https://devdocs.io/gnu_make/standard-targets)[Static Pattern Rules](https://devdocs.io/gnu_make/static-pattern)[Static Pattern Rules versus Implicit Rules](https://devdocs.io/gnu_make/static-versus-implicit)[Substitution References](https://devdocs.io/gnu_make/substitution-refs)[Suffix Rules for Archive Files](https://devdocs.io/gnu_make/archive-suffix-rules)[Summary of Options](https://devdocs.io/gnu_make/options-summary)[Suppressing Inheritance](https://devdocs.io/gnu_make/suppressing-inheritance)[Synchronized Terminal Output](https://devdocs.io/gnu_make/terminal-output)[Syntax of Conditionals](https://devdocs.io/gnu_make/conditional-syntax)[Syntax of Static Pattern Rules](https://devdocs.io/gnu_make/static-usage)[Target-specific Variable Values](https://devdocs.io/gnu_make/target_002dspecific)[Temporary Files](https://devdocs.io/gnu_make/temporary-files)[Testing the Compilation of a Program](https://devdocs.io/gnu_make/testing)[The Function wildcard](https://devdocs.io/gnu_make/wildcard-function)[The Two Flavors of Variables](https://devdocs.io/gnu_make/flavors)[The Variable MAKEFILES](https://devdocs.io/gnu_make/makefiles-variable)[The ‘--print-directory’ Option](https://devdocs.io/gnu_make/_002dw-option)[Types of Prerequisites](https://devdocs.io/gnu_make/prerequisite-types)[Undefining Variables](https://devdocs.io/gnu_make/undefine-directive)[Updating Archive Symbol Directories](https://devdocs.io/gnu_make/archive-symbols)[Using Empty Recipes](https://devdocs.io/gnu_make/empty-recipes)[Using Implicit Rules](https://devdocs.io/gnu_make/using-implicit)[Using Implicit Rules](https://devdocs.io/gnu_make/implicit-rules)[Using make to Update Archive Files](https://devdocs.io/gnu_make/archives)[Using One Shell](https://devdocs.io/gnu_make/one-shell)[Using Variables in Recipes](https://devdocs.io/gnu_make/variables-in-recipes)[Using Wildcard Characters in File Names](https://devdocs.io/gnu_make/wildcards)[Utilities in Makefiles](https://devdocs.io/gnu_make/utilities-in-makefiles)[Variables for Installation Directories](https://devdocs.io/gnu_make/directory-variables)[Variables for Specifying Commands](https://devdocs.io/gnu_make/command-variables)[Variables from the Environment](https://devdocs.io/gnu_make/environment)[Variables Make Makefiles Simpler](https://devdocs.io/gnu_make/variables-simplify)[Variables Used by Implicit Rules](https://devdocs.io/gnu_make/implicit-variables)[VPATH: Search Path for All Prerequisites](https://devdocs.io/gnu_make/general-search)[What a Rule Looks Like](https://devdocs.io/gnu_make/rule-introduction)[What Makefiles Contain](https://devdocs.io/gnu_make/makefile-contents)[What Name to Give Your Makefile](https://devdocs.io/gnu_make/makefile-names)Show more… (6)

[68 Automatic Variables](https://devdocs.io/gnu_make-automatic-variables/)[16 Built-in targets](https://devdocs.io/gnu_make-built-in-targets/)[4 Conditionals Functions](https://devdocs.io/gnu_make-conditionals-functions/)[12 Conditionals Syntax](https://devdocs.io/gnu_make-conditionals-syntax/)[3 Directives](https://devdocs.io/gnu_make-directives/)[10 File Names Functions](https://devdocs.io/gnu_make-file-names-functions/)[68 Make Cli Options](https://devdocs.io/gnu_make-make-cli-options/)[3 Make Control Functions](https://devdocs.io/gnu_make-make-control-functions/)[12 String Substitution and Analysis Functions](https://devdocs.io/gnu_make-string-substitution-and-analysis-functions/)[10 Transforming text functions](https://devdocs.io/gnu_make-transforming-text-functions/)

Syntax of Static Pattern Rules
==============================

Here is the syntax of a static pattern rule:

targets …: target-pattern: prereq-patterns …
        recipe
        …

The targets list specifies the targets that the rule applies to. The targets can contain wildcard characters, just like the targets of ordinary rules (see [Using Wildcard Characters in File Names](https://devdocs.io/gnu_make/wildcards)).

The target-pattern and prereq-patterns say how to compute the prerequisites of each target. Each target is matched against the target-pattern to extract a part of the target name, called the _stem_. This stem is substituted into each of the prereq-patterns to make the prerequisite names (one from each prereq-pattern).

Each pattern normally contains the character ‘%’ just once. When the target-pattern matches a target, the ‘%’ can match any part of the target name; this part is called the _stem_. The rest of the pattern must match exactly. For example, the target foo.o matches the pattern ‘%.o’, with ‘foo’ as the stem. The targets foo.c and foo.out do not match that pattern.

The prerequisite names for each target are made by substituting the stem for the ‘%’ in each prerequisite pattern. For example, if one prerequisite pattern is %.c, then substitution of the stem ‘foo’ gives the prerequisite name foo.c. It is legitimate to write a prerequisite pattern that does not contain ‘%’; then this prerequisite is the same for all targets.

‘%’ characters in pattern rules can be quoted with preceding backslashes (‘\’). Backslashes that would otherwise quote ‘%’ characters can be quoted with more backslashes. Backslashes that quote ‘%’ characters or other backslashes are removed from the pattern before it is compared to file names or has a stem substituted into it. Backslashes that are not in danger of quoting ‘%’ characters go unmolested. For example, the pattern the\%weird\\%pattern\\ has ‘the%weird\’ preceding the operative ‘%’ character, and ‘pattern\\’ following it. The final two backslashes are left alone because they cannot affect any ‘%’ character.

Here is an example, which compiles each of foo.o and bar.o from the corresponding .c file:

objects = foo.o bar.o

all: $(objects)

$(objects): %.o: %.c
        $(CC) -c $(CFLAGS) $< -o $@

Here ‘$<’ is the automatic variable that holds the name of the prerequisite and ‘$@’ is the automatic variable that holds the name of the target; see [Automatic Variables](https://devdocs.io/gnu_make/automatic-variables).

Each target specified must match the target pattern; a warning is issued for each target that does not. If you have a list of files, only some of which will match the pattern, you can use the `filter` function to remove non-matching file names (see [Functions for String Substitution and Analysis](https://devdocs.io/gnu_make/text-functions)):

files = foo.elc bar.o lose.o

$(filter %.o,$(files)): %.o: %.c
        $(CC) -c $(CFLAGS) $< -o $@
$(filter %.elc,$(files)): %.elc: %.el
        emacs -f batch-byte-compile $<

In this example the result of ‘$(filter %.o,$(files))’ is bar.o lose.o, and the first static pattern rule causes each of these object files to be updated by compiling the corresponding C source file. The result of ‘$(filter %.elc,$(files))’ is foo.elc, so that file is made from foo.el.

Another example shows how to use `$*` in static pattern rules:

bigoutput littleoutput : %output : text.g
        generate text.g -$* > $@

When the `generate` command is run, `$*` will expand to the stem, either ‘big’ or ‘little’.

Copyright © 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022 Free Software Foundation, Inc. 

Licensed under the GNU Free Documentation License.

[https://www.gnu.org/software/make/manual/html_node/Static-Usage.html](https://www.gnu.org/software/make/manual/html_node/Static-Usage.html)

 Back  Apply Docs Settings

##### Tracking cookies

We would like to gather usage data about how DevDocs is used through Google Analytics and Gauges. We only collect anonymous traffic information. Please confirm if you accept our tracking cookies. You can always change your decision in the settings. 

[Accept](https://devdocs.io/gnu_make/static-usage#) or [Decline](https://devdocs.io/gnu_make/static-usage#)Close
