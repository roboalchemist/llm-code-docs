# Source: http://www.opendkim.org/opendkim-lua.3.html

Title: opendkim-lua

URL Source: http://www.opendkim.org/opendkim-lua.3.html

Markdown Content:
[NAME](http://www.opendkim.org/opendkim-lua.3.html#NAME)

[DESCRIPTION](http://www.opendkim.org/opendkim-lua.3.html#DESCRIPTION)

[GLOBAL VARIABLES](http://www.opendkim.org/opendkim-lua.3.html#GLOBAL%20VARIABLES)

[SETUP SCRIPT FUNCTIONS](http://www.opendkim.org/opendkim-lua.3.html#SETUP%20SCRIPT%20FUNCTIONS)

[SCREEN SCRIPT FUNCTIONS](http://www.opendkim.org/opendkim-lua.3.html#SCREEN%20SCRIPT%20FUNCTIONS)

[STATISTICS SCRIPT FUNCTIONS](http://www.opendkim.org/opendkim-lua.3.html#STATISTICS%20SCRIPT%20FUNCTIONS)

[FINAL SCRIPT FUNCTIONS](http://www.opendkim.org/opendkim-lua.3.html#FINAL%20SCRIPT%20FUNCTIONS)

[VERSION](http://www.opendkim.org/opendkim-lua.3.html#VERSION)

[COPYRIGHT](http://www.opendkim.org/opendkim-lua.3.html#COPYRIGHT)

[SEE ALSO](http://www.opendkim.org/opendkim-lua.3.html#SEE%20ALSO)

* * *

[](http://www.opendkim.org/opendkim-lua.3.html)
NAME
----

**opendkim-lua** − Programming the OpenDKIM filter using Lua scripts

[](http://www.opendkim.org/opendkim-lua.3.html)
DESCRIPTION
-----------

The OpenDKIM filter has hooks to run user-provided scripts for making policy decisions regarding signatures to add on outbound messages or verification and acceptance of messages inbound. The hooks take the form of multiple Lua scripts which, if defined, are run at important points during processing of a message.

For a full description of the Lua language, consult Lua programming references (see below for a starting point). This man page only describes the use of Lua in the context of OpenDKIM, specifically the functions and global variables OpenDKIM provides for use in user-constructed scripts beyond what Lua provides by default.

Unless otherwise noted, all functions described below return a single result; on success they return the requested data, and on error they return the Lua constant "nil".

Four scripting hooks are provided. They are as follows:

_setup_ The setup script is run after all headers for the message have been received but before any DKIM operations have started. At this point the user can examine the available header fields to decide whether the message should be signed or verified (or both) and, if signing, which key(s) should be used to add signatures and which signature features are desired.
_screen_ The screen script is run after the DKIM verification context has been established. The main purpose of this script is to give the user an opportunity to examine the message header fields compared to the available DKIM signatures and determine which, if any, should be ignored during verification. For example, the user might decide only signatures added by domains exactly matching that in the From: domain are acceptable, and the rest should be ignored.

_statistics_

The statistics script is run after all of the DKIM verification and signing work has been completed but before any final message handling is done. The main purpose of this script is to give the user an opportunity to examine the message or its signatures and make arbitrary additional statistical observations that should be recorded by the statistics module. @STATSEXT_MANNOTICE@

_final_ The final script is run after all of the DKIM verification and signing work has been completed. The user has an opportunity to examine the results of all of the signature evaluations and make a decision about whether or not the message should be accepted, rejected, discarded, quarantined, etc. If the message is accepted, any signatures requested earlier will be added to the messages before it is released.
[](http://www.opendkim.org/opendkim-lua.3.html)
GLOBAL VARIABLES
----------------

The following global variable(s) are provided for all user scripts:

_ctx_ This is a generic context pointer referring to the context in which the filtering operation is being performed. It represents a single message in progress, and the connection that accepted it.
[](http://www.opendkim.org/opendkim-lua.3.html)
SETUP SCRIPT FUNCTIONS
----------------------

These functions are made available to Lua for processing a message through the setup script: **odkim.check_popauth(ctx)**

Returns 1 if the SMTP client represented by _ctx_ is coming from an IP address found in the POPAUTH database (if enabled and configured), and 0 otherwise. Returns the Lua constant "nil" if the POPAUTH database is not enabled or not configured.

**odkim.db_check(db, string)**

Returns 1 if _db_ refers to a valid database handle (see **odkim.get_dbhandle()** below) and _string_ is found in that database, and 0 otherwise. If an error occurs, the Lua constant "nil" is returned.

**odkim.db_close(db)**

Closes the specified data set. Returns 1. The current implementation will conduct data set garbage collection when the script terminates, so this is not strictly necessary, but is recommended.

**odkim.db_open(name[, icase])**

Opens the data set specified by _name._ If _icase_ is provided and is "true", then queries into the database will be case-insensitive. See the _opendkim(8)_ man page for information on specifying a data set. On success, returns a handle that can be passed to **odkim.db_check();** raises an exception on failure.

**odkim.export(ctx, name, value[, name2, value2[, ...]])**

Exports variables named with their corresponding values so that they will be available to later scripts.

**odkim.get_clienthost(ctx)**

Returns the name of the host on the other end of the SMTP connection sending the current message. This is usually a hostname, but might be an IP address in square brackets if the SMTP client’s IP address does not have a name associated with it.

**odkim.get_clientip(ctx)**

Returns the IP address of the client on the other end of the SMTP connection sending the current message as a string. Both IPv4 and IPv6 addresses are supported.

**odkim.get_dbhandle(ctx, db)**

Returns a handle for the requested database that can be used in later queries. The value of _db_ should be one of _DB\_MTAS_ (database of MTA names whose mail should be signed), _DB\_MACROS_ (database of MTA macro checks to be done when determining signing), _DB\_DOMAINS_ (database of domains to be signed), _DB\_SIGNINGTABLE_ (database of signing table entries), _DB\_THIRDPARTY_ (database of third party signatures to be trusted) and _DB\_DONTSIGNTO_ (database of recipients whose mail should not be signed). If the requested database is not set in the current configuration file, a Lua "nil" is returned.

**odkim.get_envfrom(ctx)**

Retrieves the SMTP envelope sender address for the message represented by _ctx._

**odkim.get_fromdomain(ctx)**

Retrieves the domain name of the sender of the message represented by _ctx._

**odkim.get_header(ctx, name, n)**

Retrieves the string contained in instance _n_ of the header field called _name_ from the message represented by _ctx,_ or the Lua constant "nil" if there was no such header field. Header field numbering starts at 0, so use 0 for the first instance, 1 for the second, etc. For example:

fromaddr = odkim.get_header(ctx, "From", 0)

This will return the value of the first (and hopefully only) "From" header field. Negative values of _n_ count backwards from the end of the set of header fields, so:

rcvd = odkim.get_header(ctx, "Received", −2)

will retrieve the second-last Received: header field on the message.

**odkim.get_mtasymbol(ctx, name)**

Retrieves the value of the symbol called _name_ from the MTA connection represented by _ctx,_ or the Lua constant "nil" if the requested symbol was not available at the time of the request.

**odkim.get_rcpt(ctx, n)**

Returns the _nth_ envelope recipient for the message represented by _ctx._ Recipient numbering starts at 0, so for the first recipient, use 0 for _n._ If _n_ references an out-of-range value, the Lua constant "nil" is returned.

**odkim.get_rcptarray(ctx)**

Returns the envelope recipients for the message represented by _ctx_ in a single Lua array.

**odkim.internal_ip(ctx)**

Returns 1 if the SMTP client is coming from an internal IP address, and 0 otherwise.

**odkim.log(ctx, log)**

Logs the string _log_ if the current configuration requested logging. (Checking current configuration is why the _ctx_ parameter is required.)

**odkim.rcpt_count(ctx)**

Returns the count of envelope recipients on the message.

**odkim.replace_header(ctx, name, n, newval)**

Retrieves the value of in instance _n_ of header field _name_ in the message referenced by _ctx_ and replaces it with the string in _newval._ See _odkim.get\_header()_ above for more information about possible parameter values for _n._ Note that this only changes the content of the header field used when generating or verifying the signature; the actual delivered message is not modified. This can be used to anticipate how an intermediate mail transfer agent might alter the message, thus correcting an avoidable signature invalidation.

**odkim.resign(ctx)**

Arranges that the arriving message will be verified and then re-signed in a single operation. Returns 1 on success or the Lua constant "nil" on failure.

**odkim.set_result(ctx, result)**

Arranges to have the MTA return a specific result code in response to the message represented by _ctx._ The value of _result_ must be one of _SMFIS\_TEMPFAIL_ (temporary failure/rejection), _SMFIS\_ACCEPT_ (accept without further processing), _SMFIS\_DISCARD_ (accept but discard the message) and _SMFIS\_REJECT_ (permanent failure/rejection). Returns 1 on success or the Lua constant "nil" on failure. Note that returning any of these codes indicates a final message disposition; the MTA will be told immediately to take the specified action, and no further filter processing will occur.

**odkim.sign(ctx[, keyname[, signer[, signlen]]])**

Requests that the filter sign the message represented by _ctx_ using the specified _keyname._ The key name will be translated into an actual domain, selector and private key via a query to the KeyTable (see the _opendkim.conf(5)_ page for details). The _keyname_ may be omitted if the KeyTable is not defined, meaning the single signing domain, selector and key should be used to sign. Returns 1 on success and 0 on failure. If a _signer_ is specified, the string there will be included in the generated signature’s "i=" tag. If a _signlen_ is specified, the signature will cover that many bytes of the message body. The order of these last two parameters is interchangeable.

**odkim.signfor(ctx, address[, multi])**

Applies whatever signatures would be applied by default if the candidate message had the specified _address_ in the message’s From: field. The _multi_ parameter, if "true" (default is "false"), allows the application of multiple signatures. Returns the number of signatures applied, which may be zero.

**odkim.spam(ctx)**

Tags the message as spam, for use in developing reputation about domains that signed the message. Returns nothing. @REPUTATION_MANNOTICE@

**odkim.use_ltag(ctx)**

Requests that all signatures added to the message represented by _ctx_ include "l=" (body length) tags. Always returns the Lua constant "nil".

**odkim.verify(ctx)**

Requests that the message represented by _ctx_ be subjected to DKIM signature verification. Returns the Lua constant "nil" on success, or an error string on failure.

**odkim.xtag(ctx, tag, value)**

Requests that all signatures added to the message represented by _ctx_ include the named extension _tag_ and _value._ Returns the number of signatures successfully modified, or −1 on error. An error can occur if the named tag is one already explicitly supported by the DKIM library, or if there is a syntax error in the tag or value.

[](http://www.opendkim.org/opendkim-lua.3.html)
SCREEN SCRIPT FUNCTIONS
-----------------------

The screen script has the following functions available to it, whose descriptions can be found above: **odkim.db_check, odkim.db_close, odkim.db_open, odkim.export, odkim.get_dbhandle, odkim.get_envfrom, odkim.get_fromdomain, odkim.get_header, odkim.get_mtasymbol, odkim.get_rcpt, odkim.get_rcptarray, odkim.log, odkim.rcpt_count,** and **odkim.spam.**

The following additional functions are provided for this script: **odkim.get_sigarray(ctx)**

Returns the complete set of signature handles found in the message represented by _ctx,_ as a Lua array, or the Lua constant "nil" in case of an error.

**odkim.get_sigcount(ctx)**

Returns the number of signatures found in the message represented by _ctx,_ or the Lua constant "nil" in case of an error.

**odkim.get_sighandle(ctx, n)**

Returns a handle representing an internal copy of the _nth_ signature found on the message represented by _ctx. n_ must be a number greater than or equal to zero (representing the first signature) and less than the number of signatures on the message, which can be determined using **odkim.get_sigcount** above. The requested handle is returned on success, or the Lua constant "nil" is returned on failure.

**odkim.parse_field(string)**

Parses the contents of a header field, provided as _string,_ into user and domain parts, discarding whitespace and comment components. Returns two strings, the user part and the domain part, or the Lua constant "nil" in case of a parsing error.

**odkim.sig_getdomain(sig)**

Returns the name of the domain in the signature handle specified by _sig,_ previously returned by a call to **odkim.get_sighandle().** This is taken from the signature’s "d=" tag.

**odkim.sig_getidentity(sig)**

Returns the identity of the agent adding the signature handle specified by _sig,_ previously returned by a call to **odkim.get_sighandle().** This is taken from the signature’s "i=" tag. This may be a default value and not one that was explicitly part of the signature. If the identity could not be determined, the Lua constant "nil" is returned.

**odkim.sig_ignore(sig)**

Instructs the verification code to ignore completely the signature specified by _sig,_ previously returned by a call to **odkim.get_sighandle().** Any pending verification of the message will act as if that signature was not present on the message. Always returns the Lua constant "nil".

[](http://www.opendkim.org/opendkim-lua.3.html)
STATISTICS SCRIPT FUNCTIONS
---------------------------

The statistics script has the following functions available to it, whose descriptions can be found above: **odkim.export, odkim.get_envfrom, odkim.get_header, odkim.get_mtasymbol, odkim.get_rcpt, odkim.get_rcptarray, odkim.get_sigarray, odkim.get_sigcount, odkim.get_sighandle, odkim.log, odkim.parse_field, odkim.rcpt_count, odkim.sig_getdomain, odkim.sig_getidentity,** and **odkim.spam.**

The following functions are also available, defined in the next section: **odkim.rbl_check, odkim.rcpt_count, odkim.sig_bhresult, odkim.sig_bodylength, odkim.sig_canonlength,** and **odkim.sig_result.**

The following additional function is provided for this script: **odkim.stats(ctx, name, value)**

Records the additional statistic called _name_ with its associated _value_ for the message represented by _ctx._

[](http://www.opendkim.org/opendkim-lua.3.html)
FINAL SCRIPT FUNCTIONS
----------------------

The final script has the following functions available to it, whose descriptions can be found above: **odkim.get_clienthost, odkim.get_clientip, odkim.get_envfrom, odkim.get_fromdomain, odkim.get_header, odkim.get_mtasymbol, odkim.get_rcpt, odkim.get_rcptarray, odkim.get_sigarray, odkim.get_sigcount, odkim.get_sighandle, odkim.log, odkim.parse_field, odkim.rcpt_count, odkim.set_result, odkim.sig_getdomain, odkim.sig_getidentity, odkim.spam,** and **odkim.xtags.**

The following additional functions are provided for this script: **odkim.add_header(ctx, name, value)**

Adds a new header field called _name_ with the specified _value_ to the message represented by _ctx._ Returns 1 on success, or the Lua constant "nil" on failure.

**odkim.add_rcpt(ctx, addr)**

Adds _addr_ as an envelope recipient to the message represented by _ctx._ Returns 1 on success, or the Lua constant "nil" on failure.

**odkim.del_header(ctx, name, n)**

Deletes the _nth_ instance (starting from 0) of the header field called _name_ from the message represented by _ctx._ Returns 1 on success, or the Lua constant "nil" on failure.

**odkim.del_rcpt(ctx, addr)**

Deletes _addr_ from the list of envelope recipients on the message represented by _ctx,_ and adds a new X-Original-Recipient: header field containing the deleted address. Returns 1 on success, or the Lua constant "nil" on failure.

**odkim.quarantine(ctx, reason)**

Asks the MTA to quarantine the message represented by _ctx_ using _reason_ as a text string indicating the reason for the request. Returns 1 on success or the Lua constant "nil" on failure.

**odkim.rbl_check(ctx, query, qroot[, timeout])**

Makes an RBL query. The root of the RBL is assumed to be at _qroot_ and the subject of the query is _query,_ so the query performed will be _query.qroot ._ The context handle _ctx_ must also be provided as it contains a handle to the established DNS service. The optional _timeout_ parameter is the timeout to use, in seconds. Returns "nil" on error, no values if the requested record was not present in the RBL, or the four octets of the RBL entry if it was. The octets are returned in big-endian order. @RBL_MANNOTICE@

**odkim.set_reply(ctx, rcode, xcode, message)**

Instructs the MTA to return the specified SMTP reply to the client sending the message represented by _ctx. rcode_ must be a three-digit SMTP reply code starting with 4 or 5 (for temporary or permanent failures, respectively); _xcode_ must be the empty string or a valid extended reply code (see RFC2034) matching _rcode;_ and _message_ must be the text portion of the SMTP reply to be sent. Returns 1 on success or the Lua constant "nil" on failure.

**odkim.sig_bhresult(sig)**

Returns the result code corresponding to the body hash evaluation of the signature handled specified by _sig,_ previously returned by a call to **odkim.get_sighandle().** Valid values are the DKIM_SIGBH_* constants defined in the **libopendkim** header file _dkim.h._

**odkim.sig_bodylength(sig)**

Returns the total length of the message signed by _sig,_ previously returned by a call to **odkim.get_sighandle(),** or the Lua constant "nil" if this value could not be determined.

**odkim.sig_canonlength(sig)**

Returns the canonicalized length of the message signed by _sig,_ previously returned by a call to **odkim.get_sighandle(),** or the Lua constant "nil" if this value could not be determined. Note that this may be less than the value returned by **odkim.get_bodylength()** if the signature only covered part of the message.

**odkim.sig_result(sig)**

Returns the result code corresponding to the signature handled specified by _sig,_ previously returned by a call to **odkim.get_sighandle().** Valid values are the constants with DKIM_SIGERROR_ prefixes as defined in the **libopendkim** header file _dkim.h._

[](http://www.opendkim.org/opendkim-lua.3.html)
VERSION
-------

This man page covers version @VERSION@ of _OpenDKIM._

[](http://www.opendkim.org/opendkim-lua.3.html)
COPYRIGHT
---------

Copyright (c) 2009-2014, The Trusted Domain Project. All rights reserved.

[](http://www.opendkim.org/opendkim-lua.3.html)
SEE ALSO
--------

_opendkim(8), opendkim.conf(5)_

Lua -- http://www.lua.org

* * *
