# Source: https://man.freebsd.org/cgi/man.cgi?query=relayd.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly

Title: relayd.conf(5)

URL Source: https://man.freebsd.org/cgi/man.cgi?query=relayd.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly

Markdown Content:
FreeBSD Manual Pages
--------------------

* * *

_RELAYD.CONF_(5)        File Formats Manual  _RELAYD.CONF_(5)

[**NAME**](https://man.freebsd.org/cgi/man.cgi?query=relayd.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#end)
       relayd.conf -- relay daemon configuration file

[**DESCRIPTION**](https://man.freebsd.org/cgi/man.cgi?query=relayd.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#end)
       **relayd.conf** is the configuration file for the relay daemon, [_relayd_(8)](https://man.freebsd.org/cgi/man.cgi?query=relayd&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly).

       **relayd.conf** is divided into the following main sections:

       **Macros**
      User-defined variables may be defined and used later, simplifying
      the configuration file.

       **Global** **Configuration**
      Global  settings for [_relayd_(8)](https://man.freebsd.org/cgi/man.cgi?query=relayd&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly).  Do note that the config file al-
      lows global settings to be added after  defining  tables  in  the
      config  file, but those tables will use the built-in defaults in-
      stead of the global settings below them.

       **Tables**
      Table definitions describe a list of hosts, in a similar  fashion
      to  [_pf_(4)](https://man.freebsd.org/cgi/man.cgi?query=pf&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) tables. They are used for relay and redirection target
      selection with the described options and health checking  on  the
      host they contain.

       **Redirections**
      Redirections  are translated  to [_pf_(4)](https://man.freebsd.org/cgi/man.cgi?query=pf&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) rdr-to rules for stateful
      forwarding to a target host from a health-checked table on  layer
      3.

       **Relays**
      Relays  allow application layer load balancing, TLS acceleration,
      and general purpose TCP proxying on layer 7.

       **Protocols**
      Protocols are predefined settings and filter rules for relays.

       Within the sections, a host _address_ can be specified by IPv4  address,
       IPv6 address, interface name, interface group, or DNS hostname. If the
       address is an interface name, [_relayd_(8)](https://man.freebsd.org/cgi/man.cgi?query=relayd&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) will look up the first IPv4 ad-
       dress  and  any other IPv4 and IPv6 addresses of the specified network
       interface.  A _port_ can be specified by number or name.  The  port  name
       to number mappings are found in the file _/etc/services_; see [_services_(5)](https://man.freebsd.org/cgi/man.cgi?query=services&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly)
       for details.

       The  current line can be extended over multiple lines using a backslash
       (`\').  Comments can be put anywhere in the  file  using  a  hash  mark
       (`#'), and extend to the end of the current line.  Care should be taken
       when commenting out multi-line text: the comment is effective until the
       end of the entire block.

       Argument  names not beginning with a letter, digit, or underscore must
       be quoted.

       Additional configuration files can be included with  the  **include**  key-
       word, for example:

      include "/usr/local/etc/relayd.conf.local"

[**MACROS**](https://man.freebsd.org/cgi/man.cgi?query=relayd.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#end)
       Macros  can  be defined that will later be expanded in context.  Macro
       names must start with a letter, digit, or underscore, and  may  contain
       any  of those  characters.  Macro names may not be reserved words (for
       example, **table**, **relay**, or **timeout**).  Macros  are  not  expanded inside
       quotes.

       For example:

      www1="10.0.0.1"
      www2="10.0.0.2"
      table <webhosts> {
       $www1
       $www2
      }

[**GLOBAL CONFIGURATION**](https://man.freebsd.org/cgi/man.cgi?query=relayd.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#end)
       Here are the settings that can be set globally:

       **agentx** [**context** _context_] [**path** _path_]
        Export [_relayd_(8)](https://man.freebsd.org/cgi/man.cgi?query=relayd&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) metrics via an agentx compatible (snmp) daemon
        by  connecting to _path_. Metrics can be found under the relayd-
        MIBObjects subtree (enterprises.30155.3).  If _path_ is  omitted,
        it  will  default to _/var/agentx/master_.  _Context_ is the SNMPv3
        context and can usually be omitted.

       **interval** _number_
        Set the interval in seconds at which the hosts will be checked.
        The default interval is 10 seconds.

       **log** (**state** **changes**|**host** **checks**)
        Log host checks: Either log only the **state** **changes** of hosts  or
        log  all  **host**  **checks**  that were run, even if the state didn't
        change. The host state can be "up" (the health check completed
        successfully), "down" (the host is down or  didn't  match  the
        check  criteria), or "unknown" (the host is disabled or has not
        been checked yet).

       **log** **connection** [**errors**]
        When using relays, log all  TCP connections.   Optionally  log
        only **connection** **errors**.

       **prefork** _number_
        When  using  relays,  run  the specified number of processes to
        handle relayed connections.  This increases the performance and
        prevents delays when connecting to a relay.  [_relayd_(8)](https://man.freebsd.org/cgi/man.cgi?query=relayd&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly)  runs  3
        relay  processes  by  default and every process will handle all
        configured relays.

       **socket** "_path_"
        Create a   control    socket  at    _path_.  By    default
        _/var/run/relayd.sock_ is used.

       **timeout** _number_
        Set the global timeout in milliseconds for checks.  This can be
        overridden  by the timeout value in the table definitions.  The
        default timeout is 200 milliseconds and it must not exceed  the
        global  interval.   The default  value is optimized for checks
        within the same collision domain - use a higher timeout,  such
        as 1000 milliseconds, for checks of hosts in other subnets.  If
        this  option is to be set, it should be placed before overrides
        in tables.

[**TABLES**](https://man.freebsd.org/cgi/man.cgi?query=relayd.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#end)
       Tables are used to group a set of hosts as the target for  redirections
       or  relays; they will be mapped to a [_pf_(4)](https://man.freebsd.org/cgi/man.cgi?query=pf&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) table for redirections.  Ta-
       bles may be defined with the following attribute:

       **disable** Start the table disabled - no hosts will be  checked  in  this
  table. The table can be later enabled through [_relayctl_(8)](https://man.freebsd.org/cgi/man.cgi?query=relayctl&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly).

       Each  table  must contain at least one host _address_; multiple hosts are
       separated by newline, comma, or whitespace.  Host entries  may  be  de-
       fined with the following attributes:

       **ip** **ttl** _number_
       Change the default time-to-live value in the IP headers for host
       checks.

       **parent** _number_
       The optional parent option inherits the state from a parent host
       with  the  specified  identifier.  The check will be skipped for
       this host and copied from the parent host.  This can be used  to
       prevent  multiple checks on hosts with multiple IP addresses for
       the same service.  The host  identifiers are  sequentially  as-
       signed  to the configured hosts starting with 1; it can be shown
       with the [_relayctl_(8)](https://man.freebsd.org/cgi/man.cgi?query=relayctl&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) **show** **summary** commands.

       **priority** _number_
       Change the route priority used when  adding  a  route.   If  not
       specified, the kernel will set a priority of 8 (RTP_STATIC).  In
       ordinary use, a fallback route should be added statically with a
       very high (e.g. 52) priority.  Unused in all other modes.

       **retry** _number_
       The  optional  retry  option  adds  a  tolerance for failed host
       checks; the check will be retried for _number_ more  times before
       setting  the host state to down. If this table is used by a re-
       lay, it will also specify the number  of retries  for  outgoing
       connection attempts.

       For example:

      table <service> { 192.168.1.1, 192.168.1.2, 192.168.2.3 }
      table <fallback> disable { 10.1.5.1 retry 2 }

      redirect "www" {
       listen on www.example.com port 80
       forward to <service> check http "/" code 200
       forward to <fallback> check http "/" code 200
      }

       Tables are used by **forward** **to** directives in redirections or relays with
       a  set  of general options, health-checking rules, and timings; see the
       "REDIRECTIONS" and "RELAYS" sections for  more  information  about  the
       forward context.  Table specific configuration directives are described
       below.  Multiple options can be appended to **forward** **to** directives, sep-
       arated by whitespaces.

       The following options will configure the health-checking method for the
       table, and is mandatory for redirections:

       **check** **http** _path_ [**host** _hostname_] **code** _number_
        For each host in the table, verify that retrieving the URL _path_
        gives  the  HTTP return code _number_.  If _hostname_ is specified,
        it is used as the "Host:" header to query a  specific  hostname
        at the target host.  To validate the HTTP return code, use this
        shell command:

       $ echo -n "HEAD <path> HTTP/1.0\r\n\r\n" | \
        nc <host> <port> | head -n1

        This prints the status header including the actual return code:

       HTTP/1.1 200 OK

       **check** **https** _path_ [**host** _hostname_] **code** _number_
        This has the same effect as above but wraps the HTTP request in
        TLS.

       **check** **http** _path_ [**host** _hostname_] **digest** _string_
        For each host in the table, verify that retrieving the URL _path_
        produces  non-binary  content  whose message digest matches the
        defined string. The algorithm used is determined by the string
        length of the _digest_ argument, either SHA1 (40  characters)  or
        MD5  (32  characters).  If _hostname_ is specified, it is used as
        the "Host:" header to query a specific hostname at  the target
        host.   The digest does not take the HTTP headers into account.
        Do not specify a binary object (such as a graphic) as the  tar-
        get of the request, as **relayd.conf** expects the data returned to
        be a string.  To compute the digest, use this simple command:

       $ ftp -o - [http://host](http://host/)[:port]/path | sha1

        This  gives  a digest that can be used as-is in a digest state-
        ment:

       a9993e36476816aba3e25717850c26c9cd0d89d

       **check** **https** _path_ [**host** _hostname_] **digest** _string_
        This has the same effect as above but wraps the HTTP request in
        TLS.

       **check** **icmp**
        Ping hosts in this table to determine whether they  are up  or
        not.  This method will automatically use ICMP or ICMPV6 depend-
        ing on the address family of each host.

       **check** **script** _path_
        Execute an external program to check the host state.  The pro-
        gram will be executed for each host by specifying the  hostname
        on the command line:

       /usr/local/bin/checkload.pl front-www1.private.example.com

        [_relayd_(8)](https://man.freebsd.org/cgi/man.cgi?query=relayd&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly)  expects  a positive return value on success and zero
        on failure.  Note that the script will  be  executed  with  the
        privileges  of  the "_relayd" user and terminated after _timeout_
        milliseconds.

       **check** **send** _data_ **expect** _pattern_ [**tls**]
        For each host in the table, a TCP connection is established  on
        the  port  specified, then _data_ is sent.  Incoming data is then
        read and is expected to match against _pattern_ using shell glob-
        bing rules.  If _data_ is an empty string or **nothing** then nothing
        is sent on the connection and data is immediately  read.   This
        can  be useful with protocols that output a banner like SMTP,
        NNTP, and FTP.  If the **tls** keyword is present, the  transaction
        will occur in a TLS tunnel.

       **check** **binary** **send** _data_ **expect** _data_ [**tls**]
        For  each host in the table, a TCP connection is established on
        the port specified, then the **send** _data_ is converted into binary
        and sent.  Incoming (binary) data is then read and is  expected
        to  match  against a binary conversion of the **expect** _data_ using
        [_memcmp_(3)](https://man.freebsd.org/cgi/man.cgi?query=memcmp&sektion=3&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly).  _data_ must be populated with a string containing  an
        even  number of hexadecimal single-byte characters and must not
        be empty.  This can be useful with  binary  protocols  such  as
        LDAP  and SNMP. If the **tls** keyword is present, the transaction
        will occur in a TLS tunnel.

       **check** **tcp**
        Use a simple TCP connect to check that hosts are up.

       **check** **tls**
        Perform a complete TLS handshake with each host to check  their
        availability.

       The following general table options are available:

       **interval** _number_
        Override  the  global  interval and specify one for this table.
        It must be a multiple of the global interval.

       **timeout** _number_
        Set the timeout in milliseconds for each host that  is  checked
        using  TCP  as  the  transport.  This will override the global
        timeout, which is 200 milliseconds by default.

       The following options will set the scheduling  algorithm  to  select  a
       host from the specified table:

       **mode** **hash** [_key_]
        Balances the outgoing connections across the active hosts based
        on the _key_, IP address and port of the relay.  Additional input
        can  be fed  into  the hash by looking at HTTP headers and GET
        variables; see the "PROTOCOLS" section  below. This  mode  is
        only supported by relays.

       **mode** **least-states**
        Forward each  outgoing connection to the active host with the
        least active [_pf_(4)](https://man.freebsd.org/cgi/man.cgi?query=pf&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) states.  This  mode  is  only  supported  by
        redirections.

       **mode** **loadbalance** [_key_]
        Balances the outgoing connections across the active hosts based
        on the _key_, the source IP address of the client, and the IP ad-
        dress  and  port  of the relay. This mode is only supported by
        relays.

       **mode** **random**
        Distributes the outgoing connections randomly through  all  ac-
        tive hosts.  This mode is supported by redirections and relays.

       **mode** **roundrobin**
        Distributes the outgoing connections using a round-robin sched-
        uler  through  all  active hosts.  This is the default mode and
        will be used if no option has been  specified. This  mode  is
        supported by redirections and relays.

       **mode** **source-hash** [_key_]
        Balances the outgoing connections across the active hosts based
        on  the _key_ and the source IP address of the client.  This mode
        is supported by redirections and relays.

       The optional _key_ argument can be specified for the  **hash**,  **loadbalance**,
       and **source-hash** modes as either a hex value with a leading `0x' or as a
       string. If omitted, [_relayd_(8)](https://man.freebsd.org/cgi/man.cgi?query=relayd&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) generates a random key when the configu-
       ration is loaded.

[**REDIRECTIONS**](https://man.freebsd.org/cgi/man.cgi?query=relayd.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#end)
       Redirections represent a [_pf_(4)](https://man.freebsd.org/cgi/man.cgi?query=pf&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) rdr-to rule.  They are used for stateful
       redirections  to the hosts in the specified tables.  [_pf_(4)](https://man.freebsd.org/cgi/man.cgi?query=pf&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) rewrites the
       target IP addresses and ports of the incoming connections, operating on
       layer 3.  The configuration directives that are valid in  the  **redirect**
       context are described below:

       **disable**
        The redirection is initially disabled.  It can be later enabled
        through [_relayctl_(8)](https://man.freebsd.org/cgi/man.cgi?query=relayctl&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly).

       **forward** **to** <_table_> [**port** _number_] _options_ _..._
        Specify the tables of target hosts to be used; see the "TABLES"
        section above for information about table options.  If the **port**
        option  is not specified, the first port from the **listen** **on** di-
        rective will be used.  This directive can be specified twice  -
        the  second entry will be used as the backup table if all hosts
        in the main table are down.  At least one entry for  the  main
        table is mandatory.

       **listen** **on** _address_ [ip-proto] **port** _port_ [**interface** _name_]
        Specify an  _address_ and a _port_ to listen on.  [_pf_(4)](https://man.freebsd.org/cgi/man.cgi?query=pf&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) will redi-
        rect incoming connections for the specified target to the hosts
        in the main or backup table.  The _port_ argument can  optionally
        specify a  port  range instead of a single port; the format is
        _min-port_:_max-port_.  The optional argument _ip-proto_ can be  used
        to  specify an IP protocol like **tcp** or **udp**; it defaults to **tcp**.
        The rule can be optionally  restricted  to  a  given  interface
        name.

       [**match**] **pftag** _name_
        Automatically tag packets passing through the [_pf_(4)](https://man.freebsd.org/cgi/man.cgi?query=pf&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) rdr-to rule
        with the name supplied. This allows simpler filter rules.  The
        optional **match** keyword will change the default rule action from
        `pass  in  quick'  to `match in' to allow further evaluation in
        the pf ruleset using the **tagged** _name_ rule option.

       **route** **to** <_table_> [**port** _number_] _options_ _..._
        Like the **forward** **to** directive, but directly routes the  packets
        to the target host without modifying the target address using a
        [_pf_(4)](https://man.freebsd.org/cgi/man.cgi?query=pf&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly)  route-to rule. This  can  be  used for "direct server
        return" to force the target host to  respond  via  a  different
        gateway.   Note that hosts have to accept sessions for the same
        address as the gateway, which is typically done by  configuring
        a loopback interface on the host with this address.

       **session** **timeout** _seconds_
        Specify the inactivity timeout in seconds for established redi-
        rections.   The default  timeout  is 600 seconds (10 minutes).
        The maximum is 2147483647 seconds (68 years).

       **sticky-address**
        This has the same effect as specifying  sticky-address  for  an
        rdr-to  rule  in [_pf.conf_(5)](https://man.freebsd.org/cgi/man.cgi?query=pf.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly).  It will ensure that multiple con-
        nections from the same source are mapped to the same  redirec-
        tion address.

[**RELAYS**](https://man.freebsd.org/cgi/man.cgi?query=relayd.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#end)
       Relays  will  forward traffic between a client and a target server.  In
       contrast to redirections and IP forwarding in the network stack, a  re-
       lay  will  accept incoming connections from remote clients as a server,
       open an outgoing connection to a target host, and forward  any  traffic
       between the target host and the remote client, operating on layer 7.  A
       relay is also called an application layer gateway or layer 7 proxy.

       The main purpose of a relay is to provide advanced load balancing func-
       tionality  based  on  specified protocol characteristics, such as HTTP
       headers, to provide TLS acceleration and to allow basic handling of the
       underlying application protocol.

       The **relay** configuration directives are described below:

       **disable**
        Start the relay but immediately close any accepted connections.

       [**transparent**] **forward** [**with** **tls**] **to** _address_ [**port** _port_] _options_ _..._
        Specify the address and port of the target host to connect  to.
        If  the **port** option is not specified, the port from the **listen**
        **on** directive will be used.  Use the **transparent** keyword to  en-
        able  fully-transparent mode; the source address of the client
        will be retained in this case.

        The **with** **tls** directive enables client-side TLS mode to  connect
        to the remote host.  Verification of server certificates can be
        enabled by setting the **ca** **file** option in the protocol section.

        The following options may be specified for forward directives:

        **inet**    If  the requested  destination is  an IPv6  address,
         [_relayd_(8)](https://man.freebsd.org/cgi/man.cgi?query=relayd&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) will forward the connection to  an  IPv4  ad-
         dress  which  is determined by the last 4 octets of the
         original IPv6 destination.  For example, if the origi-
         nal  IPv6     destination       address     is
         2001:db8:7395:ffff::a01:101, the session is relayed  to
         the IPv4 address 10.1.1.1 (a01:101).

        **inet6** _address-prefix_
         If  the requested  destination is  an IPv4  address,
         [_relayd_(8)](https://man.freebsd.org/cgi/man.cgi?query=relayd&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) will forward the connection to  an  IPv6  ad-
         dress  which is determined by setting the last 4 octets
         of the specified IPv6 _address-prefix_ to the 4 octets of
         the original IPv4 destination. For  example,  if  the
         original  IPv4  destination address is 10.1.1.1 and the
         specified address prefix is  2001:db8:7395:ffff::,  the
         session   is relayed    to  the IPv6   address
         2001:db8:7395:ffff::a01:101.

        **retry** _number_
         The optional host **retry** option will be used as a toler-
         ance for failed host connections; the  connection  will
         be retried for _number_ more times.

       **forward** **to** <_table_> [**port** _port_] _options_ _..._
        Like  the  previous  directive, but connect to a host from the
        specified table; see the "TABLES" section above for information
        about table options.  This directive can be specified  multiple
        times  - subsequent entries will be used as the backup table if
        all hosts in the previous table are down.  At least  one  entry
        for  the  main  table is mandatory.  As above, use the **with** **tls**
        directive to enable client-side TLS mode when connecting to the
        remote host.

       **forward** **to** **destination** _options_ _..._
        When redirecting connections with a rdr-to rule in  [_pf.conf_(5)](https://man.freebsd.org/cgi/man.cgi?query=pf.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly)
        to  a relay listening on localhost, this directive will look up
        the real destination address of the intended target  host,  al-
        lowing the relay to be run as a transparent proxy.  If an addi-
        tional  **forward** **to** directive to a specified address or table is
        present, it will be used as a backup if the NAT lookup  failed.
        As  above, use the **with** **tls** directive to enable client-side TLS
        mode when connecting to the remote host.

       **listen** **on** _address_ **port** _port_ [**tls**]
        Specify the address and port for the relay to listen  on.   The
        relay  will  accept  incoming  connections to the specified ad-
        dress.  If the **tls** keyword is present, the  relay  will accept
        connections using the encrypted TLS protocol.

       **protocol** _name_
        Use  the  specified  protocol  definition  for  the relay.  The
        generic TCP protocol options will be used by default;  see  the
        "PROTOCOLS" section below.

       **session** **timeout** _seconds_
        Specify the  inactivity  timeout  in seconds for accepted ses-
        sions.  The default timeout is 600 seconds (10  minutes).   The
        maximum is 2147483647 seconds (68 years).

[**TLS RELAYS**](https://man.freebsd.org/cgi/man.cgi?query=relayd.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#end)
       In  addition to plain TCP, [_relayd_(8)](https://man.freebsd.org/cgi/man.cgi?query=relayd&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) supports the Transport Layer Secu-
       rity (TLS) cryptographic protocol for authenticated and encrypted  re-
       lays.  [_relayd_(8)](https://man.freebsd.org/cgi/man.cgi?query=relayd&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) can operate as a TLS client or server to offer a vari-
       ety of options for different use cases related to TLS.

       **TLS** **client**
        When configuring the relay **forward** statements with the **with** **tls**
        directive,  [_relayd_(8)](https://man.freebsd.org/cgi/man.cgi?query=relayd&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) will enable client-side TLS to connect to
        the remote host.  This is commonly used for TLS tunneling  and
        transparent  encapsulation  of  plain TCP connections.  See the
        **forward** **to** description in the "RELAYS"  section for  more  de-
        tails.

       **TLS** **server**
        When specifying the **tls** keyword in the relay **listen** statements,
        [_relayd_(8)](https://man.freebsd.org/cgi/man.cgi?query=relayd&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) will accept connections from clients as a TLS server.
        This  mode is also known as "TLS acceleration". See the **listen**
        **on** description in the "RELAYS" section for more details.

       **TLS** **client** **and** **server**
        When combining both modes, TLS server and client, [_relayd_(8)](https://man.freebsd.org/cgi/man.cgi?query=relayd&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) can
        filter TLS connections as a man-in-the-middle. This  combined
        mode  is  also  called "TLS inspection".  The configuration re-
        quires additional X.509 certificate settings; see  the  **ca**  **key**
        description in the "PROTOCOLS" section for more details.

       When  configured  for  "TLS inspection" mode, [_relayd_(8)](https://man.freebsd.org/cgi/man.cgi?query=relayd&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) will listen for
       incoming connections which have been diverted to the  local  socket  by
       PF.   Before accepting and negotiating the incoming TLS connection as a
       server, it will look up the original destination  address  on  the  di-
       verted  socket, and pre-connect to the target server as a TLS client to
       obtain the remote TLS certificate.  It will update  or  patch  the  ob-
       tained  TLS  certificate  by replacing the included public key with its
       local server key because it doesn't have the private key of the remote
       server certificate.  It also updates the X.509 issuer name to the local
       CA  subject name and signs the certificate with its local CA key.  This
       way it keeps all the other X.509 attributes that are already present in
       the server certificate, including the "green bar"  extended  validation
       attributes.   Now  it  finally  accepts the TLS connection from the di-
       verted client using the updated certificate and continues to handle the
       connection and to connect to the remote server.

[**PROTOCOLS**](https://man.freebsd.org/cgi/man.cgi?query=relayd.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#end)
       Protocols are templates defining settings and rules for relays.   They
       allow  setting generic TCP options, TLS settings, and rules for the se-
       lected application layer protocol.

       The protocol directive is available for a number of different  applica-
       tion layer protocols.  There is no generic handler for UDP-based proto-
       cols  because  it  is  a stateless datagram-based protocol which has to
       look into the application layer protocol to find any possible state in-
       formation.

       **dns** **protocol**
        (UDP) Domain Name System (DNS) protocol.  The requested IDs  in
        the  DNS header will be used to match the state.  [_relayd_(8)](https://man.freebsd.org/cgi/man.cgi?query=relayd&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) re-
        places these IDs with random  values  to  compensate  for  pre-
        dictable values generated by some hosts.

       **http** **protocol**
        Handle the HyperText Transfer Protocol (HTTP, or "HTTPS" if en-
        capsulated in a TLS tunnel).

       [**tcp**] **protocol**
        Generic handler for TCP-based protocols.  This is the default.

       The available configuration directives are described below:

       (**block**|**pass**|**match**) [_rule_]
        Specify one or more rules to filter connections based on their
        network or application layer headers; see  the  "FILTER RULES"
        section for more details.

       **return** **error** [_option_]
        Return an error response to the client if an internal operation
        or  the forward  connection to the client failed.  By default,
        the connection will be silently dropped.  The  effect  of  this
        option  depends on the protocol: HTTP will send an error header
        and page to the client before closing  the  connection.  Addi-
        tional valid options are:

        **style** _string_
         Specify a  Cascading  Style Sheet (CSS) to be used for
         the returned HTTP error pages, for example:

        body { background: #a00000; color: white; }

       **tcp** _option_
        Enable or disable the specified TCP/IP options; see [_tcp_(4)](https://man.freebsd.org/cgi/man.cgi?query=tcp&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly)  and
        [_ip_(4)](https://man.freebsd.org/cgi/man.cgi?query=ip&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly)  for  more  information about the options.  Valid options
        are:

        **backlog** _number_
         Set the maximum length the queue of pending connections
         may grow to.  The backlog option is 10 by  default,  is
         limited  to  512  and  capped  by  the **kern.somaxconn**
         [_sysctl_(8)](https://man.freebsd.org/cgi/man.cgi?query=sysctl&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) variable.

        **ip** **minttl** _number_
         This option for the underlying  IP  connection  may  be
         used to discard packets with a TTL lower than the spec-
         ified  value.  This can be used to implement the Gener-
         alized TTL Security Mechanism (GTSM) according  to  RFC
         5082.

        **ip** **ttl** _number_
         Change  the  default time-to-live value in the IP head-
         ers.

        **nodelay**
         Enable the TCP  NODELAY option for  this  connection.
         This is recommended to avoid delays in the relayed data
         stream, e.g.  for  SSH connections.  The default is **no**
         **nodelay**.

        **no** **splice**
         Disable socket splicing for  zero-copy  data  transfer.
         The default is to enable socket splicing.

        **sack**    Use  selective  acknowledgements  for  this connection.
         The default is **no** **sack**.

        **socket** **buffer** _number_
         Set the socket-level buffer size for input  and output
         for  this  connection.  This will affect the TCP window
         size.

       **tls** _option_
        Set the TLS options and session settings.  This is only used if
        TLS is enabled in the relay.  Valid options are:

        **ca** **cert** _path_
         Specify a CA certificate for TLS inspection.  For  more
         information, see the **ca** **key** option below.

        **ca** **file** _path_
         This option enables CA verification in TLS client mode.
         The  daemon  will  load the CA (Certificate Authority)
         certificates from the  specified  path  to  verify  the
         server  certificates.   OpenBSD provides  a default CA
         bundle in _/etc/ssl/cert.pem_.

        **ca** **key** _path_ **password** _password_
         Specify a CA key for TLS inspection.  The _password_  ar-
         gument  will specify the password to decrypt the CA key
         (typically an RSA key). This option  will  enable  TLS
         inspection if the following conditions are true:

        **•**  TLS  server mode is enabled by the **listen** di-
     rective: **listen** **on** **...** **tls**.
        **•**  TLS client mode and divert  lookups  are  en-
     abled by the **forward** directive: **forward** **with**
     **tls** **to** **destination**.
        **•**  The **ca** **cert** option is specified.
        **•**  The **ca** **key** option is specified.

        **ciphers** _string_
         Set the string defining the TLS cipher suite.   If  not
         specified, the default value `HIGH:!aNULL' will be used
         (strong crypto cipher suites without anonymous DH).
         See the CIPHERS section of [_openssl_(1)](https://man.freebsd.org/cgi/man.cgi?query=openssl&sektion=1&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly)  for  information
         about TLS cipher suites and preference lists.

        **client-renegotiation**
         Allow  client-initiated renegotiation.  To mitigate a
         potential    DoS    risk,    the    default    is    **no**
         **client-renegotiation**.

        **ecdhe** _curves_
         Specify a  comma  separated list of elliptic curves to
         use for ECDHE cipher suites, in order  of  preference.
         The  special  value  of "default" will use the default
         curves; see [_tls\_config\_set\_ecdhecurves_(3)](https://man.freebsd.org/cgi/man.cgi?query=tls_config_set_ecdhecurves&sektion=3&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly)  for  further
         details.

        **edh** [**params** (**none**|**auto**|**legacy**)]
         Enable EDH-based cipher suites with Perfect Forward Se-
         crecy  (PFS)  for  older  clients  that do not support
         ECDHE.  In **auto** mode, the key size of the ephemeral key
         is automatically selected based on the size of the pri-
         vate key used for signing.  In **legacy** mode, a 1024  bit
         ephemeral  key  is used.  If **params** is omitted, **auto** is
         used.  The default is **no** **edh**.

        **keypair** _name_
         The relay will attempt to look  up  a  private  key  in
         _/etc/ssl/private/name:port.key_ and a public certificate
         in  _/etc/ssl/name:port.crt_, where _port_ is the specified
         port that the relay listens on. If these files are not
         present,  the  relay   will   continue to   look   in
         _/etc/ssl/private/name.key_  and _/etc/ssl/name.crt_.  This
         option can be specified multiple times for  TLS Server
         Name  Indication.   If not specified, a keypair will be
         loaded using the specified IP address of the  relay  as
         _name_.  See [_ssl_(8)](https://man.freebsd.org/cgi/man.cgi?query=ssl&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) for details about TLS server certifi-
         cates.

         An  optional  OCSP  staple file will be used during TLS
         handshakes with this server if it is found  as  a  non-
         empty  file   in  _/etc/ssl/name:port.ocsp_    or
         _/etc/ssl/name.ocsp_.  The file should contain a DER-for-
         mat OCSP response retrieved from an OCSP server for the
         certificate  in use,  and   can   be   created  using
         [_ocspcheck_(8)](https://man.freebsd.org/cgi/man.cgi?query=ocspcheck&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly).

        **no** **cipher-server-preference**
         Prefer the client's cipher list over the server's pref-
         erences when choosing a cipher for the connection.  The
         default is to prefer the server's cipher list.

        **session** **tickets**
         Enable  TLS session tickets.  [_relayd_(8)](https://man.freebsd.org/cgi/man.cgi?query=relayd&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) supports state-
         less TLS session tickets (RFC 5077)  to implement  TLS
         session resumption  for connections not using TLSv1.3.
         The default is to disable session tickets.

        **no** **tlsv1.3**
         Disable the TLSv1.3 protocol.  The default is to enable
         TLSv1.3.

        **no** **tlsv1.2**
         Disable the TLSv1.2 protocol.  The default is to enable
         TLSv1.2.

        **sslv3**   Is deprecated and does nothing.

        **tlsv1**   Enable all TLSv1 protocols.  This is an alias that cur-
         rently includes **tlsv1.2**, and **tlsv1.3**.  The  default  is
         **no** **tlsv1**.

        **tlsv1.0**
         Is deprecated and does nothing.

        **tlsv1.1**
         Is deprecated and does nothing.

       **http** _option_
        Set  the  HTTP options and session settings.  This is only used
        if HTTP is enabled in the relay.  Valid options are:

        **headerlen** _number_
         Set the maximum size of all HTTP headers in bytes.  The
         default value is 8192 and it is limited to a maximum of
         131072.

        **websockets**
         Allow connection upgrade to  websocket  protocol.   The
         default is **no** **websockets**.

[**FILTER RULES**](https://man.freebsd.org/cgi/man.cgi?query=relayd.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#end)
       Relays have the ability to filter connections based on their network or
       application  layer  headers.  Filter rules apply options to connections
       based on the specified filter parameters.

       For each connection that is processed by a relay, the filter rules  are
       evaluated in sequential order, from first to last.  For **block** and **pass**,
       the last matching rule decides what action is taken; if no rule matches
       the connection, the default action is to establish the connection with-
       out  any  additional action.  For **match**, rules are evaluated every time
       they match; the pass/block state of a connection remains unchanged.

       The filter action may be one of the following:

       **block**   The connection is blocked.  If a **block** rule matches a new  con-
        nection attempt,  it will not be established.  **block** rules can
        also trigger for existing connections after evaluating applica-
        tion layer parameters; any connection of the relay session will
        be instantly dropped.

       **match**   The connection is matched.  This action does not alter the con-
        nection state, but allows additional parameters to the  connec-
        tion.

       **pass**    The  connection is  passed; [_relayd_(8)](https://man.freebsd.org/cgi/man.cgi?query=relayd&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) will continue to process
        the relay session normally.

       These filter parameters can be used in the rules:

       **request** or **response**
        A  relay  session  always  consists  of two  connections:  the
        **request**,  a  client initiating a new connection to a server via
        the relay, and the **response**, the server accepting  the  connec-
        tion.  Depending on the protocol, an established session can be
        purely  request/response-based  (like HTTP), exchange data in a
        bidirectional way (like arbitrary TCP sessions), or  just  con-
        tain a single datagram and an optional response (like UDP-based
        protocols).  But the client always _requests_ to communicate with
        a remote peer; the server.

       **quick**   If a connection is matched by a rule with the **quick** option set,
        the  rule  is  considered  to be the last matching rule and any
        further evaluation is skipped.

       **inet** or **inet6**
        Only match connections with the specified address  family,  ei-
        ther of type IPv4 or IPv6.

       **from** _address_[**/**_prefix_]
        This  rule  only  matches  for  connections  from the specified
        source.

       **to** _address_[**/**_prefix_]
        This rule only matches for connections to the specified desti-
        nation. The destination is the address the client was connect-
        ing to, typically the relay's listen address in non-transparent
        mode, not the address of the forwarded backend connection.

       **forward** **to** <_table_>
        Forward the  request to a server in the specified table.  With
        this  option,  requests can  be  passed  to  specific  backend
        servers.    A  corresponding  **forward**  **to**  declaration  in  the
        "RELAYS" section is required.

       **label** _string_
        The label will be printed as part of the error message  if  the
        **return** **error** option is set and may contain HTML tags, for exam-
        ple:

       block request url digest 5c1e03f58f8ce0b457474ffb371fd1ef \
        label "<a href='[http://example.com/adv.pl?id=7359](http://example.com/adv.pl?id=7359)'>\
        Advisory provided by example.com</a>"

       **no** _parameter_
        Reset  a sticky parameter that was previously set by a matching
        rule.  The _parameter_ is a keyword that can be either  **label**  or
        **tag**.

       **tag** _string_
        Add  a  "sticky"  tag to connections matching this filter rule.
        Tags can be used to filter the connection by further rules  us-
        ing  the  **tagged**  option.  Only one tag is assigned per connec-
        tion; the tag will be replaced if  the  connection  is  already
        tagged.

       **tagged** _string_
        Match  the  connection if it is already tagged with a given tag
        by a previous rule.

       The following parameters are available when using the **http** protocol:

       **method** _name_
        Match the HTTP request method.  The method is specified by _name_
        and can be either  **ACL**, **BASELINE-CONTROL**,  **CHECKIN**,  **CHECKOUT**,
        **CONNECT**,   **COPY**,   **DELETE**,   **GET**,  **HEAD**,  **LABEL**,  **LOCK**, **MERGE**,
        **MKACTIVITY**, **MKCOL**, **MKREDIRECTREF**, **MKWORKSPACE**,  **MOVE**,  **OPTIONS**,
        **ORDERPATCH**,  **PATCH**,  **POST**,  **PROPFIND**,  **PROPPATCH**,  **PUT**, **REPORT**,
        **SEARCH**, **TRACE**, **UNCHECKOUT**, **UNLOCK**,  **UPDATE**,  **UPDATEREDIRECTREF**,
        or **VERSION-CONTROL**.

       _type_ _option_ [[**digest**] (_key_|**file** _path_) [**value** _value_]]
        Match  a  specified  HTTP header entity and an optional **key** and
        **value**.  An **option** can be specified to modify the matched entity
        or to trigger an event. The entity is extracted from the  HTTP
        request or  response  header and can be either of _type_ **cookie**,
        **header**, **path**, **query**, or **url**.

        Instead of a single _key_, multiple keys can  be  loaded  from  a
        **file**  specified by _path_ that contains one key per line.  Lines
        will be stripped at the first whitespace or  newline  character
        and  any  empty lines or lines beginning with a hash mark (`#')
        will be ignored.

        If the **digest** keyword is specified, compare the message digest
        of  the key against the defined string.  The algorithm used is
        determined by the string length of  the _key_  argument, either
        SHA1  (40  characters)  or MD5 (32 characters). To compute the
        digest, for example for a **url**, use this simple command:

       $ echo -n "example.com/path/?args" | sha1

       [_type_] may be one of:

       **cookie** _option_ [_key_ [**value** _value_]]
        Look up the entity as a value in the Cookie header.  This  type
        is only available with the direction **request**.

       **header** _option_ [_key_ [**value** _value_]]
        Look  up  the  entity in the application protocol headers, like
        HTTP headers in **http** mode.

       **path** _option_ [_key_ [**value** _value_]]
        Look up the entity as a value in the URL path  when  using  the
        **http**  protocol. This type is only available with the direction
        **request**.  The _key_ will match the  path  of  the requested  URL
        without the  hostname  and  query and the value will match the
        complete query, for example:

       block path "/index.html"
       block path "/cgi-bin/t.cgi" value "foo=bar*"

       **path** **strip** _number_
        Strip _number_ path components from the beginning of the path  of
        the  requested  URL when using the **http** protocol.  This type is
        only available with the direction **request**.

       **query** _option_ [_key_ [**value** _value_]]
        Look up the entity as a query variable in the  URL  when  using
        the **http** protocol.  This type is only available with the direc-
        tion **request**, for example:

       # Will match /cgi-bin/example.pl?foo=bar&ok=yes
       pass request query "foo" value "bar"

       **url** _option_ [[**digest**] _key_ [**value** _value_]]
        Look up the entity as a URL suffix/prefix expression consisting
        of  a  canonicalized hostname without port or suffix and a path
        name or prefix when using the **http** protocol.  This type is only
        available with the direction **request**, for example:

       block url "example.com/index.html"
       block url "example.com/test.cgi?val=1"

        [_relayd_(8)](https://man.freebsd.org/cgi/man.cgi?query=relayd&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) will match the full URL and different possible  suf-
        fix/prefix combinations by stripping subdomains and path compo-
        nents (up to 5 levels), and the query string.  For example, the
        following   lookups   will   be  done for   [http://www.exam-](http://www.exam-/)
        ple.com:81/1/2/3/4/5.html?query=yes:

       www.example.com/1/2/3/4/5.html?query=yes
       www.example.com/1/2/3/4/5.html
       www.example.com/
       www.example.com/1/
       www.example.com/1/2/
       www.example.com/1/2/3/
       example.com/1/2/3/4/5.html?query=yes
       example.com/1/2/3/4/5.html
       example.com/
       example.com/1/
       example.com/1/2/
       example.com/1/2/3/

       [_option_] may be one of:

       **append**  Append the specified _value_ to a protocol entity with  the  se-
        lected _key_ name.  If it does not exist, it will be created with
        the new value.

        The value string may contain predefined macros that will be ex-
        panded at runtime:

       **$HOST**    The Host header's value of the relay.
       **$REMOTE_ADDR**  The IP address of the connected client.
       **$REMOTE_PORT**  The  TCP  source  port  of the  connected
       client.
       **$SERVER_ADDR**  The configured IP address of the relay.
       **$SERVER_PORT**  The configured TCP server port of  the  re-
       lay.
       **$SERVER_NAME**  The server software name of [_relayd_(8)](https://man.freebsd.org/cgi/man.cgi?query=relayd&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly).
       **$TIMEOUT**    The configured  session timeout of the re-
       lay.

       **hash**    Feed the _value_ of the selected entity into the  load  balancing
        hash  to  select the target host.  See the **table** keyword in the
        "RELAYS" section above.

       **log**     Log the _key_ name and the _value_ of the entity.

       **remove**  Remove the entity with the selected _key_ name.

       **set**     Like the **append** directive above, but change the contents of the
        specified entity.  If _key_ does not exist  in  the  request,  it
        will be created with the new _value_.

        The _value_ string may contain predefined macros that will be ex-
        panded at runtime, as detailed for the **append** directive above.

[**FILES**](https://man.freebsd.org/cgi/man.cgi?query=relayd.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#end)
       _/usr/local/etc/relayd.conf_   [_relayd_(8)](https://man.freebsd.org/cgi/man.cgi?query=relayd&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) configuration file.

       _/etc/examples/relayd.conf_   Example configuration file.

       _/etc/services_     Service name database.

       _/usr/local/etc/ssl/address.crt_
       _/usr/local/etc/ssl/address:port.crt_
       _/usr/local/etc/ssl/private/address.key_
       _/usr/local/etc/ssl/private/address:port.key_
       Location  of  the  relay  TLS
       server  certificates,  where
       _address_  is the configured IP
       address and _port_ is the  con-
       figured  port number of the
       relay.

       _/usr/local/etc/ssl/cert.pem_   Default location  of  the  CA
       bundle  that can be used with
       [_relayd_(8)](https://man.freebsd.org/cgi/man.cgi?query=relayd&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly).

[**EXAMPLES**](https://man.freebsd.org/cgi/man.cgi?query=relayd.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#end)
       This configuration file would create a redirection service "www"  which
       load balances four hosts and falls back to one host containing a "sorry
       page":

      www1=front-www1.private.example.com
      www2=front-www2.private.example.com
      www3=front-www3.private.example.com
      www4=front-www4.private.example.com

      interval 5

      table <phphosts> { $www1, $www2, $www3, $www4 }
      table <sorryhost> disable { sorryhost.private.example.com }

      redirect "www" {
       listen on www.example.com port 8080 interface trunk0
       listen on www6.example.com port 80 interface trunk0

       pftag REDIRECTED

       forward to <phphosts> port 8080 timeout 300 \
        check http "/" digest "630aa3c2f..."
       forward to <sorryhost> port 8080 timeout 300 check icmp
      }

       It  is possible to specify multiple listen directives with different IP
       protocols in a single redirection configuration:

      redirect "dns" {
       listen on dns.example.com tcp port 53
       listen on dns.example.com udp port 53

       forward to <dnshosts> port 53 check tcp
      }

       The following configuration would add a relay to forward  secure  HTTPS
       connections  to a  pool  of HTTP webservers using the **loadbalance** mode
       (TLS acceleration and layer 7 load balancing).  The HTTP protocol defi-
       nition will add two HTTP headers containing address information of  the
       client and the server, set the "Keep-Alive" header value to the config-
       ured  session timeout, and include the "sessid" variable in the hash to
       calculate the target host:

      http protocol "https" {
       match header set "X-Forwarded-For" \
        value "$REMOTE_ADDR"
       match header set "X-Forwarded-By" \
        value "$SERVER_ADDR:$SERVER_PORT"
       match header set "Keep-Alive" value "$TIMEOUT"

       match query hash "sessid"

       pass
       block path "/cgi-bin/index.cgi" value "*command=*"

       tls { no tlsv1.0, ciphers "HIGH" }
      }

      relay "tlsaccel" {
       listen on www.example.com port 443 tls
       protocol "https"
       forward to <phphosts> port 8080 mode loadbalance check tcp
      }

       The second relay example will accept incoming connections to port  2222
       and  forward  them to a remote SSH server.  The TCP **nodelay** option will
       allow a "smooth" SSH session without delays between keystrokes or  dis-
       played output on the terminal:

      protocol "myssh" {
       tcp { nodelay, socket buffer 65536 }
      }

      relay "sshforward" {
       listen on www.example.com port 2222
       protocol "myssh"
       forward to shell.example.com port 22
      }

       The  following  relay  example  will  configure "TLS inspection" as de-
       scribed in the "TLS RELAYS" section.  To start, first  generate a  new
       local CA key and certificate:

      # openssl req -x509 -days 365 -newkey rsa:2048 \
       -keyout /usr/local/etc/ssl/private/ca.key \
       -out /usr/local/etc/etc/ssl/ca.crt

       A  TLS server key and self-signed cert for 127.0.0.1 are also required;
       see **listen** **on** in the "RELAYS" section for more details  about  certifi-
       cate  locations.   Configure  the  packet filter with a matching divert
       rule in [_pf.conf_(5)](https://man.freebsd.org/cgi/man.cgi?query=pf.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly):

      # Divert incoming HTTPS traffic to relayd
      pass in on vlan1 inet proto tcp to port 443 \
       divert-to localhost port 8443

       And finally configure the TLS inspection in **relayd.conf**:

      http protocol httpfilter {
       return error

       pass
       match label "Prohibited!"
       block url "social.network.example.com/"

       # New configuration directives for TLS Interception
       tls ca key "/etc/ssl/private/ca.key" password "password123"
       tls ca cert "/etc/ssl/ca.crt"
      }

      relay tlsinspect {
       listen on 127.0.0.1 port 8443 tls
       protocol httpfilter
       forward with tls to destination
      }

       The next simple router configuration example can be used to run redun-
       dant, health-checked WAN links:

      table <gateways> { $gw1 ip ttl 1, $gw2 ip ttl 1 }
      router "uplinks" {
       route 0.0.0.0/0
       forward to <gateways> check icmp
      }

[**SEE ALSO**](https://man.freebsd.org/cgi/man.cgi?query=relayd.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#end)
       [_ocspcheck_(8)](https://man.freebsd.org/cgi/man.cgi?query=ocspcheck&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly), [_relayctl_(8)](https://man.freebsd.org/cgi/man.cgi?query=relayctl&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly), [_relayd_(8)](https://man.freebsd.org/cgi/man.cgi?query=relayd&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly), [_ssl_(8)](https://man.freebsd.org/cgi/man.cgi?query=ssl&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly)

[**HISTORY**](https://man.freebsd.org/cgi/man.cgi?query=relayd.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#end)
       The  **relayd.conf**  file format, formerly known as **hoststated.conf**, first
       appeared in OpenBSD 4.1.  It was renamed to **relayd.conf** in OpenBSD 4.3.

[**AUTHORS**](https://man.freebsd.org/cgi/man.cgi?query=relayd.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#end)
       The  [_relayd_(8)](https://man.freebsd.org/cgi/man.cgi?query=relayd&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) program   was written   by   Pierre-Yves   Ritschard
       <_pyr@openbsd.org_> and Reyk Floeter <_reyk@openbsd.org_>.

[**CAVEATS**](https://man.freebsd.org/cgi/man.cgi?query=relayd.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#end)
       [_relayd_(8)](https://man.freebsd.org/cgi/man.cgi?query=relayd&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly)  verification of TLS server certificates is based on a static
       CA bundle and [_relayd_(8)](https://man.freebsd.org/cgi/man.cgi?query=relayd&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) currently does not  support  CRLs  (Certificate
       Revocation Lists).

FreeBSD 15.0         October 29, 2023   _RELAYD.CONF_(5)
[* * *](https://man.freebsd.org/cgi/man.cgi?query=relayd.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly)
[](https://man.freebsd.org/cgi/man.cgi?query=relayd.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly)[NAME](https://man.freebsd.org/cgi/man.cgi?query=relayd.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#NAME) | [DESCRIPTION](https://man.freebsd.org/cgi/man.cgi?query=relayd.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#DESCRIPTION) | [MACROS](https://man.freebsd.org/cgi/man.cgi?query=relayd.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#MACROS) | [GLOBAL CONFIGURATION](https://man.freebsd.org/cgi/man.cgi?query=relayd.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#GLOBAL_CONFIGURATION) | [TABLES](https://man.freebsd.org/cgi/man.cgi?query=relayd.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#TABLES) | [REDIRECTIONS](https://man.freebsd.org/cgi/man.cgi?query=relayd.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#REDIRECTIONS) | [RELAYS](https://man.freebsd.org/cgi/man.cgi?query=relayd.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#RELAYS) | [TLS RELAYS](https://man.freebsd.org/cgi/man.cgi?query=relayd.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#TLS_RELAYS) | [PROTOCOLS](https://man.freebsd.org/cgi/man.cgi?query=relayd.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#PROTOCOLS) | [FILTER RULES](https://man.freebsd.org/cgi/man.cgi?query=relayd.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#FILTER_RULES) | [FILES](https://man.freebsd.org/cgi/man.cgi?query=relayd.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#FILES) | [EXAMPLES](https://man.freebsd.org/cgi/man.cgi?query=relayd.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#EXAMPLES) | [SEE ALSO](https://man.freebsd.org/cgi/man.cgi?query=relayd.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#SEE_ALSO) | [HISTORY](https://man.freebsd.org/cgi/man.cgi?query=relayd.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#HISTORY) | [AUTHORS](https://man.freebsd.org/cgi/man.cgi?query=relayd.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#AUTHORS) | [CAVEATS](https://man.freebsd.org/cgi/man.cgi?query=relayd.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#CAVEATS)

Want to link to this manual page? Use this URL:

<[https://man.freebsd.org/cgi/man.cgi?query=relayd.conf&sektion=5&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly](https://man.freebsd.org/cgi/man.cgi?query=relayd.conf&sektion=5&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly)>

* * *
