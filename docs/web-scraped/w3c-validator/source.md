# Source: https://validator.w3.org/source/

Title: Source Code Availability for The W3C Markup Validation Service

URL Source: https://validator.w3.org/source/

Markdown Content:
Source code and package availability

for the W3C Markup Validator
------------------------------------------------------------------

The W3C Markup Validator provides Perl/CGI/SGML/XML/DTD-based validation of a variety of document types. SGML and DTDs are older technologies that never found wide use on the Web, so for checking of HTML documents using modern technologies, you probably want to instead use the [W3C HTML Checker](https://validator.w3.org/nu/). To do that,

![Image 1: HTML5](https://validator.w3.org/images/HTML5_Badge_32.png)

*   Download the [latest release version](https://github.com/validator/validator/releases/latest).
*   Read the [usage guide](http://validator.github.io/validator/).

If for some reason you'd rather run a service based on the same source as the W3C Markup Validator, this page provides the following information:

*   [Installing from packages](https://validator.w3.org/source/#packages)
    *   [Fedora/Red Hat RPM package](https://validator.w3.org/source/#rpm)
    *   [openSUSE/SUSE Linux RPM package](https://validator.w3.org/source/#suse)
    *   [Debian GNU/Linux package](https://validator.w3.org/source/#deb)
    *   [Mac OS X Application](https://validator.w3.org/source/#mac)

*   [Getting the source](https://validator.w3.org/source/#getting)

### [](https://validator.w3.org/source/)Installing from packages

Rather than trying to install and run an instance of the W3C from the sources, it's much easier to install one of a variety of pre-built packages. The sections below provide information about packages available for various systems.

#### [](https://validator.w3.org/source/)Fedora/Red Hat RPM package

Fedora RPM packages of the validator are included in Fedora. The name of the validator package is w3c-markup-validator, use the standard automated package management tools of the distribution (such as yum) to install it along with its dependencies.

For Red Hat Enterprise Linux and derivative distributions, the w3c-markup-validator package is available in [EPEL](https://fedoraproject.org/wiki/EPEL).

#### [](https://validator.w3.org/source/)openSUSE/SUSE Linux RPM package

openSUSE/SUSE Linux RPM packages of the validator are available, courtesy of Sierk Bornemann, at software.openSUSE.org, <[http://software.opensuse.org/](http://software.opensuse.org/)>. Starting with openSUSE 10.3, the latest stable validator package and all its dependencies are included in the official stable openSUSE distribution. The name of the validator package is w3c-markup-validator, use the standard automated package management tools of the distribution (such as _YaST_, _zypper_, _smart_, _apt4rpm_ or _yum_) to install it along with its dependencies.

Additionally, you can also get these and other needed packages from the openSUSE Software Repository at <[http://software.opensuse.org/package/w3c-markup-validator](http://software.opensuse.org/package/w3c-markup-validator)>

#### [](https://validator.w3.org/source/)Debian GNU/Linux package

[A Debian package is available](https://packages.debian.org/search?keywords=w3c-markup-validator), courtesy of Frédéric Schütz.

Starting with Debian 3.1 ("Sarge"), the package and all its dependencies are included in the official Debian distribution, and can be installed by running the command apt-get install w3c-markup-validator as root.

#### Mac OS X Application

The Validator is also packaged as a standalone Mac OS X Application, called [Validator S.A.C.](http://habilis.net/validator-sac/), courtesy of [Chuck Houpt](http://habilis.net/chuck/ "Chuck Houpt's Home Page").

### [](https://validator.w3.org/source/)Getting the source

[](https://validator.w3.org/source/) The source code for the [W3C Markup Validation Service](https://validator.w3.org/) is available under the terms of the [W3C Software License](http://www.w3.org/Consortium/Legal/copyright-software).

If you just want to glance at the code, or see its revision history, you can [browse it directly in Github](https://github.com/w3c/markup-validator/).

The most interesting files are currently [a CGI script called "check"](https://github.com/w3c/markup-validator/blob/master/httpd/cgi-bin/check) that does pretty much everything, and possibly also [the httpd.conf configuration file snippet for Apache](https://github.com/w3c/markup-validator/blob/master/httpd/conf/httpd.conf). Select the topmost revision numbers on these pages to see the most recent revision of each file.

To actually install and run an instance of the W3C Markup Validator from the sources, see the [installation manual](https://validator.w3.org/docs/install.html).
