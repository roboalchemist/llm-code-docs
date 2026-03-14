# Source: http://www.opendkim.org/libopendkim/index.html

Title: OpenDKIM Library (libopendkim)

URL Source: http://www.opendkim.org/libopendkim/index.html

Markdown Content:
OpenDKIM Library (libopendkim)
===============

OpenDKIM Library (libopendkim)
==============================

Introduction
------------

**DomainKeys Identified Mail** ("DKIM") is a specification for signing messages at the domain level using simple cryptographic methods to indicate that the signing domain accepts some responsibility for the message. While the most obvious application of this is to defend against forged mail, other applications can make use of this capability. 
DKIM is an amalgamation of DomainKeys, created by Yahoo!, Inc., and Internet Identified Mail (IIM) created by Cisco, Inc. Both can be found as historical RFCs documents via the IETF web sites. More information about DomainKeys can be found [here](http://antispam.yahoo.com/domainkeys).

This API (libopendkim) allows an application to sign or verify messages according to the **DKIM** proposed standard. It also includes a number of extensions to support other protocols that are not part of DKIM itself. Support is included for ADSP, a mechanism for determining whether or not the purported author domain claims all of its mail is signed. Also provided is an implementation of a filter, using Sendmail's **milter** package, that uses libopendkim to implement this facility.

Data Types
----------

**Data Type****Description**
[DKIM](http://www.opendkim.org/libopendkim/dkim.html)A signing/verifying context for a message.
[dkim_alg_t](http://www.opendkim.org/libopendkim/dkim_alg_t.html)A signature generation/verification method.
[dkim_atps_t](http://www.opendkim.org/libopendkim/dkim_atps_t.html)An Authorized Third-Party Signer test result.
[dkim_canon_t](http://www.opendkim.org/libopendkim/dkim_canon_t.html)A canonicalization method.
[DKIM_CBSTAT](http://www.opendkim.org/libopendkim/dkim_cbstat.html)Return value/status from user-provided callbacks.
[DKIM_DNSSEC](http://www.opendkim.org/libopendkim/dkim_dnssec.html)Key record security evaluation codes.
[DKIM_LIB](http://www.opendkim.org/libopendkim/dkim_lib.html)An instance of the libopendkim service.
[dkim_param_t](http://www.opendkim.org/libopendkim/dkim_param_t.html)A signature parameter.
[dkim_query_t](http://www.opendkim.org/libopendkim/dkim_query_t.html)A key query method.
[DKIM_QUERYINFO](http://www.opendkim.org/libopendkim/dkim_queryinfo.html)A handle describing a required DNS query.
[DKIM_SIGERROR](http://www.opendkim.org/libopendkim/dkim_sigerror.html)Signature evaluation error codes.
[DKIM_SIGINFO](http://www.opendkim.org/libopendkim/dkim_siginfo.html)Private handle referencing information about a particular signature on a signed message.
[dkim_sigkey_t](http://www.opendkim.org/libopendkim/dkim_sigkey_t.html)Private key data.
[DKIM_STAT](http://www.opendkim.org/libopendkim/dkim_stat.html)Return value/status.

Functions
---------

**Function****Description**
**Administration**
[dkim_init()](http://www.opendkim.org/libopendkim/dkim_init.html)Initialize an instance of the **DKIM** service.
[dkim_flush_cache()](http://www.opendkim.org/libopendkim/dkim_flush_cache.html)Flush the key cache.
[dkim_getcachestats()](http://www.opendkim.org/libopendkim/dkim_getcachestats.html)Retrieve caching statistics.
[dkim_geterror()](http://www.opendkim.org/libopendkim/dkim_geterror.html)Retrieve the most recent internal error message associated with a DKIM handle.
[dkim_getmode()](http://www.opendkim.org/libopendkim/dkim_getmode.html)Return the mode (signing or verifying) of a DKIM handle.
[dkim_get_signer()](http://www.opendkim.org/libopendkim/dkim_get_signer.html)Retrieve the current message signer (if any).
[dkim_get_user_context()](http://www.opendkim.org/libopendkim/dkim_get_user_context.html)Retrieve a specific user context pointer for a sign or verify operation previously set by a call to dkim_set_user_context().
[dkim_libfeature()](http://www.opendkim.org/libopendkim/dkim_libfeature.html)Test for availability of a particular feature in the library.
[dkim_libversion()](http://www.opendkim.org/libopendkim/dkim_libversion.html)Retrieve the version of libopendkim against which the application is linked.
[dkim_set_dns_callback()](http://www.opendkim.org/libopendkim/dkim_set_dns_callback.html)Request a call back into the main program from time to time while waiting for DNS results.
[dkim_set_final()](http://www.opendkim.org/libopendkim/dkim_set_final.html)Provide a function to perform final signature analysis and/or re-ordering during verifications.
[dkim_set_key_lookup()](http://www.opendkim.org/libopendkim/dkim_set_key_lookup.html)Provide a function to perform key lookups, replacing the internal implementation. Includes support for asynchronous operation.
[dkim_set_prescreen()](http://www.opendkim.org/libopendkim/dkim_set_prescreen.html)Provide a function to perform signature prescreening and/or re-ordering during verifications.
[dkim_set_signature_handle()](http://www.opendkim.org/libopendkim/dkim_set_signature_handle.html)Provide a function to allocate a user-side signature description structure and return a pointer to it.
[dkim_set_signature_handle_free()](http://www.opendkim.org/libopendkim/dkim_set_signature_handle_free.html)Provide a function to deallocate a user-side signature description structure.
[dkim_set_signature_tagvalues()](http://www.opendkim.org/libopendkim/dkim_set_signature_tagvalues.html)Provide a function to receive signature-specific tags and values for user-side analysis.
[dkim_set_user_context()](http://www.opendkim.org/libopendkim/dkim_set_user_context.html)Set a specific user context pointer for a sign or verify operation which will be passed to user callbacks.
[dkim_ssl_version()](http://www.opendkim.org/libopendkim/dkim_ssl_version.html)Retrieve the OpenSSL version used when the library was compiled.
[dkim_close()](http://www.opendkim.org/libopendkim/dkim_close.html)Terminate an instance of the **DKIM** service.
**Signing**
[dkim_sign()](http://www.opendkim.org/libopendkim/dkim_sign.html)Allocate a new **DKIM** handle for signing a message.
[dkim_add_querymethod()](http://www.opendkim.org/libopendkim/dkim_add_querymethod.html)Indicate to verifiers which signing method(s) and option(s) should be used to retrieve the public key for verification.
[dkim_add_xtag()](http://www.opendkim.org/libopendkim/dkim_add_xtag.html)Add an extension tag and corresponding value.
[dkim_getpartial()](http://www.opendkim.org/libopendkim/dkim_getpartial.html)Check partial signature request flag.
[dkim_getsighdr()](http://www.opendkim.org/libopendkim/dkim_getsighdr.html)Generate and return a signature header into a fixed-size buffer.
[dkim_getsighdr_d()](http://www.opendkim.org/libopendkim/dkim_getsighdr_d.html)Generate and return a signature header in a dynamically-allocated buffer.
[dkim_privkey_load()](http://www.opendkim.org/libopendkim/dkim_privkey_load.html)Attempt to parse and load a signing key.
[dkim_set_margin()](http://www.opendkim.org/libopendkim/dkim_set_margin.html)Set the wrapping margin to use for signature header generation.
[dkim_set_signer()](http://www.opendkim.org/libopendkim/dkim_set_signer.html)Set the message signer.
[dkim_setpartial()](http://www.opendkim.org/libopendkim/dkim_setpartial.html)Request "l=" tag on a signature.
[dkim_signhdrs()](http://www.opendkim.org/libopendkim/dkim_signhdrs.html)Select header fields to be signed for this message, overriding the default.
**Verifying**
[dkim_verify()](http://www.opendkim.org/libopendkim/dkim_verify.html)Allocate a new **DKIM** handle for verifying a message.
[dkim_atps_check()](http://www.opendkim.org/libopendkim/dkim_atps_check.html)Perform an Authorized Third-Party Signer check.
[dkim_diffheaders()](http://www.opendkim.org/libopendkim/dkim_diffheaders.html)Compare original headers to received headers and look for approximate matches to identify header munging in order to explain verification failures.
[dkim_get_reputation()](http://www.opendkim.org/libopendkim/dkim_get_reputation.html)Query a DKIM reputation service.
[dkim_getdomain()](http://www.opendkim.org/libopendkim/dkim_getdomain.html)Return the sending domain from a message represented by a DKIM handle.
[dkim_getresultstr()](http://www.opendkim.org/libopendkim/dkim_getresultstr.html)Translate a DKIM_STAT constant into a string.
[dkim_getsiglist()](http://www.opendkim.org/libopendkim/dkim_getsiglist.html)Retrieve the array of signature handles associated with a message.
[dkim_getsignature()](http://www.opendkim.org/libopendkim/dkim_getsignature.html)Retrieve the signature handle to be used for final message disposition.
[dkim_getsslbuf()](http://www.opendkim.org/libopendkim/dkim_getsslbuf.html)Retrieve the SSL error buffer for a DKIM signing handle.
[dkim_getuser()](http://www.opendkim.org/libopendkim/dkim_getuser.html)Return the sending user from a message represented by a DKIM handle.
[dkim_minbody()](http://www.opendkim.org/libopendkim/dkim_minbody.html)Return number of bytes required to satisfy all active canonicalizations referenced by a DKIM handle.
[dkim_ohdrs()](http://www.opendkim.org/libopendkim/dkim_ohdrs.html)Retrieve the original header set from a signature if such were present.
[dkim_sig_getbh()](http://www.opendkim.org/libopendkim/dkim_sig_getbh.html)Retrieve body hash test result from a signature handle.
[dkim_sig_getcanonlen()](http://www.opendkim.org/libopendkim/dkim_sig_getcanonlen.html)Retrieve information regarding total canonicalized body length, and the size of what was actually signed.
[dkim_sig_getcanons()](http://www.opendkim.org/libopendkim/dkim_sig_getcanons.html)Retrieve the canonicalization modes used to generate a signature.
[dkim_sig_getcontext()](http://www.opendkim.org/libopendkim/dkim_sig_getcontext.html)Retrieve user-side context specific to a signature.
[dkim_sig_getdnssec()](http://www.opendkim.org/libopendkim/dkim_sig_getdnssec.html)Retrieve DNSSEC evaluation of a signature's key record.
[dkim_sig_getdomain()](http://www.opendkim.org/libopendkim/dkim_sig_getdomain.html)Retrieve the domain name found in the signature on a message.
[dkim_sig_geterror()](http://www.opendkim.org/libopendkim/dkim_sig_geterror.html)Retrieve the error code associated with a rejected/disqualified signature.
[dkim_sig_geterrorstr()](http://www.opendkim.org/libopendkim/dkim_sig_geterrorstr.html)Retrieve the text version of a signature error code.
[dkim_sig_getflags()](http://www.opendkim.org/libopendkim/dkim_sig_getflags.html)Retrieve processing flags from a signature handle.
[dkim_sig_getidentity()](http://www.opendkim.org/libopendkim/dkim_sig_getidentity.html)Retrieve the identity of the signing agent from a signature or message.
[dkim_sig_getkeysize()](http://www.opendkim.org/libopendkim/dkim_sig_getkeysize.html)Retrieve the size in bits of the key used to verify a message.
[dkim_sig_getqueries()](http://www.opendkim.org/libopendkim/dkim_sig_getqueries.html)Get the set of DNS queries needed to complete signature validation.
[dkim_sig_getreportinfo()](http://www.opendkim.org/libopendkim/dkim_sig_getreportinfo.html)Retrieve information required to generate a verification failure report.
[dkim_sig_getselector()](http://www.opendkim.org/libopendkim/dkim_sig_getselector.html)Retrieve the selector found in a signature on a message.
[dkim_sig_getsignalg()](http://www.opendkim.org/libopendkim/dkim_sig_getsignalg.html)Retrieve the signature algorithm used to sign a message.
[dkim_sig_getsignedhdrs()](http://www.opendkim.org/libopendkim/dkim_sig_getsignedhdrs.html)Retrieve signed header data.
[dkim_sig_getsigntime()](http://www.opendkim.org/libopendkim/dkim_sig_getsigntime.html)Retrieve the timestamp on the signature of a message.
[dkim_sig_getsslbuf()](http://www.opendkim.org/libopendkim/dkim_sig_getsslbuf.html)Retrieve the SSL error buffer for a signature.
[dkim_sig_hdrsigned()](http://www.opendkim.org/libopendkim/dkim_sig_hdrsigned.html)Determine whether or not a particular header was signed.
[dkim_sig_ignore()](http://www.opendkim.org/libopendkim/dkim_sig_ignore.html)Flag a signature to be ignored when verifying.
[dkim_sig_process()](http://www.opendkim.org/libopendkim/dkim_sig_process.html)Process a signature for validity.
[dkim_sig_setdnssec()](http://www.opendkim.org/libopendkim/dkim_sig_setdnssec.html)Set the DNSSEC result code associated with a signature.
[dkim_sig_seterror()](http://www.opendkim.org/libopendkim/dkim_sig_seterror.html)Set the error code associated with a signature.
**Processing**
[dkim_header()](http://www.opendkim.org/libopendkim/dkim_header.html)Process a header.
[dkim_eoh()](http://www.opendkim.org/libopendkim/dkim_eoh.html)Identify end of headers.
[dkim_body()](http://www.opendkim.org/libopendkim/dkim_body.html)Process a body chunk.
[dkim_eom()](http://www.opendkim.org/libopendkim/dkim_eom.html)Identify end of message.
[dkim_chunk()](http://www.opendkim.org/libopendkim/dkim_chunk.html)Process a message chunk.
**Utility**
[dkim_getid()](http://www.opendkim.org/libopendkim/dkim_getid.html)Retrieve "id" string from handle.
[dkim_get_msgdate()](http://www.opendkim.org/libopendkim/dkim_get_msgdate.html)Attempt to parse the Date: header field of a message and return its UNIX time_t conversion as a 64-bit unsigned integer.
[dkim_get_sigsubstring()](http://www.opendkim.org/libopendkim/dkim_get_sigsubstring.html)Retrieve a minimal signature substring for matching results to signatures.
[dkim_key_syntax()](http://www.opendkim.org/libopendkim/dkim_key_syntax.html)Check the syntax of a key record.
[dkim_mail_parse()](http://www.opendkim.org/libopendkim/dkim_mail_parse.html)Parse a message header field, e.g. From:, to get user and domain.
[dkim_mail_parse_multi()](http://www.opendkim.org/libopendkim/dkim_mail_parse_multi.html)Parse a message header field, e.g. To: or Cc:, to get users and domains.
[dkim_options()](http://www.opendkim.org/libopendkim/dkim_options.html)Get or set library options.
[dkim_qi_getname()](http://www.opendkim.org/libopendkim/dkim_qi_getname.html)Retrieve the DNS name from a DKIM_QUERYINFO handle.
[dkim_qi_gettype()](http://www.opendkim.org/libopendkim/dkim_qi_gettype.html)Retrieve the DNS resource record type from a DKIM_QUERYINFO handle.
[dkim_sig_gethashes()](http://www.opendkim.org/libopendkim/dkim_sig_gethashes.html)Retrieve computed hashes related to a signature.
[dkim_sig_gettagvalue()](http://www.opendkim.org/libopendkim/dkim_sig_gettagvalue.html)Retrieve arbitrary tags and values from signatures and keys.
[dkim_sig_syntax()](http://www.opendkim.org/libopendkim/dkim_sig_syntax.html)Check the syntax of a signature.
**DNS Operations**
[dkim_dns_close()](http://www.opendkim.org/libopendkim/dkim_dns_close.html)Force shutdown of the DNS resolver in use by the library.
[dkim_dns_config()](http://www.opendkim.org/libopendkim/dkim_dns_config.html)Provide the active DNS resolver with arbitrary configuration information to be used.
[dkim_dns_init()](http://www.opendkim.org/libopendkim/dkim_dns_init.html)Force initialization of the DNS resolver to be used by the library.
[dkim_dns_nslist()](http://www.opendkim.org/libopendkim/dkim_dns_nslist.html)Provide the active DNS resolver with a new set of nameservers to be used.
[dkim_dns_set_close()](http://www.opendkim.org/libopendkim/dkim_dns_set_close.html)Set the function to be used by the library to terminate a DNS resolver.
[dkim_dns_set_config()](http://www.opendkim.org/libopendkim/dkim_dns_set_config.html)Set the function to be used by the library to pass arbitrary configuration data to the underlying resolver.
[dkim_dns_set_init()](http://www.opendkim.org/libopendkim/dkim_dns_set_init.html)Set the function to be used by the library to initialize a DNS resolver.
[dkim_dns_set_nslist()](http://www.opendkim.org/libopendkim/dkim_dns_set_nslist.html)Set the function to be used by the library to change the set of nameservers in use by a DNS resolver.
[dkim_dns_set_query_cancel()](http://www.opendkim.org/libopendkim/dkim_dns_set_query_cancel.html)Set the function to be used by the library to cancel a pending DNS query whose result is no longer needed.
[dkim_dns_set_query_service()](http://www.opendkim.org/libopendkim/dkim_dns_set_query_service.html)Set the DNS query service handle to be used by the library.
[dkim_dns_set_query_start()](http://www.opendkim.org/libopendkim/dkim_dns_set_query_start.html)Set the DNS query start function to be used by the library.
[dkim_dns_set_query_waitreply()](http://www.opendkim.org/libopendkim/dkim_dns_set_query_waitreply.html)Set the function to be used by the library to wait for a reply to a pending DNS query.
[dkim_dns_set_trustanchor()](http://www.opendkim.org/libopendkim/dkim_dns_set_trustanchor.html)Set the function to be used by the library to pass arbitrary trust anchor data to the underlying resolver.
[dkim_dns_trustanchor()](http://www.opendkim.org/libopendkim/dkim_dns_trustanchor.html)Provide the active DNS resolver with trust anchor configuration information to be used.
**Cleanup**
[dkim_free()](http://www.opendkim.org/libopendkim/dkim_free.html)Destroy a per-message handle of the **DKIM** service.

 An overview of the general use of this API is available [here](http://www.opendkim.org/libopendkim/overview.html). An overview of the DNS resolver portion of the API is available [here](http://www.opendkim.org/libopendkim/dns.html). 

* * *

 Copyright (c) 2005-2008 Sendmail, Inc. and its suppliers. All rights reserved. 

 Copyright (c) 2009-2014, The Trusted Domain Project. All rights reserved. 

 By using this file, you agree to the terms and conditions set forth in the respective licenses.
