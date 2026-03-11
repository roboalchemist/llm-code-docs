# Source: https://man.freebsd.org/cgi/man.cgi?query=relayctl&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly

Title: relayctl(8)

URL Source: https://man.freebsd.org/cgi/man.cgi?query=relayctl&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly

Markdown Content:
FreeBSD Manual Pages
--------------------

* * *

_RELAYCTL_(8)      System Manager's Manual     _RELAYCTL_(8)

[**NAME**](https://man.freebsd.org/cgi/man.cgi?query=relayctl&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#end)
       relayctl -- control the relay daemon

[**SYNOPSIS**](https://man.freebsd.org/cgi/man.cgi?query=relayctl&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#end)
       **relayctl** [**-s** _socket_] _command_ [_argument_ _..._]

[**DESCRIPTION**](https://man.freebsd.org/cgi/man.cgi?query=relayctl&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#end)
       The **relayctl** program controls the [_relayd_(8)](https://man.freebsd.org/cgi/man.cgi?query=relayd&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) daemon.

       The following options are available:

       **-s** _socket_
        Use  _socket_ instead of the default _/var/run/relayd.sock_ to com-
        municate with [_relayd_(8)](https://man.freebsd.org/cgi/man.cgi?query=relayd&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly).

       The following commands are available:

       **host** **disable** [_name_ | _id_]
        Disable a host. Treat it as though it were always down.

       **host** **enable** [_name_ | _id_]
        Enable the host.  Start checking its health again.

       **load** _filename_
        Reload the configuration from the specified file.

       **log** **brief**
        Disable verbose debug logging.

       **log** **verbose**
        Enable verbose debug logging.

       **monitor**
        Continuously report any changes in the host checking engine and
        the [_pf_(4)](https://man.freebsd.org/cgi/man.cgi?query=pf&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) engine.

       **poll**    Schedule an immediate check of all hosts.

       **redirect** **disable** [_name_ | _id_]
        Disable a redirection.  If it has [_pf_(4)](https://man.freebsd.org/cgi/man.cgi?query=pf&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) redirection  rules  in-
        stalled,  remove them.  Mark the redirection's main table and -
        if applicable - disable the backup table as well.

       **redirect** **enable** [_name_ | _id_]
        Enable a redirection.  Mark the redirection's main table and  -
        if applicable - enable the backup table as well.

       **reload**  Reload the configuration file.

       **show** **hosts**
        Show  detailed  status of hosts and tables.  It will also print
        the last error for failed host checks;  see  the  "DIAGNOSTICS"
        section below.

       **show** **redirects**
        Show  detailed status of redirections including the current and
        average access statistics.   The  statistics  will  be  updated
        every  minute. Redirections  using  the **sticky-address** option
        will count the number of sticky states, not the total number of
        redirected connections.

       **show** **relays**
        Show detailed status of relays including the current and  aver-
        age  access  statistics.   The statistics will be updated every
        minute.

       **show** **sessions**
        Dump the complete list of running relay sessions.

       **show** **summary**
        Display a list of all relays, redirections, tables, and hosts.

       **table** **disable** [_name_ | _id_]
        Disable a table.  Consider all hosts disabled.  If it is a main
        table of a redirection which has a non-empty backup table, swap
        the contents of the [_pf_(4)](https://man.freebsd.org/cgi/man.cgi?query=pf&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) table with those of the backup table.

       **table** **enable** [_name_ | _id_]
        Enable a table. Start doing checks for all hosts  that aren't
        individually disabled again.

[**FILES**](https://man.freebsd.org/cgi/man.cgi?query=relayctl&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#end)
       _/var/run/relayd.sock_    Unix-domain  socket used for communication with
          [_relayd_(8)](https://man.freebsd.org/cgi/man.cgi?query=relayd&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly).

[**DIAGNOSTICS**](https://man.freebsd.org/cgi/man.cgi?query=relayctl&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#end)
       If a host is down and a previous check failed,  **relayctl**  will  display
       the  last error in the output of the **show** **hosts** command.  This is espe-
       cially useful for debugging server or configuration failures.  The fol-
       lowing errors will be reported:

       _none_    No specific error was reported by the check engine.

       _aborted_
        All checks were aborted by an external event, like a configura-
        tion reload.

       _interval_ _timeout_
        The check did not finish in the configured time of an interval.
        This can happen if there are too many hosts  that  have to  be
        checked by  [_relayd_(8)](https://man.freebsd.org/cgi/man.cgi?query=relayd&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly)  and  can  be  avoided by increasing the
        global **interval** option in [_relayd.conf_(5)](https://man.freebsd.org/cgi/man.cgi?query=relayd.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly).

       _icmp_ _read_ _timeout_
       _tls_ _read_ _timeout_
       _tcp_ _read_ _timeout_
        The check failed because the remote host did not send  a  reply
        within the configured timeout.

       _icmp_ _write_ _timeout_
       _tls_ _write_ _timeout_
       _tcp_ _write_ _timeout_
       _tls_ _connect_ _timeout_
       _tcp_ _connect_ _timeout_
        The  check  failed  because [_relayd_(8)](https://man.freebsd.org/cgi/man.cgi?query=relayd&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) was not ready to send the
        request within the configured timeout.

       _tls_ _connect_ _error_
       _tls_ _read_ _error_
       _tls_ _write_ _error_
       _tcp_ _connect_ _error_
       _tcp_ _read_ _failed_
       _tcp_ _write_ _failed_
        An I/O error occurred.  This indicates that [_relayd_(8)](https://man.freebsd.org/cgi/man.cgi?query=relayd&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) was  run-
        ning low on resources, file descriptors, or was too busy to run
        the  request.   It can also indicate that a TLS or TCP protocol
        error occurred or that the connection was unexpectedly aborted.

       _tls_ _connect_ _failed_
       _tcp_ _connect_ _failed_
        The check failed because the protocol handshake did not succeed
        in opening a stateful connection with the remote host.

       _script_ _failed_
        The external script executed by the  check  did not  return  a
        valid return code.

       _send/expect_ _failed_
        The  payload data returned by the remote host did not match the
        expected pattern.

       _http_ _code_ _malformed_
       _http_ _digest_ _malformed_
        The remote host did not return a valid HTTP header or body.

       _http_ _code_ _mismatch_
        The remote host did not return  a  matching  HTTP  error  code.
        This  may  indicate  a real server problem (a server error, the
        page was not found, permission was denied) or  a  configuration
        error.  For example, it is a very common mistake that [_relayd_(8)](https://man.freebsd.org/cgi/man.cgi?query=relayd&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly)
        was  configured to expect a HTTP 200 OK status but the host is
        returning a HTTP 302 Found redirection. See [_relayd.conf_(5)](https://man.freebsd.org/cgi/man.cgi?query=relayd.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) for
        more information on validating the HTTP return code.

       _http_ _digest_ _mismatch_
        The remote host did not return the  expected  content  and  the
        computed  digest  was  different  to the configured value.  See
        [_relayd.conf_(5)](https://man.freebsd.org/cgi/man.cgi?query=relayd.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) for more information on validating the digest.

[**SEE ALSO**](https://man.freebsd.org/cgi/man.cgi?query=relayctl&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#end)
       [_relayd_(8)](https://man.freebsd.org/cgi/man.cgi?query=relayd&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly)

[**HISTORY**](https://man.freebsd.org/cgi/man.cgi?query=relayctl&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#end)
       The **relayctl** program, formerly known as **hoststatectl**, first appeared in
       OpenBSD 4.1.  It was renamed to **relayctl** in OpenBSD 4.3.

FreeBSD 15.0         November 29, 2017     _RELAYCTL_(8)
[* * *](https://man.freebsd.org/cgi/man.cgi?query=relayctl&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly)
[](https://man.freebsd.org/cgi/man.cgi?query=relayctl&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly)[NAME](https://man.freebsd.org/cgi/man.cgi?query=relayctl&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#NAME) | [SYNOPSIS](https://man.freebsd.org/cgi/man.cgi?query=relayctl&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#SYNOPSIS) | [DESCRIPTION](https://man.freebsd.org/cgi/man.cgi?query=relayctl&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#DESCRIPTION) | [FILES](https://man.freebsd.org/cgi/man.cgi?query=relayctl&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#FILES) | [DIAGNOSTICS](https://man.freebsd.org/cgi/man.cgi?query=relayctl&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#DIAGNOSTICS) | [SEE ALSO](https://man.freebsd.org/cgi/man.cgi?query=relayctl&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#SEE_ALSO) | [HISTORY](https://man.freebsd.org/cgi/man.cgi?query=relayctl&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#HISTORY)

Want to link to this manual page? Use this URL:

<[https://man.freebsd.org/cgi/man.cgi?query=relayctl&sektion=8&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly](https://man.freebsd.org/cgi/man.cgi?query=relayctl&sektion=8&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly)>

* * *
