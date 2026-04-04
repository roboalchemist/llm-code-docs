# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/partitioning-data/use-partitioning.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/partitioning-data/use-partitioning.md

# Use partitioning

The partitioning method you use can be based on any criteria, can include no rule (round-robin row distribution), or can be created using a [partitioning method plugin](http://wiki.pentaho.com/display/EAI/PDI+Partition+Method+Plugin+Development). The idea is to establish a criterion by which to partition the data, so that resulting storage and processing groups are logically independent from each other.

* **Step 1: Set up the partition schema:**

  Perform the following actions:

  1. Configure a partition schema. A partition schema defines how many ways the row stream will be split. The names used for the partitions can be anything you like.
  2. Apply the partition schema to the Group By step. By applying a partition schema to a step, a matching set of step copies is started automatically (for example, if applying a partition schema with three partitions, three step copies are launched).
* **Step 2: Select the partitioning method:**

  Establish the partitioning method for the step, which defines the rule for row distribution across the copies. TheRemainder of division rule allows rows with the same state value to be sent to the same step copy and the distribution of similar rows among the steps. If the modulo is calculated on a non-integer value, the PDI client calculates the modulo on a checksum created from the String, Date, and Number value.

**Note:** When you run the transformation, there are no guarantees as to which page name goes to which step copy, only that any page name encountered is consistently forwarded to the same step copy.
