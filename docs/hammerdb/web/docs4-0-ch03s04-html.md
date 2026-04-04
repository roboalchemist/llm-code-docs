# Source: https://www.hammerdb.com/docs4.0/ch03s04.html

Title: 4. Comparing HammerDB results

URL Source: https://www.hammerdb.com/docs4.0/ch03s04.html

Markdown Content:
HammerDB implements a workload called TPROC-C based on the TPC-C specification called TPROC-C however does NOT implement a full specification TPC-C benchmark and the transaction results from HammerDB cannot be compared with the official published TPC-C benchmarks in any manner. Official Audited TPC-C benchmarks are extremely costly, time consuming and complex to establish and maintain. The HammerDB implementation based on the specification of the TPC-C benchmark is designed to capture the essence of TPC-C in a form that can be run at low cost on any system bringing professional, reliable and predictable load testing to all database environments. For this reason HammerDB results cannot and should NOT be compared or used with the term tpmC in any circumstance. HammerDB workloads produce 2 statistics to compare systems called TPM and NOPM respectively. NOPM value is based on a metric captured from within the test schema itself. As such NOPM (New Orders per minute) as a performance metric independent of any particular database implementation is the recommended primary metric to use.
