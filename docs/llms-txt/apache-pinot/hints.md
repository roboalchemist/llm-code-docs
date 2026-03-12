# Source: https://docs.pinot.apache.org/release-1.3.0/for-users/user-guide-query/multi-stage-query/hints.md

# Source: https://docs.pinot.apache.org/release-1.4.0/for-users/user-guide-query/multi-stage-query/hints.md

# Source: https://docs.pinot.apache.org/users/user-guide-query/multi-stage-query/hints.md

# Hints

Multi-stage query engine behavior can be customized with hints. Hints are provided as a comment, for example `/* hintType(hint1='value1',hint2='value2') */`.

Apache Pinot supports the following hints:

* `aggOptions`, explained in [aggregate operator](https://docs.pinot.apache.org/users/user-guide-query/operator-types/aggregate#hints).
* `windowOptions`, explained in [window operator](https://docs.pinot.apache.org/users/user-guide-query/operator-types/window#hints).
* `joinOptions`, explained in [join operator](https://docs.pinot.apache.org/users/user-guide-query/operator-types/hash_join#hints).
