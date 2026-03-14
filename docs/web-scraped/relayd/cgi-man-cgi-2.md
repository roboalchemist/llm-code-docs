# Source: https://man.freebsd.org/cgi/man.cgi?query=pf.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly

Title: pf.conf(5)

URL Source: https://man.freebsd.org/cgi/man.cgi?query=pf.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly

Markdown Content:
FreeBSD Manual Pages
--------------------

* * *

_PF.CONF_(5)        File Formats Manual      _PF.CONF_(5)

[**NAME**](https://man.freebsd.org/cgi/man.cgi?query=pf.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#end)
       pf.conf -- packet filter configuration file

[**DESCRIPTION**](https://man.freebsd.org/cgi/man.cgi?query=pf.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#end)
       The  [_pf_(4)](https://man.freebsd.org/cgi/man.cgi?query=pf&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) packet filter modifies, drops or passes packets according to
       rules or definitions specified in **pf.conf**.

[**STATEMENT ORDER**](https://man.freebsd.org/cgi/man.cgi?query=pf.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#end)
       There are eight types of statements in **pf.conf**:

       **Macros**
      User-defined variables may be defined and used later, simplifying
      the configuration file.  Macros must be defined before  they  are
      referenced in **pf.conf**.

       **Tables**
      Tables  provide  a  mechanism  for increasing the performance and
      flexibility of rules with large numbers of source or  destination
      addresses.

       **Options**
      Options tune the behaviour of the packet filtering engine.

       **Ethernet** **Filtering**
      Ethernet  filtering  provides  rule-based blocking or passing of
      Ethernet packets.

       **Traffic** **Normalization** **(e.g.** _scrub_)
      Traffic normalization protects internal machines  against incon-
      sistencies in Internet protocols and implementations.

       **Queueing**
      Queueing provides rule-based bandwidth control.

       **Translation** **(Various** **forms** **of** **NAT)**
      Translation rules specify how addresses are to be mapped or redi-
      rected to other addresses.

       **Packet** **Filtering**
      Packet filtering provides rule-based blocking or passing of pack-
      ets.

       With the exception of **macros** and **tables**, the types of statements should
       be  grouped  and  appear  in  **pf.conf** in the order shown above, as this
       matches the operation of the underlying packet  filtering  engine.   By
       default [_pfctl_(8)](https://man.freebsd.org/cgi/man.cgi?query=pfctl&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) enforces this order (see _set_ _require-order_ below).

       Comments  can  be put anywhere in the file using a hash mark (`#'), and
       extend to the end of the current line.

       Additional configuration files can be included with  the  **include**  key-
       word, for example:

      include "/etc/pf/sub.filter.conf"

[**MACROS**](https://man.freebsd.org/cgi/man.cgi?query=pf.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#end)
       Macros  can  be defined that will later be expanded in context.  Macro
       names must start with a letter, and may contain letters, digits and un-
       derscores.  Macro names may not be reserved words  (for example  _pass_,
       _in_,  _out_).   Macros  are not expanded inside quotes.  Ranges of network
       addresses used in macros that will be expanded in lists later  on  must
       be quoted with additional simple quotes.

       For example,

      ext_if = "kue0"
      all_ifs = "{" $ext_if lo0 "}"
      pass out on $ext_if from any to any
      pass in  on $ext_if proto tcp from any to any port 25

      usr_lan_range = "'192.0.2.0/24'"
      srv_lan_range = "'198.51.100.0 - 198.51.100.255'"
      nat_ranges = "{" $usr_lan_range $srv_lan_range "}"
      nat on $ext_if from $nat_ranges to any -> ($ext_if)

[**TABLES**](https://man.freebsd.org/cgi/man.cgi?query=pf.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#end)
       Tables  are  named  structures which can hold a collection of addresses
       and networks.  Lookups against tables in  [_pf_(4)](https://man.freebsd.org/cgi/man.cgi?query=pf&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) are  relatively  fast,
       making  a  single  rule with  tables  much more efficient, in terms of
       processor usage and memory consumption, than a large  number  of  rules
       which differ only in IP address (either created explicitly or automati-
       cally by rule expansion).

       Tables  can be used as the source or destination of filter rules, _scrub_
       rules or translation rules such as _nat_ or _rdr_ (see below for details on
       the various rule types).  Tables can also be used for the redirect  ad-
       dress  of  _nat_  and _rdr_ and in the routing options of filter rules, but
       not for _bitmask_ pools.

       Tables can be defined with any of the  following  [_pfctl_(8)](https://man.freebsd.org/cgi/man.cgi?query=pfctl&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly)  mechanisms.
       As with macros, reserved words may not be used as table names.

       _manually_  Persistent  tables  can  be  manually created with the _add_ or
   _replace_ option of [_pfctl_(8)](https://man.freebsd.org/cgi/man.cgi?query=pfctl&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly), before or after the  ruleset  has
   been loaded.

       _pf.conf_  Table definitions  can  be placed directly in this file, and
   loaded at the same time as other  rules  are  loaded, atomi-
   cally.  Table definitions inside **pf.conf** use the _table_ state-
   ment, and are especially useful to define non-persistent ta-
   bles. The contents of a pre-existing table defined without a
   list of addresses  to initialize  it is  not  altered  when
   **pf.conf**  is loaded.  A table initialized with the empty list,
   **{** **}**, will be cleared on load.

       Tables may be defined with the following attributes:

       _persist_  The _persist_ flag forces the kernel to keep  the  table  even
   when  no rules refer to it.  If the flag is not set, the ker-
   nel will automatically remove the table when  the  last  rule
   referring to it is flushed.

       _const_  The  _const_  flag prevents the user from altering the contents
   of the table once it has been created.   Without  that  flag,
   [_pfctl_(8)](https://man.freebsd.org/cgi/man.cgi?query=pfctl&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly)  can be used to add or remove addresses from the ta-
   ble at any time, even when running with [_securelevel_(7)](https://man.freebsd.org/cgi/man.cgi?query=securelevel&sektion=7&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) = 2.

       _counters_  The _counters_ flag enables per-address packet and  byte  coun-
   ters  which  can  be displayed with [_pfctl_(8)](https://man.freebsd.org/cgi/man.cgi?query=pfctl&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly). Note that this
   feature carries significant memory overhead for large tables.

       For example,

      table <private> const { 10/8, 172.16/12, 192.168/16 }
      table <badhosts> persist
      block on fxp0 from { <private>, <badhosts> } to any

       creates a table called  private,  to  hold  RFC 1918  private  network
       blocks, and a table called badhosts, which is initially empty. A fil-
       ter rule is set up to block all traffic coming from addresses listed in
       either table.  The private table cannot have its contents  changed  and
       the  badhosts  table will exist even when no active filter rules refer-
       ence it.  Addresses may later be added to the badhosts table,  so  that
       traffic from these hosts can be blocked by using

      # pfctl -t badhosts -Tadd 204.92.77.111

       A  table  can also be initialized with an address list specified in one
       or more external files, using the following syntax:

      table <spam> persist file "/etc/spammers" file "/etc/openrelays"
      block on fxp0 from <spam> to any

       The files _/etc/spammers_ and _/etc/openrelays_ list IP addresses, one  per
       line.   Any  lines  beginning  with a # are treated as comments and ig-
       nored.  In addition to being specified by IP address, hosts may also be
       specified by their hostname.  When the resolver is  called  to add  a
       hostname  to  a table, _all_ resulting IPv4 and IPv6 addresses are placed
       into the table. IP addresses can also be entered in a table by speci-
       fying  a valid interface name, a valid interface group or the _self_ key-
       word, in which case all addresses assigned to the interface(s) will  be
       added to the table.

[**OPTIONS**](https://man.freebsd.org/cgi/man.cgi?query=pf.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#end)
       [_pf_(4)](https://man.freebsd.org/cgi/man.cgi?query=pf&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) may be tuned for various situations using the _set_ command.

       _set_ _timeout_

      _interval_ Interval between purging expired states and fragments.
      _frag_ Seconds before an unassembled fragment is expired.
      _src.track_ Length of time to retain a source tracking entry after
   the last state expires.

      When  a packet matches a stateful connection, the seconds to live
      for the connection will be updated to that of the _proto.modifier_
      which  corresponds  to  the  connection state.  Each packet which
      matches this state will reset the TTL.  Tuning these  values  may
      improve  the  performance of the firewall at the risk of dropping
      valid idle connections.

      _tcp.first_
     The state after the first packet.
      _tcp.opening_
     The state after the second packet but before both endpoints
     have acknowledged the connection.
      _tcp.established_
     The fully established state.
      _tcp.closing_
     The state after the first FIN has been sent.
      _tcp.finwait_
     The state after both FINs have been exchanged and the  con-
     nection  is closed. Some hosts (notably web servers on So-
     laris) send TCP packets even after closing the  connection.
     Increasing  _tcp.finwait_ (and possibly _tcp.closing_) can pre-
     vent blocking of such packets.
      _tcp.closed_
     The state after one endpoint sends an RST.

      SCTP timeout are handled similar to TCP, but with its own set  of
      states:

      _sctp.first_
     The state after the first packet.
      _sctp.opening_
     The state before the destination host ever sends a packet.
      _sctp.established_
     The fully established state.
      _sctp.closing_
     The state after the first SHUTDOWN chunk has been sent.
      _sctp.closed_
     The state  after  SHUTDOWN_ACK  has been exchanged and the
     connection is closed.

      ICMP and UDP are handled in a fashion similar to TCP, but with  a
      much more limited set of states:

      _udp.first_
     The state after the first packet.
      _udp.single_
     The state if the source host sends more than one packet but
     the destination host has never sent one back.
      _udp.multiple_
     The state if both hosts have sent packets.
      _icmp.first_
     The state after the first packet.
      _icmp.error_
     The state  after an ICMP error came back in response to an
     ICMP packet.

      Other protocols are handled similarly to UDP:

      _other.first_
      _other.single_
      _other.multiple_

      Timeout values can be reduced adaptively as the number  of  state
      table entries grows.

      _adaptive.start_
     When  the number of state entries exceeds this value, adap-
     tive scaling begins.  All timeout values  are  scaled  lin-
     early  with factor (adaptive.end  -  number  of states) /
     (adaptive.end - adaptive.start).
      _adaptive.end_
     When reaching this number of  state entries,  all  timeout
     values  become  zero, effectively purging all state entries
     immediately.  This value is used to define the  scale  fac-
     tor,  it  should not actually be reached (set a lower state
     limit, see below).

      Adaptive timeouts are enabled by default, with an adaptive.start
      value  equal to 60% of the state limit, and an adaptive.end value
      equal to 120% of the state limit. They can be disabled  by  set-
      ting both adaptive.start and adaptive.end to 0.

      The  adaptive timeout values can be defined both globally and for
      each rule.  When used on a per-rule basis, the values  relate  to
      the  number of states created by the rule, otherwise to the total
      number of states.

      For example:

     set timeout tcp.first 120
     set timeout tcp.established 86400
     set timeout { adaptive.start 60000, adaptive.end 120000 }
     set limit states 100000

      With 90000 state table entries, the timeout values are scaled  to
      50% (tcp.first 60, tcp.established 43200).

       _set_ _loginterface_
      Enable  collection  of  packet  and byte count statistics for the
      given interface or interface  group.   These  statistics  can  be
      viewed using

     # pfctl -s info

      In  this example [_pf_(4)](https://man.freebsd.org/cgi/man.cgi?query=pf&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) collects statistics on the interface named
      dc0:

     set loginterface dc0

      One can disable the loginterface using:

     set loginterface none

       _set_ _limit_
      Sets hard limits on the memory pools used by the  packet  filter.
      See [_zone_(9)](https://man.freebsd.org/cgi/man.cgi?query=zone&sektion=9&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) for an explanation of memory pools.

      Limits can be set on the following:

      **states**     Set  the  maximum  number of entries in the memory
       pool used by state table entries (those  generated
       by _pass_ rules which do not specify **no** **state**).  The
       default is 100000.

      **src-nodes**     Set  the  maximum  number of entries in the memory
       pool used for tracking source IP addresses (gener-
       ated by the _sticky-address_ and _src.track_ options).
       The default is 10000.

      **table-entries**  Set the number of addresses that can be stored  in
       tables.  The default is 200000.

      **anchors**     Set the number of anchors that can exist.  The de-
       fault is 512.

      **eth-anchors**    Set the number of anchors that can exist.  The de-
       fault is 512.

      Multiple limits can be combined on a single line:

     set limit { states 20000, frags 2000, src-nodes 2000 }

       _set_ _ruleset-optimization_
      _none_      Disable the ruleset optimizer.
      _basic_     Enable basic ruleset optimization.  This is the default
         behaviour.  Basic ruleset optimization does four things
         to improve the performance of ruleset evaluations:

         1.   remove duplicate rules
         2.   remove rules that are a subset of another rule
         3.   combine  multiple rules into a table when advanta-
       geous
         4.   re-order the rules to improve  evaluation  perfor-
       mance

      _profile_   Uses the currently loaded ruleset as a feedback profile
         to tailor the ordering of quick rules to actual network
         traffic.

      It  is  important to note that the ruleset optimizer will modify
      the ruleset to improve performance.  A side effect of the ruleset
      modification is that per-rule  accounting statistics  will  have
      different meanings than before.  If per-rule accounting is impor-
      tant  for billing  purposes or whatnot, either the ruleset opti-
      mizer should not be used or a label field should be added to  all
      of the accounting rules to act as optimization barriers.

      Optimization  can also  be  set  as  a  command-line argument to
      [_pfctl_(8)](https://man.freebsd.org/cgi/man.cgi?query=pfctl&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly), overriding the settings in **pf.conf**.

       _set_ _optimization_
      Optimize state timeouts for one of the following network environ-
      ments:

      _normal_
     A normal network environment.  Suitable for almost all net-
     works.
      _high-latency_
     A high-latency environment (such  as  a  satellite  connec-
     tion).
      _satellite_
     Alias for _high-latency_.
      _aggressive_
     Aggressively  expire  connections.  This can greatly reduce
     the memory usage of the firewall at the  cost  of  dropping
     idle connections early.
      _conservative_
     Extremely conservative settings.  Avoid dropping legitimate
     connections at  the  expense of greater memory utilization
     (possibly much greater on a busy network) and slightly  in-
     creased processor utilization.

      For example:

     set optimization aggressive

       _set_ _reassemble_ _yes_ | _no_ [**no-df**]
      The **reassemble** option is used to enable or disable the reassembly
      of  fragmented packets, and can be set to **yes** or **no**.  If **no-df** is
      also specified, fragments with the "dont-fragment"  bit  set  are
      reassembled too, instead of being dropped; the reassembled packet
      will  have the "dont-fragment" bit cleared.  The default value is
      **no**.

      This option is ignored if there are pre-FreeBSD  14  **scrub**  rules
      present.

       _set_ _block-policy_
      The _block-policy_ option sets the default behaviour for the packet
      _block_ action:

      _drop_      Packet is silently dropped.
      _return_    A  TCP RST is returned for blocked TCP packets, an SCTP
         ABORT chunk is returned for blocked  SCTP  packets,  an
         ICMP  UNREACHABLE  is returned for blocked UDP packets,
         and all other packets are silently dropped.

      The default value is **drop**.

      For example:

     set block-policy return

       _set_ _fail-policy_
      The _fail-policy_ option sets the behaviour of rules  which should
      pass a packet but were unable to do so.  This might happen when a
      nat or route-to rule uses an empty table as list of targets or if
      a rule fails to create state or source node.  The following _block_
      actions are possible:

      _drop_      Incoming packet is silently dropped.
      _return_    Incoming  packet is dropped and TCP RST is returned for
         TCP packets,  an  SCTP  ABORT  chunk  is  returned  for
         blocked SCTP  packets, an ICMP UNREACHABLE is returned
         for UDP packets, and no response  is  sent  for  other
         packets.

      For example:

     set fail-policy return

       _set_ _state-policy_
      The _state-policy_ option sets the default behaviour for states:

      _if-bound_   States are bound to interface.
      _floating_   States  can match packets on any interfaces (the de-
     fault).

      For example:

     set state-policy if-bound

       _set_ _syncookies_ _never_ | _always_ | _adaptive_
      When **syncookies** are active, pf will answer each incoming TCP  SYN
      with  a syncookie SYNACK, without allocating any resources.  Upon
      reception of the  client's  ACK  in  response  to the  syncookie
      SYNACK,  pf  will evaluate  the  ruleset and create state if the
      ruleset permits it, complete the three  way  handshake  with  the
      target  host  and continue the connection with synproxy in place.
      This allows pf to be resilient  against  large  synflood  attacks
      which  would  run the  state table against its limits otherwise.
      Due to the blind answers to every incoming SYN  syncookies  share
      the  caveats  of synproxy, namely seemingly accepting connections
      that will be dropped later on.

      **never**     pf will never send syncookie SYNACKs (the default).
      **always**    pf will always send syncookie SYNACKs.
      **adaptive**  pf will enable syncookie mode when a  given  percentage
         of  the state table is used up by half-open TCP connec-
         tions, as in, those that saw the initial SYN but didn't
         finish the three way handshake. The thresholds for en-
         tering and leaving syncookie mode can be specified  us-
         ing

        set syncookies adaptive (start 25%, end 12%)

       _set_ _state-defaults_
      The  _state-defaults_ option sets the state options for states cre-
      ated from rules without an explicit _keep_ _state_.  For example:

     set state-defaults no-sync

       _set_ _hostid_
      The 32-bit _hostid_ identifies this firewall's state table  entries
      to  other firewalls in a [_pfsync_(4)](https://man.freebsd.org/cgi/man.cgi?query=pfsync&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) failover cluster.  By default
      the hostid is set to a pseudo-random value, however it may be de-
      sirable to manually configure it, for  example  to  more easily
      identify the source of state table entries.

     set hostid 1

      The hostid may be specified in either decimal or hexadecimal.

       _set_ _require-order_
      By  default  [_pfctl_(8)](https://man.freebsd.org/cgi/man.cgi?query=pfctl&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) enforces an ordering of the statement types
      in the ruleset to: _options_, _normalization_, _queueing_, _translation_,
      _filtering_.  Setting this option to _no_ disables this  enforcement.
      There  may  be non-trivial and non-obvious implications to an out
      of order ruleset. Consider carefully before disabling the  order
      enforcement.

       _set_ _fingerprints_
      Load fingerprints of known operating systems from the given file-
      name.  By default fingerprints of known operating systems are au-
      tomatically  loaded  from [_pf.os_(5)](https://man.freebsd.org/cgi/man.cgi?query=pf.os&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) in _/etc_ but can be overridden
      via this option.  Setting this option may leave a small period of
      time where the fingerprints referenced by the  currently active
      ruleset  are inconsistent until the new ruleset finishes loading.
      The default location for fingerprints is _/etc/pf.os_.

      For example:

     **set** **fingerprints** **"/etc/pf.os.devel"**

       _set_ _skip_ _on_ <_ifspec_>
      List interfaces for which packets should not be filtered.  Pack-
      ets  passing in or out on such interfaces are passed as if pf was
      disabled, i.e. pf does not process them in any way.  This can  be
      useful on loopback and other virtual interfaces, when packet fil-
      tering is not desired and can have unexpected effects.  For exam-
      ple:

     **set** **skip** **on** **lo0**

       _set_ _debug_
      Set the debug _level_ to one of the following:

      _none_    Don't generate debug messages.
      _urgent_    Generate debug messages only for serious errors.
      _misc_    Generate debug messages for various errors.
      _loud_    Generate debug messages for common conditions.

       _set_ _keepcounters_
      Preserve  rule  counters across rule updates.  Usually rule coun-
      ters are reset to zero on every  update  of  the  ruleset.   With
      _keepcounters_  set pf will attempt to find matching rules between
      old and new rulesets and preserve the rule counters.

[**ETHERNET FILTERING**](https://man.freebsd.org/cgi/man.cgi?query=pf.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#end)
       [_pf_(4)](https://man.freebsd.org/cgi/man.cgi?query=pf&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) has the ability to _block_ and _pass_ packets based on attributes  of
       their Ethernet (layer 2) header.

       Each  time  a packet processed by the packet filter comes in on or goes
       out through an interface, the filter rules are evaluated in  sequential
       order,  from first to last.  The last matching rule decides what action
       is taken.  If no rule matches the packet, the default action is to pass
       the packet without creating a state.

       The following actions can be used in the filter:

       _block_
      The packet is blocked.  Unlike for layer 3 traffic the packet  is
      always silently dropped.

       _pass_  The packet is passed; no state is created for layer 2 traffic.

   **Parameters** **applicable** **to** **layer** **2** **rules**
       The  rule  parameters  specify  the packets to which a rule applies.  A
       packet always comes in on, or goes out through, one  interface.   Most
       parameters  are optional.   If a parameter is specified, the rule only
       applies to packets with matching attributes.  The matching for some pa-
       rameters can be inverted with the **!** operator.  Certain  parameters  can
       be expressed as lists, in which case [_pfctl_(8)](https://man.freebsd.org/cgi/man.cgi?query=pfctl&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) generates all needed rule
       combinations.

       _in_ or _out_
      This rule applies to incoming or outgoing packets.  If neither _in_
      nor _out_ are specified, the rule will match packets in both direc-
      tions.

       _quick_
      If  a  packet matches a rule which has the _quick_ option set, this
      rule is considered the last matching rule, and evaluation of sub-
      sequent rules is skipped.

       _on_ <_ifspec_>
      This rule applies only to packets coming  in  on, or  going  out
      through,  this particular interface or interface group.  For more
      information  on  interface  groups,  see  the  **group**  keyword  in
      [_ifconfig_(8)](https://man.freebsd.org/cgi/man.cgi?query=ifconfig&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly).   _any_ will match any existing interface except loop-
      back ones.

       _bridge-to_ <interface>
      Packets matching this rule will be sent out of the specified  in-
      terface without further processing.

       _proto_ <_protocol_>
      This  rule  applies  only to packets of this protocol.  Note that
      Ethernet protocol numbers are different from those used in  [_ip_(4)](https://man.freebsd.org/cgi/man.cgi?query=ip&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly)
      and [_ip6_(4)](https://man.freebsd.org/cgi/man.cgi?query=ip6&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly).

       _from_ <_source_> _to_ <_dest_>
      This  rule  applies only to packets with the specified source and
      destination MAC addresses.

       _queue_ <_queue_>
      Packets matching this rule will  be  assigned  to the  specified
      queue.  See "QUEUEING" for setup details.

       _tag_ <_string_>
      Packets  matching this  rule  will  be tagged with the specified
      string.  The tag acts as an internal marker that can be  used  to
      identify  these packets later on. This can be used, for example,
      to provide trust between interfaces and to determine  if  packets
      have  been  processed  by translation rules.  Tags are "sticky",
      meaning that the packet will be tagged even if the  rule  is  not
      the  last matching rule. Further matching rules can replace the
      tag with a new one but will not remove a previously applied  tag.
      A packet is only ever assigned one tag at a time.

       _tagged_ <_string_>
      Used  to  specify that  packets  must already be tagged with the
      given tag in order to match the rule.  Inverse tag  matching  can
      also be done by specifying the !  operator before the tagged key-
      word.

[**TRAFFIC NORMALIZATION**](https://man.freebsd.org/cgi/man.cgi?query=pf.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#end)
       Traffic normalization  is  a  broad  umbrella  term for aspects of the
       packet filter which deal  with  verifying  packets,  packet  fragments,
       spoofed traffic, and other irregularities.

   **Scrub**
       Scrub  involves sanitising packet content in such a way that there are
       no ambiguities in packet interpretation on the receiving side. It  is
       invoked with the **scrub** option, added to filter rules.

       Parameters  are specified enclosed in parentheses.  At least one of the
       following parameters must be specified:

       _no-df_
      Clears the _dont-fragment_ bit from a matching IP packet.  Some op-
      erating systems are known to generate fragmented packets with the
      _dont-fragment_ bit set.   This  is particularly  true  with  NFS.
      _Scrub_  will  drop such  fragmented  _dont-fragment_ packets unless
      _no-df_ is specified.

      Unfortunately  some  operating  systems   also   generate  their
      _dont-fragment_  packets  with  a  zero  IP identification field.
      Clearing the _dont-fragment_ bit on packets with a zero IP  ID  may
      cause  deleterious  results if an upstream router later fragments
      the packet.  Using the _random-id_ modifier (see below)  is recom-
      mended in combination with the _no-df_ modifier to ensure unique IP
      identifiers.

       _min-ttl_ <_number_>
      Enforces a minimum TTL for matching IP packets.

       _max-mss_ <_number_>
      Reduces  the  maximum segment size (MSS) on TCP SYN packets to be
      no greater than _number_.  This is sometimes required in  scenarios
      where the two endpoints of a TCP connection are not able to carry
      similar  sized  packets  and  the resulting mismatch can lead to
      packet fragmentation or loss.  Note that setting the MSS this way
      can have undesirable effects, such as interfering with the OS de-
      tection features of [_pf_(4)](https://man.freebsd.org/cgi/man.cgi?query=pf&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly).

       _set-tos_ <_string_> | <_number_>
      Enforces a _TOS_ for matching IP packets.  _TOS_ may be given as  one
      of   _critical_,  _inetcontrol_,  _lowdelay_,  _netcontrol_,  _throughput_,
      _reliability_, or one of the DiffServ Code Points: _ef_, _va_, _af11_ ...
      _af43_, _cs0_ ... _cs7_; or as either hex or decimal.

       _random-id_
      Replaces the IP identification field with random values  to  com-
      pensate for predictable values generated by many hosts.  This op-
      tion  only  applies  to packets that are not fragmented after the
      optional fragment reassembly.

       _reassemble_ _tcp_
      Statefully normalizes TCP connections.  _reassemble_  _tcp_  performs
      the following normalizations:

      ttl      Neither  side  of  the  connection  is allowed to reduce
        their IP TTL.  An attacker may send a packet  such  that
        it reaches the firewall, affects the firewall state, and
        expires  before   reaching   the   destination  host.
        _reassemble_ _tcp_ will raise the TTL of all packets back up
        to the highest value seen on the connection.
      timestamp modulation
        Modern TCP stacks will send a  timestamp on  every  TCP
        packet  and  echo the other endpoint's timestamp back to
        them.  Many operating  systems  will  merely  start  the
        timestamp  at  zero  when first booted, and increment it
        several times a second.  The uptime of the host  can  be
        deduced  by  reading  the timestamp and multiplying by a
        constant.  Also observing several  different  timestamps
        can  be  used  to  count hosts behind a NAT device.  And
        spoofing TCP packets into a connection requires  knowing
        or guessing valid timestamps.  Timestamps merely need to
        be monotonically increasing and not derived off a guess-
        able base time.  _reassemble_ _tcp_ will cause _scrub_ to mod-
        ulate the TCP timestamps with a random number.
      extended PAWS checks
        There is a problem with TCP on long fat pipes, in that a
        packet  might  get  delayed for longer than it takes the
        connection to wrap its 32-bit sequence space.   In  such
        an occurrence, the old packet would be indistinguishable
        from  a  new  packet and would be accepted as such.  The
        solution to this is  called  PAWS:  Protection  Against
        Wrapped  Sequence  numbers.   It protects against it by
        making sure the timestamp on each  packet  does  not  go
        backwards.  _reassemble_ _tcp_ also makes sure the timestamp
        on  the packet does not go forward more than the RFC al-
        lows.  By doing this, [_pf_(4)](https://man.freebsd.org/cgi/man.cgi?query=pf&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) artificially extends the se-
        curity of TCP sequence numbers by 10 to 18 bits when the
        host uses appropriately randomized timestamps,  since  a
        blind  attacker  would  have  to guess the timestamp as
        well.

       For example,

      match in all scrub (no-df random-id max-mss 1440)

   **Scrub** **ruleset** **(pre-FreeBSD** **14)**
       In order to maintain compatibility with older releases of FreeBSD _scrub_
       rules can also be specified in their own ruleset.  In  such  case  they
       are  invoked with the _scrub_ directive.  If there are such rules present
       they determine packet reassembly behaviour.  When  no  such  rules  are
       present the  option  _set_ _reassembly_ takes precedence.  The _scrub_ rules
       can take all parameters specified above for a _scrub_  option  of filter
       rules and 2 more parameters controlling fragment reassembly:

       _fragment_ _reassemble_
      Using _scrub_ rules, fragments can be reassembled by normalization.
      In  this  case, fragments are buffered until they form a complete
      packet, and only the completed packet is passed on to the filter.
      The advantage is that filter rules have to deal  only  with  com-
      plete packets, and can ignore fragments.  The drawback of caching
      fragments is the additional memory cost.  This is the default be-
      haviour unless no fragment reassemble is specified.

       _no_ _fragment_ _reassemble_
      Do not reassemble fragments.

       For example,

      scrub in on $ext_if all fragment reassemble

       The  _no_ option prefixed to a scrub rule causes matching packets to re-
       main unscrubbed, much in the same way as _drop_ _quick_ works in the packet
       filter (see below).  This mechanism should be used when it is necessary
       to exclude specific packets from broader scrub rules.

       _scrub_ rules in the _scrub_ ruleset are evaluated for every packet before
       stateful filtering.  This means excessive usage of them will cause per-
       formance  penalty.  _scrub_ _reassemble_ _tcp_ rules must not have the direc-
       tion (in/out) specified.

[**QUEUEING with ALTQ**](https://man.freebsd.org/cgi/man.cgi?query=pf.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#end)
       The ALTQ system is currently not available in the GENERIC kernel nor as
       loadable modules.  In order to use the herein after called queueing op-
       tions one has to use a custom built kernel.  Please refer to [_altq_(4)](https://man.freebsd.org/cgi/man.cgi?query=altq&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) to
       learn about the related kernel options.

       Packets can be assigned to queues for the purpose of bandwidth control.
       At least two declarations are required to configure queues,  and  later
       any  packet  filtering  rule  can reference the defined queues by name.
       During the filtering component of **pf.conf**, the  last  referenced  _queue_
       name  is  where any  packets from _pass_ rules will be queued, while for
       _block_ rules it specifies where any resulting ICMP or  TCP  RST  packets
       should  be  queued.  The _scheduler_ defines the algorithm used to decide
       which packets get delayed, dropped, or sent out immediately.  There are
       three _schedulers_ currently supported.

       _cbq_   Class Based Queueing.  _Queues_ attached to an  interface  build  a
      tree,  thus each _queue_ can have further child _queues_.  Each queue
      can have a _priority_ and a _bandwidth_  assigned.   _Priority_ mainly
      controls  the  time packets take to get sent out, while _bandwidth_
      has primarily effects on throughput.  _cbq_ achieves  both parti-
      tioning  and  sharing  of link bandwidth by hierarchically struc-
      tured classes.  Each class has its own _queue_ and is assigned  its
      share  of _bandwidth_.  A child class can borrow bandwidth from its
      parent class as long as excess bandwidth is  available  (see  the
      option _borrow_, below).

       _priq_  Priority  Queueing.   _Queues_  are flat attached to the interface,
      thus, _queues_ cannot have further child _queues_.  Each _queue_ has  a
      unique  _priority_  assigned, ranging from 0 to 15. Packets in the
      _queue_ with the highest _priority_ are processed first.

       _hfsc_  Hierarchical Fair Service Curve.  _Queues_ attached to an interface
      build a tree, thus each _queue_  can  have  further child  _queues_.
      Each  queue  can  have  a _priority_  and  a  _bandwidth_  assigned.
      _Priority_ mainly controls the time packets take to get  sent  out,
      while _bandwidth_ primarily affects throughput.  _hfsc_ supports both
      link-sharing  and guaranteed  real-time  services.  It employs a
      service curve based QoS model, and its unique feature is an abil-
      ity to decouple _delay_ and _bandwidth_ allocation.

       The interfaces on which queueing should be activated are declared using
       the _altq_ _on_ declaration.  _altq_ _on_ has the following keywords:

       <_interface_>
      Queueing is enabled on the named interface.

       <_scheduler_>
      Specifies which queueing scheduler to use.   Currently  supported
      values are _cbq_ for Class Based Queueing, _priq_ for Priority Queue-
      ing and _hfsc_ for the Hierarchical Fair Service Curve scheduler.

       _bandwidth_ <_bw_>
      The  maximum bitrate for all queues on an interface may be speci-
      fied using the _bandwidth_ keyword. The value can be specified  as
      an  absolute value or as a percentage of the interface bandwidth.
      When using an absolute value, the suffixes _b_, _Kb_, _Mb_, and _Gb_  are
      used to represent bits, kilobits, megabits, and gigabits per sec-
      ond, respectively.  The value must not exceed the interface band-
      width.  If _bandwidth_ is not specified, the interface bandwidth is
      used  (but take note that some interfaces do not know their band-
      width, or can adapt their bandwidth rates).

       _qlimit_ <_limit_>
      The maximum number of packets held in the queue.  The default  is
      50.

       _tbrsize_ <_size_>
      Adjusts  the  size,  in bytes, of the token bucket regulator.  If
      not specified, heuristics based on the  interface bandwidth  are
      used to determine the size.

       _queue_ <_list_>
      Defines a list of subqueues to create on an interface.

       In the following example, the interface dc0 should queue up to 5Mbps in
       four second-level queues using Class Based Queueing.  Those four queues
       will be shown in a later example.

      altq on dc0 cbq bandwidth 5Mb queue { std, http, mail, ssh }

       Once  interfaces are activated for queueing using the _altq_ directive, a
       sequence of _queue_ directives may be defined.  The name associated  with
       a  _queue_  must match a queue defined in the _altq_ directive (e.g. mail),
       or, except for the _priq_ _scheduler_, in a parent _queue_ declaration.   The
       following keywords can be used:

       _on_ <_interface_>
      Specifies the interface the queue operates on.  If not given, it
      operates on all matching interfaces.

       _bandwidth_ <_bw_>
      Specifies the maximum bitrate to be processed by the queue.  This
      value must not exceed the value of the parent _queue_  and  can  be
      specified as  an absolute  value  or a percentage of the parent
      queue's bandwidth.  If not specified, defaults  to  100%  of  the
      parent  queue's  bandwidth.   The _priq_ scheduler does not support
      bandwidth specification.

       _priority_ <_level_>
      Between queues a priority level can be set.  For  _cbq_  and  _hfsc_,
      the  range is 0 to 7 and for _priq_, the range is 0 to 15.  The de-
      fault for all is 1.  _Priq_ queues with a higher priority  are  al-
      ways  served  first.   _Cbq_ and _Hfsc_ queues with a higher priority
      are preferred in the case of overload.

       _qlimit_ <_limit_>
      The maximum number of packets held in the queue.  The default  is
      50.

       The   _scheduler_  can   get   additional  parameters  with  <_scheduler_>
       (<_parameters_>). Parameters are as follows:

       _default_    Packets not matched by another queue are assigned  to  this
     one.  Exactly one default queue is required.

       _red_    Enable  RED (Random  Early Detection) on this queue.  RED
     drops packets with a probability proportional to the  aver-
     age queue length.

       _rio_    Enables  RIO  on  this queue.  RIO is RED with IN/OUT, thus
     running RED two times more than RIO would achieve the  same
     effect.  RIO is currently not supported in the GENERIC ker-
     nel.

       _ecn_    Enables  ECN  (Explicit  Congestion Notification)  on this
     queue.  ECN implies RED.

       The _cbq_ _scheduler_ supports an additional option:

       _borrow_    The queue can borrow bandwidth from the parent.

       The _hfsc_ _scheduler_ supports some additional options:

       _realtime_ <_sc_>
     The minimum required bandwidth for the queue.

       _upperlimit_ <_sc_>
     The maximum allowed bandwidth for the queue.

       _linkshare_ <_sc_>
     The bandwidth share of a backlogged queue.

       <_sc_> is an acronym for _service_ _curve_.

       The format for service curve specifications is (_m1_, _d_,  _m2_).   _m2_  con-
       trols  the  bandwidth assigned to the queue.  _m1_ and _d_ are optional and
       can be used to control the initial bandwidth assignment.  For the first
       _d_ milliseconds the queue gets the bandwidth given as _m1_, afterwards the
       value given in _m2_.

       Furthermore, with _cbq_ and _hfsc_, child queues can be specified as in  an
       _altq_  declaration, thus building a tree of queues using a part of their
       parent's bandwidth.

       Packets can be assigned to queues based on filter rules by  using  the
       _queue_ keyword.  Normally only one _queue_ is specified; when a second one
       is  specified  it  will instead be used for packets which have a _TOS_ of
       _lowdelay_ and for TCP ACKs with no data payload.

       To continue the previous example, the examples below would specify  the
       four  referenced  queues,  plus a few child queues.  Interactive [_ssh_(1)](https://man.freebsd.org/cgi/man.cgi?query=ssh&sektion=1&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly)
       sessions get priority over bulk transfers like [_scp_(1)](https://man.freebsd.org/cgi/man.cgi?query=scp&sektion=1&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) and [_sftp_(1)](https://man.freebsd.org/cgi/man.cgi?query=sftp&sektion=1&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly).  The
       queues  may  then  be  referenced  by  filtering  rules (see   "PACKET
       FILTERING" below).

       queue std bandwidth 10% cbq(default)
       queue http bandwidth 60% priority 2 cbq(borrow red) \
      { employees, developers }
       queue  developers bandwidth 75% cbq(borrow)
       queue  employees bandwidth 15%
       queue mail bandwidth 10% priority 0 cbq(borrow ecn)
       queue ssh bandwidth 20% cbq(borrow) { ssh_interactive, ssh_bulk }
       queue  ssh_interactive bandwidth 50% priority 7 cbq(borrow)
       queue  ssh_bulk bandwidth 50% priority 0 cbq(borrow)

       block return out on dc0 inet all queue std
       pass out on dc0 inet proto tcp from $developerhosts to any port 80 \
      queue developers
       pass out on dc0 inet proto tcp from $employeehosts to any port 80 \
      queue employees
       pass out on dc0 inet proto tcp from any to any port 22 \
      queue(ssh_bulk, ssh_interactive)
       pass out on dc0 inet proto tcp from any to any port 25 \
      queue mail

[**QUEUEING with dummynet**](https://man.freebsd.org/cgi/man.cgi?query=pf.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#end)
       Queueing  can  also  be done with [_dummynet_(4)](https://man.freebsd.org/cgi/man.cgi?query=dummynet&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly).  Queues and pipes can be
       created with [_dnctl_(8)](https://man.freebsd.org/cgi/man.cgi?query=dnctl&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly).

       Packets can be assigned to queues and pipes using  _dnqueue_  and _dnpipe_
       respectively.

       Both  _dnqueue_  and  _dnpipe_ take either a single pipe or queue number or
       two numbers as arguments.  The first pipe or queue number will be  used
       to  shape the traffic in the rule direction, the second will be used to
       shape the traffic in the reverse direction.  If the rule does not spec-
       ify a direction the first packet to create state will be shaped accord-
       ing to the first number, and the response traffic according to the sec-
       ond.

       If the [_dummynet_(4)](https://man.freebsd.org/cgi/man.cgi?query=dummynet&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) module is not loaded any traffic sent into  a  queue
       or pipe will be dropped.

[**TRANSLATION**](https://man.freebsd.org/cgi/man.cgi?query=pf.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#end)
       Translation options modify either the source or destination address and
       port of the packets associated with a stateful connection.  [_pf_(4)](https://man.freebsd.org/cgi/man.cgi?query=pf&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) modi-
       fies  the  specified address and/or port in the packet and recalculates
       IP, TCP, and UDP checksums as necessary.

       If specified on a **match** rule, subsequent rules will see packets as they
       look after any addresses and ports have been translated.   These  rules
       will  therefore have to filter based on the translated address and port
       number.

       The state entry created permits [_pf_(4)](https://man.freebsd.org/cgi/man.cgi?query=pf&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) to keep track of the original ad-
       dress for traffic associated with that state and correctly  direct  re-
       turn traffic for that connection.

       Various types of translation are possible with pf:

       _af-to_
      Translation between different address families (NAT64) is handled
      using  _af-to_ rules.  Because address family translation overrides
      the routing table, it's only possible to  use  _af-to_  on  inbound
      rules, and a source address of the resulting translation must al-
      ways be specified.

      The  optional  second argument is the host or subnet the original
      addresses are translated into for the  destination.   The lowest
      bits  of  the  original destination address form the host part of
      the new destination address according to  the  specified  subnet.
      It  is possible to embed a complete IPv4 address into an IPv6 ad-
      dress using a network prefix of /96 or smaller.

      When a destination address is not specified, it is  assumed  that
      the  host part is 32-bit long.  For IPv6 to IPv4 translation this
      would mean using only the lower 32 bits of the original IPv6 des-
      tination address. For IPv4 to IPv6 translation  the  destination
      subnet defaults to the subnet of the new IPv6 source address with
      a prefix length of /96.  See RFC 6052 Section 2.2 for details on
      how the prefix determines the destination address encoding.

      For example, the following rules are identical:

     pass in inet af-to inet6 from 2001:db8::1 to 2001:db8::/96
     pass in inet af-to inet6 from 2001:db8::1

      In the above example the matching IPv4 packets will  be  modified
      to have a source address of 2001:db8::1 and a destination address
      will get prefixed with 2001:db8::/96, e.g. 198.51.100.100 will be
      translated to 2001:db8::c633:6464.

      In the reverse case the following rules are identical:

     pass in inet6 from any to 64:ff9b::/96 af-to inet \
     from 198.51.100.1 to 0.0.0.0/0
     pass in inet6 from any to 64:ff9b::/96 af-to inet \
     from 198.51.100.1

      The destination IPv4 address is assumed to be embedded inside the
      original  IPv6  destination address, e.g. 64:ff9b::c633:6464 will
      be translated to 198.51.100.100.

      The current implementation will only extract IPv4 addresses  from
      the IPv6 addresses with a prefix length of /96 and greater.

       _binat_
      A _binat-to_ rule specifies a bidirectional mapping between an ex-
      ternal IP netblock and an internal IP netblock.  It expands to an
      outbound _nat-to_ rule and an inbound _rdr-to_ rule.

       _nat-to_
      A _nat-to_ option specifies that IP addresses are to be changed  as
      the  packet traverses the given interface.  This technique allows
      one or more IP addresses on the translating host to support  net-
      work  traffic  for a larger range of machines on an "inside" net-
      work.  Although in theory any IP address can be used on  the  in-
      side,  it is strongly recommended that one of the address ranges
      defined by RFC 1918 be used.  These netblocks are:

     10.0.0.0 - 10.255.255.255 (all of net 10.0.0.0, i.e., 10.0.0.0/8)
     172.16.0.0 - 172.31.255.255 (i.e., 172.16.0.0/12)
     192.168.0.0 - 192.168.255.255 (i.e., 192.168.0.0/16)

      _nat-to_ is usually applied outbound.  If applied  inbound, nat-to
      to a local IP address is not supported.

       _rdr-to_
      The  packet  is  redirected to another destination and possibly a
      different port.  _rdr-to_ can optionally specify  port  ranges  in-
      stead of single ports.  For instance:

     match in ... port 2000:2999 rdr-to ... port 4000
      redirects ports 2000 to 2999 (inclusive) to port 4000.

     qmatch in ... port 2000:2999 rdr-to ... port 4000:*
      redirects port 2000 to 4000, 2001 to 4001, ..., 2999 to 4999.

       _rdr-to_  is  usually  applied inbound.  If applied outbound, rdr-to to a
       local IP address is not supported.  In addition to  modifying  the  ad-
       dress,  some  translation  rules may modify source or destination ports
       for [_tcp_(4)](https://man.freebsd.org/cgi/man.cgi?query=tcp&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) or [_udp_(4)](https://man.freebsd.org/cgi/man.cgi?query=udp&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) connections; implicitly in the case of _nat-to_  op-
       tions and both implicitly and explicitly in the case of _rdr-to_ ones.  A
       _rdr-to_  opion  may  cause  the  source  port to be modified if doing so
       avoids a conflict with an existing connection.  A random source port in
       the range 50001-65535 is chosen in this case.  Port numbers  are  never
       translated with a _binat-to_ option.

       Note that redirecting external incoming connections to the loopback ad-
       dress, as in

      pass in on egress proto tcp from any to any port smtp \
     rdr-to 127.0.0.1 port spamd

       will  effectively  allow  an  external host to connect to daemons bound
       solely to the loopback address, circumventing the traditional  blocking
       of  such  connections  on  a real interface.  Unless this effect is de-
       sired, any of the local non-loopback addresses should be used as  redi-
       rection target instead, which allows external connections only to dae-
       mons bound to this address or not bound to any address.

       See "TRANSLATION EXAMPLES" below.

   **NAT** **ruleset** **(pre-FreeBSD** **15)**
       In order to maintain compatibility with older releases of  FreeBSD  _NAT_
       rules  can  also be specified in their own ruleset.  A stateful connec-
       tion is automatically created to track packets matching such a rule  as
       long  as  they  are  not  blocked  by the filtering section of **pf.conf**.
       Since translation occurs before filtering the filter  engine  will  see
       packets as  they  look after any addresses and ports have been trans-
       lated.  Filter rules will therefore have to filter based on the trans-
       lated  address  and port number.  Packets that match a translation rule
       are only automatically passed if the _pass_ modifier is given,  otherwise
       they are still subject to _block_ and _pass_ rules.

       The  following rules can be defined in the NAT ruleset: _binat_, _nat_, and
       _rdr_.  They have the same effect as _binat-to_, _nat-to_ and _rdr-to_  options
       for filter rules.

       The  _no_ option prefixed to a translation rule causes packets to remain
       untranslated, much in the same way as _drop_ _quick_ works  in  the packet
       filter.  If  no rule matches the packet it is passed to the filter en-
       gine unmodified.

       Evaluation order of the translation rules is dependent on the  type  of
       the  translation  rules and of the direction of a packet.  _binat_ rules
       are always evaluated first.  Then either the _rdr_ rules are evaluated on
       an inbound packet or the _nat_ rules on an outbound packet.  Rules of the
       same type are evaluated in the same order in which they appear  in  the
       ruleset.  The first matching rule decides what action is taken.

       Translation rules apply only to packets that pass through the specified
       interface,  and if no interface is specified, translation is applied to
       packets on all interfaces.  For instance, redirecting port 80 on an ex-
       ternal interface to an internal web server will only work  for  connec-
       tions  originating from the outside.  Connections to the address of the
       external interface from local hosts will not be redirected, since  such
       packets do not actually pass through the external interface.  Redirec-
       tions cannot reflect packets back through the interface they arrive on,
       they can only be redirected to hosts connected to different  interfaces
       or to the firewall itself.

       See "COMPATIBILITY TRANSLATION EXAMPLES" below.

[**PACKET FILTERING**](https://man.freebsd.org/cgi/man.cgi?query=pf.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#end)
       [_pf_(4)](https://man.freebsd.org/cgi/man.cgi?query=pf&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly)  has  the ability to _block_ , _pass_ and _match_ packets based on at-
       tributes of their layer 3 (see [_ip_(4)](https://man.freebsd.org/cgi/man.cgi?query=ip&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly)  and  [_ip6_(4)](https://man.freebsd.org/cgi/man.cgi?query=ip6&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly))  and layer  4  (see
       [_icmp_(4)](https://man.freebsd.org/cgi/man.cgi?query=icmp&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly),  [_icmp6_(4)](https://man.freebsd.org/cgi/man.cgi?query=icmp6&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly),  [_tcp_(4)](https://man.freebsd.org/cgi/man.cgi?query=tcp&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly),  [_sctp_(4)](https://man.freebsd.org/cgi/man.cgi?query=sctp&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly),  [_udp_(4)](https://man.freebsd.org/cgi/man.cgi?query=udp&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly)) headers.  In addition,
       packets may also be assigned to queues for  the purpose  of  bandwidth
       control.

       For  each  packet  processed by the packet filter, the filter rules are
       evaluated in sequential order, from first to last.  For _block_ and  _pass_
       ,  the  last  matching  rule decides what action is taken.  For _match_ ,
       rules are evaluated every time they match; the pass/block  state  of  a
       packet  remains unchanged.  If no rule matches the packet, the default
       action is to pass the packet.

       The following actions can be used in the filter:

       _block_
      The packet is blocked.  There are a number of  ways  in  which  a
      _block_ rule can behave when blocking a packet.  The default behav-
      iour  is to _drop_ packets silently, however this can be overridden
      or made explicit either globally, by setting the _block-policy_ op-
      tion, or on a per-rule basis with one of the following options:

      _drop_  The packet is silently dropped.
      _return-rst_
     This applies only to [_tcp_(4)](https://man.freebsd.org/cgi/man.cgi?query=tcp&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) packets, and issues a  TCP  RST
     which closes the connection.
      _return-icmp_
      _return-icmp6_
     This  causes ICMP messages to be returned for packets which
     match the rule.  By default this  is  an  ICMP  UNREACHABLE
     message,  however  this  can  be overridden by specifying a
     message as a code or number.
      _return_
     This causes a TCP RST to be returned for [_tcp_(4)](https://man.freebsd.org/cgi/man.cgi?query=tcp&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) packets, an
     SCTP ABORT for SCTP and an ICMP  UNREACHABLE  for  UDP  and
     other packets.

      Options  returning ICMP packets currently have no effect if [_pf_(4)](https://man.freebsd.org/cgi/man.cgi?query=pf&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly)
      operates on a [_if\_bridge_(4)](https://man.freebsd.org/cgi/man.cgi?query=if_bridge&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly), as the code to support  this  feature
      has not yet been implemented.

      The  simplest  mechanism  to block everything by default and only
      pass packets that match explicit rules is specify a first filter
      rule of:

     block all

       _match_
      The  packet  is  matched. This mechanism is used to provide fine
      grained filtering without altering  the  block/pass  state  of  a
      packet.  _match_ rules differ from _block_ and _pass_ rules in that pa-
      rameters are set for every rule a packet matches, not only on the
      last  matching  rule.   For  the following parameters, this means
      that the parameter effectively becomes "sticky" until  explicitly
      overridden:  _nat-to_,  _binat-to_,  _rdr-to_,  _queue_, _dnpipe_, _dnqueue_,
      _rtable_, _scrub_

       _pass_  The packet is passed; state is created unless the _no_ _state_ option
      is specified.

       By default [_pf_(4)](https://man.freebsd.org/cgi/man.cgi?query=pf&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) filters packets statefully; the first  time  a packet
       matches a  _pass_ rule, a state entry is created; for subsequent packets
       the filter checks whether the packet matches any state.  If  it  does,
       the  packet  is passed without evaluation of any rules. After the con-
       nection is closed or times out, the state entry is  automatically  re-
       moved.

       This  has  several advantages.  For TCP connections, comparing a packet
       to a state involves checking its sequence numbers, as well as TCP time-
       stamps if a _scrub_ _reassemble_ _tcp_ rule applies to  the  connection.   If
       these  values  are  outside  the narrow windows of expected values, the
       packet is dropped.  This prevents spoofing attacks, such as when an at-
       tacker sends packets with a fake source address/port but does not  know
       the connection's sequence numbers.  Similarly, [_pf_(4)](https://man.freebsd.org/cgi/man.cgi?query=pf&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) knows how to match
       ICMP replies to states. For example,

      pass out inet proto icmp all icmp-type echoreq

       allows echo requests (such as those created by [_ping_(8)](https://man.freebsd.org/cgi/man.cgi?query=ping&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly)) out statefully,
       and matches incoming echo replies correctly to states.

       Also, looking up states is usually faster than evaluating rules.

       Furthermore,  correct  handling of  ICMP error messages is critical to
       many protocols, particularly TCP.  [_pf_(4)](https://man.freebsd.org/cgi/man.cgi?query=pf&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) matches ICMP error messages to
       the correct connection, checks them against connection parameters,  and
       passes  them if appropriate.  For example if an ICMP source quench mes-
       sage referring to a stateful TCP connection arrives, it will be matched
       to the state and get passed.

       Finally, state tracking is required for _nat_, _binat_ and  _rdr_  rules,  in
       order  to  track address and port translations and reverse the transla-
       tion on returning packets.

       [_pf_(4)](https://man.freebsd.org/cgi/man.cgi?query=pf&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) will also create state for other protocols which are  effectively
       stateless by nature.  UDP packets are matched to states using only host
       addresses  and  ports,  and other protocols are matched to states using
       only the host addresses.

       If stateless filtering of individual packets is desired, the  _no_  _state_
       keyword can  be used to specify that state will not be created if this
       is the last matching rule.  A number of parameters can also be  set  to
       affect  how  [_pf_(4)](https://man.freebsd.org/cgi/man.cgi?query=pf&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly)  handles  state  tracking.   See  "STATEFUL TRACKING
       OPTIONS" below for further details.

   **Parameters**
       The rule parameters specify the packets to which  a  rule  applies.   A
       packet  always  comes  in on, or goes out through, one interface.  Most
       parameters are optional.  If a parameter is specified,  the  rule  only
       applies to packets with matching attributes.  Certain parameters can be
       expressed  as  lists,  in which case [_pfctl_(8)](https://man.freebsd.org/cgi/man.cgi?query=pfctl&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) generates all needed rule
       combinations.

       _in_ or _out_
      This rule applies to incoming or outgoing packets.  If neither _in_
      nor _out_ are specified, the rule will match packets in both direc-
      tions.

       _log_ (**all** | **matches** | **to** <_interface_> | **user**)
      In addition to any action specified, log the  packet.   Only  the
      packet  that establishes the state is logged, unless the _no_ _state_
      option is specified.  The logged packets are sent to  a  [_pflog_(4)](https://man.freebsd.org/cgi/man.cgi?query=pflog&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly)
      interface,   by  default  pflog0; pflog0 is  monitored  by  the
      [_pflogd_(8)](https://man.freebsd.org/cgi/man.cgi?query=pflogd&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) logging daemon which logs to the file _/var/log/pflog_ in
      [_pcap_(3)](https://man.freebsd.org/cgi/man.cgi?query=pcap&sektion=3&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) binary format.

      The keywords **all**, **matches**, **to**, and **user** are optional and  can  be
      combined  using  commas,  but  must be enclosed in parentheses if
      given.

      Use **all** to force logging of all packets for a  connection.   This
      is not necessary when _no_ _state_ is explicitly specified.

      If  **matches**  is  specified,  it logs the packet on all subsequent
      matching rules.  It is often  combined  with  **to**  <_interface_>  to
      avoid adding noise to the default log file.

      The  keyword **user** logs the Unix user ID of the user that owns the
      socket and the PID of the process that has the socket open  where
      the  packet  is  sourced  from or destined to (depending on which
      socket is local). This is in addition to the normal  information
      logged.

      Only  the first  packet logged via _log_ _(all,_ _user)_ will have the
      user credentials logged when using stateful matching.

      To specify a logging interface other than pflog0, use the syntax
      **to** <_interface_>.

       _quick_
      If  a  packet matches a rule which has the _quick_ option set, this
      rule is considered the last matching rule, and evaluation of sub-
      sequent rules is skipped.

       _on_ <_interface_>
      This rule applies only to packets coming  in  on, or  going  out
      through,  this particular interface or interface group.  For more
      information  on  interface  groups,  see  the  **group**  keyword  in
      [_ifconfig_(8)](https://man.freebsd.org/cgi/man.cgi?query=ifconfig&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly).   _any_ will match any existing interface except loop-
      back ones.

       <_af_>  This rule applies only to packets of this address family.   Sup-
      ported values are _inet_ and _inet6_.

       _proto_ <_protocol_>
      This  rule applies only to packets of this protocol.  Common pro-
      tocols are [_icmp_(4)](https://man.freebsd.org/cgi/man.cgi?query=icmp&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly), [_icmp6_(4)](https://man.freebsd.org/cgi/man.cgi?query=icmp6&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly), [_tcp_(4)](https://man.freebsd.org/cgi/man.cgi?query=tcp&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly), [_sctp_(4)](https://man.freebsd.org/cgi/man.cgi?query=sctp&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly), and [_udp_(4)](https://man.freebsd.org/cgi/man.cgi?query=udp&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly).  For a
      list of  all  the protocol  name to  number  mappings  used  by
      [_pfctl_(8)](https://man.freebsd.org/cgi/man.cgi?query=pfctl&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly), see the file _/etc/protocols_.

       _from_ <_source_> _port_ <_source_> _os_ <_source_> _to_ <_dest_> _port_ <_dest_>
      This  rule  applies only to packets with the specified source and
      destination addresses and ports.

      Addresses can be specified in CIDR notation (matching netblocks),
      as symbolic host names, interface names or interface group names,
      or as any of the following keywords:

      _any_      Any address.
      _no-route_      Any address which is not currently routable.
      _urpf-failed_     Any source address that fails a  unicast  reverse
        path forwarding (URPF) check, i.e. packets coming
        in  on  an  interface other than that which holds
        the route back to the packet's source address.
      _self_      Expands to all addresses assigned to  all inter-
        faces.
      <_table_>      Any address that matches the given table.

      Ranges of addresses are specified by using the `-' operator.  For
      instance: "10.1.1.10  -  10.1.1.12"  means  all  addresses  from
      10.1.1.10 to 10.1.1.12, hence addresses 10.1.1.10, 10.1.1.11, and
      10.1.1.12.

      Interface names and interface group names, and _self_ can have mod-
      ifiers appended:

      _:network_    Translates to the network(s) attached to the inter-
      face.
      _:broadcast_    Translates  to  the  interface's   broadcast   ad-
      dress(es).
      _:peer_    Translates  to  the point-to-point interface's peer
      address(es).
      _:0_     Do not include interface aliases.

      Host names may also have the _:0_ option appended to  restrict  the
      name resolution to the first of each v4 and non-link-local v6 ad-
      dress found.

      Host  name  resolution  and  interface to address translation are
      done at ruleset load-time.  When the address of an interface  (or
      host name) changes (under DHCP or PPP, for instance), the ruleset
      must  be  reloaded  for the change to be reflected in the kernel.
      Surrounding the interface name (and optional modifiers) in paren-
      theses changes this behaviour.  When the interface name  is  sur-
      rounded  by  parentheses, the rule is automatically updated when-
      ever the interface changes its address.   The  ruleset  does  not
      need to be reloaded.  This is especially useful with _nat_.

      Ports can be specified either by number or by name.  For example,
      port  80 can be specified as _www_. For a list of all port name to
      number mappings used by [_pfctl_(8)](https://man.freebsd.org/cgi/man.cgi?query=pfctl&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly), see the file _/etc/services_.

      Ports and ranges of ports are specified by using these operators:

     =    (equal)
     !=    (unequal)
     <    (less than)
     <=    (less than or equal)
     >    (greater than)
     >=    (greater than or equal)
     :    (range including boundaries)
     ><    (range excluding boundaries)
     <>    (except range)

      `><', `<>' and `:' are binary  operators  (they  take  two  argu-
      ments).  For instance:

      _port_ _2000:2004_
    means `all  ports  >= 2000 and <= 2004', hence ports
    2000, 2001, 2002, 2003 and 2004.

      _port_ _2000_ _><_ _2004_
    means `all ports > 2000  and  <  2004',  hence  ports
    2001, 2002 and 2003.

      _port_ _2000_ _<>_ _2004_
    means `all  ports  < 2000  or  > 2004', hence ports
    1-1999 and 2005-65535.

      The operating system of the source host can be specified  in  the
      case  of  TCP  rules  with  the  _OS_ modifier.  See the "OPERATING
      SYSTEM FINGERPRINTING" section for more information.

      The host, port and OS specifications are optional, as in the fol-
      lowing examples:

     pass in all
     pass in from any to any
     pass in proto tcp from any port < 1024 to any
     pass in proto tcp from any to any port 25
     pass in proto tcp from 10.0.0.0/8 port >= 1024 \
    to ! 10.1.2.3 port != ssh
     pass in proto tcp from any os "OpenBSD"

       _all_   This is equivalent to "from any to any".

       _group_ <_group_>
      Similar to _user_, this rule only applies  to  packets  of  sockets
      owned by the specified group.

       _user_ <_user_>
      This  rule only applies to packets of sockets owned by the speci-
      fied user.  For outgoing connections initiated from the firewall,
      this is the user that opened the connection.  For incoming  con-
      nections to the firewall itself, this is the user that listens on
      the destination port.  For forwarded connections, where the fire-
      wall  is  not  a  connection  endpoint,  the  user  and group are
      _unknown_.

      All packets, both outgoing and incoming, of  one  connection  are
      associated  with the same user and group. Only TCP and UDP pack-
      ets can be associated with users; for other protocols these para-
      meters are ignored.

      User and group refer to the effective (as opposed to  the  real)
      IDs,  in  case  the socket is created by a setuid/setgid process.
      User and group IDs are stored when a socket is  created;  when  a
      process  creates  a  listening  socket  as root (for instance, by
      binding to a privileged port) and subsequently changes to another
      user ID (to drop privileges), the credentials will remain root.

      User and group IDs can be specified as either numbers  or names.
      The  syntax  is  similar to the one for ports.  The value _unknown_
      matches packets of forwarded connections. _unknown_  can  only  be
      used  with the operators **=** and **!=**.  Other constructs like **user** **>=**
      **unknown** are invalid.  Forwarded packets  with  unknown  user  and
      group ID match only rules that explicitly compare against _unknown_
      with  the operators  **=**  or  **!=**.  For instance **user** **>=** **0** does not
      match forwarded packets.  The following example allows  only  se-
      lected users to open outgoing connections:

     block out proto { tcp, udp } all
     pass  out proto { tcp, udp } all user { < 1000, dhartmei }

      The example below permits users with uid between 1000 and 1500 to
      open connections:

     block out proto tcp all
     pass  out proto tcp from self user { 999 >< 1501 }

      The  `:' operator, which works for port number matching, does not
      work for **user** and **group** match.

       _flags_ <_a_> /<_b_> | /<_b_> | any
      This rule only applies to TCP packets that have the flags <_a_> set
      out of set <_b_>.  Flags not specified in  <_b_>  are ignored.   For
      stateful  connections,  the  default  is _flags_ _S/SA_.  To indicate
      that flags should not be checked at all, specify _flags_ _any_.   The
      flags  are: (F)IN, (S)YN, (R)ST, (P)USH, (A)CK, (U)RG, (E)CE, and
      C(W)R.

      _flags_ _S/S_  Flag SYN is set.  The other flags are ignored.

      _flags_ _S/SA_  This is the default setting for stateful connections.
    Out of SYN and ACK, exactly SYN  may  be  set.   SYN,
    SYN+PSH  and  SYN+RST match, but  SYN+ACK,  ACK and
    ACK+RST do not.  This is more restrictive  than  the
    previous example.

      _flags_ _/SFRA_
    If  the  first  set  is not specified, it defaults to
    none. All of SYN, FIN, RST and ACK must be unset.

      Because _flags_ _S/SA_ is applied by  default (unless  _no_  _state_  is
      specified),  only the initial SYN packet of a TCP handshake will
      create a state for a TCP connection.  It is possible to  be  less
      restrictive, and allow state creation from intermediate (non-SYN)
      packets,  by specifying _flags_ _any_.  This will cause [_pf_(4)](https://man.freebsd.org/cgi/man.cgi?query=pf&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) to syn-
      chronize to existing connections, for instance if one flushes the
      state table.  However,  states  created  from  such  intermediate
      packets  may be missing connection details such as the TCP window
      scaling factor.  States which modify the  packet  flow,  such  as
      those  affected  by  _af-to_,  _nat_, _binat_ _or_ _rdr_ rules, _modulate_ or
      _synproxy_ _state_ options, or scrubbed with _reassemble_ _tcp_ will also
      not be recoverable from intermediate packets.   Such  connections
      will stall and time out.

       _icmp-type_ <_type_> _file_ _..._ [code <_code_>]

       _icmp6-type_ <_type_> _file_ _..._ [code <_code_>]
      This  rule only applies to ICMP or ICMPv6 packets with the speci-
      fied type and code.  Text names for  ICMP types  and  codes  are
      listed in [_icmp_(4)](https://man.freebsd.org/cgi/man.cgi?query=icmp&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) and [_icmp6_(4)](https://man.freebsd.org/cgi/man.cgi?query=icmp6&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly).  This parameter is only valid for
      rules  that  cover protocols ICMP or ICMP6.  The protocol and the
      ICMP type indicator (_icmp-type_ or _icmp6-type_) must match.

       _tos_ <_string_> | <_number_>
      This rule applies to packets with the  specified  _TOS_  bits  set.
      _TOS_  may  be  given  as  one  of _critical_, _inetcontrol_, _lowdelay_,
      _netcontrol_, _throughput_, _reliability_, or one of the DiffServ  Code
      Points:  _ef_,  _va_, _af11_ ... _af43_, _cs0_ ... _cs7_; or as either hex or
      decimal.

      For example, the following rules are identical:

     pass all tos lowdelay
     pass all tos 0x10
     pass all tos 16

       _allow-opts_
      By default, packets with IPv4 options or IPv6 hop-by-hop or  des-
      tination  options header are blocked.  When _allow-opts_ is speci-
      fied for a _pass_ rule, packets that pass the filter based on  that
      rule  (last  matching)  do  so even if they contain options.  For
      packets that match state, the rule  that  initially  created  the
      state  is used. The  implicit  _pass_  rule, that is used when a
      packet does not match any rules, does not allow IP options or op-
      tion headers.  Note that IPv6 packets with type 0 routing headers
      are always dropped.

       _label_ <_string_>
      Adds a label (name) to the rule, which can be  used  to  identify
      the  rule.   For instance, pfctl -s labels shows per-rule statis-
      tics for rules that have labels.

      The following macros can be used in labels:

     _$if_      The interface.
     _$srcaddr_  The source IP address.
     _$dstaddr_  The destination IP address.
     _$srcport_  The source port specification.
     _$dstport_  The destination port specification.
     _$proto_    The protocol name.
     _$nr_      The rule number.

      For example:

     ips = "{ 1.2.3.4, 1.2.3.5 }"
     pass in proto tcp from any to $ips \
    port > 1023 label "$dstaddr:$dstport"

      expands to

     pass in inet proto tcp from any to 1.2.3.4 \
    port > 1023 label "1.2.3.4:>1023"
     pass in inet proto tcp from any to 1.2.3.5 \
    port > 1023 label "1.2.3.5:>1023"

      The macro expansion for the _label_ directive occurs only  at  con-
      figuration file parse time, not during runtime.

       _ridentifier_ <_number_>
      Add an identifier (number) to the rule, which can be used to cor-
      relate the rule to pflog entries, even after ruleset updates.

       **max-pkt-rate** _number_/_seconds_
      Measure  the rate of packets matching the rule and states created
      by it.  When the specified  rate  is  exceeded,  the  rule  stops
      matching.  Only  packets in the direction in which the state was
      created are considered, so that typically requests  are  counted
      and replies are not.  For example, to pass up to 100 ICMP packets
      per 10 seconds:

     block in proto icmp
     pass in proto icmp max-pkt-rate 100/10

      When  the rate  is  exceeded, all ICMP is blocked until the rate
      falls below 100 per 10 seconds again.

       _max-pkt-size_ <_number_>
      Limit each packet to be no more  than  the  specified  number  of
      bytes.  This includes the IP header, but not any layer 2 header.

       _queue_ <_queue_> | (<_queue_>, <_queue_>)
      Packets  matching this  rule  will  be assigned to the specified
      queue.  If two queues are given, packets  which  have  a  _TOS_  of
      _lowdelay_  and  TCP  ACKs with no data payload will be assigned to
      the second one.  See "QUEUEING" for setup details.

      For example:

     pass in proto tcp to port 25 queue mail
     pass in proto tcp to port 22 queue(ssh_bulk, ssh_prio)

       **set** **prio** _priority_ | (_priority_, _priority_)
      Packets matching this rule will be assigned a  specific  queueing
      priority.  Priorities  are assigned as integers 0 through 7.  If
      the packet is transmitted on a [_vlan_(4)](https://man.freebsd.org/cgi/man.cgi?query=vlan&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly)  interface,  the  queueing
      priority will be written as the priority code point in the 802.1Q
      VLAN  header.  If two priorities are given, TCP ACKs with no data
      payload and packets which have a TOS of **lowdelay** will be assigned
      to the second one.

      For example:

     pass in proto tcp to port 25 set prio 2
     pass in proto tcp to port 22 set prio (2, 5)

       [**!**]**received-on** _interface_
      Only match packets which were received on the specified _interface_
      (or interface group).  _any_ will match any existing interface  ex-
      cept loopback ones.

       _tag_ <_string_>
      Packets  matching this  rule  will  be tagged with the specified
      string.  The tag acts as an internal marker that can be  used  to
      identify  these packets later on. This can be used, for example,
      to provide trust between interfaces and to determine  if  packets
      have  been  processed  by translation rules.  Tags are "sticky",
      meaning that the packet will be tagged even if the  rule  is  not
      the  last matching rule. Further matching rules can replace the
      tag with a new one but will not remove a previously applied  tag.
      A packet is only ever assigned one tag at a time. Packet tagging
      can  be done during _nat_, _rdr_, _binat_ or _ether_ rules in addition to
      filter rules.  Tags take the same macros as labels (see above).

       _tagged_ <_string_>
      Used with filter, translation or  scrub  rules  to  specify  that
      packets  must  already  be  tagged with the given tag in order to
      match the rule.

       _rtable_ <_number_>
      Used to select an alternate routing table for the routing lookup.
      Only effective before the route lookup happened, i.e.  when  fil-
      tering inbound.

       _divert-to_ <_host_> _port_ <_port_>
      Used to [_divert_(4)](https://man.freebsd.org/cgi/man.cgi?query=divert&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) packets to the given divert _port_.  Historically
      OpenBSD pf has another meaning for this, and FreeBSD pf uses this
      syntax  to  support [_divert_(4)](https://man.freebsd.org/cgi/man.cgi?query=divert&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) instead. Hence, _host_ has no meaning
      and can be set to anything like 127.0.0.1.  If a packet is re-in-
      jected and does not change direction then it will not  be re-di-
      verted.

       _divert-reply_
      It has no meaning in FreeBSD pf.

       _probability_ <_number_>
      A probability  attribute can be attached to a rule, with a value
      set between 0 and 1, bounds not included. In that case, the rule
      will be honoured using the given probability value only.  For ex-
      ample, the following rule will drop 20% of incoming ICMP packets:

     block in proto icmp probability 20%

       _prio_ <_number_>
      Only match packets which have the given  queueing  priority  as-
      signed.

[**ROUTING**](https://man.freebsd.org/cgi/man.cgi?query=pf.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#end)
       If  a  packet matches a rule with a route option set, the packet filter
       will route the packet according to the type of route option.  When such
       a rule creates state, the route option is also applied to  all  packets
       matching the same connection.

       _route-to_
      The  _route-to_ option routes the packet to the specified interface
      with an address for the next hop. When a _route-to_  rule  creates
      state, only packets that pass in the same direction as the filter
      rule  specifies  will  be routed in this way.  Packets passing in
      the opposite direction (replies) are not affected and are routed
      normally.

       _reply-to_
      The  _reply-to_  option  is similar to _route-to_, but routes packets
      that pass in the opposite direction (replies)  to the  specified
      interface.   Opposite direction is only defined in the context of
      a state entry, and _reply-to_ is useful only in rules  that create
      state.   It can be used on systems with multiple external connec-
      tions to route all outgoing packets of a connection  through  the
      interface the  incoming  connection  arrived  through (symmetric
      routing enforcement).

       _dup-to_
      The _dup-to_ option creates a duplicate of the packet and routes it
      like _route-to_.  The original packet gets routed  as  it  normally
      would.

[**POOL OPTIONS**](https://man.freebsd.org/cgi/man.cgi?query=pf.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#end)
       For  _nat_  and  _rdr_  rules,  (as well as for the _route-to_, _reply-to_ and
       _dup-to_ rule options) for which there is a  single  redirection  address
       which  has a subnet mask smaller than 32 for IPv4 or 128 for IPv6 (more
       than one IP address), a variety of different methods for assigning this
       address can be used:

       _bitmask_
      The _bitmask_ option applies the network portion of the redirection
      address to the address to be modified (source with _nat_,  destina-
      tion with _rdr_).

       _random_
      The _random_ option selects an address at random within the defined
      block of addresses.

       _source-hash_
      The  _source-hash_  option uses a hash of the source address to de-
      termine the redirection address, ensuring that  the  redirection
      address  is  always the same for a given source.  An optional key
      can be specified after this keyword either in hex or as a string;
      by default [_pfctl_(8)](https://man.freebsd.org/cgi/man.cgi?query=pfctl&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) randomly  generates  a  key  for  source-hash
      every time the ruleset is reloaded.

       _round-robin_
      The _round-robin_ option loops through the redirection address(es).

      When  more  than one redirection address is specified, _bitmask_ is
      not permitted as a pool type.

       _static-port_
      With _nat_ rules, the _static-port_ option prevents [_pf_(4)](https://man.freebsd.org/cgi/man.cgi?query=pf&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) from  modi-
      fying the source port on TCP and UDP packets.

       _map-e-portset_ <_psid-offset_> / <_psid-len_> / <_psid_>
      With  _nat_ rules, the _map-e-portset_ option enables the source port
      translation of MAP-E (RFC 7597) Customer Edge.  In order to  make
      the host act as a MAP-E Customer Edge, setting up a tunneling in-
      terface  and  pass rules for encapsulated packets are required in
      addition to the map-e-portset nat rule.

      For example:

     nat on $gif_mape_if from $int_if:network to any \
    -> $ipv4_mape_src map-e-portset 6/8/0x34

      sets PSID offset 6, PSID length 8, PSID 0x34.

       _endpoint-independent_
      With _nat_ rules, the _endpoint-independent_ option  caues  [_pf_(4)](https://man.freebsd.org/cgi/man.cgi?query=pf&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly)  to
      always  map connections from a UDP source address and port to the
      same NAT address and port.  This feature  implements  "full-cone"
      NAT behavior.

       Additionally,  options  _sticky-address_  and  _prefer-ipv6-nexthop_ can be
       specified to influence how IP addresses selected from pools.

       The _sticky-address_ option can be specified to help ensure that multiple
       connections from the same source are mapped to the same redirection ad-
       dress.  This option can be used with the _random_ and  _round-robin_  pool
       options.  Note that by default these associations are destroyed as soon
       as there are no longer states which refer to them; in order to make the
       mappings  last  beyond  the lifetime of the states, increase the global
       options with _set_ _timeout_ _src.track_.  See  "STATEFUL  TRACKING  OPTIONS"
       for more ways to control the source tracking.

       The  _prefer-ipv6-nexthop_ option allows for IPv6 addresses to be used as
       the nexthop for IPv4 packets routed with the _route-to_ rule option. If a
       table is used with IPv4 and IPv6 addresses, first  the  IPv6  addresses
       will be used in round-robin fashion, then IPv4 addresses.

[**STATE MODULATION**](https://man.freebsd.org/cgi/man.cgi?query=pf.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#end)
       Much  of  the security derived from TCP is attributable to how well the
       initial sequence numbers (ISNs) are chosen.  Some popular stack imple-
       mentations  choose  _very_ poor ISNs and thus are normally susceptible to
       ISN prediction exploits.  By applying a _modulate_ _state_ rule  to a  TCP
       connection, [_pf_(4)](https://man.freebsd.org/cgi/man.cgi?query=pf&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) will create a high quality random sequence number for
       each connection endpoint.

       The  _modulate_ _state_ directive implicitly keeps state on the rule and is
       only applicable to TCP connections.

       For instance:

      block all
      pass out proto tcp from any to any modulate state
      pass in  proto tcp from any to any port 25 flags S/SFRA modulate state

       Note that modulated connections will not recover when the  state  table
       is  lost  (firewall  reboot,  flushing the state table, etc...).  [_pf_(4)](https://man.freebsd.org/cgi/man.cgi?query=pf&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly)
       will not be able to infer a connection  again  after  the  state  table
       flushes the  connection's modulator.  When the state is lost, the con-
       nection may be left dangling until the respective  endpoints  time  out
       the  connection.   It  is possible on a fast local network for the end-
       points to start an ACK storm while trying to  resynchronize  after  the
       loss  of  the  modulator.  The default _flags_ settings (or a more strict
       equivalent) should be used on  _modulate_ _state_  rules  to  prevent  ACK
       storms.

       Note  that  alternative methods  are  available to prevent loss of the
       state table and allow for firewall failover.  See [_carp_(4)](https://man.freebsd.org/cgi/man.cgi?query=carp&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) and [_pfsync_(4)](https://man.freebsd.org/cgi/man.cgi?query=pfsync&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly)
       for further information.

[**SYN PROXY**](https://man.freebsd.org/cgi/man.cgi?query=pf.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#end)
       By default, [_pf_(4)](https://man.freebsd.org/cgi/man.cgi?query=pf&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) passes packets that are part of  a  [_tcp_(4)](https://man.freebsd.org/cgi/man.cgi?query=tcp&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly)  handshake
       between the endpoints. The _synproxy_ _state_ option can be used to cause
       [_pf_(4)](https://man.freebsd.org/cgi/man.cgi?query=pf&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) itself to complete the handshake with the active  endpoint,  per-
       form  a handshake  with the passive endpoint, and then forward packets
       between the endpoints.

       No packets are sent to the passive endpoint before the active  endpoint
       has  completed  the  handshake, hence so-called SYN floods with spoofed
       source addresses will not reach the passive  endpoint,  as  the sender
       can't complete the handshake.

       The proxy is transparent to both endpoints, they each see a single con-
       nection from/to  the other endpoint.  [_pf_(4)](https://man.freebsd.org/cgi/man.cgi?query=pf&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) chooses random initial se-
       quence numbers for both handshakes.  Once the handshakes are completed,
       the sequence number modulators  (see  previous  section)  are  used  to
       translate  further  packets of the connection.  _synproxy_ _state_ includes
       _modulate_ _state_.

       Rules with _synproxy_ will not work if [_pf_(4)](https://man.freebsd.org/cgi/man.cgi?query=pf&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly)  operates  on  a  [_bridge_(4)](https://man.freebsd.org/cgi/man.cgi?query=bridge&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly).
       Also they act on incoming SYN packets only.

       Example:

      pass in proto tcp from any to any port www synproxy state

[**STATEFUL TRACKING OPTIONS**](https://man.freebsd.org/cgi/man.cgi?query=pf.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#end)
       A  number  of  options related to stateful tracking can be applied on a
       per-rule basis. _keep_ _state_, _modulate_ _state_ and _synproxy_ _state_  support
       these options, and _keep_ _state_ must be specified explicitly to apply op-
       tions to a rule.

       _max_ <_number_>
      Limits the number of concurrent states the rule may create.  When
      this  limit  is  reached, further packets that would create state
      are dropped until existing states time out.
       _no-sync_
      Prevent state changes for states created by this  rule  from  ap-
      pearing on the [_pfsync_(4)](https://man.freebsd.org/cgi/man.cgi?query=pfsync&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) interface.
       <_timeout_> <_seconds_>
      Changes  the timeout values used for states created by this rule.
      For a list of all valid timeout names, see "OPTIONS" above.
       _sloppy_
      Uses a sloppy TCP connection tracker that does not check sequence
      numbers at all, which makes insertion and ICMP  teardown  attacks
      way  easier.  This is intended to be used in situations where one
      does not see all packets of  a  connection,  e.g. in  asymmetric
      routing  situations.   Cannot  be used with modulate or synproxy
      state.
       _pflow_
      States created by this rule are exported on the  [_pflow_(4)](https://man.freebsd.org/cgi/man.cgi?query=pflow&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) inter-
      face.
       _allow-related_
      Automatically  allow  connections related to this one, regardless
      of rules that might otherwise affect them.  This  currently  only
      applies to SCTP multihomed connection.

       Multiple options can be specified, separated by commas:

      pass in proto tcp from any to any \
     port www keep state \
     (max 100, source-track rule, max-src-nodes 75, \
     max-src-states 3, tcp.established 60, tcp.closing 5)

       When  the  _source-track_ keyword is specified, the number of states per
       source IP is tracked.

       _source-track_ _rule_
      The maximum number of states created by this rule is  limited  by
      the  rule's _max-src-nodes_ and _max-src-states_ options.  Only state
      entries created by this particular rule count toward  the rule's
      limits.
       _source-track_ _global_
      The number of states created by all rules that use this option is
      limited. Each  rule  can  specify  different  _max-src-nodes_ and
      _max-src-states_ options, however state entries created by any par-
      ticipating rule count towards each individual rule's limits.

       The following limits can be set:

       _max-src-nodes_ <_number_>
      Limits the maximum number of source addresses which can  simulta-
      neously have state table entries.
       _max-src-states_ <_number_>
      Limits  the  maximum  number of simultaneous state entries that a
      single source address can create with this rule.

       For stateful TCP connections, limits on established  connections  (con-
       nections  which have completed the TCP 3-way handshake) can also be en-
       forced per source IP.

       _max-src-conn_ <_number_>
      Limits the maximum number of simultaneous TCP  connections  which
      have completed the 3-way handshake that a single host can make.
       _max-src-conn-rate_ <_number_> / <_seconds_>
      Limit the rate of new connections over a time interval.  The con-
      nection rate is an approximation calculated as a moving average.

       When  one of these limits is reached, further packets that would create
       state are dropped until existing states time out.

       Because the 3-way handshake ensures that the source address is not  be-
       ing spoofed, more aggressive action can be taken based on these limits.
       With  the  _overload_ <_table_> state option, source IP addresses which hit
       either of the limits on established connections will be added  to  the
       named  table.   This  table can be used in the ruleset to block further
       activity from the offending host, redirect it to a tarpit  process,  or
       restrict its bandwidth.

       The  optional  _flush_  keyword  kills all states created by the matching
       rule which originate from the host which  exceeds  these  limits.   The
       _global_  modifier to the flush command kills all states originating from
       the offending host, regardless of which rule created the state.

       For example, the following rules will  protect  the  webserver  against
       hosts  making  more than 100 connections in 10 seconds. Any host which
       connects faster than this rate will  have  its  address added  to  the
       <bad_hosts> table and have all states originating from it flushed.  Any
       new  packets arriving from this host will be dropped unconditionally by
       the block rule.

      block quick from <bad_hosts>
      pass in on $ext_if proto tcp to $webserver port www keep state \
       (max-src-conn-rate 100/10, overload <bad_hosts> flush global)

[**OPERATING SYSTEM FINGERPRINTING**](https://man.freebsd.org/cgi/man.cgi?query=pf.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#end)
       Passive OS Fingerprinting is a mechanism to inspect nuances  of a  TCP
       connection's  initial SYN packet and guess at the host's operating sys-
       tem.  Unfortunately these nuances are easily spoofed by an attacker  so
       the  fingerprint  is  not useful in making security decisions.  But the
       fingerprint is typically accurate enough to make policy decisions upon.

       The fingerprints may be specified by operating system  class,  by  ver-
       sion,  or  by  subtype/patchlevel.  The class of an operating system is
       typically the vendor or genre and would be OpenBSD for the [_pf_(4)](https://man.freebsd.org/cgi/man.cgi?query=pf&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly)  fire-
       wall  itself.   The  version of the oldest available OpenBSD release on
       the main FTP site would be 2.6 and the fingerprint would be written

      **"OpenBSD** **2.6"**

       The subtype of an operating system is typically used  to  describe  the
       patchlevel  if that patch led to changes in the TCP stack behavior.  In
       the case of OpenBSD, the only subtype is for  a fingerprint  that  was
       normalized by the _no-df_ scrub option and would be specified as

      **"OpenBSD** **3.3** **no-df"**

       Fingerprints  for  most popular  operating  systems  are  provided  by
       [_pf.os_(5)](https://man.freebsd.org/cgi/man.cgi?query=pf.os&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly).  Once [_pf_(4)](https://man.freebsd.org/cgi/man.cgi?query=pf&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) is running, a complete list  of  known  operating
       system fingerprints may be listed by running:

      **#** **pfctl** **-so**

       Filter rules can enforce policy at any level of operating system speci-
       fication assuming a fingerprint is present.  Policy could limit traffic
       to  approved  operating systems  or  even  ban traffic from hosts that
       aren't at the latest service pack.

       The _unknown_ class can also be used as the fingerprint which will  match
       packets for which no operating system fingerprint is known.

       Examples:

      pass  out proto tcp from any os OpenBSD
      block out proto tcp from any os Doors
      block out proto tcp from any os "Doors PT"
      block out proto tcp from any os "Doors PT SP3"
      block out from any os "unknown"
      pass on lo0 proto tcp from any os "OpenBSD 3.3 lo0"

       Operating  system fingerprinting is limited only to the TCP SYN packet.
       This means that it will not work on other protocols and will not  match
       a currently established connection.

       Caveat: operating  system  fingerprints are occasionally wrong.  There
       are three problems: an attacker can trivially craft packets  to appear
       as  any operating  system;  an operating system patch could change the
       stack behavior and no fingerprints will match it until the database  is
       updated; and multiple operating systems may have the same fingerprint.

[**BLOCKING SPOOFED TRAFFIC**](https://man.freebsd.org/cgi/man.cgi?query=pf.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#end)
       "Spoofing"  is the faking of IP addresses, typically for malicious pur-
       poses.  The _antispoof_ directive expands to a set of filter rules  which
       will  block  all  traffic with a source IP from the network(s) directly
       connected to  the  specified  interface(s)  from  entering  the system
       through any other interface.

       For example, the line

      antispoof for lo0

       expands to

      block drop in on ! lo0 inet from 127.0.0.1/8 to any
      block drop in on ! lo0 inet6 from ::1 to any

       For non-loopback interfaces, there are additional rules to block incom-
       ing  packets  with  a  source  IP  address identical to the interface's
       IP(s).  For example, assuming the interface wi0 had an  IP  address  of
       10.0.0.1 and a netmask of 255.255.255.0, the line

      antispoof for wi0 inet

       expands to

      block drop in on ! wi0 inet from 10.0.0.0/24 to any
      block drop in inet from 10.0.0.1 to any

       Caveat: Rules created by the _antispoof_ directive interfere with packets
       sent  over  loopback  interfaces  to  local addresses.  One should pass
       these explicitly.

[**FRAGMENT HANDLING**](https://man.freebsd.org/cgi/man.cgi?query=pf.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#end)
       The size of IP datagrams (packets) can be significantly larger than the
       maximum transmission unit (MTU) of the network. In cases  when it  is
       necessary  or  more  efficient  to  send  such large packets, the large
       packet will be fragmented into many smaller packets that will each  fit
       onto  the wire. Unfortunately for a firewalling device, only the first
       logical fragment will contain the necessary header information for  the
       subprotocol  that allows [_pf_(4)](https://man.freebsd.org/cgi/man.cgi?query=pf&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) to filter on things such as TCP ports or
       to perform NAT.

       Besides the use of _set_ _reassemble_ option or _scrub_ rules as described in
       "TRAFFIC NORMALIZATION" above, there are  three options  for  handling
       fragments in the packet filter.

       One  alternative  is  to filter individual fragments with filter rules.
       If no _scrub_ rule applies to a fragment or _set_ _reassemble_ is set to **no** ,
       it is passed to the filter.  Filter rules with matching IP header para-
       meters decide whether the fragment is passed or blocked,  in  the  same
       way  as complete  packets are filtered.  Without reassembly, fragments
       can only be filtered based on IP header fields (source/destination  ad-
       dress,  protocol),  since  subprotocol  header fields are not available
       (TCP/UDP port numbers, ICMP code/type). The  _fragment_  option  can  be
       used  to restrict filter rules to apply only to fragments, but not com-
       plete packets.  Filter rules without the _fragment_ option still apply to
       fragments, if they only specify IP header fields.   For instance,  the
       rule

      pass in proto tcp from any to any port 80

       never  applies  to  a  fragment,  even if the fragment is part of a TCP
       packet with destination port 80, because without reassembly this infor-
       mation is not available for each fragment.  This also means that  frag-
       ments  cannot  create  new or match existing state table entries, which
       makes stateful filtering and address translation (NAT, redirection) for
       fragments impossible.

       It's also possible to reassemble only certain fragments by  specifying
       source  or  destination addresses  or protocols as parameters in _scrub_
       rules.

       In most cases, the benefits of reassembly outweigh the additional  mem-
       ory  cost,  and it's recommended to use _set_ _reassemble_ option or _scrub_
       rules with the _fragment_ _reassemble_ modifier  to reassemble  all  frag-
       ments.

       The  memory  allocated  for  fragment  caching  can  be limited  using
       [_pfctl_(8)](https://man.freebsd.org/cgi/man.cgi?query=pfctl&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly).  Once this limit is reached, fragments that would have to  be
       cached are dropped until other entries time out.  The timeout value can
       also be adjusted.

       When  forwarding reassembled IPv6 packets, pf refragments them with the
       original maximum fragment size. This allows the  sender  to  determine
       the optimal fragment size by path MTU discovery.

[**ANCHORS**](https://man.freebsd.org/cgi/man.cgi?query=pf.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#end)
       Besides the  main  ruleset, [_pfctl_(8)](https://man.freebsd.org/cgi/man.cgi?query=pfctl&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) can load rulesets into _anchor_ at-
       tachment points.  An _anchor_ is a container that can hold rules, address
       tables, and other anchors.

       An _anchor_ has a name which specifies the path  where  [_pfctl_(8)](https://man.freebsd.org/cgi/man.cgi?query=pfctl&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly)  can  be
       used  to access the anchor to perform operations on it, such as attach-
       ing child anchors to it or loading  rules  into it.   Anchors  may  be
       nested, with  components  separated  by `/' characters, similar to how
       file system hierarchies are laid out.  The main ruleset is actually the
       default anchor, so filter and translation rules, for example, may  also
       be contained in any anchor.

       An  anchor can reference another _anchor_ attachment point using the fol-
       lowing kinds of rules:

       _nat-anchor_ <_name_>
      Evaluates the _nat_ rules in the specified _anchor_.

       _rdr-anchor_ <_name_>
      Evaluates the _rdr_ rules in the specified _anchor_.

       _binat-anchor_ <_name_>
      Evaluates the _binat_ rules in the specified _anchor_.

       _anchor_ <_name_>
      Evaluates the filter rules in the specified _anchor_.

       _load_ _anchor_ <_name_> _from_ <_file_>
      Loads the rules from the specified file into the anchor _name_.

       When evaluation of the main ruleset reaches an _anchor_ rule, [_pf_(4)](https://man.freebsd.org/cgi/man.cgi?query=pf&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly)  will
       proceed to evaluate all rules specified in that anchor.

       Matching  filter and translation rules marked with the _quick_ option are
       final and abort the evaluation of the rules in other  anchors  and  the
       main  ruleset. If  the _anchor_ itself is marked with the _quick_ option,
       ruleset evaluation will terminate when the  anchor  is  exited  if  the
       packet is matched by any rule within the anchor.

       _anchor_  rules  are  evaluated  relative to the anchor in which they are
       contained.  For example, all _anchor_ rules specified in the main ruleset
       will reference anchor attachment points underneath  the main  ruleset,
       and  _anchor_  rules  specified  in a file loaded from a _load_ _anchor_ rule
       will be attached under that anchor point.

       Rules may be contained in _anchor_ attachment points which do not contain
       any rules when the main ruleset is loaded, and later such  anchors  can
       be  manipulated through [_pfctl_(8)](https://man.freebsd.org/cgi/man.cgi?query=pfctl&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) without reloading the main ruleset or
       other anchors.  For example,

      ext_if = "kue0"
      block on $ext_if all
      anchor spam
      pass out on $ext_if all
      pass in on $ext_if proto tcp from any \
     to $ext_if port smtp

       blocks all packets on the external interface by default, then evaluates
       all rules in the _anchor_ named "spam", and finally passes  all  outgoing
       connections and incoming connections to port 25.

      # echo "block in quick from 1.2.3.4 to any" | \
     pfctl -a spam -f -

       This loads a single rule into the _anchor_, which blocks all packets from
       a specific address.

       The anchor can also be populated by adding a _load_ _anchor_ rule after the
       _anchor_ rule:

      anchor spam
      load anchor spam from "/etc/pf-spam.conf"

       When  [_pfctl_(8)](https://man.freebsd.org/cgi/man.cgi?query=pfctl&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly)  loads **pf.conf**, it will also load all the rules from the
       file _/etc/pf-spam.conf_ into the anchor.

       Optionally, _anchor_ rules can specify packet filtering parameters  using
       the  same syntax as filter rules.  When parameters are used, the _anchor_
       rule is only evaluated for matching packets.  This  allows  conditional
       evaluation of anchors, like:

      block on $ext_if all
      anchor spam proto tcp from any to any port smtp
      pass out on $ext_if all
      pass in on $ext_if proto tcp from any to $ext_if port smtp

       The  rules  inside  _anchor_ spam are only evaluated for _tcp_ packets with
       destination port 25.  Hence,

      # echo "block in quick from 1.2.3.4 to any" | \
     pfctl -a spam -f -

       will only block connections from 1.2.3.4 to port 25.

       Anchors may end with the asterisk (`*') character, which signifies that
       all anchors attached at that point should be evaluated in the alphabet-
       ical ordering of their anchor name.  For example,

      anchor "spam/*"

       will evaluate each rule in each anchor attached to  the  **spam**  anchor.
       Note  that  it will only evaluate anchors that are directly attached to
       the **spam** anchor, and will not descend to evaluate anchors recursively.

       Since anchors are evaluated relative to the anchor in  which  they  are
       contained,  there  is a mechanism for accessing the parent and ancestor
       anchors of a given anchor.  Similar to file system  path  name  resolu-
       tion,  if  the  sequence  ".." appears as an anchor path component, the
       parent anchor of the current anchor in  the  path  evaluation  at  that
       point  will become the new current anchor.  As an example, consider the
       following:

      # echo ' anchor "spam/allowed" ' | pfctl -f -
      # echo -e ' anchor "../banned" \n pass' | \
     pfctl -a spam/allowed -f -

       Evaluation of the main ruleset will lead into the **spam/allowed**  anchor,
       which will evaluate the rules in the **spam/banned** anchor, if any, before
       finally evaluating the _pass_ rule.

       An  _anchor_  rule can also contain a filter ruleset in a brace-delimited
       block.  In that case, no separate loading of rules into the  anchor  is
       required.   Brace delimited blocks may contain rules or other brace-de-
       limited blocks. When an anchor is populated this way, the anchor  name
       becomes optional.

      anchor "external" on $ext_if {
       block
       anchor out {
        pass proto tcp from any to port { 25, 80, 443 }
       }
       pass in proto tcp to any port 22
      }

       Since the parser specification for anchor names is a string, any refer-
       ence  to  an  anchor name containing `/' characters will require double
       quote (`"') characters around the anchor name.

[**SCTP CONSIDERATIONS**](https://man.freebsd.org/cgi/man.cgi?query=pf.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#end)
       [_pf_(4)](https://man.freebsd.org/cgi/man.cgi?query=pf&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) supports [_sctp_(4)](https://man.freebsd.org/cgi/man.cgi?query=sctp&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) connections.  It can match  ports,  track  state
       and  NAT  SCTP traffic. However, it will not alter port numbers during
       nat or rdr translations.  Doing so would break SCTP multihoming.

[**TRANSLATION EXAMPLES**](https://man.freebsd.org/cgi/man.cgi?query=pf.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#end)
       This example maps incoming requests on port 80 to port 8080, on which a
       daemon is running (because, for example, it is not  run as  root,  and
       therefore lacks permission to bind to port 80).

      # use a macro for the interface name, so it can be changed easily
      ext_if = "ne3"

      # map daemon on 8080 to appear to be on 80
      match in on $ext_if proto tcp from any to any port 80 \
     rdr-to 127.0.0.1 port 8080

       If  a  _pass_  rule is used with the _quick_ modifier, packets matching the
       translation rule are passed without inspecting subsequent filter rules:

      pass in quick on $ext_if proto tcp from any to any port 80 \
     rdr-to 127.0.0.1 port 8080

       In the example below, vlan12 is configured as  192.168.168.1;  the  ma-
       chine   translates   all   packets   coming  from  192.168.168.0/24  to
       204.92.77.111 when they are going  out  any  interface  except  vlan12.
       This  has  the  net  effect of making traffic from the 192.168.168.0/24
       network appear as  though  it is  the  Internet   routable   address
       204.92.77.111  to  nodes  behind any interface on the router except for
       the  nodes  on  vlan12.  (Thus,  192.168.168.1  can   talk   to   the
       192.168.168.0/24 nodes.)

      match out on ! vlan12 from 192.168.168.0/24 to any nat-to 204.92.77.111

       This  longer  example  uses both a NAT and a redirection.  The external
       interface has the address 157.161.48.183.  On localhost, we are running
       [_ftp-proxy_(8)](https://man.freebsd.org/cgi/man.cgi?query=ftp-proxy&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly), waiting for FTP sessions to be  redirected  to  it.   The
       three mandatory anchors for [_ftp-proxy_(8)](https://man.freebsd.org/cgi/man.cgi?query=ftp-proxy&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) are omitted from this example;
       see the [_ftp-proxy_(8)](https://man.freebsd.org/cgi/man.cgi?query=ftp-proxy&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) manpage.

      # NAT
      # Translate outgoing packets' source addresses (any protocol).
      # In this case, any address but the gateway's external address is mapped.
      pass out on $ext_if inet from ! ($ext_if) to any nat-to ($ext_if)

      # NAT PROXYING
      # Map outgoing packets' source port to an assigned proxy port instead of
      # an arbitrary port.
      # In this case, proxy outgoing isakmp with port 500 on the gateway.
      pass out on $ext_if inet proto udp from any port = isakmp to any \
     nat-to ($ext_if) port 500

      # BINAT
      # Translate outgoing packets' source address (any protocol).
      # Translate incoming packets' destination address to an internal machine
      # (bidirectional).
      pass on $ext_if from 10.1.2.150 to any binat-to $ext_if

      # Translate packets arriving on $peer_if addressed to 172.22.16.0/20
      # to the corresponding address in 172.21.16.0/20 (bidirectional).
      pass on $peer_if from 172.21.16.0/20 to any binat-to 172.22.16.0/20

      # RDR
      # Translate incoming packets' destination addresses.
      # As an example, redirect a TCP and UDP port to an internal machine.
      pass in on $ext_if inet proto tcp from any to ($ext_if) port 8080 \
     rdr-to 10.1.2.151 port 22
      pass in on $ext_if inet proto udp from any to ($ext_if) port 8080 \
     rdr-to 10.1.2.151 port 53

      # RDR
      # Translate outgoing ftp control connections to send them to localhost
      # for proxying with [ftp-proxy(8)](https://man.freebsd.org/cgi/man.cgi?query=ftp-proxy&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) running on port 8021.
      pass in on $int_if proto tcp from any to any port 21 \
     rdr-to 127.0.0.1 port 8021

       In  this  example,  a  NAT  gateway is set up to translate internal ad-
       dresses using a pool of public addresses (192.0.2.16/28) and  to  redi-
       rect  incoming  web server connections to a group of web servers on the
       internal network.

      # NAT LOAD BALANCE
      # Translate outgoing packets' source addresses using an address pool.
      # A given source address is always translated to the same pool address by
      # using the source-hash keyword.
      pass out on $ext_if inet from any to any nat-to 192.0.2.16/28 source-hash

      # RDR ROUND ROBIN
      # Translate incoming web server connections to a group of web servers on
      # the internal network.
      pass in on $ext_if proto tcp from any to any port 80 \
     rdr-to { 10.1.2.155, 10.1.2.160, 10.1.2.161 } round-robin

[**COMPATIBILITY TRANSLATION EXAMPLES**](https://man.freebsd.org/cgi/man.cgi?query=pf.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#end)
       In the  example below, the  machine  sits  between  a fake  internal
       144.19.74.*  network, and a routable external IP of 204.92.77.100.  The
       _no_ _nat_ rule excludes protocol AH from being translated.

      # NAT
      no nat on $ext_if proto ah from 144.19.74.0/24 to any
      nat on $ext_if from 144.19.74.0/24 to any -> 204.92.77.100

       In the example below, packets bound for one specific server, as well as
       those generated by the sysadmins are not proxied; all other connections
       are.

      # RDR
      no rdr on $int_if proto { tcp, udp } from any to $server port 80
      no rdr on $int_if proto { tcp, udp } from $sysadmins to any port 80
      rdr on $int_if proto { tcp, udp } from any to any port 80 \
     -> 127.0.0.1 port 80

[**FILTER EXAMPLES**](https://man.freebsd.org/cgi/man.cgi?query=pf.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#end)
      # The external interface is kue0
      # (157.161.48.183, the only routable address)
      # and the private network is 10.0.0.0/8, for which we are doing NAT.

      # Reassemble incoming traffic
      set reassemble yes

      # use a macro for the interface name, so it can be changed easily
      ext_if = "kue0"

      # block and log everything by default
      block return log on $ext_if all

      # block anything coming from source we have no back routes for
      block in from no-route to any

      # block packets whose ingress interface does not match the one in
      # the route back to their source address
      block in from urpf-failed to any

      # block and log outgoing packets that do not have our address as source,
      # they are either spoofed or something is misconfigured (NAT disabled,
      # for instance), we want to be nice and do not send out garbage.
      block out log quick on $ext_if from ! 157.161.48.183 to any

      # silently drop broadcasts (cable modem noise)
      block in quick on $ext_if from any to 255.255.255.255

      # block and log incoming packets from reserved address space and invalid
      # addresses, they are either spoofed or misconfigured, we cannot reply to
      # them anyway (hence, no return-rst).
      block in log quick on $ext_if from { 10.0.0.0/8, 172.16.0.0/12, \
     192.168.0.0/16, 255.255.255.255/32 } to any

      # ICMP

      # pass out/in certain ICMP queries and keep state (ping)
      # state matching is done on host addresses and ICMP id (not type/code),
      # so replies (like 0/0 for 8/0) will match queries
      # ICMP error messages (which always refer to a TCP/UDP packet) are
      # handled by the TCP/UDP states
      pass on $ext_if inet proto icmp all icmp-type 8 code 0

      # UDP

      # pass out all UDP connections and keep state
      pass out on $ext_if proto udp all

      # pass in certain UDP connections and keep state (DNS)
      pass in on $ext_if proto udp from any to any port domain

      # TCP

      # pass out all TCP connections and modulate state
      pass out on $ext_if proto tcp all modulate state

      # pass in certain TCP connections and keep state (SSH, SMTP, DNS, IDENT)
      pass in on $ext_if proto tcp from any to any port { ssh, smtp, domain, \
     auth }

      # Do not allow Windows 9x SMTP connections since they are typically
      # a viral worm. Alternately we could limit these OSes to 1 connection each.
      block in on $ext_if proto tcp from any os {"Windows 95", "Windows 98"} \
     to any port smtp

      # IPv6
      # pass in/out all IPv6 traffic: note that we have to enable this in two
      # different ways, on both our physical interface and our tunnel
      pass quick on gif0 inet6
      pass quick on $ext_if proto ipv6

      # Packet Tagging

      # three interfaces: $int_if, $ext_if, and $wifi_if (wireless). NAT is
      # being done on $ext_if for all outgoing packets. tag packets in on
      # $int_if and pass those tagged packets out on $ext_if.  all other
      # outgoing packets (i.e., packets from the wireless network) are only
      # permitted to access port 80.

      pass in on $int_if from any to any tag INTNET
      pass in on $wifi_if from any to any

      block out on $ext_if from any to any
      pass out quick on $ext_if tagged INTNET
      pass out on $ext_if proto tcp from any to any port 80

      # tag incoming packets as they are redirected to [spamd(8)](https://man.freebsd.org/cgi/man.cgi?query=spamd&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly). use the tag
      # to pass those packets through the packet filter.

      rdr on $ext_if inet proto tcp from <spammers> to port smtp \
       tag SPAMD -> 127.0.0.1 port spamd

      block in on $ext_if
      pass in on $ext_if inet proto tcp tagged SPAMD

       In  the example  below, a router handling both address families trans-
       lates an internal IPv4 subnet to IPv6 using the well-known 64:ff9b::/96
       prefix:

    pass in on $v4_if inet af-to inet6 from ($v6_if) to 64:ff9b::/96

       Paired with the example above, the example below can be used on another
       router handling both address families to translate back to IPv4:

    pass in on $v6_if inet6 to 64:ff9b::/96 af-to inet from ($v4_if)

[**GRAMMAR**](https://man.freebsd.org/cgi/man.cgi?query=pf.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#end)
       Syntax for **pf.conf** in BNF:

       line       = ( option | ether-rule | pf-rule | nat-rule | binat-rule |
   rdr-rule | antispoof-rule | altq-rule | queue-rule |
   trans-anchors | anchor-rule | anchor-close | load-anchor |
   table-rule | include )

       option       = "set" ( [ "timeout" ( timeout | "{" timeout-list "}" ) ] |
   [ "ruleset-optimization" [ "none" | "basic" | "profile" ]] |
   [ "optimization" [ "default" | "normal" |
   "high-latency" | "satellite" |
   "aggressive" | "conservative" ] ]
   [ "limit" ( limit-item | "{" limit-list "}" ) ] |
   [ "loginterface" ( interface-name | "none" ) ] |
   [ "block-policy" ( "drop" | "return" ) ] |
   [ "state-policy" ( "if-bound" | "floating" ) ]
   [ "state-defaults" state-opts ]
   [ "require-order" ( "yes" | "no" ) ]
   [ "fingerprints" filename ] |
   [ "skip on" ifspec ] |
   [ "debug" ( "none" | "urgent" | "misc" | "loud" ) ]
   [ "keepcounters" ] )

       ether-rule     = "ether" etheraction [ ( "in" | "out" ) ]
   [ "quick" ] [ "on" ifspec ] [ "bridge-to" interface-name ]
   [ etherprotospec ] [ etherhosts ] [ "l3" hosts ]
   [ etherfilteropt-list ]

       pf-rule       = action [ ( "in" | "out" ) ]
   [ "log" [ "(" logopts ")"] ] [ "quick" ]
   [ "on" ifspec ] [ route ] [ af ] [ protospec ]
   [ hosts ] [ filteropt-list ]

       logopts       = logopt [ "," logopts ]
       logopt       = "all" | "matches" | "user" | "to" interface-name

       etherfilteropt-list = etherfilteropt-list etherfilteropt | etherfilteropt
       etherfilteropt = "tag" string | "tagged" string | "queue" ( string ) |
   "ridentifier" number | "label" string

       filteropt-list = filteropt-list filteropt | filteropt
       filteropt      = user | group | flags | icmp-type | icmp6-type | "tos" tos |
   "af-to" af "from" ( redirhost | "{" redirhost-list "}" )
   [ "to" ( redirhost | "{" redirhost-list "}" ) ] |
   ( "no" | "keep" | "modulate" | "synproxy" ) "state"
   [ "(" state-opts ")" ] |
   "fragment" | "no-df" | "min-ttl" number | "set-tos" tos |
   "max-mss" number | "random-id" | "reassemble tcp" |
   fragmentation | "allow-opts" |
   "label" string | "tag" string | [ "!" ] "tagged" string |
   "max-pkt-rate" number "/" seconds |
   "set prio" ( number | "(" number [ [ "," ] number ] ")" ) |
   "max-pkt-size" number |
   "queue" ( string | "(" string [ [ "," ] string ] ")" ) |
   "rtable" number | "probability" number"%" | "prio" number |
   "dnpipe" ( number | "(" number "," number ")" ) |
   "dnqueue" ( number | "(" number "," number ")" ) |
   "ridentifier" number |
   [ ! ] "received-on" ( interface-name | interface-group )

       nat-rule       = [ "no" ] "nat" [ "pass" [ "log" [ "(" logopts ")" ] ] ]
   [ "on" ifspec ] [ af ]
   [ protospec ] hosts [ "tag" string ] [ "tagged" string ]
   [ "->" ( redirhost | "{" redirhost-list "}" )
   [ portspec ] [ pooltype ] [ "static-port" ]
   [ "map-e-portset" number "/" number "/" number ] ]

       binat-rule     = [ "no" ] "binat" [ "pass" [ "log" [ "(" logopts ")" ] ] ]
   [ "on" interface-name ] [ af ]
   [ "proto" ( proto-name | proto-number ) ]
   "from" address [ "/" mask-bits ] "to" ipspec
   [ "tag" string ] [ "tagged" string ]
   [ "->" address [ "/" mask-bits ] ]

       rdr-rule       = [ "no" ] "rdr" [ "pass" [ "log" [ "(" logopts ")" ] ] ]
   [ "on" ifspec ] [ af ]
   [ protospec ] hosts [ "tag" string ] [ "tagged" string ]
   [ "->" ( redirhost | "{" redirhost-list "}" )
   [ portspec ] [ pooltype ] ]

       antispoof-rule = "antispoof" [ "log" ] [ "quick" ]
   "for" ifspec [ af ] [ "label" string ]
   [ "ridentifier" number ]

       table-rule     = "table" "<" string ">" [ tableopts-list ]
       tableopts-list = tableopts-list tableopts | tableopts
       tableopts      = "persist" | "const" | "counters" | "file" string |
   "{" [ tableaddr-list ] "}"
       tableaddr-list = tableaddr-list [ "," ] tableaddr-spec | tableaddr-spec
       tableaddr-spec = [ "!" ] tableaddr [ "/" mask-bits ]
       tableaddr      = hostname | ifspec | "self" |
   ipv4-dotted-quad | ipv6-coloned-hex

       altq-rule      = "altq on" interface-name queueopts-list
   "queue" subqueue
       queue-rule     = "queue" string [ "on" interface-name ] queueopts-list
   subqueue

       anchor-rule    = "anchor" [ string ] [ ( "in" | "out" ) ] [ "on" ifspec ]
   [ af ] [ protospec ] [ hosts ] [ filteropt-list ] [ "{" ]

       anchor-close   = "}"

       trans-anchors  = ( "nat-anchor" | "rdr-anchor" | "binat-anchor" ) string
   [ "on" ifspec ] [ af ] [ "proto" ] [ protospec ] [ hosts ]

       load-anchor    = "load anchor" string "from" filename

       queueopts-list = queueopts-list queueopts | queueopts
       queueopts      = [ "bandwidth" bandwidth-spec ] |
   [ "qlimit" number ] | [ "tbrsize" number ] |
   [ "priority" number ] | [ schedulers ]
       schedulers     = ( cbq-def | priq-def | hfsc-def )
       bandwidth-spec = "number" ( "b" | "Kb" | "Mb" | "Gb" | "%" )

       etheraction    = "pass" | "block"
       action       = "pass" | "match" | "block" [ return ] | [ "no" ] "scrub"
       return       = "drop" | "return" | "return-rst" [ "( ttl" number ")" ] |
   "return-icmp" [ "(" icmpcode [ [ "," ] icmp6code ] ")" ] |
   "return-icmp6" [ "(" icmp6code ")" ]
       icmpcode       = ( icmp-code-name | icmp-code-number )
       icmp6code      = ( icmp6-code-name | icmp6-code-number )

       ifspec       = ( [ "!" ] ( interface-name | interface-group ) ) |
   "{" interface-list "}"
       interface-list = [ "!" ] ( interface-name | interface-group )
   [ [ "," ] interface-list ]
       route       = ( "route-to" | "reply-to" | "dup-to" )
   ( routehost | "{" routehost-list "}" )
   [ pooltype ]
       af       = "inet" | "inet6"

       etherprotospec = "proto" ( proto-number | "{" etherproto-list "}" )
       etherproto-list = proto-number [ [ "," ] etherproto-list ]
       protospec      = "proto" ( proto-name | proto-number |
   "{" proto-list "}" )
       proto-list     = ( proto-name | proto-number ) [ [ "," ] proto-list ]

       etherhosts     = "from" macaddress "to" macaddress
       macaddress     = mac | mac "/" masklen | mac "&" mask

       hosts       = "all" |
   "from" ( "any" | "no-route" | "urpf-failed" | "self" | host |
   "{" host-list "}" ) [ port ] [ os ]
   "to"   ( "any" | "no-route" | "self" | host |
   "{" host-list "}" ) [ port ]

       ipspec       = "any" | host | "{" host-list "}"
       host       = [ "!" ] ( address [ "/" mask-bits ] | "<" string ">" )
       redirhost      = address [ "/" mask-bits ]
       routehost      = "(" interface-name address [ "/" mask-bits ] ")"
       address       = ( interface-name | interface-group |
   "(" ( interface-name | interface-group ) ")" |
   hostname | ipv4-dotted-quad | ipv6-coloned-hex )
       host-list      = host [ [ "," ] host-list ]
       redirhost-list = redirhost [ [ "," ] redirhost-list ]
       routehost-list = routehost [ [ "," ] routehost-list ]

       port       = "port" ( unary-op | binary-op | "{" op-list "}" )
       portspec       = "port" ( number | name ) [ ":" ( "*" | number | name ) ]
       os       = "os"  ( os-name | "{" os-list "}" )
       user       = "user" ( unary-op | binary-op | "{" op-list "}" )
       group       = "group" ( unary-op | binary-op | "{" op-list "}" )

       unary-op       = [ "=" | "!=" | "<" | "<=" | ">" | ">=" ]
   ( name | number )
       binary-op      = number ( "<>" | "><" | ":" ) number
       op-list       = ( unary-op | binary-op ) [ [ "," ] op-list ]

       os-name       = operating-system-name
       os-list       = os-name [ [ "," ] os-list ]

       flags       = "flags" ( [ flag-set ] "/"  flag-set | "any" )
       flag-set       = [ "F" ] [ "S" ] [ "R" ] [ "P" ] [ "A" ] [ "U" ] [ "E" ]
   [ "W" ]

       icmp-type      = "icmp-type" ( icmp-type-code | "{" icmp-list "}" )
       icmp6-type     = "icmp6-type" ( icmp-type-code | "{" icmp-list "}" )
       icmp-type-code = ( icmp-type-name | icmp-type-number )
   [ "code" ( icmp-code-name | icmp-code-number ) ]
       icmp-list      = icmp-type-code [ [ "," ] icmp-list ]

       tos       = ( "lowdelay" | "throughput" | "reliability" |
   [ "0x" ] number )

       state-opts     = state-opt [ [ "," ] state-opts ]
       state-opt      = ( "max" number | "no-sync" | timeout | "sloppy" |
   "source-track" [ ( "rule" | "global" ) ] |
   "max-src-nodes" number | "max-src-states" number |
   "max-src-conn" number |
   "max-src-conn-rate" number "/" number |
   "overload" "<" string ">" [ "flush" ] |
   "if-bound" | "floating" | "pflow" )

       fragmentation  = [ "fragment reassemble" ]

       timeout-list   = timeout [ [ "," ] timeout-list ]
       timeout       = ( "tcp.first" | "tcp.opening" | "tcp.established" |
   "tcp.closing" | "tcp.finwait" | "tcp.closed" |
   "sctp.first" | "sctp.opening" | "sctp.established" |
   "sctp.closing" | "sctp.closed" |
   "udp.first" | "udp.single" | "udp.multiple" |
   "icmp.first" | "icmp.error" |
   "other.first" | "other.single" | "other.multiple" |
   "frag" | "interval" | "src.track" |
   "adaptive.start" | "adaptive.end" ) number

       limit-list     = limit-item [ [ "," ] limit-list ]
       limit-item     = ( "states" | "frags" | "src-nodes" ) number

       pooltype       = ( "bitmask" | "random" |
   "source-hash" [ ( hex-key | string-key ) ] |
   "round-robin" ) [ sticky-address | prefer-ipv6-nexthop ]

       subqueue       = string | "{" queue-list "}"
       queue-list     = string [ [ "," ] string ]
       cbq-def       = "cbq" [ "(" cbq-opt [ [ "," ] cbq-opt ] ")" ]
       priq-def       = "priq" [ "(" priq-opt [ [ "," ] priq-opt ] ")" ]
       hfsc-def       = "hfsc" [ "(" hfsc-opt [ [ "," ] hfsc-opt ] ")" ]
       cbq-opt       = ( "default" | "borrow" | "red" | "ecn" | "rio" )
       priq-opt       = ( "default" | "red" | "ecn" | "rio" )
       hfsc-opt       = ( "default" | "red" | "ecn" | "rio" |
   linkshare-sc | realtime-sc | upperlimit-sc )
       linkshare-sc   = "linkshare" sc-spec
       realtime-sc    = "realtime" sc-spec
       upperlimit-sc  = "upperlimit" sc-spec
       sc-spec       = ( bandwidth-spec |
   "(" bandwidth-spec number bandwidth-spec ")" )
       include       = "include" filename

[**FILES**](https://man.freebsd.org/cgi/man.cgi?query=pf.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#end)
       _/etc/hosts_      Host name database.
       _/etc/pf.conf_    Default location of the ruleset file.  The file has  to
         be created manually as it is not installed with a stan-
         dard installation.
       _/etc/pf.os_      Default location of OS fingerprints.
       _/etc/protocols_  Protocol name database.
       _/etc/services_   Service name database.

[**SEE ALSO**](https://man.freebsd.org/cgi/man.cgi?query=pf.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#end)
       [_altq_(4)](https://man.freebsd.org/cgi/man.cgi?query=altq&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly),  [_carp_(4)](https://man.freebsd.org/cgi/man.cgi?query=carp&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly),  [_icmp_(4)](https://man.freebsd.org/cgi/man.cgi?query=icmp&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly),  [_icmp6_(4)](https://man.freebsd.org/cgi/man.cgi?query=icmp6&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly), [_ip_(4)](https://man.freebsd.org/cgi/man.cgi?query=ip&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly), [_ip6_(4)](https://man.freebsd.org/cgi/man.cgi?query=ip6&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly), [_pf_(4)](https://man.freebsd.org/cgi/man.cgi?query=pf&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly), [_pflow_(4)](https://man.freebsd.org/cgi/man.cgi?query=pflow&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly),
       [_pfsync_(4)](https://man.freebsd.org/cgi/man.cgi?query=pfsync&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly), [_sctp_(4)](https://man.freebsd.org/cgi/man.cgi?query=sctp&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly), [_tcp_(4)](https://man.freebsd.org/cgi/man.cgi?query=tcp&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly), [_udp_(4)](https://man.freebsd.org/cgi/man.cgi?query=udp&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly), [_hosts_(5)](https://man.freebsd.org/cgi/man.cgi?query=hosts&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly),  [_pf.os_(5)](https://man.freebsd.org/cgi/man.cgi?query=pf.os&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly),  [_protocols_(5)](https://man.freebsd.org/cgi/man.cgi?query=protocols&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly),
       [_services_(5)](https://man.freebsd.org/cgi/man.cgi?query=services&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly), [_ftp-proxy_(8)](https://man.freebsd.org/cgi/man.cgi?query=ftp-proxy&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly), [_pfctl_(8)](https://man.freebsd.org/cgi/man.cgi?query=pfctl&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly), [_pflogd_(8)](https://man.freebsd.org/cgi/man.cgi?query=pflogd&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly)

[**HISTORY**](https://man.freebsd.org/cgi/man.cgi?query=pf.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#end)
       The **pf.conf** file format first appeared in OpenBSD 3.0.

FreeBSD 15.0   October 7, 2025       _PF.CONF_(5)
[* * *](https://man.freebsd.org/cgi/man.cgi?query=pf.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly)
[](https://man.freebsd.org/cgi/man.cgi?query=pf.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly)[NAME](https://man.freebsd.org/cgi/man.cgi?query=pf.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#NAME) | [DESCRIPTION](https://man.freebsd.org/cgi/man.cgi?query=pf.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#DESCRIPTION) | [STATEMENT ORDER](https://man.freebsd.org/cgi/man.cgi?query=pf.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#STATEMENT_ORDER) | [MACROS](https://man.freebsd.org/cgi/man.cgi?query=pf.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#MACROS) | [TABLES](https://man.freebsd.org/cgi/man.cgi?query=pf.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#TABLES) | [OPTIONS](https://man.freebsd.org/cgi/man.cgi?query=pf.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#OPTIONS) | [ETHERNET FILTERING](https://man.freebsd.org/cgi/man.cgi?query=pf.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#ETHERNET_FILTERING) | [TRAFFIC NORMALIZATION](https://man.freebsd.org/cgi/man.cgi?query=pf.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#TRAFFIC%09NORMALIZATION) | [QUEUEING with ALTQ](https://man.freebsd.org/cgi/man.cgi?query=pf.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#QUEUEING_with_ALTQ) | [QUEUEING with dummynet](https://man.freebsd.org/cgi/man.cgi?query=pf.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#QUEUEING_with_dummynet) | [TRANSLATION](https://man.freebsd.org/cgi/man.cgi?query=pf.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#TRANSLATION) | [PACKET FILTERING](https://man.freebsd.org/cgi/man.cgi?query=pf.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#PACKET_FILTERING) | [ROUTING](https://man.freebsd.org/cgi/man.cgi?query=pf.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#ROUTING) | [POOL OPTIONS](https://man.freebsd.org/cgi/man.cgi?query=pf.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#POOL_OPTIONS) | [STATE MODULATION](https://man.freebsd.org/cgi/man.cgi?query=pf.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#STATE_MODULATION) | [SYN PROXY](https://man.freebsd.org/cgi/man.cgi?query=pf.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#SYN_PROXY) | [STATEFUL TRACKING OPTIONS](https://man.freebsd.org/cgi/man.cgi?query=pf.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#STATEFUL_TRACKING_OPTIONS) | [OPERATING SYSTEM FINGERPRINTING](https://man.freebsd.org/cgi/man.cgi?query=pf.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#OPERATING_SYSTEM_FINGERPRINTING) | [BLOCKING SPOOFED TRAFFIC](https://man.freebsd.org/cgi/man.cgi?query=pf.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#BLOCKING_SPOOFED_TRAFFIC) | [FRAGMENT HANDLING](https://man.freebsd.org/cgi/man.cgi?query=pf.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#FRAGMENT_HANDLING) | [ANCHORS](https://man.freebsd.org/cgi/man.cgi?query=pf.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#ANCHORS) | [SCTP CONSIDERATIONS](https://man.freebsd.org/cgi/man.cgi?query=pf.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#SCTP_CONSIDERATIONS) | [TRANSLATION EXAMPLES](https://man.freebsd.org/cgi/man.cgi?query=pf.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#TRANSLATION_EXAMPLES) | [COMPATIBILITY TRANSLATION EXAMPLES](https://man.freebsd.org/cgi/man.cgi?query=pf.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#COMPATIBILITY_TRANSLATION_EXAMPLES) | [FILTER EXAMPLES](https://man.freebsd.org/cgi/man.cgi?query=pf.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#FILTER_EXAMPLES) | [GRAMMAR](https://man.freebsd.org/cgi/man.cgi?query=pf.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#GRAMMAR) | [FILES](https://man.freebsd.org/cgi/man.cgi?query=pf.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#FILES) | [SEE ALSO](https://man.freebsd.org/cgi/man.cgi?query=pf.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#SEE_ALSO) | [HISTORY](https://man.freebsd.org/cgi/man.cgi?query=pf.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#HISTORY)

Want to link to this manual page? Use this URL:

<[https://man.freebsd.org/cgi/man.cgi?query=pf.conf&sektion=5&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly](https://man.freebsd.org/cgi/man.cgi?query=pf.conf&sektion=5&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly)>

* * *
