# Source: https://www.hammerdb.com/docs4.0/ch01s08.html

Title: 8. Verifying the Installation of Database Client Libraries

URL Source: https://www.hammerdb.com/docs4.0/ch01s08.html

Markdown Content:
For all of the databases that HammerDB supports it is necessary to have a third-party client library installed that HammerDB can use to connect and interact with the database. This client library will also typically be installed with database server software. HammerDB does not statically link the 3rd party libraries to minimise executable size and provide flexibility in the third-party libraries used. For example if a bug is detected in a particular library then this can be upgraded without requiring the HammerDB libraries to be rebuilt. However as the client libraries are dynamically linked it is essential that the correct client libraries are already installed and environment variables set to ensure that HammerDB can find the correct libraries. Note that it is only necessary to load the libraries for the database that your are testing.

The HammerDB command line tool can be used to check the status of library availability for all databases.

To run this utility run the following command

./hammerdbcli
and type librarycheck.

HammerDB CLI v4.0
Copyright (C) 2003-2020 Steve Shaw
Type "help" for a list of commands
The xml is well-formed, applying configuration
hammerdb>librarycheck
Checking database library for Oracle
Success ... loaded library Oratcl for Oracle
Checking database library for MSSQLServer
Success ... loaded library tdbc::odbc for MSSQLServer
Checking database library for Db2
Success ... loaded library db2tcl for Db2
Checking database library for MySQL
Success ... loaded library mysqltcl for MySQL
Checking database library for PostgreSQL
Success ... loaded library Pgtcl for PostgreSQL

hammerdb>

