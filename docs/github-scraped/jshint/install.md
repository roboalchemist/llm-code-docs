# Source: https://jshint.com/install/

Download and install

JSHint

About

Docs

Install

Contribute

Blog

Jump to docs

This page&#39;s content is sourced from 
the JSHint project repository
. If you spot an error, please 
open an issue
 or (better yet) 
make a pull request
!

Download and install

JSHint runs in a number of different environments; installation is different
for each.

Browser-like environments

A standalone files is built for browser-like environments with every release.
You&#39;ll find it in the 
dist
 directory of the download. 
Download the latest
release here
.

Rhino

A standalone files is built for Mozilla&#39;s 
Rhino JavaScript
engine
 with every release. You&#39;ll find it in
the 
dist
 directory of the download. 
Download the latest release
here
.

Node.js

Each release of JSHint is published to 
npm
, the package
manager for 
the Node.js platform
.

You may 
install it globally
 using the following command:

npm install -g jshint

After this, you can use the 
jshint
 command-line interface.

It is common to install JSHint as a development dependency within an existing
Node.js project:

npm install --save-dev jshint

Plugins for text editors and IDEs

VIM

jshint.vim
, VIM plugin and command line
tool for running JSHint.

jshint2.vim
, modern VIM plugin with
extra features for running JSHint.

Syntastic
,
supports JSHint both older/newer than 1.1.0.

Emacs

jshint-mode
, JSHint mode for GNU
Emacs.

Flycheck
, on-the-fly syntax checking
extension for GNU Emacs, built-in JSHint support.

web-mode
, an autonomous major-mode for editing web templates
supports JSHint.

Sublime Text

Sublime-JSHint Gutter
, JSHint
plugin for graphically displaying lint results in ST2 and ST3.

sublime-jshint
, JSHint build package
for ST2.

Sublime Linter
, inline lint
highlighting for ST2.

Atom

linter-jshint
, JSHint plugin for Atom&#39;s Linter.

JSHint for Atom
, JSHint package for Atom.

TextMate

JSHint Bundle for TextMate 2

JSHint TextMate Bundle
.

JSLintMate
 (supports both JSHint and
JSLint).

JSHint-external TextMate Bundle

Visual Studio

SharpLinter
 (supports both JSLint and
JSHint).

JSLint for Visual Studio
 (supports both
JSLint and JSHint).

Web Essentials
 (Runs JSHint automatically).

Visual Studio Code

VS Code JSHint extension
, integrates JSHint into VS Code.

Brackets

Brackets JSHint plugin

Brackets Interactive Linter

Other

ShiftEdit IDE
 has built-in support for JSHint.

Komodo 7 now ships

with built-in support for JSHint.

JSHint integration for the Eclipse IDE

JSHint integration for the NetBeans IDE

JetBrains IDE family
 supports realtime
code inspection with both JSHint and JSLint out of the box.

JSLint plugin for Notepad++
 now
supports JSHint.

JSHint plugin for Gedit
.

Other cool stuff

JSHintr
 is a web tool that allows you to
set your own code standards, easily review a file against these standards, and
share the output with other developers.

FixMyJS
 is a tool that automatically fixes
mistakes—such as missing semicolon, multiple definitions, etc.—reported by
JSHint.

A ruby gem for JSHint
.

Another ruby gem
 but without Java
dependency.

pre-commit
 checks your code for errors
before you commit it.

Dedicated Ant task
 to easily
automate JSHint in Ant Maven.

QHint - JSHint in QUnit
. Check for errors in
your code from within your unit tests. Lint errors result in failed tests.

Grunt
, a task-based command line build tool for JavaScript
projects, supports JSHint out of the box.

overcommit
 is an extensible Git hook
manager with built-in JSHint linting, distributed as a Ruby gem. 
Read
more

about it.

jshint-mojo
, a plugin for Maven.

JSXHint
, a wrapper around JSHint to allow
linting of files containing JSX syntax.