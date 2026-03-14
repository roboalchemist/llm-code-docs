# Source: http://www.opendkim.org/opendkim-testkey.8.html

Title: opendkim-testkey

URL Source: http://www.opendkim.org/opendkim-testkey.8.html

Markdown Content:
[NAME](http://www.opendkim.org/opendkim-testkey.8.html#NAME)

[SYNOPSIS](http://www.opendkim.org/opendkim-testkey.8.html#SYNOPSIS)

[DESCRIPTION](http://www.opendkim.org/opendkim-testkey.8.html#DESCRIPTION)

[OPTIONS](http://www.opendkim.org/opendkim-testkey.8.html#OPTIONS)

[NOTES](http://www.opendkim.org/opendkim-testkey.8.html#NOTES)

[VERSION](http://www.opendkim.org/opendkim-testkey.8.html#VERSION)

[COPYRIGHT](http://www.opendkim.org/opendkim-testkey.8.html#COPYRIGHT)

[SEE ALSO](http://www.opendkim.org/opendkim-testkey.8.html#SEE%20ALSO)

* * *

[](http://www.opendkim.org/opendkim-testkey.8.html)
NAME
----

**opendkim-testkey** − DKIM filter installation test

[](http://www.opendkim.org/opendkim-testkey.8.html)
SYNOPSIS
--------

**opendkim-testkey** [−d domain] [−s selector] [−k keypath] [−v] [−x configfile]

[](http://www.opendkim.org/opendkim-testkey.8.html)
DESCRIPTION
-----------

**opendkim-testkey** verifies the setup of signing and verifying (private and public) keys for use with _opendkim(8)._

The test program will read a domain name and selector from the command line, configuration file or a key table, then query and parse the resulting DKIM key(s), reporting any errors found.

If a key path is also provided, the test program will read the private key named and attempt to confirm that the private key specified by _keypath_ (or in the key table) and the public DKIM key retrieved match.

[](http://www.opendkim.org/opendkim-testkey.8.html)
OPTIONS
-------

_-d domain_

Names the domain in which signing is to be done. More specifically, names the domain in which the public key matching the provided private key will be found. This parameter must be provided either explicitly, or in the configuration file, or via a KeyTable (see _opendkim.conf(5)_ for details).

_-k keypath_

Specifies the path to the private key file which should be used for this test. This parameter is optional

_-s selector_

Names the selector within the specified domain whose public key should be retrieved and tested, comparing it to the private key if provided. This parameter must be provided either explicitly, or in the configuration file, or via a KeyTable (see _opendkim.conf(5)_ for details).

_-v_ Increases the amount of output (verbosity) of the program. May be specified multiple times for increased output.

_-x conffile_

Names a configuration file to be parsed. See the _opendkim.conf(5)_ man page for details. The only values used are Domain, Selector, KeyFile, KeyTable, TrustAnchorFile and ResolverConfig. The default is _@SYSCONFDIR@/opendkim.conf._

[](http://www.opendkim.org/opendkim-testkey.8.html)
NOTES
-----

The test program will also complain if a private key file is readable by anyone other than the user executing the program.

[](http://www.opendkim.org/opendkim-testkey.8.html)
VERSION
-------

This man page covers the version of _opendkim-testkey_ that shipped with version @VERSION@ of _OpenDKIM._

[](http://www.opendkim.org/opendkim-testkey.8.html)
COPYRIGHT
---------

Copyright (c) 2007, 2008, Sendmail, Inc. and its suppliers. All rights reserved.

Copyright (c) 2009-2012, The Trusted Domain Project. All rights reserved.

[](http://www.opendkim.org/opendkim-testkey.8.html)
SEE ALSO
--------

_opendkim(8)_

RFC6376 - DomainKeys Identified Mail

* * *
