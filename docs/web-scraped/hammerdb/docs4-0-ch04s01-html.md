# Source: https://www.hammerdb.com/docs4.0/ch04s01.html

Title: 1. Test Network Configuration

URL Source: https://www.hammerdb.com/docs4.0/ch04s01.html

Markdown Content:
You require the database server to be tested known as the system under test (SUT) installed and configured with the target database server. You also require a load generation server to run HammerDB installed with the HammerDB software and a database client. Typically the load generation server is run on a separate system from the SUT with the load generated across the network. It is possible to run HammerDB on the same system as the SUT however this will be expected to produce different results from a network based load. For example where the database software is highly scalable then running HammerDB on the same system will result in lower performance as the database software will not be able to take advantage of all of the available CPU. Conversely where the database software is less scalable and there is more network overhead it can take more virtual users to reach the same levels of performance using an additional load generation server compared to running HammerDB on the SUT. Both the SUT and the load generation server may be virtualized or container databases although similarly results may differ from a native hardware based installation. In all cases when comparing performance results you should ensure that you are comparing across the same configurations test network configurations.

### [](https://www.hammerdb.com/docs4.0/ch04s01.html)1.1.SUT Database Server Configuration

The database server architecture to be tested must meet the minimum requirements for your chosen database software, however to reach maximum performance it is likely that the specifications will considerably exceed these standard. To run a HammerDB transactional load test there are minimum requirements in memory and I/O (disk performance) to prevent these components being a bottleneck on performance. For a configuration requiring the minimal level of memory and I/O to maximize CPU utilization keying and thinking time should be set to FALSE (keying and thinking time is detailed later in this guide). To achieve this you should aim to create a schema with approximately 250-500 warehouses per CPU socket. By default each Virtual User will select a home warehouse at random and most of its work takes place on that home warehouse and therefore the schema sizing of 250-500 warehouses per socket should ensure that when the Virtual Users login the choice of a home warehouse at random is evenly distributed without a large number of Virtual Users selecting the same home warehouse. As long as it is not too small resulting in contention the schema size should not significantly impact results when testing in a default configuration. You should have sufficient memory to cache as much of your test schema in memory as possible. If keying and thinking time is set to TRUE you will need a significantly larger schema and number of virtual users to create a meaningful system load and should consider the advanced event-driven scaling option. Reductions in memory will place more emphasis on the I/O performance of the database containing the schema. If the allocated memory is sufficient most of the data will be cached during an OLTP test and I/O to the data area will be minimal. As a consequence the key I/O dependency will be to the redo/WAL/transaction logs for both bandwidth and sequential write latency. Modern PCIe SSDs when correctly configured have been shown to provide the capabilities to sustain high performance transaction logging.

### [](https://www.hammerdb.com/docs4.0/ch04s01.html)1.2.Load Generation Server Configuration

The most important component of the load generation server is the server processor. The overall load generation server capacity required depends on the system capabilities of the SUT. It is recommend to use an up to date multi-core processor. HammerDB is a multi-threaded application and implicitly benefits from a multi-core server CPU. To determine whether CPU capacity is sufficient for testing you can monitor the CPU utilisation with HammerDB Metrics. CPU utilisation reaching 100% is an indication that the CPU on the load generation server is limiting performance. Load generation memory requirements are dependent on the operating system configuration and the number of virtual users created with each virtual user requiring its own database client. Typically server sizing guidelines should be within the limits expected to support a real user count. Multiple load generation servers connected in a “master-slave” configuration are enabled within HammerDB to exceed the capacity of a single load generation client. The load generation server does not need to be running the same version of SQL Server as the SUT.

### [](https://www.hammerdb.com/docs4.0/ch04s01.html)1.3.CPU Single-Threaded Performance Calibration

