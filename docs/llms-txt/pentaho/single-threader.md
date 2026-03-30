# Source: https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/single-threader.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/single-threader.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/single-threader.md

# Single Threader

The Single Threader step executes a sequence of steps in a single thread, which allows you to tune the performance of your transformations by limiting the number of threads or processors used:

* To solve issues in transformations with many steps by reducing the data passing and thread context switching overhead.
* To sort data rows in a specific time frame or by a specific number for real-time streaming.
* To process chunks of data, pause, and then continue processing after reaching the chunk size.

Related information: [White Paper on Single Threading in Pentaho Data Integration](http://www.ibridge.be/?p=200)
