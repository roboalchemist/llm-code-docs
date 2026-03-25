# Source: https://docs.pentaho.com/pdia-data-integration/pdi-job-entries-reference-overview/pentaho-mapreduce.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-job-entries-reference-overview/pentaho-mapreduce.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-job-entries-reference-overview/pentaho-mapreduce.md

# Pentaho MapReduce

This job entry executes transformations as part of a Hadoop MapReduce job in place of a traditional Hadoop Java class. A Hadoop MapReduce job is made up of any combination of following types of transformations:

* The Mapper transformation takes a set of data and converts it into another set of data, where individual elements are broken down into tuples (key/value pairs). It performs filtering and sorting (such as sorting students by first name into queues, one queue for each name). It applies a given function to each element of a list, returning a list of results in the same order.
* The Combiner transformation summarizes the map output records with the same key, which helps to reduce the amount of data written to disk, and transmitted over the network.
* The Reducer transformation performs a summary operation (such as counting the number of students in each queue, yielding name frequencies). It analyzes a recursive data structure and through use of a given combining operation, recombine the results of recursively processing its constituent parts, building up a return value.

**Note:** This entry was formerly known as Hadoop Transformation Job Executor.

With the Pentaho MapReduce entry, you specify PDI transformations to use for the mapper, combiner, and/or reducer through their related tabs. The mapper transformation is required. The combiner and reducer transformations are optional. See [Pentaho MapReduce workflow](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-job-entries-reference-overview/pentaho-mapreduce/use-pdi-outside-and-inside-the-hadoop-cluster/pentaho-mapreduce-workflow) for details on how PDI works with Hadoop clusters.

**Note:** The **Hadoop job name** field in the **Cluster** tab is required and must be specified for the Pentaho MapReduce entry to work.
