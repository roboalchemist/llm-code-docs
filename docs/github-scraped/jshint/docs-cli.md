# Source: https://jshint.com/docs/cli/

JSHint CLI flags

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

Command-line Interface

The JSHint CLI can be installed via npm (see 
the Installation
page
 for instructions).

Contents: 
Specifying Input
 · 
Specifying Linting
Options
 · 
Special Options
 ·

Ignoring Files
 · 
Flags

Specifying Input

The 
jshint
 executable accepts file system paths as command-line arguments. If
a provided path describes a file, the executable will read that file and lint
the JavaScript code it contains:

$ jshint myfile.js
myfile.js: line 10, col 39, Octal literals are not allowed in strict mode.

1 error

If a provided path describes a file system directory, JSHint will traverse
the directory and any subdirectories recursively, reading all JavaScript files
and linting their contents:

$ tree a-directory/
a-directory/
├── file-1.js
└── nested
 └── file-2.js

1 directory, 2 files

$ jshint a-directory/
a-directory/file-1.js: line 3, col 1, &#39;with&#39; is not allowed in strict mode.

a-directory/nested/file-2.js: line 3, col 3, Unreachable &#39;void&#39; after &#39;return&#39;.

2 errors

If a file path is a dash (
-
) then JSHint will read from standard input.

Specifying Linting Options

The 
jshint
 executable is capable of applying 
linting
options
 specified in an external

JSON
-formatted file. Such a file might look like this:

{
 &quot;curly&quot;: true,
 &quot;eqeqeq&quot;: true,
 &quot;nocomma&quot;: true
}

jshint
 will look for this configuration in a number of locations, stopping at
the first positive match:

The location specified with the 
--config

flag

A file named 
package.json
 located in the current directory or any parent
of the current directory (the configuration should be declared as the

jshintConfig
 attribute of that file&#39;s JSON value)

A file named 
.jshintrc
 located in the current directory or any parent of
the current directory

A file named 
.jshintrc
 located in the current user&#39;s &quot;home&quot; directory
(where defined)

If this search yields no results, 
jshint
 will lint the input code as if no
linting rules had been enabled.

The command-line interface offers some 
special options
 in
addition to 
the ones available in other
contexts

Special Options

The following options concern the file system and are only available from
within configuration files (i.e. not from inline directives or the API):

extends

Use another configuration file as a &quot;base&quot;. The value of this option should be
a file path to another configuration file, and the path should be relative to
the current file.

For example, you might define a 
.jshintrc
 file in the top-level directory of
your project (say, 
./.jshintrc
) to specify the 
linting
options
 you would like to use in your entire project:

{
 &quot;undef&quot;: true,
 &quot;unused&quot;: true
}

You may want to re-use this configuration for your project&#39;s automated tests,
but also 
allow for global
variables
 that are specific to the
test environment. In this case, you could create a a new file in their test
directory, (
./test/.jshintrc
 for example), and include the following
configuration:

{
 &quot;extends&quot;: &quot;../.jshintrc&quot;,
 &quot;globals&quot;: {
 &quot;test&quot;: false,
 &quot;assert&quot;: false
 }
}

overrides

Specify options that should only be applied to files matching a given path
pattern.

The following configuration file 
disallows variable
shadowing
 for 
all
 files and 
allows
expressions as statements
 for only those
files ending in 
-test.js
:

{
 &quot;shadow&quot;: false,
 &quot;overrides&quot;: {
 &quot;lib/*-test.js&quot;: {
 &quot;expr&quot;: true
 }
 }
}

Ignoring Files

jshint
 can be configured to ignore files based on their location in the
filesystem. You may create a dedicated &quot;ignore&quot; file to list any number of file
names, file paths, or file path patterns that should not be linted. Path
patterns will be interpreted using 
the 
minimatch
 npm
module
, which itself is based on 
the
Unix filename matching syntax, fnmatch
.

build/
src/**/tmp.js

jshint
 will look for this configuration in a number of locations, stopping at
the first positive match:

The location specified with the 
--exclude-path

flag

A file named 
.jshintignore
 located in the current directory or any parent
of the current directory

If this search yields no results, 
jshint
 will not ignore any files.

Flags

--config

Explicitly sets the location on the file system from which 
jshint
 should load
linting options.

$ jshint --config ../path/to/my/config.json

--reporter

Allows you to modify JSHint&#39;s output by replacing its default output function
with your own implementation.

$ jshint --reporter=myreporter.js myfile.js

This flag also supports two pre-defined reporters: 
jslint
, to make output
compatible with JSLint, and 
checkstyle
, to make output compatible with
CheckStyle XML.

$ jshint --reporter=checkstyle myfile.js
&lt;?xml version=&quot;1.0&quot; encoding=&quot;utf-8&quot;?&gt;
&lt;checkstyle version=&quot;4.3&quot;&gt;
 &lt;file name=&quot;myfile.js&quot;&gt;
 &lt;error line=&quot;10&quot; column=&quot;39&quot; severity=&quot;error&quot;
 message=&quot;Octal literals are not allowed in strict mode.&quot;/&gt;
 &lt;/file&gt;
&lt;/checkstyle&gt;

See also: 
Writing your own JSHint
reporter
.

--verbose

Adds message codes to the JSHint output.

--show-non-errors

Shows additional data generated by JSHint.

$ jshint --show-non-errors myfile.js
myfile.js: line 10, col 39, Octal literals are not allowed in strict mode.

1 error

myfile.js:
 Unused variables:
 foo, bar

--extra-ext

Allows you to specify additional file extensions to check (default is .js).

--extract=[auto|always|never]

Tells JSHint to extract JavaScript from HTML files before linting:

tmp ☭ cat test.html
&lt;html&gt;
 &lt;head&gt;
 &lt;title&gt;Hello, World!&lt;/title&gt;
 &lt;script&gt;
 function hello() {
 return &quot;Hello, World!&quot;;
 }
 &lt;/script&gt;
 &lt;/head&gt;
 &lt;body&gt;
 &lt;h1&gt;Hello, World!&lt;/h1&gt;
 &lt;script&gt;
 console.log(hello())
 &lt;/script&gt;
 &lt;/body&gt;
&lt;/html&gt;

tmp ☭ jshint --extract=auto test.html
test.html: line 13, col 27, Missing semicolon.

1 error

If you set it to 
always
 JSHint will always attempt to extract JavaScript.
And if you set it to 
auto
 it will make an attempt only if file looks
like it&#39;s an HTML file.

--exclude

Allows you to specify directories which you DON&#39;T want to be linted.

--exclude-path

Allows you to provide your own .jshintignore file. For example, you can point
JSHint to your .gitignore file and use it instead of default .jshintignore.

--prereq

Allows you to specify prerequisite files i.e. files which include definitions
of global variables used throughout your project.

--help

Shows a nice little help message similar to what you&#39;re reading right now.

--version

Shows the installed version of JSHint.