in the example it can be seen that the libraries for all databases were found and loaded. The following table illustrates the first level library that HammerDB requires however there may be additional dependencies. Refer to the Test Matrix to determine which database versions HammerDB was built against. On Windows the [Dependency Walker Utility](https://dependencywalker.com/) can be used to determine the dependencies and on Linux the command ldd.

For example on Windows use dependency walker to open the HammerDB library for your chosen database. In the following example libmysqltcl.dll is opened for MySQL. This shows that the key dependency is on the 64-bit libmysql.dll.

**Figure 1.11.Dependency Walker MySQL**

![Image 1: Dependency Walker MySQL](https://www.hammerdb.com/docs4.0/resources/ch1-13.PNG)

Right-clicking on this library shows the properties including where it was found.

**Figure 1.12.LIBMYSQL.DLL Properties**

![Image 2: LIBMYSQL.DLL Properties](https://www.hammerdb.com/docs4.0/resources/ch1-14.PNG)

This location was set in the Environment variables under the Path option.

**Figure 1.13.Environment Variables**

![Image 3: Environment Variables](https://www.hammerdb.com/docs4.0/resources/ch1-15.PNG)

As shown below hammerDB found the correct MySQL 8.0 library because the path to the 64-bit MySQL 8.0 library was set correctly in the environment variables.

**Figure 1.14.Path environment variable**

![Image 4: Path environment variable](https://www.hammerdb.com/docs4.0/resources/ch1-16.PNG)

On Linux we run a similar test with librarycheck, however in this instance the library file is not found, although note that it identifies the file that is missing as libmysqlclient.so.21.

Checking database library for MySQL
Error: failed to load mysqltcl - couldn't load file "/home/steve/HammerDB-4.0/lib/mysqltcl-3.052/libmysqltcl3.052.so": libmysqlclient.so.21: cannot open shared object file: No such file or directory
Ensure that MySQL client libraries are installed and the location in the LD_LIBRARY_PATH environment variable

We can investigate further using the ldd command in an equivalent way to dependency walker on Windows. This also identifies the file that is missing.

$ ldd libmysqltcl3.052.so 
linux-vdso.so.1 (0x00007ffc44f7d000)
**libmysqlclient.so.21 => not found**
libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f33e73e7000)
/lib64/ld-linux-x86-64.so.2 (0x00007f33e79e2000)

Checking in our MySQL installation we can find the file libmysqlclient.so.21.

$ pwd
/opt/mysql-8.0.18-linux-glibc2.12-x86_64/lib
$ ls libmysqlclient*
libmysqlclient.a  libmysqlclient.so  libmysqlclient.so.21  libmysqlclient.so.21.1.18

Therefore we know that the file is installed, however we need to tell HammerDB where to find it. This is done by adding the MySQL library to the LD_LIBRARY_PATH.

$ export LD_LIBRARY_PATH=/opt/mysql-8.0.18-linux-glibc2.12-x86_64/lib:$LD_LIBRARY_PATH
Reversing our steps we can see that the library is now found.

$ ldd libmysqltcl3.052.so 
linux-vdso.so.1 (0x00007fff7f7e6000)
libmysqlclient.so.21 => /opt/mysql-8.0.18-linux-glibc2.12-x86_64/lib/libmysqlclient.so.21 (0x00007f92b0153000)
libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f92afd62000)
libpthread.so.0 => /lib/x86_64-linux-gnu/libpthread.so.0 (0x00007f92afb43000)
libdl.so.2 => /lib/x86_64-linux-gnu/libdl.so.2 (0x00007f92af93f000)
libssl.so.1.1 => /opt/mysql-8.0.18-linux-glibc2.12-x86_64/lib/libssl.so.1.1 (0x00007f92af6b5000)
libcrypto.so.1.1 => /opt/mysql-8.0.18-linux-glibc2.12-x86_64/lib/libcrypto.so.1.1 (0x00007f92af270000)
librt.so.1 => /lib/x86_64-linux-gnu/librt.so.1 (0x00007f92af068000)
libstdc++.so.6 => /usr/lib/x86_64-linux-gnu/libstdc++.so.6 (0x00007f92aecdf000)
libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007f92ae941000)
libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1 (0x00007f92ae729000)
/lib64/ld-linux-x86-64.so.2 (0x00007f92b0c34000)
and library check confirms that it can be loaded.

Checking database library for MySQL
Success ... loaded library mysqltcl for MySQL
Add the export command to the .bash_profile ensures that it will be found each time HammerDB is launched from a new shell.

The following table shows the libraries that are required for each database version. All libraries are 64-bit. Note that some databases are considerably more flexible in library versions and therefore the following section is important to ensure that you install the correct library for your needs.

**Table 1.3.3rd party libraries**

| Database / OS | Library |
| --- | --- |
| Oracle Linux | libclntsh.so |
| Oracle Windows | OCI.DLL |
| SQL Server Linux | libodbc.so |
| SQL Server Windows | ODBC32.DLL |
| Db2 Linux | libdb2.so |
| Db2 Windows | DB2CLI64.DLL |
| MySQL Linux | libmysqlclient.so |
| MySQL Windows | LIBMYSQL.DLL |
| PostgreSQL Linux | libpq.so |
| PostgreSQL Windows | LIBPQ.DLL |

### [](https://www.hammerdb.com/docs4.0/ch01s08.html)8.1.Oracle Client

When using the Oracle instant client Oratcl uses the additional environment variable ORACLE_LIBRARY to identify the Oracle client library. On the Windows the Oracle client library is called oci.dll in a location such as: C:\oraclexe\app\oracle\product\11.2.0\server\bin. On Linux the library is called libclntsh.so where this is typically a symbolic link to a product specific name such as libclntsh.so.12.1 for Oracle 12c. An example .bash_profile file is shown for a typical Oracle environment.

oracle@server1  oracle]$ cat ~/.bash_profile
# .bash_profile

if [ -t 0 ]; then
stty intr ^C
fi

# Get the aliases and functions
if [ -f ~/.bashrc ]; then
        . ~/.bashrc
fi
# User specific environment and startup programs
umask 022
export ORACLE_BASE=/u01/app/oracle
export ORACLE_HOME=$ORACLE_BASE/product/12.1.0/dbhome_1
export LD_LIBRARY_PATH=$ORACLE_HOME/lib
export ORACLE_LIBRARY=$ORACLE_HOME/lib/libclntsh.so
export ORACLE_SID=PROD1
export PATH=$ORACLE_HOME/bin:$PATH

### [](https://www.hammerdb.com/docs4.0/ch01s08.html)8.2.SQL Server

On SQL Server on Windows the client libraries and necessary environment variables are set automatically during the SQL Server installation. Note that on 64-bit Windows the 64-bit ODBC client library is named ODBC32.DLL in the following location. C:\Windows\System32\odbc32.dll. On Linux follow the SQL Server on Linux installation guide to install 'mssql-tools' with the unixODBC developer package. The command database drivers will show the installed ODBC Driver.

hammerdb>database drivers
{{ODBC Driver 17 for SQL Server} {{Description=Microsoft ODBC Driver 17 for SQL Server} 
Driver=/opt/microsoft/msodbcsql/lib64/libmsodbcsql-17.0.so.1.1 UsageCount=1}}

### [](https://www.hammerdb.com/docs4.0/ch01s08.html)8.3.Db2

For DB2 on Linux the client library libdb2.so.1 is required either in the lib64 directory for 32. Similarly on Windows the db2cli64.dll is required. These libraries are included with a standard DB2 installation or also with a standalone DB2 client install.

### [](https://www.hammerdb.com/docs4.0/ch01s08.html)8.4.MySQL

HammerDB version 4.0 (and version 3.3) has been built and tested against a MySQL 8.0 client installation, hammerDB version 3.0-3.2 has been built against MySQL 5.7. On Linux this means that HammerDB will require a MySQL client library called libmysqlclient.so.21 for HammerDB version 4.0 and 3.3 and libmysqlclient.so.20 for version 3.2 and earlier. This client library needs to be referenced in the LD_LIBRARY_PATH as shown previously in this section. Note that for testing MariaDB you also need the libmysqlclient.so.21 from an installation of MySQL 8.0. You do not need to install MySQL 8.0 as the only file you need is "libmysqlclient.so.21". With this file installed and in the library path the HammerDB client can connect to MariaDB.

### [](https://www.hammerdb.com/docs4.0/ch01s08.html)8.5.PostgreSQL

For PostgreSQL the client library is called libpq.dll on Windows and libpq.so on Linux however note that additional libraries are also required. For Windows this means setting your PATH environment variable such as the following: D:\PostgreSQL\pgsql\bin; On Linux it is required to set the LD_LIBRARY_PATH environment variable in the same way described for Oracle previously in this section to the location of the PostgreSQL lib directory. Alternatively for installations of EnterpriseDB the client directory also contains the necessary files for a HammerDB installation.
