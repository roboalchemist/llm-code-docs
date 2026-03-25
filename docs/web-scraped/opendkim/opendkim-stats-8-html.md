# Source: http://www.opendkim.org/opendkim-stats.8.html

Title: OPENDKIM-STATS

URL Source: http://www.opendkim.org/opendkim-stats.8.html

Markdown Content:
[NAME](http://www.opendkim.org/opendkim-stats.8.html#NAME)

[SYNOPSIS](http://www.opendkim.org/opendkim-stats.8.html#SYNOPSIS)

[DESCRIPTION](http://www.opendkim.org/opendkim-stats.8.html#DESCRIPTION)

[SEE ALSO](http://www.opendkim.org/opendkim-stats.8.html#SEE%20ALSO)

[VERSION](http://www.opendkim.org/opendkim-stats.8.html#VERSION)

* * *

[](http://www.opendkim.org/opendkim-stats.8.html)
NAME
----

**opendkim-stats** − output opendkim statistics

[](http://www.opendkim.org/opendkim-stats.8.html)
SYNOPSIS
--------

**opendkim-stats**_file_

[](http://www.opendkim.org/opendkim-stats.8.html)
DESCRIPTION
-----------

The **opendkim-stats** utility reads from an _opendkim_ statistics database and dumps the data therein to standard output. It takes as its only argument the path to this database. The _opendkim_ statistics gathering is disabled by default, but can be enabled through a _Statistics_ entry in _@SYSCONFDIR@/opendkim.conf._

See the _opendkim.conf(5)_ man page for details.

[](http://www.opendkim.org/opendkim-stats.8.html)
SEE ALSO
--------

_opendkim(8), opendkim.conf(5)_

[](http://www.opendkim.org/opendkim-stats.8.html)
VERSION
-------

This man page covers the _opendkim-stats_ that shipped with version @VERSION@ of _OpenDKIM._

* * *
