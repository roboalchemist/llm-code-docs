# Source: https://tomcat.apache.org/connectors-doc/miscellaneous/changelog.html

Title: The Apache Tomcat Connectors - Miscellaneous Documentation (1.2.50)

URL Source: https://tomcat.apache.org/connectors-doc/miscellaneous/changelog.html

Markdown Content:
Changelog
---------

### Preface

This is the Changelog for Apache Tomcat Connectors. This changelog does not contain all updates and fixes to the Tomcat connectors (yet). It should contain fixes made only after November 10th 2004, when the new documentation project for JK was started.

### Changes between 1.2.49 and 1.2.50

#### IIS

*   ![Image 1: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) Update PCRE bundled with the ISAPI redirector to 8.45. (rjung) 

### Changes between 1.2.48 and 1.2.49

### Changes between 1.2.47 and 1.2.48

#### IIS

*   ![Image 2: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) Update the installation how-to to remove windows versions that are no longer supported and to add Windows Server 2019. (markt) 

### Changes between 1.2.46 and 1.2.47

### Changes between 1.2.45 and 1.2.46

#### Apache

*   ![Image 3: Fix: ](https://tomcat.apache.org/connectors-doc/images/fix.gif)[62751](https://bz.apache.org/bugzilla/show_bug.cgi?id=62751): Fix regression in 1.2.44 which resulted in socket_connect_timeout to be interpreted in units of seconds instead of milliseconds on platforms that provide poll(). (rjung) 

### Changes between 1.2.44 and 1.2.45

#### IIS

*   ![Image 4: Fix: ](https://tomcat.apache.org/connectors-doc/images/fix.gif) Improve path parameter handling so that `strip_session` can remove session IDs that are specified on path parameters in any segment of the URI rather than only the final segment. (markt) 

### Changes between 1.2.43 and 1.2.44

### Changes between 1.2.42 and 1.2.43

### Changes between 1.2.41 and 1.2.42

### Changes between 1.2.40 and 1.2.41

#### Native

*   ![Image 5: Fix: ](https://tomcat.apache.org/connectors-doc/images/fix.gif) AJP, LB: Reduce lock contention during maintenance function. This was observable when using a big number of AJP13 and LB workers, especially in combination with the Apache httpd prefork MPM. (rjung) 
*   ![Image 6: Fix: ](https://tomcat.apache.org/connectors-doc/images/fix.gif)[57060](https://bz.apache.org/bugzilla/show_bug.cgi?id=57060): Allow building from outside of source tree. Patch contributed by Petr Sumbera. (rjung) 
*   ![Image 7: Fix: ](https://tomcat.apache.org/connectors-doc/images/fix.gif)[56703](https://bz.apache.org/bugzilla/show_bug.cgi?id=56703): Status: Fix inflated counter for current number of backend connections especially when a connection timeout occurred on the backend. (rjung) 
*   ![Image 8: Fix: ](https://tomcat.apache.org/connectors-doc/images/fix.gif)[56661](https://bz.apache.org/bugzilla/show_bug.cgi?id=56661): Fix Servlet API getLocalAddr(). Works for Tomcat 6.0.42, 7.0.55 and 8.0.11 and Apache and ISAPI plugins. (rjung) 
*   ![Image 9: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) Status: Log old and new values when changing worker attributes. (rjung) 
*   ![Image 10: Fix: ](https://tomcat.apache.org/connectors-doc/images/fix.gif)[56667](https://bz.apache.org/bugzilla/show_bug.cgi?id=56667): Status: Fix log message when changing activation state of all members. (rjung) 
*   ![Image 11: Fix: ](https://tomcat.apache.org/connectors-doc/images/fix.gif)[56565](https://bz.apache.org/bugzilla/show_bug.cgi?id=56565): Fix IPV6 address resolve on non-dual network stacks. (mturk) 
*   ![Image 12: Fix: ](https://tomcat.apache.org/connectors-doc/images/fix.gif)[50511](https://bz.apache.org/bugzilla/show_bug.cgi?id=50511): Reduce log level for "OPTIONS *" requests from warning to debug. (rjung) 
*   ![Image 13: Fix: ](https://tomcat.apache.org/connectors-doc/images/fix.gif) Apache: Copy log notes instead of using references to prevent access to memory from closed pool. (rjung) 
*   ![Image 14: Add: ](https://tomcat.apache.org/connectors-doc/images/add.gif) Add option to control handling of multiple adjacent slashes in mount and unmount. New default is collapsing the slashes only in unmount. Configuration is done via new JkOption for Apache ("CollapseSlashesAll", "CollapseSlashesNone" or "CollapseSlashesUnmount") and via property "collapse_slashes" for IIS (values "all", "none", "unmount"). This is the fix for CVE-2014-8111. (rjung) 
*   ![Image 15: Add: ](https://tomcat.apache.org/connectors-doc/images/add.gif) Add more checks for shared memory allocation. (rjung) 
*   ![Image 16: Add: ](https://tomcat.apache.org/connectors-doc/images/add.gif)[56869](https://bz.apache.org/bugzilla/show_bug.cgi?id=56869): Status: Add maximum number of open backend connections to status worker. Patch contributed by Martin Knoblauch. (rjung) 
*   ![Image 17: Add: ](https://tomcat.apache.org/connectors-doc/images/add.gif)[56770](https://bz.apache.org/bugzilla/show_bug.cgi?id=56770): AJP: Add worker name to all log messages. Patch contributed by Martin Knoblauch. (rjung) 
*   ![Image 18: Fix: ](https://tomcat.apache.org/connectors-doc/images/fix.gif)[50186](https://bz.apache.org/bugzilla/show_bug.cgi?id=50186): Docs: Clarify relation between "connection_pool_timeout" and "keepAliveTimeout" or "connectionTimeout" in the Tomcat AJP connector configuration. (rjung) 
*   ![Image 19: Fix: ](https://tomcat.apache.org/connectors-doc/images/fix.gif)[52334](https://bz.apache.org/bugzilla/show_bug.cgi?id=52334): LB: Calculate worker recovery time based on last recovery attempt time instead of original error time after the first recovery attempt. (rjung) 
*   ![Image 20: Fix: ](https://tomcat.apache.org/connectors-doc/images/fix.gif)[54596](https://bz.apache.org/bugzilla/show_bug.cgi?id=54596) part 1: IIS: Fix missing last character when parsing relative file names with no ".." directory components from configuration. (rjung) 
*   ![Image 21: Fix: ](https://tomcat.apache.org/connectors-doc/images/fix.gif)[54596](https://bz.apache.org/bugzilla/show_bug.cgi?id=54596) part 2: IIS: Fix using relative file names in config with ".." path segments that go up the directory hierarchy higher than the starting point of the relative file name. (rjung) 
*   ![Image 22: Fix: ](https://tomcat.apache.org/connectors-doc/images/fix.gif) Status: Add logging if status worker output was dropped due to insufficient buffer size. (rjung) 
*   ![Image 23: Fix: ](https://tomcat.apache.org/connectors-doc/images/fix.gif) Reduce log buffer from 8KB to 1KB. Add logging in case of failed logging and add trailing "..." to lines which were likely truncated. (rjung) 
*   ![Image 24: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) Replace fixed allocation of 32 entries for fail_on_status by dynamic allocation. (rjung) 
*   ![Image 25: Add: ](https://tomcat.apache.org/connectors-doc/images/add.gif) Enforce implementation restriction on maximal length "60" of worker attributes "name", "host", "route", "domain", "redirect", "session_cookie", "session_path" and "set_session_cookie". Checks were added to configuration file processing and configuration updates via the status worker. (rjung) 
*   ![Image 26: Add: ](https://tomcat.apache.org/connectors-doc/images/add.gif)[52483](https://bz.apache.org/bugzilla/show_bug.cgi?id=52483): Apache: Add debug logging for result of JkOptions configuration processing. (rjung) 
*   ![Image 27: Fix: ](https://tomcat.apache.org/connectors-doc/images/fix.gif)[54177](https://bz.apache.org/bugzilla/show_bug.cgi?id=54177): Status: Use numeric time stamps instead of textual ones to avoid non-well-formed XML output. Textual timestamps are formatted according to locale settings and reencoding them to UTF-8 would be cumbersome. (rjung) 
*   ![Image 28: Fix: ](https://tomcat.apache.org/connectors-doc/images/fix.gif)[56618](https://bz.apache.org/bugzilla/show_bug.cgi?id=56618): Status: Use percent decoding when reading query string parameters. For example this fixes editing IPv6 addresses via the status worker if the client encodes ":" as "%3A". Patch contributed by Christopher Schultz. (rjung) 
*   ![Image 29: Fix: ](https://tomcat.apache.org/connectors-doc/images/fix.gif)[56452](https://bz.apache.org/bugzilla/show_bug.cgi?id=56452): Fix crash in debug logging for IPv6 adresses. Patch contributed by Christopher Schultz. (rjung) 
*   ![Image 30: Fix: ](https://tomcat.apache.org/connectors-doc/images/fix.gif)[34526](https://bz.apache.org/bugzilla/show_bug.cgi?id=34526): Apache: Improve compatibility with mod_deflate request body inflation. An automatic detection of mod_deflate inflation is not implemented. Use the new Apache environment variable JK_IGNORE_CL instead, to let mod_jk ignore an existing Content-Length request header. (rjung) 
*   ![Image 31: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif)[44454](https://bz.apache.org/bugzilla/show_bug.cgi?id=44454): LB: Add warning to docs about problems with "busyness" load balancing method. (rjung) 
*   ![Image 32: Fix: ](https://tomcat.apache.org/connectors-doc/images/fix.gif)[44454](https://bz.apache.org/bugzilla/show_bug.cgi?id=44454): Improve busy counter by using atomics. (rjung) 
*   ![Image 33: Fix: ](https://tomcat.apache.org/connectors-doc/images/fix.gif)[56703](https://bz.apache.org/bugzilla/show_bug.cgi?id=56703): Status: Improve connected counter. Use atomics and for mod_jk (Apache) currectly count down connections closed by child processes that are stopped. (rjung) 
*   ![Image 34: Fix: ](https://tomcat.apache.org/connectors-doc/images/fix.gif)[44571](https://bz.apache.org/bugzilla/show_bug.cgi?id=44571): Ensure that we return with status 503 if we can not get and endpoint for a worker. (rjung) 
*   ![Image 35: Fix: ](https://tomcat.apache.org/connectors-doc/images/fix.gif) Apache: Improve log handling during graceful or normal restart. (rjung) 
*   ![Image 36: Fix: ](https://tomcat.apache.org/connectors-doc/images/fix.gif) Don't update last access time of worker connections during optional checking of idle connections using CPing. Updating the time stamp breaks closing idle connections. (rjung) 
*   ![Image 37: Fix: ](https://tomcat.apache.org/connectors-doc/images/fix.gif) Adjust linger parameters used during connection shutdown. (rjung) 
*   ![Image 38: Fix: ](https://tomcat.apache.org/connectors-doc/images/fix.gif) Fix annoying redefine warnings for the autoconf PACKAGE defines during configure based builds. (rjung) 
*   ![Image 39: Fix: ](https://tomcat.apache.org/connectors-doc/images/fix.gif) Status: Use multi-line table headers and fix invalid xml output. (rjung) 
*   ![Image 40: Fix: ](https://tomcat.apache.org/connectors-doc/images/fix.gif)[44571](https://bz.apache.org/bugzilla/show_bug.cgi?id=44571): Implement an optional limit on concurrent requests allowed for a worker (attribute "busy_limit"). Original patch contributed by zealot0630 at gmail dot com. (rjung) 
*   ![Image 41: Fix: ](https://tomcat.apache.org/connectors-doc/images/fix.gif) Correct log message "all endpoints are disconnected" to "no usable connection found, will create a new one". Tone done from info log level to debug for the common case. (rjung) 
*   ![Image 42: Add: ](https://tomcat.apache.org/connectors-doc/images/add.gif)[57536](https://bz.apache.org/bugzilla/show_bug.cgi?id=57536): AJP: Allow to configure connection source address. This should only be used on multi-homed hosts. The feature is experimental. (rjung) 
*   ![Image 43: Add: ](https://tomcat.apache.org/connectors-doc/images/add.gif)[57540](https://bz.apache.org/bugzilla/show_bug.cgi?id=57540): AJP: Forward name of SSL protocol used for handling the request (SSLv3, TLSv1, TLSv1.1, TLSv1.2). (rjung) 

### Changes between 1.2.39 and 1.2.40

### Changes between 1.2.37 and 1.2.39

### Changes between 1.2.36 and 1.2.37

### Changes between 1.2.35 and 1.2.36

### Changes between 1.2.33 and 1.2.35

### Changes between 1.2.32 and 1.2.33

### Changes between 1.2.31 and 1.2.32

### Changes between 1.2.30 and 1.2.31

### Changes between 1.2.28 and 1.2.30

### Changes between 1.2.27 and 1.2.28

### Changes between 1.2.26 and 1.2.27

#### Native

*   ![Image 44: Fix: ](https://tomcat.apache.org/connectors-doc/images/fix.gif)[46109](https://bz.apache.org/bugzilla/show_bug.cgi?id=46109): Decay reply_timeouts even when lb method is busyness. Also reset reply_timeouts during forced recovery. (rjung) 
*   ![Image 45: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) AJP13: Recycle connection if previous request didn't complete. (mturk) 
*   ![Image 46: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) Maintain should not run multiple times in parallel. (mturk) 
*   ![Image 47: Fix: ](https://tomcat.apache.org/connectors-doc/images/fix.gif) Apache: Fix small memory leak during restart. (mturk) 
*   ![Image 48: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) Improve signal handling during socket shutdown. (mturk) 
*   ![Image 49: Add: ](https://tomcat.apache.org/connectors-doc/images/add.gif) URI Map: Add debug dump function for uri worker map. (rjung) 
*   ![Image 50: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) Add revision number to version info for non-release builds. (rjung) 
*   ![Image 51: Add: ](https://tomcat.apache.org/connectors-doc/images/add.gif) IIS: Optionally allow chunked encoding for responses. At the moment only usable, if build with ISAPI_ALLOW_CHUNKING defined. Based on patch by Tim Whittington. (rjung) 
*   ![Image 52: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) IIS: Optionally use raw headers instead of CGI headers. Fixes problem "underscore=dash" problem in header names. At the moment only available, if build with USE_RAW_HEADERS defined. (rjung) 
*   ![Image 53: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) IIS: Optionally improve IIS 5.1 compatibility. At the moment only available, if build with AUTOMATIC_AUTH_NOTIFICATION defined. Based on patch by Tim Whittington. (rjung) 
*   ![Image 54: Fix: ](https://tomcat.apache.org/connectors-doc/images/fix.gif) IIS: Fix memory corruption due to parallel initialization by multiple threads. (rjung) 
*   ![Image 55: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) Windows: Use non-default socket keepalive interval. (mturk) 
*   ![Image 56: Add: ](https://tomcat.apache.org/connectors-doc/images/add.gif) IIS: Add environment variables JKISAPI_PATH and JKISAPI_NAME. (mturk) 
*   ![Image 57: Add: ](https://tomcat.apache.org/connectors-doc/images/add.gif) Added socket_connect_timeout directive for setting the connect timeout for the socket. This enables to have low connection timeout but higher operational timeouts. (mturk) 
*   ![Image 58: Fix: ](https://tomcat.apache.org/connectors-doc/images/fix.gif) AJP13: [[**CVE-2008-5519**](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2008-5519)] Always send initial POST packet even if the client disconnected after sending request but before providing POST data. In that case or in case the client broke the connection in a middle of read send an zero size packet informing container about broken client connection. (mturk) 
*   ![Image 59: Add: ](https://tomcat.apache.org/connectors-doc/images/add.gif) AJP13: Added connection_acquire_timeout directive for setting the absolute timeout the worker will wait for a free endpoint. (mturk) 
*   ![Image 60: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) Apache: Allow to set path parameter used when doing JkStripSession. (mturk) 
*   ![Image 61: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) Refactor retries implementation and change semantics of retries attributes. (mturk) 
*   ![Image 62: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) Status: Allow showing only a single member for a load balancer. (rjung) 
*   ![Image 63: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) Status: Add display of seconds since last statistics reset and access and transfer rates. (rjung) 
*   ![Image 64: Add: ](https://tomcat.apache.org/connectors-doc/images/add.gif) AJP13: Add a configurable retry_interval time. (rjung) 
*   ![Image 65: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) Documentation: Enhance description of connection_pool_size. (rjung) 
*   ![Image 66: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) IIS: Refactor error page generation. (mturk) 
*   ![Image 67: Fix: ](https://tomcat.apache.org/connectors-doc/images/fix.gif) IIS: SERVER_NAME variable can be the same for multiple different server instances if requests are handled according to the ip:port combination. Use INSTANCE_ID variable to which the request belongs instead. (mturk) 
*   ![Image 68: Add: ](https://tomcat.apache.org/connectors-doc/images/add.gif) Allow forwarding server error pages. This can be done on per-uri basis using new use_server_errors extension. (mturk) 
*   ![Image 69: Add: ](https://tomcat.apache.org/connectors-doc/images/add.gif) Added session_cookie and session_path for configuring default session identifiers. (mturk) 
*   ![Image 70: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) Use max_packet_size also as TCP send and receive buffer size. (mturk) 
*   ![Image 71: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) Apache: Do not allow Apache to start in multi-threaded mode if mod_jk was only build for single threaded server (prefork). (mturk) 
*   ![Image 72: Fix: ](https://tomcat.apache.org/connectors-doc/images/fix.gif)[45812](https://bz.apache.org/bugzilla/show_bug.cgi?id=45812): Add done() service method that causes sending EOS bucket for Apache httpd 2.x. This allows filter chain to work properly. (mturk) 
*   ![Image 73: Add: ](https://tomcat.apache.org/connectors-doc/images/add.gif) Added connection_ping_interval, ping_timeout and ping_mode directives. (mturk) 
*   ![Image 74: Fix: ](https://tomcat.apache.org/connectors-doc/images/fix.gif) Apache: Use correct ld flags provided by apxs when building module. Prevents some crashes on AIX for httpd 1.3 module. (rjung) 
*   ![Image 75: Fix: ](https://tomcat.apache.org/connectors-doc/images/fix.gif) Documentation: "val" attribute numbering in status worker needs to start with 0 instead of 1. (rjung) 
*   ![Image 76: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) Documentation: Remove JNI parameters from sample configuration in the workers common howto. (rjung) 
*   ![Image 77: Fix: ](https://tomcat.apache.org/connectors-doc/images/fix.gif)[45026](https://bz.apache.org/bugzilla/show_bug.cgi?id=45026): For Apache httpd 2.x add "Unknown Reason" as the reason phrase, if we get an empty one from the backend. Otherwise httpd 2.x returns status 500. (rjung) 
*   ![Image 78: Fix: ](https://tomcat.apache.org/connectors-doc/images/fix.gif) Build: Fix Cygwin build. (rjung) 
*   ![Image 79: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) Documentation: Add info to docs, that variables sent via JkEnvVar are not listed in request.getAttributeNames(). (rjung) 
*   ![Image 80: Add: ](https://tomcat.apache.org/connectors-doc/images/add.gif) Add watchdog background thread for Apache 2.x and IIS doing internal maintenance (idle connection checks, backend probing). See JkWatchdogInternal (Apache) and watchdog_interval (IIS). (mturk) 
*   ![Image 81: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) Change log level of some messages from error to info. (mturk) 
*   ![Image 82: Fix: ](https://tomcat.apache.org/connectors-doc/images/fix.gif) Documentation: Fix docs for worker attribute "secret". (rjung) 
*   ![Image 83: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) Detect correct plugin name for various web servers via additional preprocessor defines. (rjung) 
*   ![Image 84: Fix: ](https://tomcat.apache.org/connectors-doc/images/fix.gif) LB: Do not put loadbalancer node in error state if there is opened channel. This fixes the bug when new connection fails due to busyness, causing opened connections fail stickyness. This brings back per-node busy counter and private state array for each request. We can mark the state as error for failover to work while still operating and reporting node as OK if there are opened working connections. (mturk) 
*   ![Image 85: Fix: ](https://tomcat.apache.org/connectors-doc/images/fix.gif)[44738](https://bz.apache.org/bugzilla/show_bug.cgi?id=44738): Fix merging of JkOption ForwardURI* between virtual hosts. Patch contributed by Toshihiro Sasajima. (rjung) 
*   ![Image 86: Add: ](https://tomcat.apache.org/connectors-doc/images/add.gif) URI Map: Add extension attributes to uri worker map. Allowed are reply_timeout, active/disabled/stopped and fail_on_status. Usage currently only implemented for httpd and IIS. (rjung+mturk) 
*   ![Image 87: Fix: ](https://tomcat.apache.org/connectors-doc/images/fix.gif) URI Map: Make dynamic reloading atomic and free memory not needed any longer. (rjung) 
*   ![Image 88: Add: ](https://tomcat.apache.org/connectors-doc/images/add.gif) Configure: Don't use post httpd 2.2.0 API functions when building with new --enable-api-compatibility configure switch. (rjung) 
*   ![Image 89: Fix: ](https://tomcat.apache.org/connectors-doc/images/fix.gif) Apache: JkAutoAlias does not work in combination with JkMountCopy if there are no JkMount in virtual host. (rjung) 
*   ![Image 90: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) LB: Optimize state macros to improve performance. (rjung) 
*   ![Image 91: Add: ](https://tomcat.apache.org/connectors-doc/images/add.gif) Apache: Allow dynamic setting of reply timeout using the environment variable JK_REPLY_TIMEOUT. (rjung) 
*   ![Image 92: Add: ](https://tomcat.apache.org/connectors-doc/images/add.gif) Status: Add manageability for ajp parameters of ajp workers and ajp lb members. (rjung) 
*   ![Image 93: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) Status: Change parameter names of update action to make them more easily distinguishable from other parameters. (rjung) 
*   ![Image 94: Add: ](https://tomcat.apache.org/connectors-doc/images/add.gif) Status: Add ajp worker statistics also for workers, that are not lb members. (rjung) 
*   ![Image 95: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) AJP: Refactor factories, move ajp13/ajp14 common parts into ajp_factory. (rjung) 
*   ![Image 96: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) Status: Only sync shm worker config values of the workers for which we changed values. (rjung) 
*   ![Image 97: Fix: ](https://tomcat.apache.org/connectors-doc/images/fix.gif) Status: Set lb_factor instead of distance. (rjung) 
*   ![Image 98: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) Status: Minor layout changes, use drop down instead of multiple text links. (rjung) 
*   ![Image 99: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) SHM: Use local copies of read mostly attributes of lb sub workers in lb and status worker. (rjung) 
*   ![Image 100: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) Status: Add "dump" action to dump our initial configuration. (rjung) 
*   ![Image 101: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) Status: Use property table to decide which cmd action uses which output elements. (rjung) 
*   ![Image 102: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) Common: Include original configuration map in worker_env to make it available for workers, e.g. the status worker. (rjung) 
*   ![Image 103: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) LB: Refactor "route" return for httpd note. Don't use a member of the worker_record, because that's not thread safe. (rjung) 
*   ![Image 104: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) Common: Refactor "retries", remove from service and jk_worker, move into ajp worker instead. (rjung) 
*   ![Image 105: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) SHM: Use distinct structs for lb and ajp13 in shm. Improves type safety and saves a few bytes. (rjung) 
*   ![Image 106: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) SHM: Remove unused attributes. (rjung) 
*   ![Image 107: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) SHM: Automatically determine shm size for all web servers. (rjung) 
*   ![Image 108: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) SHM: Make open/attach logging consistent for all web servers. (rjung) 
*   ![Image 109: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) Status: Include server local time in output. (rjung) 
*   ![Image 110: Fix: ](https://tomcat.apache.org/connectors-doc/images/fix.gif)[44116](https://bz.apache.org/bugzilla/show_bug.cgi?id=44116): Fix handling of multiple JSESSIONID cookies. (rjung) 
*   ![Image 111: Fix: ](https://tomcat.apache.org/connectors-doc/images/fix.gif)[37850](https://bz.apache.org/bugzilla/show_bug.cgi?id=37850): Use thread safe localtime_r where appropriate. (rjung) 
*   ![Image 112: Fix: ](https://tomcat.apache.org/connectors-doc/images/fix.gif) Use thread safe strtok_r on more platforms, especially AIX. (rjung) 
*   ![Image 113: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) Status: Improve XSS hardening. (rjung) 
*   ![Image 114: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif)[35303](https://bz.apache.org/bugzilla/show_bug.cgi?id=35303): Move initialization of service members with defaults from web server specific code to our generic jk_init_ws_service() function. (rjung) 
*   ![Image 115: Fix: ](https://tomcat.apache.org/connectors-doc/images/fix.gif)[36385](https://bz.apache.org/bugzilla/show_bug.cgi?id=36385): Add missing prepost CPing/CPong directly after connect in case prepost CPing is used, but no connect CPing. (rjung) 
*   ![Image 116: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif)[37322](https://bz.apache.org/bugzilla/show_bug.cgi?id=37322): Apache: Enhance robustness of message formating in jk_error_exit(). (rjung) 
*   ![Image 117: Fix: ](https://tomcat.apache.org/connectors-doc/images/fix.gif)[44147](https://bz.apache.org/bugzilla/show_bug.cgi?id=44147): Multiple load balancing workers problem. (rjung) 

### Changes between 1.2.25 and 1.2.26

### Changes between 1.2.24 and 1.2.25

### Changes between 1.2.23 and 1.2.24

#### Native

*   ![Image 118: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) Documentation: Improved workers.properties description in the reference guide. (rjung) 
*   ![Image 119: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) Documentation: Add a HowTo about the various timeouts. rjung) 
*   ![Image 120: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) Logging: add milliseconds to the default timestamp format, if we have gettimeofday(). (rjung) 
*   ![Image 121: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) Apache: add milliseconds (%Q) and microseconds (%q) as possible JkLogStampFormat conversion specifiers. This does not use strftime(), but needs gettimeofday(). (rjung) 
*   ![Image 122: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) IIS & Sun: Log service failures also, if return code is negative. (rjung) 
*   ![Image 123: Fix: ](https://tomcat.apache.org/connectors-doc/images/fix.gif)[42849](https://bz.apache.org/bugzilla/show_bug.cgi?id=42849): Abort startup of Apache httpd 1.3 in case mod_jk initialization failed. We already do the same for Apache httpd 2.x. (rjung) 
*   ![Image 124: Fix: ](https://tomcat.apache.org/connectors-doc/images/fix.gif)[42849](https://bz.apache.org/bugzilla/show_bug.cgi?id=42849): Refuse to operate with IIS in case the initialization failed. Instead requesting isapi_redirect.dll 500 will be returned to the user. This is as closest as it can get to Apache Httpd where we refuse to start the server in case of fatal initialization errors. (mturk) 
*   ![Image 125: Fix: ](https://tomcat.apache.org/connectors-doc/images/fix.gif) Load Balancer: Fix a deadlock in lb worker, which was exposed on Solaris for threaded Apache MPMs. (rjung) 
*   ![Image 126: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) Logging: handle LWP IDs as 32 Bit unsigned. Try to make it work, although pthread IDs are opaque. (rjung) 
*   ![Image 127: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) JkStatus: Added manipulation of max_reply_timeouts. (rjung) 
*   ![Image 128: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) LB, Status: Add feature max_reply_timeouts, to make lb tolerant against occasional long running requests. (rjung) 
*   ![Image 129: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) JkStatus: Added OK/IDLE as the successor of N/A. (rjung) 
*   ![Image 130: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) Status worker: Renamed runtime states. All states have a major state (OK or ERR) and a substate. Changed the name N/A to OK/IDLE. Added docs about the meaning of the states to the status worker page in the reference guide. No new states have been added to code. (rjung) 
*   ![Image 131: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) Common: Add recovery options for recovering idempotent http methods HEAD and GET. (rjung) 
*   ![Image 132: Fix: ](https://tomcat.apache.org/connectors-doc/images/fix.gif) Correct documentation for worker attributes retries and recovery_options. (rjung) 
*   ![Image 133: Fix: ](https://tomcat.apache.org/connectors-doc/images/fix.gif) Make writing log lines and line endings more atomic. (rjung) 
*   ![Image 134: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) Common: Refactored and unified jk_map_read_prop* and jk_map_load_prop* for all use cases. (rjung) 
*   ![Image 135: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) Common/Apache/IIS/Netscape: Add an option to check decoded URLs for potentially malicious constructions. (rjung) 
*   ![Image 136: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) IIS: Document auth_complete and uri_select. (rjung) 
*   ![Image 137: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) Apache/IIS/Netscape: Change the default forwarding encoding to the new proxy method. (jfclere, rjung) 
*   ![Image 138: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) Common: Optionally reencode URIs before forwarding to the backend. Based on the URI reencoding done bei httpd mod_proxy. (jfclere, rjung) 
*   ![Image 139: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) Common: auto-detect correct print format for pid_t. This fixes at least compiler warnings on Solaris. (rjung) 
*   ![Image 140: Fix: ](https://tomcat.apache.org/connectors-doc/images/fix.gif)[42608](https://bz.apache.org/bugzilla/show_bug.cgi?id=42608): Handle Content-length as unsigned 64Bit to allow for huge up- and downloads. (rjung) 
*   ![Image 141: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) Apache: Add forwarding uri to debug log. (rjung) 
*   ![Image 142: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) Docs: Clarify relation between worker names and jvmRoute for load balancing. (rjung) 
*   ![Image 143: Fix: ](https://tomcat.apache.org/connectors-doc/images/fix.gif) Use initial zero timeout for jk_is_socket_connected. The resulting detection is the same but offers a huge performance increase with mod_jk. In most cases the Operating System does not favor the 1 microsecond timeout, but it rather rounds that up to much higher value (frequency of interrupt timer which on most systems defaults to 100Hz). Patch provided by David McLaughlin. (mturk) 
*   ![Image 144: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) NSAPI: Check correct log file and shm file configuration during startup. (rjung) 
*   ![Image 145: Fix: ](https://tomcat.apache.org/connectors-doc/images/fix.gif) NSAPI: Add support for the general options concerning retries, flushing and connection persistance. (rjung) 
*   ![Image 146: Fix: ](https://tomcat.apache.org/connectors-doc/images/fix.gif) NSAPI: fix crashes due to use of mount attribute in workers.properties. Changed initialization order. (rjung) 
*   ![Image 147: Fix: ](https://tomcat.apache.org/connectors-doc/images/fix.gif) Improved handling of libtool and discrepancies between CC env variable and CC used during apache build by configure script. (rjung) 
*   ![Image 148: Fix: ](https://tomcat.apache.org/connectors-doc/images/fix.gif) Always build with thread support, unless flag --enable-prefork is set during for configure. (rjung) 
*   ![Image 149: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) Use snprintf/vsnprintf from ap_snprintf.c for platforms other than Windows, which might lack snprintf/vsnprintf implementations when NOT build for Apache httpd 2.x/APR (e.g. Sub Web Server) or without using configure. (fuankg) 
*   ![Image 150: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) Imported ap_snprintf() from Apache 1.3. (fuankg) 
*   ![Image 151: Fix: ](https://tomcat.apache.org/connectors-doc/images/fix.gif) Fix incorrect log object cleanup during statup, leading to crashes at least on iSeries. (rjung) 
*   ![Image 152: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) Add jk_stat() and jk_file_exists() as wrapper functions. i5/OS V5R4 expects filename in ASCII for fopen but requires them in EBCDIC for stat(). (hgomez) 
*   ![Image 153: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) i5/OS (AS/400) V5R4 port where Apache 2.0 modules should now use UTF8. (hgomez) 
*   ![Image 154: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) Docs: Add comments on i5/OS build for V5R4 and previous releases. (hgomez) 

### Changes between 1.2.22 and 1.2.23

#### Native

*   ![Image 155: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) [[**CVE-2007-0450**](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2007-0450)] and [[**CVE-2007-1860**](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2007-1860)]: Change the default value of JkOptions to ForwardURICompatUnparsed. The old default value was ForwardURICompat. This should make URL interpretation between Apache httpd and Tomcat consistent (prevent double decoding problems). (rjung) 

### Changes between 1.2.21 and 1.2.22

### Changes between 1.2.20 and 1.2.21

### Changes between 1.2.19 and 1.2.20

#### Native

*   ![Image 156: Add: ](https://tomcat.apache.org/connectors-doc/images/add.gif) JkStatus Ant Task documentation page. (pero/rjung) 
*   ![Image 157: Add: ](https://tomcat.apache.org/connectors-doc/images/add.gif) JkStatus Ant Tasks: Add new tasks for update and reset. (pero) 
*   ![Image 158: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) JkStatus Ant Tasks: Update for new xml status format. (pero) 
*   ![Image 159: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) Allow integer and string values when setting enumeration/boolean attributes via status worker update action. (rjung) 
*   ![Image 160: Add: ](https://tomcat.apache.org/connectors-doc/images/add.gif) Docs: New reference guide page for status worker. (rjung) 
*   ![Image 161: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) Docs: Renaming the config dir to reference and using the title Reference Guide in the docs. (rjung) 
*   ![Image 162: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) Added retry_on_status for workers directive. (mturk) 
*   ![Image 163: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) Status Worker: Add directive to make property prefix and good/bad rule configurable. (rjung) 
*   ![Image 164: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) Status Worker: Omit lb members when att=nosw. (rjung) 
*   ![Image 165: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) Status Worker: New command cmd=version for a short version output. (rjung) 
*   ![Image 166: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) Status Worker: New output stype mime=prop produces property lists. (rjung) 
*   ![Image 167: Fix: ](https://tomcat.apache.org/connectors-doc/images/fix.gif) Apache: Fix incorrect handling of JkEnvVar when Vars are set multiple times. (rjung) 
*   ![Image 168: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) Renamed jvm_route to route. Deprecated jvm_route, but still use it as fallback when parsing the worker configuration. (rjung) 
*   ![Image 169: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) IIS: Make uriworkermap file reload check interval configurable. (mturk) 
*   ![Image 170: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) Apache: Make uriworkermap file reload check interval configurable. (rjung) 
*   ![Image 171: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) Status Worker: Add directives for customizing the XML output (ns, xmlns, doctype). (mturk) 
*   ![Image 172: Add: ](https://tomcat.apache.org/connectors-doc/images/add.gif) Docs: New page with description of uriworkermap. (rjung) 
*   ![Image 173: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) Docs: Added short description of max_packet_size to worker reference. (rjung) 
*   ![Image 174: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) Status Worker: All functions accessible also for xml and txt mime types (list, show, update, reset). (rjung) 
*   ![Image 175: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) Status Worker: New global health indicators for load balancers named bad (error, recovering or stopped), degraded (busy or disabled) and good (the rest, active and OK or N/A). (rjung) 
*   ![Image 176: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) Status Worker: New edit page, to change one attribute for all members of a load balancer. (rjung) 
*   ![Image 177: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) Status Worker: Standard logging for status worker. (rjung) 
*   ![Image 178: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) Status Worker: code refactoring. (rjung) 
*   ![Image 179: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) Status Worker: New attribute user (list) denies access, if the request user in the sense of remote_user is not in this list. Empty list = no deny (rjung) 
*   ![Image 180: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) Status Worker: New attribute read_only disables the parts of the status worker, that change states and configurations. (rjung) 
*   ![Image 181: Fix: ](https://tomcat.apache.org/connectors-doc/images/fix.gif)[36121](https://bz.apache.org/bugzilla/show_bug.cgi?id=36121): Don't change main uri when mod_jk serves included uri. (markt) 
*   ![Image 182: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) Apache VHosts: Merge JkOptions +base - -base + +vhost - -vhost. (rjung) 
*   ![Image 183: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) Apache Docs: Adding requirements, context information, default values and inheritance rules to the Apache config documentation. (rjung) 
*   ![Image 184: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) Status Worker: Add source type to status worker, remove the redundant "context" column in the map listing (context=uri). (rjung) 
*   ![Image 185: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) uriworkermap: On reload of the file, all old entries from the previous file version get deleted, before the new ones are being read. (rjung) 
*   ![Image 186: Fix: ](https://tomcat.apache.org/connectors-doc/images/fix.gif) Keep normal maps and exclusion maps internally separate. Don't treat them as the same when adding a rule. (rjung) 
*   ![Image 187: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) Status Worker: Display mapping rules also for non-lb workers and in global view. (rjung) 
*   ![Image 188: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) Apache VHosts: Use the vhost log files instead of the main log. (rjung) 
*   ![Image 189: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) Apache VHosts: Allow individual timestamp formats by refactoring the formatting method. (rjung) 
*   ![Image 190: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) Apache VHosts: Adding all missing config items to the virtual host level. Don't overwrite the settings from the global server, but inherit them in case they are not set in the virtual host. (rjung) 
*   ![Image 191: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) Apache: remove unnecessary function names from log messages. (rjung) 
*   ![Image 192: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) Apache: add a default log file location and a message, if the default gets used. (rjung) 
*   ![Image 193: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) Apache: add missing JK_IS_DEBUG_LEVEL() (rjung) 
*   ![Image 194: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) Apache VHosts: Allow JkWorkersFile, JKWorkerProperty, JkShmFile and JkShmFileSize only in global virtual server. (rjung) 
*   ![Image 195: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) Add some more jk_close_socket() and reduce log level for some info messages. (rjung) 
*   ![Image 196: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) Load Balancer: Added the Sessions strategy. Contributed by Takayuki Kaneko. (rjung) 
*   ![Image 197: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) Docs: Minor enhancements and syncing with more recent versions. (rjung) 
*   ![Image 198: Fix: ](https://tomcat.apache.org/connectors-doc/images/fix.gif)[40997](https://bz.apache.org/bugzilla/show_bug.cgi?id=40997): Separate uri mappings from their '!' counterpart when checking for duplicates in uriworkermap reloading. (rjung) 
*   ![Image 199: Fix: ](https://tomcat.apache.org/connectors-doc/images/fix.gif)[40877](https://bz.apache.org/bugzilla/show_bug.cgi?id=40877): Make sure the shared memory is reset on attach for multiple web server child processes. (mturk) 
*   ![Image 200: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) IIS: Added shm_size property to be able to deal with over 64 workers configurations. (mturk) 
*   ![Image 201: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) IIS: Increase default thread count to 250, so its the same as Apache Httpd default configuration. (mturk) 
*   ![Image 202: Fix: ](https://tomcat.apache.org/connectors-doc/images/fix.gif)[40966](https://bz.apache.org/bugzilla/show_bug.cgi?id=40966): Fix socket descriptor checks on windows. (mturk) 
*   ![Image 203: Fix: ](https://tomcat.apache.org/connectors-doc/images/fix.gif)[40965](https://bz.apache.org/bugzilla/show_bug.cgi?id=40965): Initialize missing service parameters. (mturk) 
*   ![Image 204: Fix: ](https://tomcat.apache.org/connectors-doc/images/fix.gif)[40938](https://bz.apache.org/bugzilla/show_bug.cgi?id=40938): Fix releasing of rewrite map. Thanks to Chris Adams for spotting that. (mturk) 
*   ![Image 205: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) Apache: Added +FlushHeader JkOptions. (mturk) 
*   ![Image 206: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) Added explicit flush when AJP body packet size is zero. (mturk) 
*   ![Image 207: Fix: ](https://tomcat.apache.org/connectors-doc/images/fix.gif)[40856](https://bz.apache.org/bugzilla/show_bug.cgi?id=40856): Fixing case sensitivity bug in URL mapping. (rjung) 
*   ![Image 208: Fix: ](https://tomcat.apache.org/connectors-doc/images/fix.gif)[40793](https://bz.apache.org/bugzilla/show_bug.cgi?id=40793): Documentation: Improvements to Apache HowTo provided by Paul Charles Leddy. (markt) 
*   ![Image 209: Fix: ](https://tomcat.apache.org/connectors-doc/images/fix.gif)[40774](https://bz.apache.org/bugzilla/show_bug.cgi?id=40774): Fixing wrong recursion termination. This one restricted the "reference" feature unintentionally to 20 workers. (rjung) 
*   ![Image 210: Fix: ](https://tomcat.apache.org/connectors-doc/images/fix.gif)[40716](https://bz.apache.org/bugzilla/show_bug.cgi?id=40716): Adding "reference" feature to IIS and Netscape. (rjung) 
*   ![Image 211: Fix: ](https://tomcat.apache.org/connectors-doc/images/fix.gif) Documentation: Corrected SetEnvIf syntax in JK_WORKER_NAME example. (rjung) 
*   ![Image 212: Fix: ](https://tomcat.apache.org/connectors-doc/images/fix.gif) Documentation: Added forgotten STATE and ACTIVATION notes for load balancer logging in Apache. (rjung) 
*   ![Image 213: Update: ](https://tomcat.apache.org/connectors-doc/images/update.gif) Apache: Use instdso.sh instead libtool: libtool does not work on HP-UX for example. (jfclere) 

### Changes between 1.2.18 and 1.2.19

### Changes between 1.2.17 and 1.2.18

### Changes between 1.2.16 and JK 1.2.17

### Changes between 1.2.15 and JK 1.2.16

### Changes between 1.2.14 and 1.2.15

### Changes between 1.2.13 and 1.2.14

### Changes between 1.2.12 and 1.2.13

### Changes between 1.2.11 and 1.2.12

### Changes between 1.2.10 and 1.2.11

### Changes between 1.2.8 and 1.2.10

### Changes between 1.2.7 and 1.2.8

### Changes between 1.2.6 and 1.2.7

### Changes between 1.2.5 and 1.2.6

### Changes between 1.2.4 and 1.2.5

### Changes between 1.2.3 and 1.2.4

### Changes between 1.2.2 and 1.2.3

### Changes between 1.2.1 and 1.2.2

### Changes between 1.2.0 and 1.2.1

### JK 2

JK2 has been put in maintainer mode and no further development will take place. The reason for shutting down JK2 development was the lack of developers interest. Other reason was lack of users interest in adopting JK2, caused by configuration complexity when compared to JK.
