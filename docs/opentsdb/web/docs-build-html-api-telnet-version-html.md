# Source: https://opentsdb.net/docs/build/html/api_telnet/version.html

Title: version — OpenTSDB 2.4 documentation

URL Source: https://opentsdb.net/docs/build/html/api_telnet/version.html

Markdown Content:
This command is similar to the HTTP [/api/version](https://opentsdb.net/docs/build/html/api_http/version.html) endpoint in that it will return information about the currently running version of OpenTSDB. This command does not modify TSD in any way.

Request[¶](https://opentsdb.net/docs/build/html/api_telnet/version.html#request "Permalink to this heading")
------------------------------------------------------------------------------------------------------------

The command format is:

version

Response[¶](https://opentsdb.net/docs/build/html/api_telnet/version.html#response "Permalink to this heading")
--------------------------------------------------------------------------------------------------------------

A set of lines with version information.

### Example[¶](https://opentsdb.net/docs/build/html/api_telnet/version.html#example "Permalink to this heading")

net.opentsdb.tools BuildData built at revision a7a0980 (MODIFIED)
Built on 2016/11/03 19:35:50 +0000 by clarsen@tsdvm:/Users/clarsen/Documents/opentsdb/opentsdb_dev
