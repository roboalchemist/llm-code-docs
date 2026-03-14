# Source: https://www.hammerdb.com/docs4.0/ch10s01.html

Title: 1. Web Service Configuration

URL Source: https://www.hammerdb.com/docs4.0/ch10s01.html

Markdown Content:
There are 2 configuration parameters for the webservice in the file generic.xml in the config directory, ws_port and sqlite_db. ws_port defines the port on which the service will run and sqlite_db defines the location of the SQLite database file. By default an in-memory location is used. Alternatively the name of a file can be given or "TMP" or "TEMP" for HammerDB to find a temporary directory to use for the file.

  <webservice>
   <ws_port>8080</ws_port> 
   <sqlite_db>:memory:</sqlite_db> 
  </webservice>
