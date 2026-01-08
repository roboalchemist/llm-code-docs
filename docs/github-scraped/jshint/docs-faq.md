# Source: https://jshint.com/docs/faq/

FAQ

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

Frequently Asked Questions

Can I use multiple reporters at the same time?

Yes, you may do so by authoring a new reporter that composes the reporters you
are interested in using.

For example, to use reporters named 
first-reporter
 and 
second-reporter
,
create a new module that invokes them both:

var first = require(&#39;first-reporter&#39;);
var second = require(&#39;second-reporter&#39;);

exports.reporter = function(results, data, opts) {
 first.reporter(results, data, opts);
 second.reporter(results, data, opts);
};

Save that to a file named 
dual-reporter.js
, and run JSHint with:

$ jshint --reporter ./dual-reporter.js

...and you should see the output of 
first-reporter
 followed by the output of

second-reporter
.

This approach is especially well-suited to using the different reporters&#39;
output in different contexts (for instance, e-mailing one reporter&#39;s output to
the development team and feeding another reporter&#39;s output to a continuous
integration system). You might output a custom delimiter between the output
streams in order to demultiplex them. Alternatively, you might replace the
global 
process.stdout
 value with another stream between reporter invocations.
This latter solution is somewhat fragile because it involves mutating global
state--a future release of JSHint may expose a safer mechanism for this
operation.

See 
the documentation on JSHint&#39;s &quot;reporter&quot;
API
 for more details on creating your own
reporter.

JSHint skips some unused variables

If your code looks like this:

function test(a, b, c) {
 return c;
}

Then JSHint will not warn about unused variables 
a
 and 
b
 if you set the

unused
 option to 
true
. It figures that if unused arguments are followed
by used ones, it was a conscious decision and not a typo. If you want to
warn about all unused variables not matter where they appear, set the 
unused

option to 
strict
:

/*jshint unused:strict */
function test(a, b, c) {
 return c;
}

// Warning: unused variable &#39;a&#39;
// Warning: unused variable &#39;b&#39;

For more information see: 
options/unused
.