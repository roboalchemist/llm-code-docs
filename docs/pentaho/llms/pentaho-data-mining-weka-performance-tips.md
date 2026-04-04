# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/optimize-the-pentaho-system/performance-tuning/pentaho-data-mining-weka-performance-tips.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/optimize-the-pentaho-system/performance-tuning/pentaho-data-mining-weka-performance-tips.md

# Pentaho data mining (Weka) performance tips

The most common Weka performance issue is the `OutOfMemory` exception.

This is caused by using resource-intensive algorithms with large data sources. To address this, refer to: [Increase the Memory Limit in Weka](https://docs.pentaho.com/pdia-admin/10.2-admin/optimize-the-pentaho-system/change-the-java-vm-memory-limits#weka)

Learning algorithms convert multi-valued discrete fields to binary indicator fields, thus potentially expanding the total number of fields. This sort of pre-processing can result in two copies of the data being held in main memory briefly until the transformation is complete. So even if you have enough memory to complete the task, it could take a while to perform. For this reason, you may need to run Weka on very fast multi-core, multi-CPU 64-bit machines if you are concerned with poor performance.

Beyond this, data mining tuning involves looking at each algorithm you're using and tweaking its parameters to improve the speed and accuracy of the results. This is always data- and algorithm-specific, and requires empirical experimentation. If you are running out of memory or experiencing poor performance, you might consider switching to an incrementally learning algorithm such as:

* Naive Bayes
* Naive Bayes multinomial
* DMNBtext
* AODE and AODEsr
* SPegasos
* SGD
* IB1, IBk and KStar
* Locally weighted learning
* RacedIncrementalLogitBoost
* Cobweb
