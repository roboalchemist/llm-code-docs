# Source: http://www.opendkim.org/opendkim-genkey.8.html

Title: opendkim-genkey

URL Source: http://www.opendkim.org/opendkim-genkey.8.html

Markdown Content:
[NAME](http://www.opendkim.org/opendkim-genkey.8.html#NAME)

[SYNOPSIS](http://www.opendkim.org/opendkim-genkey.8.html#SYNOPSIS)

[DESCRIPTION](http://www.opendkim.org/opendkim-genkey.8.html#DESCRIPTION)

[OPTIONS](http://www.opendkim.org/opendkim-genkey.8.html#OPTIONS)

[NOTES](http://www.opendkim.org/opendkim-genkey.8.html#NOTES)

[VERSION](http://www.opendkim.org/opendkim-genkey.8.html#VERSION)

[COPYRIGHT](http://www.opendkim.org/opendkim-genkey.8.html#COPYRIGHT)

[SEE ALSO](http://www.opendkim.org/opendkim-genkey.8.html#SEE%20ALSO)

* * *

[](http://www.opendkim.org/opendkim-genkey.8.html)
NAME
----

**opendkim-genkey** − DKIM filter key generation tool

[](http://www.opendkim.org/opendkim-genkey.8.html)
SYNOPSIS
--------

**opendkim-genkey** [options]

[](http://www.opendkim.org/opendkim-genkey.8.html)
DESCRIPTION
-----------

**opendkim-genkey** generates (1) a private key for signing messages using _opendkim(8)_ and (2) a DNS TXT record suitable for inclusion in a zone file which publishes the matching public key for use by remote DKIM verifiers.

The filenames of these are based on the selector (see below); the private key will have a suffix of ".private" and the TXT record will have a suffix of ".txt".

Both long and short names are supported for most options.

[](http://www.opendkim.org/opendkim-genkey.8.html)
OPTIONS
-------

_−a_(−−append-domain) Appends the domain name (see −d below) to the label in the generated TXT record, followed by a trailing period. By default it is assumed the domain name is implicit from the context of the zone file, and is therefore not included in the output.

_−b bits_

(−−bits=n) Specifies the size of the key, in _bits,_ to be generated. The default is 1024 which is the value recommended by the DKIM specification.

_−d domain_

(−−domain=string) Names the _domain_ which will use this key for signing. Currently only used in a comment in the TXT record file. The default is "@DOMAIN@".

_−D directory_

(−−directory=path) Instructs the tool to change to the named _directory_ prior to creating files. By default the current directory is used.

_−h algorithms_

(−−hash-algorithms=name[:name[...]]) Specifies a list of hash _algorithms_ which can be used with this key. By default all hash algorithms are allowed.

_−−help_ Print a help message and exit.

_−n note_

(−−note=string) Includes arbitrary _note_ text in the key record. By default, no such text is included.

_−r_(−−restricted) Restricts the key for use in e-mail signing only. The default is to allow the key to be used for any service.

_−s selector_

(−−selector=name) Specifies the _selector,_ or name, of the key pair generated. The default is "default".

_−S_(−−[no]subdomains) Disallows subdomain signing by this key. By default the key record will be generated such that verifiers are told subdomain signing is permitted. Note that for backward compatibility reasons, _−S_ means the same as _−−nosubdomains._
_−t_(−−[no]testmode) Indicates the generated key record should be tagged such that verifiers are aware DKIM is in test at the signing domain.
_-v_(−−verbose) Increase verbose output.
_-V_(−−version) Print version number and exit.
[](http://www.opendkim.org/opendkim-genkey.8.html)
NOTES
-----

Requires that the _openssl(8)_ binary be installed and in the executing shell’s search path.

[](http://www.opendkim.org/opendkim-genkey.8.html)
VERSION
-------

This man page covers the version of _opendkim-genkey_ that shipped with version @VERSION@ of _OpenDKIM._

[](http://www.opendkim.org/opendkim-genkey.8.html)
COPYRIGHT
---------

Copyright (c) 2007, 2008 Sendmail, Inc. and its suppliers. All rights reserved.

Copyright (c) 2009, 2011-2013, The Trusted Domain Project. All rights reserved.

[](http://www.opendkim.org/opendkim-genkey.8.html)
SEE ALSO
--------

_opendkim(8), openssl(8)_

RFC6376 - DomainKeys Identified Mail

* * *
