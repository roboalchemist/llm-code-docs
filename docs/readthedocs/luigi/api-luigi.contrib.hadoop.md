# luigi.contrib.hadoop

Run Hadoop Mapreduce jobs using Hadoop Streaming. To run a job, you need
to subclass `luigi.contrib.hadoop.JobTask` and implement a
`mapper` and `reducer` methods. See Example – Top Artists for
an example of how to run a Hadoop job.

Functions

`attach`(*packages)

Attach a python package to hadoop map reduce tarballs to make those packages available on the hadoop cluster.

`create_packages_archive`(packages, filename)

Create a tar archive which will contain the files for the packages listed in packages.

`dereference`(f)

`fetch_task_failures`(tracking_url)

Uses mechanize to fetch the actual task logs from the task tracker.

`flatten`(sequence)

A simple generator which flattens a sequence.

`get_extra_files`(extra_files)

`run_and_track_hadoop_job`(arglist[, ...])

Runs the job by invoking the command from the given arglist.

Classes

`BaseHadoopJobTask`(*args, **kwargs)

`DefaultHadoopJobRunner`()

The default job runner just reads from config and sets stuff.

`HadoopJobRunner`(streaming_jar[, modules, ...])

Takes care of uploading & executing a Hadoop job using Hadoop streaming.

`HadoopRunContext`()

`JobRunner`()

`JobTask`(*args, **kwargs)

`LocalJobRunner`([samplelines])

Will run the job locally.

`hadoop`(*args, **kwargs)

Exceptions

`HadoopJobError`(message[, out, err])

class luigi.contrib.hadoop.hadoop(**args*, ***kwargs*)

pool

Class to parse optional parameters.

luigi.contrib.hadoop.attach(**packages*)

Attach a python package to hadoop map reduce tarballs to make those packages available
on the hadoop cluster.

luigi.contrib.hadoop.dereference(*f*)

luigi.contrib.hadoop.get_extra_files(*extra_files*)

luigi.contrib.hadoop.create_packages_archive(*packages*, *filename*)

Create a tar archive which will contain the files for the packages listed in packages.

luigi.contrib.hadoop.flatten(*sequence*)

A simple generator which flattens a sequence.

Only one level is flattened.

```
(1, (2, 3), 4) -> (1, 2, 3, 4)

```