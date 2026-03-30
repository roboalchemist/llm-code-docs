# Source: https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/python-executor.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/python-executor.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/python-executor.md

# Python Executor

The Python Executor step leverages the [Python](https://www.python.org/) programming language as part of the data integration pipeline from within PDI. This step helps developers and data scientists take advantage of the strengths of the Python's versatile programming language to develop predictive solutions using existing PDI steps. Instead of writing code to connect to relational databases and Hadoop file systems, and to join and filter data, PDI allows the developer to focus their coding efforts on the data science-driven algorithms.

This step offers several options for execution. You can choose to map upstream data from a PDI input step to generate data or have the Python script generate its own data. You can opt to send all rows to Python at once, or send rows one-by-one.

When you deliver the input row-by-row, the field values of each incoming row are mapped to separate variables containing built-in types, such as numerics, strings, and Booleans. You set the names of these field values which are then available within the Python script.

When you send all rows, the data sent is considered a dataset. Python stores the dataset in a user-specified variable that kicks off your user-defined Python script. You can use the pandas DataFrame, a NumPy array, or the Python list of dictionaries as the data structure for datasets transferred into Python.

**Note:** This step only supports the CPython runtime.
