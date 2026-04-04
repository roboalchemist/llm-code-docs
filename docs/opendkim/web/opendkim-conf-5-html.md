# Source: http://www.opendkim.org/opendkim.conf.5.html

Title: opendkim.conf

URL Source: http://www.opendkim.org/opendkim.conf.5.html

Markdown Content:
[NAME](http://www.opendkim.org/opendkim.conf.5.html#NAME)

[LOCATION](http://www.opendkim.org/opendkim.conf.5.html#LOCATION)

[DESCRIPTION](http://www.opendkim.org/opendkim.conf.5.html#DESCRIPTION)

[PARAMETERS](http://www.opendkim.org/opendkim.conf.5.html#PARAMETERS)

[NOTES](http://www.opendkim.org/opendkim.conf.5.html#NOTES)

[FILES](http://www.opendkim.org/opendkim.conf.5.html#FILES)

[VERSION](http://www.opendkim.org/opendkim.conf.5.html#VERSION)

[COPYRIGHT](http://www.opendkim.org/opendkim.conf.5.html#COPYRIGHT)

[SEE ALSO](http://www.opendkim.org/opendkim.conf.5.html#SEE%20ALSO)

* * *

[](http://www.opendkim.org/opendkim.conf.5.html)
NAME
----

**opendkim.conf** − Configuration file for opendkim

[](http://www.opendkim.org/opendkim.conf.5.html)
LOCATION
--------

_@SYSCONFDIR@/opendkim.conf_

[](http://www.opendkim.org/opendkim.conf.5.html)
DESCRIPTION
-----------

_opendkim(8)_ implements the **DKIM** specification for signing and verifying e-mail messages on a per-domain basis. This file is its configuration file.

Blank lines are ignored. Lines containing a hash ("#") character are truncated at the hash character to allow for comments in the file.

Other content should be the name of a parameter, followed by white space, followed by the value of that parameter, each on a separate line.

For parameters that are Boolean in nature, only the first byte of the value is processed. For positive values, the following are accepted: "T", "t", "Y", "y", "1". For negative values, the following are accepted: "F", "f", "N", "n", "0".

Many, but not all, of these parameters are also available as command line options to _opendkim(8)._ However, new parameters are generally not added as command line options so the complete set of options is available here, and thus use of the configuration file is encouraged. In some future release, the set of available command line options is likely to get trimmed.

See the _opendkim(8)_ man page for details about how and when the configuration file contents are reloaded.

Some of these parameters are listed as having a type of "dataset". See the _opendkim(8)_ man page for a description of such parameters.

Unless otherwise stated, Boolean values default to "false", integer values default to 0, and string and dataset values default to being undefined.

[](http://www.opendkim.org/opendkim.conf.5.html)
PARAMETERS
----------

_AllowSHA1Only (Boolean)_

Permit verify mode when only SHA1 support is available. RFC6376 requires that verifiers implement both SHA1 and SHA256 support. Setting this feature changes the absence of SHA256 support from an error to a warning.

_AlwaysAddARHeader (Boolean)_

Add an "Authentication-Results:" header field even to unsigned messages from domains with no "signs all" policy. The reported DKIM result will be "none" in such cases. Normally unsigned mail from non-strict domains does not cause the results header field to be added.

_AuthservID (string)_

Sets the "authserv-id" to use when generating the Authentication-Results: header field after verifying a message. The default is to use the name of the MTA processing the message. If the string "HOSTNAME" is provided, the name of the host running the filter (as returned by the _gethostname(3)_ function) will be used.

_AuthservIDWithJobID (Boolean)_

If "true", requests that the authserv-id portion of the added Authentication-Results: header fields contain the job ID of the message being evaluated.

_AutoRestart (Boolean)_

Automatically re-start on failures. Use with caution; if the filter fails instantly after it starts, this can cause a tight _fork(2)_ loop.

_AutoRestartCount (integer)_

Sets the maximum automatic restart count. After this number of automatic restarts, the filter will give up and terminate. A value of 0 implies no limit; this is the default.

_AutoRestartRate (string)_

Sets the maximum automatic restart rate. If the filter begins restarting faster than the rate defined here, it will give up and terminate. This is a string of the form _n/t[u]_ where _n_ is an integer limiting the count of restarts in the given interval and _t[u]_ defines the time interval through which the rate is calculated; _t_ is an integer and _u_ defines the units thus represented ("s" or "S" for seconds, the default; "m" or "M" for minutes; "h" or "H" for hours; "d" or "D" for days). For example, a value of "10/1h" limits the restarts to 10 in one hour. There is no default, meaning restart rate is not limited.

_Background (Boolean)_

Causes _opendkim_ to fork and exits immediately, leaving the service running in the background. The default is "true".

_BaseDirectory (string)_

If set, instructs the filter to change to the specified directory using _chdir(2)_ before doing anything else. This means any files referenced elsewhere in the configuration file can be specified relative to this directory. It’s also useful for arranging that any crash dumps will be saved to a specific location.

_BodyLengthDB (dataset)_

Requests that _opendkim_ include a "l=" body length tag when the set contains any of the envelope recipient addresses. The addresses presented are tested against the database in various forms as described under the _SigningTable_ setting (below). This feature of the protocol exists to improve the likelihood that a signature will survive transit through a mailing list server, as they commonly append footers to messages. Note, however, that this creates a potential security issue since someone could add arbitrary text to the signed message and the signature would still validate. See the DKIM specification for details.

_BogusKey (string)_

Instructs the filter to treat a passing signature associated with a bogus (forged) key in a special way. Possible values are _neutral_ (return a "neutral" result), _none_ (take no special action) and _fail_ (return a "fail" result; this is the default). @UNBOUND_MANNOTICE@

_CaptureUnknownErrors (Boolean)_

When set, and on systems where MTA quarantine is available, the filter will request quarantine of a message that results in an internal error or resource exhaustion.

_Canonicalization (string)_

Selects the canonicalization method(s) to be used when signing messages. When verifying, the message’s DKIM-Signature: header field specifies the canonicalization method. The recognized values are _relaxed_ and _simple_ as defined by the DKIM specification. The default is _simple._ The value may include two different canonicalizations separated by a slash ("/") character, in which case the first will be applied to the header and the second to the body.

_ChangeRootDirectory (string)_

Requests that the operating system change the effective root directory of the process to the one specified here prior to beginning execution. **chroot**(2) requires superuser access. A warning will be generated if _UserID_ is not also set.

_ClockDrift (integer)_

Sets the tolerance in seconds to be applied when determining whether a signature was either expired or generated in the future. The default is 300.

_Diagnostics (Boolean)_

Requests the inclusion of "z=" tags in signatures, which encode the original header field set for use by verifiers when diagnosing verification failures. Not recommended for normal operation.

_DiagnosticDirectory (string)_

Directory into which to write diagnostic reports when message verification fails on a message bearing a "z=" tag. If not set (the default), these files are not generated.

_DisableCryptoInit (Boolean)_

If set, skips initialization of the SSL library initialization steps, which are normaly required in multi-threaded environments. This assumes some other library opendkim is using will do the required initialization and shutdown.

_DNSConnect (Boolean)_

Requests that the asynchronous resolver start using TCP immediately rather than using UDP until TCP is actually needed. Does not work with all resolvers.

_DNSTimeout (integer)_

Sets the DNS timeout in seconds. A value of 0 causes an infinite wait. The default is 5. Ignored if not using an asynchronous resolver package. See also the NOTES section below.

_Domain (dataset)_

A set of domains whose mail should be signed by this filter. Mail from other domains will be verified rather than being signed.

This parameter is not required if a _SigningTable_ is in use; in that case, the list of signed domains is implied by the lines in that file.

This parameter is ignored if a _KeyTable_ is defined.

_DomainKeysCompat (boolean)_

If set, backward compatibility with DomainKeys (RFC4870) key records is enabled. When not set, such keys are considered to be syntactically invalid. The default is "false".

_DontSignMailTo (dataset)_

A set of e-mail address, mail to which should never be signed by the filter. Note that this is an "any" feature; if any one of the recipients of the message matches a member of this list, the message will not be signed.

_EnableCoredumps (boolean)_

On systems that have such support, make an explicit request to the kernel to dump cores when the filter crashes for some reason. Some modern UNIX systems suppress core dumps during crashes for security reasons if the user ID has changed during the lifetime of the process. Currently only supported on Linux.

_ExemptDomains (dataset)_

Specifies a set of domains, mail from which should be ignored entirely by the filter. This is similar to the _PeerList_ setting except that it bases its decision on the sender of the message as identified from the header fields or other message data, not the identity of the SMTP client sending the message.

_ExternalIgnoreList (dataset)_

Identifies a set of "external" hosts that may send mail through the server as one of the signing domains without credentials as such. This has the effect of suppressing the "external host (hostname) tried to send mail as (domain)" log messages. Entries in the data set should be of the same form as those of the _PeerList_ option below. The set is empty by default.

_FinalPolicyScript (string)_

Gives the name of a Lua script that should be run after the entire message has been received. This can be used to enact local policy decisions such as message rejection, quarantine, rerouting, etc. based on signatures found on the message, the results of attempts to verify them, and other properties of the message or signatures. See _opendkim-lua(3)_ for details. @LUA_MANNOTICE@

_FixCRLF (Boolean)_

Requests that the DKIM library convert bare CRs and LFs to CRLFs during body canonicalization, anticipating that an MTA somewhere before delivery will do that conversion anyway. The default is to leave them as-is.

_IdentityHeader (string)_

This specifies the header field where an identity is stored. @IDENTITY_HEADER_MANNOTICE@

_IdentityHeaderRemove (Boolean)_

Remove the _IdentityHeader_ after signing. @IDENTITY_HEADER_MANNOTICE@

_IgnoreMalformedMail (boolean)_

Silently passes malformed messages without alteration. This includes messages that fail the _RequiredHeaders_ check, if enabled. The default is to pass those messages but add an Authentication-Results field indicating that they were malformed.

_Include (string)_

Names a file to be opened and read as an additional configuration file. Nesting is allowed to a maximum of five levels.

_InternalHosts (dataset)_

Identifies a set internal hosts whose mail should be signed rather than verified. Entries in this data set follow the same form as those of the _PeerList_ option below. If not specified, the default of "127.0.0.1" is applied. Naturally, providing a value here overrides the default, so if mail from 127.0.0.1 should be signed, the list provided here should include that address explicitly.

_KeepAuthResults (boolean)_

Suppresses removal of Authentication-Results header fields containing DKIM results apparently added by this filter (usually the result of a misconfiguration or a forgery).

_KeepTemporaryFiles (boolean)_

Instructs the filter to create temporary files containing the header and body canonicalizations of messages that are signed or verified. The location of these files can be set using the _TemporaryDirectory_ parameter. Intended only for debugging verification problems.

_KeyFile (string)_

Gives the location of a PEM-formatted private key to be used for signing all messages. Ignored if a _KeyTable_ is defined.

_KeyTable (dataset)_

Gives the location of a file mapping key names to signing keys. If present, overrides any _KeyFile_ setting in the configuration file. The data set named here maps each key name to three values: (a) the name of the domain to use in the signature’s "d=" value; (b) the name of the selector to use in the signature’s "s=" value; and (c) either a private key or a path to a file containing a private key. If the first value consists solely of a percent sign ("%") character, it will be replaced by the apparent domain of the sender when generating a signature. If the third value starts with a slash ("/") character, or "./" or "../", then it is presumed to refer to a file from which the private key should be read, otherwise it is itself a PEM-encoded private key or a base64-encoded DER private key; a "%" in the third value in this case will be replaced by the apparent domain name of the sender. The _SigningTable_ (see below) is used to select records from this table to be used to add signatures based on the message sender.

_LDAPAuthMechanism (string)_

Names the authentication mechanism to use when connecting to an LDAP server. The default is the empty string, meaning "simple" authentication should be done.

_LDAPAuthName (string)_

Specifies the authenticating name to use when using SASL to authenticate to an LDAP server. Requires SASL support be installed on the local system. There is no default.

_LDAPAuthRealm (string)_

Specifies the authentication realm to use when using SASL to authenticate to an LDAP server. Requires SASL support be installed on the local system. There is no default.

_LDAPAuthUser (string)_

Specifies the authenticating user to use when using SASL to authenticate to an LDAP server. Requires SASL support be installed on the local system. There is no default.

_LDAPBindPassword (string)_

Specifies the password to use when conducting an LDAP "bind" operation. There is no default.

_LDAPBindUser (string)_

Specifies the user ID to use when conducting an LDAP "bind" operation. There is no default.

_LDAPDisableCache (Boolean)_

Suppresses creation of a local cache in front of LDAP queries.

_LDAPKeepaliveIdle (integer)_

Sets the number of seconds a connection to an LDAP server needs to remain idle before TCP starts sending keepalive probes. If not specified, the LDAP library default is used.

_LDAPKeepaliveInterval (integer)_

Sets the interval in seconds between TCP keepalive probes. If not specified, the LDAP library default is used.

_LDAPKeepaliveProbes (integer)_

Sets the maximum number of keepalive probes TCP should send before abandoning the connection. If not specified, the LDAP library default is used.

_LDAPTimeout (integer)_

Sets the time in seconds after which an LDAP operation should be abandoned. The default is 5.

_LDAPUseTLS (Boolean)_

Indicates whether or not a TLS connection should be established when contacting an LDAP server. The default is "False".

_LogResults (boolean)_

If logging is enabled (see _Syslog_ below), requests that the results of evaluation of all signatures that were at least partly intact (i.e., the "d=", "s=", and "b=" tags could be extracted).

_LogWhy (boolean)_

If logging is enabled (see _Syslog_ below), issues very detailed logging about the logic behind the filter’s decision to either sign a message or verify it. The logic behind the decision is non-trivial and can be confusing to administrators not familiar with its operation. A description of how the decision is made can be found in the OPERATIONS section of the _opendkim(8)_ man page. This causes a large increase in the amount of log data generated for each message, so it should be limited to debugging use and not enabled for general operation.

_MacroList (dataset)_

Defines a set of MTA-provided _macros_ that should be checked to see if the sender has been determined to be a local user and therefore whether or not the message should be signed. If a _value_ is specified matching a macro name in the data set, the value of the macro must match a value specified (matching is case-sensitive), otherwise the macro must be defined but may contain any value. The set is empty by default, meaning macros are not considered when making the sign-verify decision. The general format of the value is _value1[|value2[|...]];_ if one or more value is defined then the macro must be set to one of the listed values, otherwise the macro must be set but can contain any value.

In order for the macro and its value to be available to the filter for checking, the MTA must send it during the protocol exchange. This is either accomplished via manual configuration of the MTA to send the desired macros or, for MTA/filter combinations that support the feature, the filter can request those macros that are of interest. The latter is a feature negotiated at the time the filter receives a connection from the MTA and its availability depends upon the version of milter used to compile the filter and the version of the MTA making the connection.

This data set must be of type "file" or "csl".

_MaximumHeaders (integer)_

Defines the maximum number of bytes the header block of a message may consume before the filter will reject the message. This mitigates a denial-of-service attack in which a client connects to the MTA and begins feeding an unbounded number of header fields of arbitrary size; since the filter keeps a cache of these, the attacker could cause the filter to allocate an unspecified amount of memory. The default is 65536; a value of 0 removes the limit.

_MaximumSignaturesToVerify (integer)_

Defines the maximum number of signatures on a message for which verification should be conducted. The default is three. Signatures are selected from the top of the message downward. If _TrustSignaturesFrom_ is set, signatures from domains in that data set are always verified, which may consume part or all of, or even exceed, this limit.

_MaximumSignedBytes (integer)_

Specifies the maximum number of bytes of message body to be signed. Messages shorter than this limit will be signed in their entirety. Setting this value implies use of _BodyLengthDB_ for all addresses.

_MilterDebug (integer)_

Sets the debug level to be requested from the milter library. The default is 0.

_Minimum (string)_

Instructs the verification code to fail messages for which a partial signature was received. There are three possible formats: _min_ indicating at least _min_ bytes of the message must be signed (or if the message is smaller than _min_ then all of it must be signed); _min%_ requiring that at least _min_ percent of the received message must be signed; and _min+_ meaning there may be no more than _min_ bytes of unsigned data appended to the message for it to be considered valid.

_MinimumKeyBits (integer)_

Establishes a minimum key size for acceptable signatures. Signatures with smaller key sizes, even if they otherwise pass DKIM validation, will me marked as invalid. The default is 1024, which accepts all signatures. A value of 0 causes the default to be used.

_Mode (string)_

Selects operating modes. The string is a concatenation of characters that indicate which mode(s) of operation are desired. Valid modes are _s_ (signer) and _v_ (verifier). The default is _sv_ except in test mode (see the _opendkim(8)_ man page) in which case the default is _v._ When signing mode is enabled, one of the following combinations must also be set: (a) Domain, KeyFile, Selector, no KeyTable, no SigningTable; (b) KeyTable, SigningTable, no Domain, no KeyFile, no Selector; (c) KeyTable, SetupPolicyScript, no Domain, no KeyFile, no Selector.

_MTA (dataset)_

A set of MTA names (a la the _sendmail(8)_ DaemonPortOptions Name parameter) whose mail should be signed by this filter. There is no default, meaning MTA name is not considered when making the sign-verify decision.

_MTACommand (string)_

Specifies the path to an executable to be used for sending mail such as that generated by _SendReports._ The default is @SENDMAIL_PATH@. The executable should accept typical **sendmail(8)** command line options "−t" (take addresses from message body) and "−f" (set envelope sender), accept the new message on its standard input, and return a non-zero exit status on any error.

_MultipleSignatures (Boolean)_

Allow addition of multiple signatures when a signing table is in use. See _SigningTable_ for more information.

_MustBeSigned (dataset)_

Specifies a set of header fields that, if present, must be covered by the DKIM signature when verifying a message. If a header field in this set is present in the message and is not signed, the filter will treat even an otherwise valid signature as invalid. The default is an empty list.

_Nameservers (string)_

Provides a comma-separated list of IP addresses that are to be used when doing DNS queries to retrieve DKIM keys, VBR records, etc. These override any local defaults built in to the resolver in use, which may be defined in _/etc/resolv.conf_ or hard-coded into the software.

_NoHeaderB (Boolean)_

If set, this feature suppresses the use of "header.b" tags in added Authentication-Results header fields. The default is "false", which means those tags will be applied.

_OmitHeaders (dataset)_

Specifies a set of header fields that should be omitted when generating signatures. If an entry in the list names any header field that is mandated by the DKIM specification, the entry is ignored. A set of header fields is listed in the DKIM specification (RFC6376, Section 5.4) as "SHOULD NOT" be signed; the default list for this parameter contains those fields (Return-Path, Received, Comments, Keywords, Bcc, Resent-Bcc and DKIM-Signature). To omit no headers, simply use the string "." (or any string that will match no header field names). Specifying a list with this parameter replaces the default entirely, unless one entry is "*" in which case the list is interpreted as a delta to the default; for example, "*,+foobar" will use the entire default list plus the name "foobar", while "*,-Bcc" would use the entire default list except for the "Bcc" entry.

_On-BadSignature (string)_

Selects the action to be taken when a signature fails to validate. Possible values (with abbreviated forms in parentheses): _accept_ (a) accept the message; _discard_ (d) discard the message; _quarantine_ (q) quarantine the message; _reject_ (r) reject the message; _tempfail_ (t) temp-fail the message. The default is _accept._ Note that the "t" (testing) flag in a DKIM key bypasses this behaviour; a bad signature that references a testing flag will still be delivered, though the added Authentication-Results field will indicate both the failed result and the test mode so that consumers of the message can take appropriate action.

_On-Default (string)_

Selects the action to be taken when any verification or internal error of any kind is encountered. This is processed before the other "On-" values so it can be used as a blanket setting followed by specific overrides.

_On-DNSError (string)_

Selects the action to be taken when a transient DNS error is encountered. Possible values are the same as those for _On-BadSignature._ The default is _tempfail._

_On-InternalError (string)_

Selects the action to be taken when an internal error of some kind is encountered. Possible values are the same as those for _On-BadSignature._ The default is _tempfail._

_On-KeyNotFound (string)_

Selects the action to be taken when the key referenced by a signature is not present in the DNS. Possible values are the same as those for _On-BadSignature._ The default is _accept._

_On-NoSignature (string)_

Selects the action to be taken when a message arrives unsigned. Possible values are the same as those for _On-BadSignature._ The default is _accept._

_On-Security (string)_

Selects the action to be taken when a message arrives containing properties that may be a security concern. Possible values are the same as those for _On-BadSignature._ The default is _tempfail._

_On-SignatureError (string)_

Selects the action to be taken when a message cannot be signed because of issues with the message or the key provided for signing. Possible values are the same as those for _On-BadSignature._ The default is _reject._

_OversignHeaders (dataset)_

Specifies a set of header fields that should be included in all signature header lists (the "h=" tag) once more than the number of times they were actually present in the signed message. The set is empty by default. The purpose of this, and especially of listing an absent header field, is to prevent the addition of important fields between the signer and the verifier. Since the verifier would include that header field when performing verification if it had been added by an intermediary, the signed message and the verified message were different and the verification would fail. Note that listing a field name here and not listing it in the _SignHeaders_ list is likely to generate invalid signatures.

_PeerList (dataset)_

Identifies a set of "peers" that identifies clients whose connections should be accepted without processing by this filter. The set should contain on each line a hostname, domain name (e.g. ".example.com"), IP address, an IPv6 address (including an IPv4 mapped address), or a CIDR-style IP specification (e.g. "192.168.1.0/24"). An entry beginning with a bang ("!") character means "not", allowing exclusions of specific hosts that are otherwise members of larger sets. Host and domain names are matched first, then the IP or IPv6 address depending on the connection type. More precise entries are preferred over less precise ones, i.e. "192.168.1.1" will match before "!192.168.1.0/24". The text form of IPv6 addresses will be forced to lowercase when queried (RFC5952), so the contents of this data set should also use lowercase. The IP address portion of an entry may optionally contain square brackets; both forms (with and without) will be checked.

_PidFile (string)_

Specifies the path to a file that should be created at process start containing the process ID.

_POPDBFile (dataset)_

Requests that the filter consult a set for IP addresses that should be allowed for signing. This feature was designed for POP-before-SMTP datastores. @POPAUTH_MANNOTICE@

_Quarantine (Boolean)_

Requests that messages which fail verification be quarantined by the MTA. (Requires a sufficiently recent version of the milter library.)

_QueryCache (Boolean)_

Instructs the DKIM library to maintain its own local cache of keys and policies retrieved from DNS, rather than relying on the nameserver for caching service. Useful if the nameserver being used by the filter is not local. @QUERY_CACHE_MANNOTICE@

_RedirectFailuresTo (address)_

Messages bearing signatures that failed to verify are redirected to the specified address. The original envelope recipient set is recorded in the header before redirection occurs. By default, no redirection is done.

_RemoveARAll (Boolean)_

Removes all Authentication-Results: header fields that also satisfy the requirements of _RemoveARFrom_ below. By default, only those containing a DKIM result are removed.

_RemoveARFrom (dataset)_

Defines a set of hostnames whose Authentication-Results: header fields should be removed before the message is passed for delivery. By default only those header fields matching the local host’s canonical name will be removed. Matching is only done on full hostnames (e.g. "host.example.com") or on domain names (e.g. ".example.com").

_RemoveOldSignatures (Boolean)_

Removes all existing signatures when operating in signing mode.

_ReplaceHeaders (data set)_

Defines a set of header fields that should be affected by the text replacement rules defined by the _ReplaceRules_ setting. By default, all header fields are included. @REPLACE_RULES_MANNOTICE@

_ReplaceRules (string)_

Specifies a file containing a list of text replacement rules that are applied to the message header fields to replace certain content expected to be changed as the message passes through local MTAs. This can be used to accommodate expected changes such as are made to From: fields by MTA "masquerade" features. Each entry in the file consists of a POSIX regular expression, followed by a tab (ASCII 9), followed by the text that should be used to replace the text matching the expression. The ’#’ character denotes the beginning of a comment and text from that point on in a single line is ignored. Blank lines are also skipped. @REPLACE_RULES_MANNOTICE@

_ReportAddress (string)_

Specifies the string to use in the From: header field for outgoing reports (see _SendReports_ below). If not specified, the executing user and local hostname will be used to construct the address.

_ReportBccAddress (string)_

Specifies address(es) to include in a Bcc: header field on outgoing reports (see _SendReports_ below). If multiple addresses are required, they should be comma separated.

_RequestReports (boolean)_

When signing, includes a request for signature evaluation failures in the signature. (See RFC6651 for details.)

_RequiredHeaders (boolean)_

Checks all messages for compliance with RFC5322 header field count requirements. Non-compliant messages are rejected.

_RequireSafeKeys (boolean)_

When reading a key file, a message will be logged if the key file has the read or write bit set other than for the owner or for a group that the executing process is in. With this feature set to "true", the filter will further consider this an error and refuse to make use of the file’s contents. The default is "true".

_ResignAll (boolean)_

Where _ResignMailTo_ triggers a re-signing action, this flag indicates whether or not all mail should be signed (if set) versus only verified mail being signed (if not set). The default is "false". @RESIGN_MANNOTICE@

_ResignMailTo (dataset)_

Checks each message recipient against the specified dataset for a matching record. The full address is checked in each case, then the hostname, then each domain preceded by ".". If there is a match, the value returned is presumed to be the name of a key in the _KeyTable_ (if defined) to be used to re-sign the message in addition to verifying it. If there is a match without a _KeyTable,_ the default key is applied. @RESIGN_MANNOTICE@

_ResolverConfiguration (string)_

Provides the given string as configuration information to the underlying resolver. For the standard UNIX resolver, this is unused; for Unbound, the string contains a filename that is considered to be a configuration file. There is no default.

_ResolverTracing (Boolean)_

Requests resolver tracing features be enabled, if available. The effect of this depends on how debugging features of the resolver might be implemented. Currently only effective with the OpenDKIM asynchronous resolver library.

_ScreenPolicyScript (string)_

Gives the name of a Lua script that should be run after all of the header fields have been processed for a message; in particular, this is useful after all DKIM signatures have been detected and initial evaluation has been done. The script has access to all of the header fields and connection information and can that certain signatures be ignored based on that information. See _opendkim-lua(3)_ for details. @LUA_MANNOTICE@

_SelectCanonicalizationHeader (string)_

Defines a header field name which, if present, adjusts which canonicalization will be used to generate an outgoing signature. Overrides the _Canonicalization_ setting if the header field is present. The default is "X-Canonicalization".

_Selector (string)_

Defines the name of the selector to be used when signing messages. See the **DKIM** specification for details. Used only when signing with a single key; see the _SigningTable_ parameter below for more information.

This parameter is ignored if a _KeyTable_ is defined.

_SenderHeaders (dataset)_

Specifies an ordered list of header fields that should be searched to determine the sender of a message. The first header field found is the one whose value is used. This is mainly used when signing for deciding which signing request(s) to make. By default, the "From" header field is the only one checked. See the _OmitHeaders_ setting for a description of possible values.

_SenderMacro (string)_

Use the milter macro string to determine the sender of the message. @SENDER_MACRO_MANNOTICE@

_SendReports (Boolean)_

If true, when a signature verification fails and the signature included a reporting request ("r=y") and the signing domain advertises a reporting address (i.e. _ra=user)_ in a reporting record in the DNS, the filter will send a structured report to that address containing details needed to reproduce the problem. See RFC6651 for a complete description of this mechanism.

_SetupPolicyScript (string)_

Gives the name of a Lua script that should be run once all header fields for a message have arrived. The script has access to all of the header fields and connection information and can request DKIM verification or signing based on that information. See _opendkim-lua(3)_ for details. @LUA_MANNOTICE@

_SignatureAlgorithm (string)_

Selects the signing algorithm to use when generating signatures. Use ’opendkim −V’ to see the list of supported algorithms. The default is _rsa-sha256_ if it is available, otherwise it will be _rsa-sha1._

_SignatureTTL (integer)_

Sets the time-to-live, in seconds, of signatures generated by the filter. If not set, no expiration time is added to signatures.

_SignHeaders (dataset)_

Specifies the set of header fields that should be included when generating signatures. If the list omits any header field that is mandated by the DKIM specification, those fields are implicitly added. By default, those fields listed in the DKIM specification as "SHOULD" be signed (RFC6376, Section 5.4) will be signed by the filter. See the _OmitHeaders_ configuration option for more information about the format and interpretation of this field.

_SigningTable (dataset)_

Defines a table used to select one or more signatures to apply to a message based on the address found in the From: header field. Keys in this table vary depending on the type of table used; values in this data set should include one field that contains a name found in the _KeyTable_ (see above) that identifies which key should be used in generating the signature, and an optional second field naming the signer of the message that will be included in the "i=" tag in the generated signature. Note that the "i=" value will not be included in the signature if it conflicts with the signing domain (the "d=" value).

If the first field contains only a "%" character, it will be replaced by the domain found in the From: header field. Similarly, within the optional second field, any "%" character will be replaced by the domain found in the From: header field.

If this table specifies a regular expression file ("refile"), then the keys are wildcard patterns that are matched against the address found in the From: header field. Entries are checked in the order in which they appear in the file.

For all other database types, the full _user@host_ is checked first, then simply _host,_ then _user@.domain_ (with all superdomains checked in sequence, so "foo.example.com" would first check "user@foo.example.com", then "user@.example.com", then "user@.com"), then _.domain,_ then _user@*,_ and finally _*._

In any case, only the first match is applied, unless _MultipleSignatures_ is enabled in which case all matches are applied.

_SMTPURI (string)_

Specifies a URI (e.g., "smtp://localhost") to which mail should be sent via SMTP when notifications are generated. @LIBCURL_MANNOTICE@

_Socket (string)_

Specifies the socket that should be established by the filter to receive connections from _sendmail(8)_ in order to provide service. _socketspec_ is in one of two forms: _local:path,_ which creates a UNIX domain socket at the specified _path,_ or _inet:port[@host]_ or _inet6:port[@host]_ which creates a TCP socket on the specified _port_ and in the specified protocol family. If the _host_ is not given as either a hostname or an IP address, the socket will be listening on all interfaces. A literal IP address must be enclosed in square brackets. This option is mandatory either in the configuration file or on the command line.

_SoftStart (Boolean)_

If set, the inability to connect and authenticate to an LDAP or SQL server will not prevent the filter from starting, and reconnections will be attempted for each query. The default is "False".

_SoftwareHeader (Boolean)_

Causes _opendkim_ to add an "DKIM-Filter" header field indicating the presence of this filter in the path of the message from injection to delivery. The product’s name, version, and the job ID are included in the header field’s contents. Note that the header field is not added if the _Mode_ setting causes the message to be ignored (e.g., if only signing mode is enabled and the configuration causes the message not to be signed, or only verify mode is enabled and configuration would otherwise have caused the message to be signed, then it will not have this header field added).

_Statistics (filename)_

This specifies a file in which to store DKIM transaction statistics. See _opendkim-stats(8)_ for a mechanism to parse the file’s contents, and _opendkim-importstats()_ for a mechanism to translate the file’s contents into SQL database insertions. @STATS_MANNOTICE@

_StatisticsName (string)_

Defines the name to be used as the reporting host in statistics logs. By default, the local host’s name returned by _gethostname(3)_ is used. @STATS_MANNOTICE@

_StatisticsPrefix (string)_

When _AnonymousStatistics_ is enabled, this string may be specified and will be prepended to all data before hashing for more complete anonymization. This means two records from different sources referencing the same source will still produce different hashes, meaning such correlation is now only possible within the data from a single repoter.

_StrictHeaders (Boolean)_

If set, instructs the DKIM library to refuse processing of a message if the header field count does not conform to RFC5322 Section 3.6.

_StrictTestMode (Boolean)_

Selects strict CRLF mode during testing (see the _-t_ command line flag in the _opendkim(8)_ man page); messages for which all header fields and body lines are not CRLF-terminated are considered malformed and will produce an error.

_SubDomains (Boolean)_

Sign subdomains of those listed by the _Domain_ parameter as well as the actual domains.

_Syslog (Boolean)_

Log via calls to _syslog(3)_ any interesting activity.

_SyslogFacility (string)_

Log via calls to _syslog(3)_ using the named facility. The facility names are the same as the ones allowed in _syslog.conf(5)._ The default is "mail".

_SyslogSuccess (Boolean)_

Log via calls to _syslog(3)_ additional entries indicating successful signing or verification of messages.

_TemporaryDirectory (string)_

Specifies the directory in which temporary canonicalization files should be written. The default is to use the _libdkim_ default location, currently _/tmp._

_TestDNSData (data set)_

Provides a data set whose keys will be treated as DNS record names and values as TXT record contents. Intended for use during automated testing.

_TestPublicKeys (string)_

Names a file from which public keys should be read. Intended for use only during automated testing.

_TrustAnchorFile (string)_

Specifies a file from which trust anchor data should be read when doing DNS queries and applying the DNSSEC protocol. This is currently ignored unless the underlying library is compiled to use Unbound; see the documentation at at http://unbound.net for the expected format of this file.

_TrustSignaturesFrom (dataset)_

This value consists of a set of domains that are considered trustworthy in terms of third-party signatures. That is, if a message arrives with a signature from a domain that doesn’t match the domain in the From: header, this setting determines whether or not that signature will be trusted. If this value is undefined, all signatures are trusted.

_UMask (integer)_

Requests a specific permissions mask to be used for file creation. This only really applies to creation of the socket when _Socket_ specifies a UNIX domain socket, and to the _PidFile_ (if any); temporary files are created by the _mkstemp(3)_ function that enforces a specific file mode on creation regardless of the process umask. See _umask(2)_ for more information.

_UnprotectedKey (string)_

Instructs the filter to treat a passing signature associated with a key found in an insecure (i.e. not protected by DNSSEC) DNS record in a special way. Possible values are _neutral_ (return a "neutral" result), _none_ (take no special action; this is the default) and _fail_ (return a "fail" result). @UNBOUND_MANNOTICE@

_UserID (string)_

Attempts to become the specified userid before starting operations. The value is of the form _userid[:group]._ The process will be assigned all of the groups and primary group ID of the named _userid_ unless an alternate _group_ is specified.

_VBR-Certifiers (string)_

The default certifiers if not specified in X-VBR-Certifiers header field. @VBR_MANNOTICE@

_VBR-PurgeFields (string)_

If set, arranges to remove X-VBR-Certifiers and X-VBR-Type fields on messages prior to sending them. @VBR_MANNOTICE@

_VBR-TrustedCertifiers (string)_

A colon or comma sparated list of trusted certifiers to accept when verifying VBR-Info header field. @VBR_MANNOTICE@

_VBR-TrustedCertifiersOnly (Boolean)_

By default, the certifiers that are in both the trusted certifiers list (above) and those in the message’s VBR-Info header field will be checked for vouching. With this option set, the trusted certifiers will be checked and the ones claimed by the message will be ignored. @VBR_MANNOTICE@

_VBR-Type (string)_

This default VBR type if not specified in the X-VBR-Type header field. @VBR_MANNOTICE@

_WeakSyntaxChecks (Boolean)_

Requests that the library continue processing messages even if syntax errors are discovered early in message analysis. This means, for example, that a signed message with a mangled From: field will still proceed to verification even if the author’s domain could not be determined.

[](http://www.opendkim.org/opendkim.conf.5.html)
NOTES
-----

When using DNS timeouts (see the _DNSTimeout_ option above), be sure not to use a timeout that is larger than the timeout being used for interaction between _sendmail_ and the filter. Otherwise, the MTA could abort a message while waiting for a reply from the filter, which in turn is still waiting for a DNS reply.

Features that involve specification of IPv4 addresses or CIDR blocks will use the _inet\_addr(3)_ function to parse that information. Users should be familiar with the way that function handles the non-trivial cases (for example, "192.0.2/24" and "192.0.2.0/24" are not the same thing).

[](http://www.opendkim.org/opendkim.conf.5.html)
FILES
-----

_@SYSCONFDIR@/opendkim.conf_

Default location of this file.

[](http://www.opendkim.org/opendkim.conf.5.html)
VERSION
-------

This man page covers version @VERSION@ of _opendkim._

[](http://www.opendkim.org/opendkim.conf.5.html)
COPYRIGHT
---------

Copyright (c) 2007, 2008, Sendmail, Inc. and its suppliers. All rights reserved.

Copyright (c) 2009-2015, The Trusted Domain Project. All rights reserved.

[](http://www.opendkim.org/opendkim.conf.5.html)
SEE ALSO
--------

_opendkim(8), opendkim-lua(3), sendmail(8)_

RFC5451 - Message Header Field for Indicating Message Authentication Status

RFC5617 - DKIM Author Domain Signing Practises

RFC5965 - An Extensible Format for Email Feedback Reports

RFC6008 - Authentication-Results Registration for Differentiating among Cryptographic Results

RFC6376 - DomainKeys Identified Mail

RFC6651 - Extensions to DomainKeys Identified Mail (DKIM) for Failure Reporting

* * *
