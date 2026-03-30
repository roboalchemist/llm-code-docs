# Source: https://gpiozero.readthedocs.io/en/stable/contributing.html

Title: 12. Contributing — gpiozero 2.0.1 Documentation

URL Source: https://gpiozero.readthedocs.io/en/stable/contributing.html

Markdown Content:
Contributions to the library are welcome! Here are some guidelines to follow.

12.1. Suggestions[](https://gpiozero.readthedocs.io/en/stable/contributing.html#suggestions "Link to this heading")
--------------------------------------------------------------------------------------------------------------------

Please make suggestions for additional components or enhancements to the codebase by opening an [issue](https://github.com/gpiozero/gpiozero/issues/new) explaining your reasoning clearly.

12.2. Bugs[](https://gpiozero.readthedocs.io/en/stable/contributing.html#bugs "Link to this heading")
------------------------------------------------------------------------------------------------------

Please submit bug reports by opening an [issue](https://github.com/gpiozero/gpiozero/issues/new) explaining the problem clearly using code examples.

12.3. Documentation[](https://gpiozero.readthedocs.io/en/stable/contributing.html#documentation "Link to this heading")
------------------------------------------------------------------------------------------------------------------------

The documentation source lives in the [docs](https://github.com/gpiozero/gpiozero/tree/master/docs) folder. Contributions to the documentation are welcome but should be easy to read and understand.

12.4. Commit messages and pull requests[](https://gpiozero.readthedocs.io/en/stable/contributing.html#commit-messages-and-pull-requests "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------------------------

Commit messages should be concise but descriptive, and in the form of a patch description, i.e. instructional not past tense (“Add LED example” not “Added LED example”).

Commits which close (or intend to close) an issue should include the phrase “fix #123” or “close #123” where `#123` is the issue number, as well as include a short description, for example: “Add LED example, close #123”, and pull requests should aim to match or closely match the corresponding issue title.

Copyrights on submissions are owned by their authors (we don’t bother with copyright assignments), and we assume that authors are happy for their code to be released under the project’s [license](https://gpiozero.readthedocs.io/en/stable/license.html). Do feel free to add your name to the list of contributors in `README.rst` at the top level of the project in your pull request! Don’t worry about adding your name to the copyright headers in whatever files you touch; these are updated automatically from the git metadata before each release.

12.5. Backwards compatibility[](https://gpiozero.readthedocs.io/en/stable/contributing.html#backwards-compatibility "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------

Since this library reached v1.0 we aim to maintain backwards-compatibility thereafter. Changes which break backwards-compatibility will not be accepted.

12.6. Python 2/3[](https://gpiozero.readthedocs.io/en/stable/contributing.html#python-2-3 "Link to this heading")
------------------------------------------------------------------------------------------------------------------

The library is 100% compatible with both Python 2.7 and Python 3 from version 3.2 onwards. Since Python 2 is now past its [end-of-life](http://legacy.python.org/dev/peps/pep-0373/), the 1.6.2 release (2021-03-18) is the last to support Python 2.
