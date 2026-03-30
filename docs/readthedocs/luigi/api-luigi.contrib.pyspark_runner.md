# luigi.contrib.pyspark_runner

The pyspark program.

This module will be run by spark-submit for PySparkTask jobs.

The first argument is a path to the pickled instance of the PySparkTask,
other arguments are the ones returned by PySparkTask.app_options()

Classes

`AbstractPySparkRunner`(job, *args)

`PySparkRunner`(job, *args)

`PySparkSessionRunner`(job, *args)

`SparkContextEntryPoint`(conf)

`SparkSessionEntryPoint`(conf)

class luigi.contrib.pyspark_runner.SparkContextEntryPoint(*conf*)

sc = None

class luigi.contrib.pyspark_runner.SparkSessionEntryPoint(*conf*)

spark = None

class luigi.contrib.pyspark_runner.AbstractPySparkRunner(*job*, **args*)

run()

class luigi.contrib.pyspark_runner.PySparkRunner(*job*, **args*)

class luigi.contrib.pyspark_runner.PySparkSessionRunner(*job*, **args*)