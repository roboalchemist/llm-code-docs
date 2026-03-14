# Source: https://www.hammerdb.com/docs4.0/ch03s06.html

Title: 6. TPROC-C key similarities and differences from TPC-C

URL Source: https://www.hammerdb.com/docs4.0/ch03s06.html

Markdown Content:
HammerDB can be seen as a subset of the the full TPC-C specification, intentionally modified to make the workload simpler and easier to run. The key similarities are the schema definition and data and the 5 transactions implemented as stored procedures. The key difference is that by default HammerDB will run without keying and thinking time enabled (Note enabling event driven scaling will enable keying and thinking time to be run with a large number of user sessions). This means that HammerDB TPROC-C will run a CPU and memory intensive version of the TPC-C workload. In turn this also means that the number of virtual users and the required data set will be much smaller than a full TPC-C implementation to reach maximum levels of performance. HammerDB also does not implement terminals as the full specification does. Nevertheless with the HammerDB TPROC-C implementation a large number of client systems and third-party middleware is not required nor a very large data set to reach maximum levels of performance whilst still providing a robust test of relational databases capabilities.
