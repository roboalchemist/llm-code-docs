# luigi.contrib.spark

Classes

`PySparkTask`(*args, **kwargs)

Template task for running an inline PySpark job

`SparkSubmitTask`(*args, **kwargs)

Template task for running a Spark job

class luigi.contrib.spark.SparkSubmitTask(**args*, ***kwargs*)

Template task for running a Spark job

Supports running jobs on Spark local, standalone, Mesos or Yarn

See http://spark.apache.org/docs/latest/submitting-applications.html
for more information

name = None

entry_class = None

app = None

always_log_stderr = False

stream_for_searching_tracking_url = 'stderr'

Used for defining which stream should be tracked for URL, may be set to ‘stdout’, ‘stderr’ or ‘none’.

Default value is ‘none’, so URL tracking is not performed.

property tracking_url_pattern

Class to parse optional parameters.

app_options()

Subclass this method to map your task parameters to the app’s arguments

property pyspark_python

property pyspark_driver_python

property hadoop_user_name

property spark_version

property spark_submit

property master

property deploy_mode

property jars

property packages

property py_files

property files

property conf

property properties_file

property driver_memory

property driver_java_options

property driver_library_path

property driver_class_path

property executor_memory

property driver_cores

property supervise

property total_executor_cores

property executor_cores

property queue

property num_executors

property archives

property hadoop_conf_dir

get_environment()

program_environment()

Override this method to control environment variables for the program

Returns:

dict mapping environment variable names to values

program_args()

Override this method to map your task parameters to the program arguments

Returns:

list to pass as `args` to `subprocess.Popen`

spark_command()

app_command()

class luigi.contrib.spark.PySparkTask(**args*, ***kwargs*)

Template task for running an inline PySpark job

Simply implement the `main` method in your subclass

You can optionally define package names to be distributed to the cluster
with `py_packages` (uses luigi’s global py-packages configuration by default)

app = '/home/docs/checkouts/readthedocs.org/user_builds/luigi/checkouts/latest/luigi/contrib/pyspark_runner.py'

property name

The type of the None singleton.

property py_packages

property files

property pickle_protocol

setup(*conf*)

Called by the pyspark_runner with a SparkConf instance that will be used to instantiate the SparkContext

Parameters:

**conf** – SparkConf

setup_remote(*sc*)

main(*sc*, **args*)

Called by the pyspark_runner with a SparkContext and any arguments returned by `app_options()`

Parameters:

- 

**sc** – SparkContext

- 

**args** – arguments list

app_command()

run()

The task run method, to be overridden in a subclass.

See Task.run