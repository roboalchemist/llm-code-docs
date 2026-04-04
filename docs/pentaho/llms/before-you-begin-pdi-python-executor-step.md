# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/python-executor/before-you-begin-pdi-python-executor-step.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/python-executor/before-you-begin-pdi-python-executor-step.md

# Before you begin

Before using the Python Executor step, be aware of the following conditions.

You must install the following Python libraries before using the Python Executor step:

* [Pandas](http://pandas.pydata.org/) (1.5.3 or later) is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language. The pandas DataFrame along with the Series are the two parts of the pandas data structure, a flexible container for lower dimensional data. For example, DataFrame is a container for Series, and Series is a container for scalars. Ultimately, you want to be able to insert and remove objects from these containers in a dictionary-like fashion.
* [NumPy](http://www.numpy.org/) (1.24.2 or later) is a library for the Python programming language which adds both robust support for multi-dimensional arrays and matrices, and a large collection of high-level mathematical functions to operate on these arrays. A NumPy array is a table of values, all of the same type, which is indexed by a tuple of positive integers. NumPy arrays can be fast, easy to work with, providing users opportunities to perform calculations across entire arrays.
* [Py4J](https://www.py4j.org/) (0.10.9.7 or later) is a bridge between Python and Java, permitting Python programs running with a Python interpreter to dynamically access Java objects in a JVM. It also allows Java programs to access Python objects.
* [Matplotlib](https://matplotlib.org/)(3.7.1 or later) is a plotting library for Python and NumPy.

**Note:** If you install Python using the Anaconda distribution, all the required libraries will be installed.
