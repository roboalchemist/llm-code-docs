# Source: https://www.hammerdb.com/docs4.0/ch10.html

Title: Chapter 10. Web Service Interface (WS)

URL Source: https://www.hammerdb.com/docs4.0/ch10.html

Markdown Content:
In addition to the CLI there is a HTTP Web Service that provides the same commands as the CLI that can be accessed with a HTTP/REST client passing parameters and returning output in JSON format. The key difference from the configuration of the CLI is the addition of jobs. Under the web service output from schema builds or tests are stored in a SQLite database and retrieved at a later point using a job id. A rest interface has been provided in HammerDB for interacting with the web service using TCL, however this is not a necessity and although the examples in this section are given using TCL the web service can be driven with scripts written in any language. Additionally the huddle package has been provided for TCL to JSON formatting.
