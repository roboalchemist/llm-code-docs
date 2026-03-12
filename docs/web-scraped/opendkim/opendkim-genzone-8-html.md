# Source: http://www.opendkim.org/opendkim-genzone.8.html

Title: opendkim-genzone

URL Source: http://www.opendkim.org/opendkim-genzone.8.html

Markdown Content:
[NAME](http://www.opendkim.org/opendkim-genzone.8.html#NAME)

[SYNOPSIS](http://www.opendkim.org/opendkim-genzone.8.html#SYNOPSIS)

[DESCRIPTION](http://www.opendkim.org/opendkim-genzone.8.html#DESCRIPTION)

[OPTIONS](http://www.opendkim.org/opendkim-genzone.8.html#OPTIONS)

[VERSION](http://www.opendkim.org/opendkim-genzone.8.html#VERSION)

[COPYRIGHT](http://www.opendkim.org/opendkim-genzone.8.html#COPYRIGHT)

[SEE ALSO](http://www.opendkim.org/opendkim-genzone.8.html#SEE%20ALSO)

* * *

[](http://www.opendkim.org/opendkim-genzone.8.html)
NAME
----

**opendkim-genzone** − DKIM public key zone file generation tool

[](http://www.opendkim.org/opendkim-genzone.8.html)
SYNOPSIS
--------

**opendkim-genzone** [−C address] [−d domain] [−D] [−E secs] [−F] [−N ns[,...]] [−o file] [−r secs] [−R secs] [−S] [−t secs] [−T secs] [−u] [−v] [−x conffile] [dataset]

[](http://www.opendkim.org/opendkim-genzone.8.html)
DESCRIPTION
-----------

**opendkim-genzone** generates a file suitable for use with _named(8)_ to publish a set of public keys.

The _dataset_ parameter should specify a set of data as described in the _opendkim(8)_ man page. It can currently refer to flat files, Sleepycat databases, comma-separated lists, LDAP directories or SQL databases. The _dataset_ may be omitted if a configuration file (via the _−x_ command line flag) is specified referring to a configuration file that sets a _KeyTable_ parameter, in which case that value will be used.

The database contents should be formatted as described for the _KeyTable_ parameter, described in the _opendkim.conf(5)_ man page.

[](http://www.opendkim.org/opendkim-genzone.8.html)
OPTIONS
-------

_−C contact_

Uses _contact_ as the contact information to be used when an SOA record is generated (see _−S_ below). If not specified, the userid of the executing user and the local hostname will be used; if the executing user can’t be determined, "hostmaster" will be used.

_−d domain_

Restricts output to those records for which the domain field is the specified _domain._

_−D_ Adds a "._domainkey" suffix to selector names in the zone file.

_−E secs_

When generating an SOA record (see _−S_ below), use _secs_ as the default record expiration time. The default is 604800.

_−F_ Adds a "._domainkey" suffix and the domainname to selector names in the zone file.

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

_−u_ Produce output suitable for use as input to **nsupdate(8).**
_−v_ Increases the verbosity of debugging output written to standard error.

_−x conffile_

Names an _opendkim.conf(5)_ file to be read for LDAP-specific parameters when an LDAP dataset is given on the command line. Not required for other dataset types. The default is _@SYSCONFDIR@/opendkim.conf._

[](http://www.opendkim.org/opendkim-genzone.8.html)
VERSION
-------

This man page covers the version of _opendkim-genzone_ that shipped with version @VERSION@ of _OpenDKIM._

[](http://www.opendkim.org/opendkim-genzone.8.html)
COPYRIGHT
---------

Copyright (c) 2010, 2012, 2014, The Trusted Domain Project. All rights reserved.

[](http://www.opendkim.org/opendkim-genzone.8.html)
SEE ALSO
--------

_nsupdate(8), opendkim(8), opendkim.conf(5)_

* * *
