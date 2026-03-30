# Source: https://www.hammerdb.com/docs4.0/ch03s02.html

Title: 2. What is the TPC and the TPROC-C workload derived from TPC-C?

URL Source: https://www.hammerdb.com/docs4.0/ch03s02.html

Markdown Content:
Designing and implementing a database benchmark is a significant challenge. Many performance tests and tools experience difficulties in comparing system performance especially in the area of scalability, the ability of a test conducted on a certain system and schema size to be comparable with a test on a larger scale system. When system vendors wish to publish validated benchmark information about database performance they have needed to access sophisticated test specifications and the TPC is the industry body most widely recognized for defining benchmarks. TPC specifications are the only published benchmarks in the database industry recognized by all of the leading database vendors. TPC-C is the benchmark published by the TPC for Online Transaction Processing and you can view the published TPC-C results at the TPC website.

The TPC Policies allow for derivations of TPC Benchmark Standards that comply with the TPC Fair Use rules. TPROC-C is the OLTP workload implemented in HammerDB derived from the TPC-C specification with modification to make running HammerDB straightforward and cost-effective on any of the supported database environments. The HammerDB TPROC-C workload is an open source workload derived from the TPC-C Benchmark Standard and as such is not comparable to published TPC-C results, as the results comply with a subset rather than the full TPC-C Benchmark Standard. The name for the HammerDB workload TPROC-C means "Transaction Processing Benchmark derived from the TPC "C" specification".
