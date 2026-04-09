# luigi.contrib.hadoop_jar

Provides functionality to run a Hadoop job using a Jar

Functions

`fix_paths`(job)

Coerce input arguments to use temporary files when used for output.

Classes

`HadoopJarJobRunner`()

JobRunner for hadoop jar commands.

`HadoopJarJobTask`(*args, **kwargs)

A job task for hadoop jar commands that define a jar and (optional) main method.

Exceptions

`HadoopJarJobError`

luigi.contrib.hadoop_jar.fix_paths(*job*)

Coerce input arguments to use temporary files when used for output.

Return a list of temporary file pairs (tmpfile, destination path) and
a list of arguments.

Converts each HdfsTarget to a string for the path.

exception luigi.contrib.hadoop_jar.HadoopJarJobError

class luigi.contrib.hadoop_jar.HadoopJarJobRunner

JobRunner for hadoop jar commands. Used to run a HadoopJarJobTask.

run_job(*job*, *tracking_url_callback=None*)

The type of the NotImplemented singleton.

class luigi.contrib.hadoop_jar.HadoopJarJobTask(**args*, ***kwargs*)

A job task for hadoop jar commands that define a jar and (optional) main method.

jar()

Path to the jar for this Hadoop Job.

main()

optional main method for this Hadoop Job.

job_runner()

atomic_output()

If True, then rewrite output arguments to be temp locations and
atomically move them into place after the job finishes.

ssh()

Set this to run hadoop command remotely via ssh. It needs to be a dict that looks like
{“host”: “myhost”, “key_file”: None, “username”: None, [“no_host_key_check”: False]}

args()

Returns an array of args to pass to the job (after hadoop jar <jar> <main>).