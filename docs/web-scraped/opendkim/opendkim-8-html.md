# Source: http://www.opendkim.org/opendkim.8.html

Title: opendkim

URL Source: http://www.opendkim.org/opendkim.8.html

Markdown Content:
[NAME](http://www.opendkim.org/opendkim.8.html#NAME)

[SYNOPSIS](http://www.opendkim.org/opendkim.8.html#SYNOPSIS)

[DESCRIPTION](http://www.opendkim.org/opendkim.8.html#DESCRIPTION)

[DATA SETS](http://www.opendkim.org/opendkim.8.html#DATA%20SETS)

[OPTIONS](http://www.opendkim.org/opendkim.8.html#OPTIONS)

[OPERATION](http://www.opendkim.org/opendkim.8.html#OPERATION)

[MTA MACROS](http://www.opendkim.org/opendkim.8.html#MTA%20MACROS)

[FILE PERMISSIONS](http://www.opendkim.org/opendkim.8.html#FILE%20PERMISSIONS)

[ENVIRONMENT](http://www.opendkim.org/opendkim.8.html#ENVIRONMENT)

[NOTES](http://www.opendkim.org/opendkim.8.html#NOTES)

[EXIT STATUS](http://www.opendkim.org/opendkim.8.html#EXIT%20STATUS)

[HISTORY](http://www.opendkim.org/opendkim.8.html#HISTORY)

[VERSION](http://www.opendkim.org/opendkim.8.html#VERSION)

[COPYRIGHT](http://www.opendkim.org/opendkim.8.html#COPYRIGHT)

[SEE ALSO](http://www.opendkim.org/opendkim.8.html#SEE%20ALSO)

* * *

[](http://www.opendkim.org/opendkim.8.html)
NAME
----

**opendkim** − DKIM signing and verifying filter for MTAs

[](http://www.opendkim.org/opendkim.8.html)
SYNOPSIS
--------

**opendkim** [−A] [−b modes] [−c canon] [−d domain[,...]] [−D] [−e name] [−f] [−F time] [−k keyfile] [−l] [−L min] [−n] [−o hdrlist] [−p socketspec] [−P pidfile] [−Q] [−r] [−s selector] [−S signalg] [−t testfiles] [−T secs] [−u userid[:group]] [−v] [−V] [−W] [−x configfile] [−X]

[](http://www.opendkim.org/opendkim.8.html)
DESCRIPTION
-----------

**opendkim** implements the **DKIM** standard for signing and verifying e-mail messages on a per-domain basis.

**opendkim** uses the _milter_ interface, originally distributed as part of version 8.11 of **sendmail(8),** to provide DKIM signing and/or verifying service for mail transiting a milter-aware MTA.

Most, if not all, of the command line options listed below can also be set using a configuration file. See the _−x_ option for details.

[](http://www.opendkim.org/opendkim.8.html)
DATA SETS
---------

Many of the command line and configuration file parameters will refer to a "dataset" as their values. This refers to a string that either contains the list of desirable values, or to a file that contains them, or (if enabled at compile time) a database containing the data.

Some data sets require that the value contain more than one entry. How this is done depends on which data set type is used.

Which type is used depends on the format of the specification string. Note that not all of these are necessarily supported for all installations; most of them depend on the availability of a particular third-party library at compile time.

In particular:

_a)_ If the string begins with "file:", then the remainder of the string is presumed to refer to a flat file that contains elements of the data set, one per line. If a line contains whitespace-separated values, then the line is presumed to define a key and its corresponding value. Blank lines are ignored, and the hash ("#") character denotes the start of a comment. If a value contains multiple entries, the entries should be separated by colons.
_b)_ If the string begins with "refile:", then the remainder of the string is presumed to specify a file that contains a set of patterns, one per line, and their associated values. The pattern is taken as the start of the line to the first whitespace, and the portion after that whitespace is taken as the value to be used when that pattern is matched. Patterns are simple wildcard patterns, matching all text except that the asterisk ("*") character is considered a wildcard. If a value contains multiple entries, the entries should be separated by colons.
_c)_ If the string begins with "db:" and the program was compiled with Sleepycat DB support, then the remainder of the string is presumed to identify a Sleepycat database containing keys and corresponding values. These may be used only to test for membership in the data set, or for storing keys and corresponding values. If a value contains multiple entries, the entries should be separated by colons.
_d)_ If the string begins with "dsn:" and the OpenDKIM library was compiled to support that database type, then the remainder of the string is a Data Store Name describing the type, location parameters and access credentials for an ODBC or SQL database. The DSN is of the form:

backend://[user[:pwd]@][port+]host/dbase[/key=value[?...]]

where _backend_ is the name of a supported backend database mechanism (e.g. "mysql"), _user_ and _password_ are optional login credentials for the database, _port_ and _host_ describe the destination of a TCP connection to connect to that database, _dbase_ is the name of the database to be accessed, and the _key=value_ pairs must specify at least "table", "keycol" and "datacol" values specifying the name of the table, the name of the column to consider as the key, and the name(s) of the column(s) to be considered as the values (separated by commas). For example (all in one line):

mysql:://dbuser:dbpass@3306+dbhost/odkim/table=macros 

 ?keycol=host?datacol=v1,v2

defines a MySQL database listening at port 3306 on host "dbhost"; the userid "dbuser" and password "dbpass" should be used to access the database; the database name is "odkim", and the data are in columns "host" (the keys) and "v1" and "v2" (the values) inside table "macros". This example would thus return two values when a match is found.

No value within the DSN may contain any of the six punctuation characters (":", "/", "@", "+", "?" and "=") used to separate portions of the DSN from each other.

_e)_ If the string begins with "ldap:", "ldaps:" or "ldapi:", it is presumed to be a space-separated set of one or more LDAP URLs that identify a set of servers to be queried. The first one should be a full RFC4516 LDAP URL indicating a base DN template and optional scope, filter and attribute names to use in queries. When constructing a DN template or filter, the special tokens "$d" and "$D" are replaced with the key being queried and the key broken into components, separated at "." characters, each component preceded by "dc=" and followed by "," (so "example.com" would become "dc=example,dc=com"). If a data set requires multiple values to be returned, the appropriate attribute names should be given in the correct order to satisfy such requests.
_f)_ If the string begins with "lua:", it is presumed to refer to a file that contains a Lua script to be executed whenever a query is performed. The key for the query is placed in a global variable called "query", which the called script can then access. The script may return any number of values as required for the type of query being performed.
_g)_ If the string begins with "memcache:", it is presumed to refer to a memory cache database provided by **memcached.** The remainder of the string is a comma-separated list of hosts to which query attempts should be made, each optionally followed by ":" and a port number; that list must be followed by a slash ("/") character and a string that will be used to prefix queries send to the cache. For example:

memcache:localhost,otherhost/keyname

This would use either "localhost" or "otherhost" to conduct queries, and all strings sent to the dataset will be prefixed with "keyname:".

_h)_ If the string contains none of these prefixes but ends with ".db", it is presumed to be a Sleepycat DB as described above (if support for same is compiled in).
_i)_ If the string contains none of these prefixes but starts with a slash ("/") character, it is presumed to be a flat file as described above.
_j)_ If the string begins with "csl:", the string is treated as a comma-separated list as described in m) below.
_k)_ If the string begins with "erlang:", it is presumed to refer to a function called to be made to the specified distributed Erlang node(s). The specification is of the form

erlang:node@host[,...]:cookie:module:function

where _node[,...]_ is a list of comma-separated erlang nodes, _cookie_ is the cookie for the known nodes of the distributed Erlang setup, _module_ is the name of the Erlang module where the function to be called resides, _function_ is the name of the Erlang function to be called. For example, (all in one line):

erlang:mynode@myhost,myothernode@myotherhost: 

 chocolate:dkim:lookup

will join the distributed Erlang setup connecting to either "mynode@myhost" or "myothernode@myotherhost" (connections to nodes are tried in order) using "chocolate" as the cookie, and use the function "dkim:lookup/1" for lookups.

_l)_ If the string begins with "mdb:", it refers to a directory that contains a memory database, as provided by libmdb from OpenLDAP.
_m)_ In any other case, the string is presumed to be a comma-separated list. Elements in the list are either simple data elements that are part of the set or, in the case of an entry of the form "x=y", are stored as key-value pairs as described above.
[](http://www.opendkim.org/opendkim.8.html)
OPTIONS
-------

_−A_ Automatically re-start on failures. Use with caution; if the filter fails instantly after it starts, this can cause a tight _fork(2)_ loop. This can be mitigated using some values in the configuration file to limit restarting. See _opendkim.conf(5)._

_−b modes_

Selects operating modes. _modes_ is a concatenation of characters that indicate which mode(s) of operation are desired. Valid modes are _s_ (signer) and _v_ (verifier). The default is _sv_ except in test mode (see _−t_ below) in which case the default is _v._

_−c canon_

Selects the canonicalization method(s) to be used when signing messages. When verifying, the message’s DKIM-Signature: header specifies the canonicalization method. The recognized values are _relaxed_ and _simple_ as defined by the DKIM specification. The default is _simple._ The value may include two different canonicalizations separated by a slash ("/") character, in which case the first will be applied to the headers and the second to the body.

_−d dataset_

A set of domains whose mail should be signed by this filter. Mail from other domains will be verified rather than being signed.

_−D_ Sign subdomains of those listed by the _−d_ option as well as the actual domains.

_−e name_

Extracts the value of _name_ from the configuration file (if any).

_−f_ Normally _opendkim_ forks and exits immediately, leaving the service running in the background. This flag suppresses that behaviour so that it runs in the foreground.

_−F time_

Specifies a fixed time to use when generating signatures. Ignored unless also used in conjunction with _−t_ (see below). The time must be expressed in the usual UNIX _time\_t_ (seconds since epoch) format.

_−k keyfile_

Gives the location of a PEM-formatted private key to be used for signing all messages. Ignored if a configuration file is referenced that defines a KeyTable.

_−l_ Log via calls to _syslog(3)_ any interesting activity.

_−L min[%+]_

Instructs the verification code to fail messages for which a partial signature was received. There are three possible formats: _min_ indicating at least _min_ bytes of the message must be signed (or if the message is smaller than _min_ then all of it must be signed); _min%_ requiring that at least _min_ percent of the received message must be signed; and _min+_ meaning there may be no more than _min_ bytes of unsigned data appended to the message for it to be considered valid.

_−n_ Parse the configuration file and command line arguments, reporting any errors found, and then exit. The exit value will be 0 if the filter would start up without complaint, or non-zero otherwise.

_−o dataset_

Specifies a list of headers that should be omitted when generating signatures. If an entry in the list names any header which is mandated by the DKIM specification, the entry is ignored. A set of headers is listed in the DKIM specification as "SHOULD NOT" be signed; the default list for this parameter contains those headers (Return-Path, Received, Comments, Keywords, Bcc, Resent-Bcc and DKIM-Signature). To omit no headers, simply use the string "-" (or any string that will match no headers).

_−p socketspec_

Specifies the socket that should be established by the filter to receive connections from _sendmail(8)_ in order to provide service. _socketspec_ is in one of two forms: _local:path_ which creates a UNIX domain socket at the specified _path,_ or _inet:port[@host]_ or _inet6:port[@host]_ which creates a TCP socket on the specified _port_ using the requested protocol family. If the _host_ is not given as either a hostname or an IP address, the socket will be listening on all interfaces. A literal IP address must be enclosed in square brackets. If neither socket type is specified, _local_ is assumed, meaning the parameter is interpreted as a path at which the socket should be created. This parameter is mandatory either here or in the configuration file.

_−P pidfile_

Specifies a file into which the filter should write its process ID at startup.

_−Q_ Query test mode. The filter will read two lines from standard input, one containing a database description to be opened and one containing a string of the form "q/n" where "q" is the query to be performed and "n" is the number of fields to be retrieved.
_−r_ Checks all messages for compliance with RFC5322 header count requirements. Non-compliant messages are rejected.

_−s selector_

Defines the name of the selector to be used when signing messages. See the **DKIM** specification for details.

_−S signalg_

Selects the signing algorithm to use when generating signatures. Use ’opendkim −V’ to see the list of supported algorithms. The default is _rsa-sha256_ if it is available, otherwise it will be _rsa-sha1._

_−t testfiles_

Evaluates (verifies) one or more RFC5322-formatted message found in _testfiles_ and exits. The value of _testfiles_ should be a comma-separated list of one or more filenames, one of which may be "-" if the message should be read from standard input.

_−T secs_

Sets the DNS timeout in seconds. A value of 0 causes an infinite wait. The default is 5. Ignored if not using an asynchronous resolver package. See also the NOTES section below.

_−u userid[:group]_

Attempts to be come the specified _userid_ before starting operations. The process will be assigned all of the groups and primary group ID of the named _userid_ unless an alternate _group_ is specified. See the FILE PERMISSIONS section for more information.

_−v_ Increase verbose output during test mode (see _−t_ above). May be specified more than once to request increasing amounts of output.
_−V_ Print the version number and supported canonicalization and signature algorithms, and then exit without doing anything else.
_−W_ If logging is enabled (see _−l_ above), issues very detailed logging about the logic behind the filter’s decision to either sign a message or verify it. The "W" stands for "Why?!" since the logic behind the decision is non-trivial and can be confusing to administrators not familiar with its operation. A description of how the decision is made can be found in the OPERATION section of this document. This causes a large increase in the amount of log data generated for each message, so it should be limited to debugging use and not enabled for general operation.

_−x configfile_

Read the named configuration file. See the _opendkim.conf(5)_ man page for details. Values in the configuration file are overridden when their equivalents are provided on the command line until a configuration reload occurs. The OPERATION section describes how reloads are triggered. The default is to read a configuration file from _@SYSCONFDIR@/opendkim.conf_ if one exists, or otherwise to apply defaults to all values.

_−X_ Tolerates configuration file items that have been internally marked as "deprecated". Normally when a configuration file item is removed from the package, it is flagged in this way for at least one full release cycle. The presence of a deprecated configuration file item typically causes the filter to return an error and refuse to start. Setting this flag will allow the filter to start and a warning is logged. In some future release when the item is removed completely, a different error results, and it will not be possible to start the filter. Use of this flag is NOT RECOMMENDED; it could effectively hide a major configuration change with serious security implications.
[](http://www.opendkim.org/opendkim.8.html)
OPERATION
---------

A message will be verified unless it conforms to the signing criteria, which are: (1) the domain on the From: address (if present) must be listed by the _−d_ command line switch or the _Domain_ configuration file setting, and (2) (a) the client connecting to the MTA must have authenticated, or (b) the client connecting to the MTA must be listed in the file referenced by the _InternalHosts_ configuration file setting (or be in the default list for that option), or (c) the client must be connected to a daemon port named by the _MTAs_ configuration file setting, or (d) the MTA must have set one or more macros matching the criteria set by the _MacroList_ configuration file setting.

For (a) above, the test is whether or not the MTA macro "{auth_type}" is set and contains any non-empty value. This means the MTA must pass the value of that macro to the filter before or during the end-of-header (EOH) phase in order for its value to be tested. Check your MTA’s configuration documentation for details.

For (1) above, other header fields may be selected using the SenderHeaders configuration file setting. See _opendkim.conf(5)_ for more information.

When signing a message, a _DKIM-Signature:_ header will be prepended to the message. The signature is computed using the private key provided. You must be running a version of _sendmail(8)_ recent enough to be able to do header prepend operations (8.13.0 or later).

When verifying a message, an _Authentication-Results:_ header will be prepended to indicate the presence of a signature and whether or not it could be validated against the body of the message using the public key advertised by the sender’s nameserver. The value of this header can be used by mail user agents to sort or discard messages that were not signed or could not be verified.

Upon receiving SIGUSR1, if the filter was started with a configuration file, it will be re-read and the new values used. Note that any command line overrides provided at startup time will be lost when this is done. Also, the following configuration file values (and their corresponding command line items, if any) are not reloaded through this process: AutoRestart (−A), AutoRestartCount, AutoRestartRate, Background, MilterDebug, PidFile (−P), POPDBFile, Quarantine (−q), QueryCache, Socket (−p), StrictTestMode, TestPublicKeys, UMask, UserID (−u). The filter does not automatically check the configuration file for changes and reload.

[](http://www.opendkim.org/opendkim.8.html)
MTA MACROS
----------

**opendkim** makes use of three MTA-provided macros, plus any demanded by configuration. The basic three are: "i" (the envelope ID, also known as the job ID or the queue ID), which is used for logging; "daemon_name" (the symbolic name given to the MTA instance that accepted the connection), which is used when performing tests against any "MTAs" setting used; and "auth_type", which is used to determine whether or not the SMTP client authenticated to the MTA. If the MTA does not provide them to **opendkim** then it is not able to apply their corresponding tests or do useful logging. Consult your MTA documentation to determine how to adjust your its configuration if some or all of these are not available.

[](http://www.opendkim.org/opendkim.8.html)
FILE PERMISSIONS
----------------

When the filter is started as the superuser and the UserID (−u) setting is used, the filter gives up its root privileges by changing to the specified user after the following steps are taken: (1) the configuration file (if any) is loaded; (2) if the KeyFile (−k) setting is used, that key is loaded into memory; (3) all data sets in the configuration file are opened, and those that are based on flat files are also read into memory; and (4) if ChangeRootDirectory is set, the process root is changed to that directory. This means on configuration reload, the filter will not be accessing these files or the configuration file as the superuser (and possibly from a different root), and any key files referenced by the KeyTable will also be accessed by the new user.

Thus, keys referenced by the KeyTable must always be accessible for read by the unprivileged user. Also, run-time reloads are not possible if any of the other files will not be readable by the unprivileged user.

[](http://www.opendkim.org/opendkim.8.html)
ENVIRONMENT
-----------

The following environment variable(s) can be used to adjust the behaviour of this filter: _DKIM\_TMPDIR_

The directory to use when creating temporary files. The default is _/tmp._

[](http://www.opendkim.org/opendkim.8.html)
NOTES
-----

When using DNS timeouts (see the _−T_ option above), be sure not to use a timeout that is larger than the timeout being used for interaction between _sendmail_ and the filter. Otherwise, the MTA could abort a message while waiting for a reply from the filter, which in turn is still waiting for a DNS reply.

The POP authentication database is expected to be a Sleepycat DB file (formerly known as a Berkeley DB) in hash format with keys containing the IP address in text form without a terminating NULL. The values of these records are not checked; only the existence of such records is of interest. The filter will attempt to establish a shared lock on the database before reading from it, so any programs which write to the database should keep their lock use to a minimum or else this filter will appear to hang while waiting for the lock operation to complete.

Features that involve specification of IPv4 addresses or CIDR blocks will use the _inet\_addr(3)_ function to parse that information. Users should be familiar with the way that function handles the non-trivial cases (for example, "192.0.2/24" and "192.0.2.0/24" are not the same thing).

[](http://www.opendkim.org/opendkim.8.html)
EXIT STATUS
-----------

Filter exit status codes are selected according to _sysexits(3)._

[](http://www.opendkim.org/opendkim.8.html)
HISTORY
-------

DKIM is an amalgam of Yahoo!’s **DomainKeys** proposal, and Cisco’s **Internet Identified Mail** (IIM) proposal.

[](http://www.opendkim.org/opendkim.8.html)
VERSION
-------

This man page covers version @VERSION@ of _opendkim._

[](http://www.opendkim.org/opendkim.8.html)
COPYRIGHT
---------

Copyright (c) 2005-2008, Sendmail, Inc. and its suppliers. All rights reserved.

Copyright (c) 2009-2013, 2015, The Trusted Domain Project. All rights reserved.

[](http://www.opendkim.org/opendkim.8.html)
SEE ALSO
--------

_opendkim.conf(5), sendmail(8)_

Sendmail Operations Guide

RFC5321 - Simple Mail Transfer Protocol

RFC5322 - Internet Messages

RFC5451 - Message Header Field for Indicating Message Authentication Status

RFC6008 - Authentication-Results Registration for Differentiating among Cryptographic Results

RFC6376 - DomainKeys Identified Mail

* * *
