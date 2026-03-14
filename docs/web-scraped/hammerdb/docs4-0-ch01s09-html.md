# Source: https://www.hammerdb.com/docs4.0/ch01s09.html

Title: 9. XML Configuration

URL Source: https://www.hammerdb.com/docs4.0/ch01s09.html

Markdown Content:
![Image 1: XML Configuration Files](https://www.hammerdb.com/docs4.0/resources/ch1-17.PNG)

By default the databases in the GUI menu are listed in the order that the workloads were added to HammerDB. If you wish to change the order to put a particular database first you can change the rdbms value in generic.xml to the name of the database of your choice. The name entry for a particular database can be found in the database.xml file. For example the following would set SQL Server to be the database at the top of the menu on startup.

<benchmark>
<rdbms>MSSQLServer</rdbms>
<bm>TPC-C</bm>
<first_result>NOPM</first_result>
</benchmark>
