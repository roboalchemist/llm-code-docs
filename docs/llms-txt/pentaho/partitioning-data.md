# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/partitioning-data.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/partitioning-data.md

# Partitioning data

Partitioning data allows you to distribute all the data from a set into distinct subsets according to the rule applied on a table or row, where these subsets form a partition of the original set with no item replicated into multiple groups.

Partitioning data is an important feature for scaling up and scaling out your [Pentaho Data Integration](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/broken-reference) transformations and jobs. Scaling up makes the most of a single server with multiple CPU cores, while scaling out maximizes the resources of multiple servers operating in parallel.
