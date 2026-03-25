# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/parquet-input/select-an-engine-parquet-input/using-parquet-input-on-spark-engine/general-parquet-input-spark/fields-parquet-input-spark-engine/using-get-fields-with-parquet-partitioned-datasets.md

# Using Get Fields with Parquet partitioned datasets

This section explains how to use **Get Fields** and partitioned Parquet files in a Parquet Input step running under AEL-Spark.

When partitioning by column is used with Parquet in a Hadoop cluster, the data is stored in the file system in a structure where additional sub-directories hold the Parquet files with data. The field used as the partitioning column, along with its corresponding values, is used as the sub-directory name and is not actually stored within the Parquet file.

For example, if you had a Parquet dataset named `/tmp/sales_parquet` that is partitioned by a field called `year`, the directory structure looks like this:

`/tmp/sales.parquet/year=2019`

`/tmp/sales.parquet/year=2020`

The Parquet files with the year data are stored inside these "`year=`" sub-directories. Since the directory name already contains the year field and its value, this data is not stored within each Parquet file. Because **Get Fields** reads an actual Parquet file and not a Parquet Hadoop directory structure using this partitioning convention, **Get Fields** cannot parse the data, in this case, a year value, that is contained in the partitioned sub-directories.

If you are using Parque with partitioned datasets, use one of the following methods to add fields to the table instead of **Get Fields**.

* Manually edit the XML in the `.ktr` file using any text editor and add the partitioned fields.
* Use **Get Fields** to read a different, temporary Parquet file with the same schema and fields, but without the partitioning. After the fields are added to the table using this temporary file, change the file path to the target dataset. You can generate this non-partitioned Parquet file by using the Spark Shell with the code snippet `spark.read.parquet("*/tmp/dataset.parquet*").limit(1).coalesce(1).write.parquet("/tmp/dataset_unpartitioned.parquet")` where `*/tmp/dataset.parquet*` is your partitioned dataset.
