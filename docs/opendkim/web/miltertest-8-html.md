# Source: http://www.opendkim.org/miltertest.8.html

Title: miltertest

URL Source: http://www.opendkim.org/miltertest.8.html

Markdown Content:
[NAME](http://www.opendkim.org/miltertest.8.html#NAME)

[SYNOPSIS](http://www.opendkim.org/miltertest.8.html#SYNOPSIS)

[DESCRIPTION](http://www.opendkim.org/miltertest.8.html#DESCRIPTION)

[OPTIONS](http://www.opendkim.org/miltertest.8.html#OPTIONS)

[FUNCTIONS](http://www.opendkim.org/miltertest.8.html#FUNCTIONS)

[EOM CHECKS](http://www.opendkim.org/miltertest.8.html#EOM%20CHECKS)

[EXAMPLE](http://www.opendkim.org/miltertest.8.html#EXAMPLE)

[NOTES](http://www.opendkim.org/miltertest.8.html#NOTES)

[MILTER NOTES](http://www.opendkim.org/miltertest.8.html#MILTER%20NOTES)

[VERSION](http://www.opendkim.org/miltertest.8.html#VERSION)

[COPYRIGHT](http://www.opendkim.org/miltertest.8.html#COPYRIGHT)

[SEE ALSO](http://www.opendkim.org/miltertest.8.html#SEE%20ALSO)

* * *

[](http://www.opendkim.org/miltertest.8.html)
NAME
----

**miltertest** − milter unit test utility

[](http://www.opendkim.org/miltertest.8.html)
SYNOPSIS
--------

**miltertest** [−D name[=value]] [−s script] [−u] [−v] [−V] [−w]

[](http://www.opendkim.org/miltertest.8.html)
DESCRIPTION
-----------

**miltertest** simulates the MTA side of an MTA-milter interaction for testing a milter-aware filter application. It takes as input a script using the Lua language, and by exporting some utility functions, makes it possible for users to write scripts that exercise a filter.

See documentation on Lua (e.g. http://www.lua.org) for the syntax of the language in general. The documentation below describes functions that are added to Lua by this application to make testing possible.

Documentation on milter can be found at http://www.milter.org. A particular transaction must follow a series of steps to be completed, namely negotiate, connection information, envelope sender, envelope recipient(s), header field(s), end-of-header, body chunk(s), end-of-message. To make the work of writing tests with **miltertest** simpler, any of these steps prior to end-of-message that is skipped will be filled in using arbitrary, but legal, data.

Interspersed with these protocol phases are optional macro (key/value) deliveries from the MTA. **miltertest** will never send these automatically. If they are needed for your tests, you must send them as part of your test script.

[](http://www.opendkim.org/miltertest.8.html)
OPTIONS
-------

_-D name[=value]_

Defines a global variable called _name_ to the Lua interpreter. If a _value_ is provided, the global variable is set to that value (as a string, although Lua can convert strings to numbers internally). If no _value_ is provided, the global variable is set to 1.

_-s script_

Use the contents of file _script_ as the Lua script to be executed. The default is to read from standard input.

_-u_ After the filter being tested is terminated, report user and system time consumed. See _getrusage(2)._
_-v_ Increase verbose output. May be specified multiple times to request more and more information.
_-V_ Print version number and exit.
_-w_ Don’t wait for child status to be returned when testing is complete.
[](http://www.opendkim.org/miltertest.8.html)
FUNCTIONS
---------

The following functions are made available to Lua scripts for exercising a filter. All functions return Lua constant "nil" on success or an error string on failure, unless otherwise indicated. **mt.abort(conn)**

Aborts the transaction in progress on the specified connection.

**mt.bodyfile(conn, file)**

Sends the contents of the named _file_ to the connection as body data. If there is any error opening _file_ for reading, the test aborts.

**mt.bodyrandom(conn, n)**

Sends at least _n_ bytes of random-length lines of random printable ASCII data as body chunks to the specified connection.

**mt.bodystring(conn, str)**

Sends _str_ as a chunk of body text on the specified connection.

**mt.chdir(directory)**

Changes the current working directory to the named _directory._

**mt.connect(sockinfo[, count, interval])**

Makes a connection to a filter listening at the socket described by _sockinfo._ Returns a handle referring to that connection, or the Lua constant "nil" on error. If _count_ and _interval_ are included, they specify the number of times to try to connect to the filter and the delay between each connection in seconds (with floating point values permitted). If the environment variable MILTERTEST_RETRY_SPEED_FACTOR is set and appears to contain an integer, the value of _interval_ (if set) will be multiplied by the value found in that environment variable. This is included to allow tests in a large test suite to be easily adjusted on slow systems without reconfiguring the entire test suite.

**mt.conninfo(conn, host, ip)**

Sends information about a new SMTP connection to the MTA, represented by connection _conn,_ from the host named _host_ at IP address _ip_ (both strings). If _host_ is the Lua constant "nil", the string "localhost" is assumed. If _ip_ is the Lua constant "nil", a DNS query will be made for the IP address matching _host;_ if none is found, the test will abort. The _ip_ may also be the special string "unspec", which will tell the filter that a connection came in from an unknown protocol family.

**mt.data(conn)**

Announces the DATA command on the specified connection, which occurs between the last RCPT TO command and the beginning of the header block.

**mt.disconnect(conn[, polite]))**

Sends a "quit" message to the specified connection and then closes that connection. The specified _conn_ handle should no longer be used. If _polite_ is defined, it must be a Boolean indicating whether a normal disconnect should be done (true) or an abrupt disconnect should be done (false). An abrupt disconnect skips standard protocol shutdown steps.

**mt.echo(string)**

Prints the specified _string_ on standard output. Returns nothing.

**mt.eoh(conn)**

Announces end-of-header on the specified connection.

**mt.eom(conn)**

Announces end-of-message on the specified connection, and begins capturing any other operations the filter might perform in that phase.

**mt.eom_check(conn, op, param[, ...])**

Checks the captured set of EOM operations (see above) to determine whether or not specific milter actions were requested by the filter. Returns a Boolean value (true or false). See the EOM CHECKS section for details.

**mt.getheader(conn, hdr, n)**

Retrieves the value of the _nth_ instance of header field named _hdr_ added during end-of-message processing on the specified connection. This can be used by the script to verify that the header thus added contains the right thing. Returns the value as a string, or the Lua constant "nil" on error.

**mt.getcwd()**

Returns the current working directory as a string.

**mt.getreply(conn)**

Returns the last milter reply received from the specified connection, as an integer. This can be compared to any of the SMFIR_* constants defined by milter to see if the filter responded as expected. This value is initially set to the NULL character.

**mt.header(conn, name, value)**

Sends the header with the given _name_ and _value_ to the specified connection.

**mt.helo(conn, name)**

Sends HELO/EHLO information using the specified _name_ as the parameter given.

**mt.macro(conn, type, name, value[, name2, value2[, ...]])**

Declares a macro called _name_ whose value is _value_ and whose type (matching protocol element) is _type._ Valid types are SMFIC_CONNECT, SMFIC_HELO, SMFIC_MAIL and SMFIC_RCPT. Multiple macro names and values can be provided, but they must appear in pairs.

**mt.mailfrom(conn, envfrom[, ...])**

Announces _envfrom_ as the envelope sender of a new message. ESMTP parameters as additional arguments are permitted.

**mt.negotiate(conn, version, actions, steps)**

Performs milter option negotiation with the connection _conn,_ advertising that the specified protocol _version,_ protocol _actions_ and protocol _steps_ are offered by the MTA. Returns the Lua constant "nil" on success or an error string on failure. If any of the protocol parameters are "nil", the current defaults (defined in _libmilter/mfdef.h,_ provided with the milter source code) will be used.

**mt.rcptto(conn, envrcpt[, ...])**

Announces _envrcpt_ as an envelope recipient of a message. ESMTP parameters as additional arguments are permitted.

**mt.set_timeout(n)**

Sets the read timeout to _n_ seconds. The default is ten seconds. Returns nothing.

**mt.sleep(n)**

Sleeps for _n_ seconds. The value may be an integer (for whole seconds) or a floating-point value (for partial seconds).

**mt.signal(n)**

Sends the specified signal number _n_ to the running filter.

**mt.startfilter(path, arg1, arg2, ...)**

Starts the filter whose binary is located at _path_ with argument vector comprised of strings _path, arg1, arg2,_ etc. Basically this is almost the same syntax as _execl(3)_ except that **miltertest** also does the fork for you, and will remember the process ID in order to request a clean shutdown using SIGTERM and _wait(2)_ at the end of the test script. If the filter could not be started, an exception is generated with an error message returned.

**mt.test_action(conn, action)**

Tests whether or not the connection represented by _conn_ requested the specified milter protocol _action,_ specified by an SMFIF_* constant, during option negotiation. (See the libmilter documentation and/or include files for details.)

**mt.test_option(conn, option)**

Tests whether or not the connection represented by _conn_ requested the specified milter protocol _option,_ specified by an SMFIP_* constant, during option negotiation. (See the libmilter documentation and/or include files for details.)

**mt.unknown(conn, str)**

Announces that the unknown SMTP command _str_ arrived over the connection represented by _conn._

[](http://www.opendkim.org/miltertest.8.html)
EOM CHECKS
----------

The **mt.eom_check()** function is used to determine what changes to the message the filter requested during its EOM callback. The changes can be requested in any order. The first parameter, _op,_ indicates what operation is of interest, and it also dictates what the possible parameter list is. Valid values and corresponding parameters for _op_ are as follows: _MT\_HDRADD_

Checks to see if a header field was added to the message. If no parameters are given, the function returns true if any header field was added. If one parameter was given, the function returns true only if the named header field was added (regardless of its value). If two parameters are given, the function returns true only if the named header field was added with the specified value.

_MT\_HDRCHANGE_

Checks to see if an existing header field was changed. If no parameters are given, the function returns true if any header field was modified. If one parameter was given, the function returns true only if the named header field was modified (regardless of its new value). If two parameters are given, the function returns true only if the named header field was modified to have the specified new value.

_MT\_HDRDELETE_

Checks to see if an existing header field was deleted. If no parameters are given, the function returns true if any header field was deleted. If one parameter was given, the function returns true only if the named header field was deleted.

_MT\_HDRINSERT_

Checks to see if a header field was inserted into the message. If no parameters are given, the function returns true if any header field was added. If one parameter was given, the function returns true only if the named header field was added (regardless of its value). If two parameters are given, the function returns true only if the named header field was added with the specified value. If three parameters are given, the function returns true only if the named header field was added with the specified value at the specified index.

_MT\_RCPTADD_

Checks to see if an envelope recipient was added. Currently only one parameter may be provided.

_MT\_RCPTDELETE_

Checks to see if an envelope recipient was deleted. Currently only one parameter may be provided.

_MT\_BODYCHANGE_

Checks to see if the message’s body was replaced by other content. With no parameters, the function returns true only if the body was changed (regardless of the new content). With one parameter, the function returns true only if the body was changed to the specified new content.

_MT\_QUARANTINE_

Checks to see if the filter requested quarantining of the message. With no parameters, the function returns true only if quarantine was requested. With one parameter, the function returns true only if quarantine was requested with the specified reason string.

_MT\_SMTPREPLY_

Checks to see if the filter requested a specific SMTP reply message. With no parameters, the function returns true only if a specific reply was requested. With one parameter, the function returns true only if a specific reply was requested with the specified SMTP code. With two parameters, the function returns true only if a specific reply was requested with the specified SMTP code and enhanced status code. With three parameters, the function returns true only if a specific reply was requested with the specified SMTP code, enhanced status code, and text.

[](http://www.opendkim.org/miltertest.8.html)
EXAMPLE
-------

-- Echo that the test is starting 

 mt.echo("*** begin test") 

 -- start the filter 

 mt.startfilter("../myfilter", "−p", "inet:12345@localhost") 

 mt.sleep(2)

-- try to connect to it 

 conn = mt.connect("inet:12345@localhost") 

 if conn == nil then

error "mt.connect() failed"

end

-- send connection information 

 -- mt.negotiate() is called implicitly 

 if mt.conninfo(conn, "localhost", "127.0.0.1") ~= nil then

error "mt.conninfo() failed"

end 

 if mt.getreply(conn) ~= SMFIR_CONTINUE then

error "mt.conninfo() unexpected reply"

end

-- send envelope macros and sender data 

 -- mt.helo() is called implicitly 

 mt.macro(conn, SMFIC_MAIL, "i", "test-id") 

 if mt.mailfrom(conn, "user@example.com") ~= nil then

error "mt.mailfrom() failed"

end 

 if mt.getreply(conn) ~= SMFIR_CONTINUE then

error "mt.mailfrom() unexpected reply"

end

-- send headers 

 -- mt.rcptto() is called implicitly 

 if mt.header(conn, "From", "user@example.com") ~= nil then

error "mt.header(From) failed"

end 

 if mt.getreply(conn) ~= SMFIR_CONTINUE then

error "mt.header(From) unexpected reply"

end 

 if mt.header(conn, "Date", "Tue, 22 Dec 2009 13:04:12 −0800") ~= nil then

error "mt.header(Date) failed"

end 

 if mt.getreply(conn) ~= SMFIR_CONTINUE then

error "mt.header(Date) unexpected reply"

end 

 if mt.header(conn, "Subject", "Signing test") ~= nil then

error "mt.header(Subject) failed"

end 

 if mt.getreply(conn) ~= SMFIR_CONTINUE then

error "mt.header(Subject) unexpected reply"

end

-- send EOH 

 if mt.eoh(conn) ~= nil then

error "mt.eoh() failed"

end 

 if mt.getreply(conn) ~= SMFIR_CONTINUE then

error "mt.eoh() unexpected reply"

end

-- send body 

 if mt.bodystring(conn, "This is a test!\r\n") ~= nil then

error "mt.bodystring() failed"

end 

 if mt.getreply(conn) ~= SMFIR_CONTINUE then

error "mt.bodystring() unexpected reply"

end

-- end of message; let the filter react 

 if mt.eom(conn) ~= nil then

error "mt.eom() failed"

end 

 if mt.getreply(conn) ~= SMFIR_ACCEPT then

error "mt.eom() unexpected reply"

end

-- verify that a test header field got added 

 if not mt.eom_check(conn, MT_HDRINSERT, "Test-Header") then

error "no header added"

end

-- wrap it up! 

 mt.disconnect(conn)

[](http://www.opendkim.org/miltertest.8.html)
NOTES
-----

If a filter negotiates one of the SMFIP_NO* protocol option bits and a script attempts to perform one of those protocol steps, an error is returned. It is up to the test author to use _mt.test\_option()_ function to see if performing a protocol step has been explicitly disabled by the filter.

[](http://www.opendkim.org/miltertest.8.html)
MILTER NOTES
------------

When _mt.macro()_ is called, it replaces all previous macros of the same _type_ with the ones provided in the argument list. Thus, one call should be made that lists the complete set rather than one call per name-value pair. Also, as each stage in the milter process is executed, all macros corresponding stages after the current one are discarded. For example, calling _mt.helo(),_ which corresponds to SMFIC_HELO, will cause all prior macros of type SMFIC_MAIL and SMFIC_RCPT to be discarded as they represent a milter stage that comes later than SMFIC_HELO.

Since the milter protocol and the internals of libmilter itself are not formally documented, there are myriad other subtleties of the milter protocol and implementation that are not documented here and may not be documented elsewhere, and could change without notice. Caveat emptor.

[](http://www.opendkim.org/miltertest.8.html)
VERSION
-------

This man page covers version 1.5.0 of _miltertest._

[](http://www.opendkim.org/miltertest.8.html)
COPYRIGHT
---------

Copyright (c) 2009-2014, The Trusted Domain Project. All rights reserved.

[](http://www.opendkim.org/miltertest.8.html)
SEE ALSO
--------

Milter -- http://www.milter.org

Lua -- http://www.lua.org

* * *
