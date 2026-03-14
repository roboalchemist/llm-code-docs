# Source: https://validator.w3.org/docs/devel.html

Title: Developer Documentation for The W3C Markup Validation Service

URL Source: https://validator.w3.org/docs/devel.html

Markdown Content:
Installation and development information 

for the W3C Markup Validator
-----------------------------------------------------------------------

### Table of Contents

*   [Participate](https://validator.w3.org/docs/devel.html#participate)
*   [Development Framework](https://validator.w3.org/docs/devel.html#devel-frame)
    *   [Bugs and Issue Tracking](https://validator.w3.org/docs/devel.html#bug)
    *   [Test suite](https://validator.w3.org/docs/devel.html#test)
    *   [TODO](https://validator.w3.org/docs/devel.html#todo)

[](https://validator.w3.org/docs/devel.html) This document is an overview of how developers can modify the Markup Validator, and how to contribute to the development of the project. It is intended for system administrators and developers. **This is not end user documentation**. See the [User Manual](https://validator.w3.org/docs/users.html) for usage instructions.

### [](https://validator.w3.org/docs/devel.html)Participating in the development of the Markup Validator

The Markup Validator is managed as an open source project by a [team of volunteer developers and people from the W3C Team](http://www.w3.org/QA/Tools/qa-dev/).

Help on this project is always welcome, usually as [feedback](https://validator.w3.org/feedback.html), but developers may also be interested in working directly on the code, which is certainly encouraged.

This document tries to give a general overview of the development framework for the Markup Validator, and should help developers get a good idea of how the project is managed.

The next steps would certainly be to read about [source availability](https://validator.w3.org/source/) and then try a [local installation](https://validator.w3.org/docs/install.html) of the validator, if not done yet. We also (obviously) recommend to get in touch with other developers, either through [regular means](https://validator.w3.org/feedback.html), or on the IRC channel #validator on irc.freenode.net where many developers and contributors often are.

### [](https://validator.w3.org/docs/devel.html)Development Framework

#### [](https://validator.w3.org/docs/devel.html)Bug and Issue Tracking System

Bug and Issue Tracking for the Validator happens in the [issue tracker](https://github.com/w3c/markup-validator/issues). Developers should feel free to set up an account and report bugs, enhancement requests, patches, etc. directly there (end users should continue to send reports and ideas to the [mailing list](http://lists.w3.org/Archives/Public/www-validator/)).

#### [](https://validator.w3.org/docs/devel.html)Test suite

Any changes to the service will attempt to maintain compatibility with a [list of test cases](https://validator.w3.org/dev/tests/).

The validator has an [automated test suite](http://dvcs.w3.org/hg/markup-validator/file/tip/misc/testsuite/) which is used frequently to check that no change has broken any feature or resurfaced a bug. Whenever possible, join a _test case_ with your patches.

_example_: for a patch for the detection of document encoding in the <head>, join as a test case a simple HTML document with encoding information in the <head>, and another document without.

#### [](https://validator.w3.org/docs/devel.html)TODO

The TODO list for the Validator is online at <[https://validator.w3.org/todo.html](https://validator.w3.org/todo.html)>. This is probably the best place to start.

However this list is by no means comprehensive. Feel free to suggest other features that should be on this list or send patches for your favourite feature.

Keep in mind that features should be of general utility and that the point if the validator is that it does an _objective_ validation instead of just what some random developer happens to think is a Good Idea®. While extra features are nice, they shouldn't dilute the value of the validator as an objective check.
