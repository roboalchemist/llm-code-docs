# Source: https://opentsdb.net/docs/build/html/api_telnet/index.html

Title: Telnet Style API — OpenTSDB 2.4 documentation

URL Source: https://opentsdb.net/docs/build/html/api_telnet/index.html

Markdown Content:
The original way of interacting with OpenTSDB was through a Telnet style API. A user or application simply had to open a socket to the TSD and start sending ASCII string commands and expect a response. This documentation lists the various commands provided by OpenTSDB.

Each command must be sent as a series of strings with a **new line** character terminating the request.

Note

Connections will be closed after a period of inactivity, typically 5 minutes.

If a command is sent to the API that is not supported or recognized, a response similar to the following will be shown:

unknown command: nosuchcommand.  Try `help'.

At any time the connection can be closed by issuing the `exit` command.

* [put](https://opentsdb.net/docs/build/html/api_telnet/put.html)
* [rollup](https://opentsdb.net/docs/build/html/api_telnet/rollup.html)
* [histogram](https://opentsdb.net/docs/build/html/api_telnet/histogram.html)
* [stats](https://opentsdb.net/docs/build/html/api_telnet/stats.html)
* [version](https://opentsdb.net/docs/build/html/api_telnet/version.html)
* [help](https://opentsdb.net/docs/build/html/api_telnet/help.html)
* [dropcaches](https://opentsdb.net/docs/build/html/api_telnet/dropcaches.html)
* [diediedie](https://opentsdb.net/docs/build/html/api_telnet/diediedie.html)
