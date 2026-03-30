# Source: https://man.freebsd.org/cgi/man.cgi?query=relayd

Title: relayd

URL Source: https://man.freebsd.org/cgi/man.cgi?query=relayd

Markdown Content:
FreeBSD Manual Pages
--------------------

* * *

_RELAYD_(8)      System Manager's Manual       _RELAYD_(8)

[**NAME**](https://man.freebsd.org/cgi/man.cgi?query=relayd#end)
       relayd -- relay daemon

[**SYNOPSIS**](https://man.freebsd.org/cgi/man.cgi?query=relayd#end)
       **relayd** [**-dnv**] [**-D** _macro_=_value_] [**-f** _file_]

[**DESCRIPTION**](https://man.freebsd.org/cgi/man.cgi?query=relayd#end)
       **relayd**  is  a daemon to relay and dynamically redirect incoming connec-
       tions to a target host. Its main purposes are to run  as  a  load-bal-
       ancer,  application layer gateway, or transparent proxy.  The daemon is
       able to monitor groups of hosts for availability, which is  determined
       by checking for a specific service common to a host group.  When avail-
       ability is  confirmed, layer 3 and/or layer 7 forwarding services are
       set up by **relayd**.

       Layer 3 redirection happens at  the  packet  level;  to configure  it,
       **relayd**  communicates  with  [_pf_(4)](https://man.freebsd.org/cgi/man.cgi?query=pf&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly).   To allow **relayd** to properly set up
       [_pf_(4)](https://man.freebsd.org/cgi/man.cgi?query=pf&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) rules, the following line is required in the  filter  section  of
       [_pf.conf_(5)](https://man.freebsd.org/cgi/man.cgi?query=pf.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly):

      anchor "relayd/*"

       On  FreeBSD,  the filter section requires the `rdr-anchor' rule instead
       of `anchor':

      rdr-anchor "relayd/*"

       Layer 7 relaying happens at the application level  and  is  handled  by
       **relayd**  itself.  Various application level filtering and protocol-spe-
       cific load-balancing options are available for relays.

       **relayd** works in terms of the  following _entities_:  relays,  protocols,
       redirections,  and tables.  A _relay_ represents a layer 7 load-balancing
       instance.  Each instance translates to a listening TCP or UDP port.   A
       _protocol_ defines which actions, if any, are taken on the packet payload
       as  data crosses a relay.  A _redirection_ represents a layer 3 load-bal-
       ancing instance.  Each instance translates to a [_pf_(4)](https://man.freebsd.org/cgi/man.cgi?query=pf&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) rdr-to rule being
       added.  A _table_ represents a group of hosts which can  be  checked  for
       availability  using  the same method.  Each table contains at least one
       host.  If a table is used in a layer 3 load-balancing instance, it will
       be mapped to a [_pf_(4)](https://man.freebsd.org/cgi/man.cgi?query=pf&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) table containing only those hosts which are up.

       All these entities can be configured in [_relayd.conf_(5)](https://man.freebsd.org/cgi/man.cgi?query=relayd.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly), and [_relayctl_(8)](https://man.freebsd.org/cgi/man.cgi?query=relayctl&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly)
       can be used to alter or report on the status of each entity.

       The options are as follows:

       **-D** _macro_=_value_
        Define _macro_ to be set to _value_ on the command line.  Overrides
        the definition of _macro_ in the configuration file.

       **-d**      Do not daemonize.  If this option is specified, **relayd** will run
        in the foreground and log to _stderr_.

       **-f** _file_
        Specify an alternative  configuration  file.   The  default  is
        _/usr/local/etc/relayd.conf_.

       **-n**      Configtest  mode.  Only check the configuration file for valid-
        ity.

       **-v**      Produce more verbose output.

[**FILES**](https://man.freebsd.org/cgi/man.cgi?query=relayd#end)
       /usr/local/etc/relayd.conf
          Default configuration file.
       _/var/run/relayd.sock_    Unix-domain socket used for communication  with
          [_relayctl_(8)](https://man.freebsd.org/cgi/man.cgi?query=relayctl&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly).

[**SEE ALSO**](https://man.freebsd.org/cgi/man.cgi?query=relayd#end)
       [_relayd.conf_(5)](https://man.freebsd.org/cgi/man.cgi?query=relayd.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly), [_relayctl_(8)](https://man.freebsd.org/cgi/man.cgi?query=relayctl&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly)

[**HISTORY**](https://man.freebsd.org/cgi/man.cgi?query=relayd#end)
       The  **relayd**  program,  formerly known as **hoststated**, first appeared in
       OpenBSD 4.1.  It was renamed to **relayd** in OpenBSD 4.3.

[**AUTHORS**](https://man.freebsd.org/cgi/man.cgi?query=relayd#end)
       The   **relayd**   program was   written by    Pierre-Yves    Ritschard
       <_pyr@openbsd.org_> and Reyk Floeter <_reyk@openbsd.org_>.

FreeBSD 15.0    July 27, 2015        _RELAYD_(8)
[* * *](https://man.freebsd.org/cgi/man.cgi?query=relayd)
[](https://man.freebsd.org/cgi/man.cgi?query=relayd)[NAME](https://man.freebsd.org/cgi/man.cgi?query=relayd#NAME) | [SYNOPSIS](https://man.freebsd.org/cgi/man.cgi?query=relayd#SYNOPSIS) | [DESCRIPTION](https://man.freebsd.org/cgi/man.cgi?query=relayd#DESCRIPTION) | [FILES](https://man.freebsd.org/cgi/man.cgi?query=relayd#FILES) | [SEE ALSO](https://man.freebsd.org/cgi/man.cgi?query=relayd#SEE_ALSO) | [HISTORY](https://man.freebsd.org/cgi/man.cgi?query=relayd#HISTORY) | [AUTHORS](https://man.freebsd.org/cgi/man.cgi?query=relayd#AUTHORS)

Want to link to this manual page? Use this URL:

<[https://man.freebsd.org/cgi/man.cgi?query=relayd&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly](https://man.freebsd.org/cgi/man.cgi?query=relayd&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly)>

* * *
