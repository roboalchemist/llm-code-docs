# Source: http://www.opendkim.org/opendkim-spam.1.html

Title: opendkim-spam

URL Source: http://www.opendkim.org/opendkim-spam.1.html

Markdown Content:
[NAME](http://www.opendkim.org/opendkim-spam.1.html#NAME)

[SYNOPSIS](http://www.opendkim.org/opendkim-spam.1.html#SYNOPSIS)

[DESCRIPTION](http://www.opendkim.org/opendkim-spam.1.html#DESCRIPTION)

[OPTIONS](http://www.opendkim.org/opendkim-spam.1.html#OPTIONS)

[CONFIGURATION FILE](http://www.opendkim.org/opendkim-spam.1.html#CONFIGURATION%20FILE)

[NOTES](http://www.opendkim.org/opendkim-spam.1.html#NOTES)

[VERSION](http://www.opendkim.org/opendkim-spam.1.html#VERSION)

[COPYRIGHT](http://www.opendkim.org/opendkim-spam.1.html#COPYRIGHT)

[SEE ALSO](http://www.opendkim.org/opendkim-spam.1.html#SEE%20ALSO)

* * *

[](http://www.opendkim.org/opendkim-spam.1.html)
NAME
----

**opendkim-spam** − DKIM filter spam correlation tool

[](http://www.opendkim.org/opendkim-spam.1.html)
SYNOPSIS
--------

**opendkim-spam** [options]

[](http://www.opendkim.org/opendkim-spam.1.html)
DESCRIPTION
-----------

**opendkim-spam** accepts a regular format message (RFC5322) on standard input and uses it to update a local SQL database being updated by _opendkim(8)_ with an indiciation that a user believes the input message is spam or otherwise abusive. This feedback is important input toward developing DKIM-based domain reputation systems.

The tool is intended to be used directly from within shell-based mail readers such as _alpine(1)_ or _mutt(1)_ using a "pipe" command, which feeds the message being read to the specified program.

This tool is experimental. If the experiment proves useful, the feedback could be used as an input stream to a larger-scale collaborative feedback system that can be used to identify sources of signed mail that have good reputations.

[](http://www.opendkim.org/opendkim-spam.1.html)
OPTIONS
-------

_-b backend_

Specifies the style of backend database in use. The default is "@SQL_BACKEND@".

_-c file_

Names a configuration file from which operating parameters will be read. The configuration file contains entries of the form "key value", one per line. Empty lines or lines beginning with a hash ("#") character are ignored. Command line equivalents for the configuration file are available as runtime overrides. The default configuration file location is _@SYSCONFDIR@/opendkim-spam.conf._ See the CONFIGURATION FILE section for a list of known values.

_-f_ Run in the foreground rather than executing as a background process. Intended mainly for debugging.

_-d name_

Indicates the name of the database to be accessed. The default is "opendkim".

_-h host_

Specifies the host where the database server is running. The default is "localhost".

_-o file_

Writes an update record to an OpenDKIM statistics file rather than directly to a database. There is no default. Note that if this option is used, all database-specific options are ignored.

_-p password_

Specifies the password to be used when authenticating to the database. The default is "opendkim".

_-P port_

Specifies the port number where the database server is listening. The default depends on which backend is in use.

_-r reporter_

Provides the name of the site reporting the spam. If not provided, an attempt will be made to extract this information from the topmost Received header field from the input message.

_-s column_

Names the database column whose value should be incremented as a result of this user action. The default is "spam".

_-u user_

Identifies the database user to be used when connecting to the database. The default is "opendkim".

_-v_ Requests verbose output. Can be specified multiple times for more and more information.
_-V_ Print version number and exit.
[](http://www.opendkim.org/opendkim-spam.1.html)
CONFIGURATION FILE
------------------

The configuration file used by **opendkim-spam(1)** is expected to be a text file. Empty lines or lines starting with a hash ("#") character are ignored. All other lines should consist of a parameter name followed by one or more whitespace characters, then followed by its intended value.

Parameters generally match command line options (specified above), but when present the command line options override the configuration file options. The list of configuration file parameters and their command line equivalents are as follows; see above for descriptions: _Background_

−f (opposite meaning)

_DatabaseBackend_

−b

_DatabaseName_

−d

_DatabaseHost_

−h

_DatabasePassword_

−p

_DatabasePort_

−P

_DatabaseSpamColumn_

−s

_DatabaseUser_

−u

_ReporterID_

−r

_SkipReceived_

An integer that defines a number of Received fields that should be skipped while searching for the one that was also seen by **opendkim(8)** so that this command refers to the same Received field. Defaults to 0.

_StatisticsFile_

−o

[](http://www.opendkim.org/opendkim-spam.1.html)
NOTES
-----

It is possible to compile this application without SQL support, in which case only the _StatisticsFile_ setting has any meaning (and, in fact, it is required in that case).

[](http://www.opendkim.org/opendkim-spam.1.html)
VERSION
-------

This man page covers the version of _opendkim-spam_ that shipped with version @VERSION@ of _OpenDKIM._

[](http://www.opendkim.org/opendkim-spam.1.html)
COPYRIGHT
---------

Copyright (c) 2011, 2012, The Trusted Domain Project. All rights reserved.

[](http://www.opendkim.org/opendkim-spam.1.html)
SEE ALSO
--------

_alpine(1), mutt(1), opendkim(8)_

RFC6376 - DomainKeys Identified Mail

* * *
