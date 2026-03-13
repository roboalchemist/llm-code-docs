# Source: http://michaelherold.github.io/pyIsEmail

Title: pyIsEmail by michaelherold

URL Source: http://michaelherold.github.io/pyIsEmail

Markdown Content:
[](http://michaelherold.github.io/pyIsEmail#getting-started)Getting Started
---------------------------------------------------------------------------

pyIsEmail is a no-nonsense approach for checking whether that user-supplied email address could be real. Sick of not being able to use [email address tagging](http://en.wikipedia.org/wiki/Email_address#Address_tags) to sort through your [Bacn](http://en.wikipedia.org/wiki/Bacn)? We can fix that.

Regular expressions are cheap to write, but often require maintenance when new top-level domains come out or don't conform to email addressing features that come back into vogue. pyIsEmail allows you to validate an email address -- and even check the domain, if you wish -- with one simple call, making your code more readable and faster to write. When you want to know why an email address doesn't validate, we even provide you with a diagnosis.

[](http://michaelherold.github.io/pyIsEmail#install)Install
-----------------------------------------------------------

Install from PyPI using [pip](http://www.pip-installer.org/en/latest/), a package manager for Python.

```
$ pip install pyIsEmail
```

Don't have pip installed? Try installing it, by running this from the command line:

```
$ curl https://raw.github.com/pypa/pip/master/contrib/get-pip.py | python
```

Or, you can [download the source code (zip)](https://github.com/michaelherold/pyIsEmail/zipball/develop) for `pyIsEmail`, and then run:

```
$ python setup.py install
```

You may need to run the above commands with `sudo`.

[](http://michaelherold.github.io/pyIsEmail#usage)Usage
-------------------------------------------------------

For the simplest usage, import and use the `is_email` function:

from pyisemail import is_email

address = "test@example.com"
bool_result = is_email(address)
detailed_result = is_email(address, diagnose=True)

You can also check whether the domain used in the email is a valid domain and whether or not it has a valid MX record:

from pyisemail import is_email

address = "test@example.com"
bool_result_with_dns = is_email(address, check_dns=True)
detailed_result_with_dns = is_email(address, check_dns=True, diagnose=True)

These are primary indicators of whether an email address can even be issued at that domain. However, a valid response here _is not a guarantee that the email exists_, merely that is _can_ exist.

In addition to the base `is_email` functionality, you can also use the validators by themselves. Check the validator source code to see how this works.

[](http://michaelherold.github.io/pyIsEmail#uninstall)Uninstall
---------------------------------------------------------------

Want to get rid of pyIsEmail? Did you install with pip? Here you go:

```
$ pip uninstall pyIsEmail
```

[](http://michaelherold.github.io/pyIsEmail#acknowledgments)Acknowledgments
---------------------------------------------------------------------------

The base `ParserValidator` is based off of [Dominic Sayers](https://github.com/dominicsayers)' [is_email script](https://github.com/dominicsayers/isemail). I wanted the functionality in Python, so I ported it from the original PHP.

[](http://michaelherold.github.io/pyIsEmail#contributing)Contributing
---------------------------------------------------------------------

1.   Fork it
2.   Create your feature branch (`git checkout -b my-new-feature`)
3.   Commit your changes (`git commit -am 'Add some feature'`)
4.   Push to the branch (`git push origin my-new-feature`)
5.   Create new Pull Request

[](http://michaelherold.github.io/pyIsEmail#versioning)Versioning
-----------------------------------------------------------------

This library aims to adhere to [Semantic Versioning 2.0.0](http://semver.org/). Violations of this scheme should be reported as bugs.

[](http://michaelherold.github.io/pyIsEmail#copyright)Copyright
---------------------------------------------------------------

Copyright (c) 2013 Michael Herold. See LICENSE for details.
