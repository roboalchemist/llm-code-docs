# Source: https://www.hammerdb.com/docs4.0/ch01s01.html

Title: 1. Release Notes

URL Source: https://www.hammerdb.com/docs4.0/ch01s01.html

Markdown Content:
The following are the release notes for HammerDB v4.0.

### [](https://www.hammerdb.com/docs4.0/ch01s01.html)1.1.Nomenclature Change

In the database.xml file and the User Interface the workload names have changed to TPROC-C and TPROC-H. This is a nomenclature change only to represent that the workloads are fair use implementations derived from the TPC specifications and the nomenclature does not change the functionality of the workload compared to prior versions using the TPC-C and TPC-H terminology.

### [](https://www.hammerdb.com/docs4.0/ch01s01.html)1.2.Stored Procedure Refactoring and Performance

At version 4.0 the stored procedures for the Oracle and PostgreSQL TPROC-C workloads have been refactored. This increases the expected performance between versions and consequently the performance from HammerDB v4.0 cannot be compared directly to the performance of v3.3 or previous releases. Additionally for some workloads HammerDB v4.0 changes the relationship between the NOPM and TPM metrics compared to previous versions. As a result of the stored procedure refactoring using bulk operations more work is processed per commit and therefore in these cases the NOPM has increased whilst the TPM remains the same. This indicates a real measure of increased throughput by doing more work per database transaction and consequently NOPM is now listed first as the primary metric in reporting output. However as raised in [HammerDB GitHub Issue #111](https://github.com/TPC-Council/HammerDB/issues/111) there may be cases where there is a dependency on the wording of the HammerDB log. For this reason a configuration option in the generic.xml file of first_result is given. If this option is set to NOPM then the v4.0 format is used if set to TPM then the output is compatible with v3.3.

<benchmark>
<rdbms>Oracle</rdbms>
<bm>TPC-C</bm>
**<first_result>NOPM</first_result>**
</benchmark>

### [](https://www.hammerdb.com/docs4.0/ch01s01.html)1.3.Redis Deprecated

The Redis workload has been deprecated and no longer features by default in the main HammerDB menu. In particular as a single-threaded database without support for stored procedures it was considered that Redis was not suitable for running workloads derived from the TPC specifications and could not reach similar levels of performance as the relational databases currently supported. Redis can still be enabled for unsupported use by uncommenting the Redis database entry in database.xml.

**<!--Redis deprecated, uncomment to enable as unsupported**
<redis>
<name>Redis</name>
<description>Redis</description>
<prefix>redis</prefix>
<library>redis</library>
<workloads>{TPROC-C}</workloads>
<commands>redis</commands>
</redis>
**-->**

### [](https://www.hammerdb.com/docs4.0/ch01s01.html)1.4.Known Third-Party Driver Issues

HammerDB has a dependency on 3rd party driver libraries to connect to the target databases. The following are known issues with some of the 3rd party drivers that HammerDB uses.

#### [](https://www.hammerdb.com/docs4.0/ch01s01.html)1.4.1.Oracle on Windows: Oracle Bug 12733000 OCIStmtRelease crashes or hangs if called after freeing the service context handle

If you are running HammerDB against Oracle on Windows there is long established bug in Oracle that can cause application crashes for multi-threaded applications on Windows.This bug can be investigated on the My Oracle Support website with the following reference. Bug 12733000 OCIStmtRelease crashes or hangs if called after freeing the service context handle. To resolve this Oracle issue add the following entry to the SQLNET.ORA file on your HammerDB client.

SQLNET.AUTHENTICATION_SERVICES = (NTS)
DIAG_ADR_ENABLED=OFF 
DIAG_SIGHANDLER_ENABLED=FALSE
DIAG_DDE_ENABLED=FALSE

#### [](https://www.hammerdb.com/docs4.0/ch01s01.html)1.4.2.SQL Server on Linux: unixODBC's handle validation may become a performance bottleneck

Using the HammerDB client for SQL Server on Linux can be slower than the same client on Windows when using the default installed unixODBC drivers on many Linux distributions. As described in the [SQL Server Programming Guidelines](https://docs.microsoft.com/en-us/sql/connect/odbc/linux-mac/programming-guidelines?view=sql-server-ver15) "_When using the driver with highly multithreaded applications, unixODBC's handle validation may become a performance bottleneck. In such scenarios, significantly more performance may be obtained by compiling unixODBC with the --enable-fastvalidate option. However, beware that this may cause applications which pass invalid handles to ODBC APIs to crash instead of returning SQL\_INVALID\_HANDLE errors._" Recompiling unixODBC with the --enable-fastvalidate option has been measured to improve client performance by 2X. Example configure options used to build unixODBC are shown as follows:

./configure --prefix=/usr/local/unixODBC --enable-gui=no --enable-drivers=no --enable-iconv 
--with-iconv-char-enc=UTF8 --with-iconv-ucode-enc=UTF16LE --enable-threads=yes **--enable-fastvalidate**

### [](https://www.hammerdb.com/docs4.0/ch01s01.html)1.5.Linux Font Pre-Installation Requirements

On Linux HammerDB requires the Xft FreeType-based font drawing library for X installed as follows:

Ubuntu:

$ sudo apt-get install libxft-dev
Red Hat:

$ yum install libXft
