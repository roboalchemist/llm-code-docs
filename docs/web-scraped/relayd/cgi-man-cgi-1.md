# Source: https://man.freebsd.org/cgi/man.cgi?query=pf&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly

Title: pf(4)

URL Source: https://man.freebsd.org/cgi/man.cgi?query=pf&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly

Markdown Content:
FreeBSD Manual Pages
--------------------

* * *

_PF_(4)       Kernel Interfaces Manual    _PF_(4)

[**NAME**](https://man.freebsd.org/cgi/man.cgi?query=pf&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#end)
       pf -- packet filter

[**SYNOPSIS**](https://man.freebsd.org/cgi/man.cgi?query=pf&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#end)
       **device** **pf**
       **options** **PF_DEFAULT_TO_DROP**

       In [_rc.conf_(5)](https://man.freebsd.org/cgi/man.cgi?query=rc.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly):
       **pf_enable="YES"**

       In [_loader.conf_(5)](https://man.freebsd.org/cgi/man.cgi?query=loader.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly):
       **net.pf.states_hashsize**
       **net.pf.source_nodes_hashsize**
       **net.pf.rule_tag_hashsize**
       **net.pf.udpendpoint_hashsize**
       **net.pf.default_to_drop**

       In [_sysctl.conf_(5)](https://man.freebsd.org/cgi/man.cgi?query=sysctl.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly):
       **net.pf.request_maxcount**
       **net.pf.filter_local**

[**DESCRIPTION**](https://man.freebsd.org/cgi/man.cgi?query=pf&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#end)
       Packet  filtering takes place in the kernel.  A pseudo-device, _/dev/pf_,
       allows userland processes to control the behavior of the packet filter
       through an  [_ioctl_(2)](https://man.freebsd.org/cgi/man.cgi?query=ioctl&sektion=2&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) interface.  There are commands to enable and dis-
       able the filter, load rulesets, add  and  remove  individual  rules  or
       state  table  entries, and retrieve statistics. The most commonly used
       functions are covered by [_pfctl_(8)](https://man.freebsd.org/cgi/man.cgi?query=pfctl&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly).

       Manipulations like loading a ruleset that involve more  than  a single
       [_ioctl_(2)](https://man.freebsd.org/cgi/man.cgi?query=ioctl&sektion=2&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) call require a so-called _ticket_, which prevents the occurrence
       of multiple concurrent manipulations.

       Fields of [_ioctl_(2)](https://man.freebsd.org/cgi/man.cgi?query=ioctl&sektion=2&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) parameter structures that refer to packet data (like
       addresses and ports) are generally expected in network byte-order.

       Rules and address tables are contained in so-called _anchors_.  When ser-
       vicing  an [_ioctl_(2)](https://man.freebsd.org/cgi/man.cgi?query=ioctl&sektion=2&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) request, if the anchor field of the argument struc-
       ture is empty, the kernel will use the default anchor (i.e.,  the  main
       ruleset)  in  operations.   Anchors  are  specified  by name and may be
       nested, with components separated by `/'  characters,  similar  to  how
       file  system  hierarchies are laid out. The final component of the an-
       chor path is the anchor under which operations will be performed.

[**SYSCTL VARIABLES**](https://man.freebsd.org/cgi/man.cgi?query=pf&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#end)
       The following variables can be entered at the [_loader_(8)](https://man.freebsd.org/cgi/man.cgi?query=loader&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) prompt, set  in
       [_loader.conf_(5)](https://man.freebsd.org/cgi/man.cgi?query=loader.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly), [_sysctl.conf_(5)](https://man.freebsd.org/cgi/man.cgi?query=sysctl.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly), or changed at runtime with [_sysctl_(8)](https://man.freebsd.org/cgi/man.cgi?query=sysctl&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly):

       _net.pf.filter\_local_
        This tells **pf** to also filter on the loopback output hook.  This
        is  typically used to allow redirect rules to adjust the source
        address.

       _net.pf.request\_maxcount_
        The maximum number of items in a single ioctl call.

[**LOADER TUNABLES**](https://man.freebsd.org/cgi/man.cgi?query=pf&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#end)
       The following tunables can be entered at the [_loader_(8)](https://man.freebsd.org/cgi/man.cgi?query=loader&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) prompt,  or  set
       in [_loader.conf_(5)](https://man.freebsd.org/cgi/man.cgi?query=loader.conf&sektion=5&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly):

       _net.pf.states\_hashsize_
        Size  of  hash table that stores states.  Should be power of 2.
        Default value is 131072.

       _net.pf.source\_nodes\_hashsize_
        Size of hash table that stores source nodes.  Should  be  power
        of 2.  Default value is 32768.

       _net.pf.rule\_tag\_hashsize_
        Size of the hash table that stores tags.

       _net.pf.udpendpoint\_hashsize_
        Size of hash table that store UDP endpoint mappings.  Should be
        power of 2.  Default value is 32768.

       _net.pf.default\_to\_drop_
        This  value  overrides  **options** **PF_DEFAULT_TO_DROP** from kernel
        configuration file.

       _net.pf.filter\_local_
        This tells **pf** to also filter on the loopback output hook.  This
        is typically used to allow redirect rules to adjust the source
        address.

       _net.pf.request\_maxcount_
        The maximum number of items in a single ioctl call.

       Read  only  [_sysctl_(8)](https://man.freebsd.org/cgi/man.cgi?query=sysctl&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) variables with matching names are provided to ob-
       tain current values at runtime.

[**KERNEL OPTIONS**](https://man.freebsd.org/cgi/man.cgi?query=pf&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#end)
       The following options in the kernel configuration file are  related  to
       **pf** operation:

       PF_DEFAULT_TO_DROP  Change default policy to drop by default

[**IOCTL INTERFACE**](https://man.freebsd.org/cgi/man.cgi?query=pf&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#end)
       **pf**   supports   the  following  [_ioctl_(2)](https://man.freebsd.org/cgi/man.cgi?query=ioctl&sektion=2&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly)  commands,  available  through
       <_net/pfvar.h_>:

       DIOCSTART
        Start the packet filter.

       DIOCSTOP
        Stop the packet filter.

       DIOCSTARTALTQ
        Start the ALTQ bandwidth control system (see [_altq_(9)](https://man.freebsd.org/cgi/man.cgi?query=altq&sektion=9&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly)).

       DIOCSTOPALTQ
        Stop the ALTQ bandwidth control system.

       DIOCBEGINADDRS _struct_ _pfioc\_pooladdr_ _*pp_

        struct pfioc_pooladdr {
         u_int32_t        action;
         u_int32_t        ticket;
         u_int32_t        nr;
         u_int32_t        r_num;
         u_int8_t         r_action;
         u_int8_t         r_last;
         u_int8_t         af;
         char         anchor[MAXPATHLEN];
         struct pf_pooladdr      addr;
        };

        Clear the buffer address pool and get a _ticket_  for  subsequent
        DIOCADDADDR, DIOCADDRULE, and DIOCCHANGERULE calls.

       DIOCADDADDR _struct_ _pfioc\_pooladdr_ _*pp_

        Add the pool address _addr_ to the buffer address pool to be used
        in the following DIOCADDRULE or DIOCCHANGERULE call.  All other
        members of the structure are ignored.

       DIOCADDRULE _struct_ _pfioc\_rule_ _*pr_

        struct pfioc_rule {
         u_int32_t       action;
         u_int32_t       ticket;
         u_int32_t       pool_ticket;
         u_int32_t       nr;
         char        anchor[MAXPATHLEN];
         char        anchor_call[MAXPATHLEN];
         struct pf_rule  rule;
        };

        Add  _rule_  at  the  end of the inactive ruleset.  This call re-
        quires a _ticket_ obtained through a  preceding  DIOCXBEGIN  call
        and  a  _pool\_ticket_  obtained  through  a  DIOCBEGINADDRS call.
        DIOCADDADDR must also be called if any pool addresses  are  re-
        quired. The optional _anchor_ name indicates the anchor in which
        to append the rule.  _nr_ and _action_ are ignored.

       DIOCADDALTQ _struct_ _pfioc\_altq_ _*pa_
        Add an ALTQ discipline or queue.

        struct pfioc_altq {
         u_int32_t       action;
         u_int32_t       ticket;
         u_int32_t       nr;
         struct pf_altq  altq;
        };

       DIOCGETRULES _struct_ _pfioc\_rule_ _*pr_
        Get a _ticket_ for subsequent DIOCGETRULE calls and the number _nr_
        of rules in the active ruleset.

       DIOCGETRULE _struct_ _pfioc\_rule_ _*pr_
        Get a _rule_ by its number _nr_ using the _ticket_ obtained through a
        preceding   DIOCGETRULES   call.    If _action_  is   set   to
        PF_GET_CLR_CNTR, the per-rule statistics on the requested  rule
        are cleared.

       DIOCGETADDRS _struct_ _pfioc\_pooladdr_ _*pp_
        Get a _ticket_ for subsequent DIOCGETADDR calls and the number _nr_
        of  pool  addresses in the rule specified with _r\_action_, _r\_num_,
        and _anchor_.

       DIOCGETADDR _struct_ _pfioc\_pooladdr_ _*pp_
        Get the pool address _addr_ by its number _nr_ from the rule speci-
        fied with _r\_action_, _r\_num_, and _anchor_ using the _ticket_ obtained
        through a preceding DIOCGETADDRS call.

       DIOCGETALTQS _struct_ _pfioc\_altq_ _*pa_
        Get a _ticket_ for subsequent DIOCGETALTQ calls and the number _nr_
        of queues in the active list.

       DIOCGETALTQ _struct_ _pfioc\_altq_ _*pa_
        Get the queueing discipline _altq_ by its number _nr_  using  the
        _ticket_ obtained through a preceding DIOCGETALTQS call.

       DIOCGETQSTATS _struct_ _pfioc\_qstats_ _*pq_
        Get the statistics on a queue.

        struct pfioc_qstats {
         u_int32_t ticket;
         u_int32_t nr;
         void        *buf;
         int  nbytes;
         u_int8_t  scheduler;
        };

        This  call  fills in a pointer to the buffer of statistics _buf_,
        of length _nbytes_, for the queue specified by _nr_.

       DIOCGETRULESETS _struct_ _pfioc\_ruleset_ _*pr_

        struct pfioc_ruleset {
         u_int32_t nr;
         char  path[MAXPATHLEN];
         char  name[PF_ANCHOR_NAME_SIZE];
        };

        Get the number _nr_ of rulesets (i.e., anchors) directly attached
        to  the anchor named  by   _path_   for  use   in   subsequent
        DIOCGETRULESET  calls. Nested anchors, since they are not di-
        rectly attached to the given  anchor,  will  not  be  included.
        This  ioctl  returns  ENOENT if the parent anchor given at _path_
        does not exist.

       DIOCGETRULESET _struct_ _pfioc\_ruleset_ _*pr_
        Get a ruleset (i.e., an anchor) _name_ by its number _nr_ from  the
        given  anchor _path_, the maximum number of which can be obtained
        from a preceding  DIOCGETRULESETS  call.   This ioctl  returns
        ENOENT  if  the parent anchor given by _path_ does not exist or
        EBUSY if the index passed in by _nr_ is greater than  the number
        of anchors.

       DIOCADDSTATE _struct_ _pfioc\_state_ _*ps_
        Add a state entry.

        struct pfioc_state {
         struct pfsync_state     state;
        };

       DIOCGETSTATENV _struct_ _pfioc\_nv_ _*nv_
        Extract the entry identified by the _id_ and _creatorid_ fields of
        the _state_ nvlist from the state table.

       DIOCKILLSTATESNV _struct_ _pfioc\_nv_ _nv_
        Remove matching entries from the state table.  This  ioctl  re-
        turns the number of killed states in _killed_.

        nvlist pf_state_cmp {
         number         id;
         number         creatorid;
         number         direction;
        };

        nvlist pf_kill {
         nvlist pf_state_cmp     cmp;
         number         af;
         number         proto;
         nvlist pf_rule_addr     src;
         nvlist pf_rule_addr     dst;
         string         ifname[IFNAMSIZ];
         string         label[PF_RULE_LABEL_SIZE];
        };

       DIOCCLRSTATESNV _struct_ _pfioc\_nv_ _nv_
        Clear  all states.  It works like DIOCKILLSTATESNV, but ignores
        the _af_, _proto_, _src_, and _dst_ fields of the _pf\_kill_ nvlist.

       DIOCSETSTATUSIF _struct_ _pfioc\_if_ _*pi_
        Specify the interface for which statistics are accumulated.

        struct pfioc_if {
         char  ifname[IFNAMSIZ];
        };

       DIOCGETSTATUS _struct_ _pf\_status_ _*s_
        Get the internal packet filter statistics.

        struct pf_status {
         u_int64_t       counters[PFRES_MAX];
         u_int64_t       lcounters[LCNT_MAX];
         u_int64_t       fcounters[FCNT_MAX];
         u_int64_t       scounters[SCNT_MAX];
         u_int64_t       pcounters[2][2][3];
         u_int64_t       bcounters[2][2];
         u_int32_t       running;
         u_int32_t       states;
         u_int32_t       src_nodes;
         u_int32_t       since;
         u_int32_t       debug;
         u_int32_t       hostid;
         char        ifname[IFNAMSIZ];
         u_int8_t        pf_chksum[MD5_DIGEST_LENGTH];
        };

       DIOCCLRSTATUS
        Clear the internal packet filter statistics.

       DIOCNATLOOK _struct_ _pfioc\_natlook_ _*pnl_
        Look up a state table entry by source and destination addresses
        and ports.

        struct pfioc_natlook {
         struct pf_addr saddr;
         struct pf_addr daddr;
         struct pf_addr rsaddr;
         struct pf_addr rdaddr;
         u_int16_t sport;
         u_int16_t dport;
         u_int16_t rsport;
         u_int16_t rdport;
         sa_family_t af;
         u_int8_t  proto;
         u_int8_t  direction;
        };

       DIOCSETDEBUG _u\_int32\_t_ _*level_
        Set the debug level.

        enum    { PF_DEBUG_NONE, PF_DEBUG_URGENT, PF_DEBUG_MISC,
    PF_DEBUG_NOISY };

       DIOCGETSTATESV2 _struct_ _pfioc\_states\_v2_ _*ps_
        Get state table entries.

        struct pfioc_states_v2 {
         int        ps_len;
         uint64_t        ps_req_version;
         union {
          void         *ps_buf;
          struct pf_state_export  *ps_states;
         };
        };

        struct pf_state_export {
         uint64_t  version;
         uint64_t  id;
         char  ifname[IFNAMSIZ];
         char  orig_ifname[IFNAMSIZ];
         struct pf_state_key_export key[2];
         struct pf_state_peer_export src;
         struct pf_state_peer_export dst;
         struct pf_addr rt_addr;
         uint32_t  rule;
         uint32_t  anchor;
         uint32_t  nat_rule;
         uint32_t  creation;
         uint32_t  expire;
         uint32_t  spare0;
         uint64_t  packets[2];
         uint64_t  bytes[2];
         uint32_t  creatorid;
         uint32_t  spare1;
         sa_family_t af;
         uint8_t  proto;
         uint8_t  direction;
         uint8_t  log;
         uint8_t  state_flags_compat;
         uint8_t  timeout;
         uint8_t  sync_flags;
         uint8_t  updates;
         uint16_t  state_flags;
         uint16_t  qid;
         uint16_t  pqid;
         uint16_t  dnpipe;
         uint16_t  dnrpipe;
         int32_t  rtableid;
         uint8_t  min_ttl;
         uint8_t  set_tos;
         uint16_t  max_mss;
         uint8_t  set_prio[2];
         uint8_t  rt;
         char  rt_ifname[IFNAMSIZ];
         uint8_t  spare[72];
        };

       DIOCCHANGERULE _struct_ _pfioc\_rule_ _*pcr_
        Add or remove the _rule_ in the ruleset specified by _rule.action_.

        The type of operation to be performed is indicated  by  _action_,
        which can be any of the following:

        enum    { PF_CHANGE_NONE, PF_CHANGE_ADD_HEAD, PF_CHANGE_ADD_TAIL,
    PF_CHANGE_ADD_BEFORE, PF_CHANGE_ADD_AFTER,
    PF_CHANGE_REMOVE, PF_CHANGE_GET_TICKET };

        _ticket_  must  be   set   to  the   value   obtained   with
        PF_CHANGE_GET_TICKET  for   all    actions except
        PF_CHANGE_GET_TICKET.  _pool\_ticket_ must be set to the value ob-
        tained  with  the  DIOCBEGINADDRS  call for all actions except
        PF_CHANGE_REMOVE and PF_CHANGE_GET_TICKET.  _anchor_ indicates to
        which anchor the operation applies.  _nr_ indicates the rule num-
        ber against which PF_CHANGE_ADD_BEFORE, PF_CHANGE_ADD_AFTER, or
        PF_CHANGE_REMOVE actions are applied.

       DIOCCHANGEADDR _struct_ _pfioc\_pooladdr_ _*pca_
        Add or remove the pool address _addr_ from the rule specified  by
        _r\_action_, _r\_num_, and _anchor_.

       DIOCSETTIMEOUT _struct_ _pfioc\_tm_ _*pt_

        struct pfioc_tm {
         int  timeout;
         int  seconds;
        };

        Set  the  state timeout  of _timeout_ to _seconds_.  The old value
        will be placed into _seconds_.  For possible values  of  _timeout_,
        consult the PFTM_* values in <_net/pfvar.h_>.

       DIOCGETTIMEOUT _struct_ _pfioc\_tm_ _*pt_
        Get  the  state timeout  of _timeout_.  The value will be placed
        into the _seconds_ field.

       DIOCCLRRULECTRS
        Clear per-rule statistics.

       DIOCSETLIMIT _struct_ _pfioc\_limit_ _*pl_
        Set the hard limits on the memory pools used by the packet fil-
        ter.

        struct pfioc_limit {
         int        index;
         unsigned        limit;
        };

        enum    { PF_LIMIT_STATES, PF_LIMIT_SRC_NODES, PF_LIMIT_FRAGS,
    PF_LIMIT_TABLE_ENTRIES, PF_LIMIT_MAX };

       DIOCGETLIMIT _struct_ _pfioc\_limit_ _*pl_
        Get the hard _limit_ for the memory pool indicated by _index_.

       DIOCRCLRTABLES _struct_ _pfioc\_table_ _*io_
        Clear all tables.  All the ioctls that manipulate radix tables
        use  the  same  structure described below.  For DIOCRCLRTABLES,
        _pfrio\_ndel_ contains on exit the number of tables deleted.

        struct pfioc_table {
         struct pfr_table  pfrio_table;
         void         *pfrio_buffer;
         int   pfrio_esize;
         int   pfrio_size;
         int   pfrio_size2;
         int   pfrio_nadd;
         int   pfrio_ndel;
         int   pfrio_nchange;
         int   pfrio_flags;
         u_int32_t  pfrio_ticket;
        };
        #define pfrio_exists    pfrio_nadd
        #define pfrio_nzero     pfrio_nadd
        #define pfrio_nmatch    pfrio_nadd
        #define pfrio_naddr     pfrio_size2
        #define pfrio_setflag   pfrio_size2
        #define pfrio_clrflag   pfrio_nadd

       DIOCRADDTABLES _struct_ _pfioc\_table_ _*io_
        Create one or more tables.  On entry, _pfrio\_buffer_  must  point
        to  an array of _struct_ _pfr\_table_ containing at least _pfrio\_size_
        elements.  _pfrio\_esize_ must be the size of  _struct_  _pfr\_table_.
        On  exit,  _pfrio\_nadd_ contains the number of tables effectively
        created.

        struct pfr_table {
         char        pfrt_anchor[MAXPATHLEN];
         char        pfrt_name[PF_TABLE_NAME_SIZE];
         u_int32_t       pfrt_flags;
         u_int8_t        pfrt_fback;
        };

       DIOCRDELTABLES _struct_ _pfioc\_table_ _*io_
        Delete one or more tables.  On entry, _pfrio\_buffer_  must  point
        to  an array of _struct_ _pfr\_table_ containing at least _pfrio\_size_
        elements.  _pfrio\_esize_ must be the size of  _struct_  _pfr\_table_.
        On  exit,  _pfrio\_ndel_ contains the number of tables effectively
        deleted.

       DIOCRGETTABLES _struct_ _pfioc\_table_ _*io_
        Get the list of all tables.  On entry, _pfrio\_buffer[pfrio\_size]_
        contains a valid writeable buffer for _pfr\_table_ structures.  On
        exit, _pfrio\_size_ contains the number of tables written into the
        buffer. If the buffer is too small, the kernel does not  store
        anything but just returns the required buffer size, without er-
        ror.

       DIOCRGETTSTATS _struct_ _pfioc\_table_ _*io_
        This call is like DIOCRGETTABLES but is used to get an array of
        _pfr\_tstats_ structures.

        struct pfr_tstats {
         struct pfr_table pfrts_t;
         u_int64_t pfrts_packets
         [PFR_DIR_MAX][PFR_OP_TABLE_MAX];
         u_int64_t pfrts_bytes
         [PFR_DIR_MAX][PFR_OP_TABLE_MAX];
         u_int64_t pfrts_match;
         u_int64_t pfrts_nomatch;
         time_t  pfrts_tzero;
         int  pfrts_cnt;
         int  pfrts_refcnt[PFR_REFCNT_MAX];
        };
        #define pfrts_name pfrts_t.pfrt_name
        #define pfrts_flags pfrts_t.pfrt_flags

       DIOCRCLRTSTATS _struct_ _pfioc\_table_ _*io_
        Clear  the  statistics  of  one or  more  tables.   On entry,
        _pfrio\_buffer_ must point to an array of  _struct_  _pfr\_table_  con-
        taining at least _pfrio\_size_ elements.  _pfrio\_esize_ must be the
        size of _struct_ _pfr\_table_.  On exit,  _pfrio\_nzero_  contains  the
        number of tables effectively cleared.

       DIOCRCLRADDRS _struct_ _pfioc\_table_ _*io_
        Clear all addresses in a table. On entry, _pfrio\_table_ contains
        the table to clear.  On exit, _pfrio\_ndel_ contains the number of
        addresses removed.

       DIOCRADDADDRS _struct_ _pfioc\_table_ _*io_
        Add  one  or  more addresses to a table.  On entry, _pfrio\_table_
        contains the table ID and _pfrio\_buffer_ must point to  an  array
        of  _struct_  _pfr\_addr_ containing at least _pfrio\_size_ elements to
        add to the table.  _pfrio\_esize_  must  be  the  size  of _struct_
        _pfr\_addr_.  On exit, _pfrio\_nadd_ contains the number of addresses
        effectively added.

        struct pfr_addr {
         union {
          struct in_addr _pfra_ip4addr;
          struct in6_addr _pfra_ip6addr;
         }  pfra_u;
         u_int8_t  pfra_af;
         u_int8_t  pfra_net;
         u_int8_t  pfra_not;
         u_int8_t  pfra_fback;
        };
        #define pfra_ip4addr    pfra_u._pfra_ip4addr
        #define pfra_ip6addr    pfra_u._pfra_ip6addr

       DIOCRDELADDRS _struct_ _pfioc\_table_ _*io_
        Delete one  or  more  addresses  from a  table.   On entry,
        _pfrio\_table_ contains the table ID and _pfrio\_buffer_  must  point
        to  an  array of _struct_ _pfr\_addr_ containing at least _pfrio\_size_
        elements to delete from the table.   _pfrio\_esize_  must  be  the
        size of _struct_ _pfr\_addr_.  On exit, _pfrio\_ndel_ contains the num-
        ber of addresses effectively deleted.

       DIOCRSETADDRS _struct_ _pfioc\_table_ _*io_
        Replace the content of a table by a new address list.  This is
        the most complicated command, which uses all the structure mem-
        bers.

        On entry, _pfrio\_table_ contains the table  ID  and  _pfrio\_buffer_
        must  point  to an array of _struct_ _pfr\_addr_ containing at least
        _pfrio\_size_ elements which become the new contents of the table.
        _pfrio\_esize_ must be the size of _struct_ _pfr\_addr_.  Additionally,
        if       _pfrio\_size2_       is      non-zero,
        _pfrio\_buffer[pfrio\_size..pfrio\_size2]_   must   be  a  writeable
        buffer, into which the kernel can copy the addresses that  have
        been   deleted during  the   replace operation.   On  exit,
        _pfrio\_ndel_, _pfrio\_nadd_, and _pfrio\_nchange_ contain the number of
        addresses deleted,  added,  and changed  by  the  kernel.   If
        _pfrio\_size2_  was  set  on  entry, _pfrio\_size2_ will point to the
        size of the buffer used, exactly like DIOCRGETADDRS.

       DIOCRGETADDRS _struct_ _pfioc\_table_ _*io_
        Get all the addresses of a table.  On entry,  _pfrio\_table_  con-
        tains  the  table  ID  and  _pfrio\_buffer[pfrio\_size]_ contains a
        valid writeable buffer for  _pfr\_addr_  structures.   On  exit,
        _pfrio\_size_  contains  the  number of addresses written into the
        buffer. If the buffer was too small, the kernel does not store
        anything but just returns the required buffer size, without re-
        turning an error.

       DIOCRGETASTATS _struct_ _pfioc\_table_ _*io_
        This call is like DIOCRGETADDRS but is used to get an array  of
        _pfr\_astats_ structures.

        struct pfr_astats {
         struct pfr_addr pfras_a;
         u_int64_t pfras_packets
         [PFR_DIR_MAX][PFR_OP_ADDR_MAX];
         u_int64_t pfras_bytes
         [PFR_DIR_MAX][PFR_OP_ADDR_MAX];
         time_t  pfras_tzero;
        };

       DIOCRCLRASTATS _struct_ _pfioc\_table_ _*io_
        Clear  the  statistics  of  one or  more addresses.  On entry,
        _pfrio\_table_ contains the table ID and _pfrio\_buffer_  must  point
        to  an  array of _struct_ _pfr\_addr_ containing at least _pfrio\_size_
        elements to be cleared from the table.  _pfrio\_esize_ must be the
        size of _struct_ _pfr\_addr_.  On  exit,  _pfrio\_nzero_  contains  the
        number of addresses effectively cleared.

       DIOCRTSTADDRS _struct_ _pfioc\_table_ _*io_
        Test   if  the  given  addresses  match a  table.   On entry,
        _pfrio\_table_ contains the table ID and _pfrio\_buffer_  must  point
        to  an  array of _struct_ _pfr\_addr_ containing at least _pfrio\_size_
        elements, each of which will be tested for a match in  the  ta-
        ble.   _pfrio\_esize_  must  be  the  size of _struct_ _pfr\_addr_.  On
        exit, the kernel updates the  _pfr\_addr_  array  by  setting  the
        _pfra\_fback_ member appropriately.

       DIOCRSETTFLAGS _struct_ _pfioc\_table_ _*io_
        Change  the PFR_TFLAG_CONST or PFR_TFLAG_PERSIST flags of a ta-
        ble.  On entry, _pfrio\_buffer_ must point to an array  of _struct_
        _pfr\_table_ containing at least _pfrio\_size_ elements.  _pfrio\_esize_
        must  be the size of _struct_ _pfr\_table_.  _pfrio\_setflag_ must con-
        tain the flags to add, while  _pfrio\_clrflag_  must  contain  the
        flags to remove.  On exit, _pfrio\_nchange_ and _pfrio\_ndel_ contain
        the  number  of tables altered or deleted by the kernel.  Yes,
        tables can be deleted if one removes the PFR_TFLAG_PERSIST flag
        of an unreferenced table.

       DIOCRINADEFINE _struct_ _pfioc\_table_ _*io_
        Defines a table in the inactive set.   On  entry,  _pfrio\_table_
        contains  the table ID and _pfrio\_buffer[pfrio\_size]_ contains an
        array of _pfr\_addr_ structures to put  in the  table.   A  valid
        ticket  must  also  be  supplied  to  _pfrio\_ticket_.   On  exit,
        _pfrio\_nadd_ contains 0 if the table was already defined  in  the
        inactive   list  or  1 if  a  new  table  has been  created.
        _pfrio\_naddr_ contains the number of addresses effectively put in
        the table.

       DIOCXBEGIN _struct_ _pfioc\_trans_ _*io_

        struct pfioc_trans {
         int  size;  /* number of elements */
         int  esize; /* size of each element in bytes */
         struct pfioc_trans_e {
          int        rs_num;
          char        anchor[MAXPATHLEN];
          u_int32_t       ticket;
         }        *array;
        };

        Clear all the inactive rulesets specified in the  _pfioc\_trans\_e_
        array. For  each ruleset, a ticket is returned for subsequent
        "add  rule"  ioctls,  as  well  as  for the  DIOCXCOMMIT   and
        DIOCXROLLBACK calls.

        Ruleset types, identified by _rs\_num_, include the following:

    PF_RULESET_SCRUB   Scrub (packet normalization) rules.
    PF_RULESET_FILTER  Filter rules.
    PF_RULESET_NAT     NAT (Network Address Translation) rules.
    PF_RULESET_BINAT   Bidirectional NAT rules.
    PF_RULESET_RDR     Redirect rules.
    PF_RULESET_ALTQ    ALTQ disciplines.
    PF_RULESET_TABLE   Address tables.

       DIOCXCOMMIT _struct_ _pfioc\_trans_ _*io_
        Atomically  switch  a vector of inactive rulesets to the active
        rulesets.  This call is implemented  as a  standard  two-phase
        commit, which  will either fail for all rulesets or completely
        succeed.  All tickets need to be  valid.   This ioctl  returns
        EBUSY  if  another process is concurrently updating some of the
        same rulesets.

       DIOCXROLLBACK _struct_ _pfioc\_trans_ _*io_
        Clean up the kernel by undoing  all  changes  that  have  taken
        place  on  the  inactive  rulesets  since  the last DIOCXBEGIN.
        DIOCXROLLBACK will  silently  ignore  rulesets  for  which  the
        ticket is invalid.

       DIOCSETHOSTID _u\_int32\_t_ _*hostid_
        Set  the  host ID, which is used by [_pfsync_(4)](https://man.freebsd.org/cgi/man.cgi?query=pfsync&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) to identify which
        host created state table entries.

       DIOCOSFPFLUSH
        Flush the passive OS fingerprint table.

       DIOCOSFPADD _struct_ _pf\_osfp\_ioctl_ _*io_

        struct pf_osfp_ioctl {
         struct pf_osfp_entry {
          SLIST_ENTRY(pf_osfp_entry) fp_entry;
          pf_osfp_t        fp_os;
          char         fp_class_nm[PF_OSFP_LEN];
          char         fp_version_nm[PF_OSFP_LEN];
          char         fp_subtype_nm[PF_OSFP_LEN];
         }         fp_os;
         pf_tcpopts_t        fp_tcpopts;
         u_int16_t        fp_wsize;
         u_int16_t        fp_psize;
         u_int16_t        fp_mss;
         u_int16_t        fp_flags;
         u_int8_t         fp_optcnt;
         u_int8_t         fp_wscale;
         u_int8_t         fp_ttl;
         int         fp_getnum;
        };

        Add a passive OS fingerprint to the table.  Set _fp\_os.fp\_os_  to
        the  packed  fingerprint,  _fp\_os.fp\_class\_nm_ to the name of the
        class (Linux, Windows, etc), _fp\_os.fp\_version\_nm_ to the name of
        the version (NT, 95, 98), and _fp\_os.fp\_subtype\_nm_ to  the  name
        of  the subtype  or patchlevel.  The members _fp\_mss_, _fp\_wsize_,
        _fp\_psize_, _fp\_ttl_, _fp\_optcnt_, and _fp\_wscale_ are set to  the  TCP
        MSS, the TCP window size, the IP length, the IP TTL, the number
        of  TCP options, and the TCP window scaling constant of the TCP
        SYN packet, respectively.

        The _fp\_flags_ member is filled according to  the  <_net/pfvar.h_>
        include file PF_OSFP_* defines. The _fp\_tcpopts_ member contains
        packed  TCP options.  Each option uses PF_OSFP_TCPOPT_BITS bits
        in   the   packed    value.     Options   include    any    of
        PF_OSFP_TCPOPT_NOP, PF_OSFP_TCPOPT_SACK, PF_OSFP_TCPOPT_WSCALE,
        PF_OSFP_TCPOPT_MSS, or PF_OSFP_TCPOPT_TS.

        The _fp\_getnum_ member is not used with this ioctl.

        The  structure's  slack space must be zeroed for correct opera-
        tion; [_memset_(3)](https://man.freebsd.org/cgi/man.cgi?query=memset&sektion=3&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly) the whole structure to zero before filling  and
        sending to the kernel.

       DIOCOSFPGET _struct_ _pf\_osfp\_ioctl_ _*io_
        Get  the  passive OS fingerprint number _fp\_getnum_ from the ker-
        nel's fingerprint list. The rest of the structure members will
        come back filled.  Get the whole list by repeatedly  increment-
        ing the _fp\_getnum_ number until the ioctl returns EBUSY.

       DIOCGETSRCNODES _struct_ _pfioc\_src\_nodes_ _*psn_

        struct pfioc_src_nodes {
         int     psn_len;
         union {
          caddr_t        psu_buf;
          struct pf_src_node      *psu_src_nodes;
         } psn_u;
        #define psn_buf        psn_u.psu_buf
        #define psn_src_nodes   psn_u.psu_src_nodes
        };

        Get  the  list  of  source  nodes  kept by sticky addresses and
        source tracking.  The ioctl must be called  once  with  _psn\_len_
        set  to 0.  If the ioctl returns without error, _psn\_len_ will be
        set to the  size  of  the  buffer  required  to hold  all  the
        _pf\_src\_node_  structures held  in  the table.  A buffer of this
        size should then be allocated, and a  pointer  to  this buffer
        placed in _psn\_buf_.  The ioctl must then be called again to fill
        this buffer with the actual source node data.  After that call,
        _psn\_len_ will be set to the length of the buffer actually used.

       DIOCCLRSRCNODES
        Clear the tree of source tracking nodes.

       DIOCIGETIFACES _struct_ _pfioc\_iface_ _*io_
        Get  the  list  of interfaces and interface groups known to **pf**.
        All the ioctls that manipulate interfaces use the  same struc-
        ture described below:

        struct pfioc_iface {
         char   pfiio_name[IFNAMSIZ];
         void         *pfiio_buffer;
         int   pfiio_esize;
         int   pfiio_size;
         int   pfiio_nzero;
         int   pfiio_flags;
        };

        If  not empty, _pfiio\_name_ can be used to restrict the search to
        a specific interface or group.  _pfiio\_buffer[pfiio\_size]_ is the
        user-supplied  buffer  for  returning  the  data.   On entry,
        _pfiio\_size_  contains the number of _pfi\_kif_ entries that can fit
        into the buffer.  The kernel will replace  this value  by  the
        real  number of entries it wants to return.  _pfiio\_esize_ should
        be set to **sizeof(struct** **pfi_kif)**.

        The data is returned in the _pfi\_kif_ structure described below:

        struct pfi_kif {
         char    pfik_name[IFNAMSIZ];
         union {
          RB_ENTRY(pfi_kif) pfik_tree;
          LIST_ENTRY(pfi_kif) pfik_list;
         };
         u_int64_t   pfik_packets[2][2][2];
         u_int64_t   pfik_bytes[2][2][2];
         u_int32_t   pfik_tzero;
         u_int    pfik_flags;
         struct ifnet         *pfik_ifp;
         struct ifg_group         *pfik_group;
         u_int    pfik_rulerefs;
         TAILQ_HEAD(, pfi_dynaddr) pfik_dynaddrs;
        };

       DIOCSETIFFLAG _struct_ _pfioc\_iface_ _*io_
        Set the user settable flags (described above) of the **pf** inter-
        nal  interface  description.  The filtering process is the same
        as for DIOCIGETIFACES.

        #define PFI_IFLAG_SKIP  0x0100  /* skip filtering on interface */

       DIOCCLRIFFLAG _struct_ _pfioc\_iface_ _*io_
        Works as DIOCSETIFFLAG above but clears the flags.

       DIOCKILLSRCNODES _struct_ _pfioc\_iface_ _*io_
        Explicitly remove source tracking nodes.

[**FILES**](https://man.freebsd.org/cgi/man.cgi?query=pf&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#end)
       _/dev/pf_ packet filtering device.

[**EXAMPLES**](https://man.freebsd.org/cgi/man.cgi?query=pf&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#end)
       The following example demonstrates how to use the  DIOCNATLOOK  command
       to find the internal host/port of a NATed connection:

       #include <sys/types.h>
       #include <sys/socket.h>
       #include <sys/ioctl.h>
       #include <sys/fcntl.h>
       #include <net/if.h>
       #include <netinet/in.h>
       #include <net/pfvar.h>
       #include <err.h>
       #include <stdio.h>
       #include <stdlib.h>

       u_int32_t
       read_address(const char *s)
       {
        int a, b, c, d;

        sscanf(s, "%i.%i.%i.%i", &a, &b, &c, &d);
        return htonl(a << 24 | b << 16 | c << 8 | d);
       }

       void
       print_address(u_int32_t a)
       {
        a = ntohl(a);
        printf("%d.%d.%d.%d", a >> 24 & 255, a >> 16 & 255,
     a >> 8 & 255, a & 255);
       }

       int
       main(int argc, char *argv[])
       {
        struct pfioc_natlook nl;
        int dev;

        if (argc != 5) {
         printf("%s <gwy addr> <gwy port> <ext addr> <ext port>\n",
      argv[0]);
         return 1;
        }

        dev = open("/dev/pf", O_RDWR);
        if (dev == -1)
         err(1, "open(\"/dev/pf\") failed");

        memset(&nl, 0, sizeof(struct pfioc_natlook));
        nl.saddr.v4.s_addr      = read_address(argv[1]);
        nl.sport         = htons(atoi(argv[2]));
        nl.daddr.v4.s_addr      = read_address(argv[3]);
        nl.dport         = htons(atoi(argv[4]));
        nl.af         = AF_INET;
        nl.proto         = IPPROTO_TCP;
        nl.direction        = PF_IN;

        if (ioctl(dev, DIOCNATLOOK, &nl))
         err(1, "DIOCNATLOOK");

        printf("internal host ");
        print_address(nl.rsaddr.v4.s_addr);
        printf(":%u\n", ntohs(nl.rsport));
        return 0;
       }

[**SEE ALSO**](https://man.freebsd.org/cgi/man.cgi?query=pf&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#end)
       [_ioctl_(2)](https://man.freebsd.org/cgi/man.cgi?query=ioctl&sektion=2&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly), [_altq_(4)](https://man.freebsd.org/cgi/man.cgi?query=altq&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly), [_if\_bridge_(4)](https://man.freebsd.org/cgi/man.cgi?query=if_bridge&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly), [_pflog_(4)](https://man.freebsd.org/cgi/man.cgi?query=pflog&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly), [_pfsync_(4)](https://man.freebsd.org/cgi/man.cgi?query=pfsync&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly), [_pfctl_(8)](https://man.freebsd.org/cgi/man.cgi?query=pfctl&sektion=8&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly), [_altq_(9)](https://man.freebsd.org/cgi/man.cgi?query=altq&sektion=9&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly)

[**HISTORY**](https://man.freebsd.org/cgi/man.cgi?query=pf&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#end)
       The  **pf** packet filtering  mechanism first appeared in OpenBSD 3.0 and
       then FreeBSD 5.2.

       This implementation is derived from OpenBSD 4.5.  A number of  individ-
       ual  features,  improvements,  bug  fixes  and security fixes have been
       ported from later versions of OpenBSD.  It has been heavily modified to
       be capable of running in multithreaded FreeBSD  kernel  and  scale  its
       performance on multiple CPUs.

FreeBSD 15.0    July 2, 2025     _PF_(4)
[* * *](https://man.freebsd.org/cgi/man.cgi?query=pf&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly)
[](https://man.freebsd.org/cgi/man.cgi?query=pf&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly)[NAME](https://man.freebsd.org/cgi/man.cgi?query=pf&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#NAME) | [SYNOPSIS](https://man.freebsd.org/cgi/man.cgi?query=pf&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#SYNOPSIS) | [DESCRIPTION](https://man.freebsd.org/cgi/man.cgi?query=pf&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#DESCRIPTION) | [SYSCTL VARIABLES](https://man.freebsd.org/cgi/man.cgi?query=pf&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#SYSCTL_VARIABLES) | [LOADER TUNABLES](https://man.freebsd.org/cgi/man.cgi?query=pf&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#LOADER_TUNABLES) | [KERNEL OPTIONS](https://man.freebsd.org/cgi/man.cgi?query=pf&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#KERNEL_OPTIONS) | [IOCTL INTERFACE](https://man.freebsd.org/cgi/man.cgi?query=pf&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#IOCTL_INTERFACE) | [FILES](https://man.freebsd.org/cgi/man.cgi?query=pf&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#FILES) | [EXAMPLES](https://man.freebsd.org/cgi/man.cgi?query=pf&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#EXAMPLES) | [SEE ALSO](https://man.freebsd.org/cgi/man.cgi?query=pf&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#SEE_ALSO) | [HISTORY](https://man.freebsd.org/cgi/man.cgi?query=pf&sektion=4&apropos=0&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly#HISTORY)

Want to link to this manual page? Use this URL:

<[https://man.freebsd.org/cgi/man.cgi?query=pf&sektion=4&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly](https://man.freebsd.org/cgi/man.cgi?query=pf&sektion=4&manpath=FreeBSD+15.0-RELEASE+and+Ports.quarterly)>

* * *
