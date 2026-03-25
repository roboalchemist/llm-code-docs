# Source: https://docs.pentaho.com/pdc-get-started/pdc-get-started-get-started-cp/pdc-data-profiling-and-data-identification.md

# Data profiling and data identification

After you select the data you want to analyze, you must profile it and run the data identification process to tag the data. See the topics below and **Processing Data** in the **User Guide** for more information on profiling and data identification.

## Data profiling

Data Catalog supports various file formats like Avro, ORC (Optimized Row Columnar), Parquet, CSV (Comma Separated Values), TSV (Tab Separated Values), XLS, and XLSX files, while profiling the structured data. The data profiling process generates statistical and intermediate data that is required by other data analytics processes. The intermediate data is consumed by downstream processes such as data flow and foreign key detection.

The intermediate data generated for each column of data includes:

* **Roaring Bitset**: A bitmap of the hash values for all entries in the column.
* **HyperLogLog (HLL)**: Provides an estimate of the cardinality of the data, with a roughly \~2% margin of error.
* **Data Pattern Analysis**: Performs a rudimentary data pattern analysis using dimensional reduction, tracking the most frequently occurring patterns.
* **Data Quality Pre-Analysis**: Using the Data Pattern Analysis results, Data Catalog performs a statistical estimation of the data quality. This is summarized as an overall percentage as well as a heat map for each data pattern. Additionally, Data Catalog makes RegEx recommendations for the most probable matches.
* **Statistics**: Data Catalog gathers the following statistics when examining all the data:
  * Minimum and Maximum values (for numeric columns)
  * Widest and Narrowest (non-null) string widths
  * Null count
  * Total row count
* **Data Sampling**: Data Catalog takes a controlled sampling of the data so that the samples are consistently chosen across different columns.

## Data identification

The data identification process uses dictionaries and data pattern analysis to automatically classify data, applying tags defined in dictionary and pattern configuration files. In addition to the dictionaries and patterns included with Data Catalog, you can create your own dictionaries and pattern analysis configuration files to better suit your organization's needs.

You can use the data patterns to help identify (or to disqualify) data of a certain type.

### Data pattern analysis

Fundamental to data quality analysis is either the use of a regular expression to check data, or to statistically analyze the data itself to find patterns and outlier patterns (which could indicate bad data).

The data identification process generates roughly the top 20 most common patterns which capture the characteristics of the data. You can then use these patterns, along with their statistical frequency and supplementary information, to generate regular expression (RegEx) recommendations for your data. You can tune the RegEx to meet your specific needs. Or you can select the valid patterns, so that subsequent data quality checks will identify any data entries that are outside the accepted patterns.

After running data identification, you can use the Galaxy View feature to visualize the data tagging, identify the data flow, locate your data, and view the sensitivity and security of that data.
