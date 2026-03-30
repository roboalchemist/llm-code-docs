# Source: http://www.opendkim.org/opendkim-atpszone.8.html

Title: opendkim-atpszone

URL Source: http://www.opendkim.org/opendkim-atpszone.8.html

Markdown Content:
[NAME](http://www.opendkim.org/opendkim-atpszone.8.html#NAME)

[SYNOPSIS](http://www.opendkim.org/opendkim-atpszone.8.html#SYNOPSIS)

[DESCRIPTION](http://www.opendkim.org/opendkim-atpszone.8.html#DESCRIPTION)

[OPTIONS](http://www.opendkim.org/opendkim-atpszone.8.html#OPTIONS)

[VERSION](http://www.opendkim.org/opendkim-atpszone.8.html#VERSION)

[COPYRIGHT](http://www.opendkim.org/opendkim-atpszone.8.html#COPYRIGHT)

[SEE ALSO](http://www.opendkim.org/opendkim-atpszone.8.html#SEE%20ALSO)

* * *

[](http://www.opendkim.org/opendkim-atpszone.8.html)
NAME
----

**opendkim-atpszone** − DKIM ATPS zone file generation tool

[](http://www.opendkim.org/opendkim-atpszone.8.html)
SYNOPSIS
--------

**opendkim-atpszone** [−A] [−C address] [−E secs] [−h hash] [−N ns[,...]] [−o file] [−r secs] [−R secs] [−S] [−t secs] [−T secs] [−u domain] [−v] [dataset]

[](http://www.opendkim.org/opendkim-atpszone.8.html)
DESCRIPTION
-----------

**opendkim-atpszone** generates a file suitable for use with _named(8)_ to publish a set of domains authorized as third-party signers for a local domain.

The _dataset_ parameter should specify a set of data as described in the _opendkim(8)_ man page. It can currently refer to flat files, Sleepycat databases, comma-separated lists, LDAP directories or SQL databases. The keys in the named database are assumed to comprise a set of domains that are to be advertised using the experimental Authorized Third-Party Signers protocol as permitted to sign mail using DKIM on behalf of the local domain. Values in the database are not used.

[](http://www.opendkim.org/opendkim-atpszone.8.html)
OPTIONS
-------

_−A_ Adds a "._atps" suffix to records in the zone file.

_−C contact_

Uses _contact_ as the contact information to be used when an SOA record is generated (see _−S_ below). If not specified, the userid of the executing user and the local hostname will be used; if the executing user can’t be determined, "hostmaster" will be used.

_−E secs_

When generating an SOA record (see _−S_ below), use _secs_ as the default record expiration time. The default is 604800.

_−h hash_

Specifies which SHA hash algorithm to use. Must be one of "none", "sha1" and "sha256", with "sha256" being the default if it is available.

_−N nslist_

Specifies a comma-separated list of nameservers, which will be output in NS records before the TXT records. The first nameserver in this list will also be used in the SOA record (if _−S_ is also specified) as the authority hostname.

_−o file_

Sends output to the named _file_ rather than standard output.

_−r secs_

When generating an SOA record (see _−S_ below), use _secs_ as the zone refresh time. The default is 10800.

_−R secs_

When generating an SOA record (see _−S_ below), use _secs_ as the zone retry time. The default is 1800.

_−S_ Asks for an SOA record to be generated at the top of the output. The content of this output can be controlled using the _−E, −r, −R, −T_ options. The serial number will be generated based on the current time of day.
_−t ttl_ Puts a TTL (time-to-live) value of _ttl_ on all records output. The units are in seconds.

_−T secs_

When generating an SOA record (see _−S_ below), use _secs_ as the default record TTL time. The default is 86400.

_−u domain_

Produce output suitable for use as input to **nsupdate(8)** to add ATPS records to the named _domain._

_−v_ Increases the verbosity of debugging output written to standard error.
[](http://www.opendkim.org/opendkim-atpszone.8.html)
VERSION
-------

This man page covers the version of _opendkim-atpszone_ that shipped with version @VERSION@ of _OpenDKIM._

[](http://www.opendkim.org/opendkim-atpszone.8.html)
COPYRIGHT
---------

Copyright (c) 2011, 2012, The Trusted Domain Project. All rights reserved.

[](http://www.opendkim.org/opendkim-atpszone.8.html)
SEE ALSO
--------

_nsupdate(8), opendkim(8), opendkim.conf(5)_

* * *
