# Source: https://jshint.com/docs/

JSHint Documentation

JSHint

About

Docs

Install

Contribute

Blog

Jump to docs

Documentation

JSHint is a program that flags suspicious usage in programs written in JavaScript.
The core project consists of a library itself as well as a CLI program distributed
as a Node module.

More docs: 
List of all JSHint options
 · 
Command-line
Interface
 · 
API
 · 
Writing your own
reporter
 · 
FAQ

Basic usage

First, check out 
the installation instructions
 for details on
how to install JSHint in your preferred environment. Both the command line
executable and the JavaScript API offer unique ways to configure JSHint&#39;s
behaviour. The most common usages are:

As a command-line tool
 (via 
Node.js
)

As a JavaScript module

Regardless of your preferred environment, you can control JSHint&#39;s behavior
through specifying any number of 
linting options
. In
addition, JSHint will honor any directives declared within the input source
code--see 
the section on in-line directives
 for more
information.

Configuration

JSHint comes with a default set of warnings but it was designed to be very
configurable. There are three main ways to configure your copy of JSHint:
you can either specify the configuration file manually via the 
--config
 flag,
use a special file 
.jshintrc
 or put your config into your projects 
package.json

file under the 
jshintConfig
 property. In case of 
.jshintrc
, JSHint will start
looking for this file in the same directory as the file that&#39;s being linted.
If not found, it will move one level up the directory tree all the way up to
the filesystem root. (Note that if the input comes from stdin, JSHint doesn&#39;t
attempt to find a configuration file)

This setup allows you to have different configuration files per project. Place
your file into the project root directory and, as long as you run JSHint from
anywhere within your project directory tree, the same configuration file will
be used.

Configuration file is a simple JSON file that specifies which JSHint options
to turn on or off. For example, the following file will enable warnings about
undefined and unused variables and tell JSHint about a global variable named

MY_GLOBAL
.

{
 &quot;undef&quot;: true,
 &quot;unused&quot;: true,
 &quot;globals&quot;: {
 &quot;MY_GLOBAL&quot;: true
 }
}

Inline configuration

In addition to using configuration files you can configure JSHint from within your
files using special comments. These comments start with a label such as

jshint
 or 
globals
 (complete list below) and are followed by a
comma-separated list of values. For example, the following snippet will enable
warnings about undefined and unused variables and tell JSHint about a global
variable named 
MY_GLOBAL
.

/* jshint undef: true, unused: true */
/* globals MY_GLOBAL */

You can use both multi- and single-line comments to configure JSHint. These
comments are function scoped meaning that if you put them inside a function they
will affect only this function&#39;s code.

Directives

Here&#39;s a list of configuration directives supported by JSHint:

jshint

A directive for setting JSHint options.

/* jshint strict: true */

jslint

A directive for setting JSHint-compatible JSLint options.

/* jslint vars: true */

globals

A directive for telling JSHint about global variables that are defined
elsewhere. If value is 
false
 (default), JSHint will consider that variable
as read-only. Affects the 
undef
 option.

/* globals MY_LIB: false */

You can also blacklist certain global variables to make sure they are not used
anywhere in the current file.

/* globals -BAD_LIB */

exported

A directive for telling JSHint about global variables that are defined in the
current file but used elsewhere. Affects the 
unused
 option.

/* exported EXPORTED_LIB */

members

A directive for telling JSHint about all properties you intend to use. 
This
directive is deprecated.

ignore

A directive for telling JSHint to ignore a block of code.

// Code here will be linted with JSHint.
/* jshint ignore:start */
// Code here will be ignored by JSHint.
/* jshint ignore:end */

All code in between 
ignore:start
 and 
ignore:end
 won&#39;t be passed to JSHint
so you can use any language extension such as 
Facebook React
.
Additionally, you can ignore a single line with a trailing comment:

ignoreThis(); // jshint ignore:line

Options

Most often, when you need to tune JSHint to your own taste, all you need to do
is to find an appropriate option. Trying to figure out how JSHint options work
can be confusing and frustrating (and we&#39;re working on fixing that!) so please
read the following couple of paragraphs carefully.

JSHint has two types of options: enforcing and relaxing. The former are used to
make JSHint more strict while the latter are used to suppress some warnings.
Take the following code as an example:

function main(a, b) {
 return a == null;
}

This code will produce the following warning when run with default JSHint
options:

line 2, col 14, Use &#39;===&#39; to compare with &#39;null&#39;.

Let&#39;s say that you know what you&#39;re doing and want to disable the produced
warning but, in the same time, you&#39;re curious whether you have any variables
that were defined but never used. What you need to do, in this case, is to
enable two options: one relaxing that will suppress the 
=== null
 warning and
one enforcing that will enable checks for unused variables. In your case these
options are 
unused
 and 
eqnull
.

/*jshint unused:true, eqnull:true */
function main(a, b) {
 return a == null;
}

After that, JSHint will produce the following warning while linting this example
code:

demo.js: line 2, col 14, &#39;main&#39; is defined but never used.
demo.js: line 2, col 19, &#39;b&#39; is defined but never used.

Sometimes JSHint doesn&#39;t have an appropriate option that disables some
particular warning. In this case you can use 
jshint
 directive to disable
warnings by their code. Let&#39;s say that you have a file that was created by
combining multiple different files into one:

&quot;use strict&quot;;
/* ... */

// From another file
function b() {
 &quot;use strict&quot;;
 /* ... */
}

This code will trigger a warning about an unnecessary directive in function 
b
.
JSHint sees that there&#39;s already a global &quot;use strict&quot; directive and informs you
that all other directives are redundant. But you don&#39;t want to strip out these
directives since the file was auto-generated. The solution is to run JSHint
with a flag 
--verbose
 and note the warning code (W034 in this case):

$ jshint --verbose myfile.js
myfile.js: line 6, col 3, Unnecessary directive &quot;use strict&quot;. (W034)

Then, to hide this warning, just add the following snippet to your file:

/* jshint -W034 */

A couple things to note:

This syntax works only with warnings (code starts with 
W
), it doesn&#39;t work
with errors (code starts with 
E
).

This syntax will disable all warnings with this code. Some warnings are more
generic than others so be cautious.

To re-enable a warning that has been disabled with the above snippet you can
use:

/* jshint +W034 */

This is especially useful when you have code which causes a warning but that
you know is safe in the context. In these cases you can disable the warning as
above and then re-enable the warning afterwards:

var y = Object.create(null);
// ...
/*jshint -W089 */
for (var prop in y) {
 // ...
}
/*jshint +W089 */

This page
 contains a list of all options supported by JSHint.

Switch statements

By default JSHint warns when you omit 
break
 or 
return
 statements within
switch statements:

switch (cond) {
case &quot;one&quot;:
 doSomething(); // JSHint will warn about missing &#39;break&#39; here.
case &quot;two&quot;:
 doSomethingElse();
}

If you really know what you&#39;re doing you can tell JSHint that you intended the
case block to fall through by adding a 
/* falls through */
 comment:

switch (cond) {
case &quot;one&quot;:
 doSomething();
 /* falls through */
case &quot;two&quot;:
 doSomethingElse();
}