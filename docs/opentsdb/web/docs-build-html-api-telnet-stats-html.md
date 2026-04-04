# Source: https://opentsdb.net/docs/build/html/api_telnet/stats.html

Title: stats — OpenTSDB 2.4 documentation

URL Source: https://opentsdb.net/docs/build/html/api_telnet/stats.html

Markdown Content:
This command is similar to the HTTP [/api/stats](https://opentsdb.net/docs/build/html/api_http/stats/index.html) endpoint in that it will return a list of the TSD stats, one per line, in the `put` format. This command does not modify TSD in any way.

Request[¶](https://opentsdb.net/docs/build/html/api_telnet/stats.html#request "Permalink to this heading")
----------------------------------------------------------------------------------------------------------

The command format is:

stats

Response[¶](https://opentsdb.net/docs/build/html/api_telnet/stats.html#response "Permalink to this heading")
------------------------------------------------------------------------------------------------------------

A set of time series with data about the running TSD.

### Example[¶](https://opentsdb.net/docs/build/html/api_telnet/stats.html#example "Permalink to this heading")

tsd.hbase.rpcs 1479600574 0 type=increment host=web01
tsd.hbase.rpcs 1479600574 0 type=delete host=web01
tsd.hbase.rpcs 1479600574 1 type=get host=web01
tsd.hbase.rpcs 1479600574 0 type=put host=web01
tsd.hbase.rpcs 1479600574 0 type=append host=web01
tsd.hbase.rpcs 1479600574 0 type=rowLock host=web01
tsd.hbase.rpcs 1479600574 0 type=openScanner host=web01
tsd.hbase.rpcs 1479600574 0 type=scan host=web01
tsd.hbase.rpcs.batched 1479600574 0 host=web01
