# Source: https://opentsdb.net/docs/build/html/api_telnet/diediedie.html

Title: diediedie — OpenTSDB 2.4 documentation

URL Source: https://opentsdb.net/docs/build/html/api_telnet/diediedie.html

Markdown Content:
This command will cause the running TSD to shutdown and the process to exit. Please use carefully.

Warning

As stated, when this command executes, the TSD will shutdown. You’ll have to restart it manually, using a script, or use something like Daemontools or Runit.

Request[¶](https://opentsdb.net/docs/build/html/api_telnet/diediedie.html#request "Permalink to this heading")
--------------------------------------------------------------------------------------------------------------

The command format is:

diediedie

Response[¶](https://opentsdb.net/docs/build/html/api_telnet/diediedie.html#response "Permalink to this heading")
----------------------------------------------------------------------------------------------------------------

A response that it’s cleaning up and exiting.

### Example[¶](https://opentsdb.net/docs/build/html/api_telnet/diediedie.html#example "Permalink to this heading")

Cleaning up and exiting now.