By far one of the most common configuration errors with database performance testing is to have configured the CPUs to run in powersave mode. On some Linux operating systems this is the default configuration and therefore it is recommended to verify the CPU single-threaded performance and operating mode before running database workloads. One way to do this is to use the [Julian Dyke CPU performance test](http://www.juliandyke.com/CPUPerformance/CPUPerformance.php) (referenced by permission of Julian Dyke and there are versions shown below to run directly in HammerDB and for Oracle PL/SQL and SQL Server T-SQL). Note that the timings are not meant to equivalent and it is expected that the HammerDB based test is approximately twice as fast as PL/SQL or T-SQL. The reason for the faster performance is that the TCL version is compiled into bytecode and you can observe this by running a Linux utility such as perf to see that the top function is TEBCresume. (Tcl Execute ByteCode Resume). During normal HammerDB operations TEBCResume should also be the top function for the same reason.

Samples: 67K of event 'cycles:ppp', Event count (approx.): 33450114923
Overhead  Shared Object                  Symbol
**33.56% libtcl8.6.so [.] TEBCresume**
   7.68%  libtcl8.6.so                   [.] Tcl_GetDoubleFromObj
   6.28%  libtcl8.6.so                   [.] EvalObjvCore
   6.14%  libtcl8.6.so                   [.] TclNRRunCallbacks

The goal of running these tests is to ensure that your CPU runs the test at the CPU advertised boost frequency. To do this you can use the turbostat utility on Linux and the Task Manager utility on Windows. By default the tests run for 10000000 iterations however this can be extended if desired to allow sufficient time to monitor the boost frequency is operational. For the HammerDB version save the script shown and run it using the CLI. A commented out command is shown that can be uncommented to observe the bytecode for a particular procedure.

proc runcalc {} {
set n 0
for {set f 1} {$f <= 10000000} {incr f} {
set n [ expr {[::tcl::mathfunc::fmod $n 999999] + sqrt($f)} ] 
}
return $n
}
#puts "bytecode:[::tcl::unsupported::disassemble proc runcalc]"
set start [clock milliseconds]
set output [ runcalc ]
set end [ clock milliseconds]
set duration [expr {($end - $start)}]
puts "Res = [ format %.02f $output ]"
puts "Time elapsed : [ format %.03f [ expr $duration/1000.0 ] ]"
The expected result is 873729.72 as shown in the example output. Depending on the CPU used the default completion time should be up to 3 seconds, if longer then investigating the CPU configuration is recommended.

hammerdb>source CPUTEST.tcl
Res = 873729.72
Time elapsed : 2.990

hammerdb>source CPUTEST.tcl
Res = 873729.72
Time elapsed : 2.966

hammerdb>source CPUTEST.tcl
Res = 873729.72
Time elapsed : 2.980

hammerdb>source CPUTEST.tcl
Res = 873729.72
Time elapsed : 2.976

hammerdb>source CPUTEST.tcl
Res = 873729.72
Time elapsed : 2.972

hammerdb>source CPUTEST.tcl
Res = 873729.72
Time elapsed : 2.988

hammerdb>source CPUTEST.tcl
Res = 873729.72
Time elapsed : 2.976

The following listing shows the original Julian Dyke PL/SQL CPU test that can be run in an Oracle instance. Example timings are given at the website link above.

SET SERVEROUTPUT ON
SET TIMING ON
 
DECLARE
  n NUMBER := 0;
BEGIN
  FOR f IN 1..10000000
  LOOP
    n := MOD (n,999999) + SQRT (f);
  END LOOP;
  DBMS_OUTPUT.PUT_LINE ('Res = '||TO_CHAR (n,'999999.99'));
END;
/
The following listing shows the same routine in T-SQL for SQL Server.

USE [tpcc]
GO
SET ANSI_NULLS ON
GO
CREATE PROCEDURE [dbo].[CPUSIMPLE] 
AS
   BEGIN
      DECLARE
         @n numeric(16,6) = 0,
         @a DATETIME,
         @b DATETIME
      DECLARE
         @f int
      SET @f = 1
      SET @a = CURRENT_TIMESTAMP
      WHILE @f <= 10000000 
         BEGIN
      SET @n = @n % 999999 + sqrt(@f)
            SET @f = @f + 1
         END
         SET @b = CURRENT_TIMESTAMP
         PRINT ‘Timing = ‘ + ISNULL(CAST(DATEDIFF(MS, @a, @b)AS VARCHAR),”)
         PRINT ‘Res = ‘+ ISNULL(CAST(@n AS VARCHAR),”)
   END

### [](https://www.hammerdb.com/docs4.0/ch04s01.html)1.4.Administrator PC Configuration

When using the graphical version of HammerDB the administrator PC must have the minimal requirement to display the graphical output from the load generation server. The PC should also have the ability to connect to the SUT to monitor performance by the installation of an appropriate database client. For Linux clients where remote desktop displays are used it is recommended to use VNC instead of X Windows for better graphics performance in particular when using v4.0 SVG based scalable graphics. running X windows over long distances is known to impact display refresh rates and is not a HammerDB issue.
