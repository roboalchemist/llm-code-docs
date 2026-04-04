# Source: https://jshint.com/docs/reporters/

Writing your own JSHint reporter

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

Writing your own JSHint reporter

JSHint Reporter is a JavaScript file that accepts raw data from JSHint and
outputs something into the console (or another file, or sends an email; it&#39;s
really up to you).

Here&#39;s the simplest reporter, the one that prints 
OK
 if JSHint passed the file
and 
FAIL
 if it didn&#39;t:

module.exports = {
 reporter: function (errors) {
 console.log(errors.length ? &quot;FAIL&quot; : &quot;OK&quot;);
 }
};

Each reporter file must expose one function, 
reporter
, that accepts an array
of errors. Each entry of this array has the following structure:

{
 file: [string, filename]
 error: {
 id: [string, usually &#39;(error)&#39;],
 code: [string, error/warning code],
 reason: [string, error/warning message],
 evidence: [string, a piece of code that generated this error]
 line: [number]
 character: [number]
 scope: [string, message scope;
 usually &#39;(main)&#39; unless the code was eval&#39;ed]

 [+ a few other legacy fields that you don&#39;t need to worry about.]
 }
}

And a real-world example:

[
 {
 file: &#39;demo.js&#39;,
 error: {
 id: &#39;(error)&#39;,
 code: &#39;W117&#39;,
 reason: &#39;\&#39;module\&#39; is not defined.&#39;
 evidence: &#39;module.exports = {&#39;,
 line: 3,
 character: 1,
 scope: &#39;(main)&#39;,

 // [...]
 }
 },

 // [...]
]

If you&#39;re still confused, JSHint repository has

an example reporter
.