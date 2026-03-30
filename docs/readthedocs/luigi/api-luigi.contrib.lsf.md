# luigi.contrib.lsf

Functions

`kill_job`(job_id)

Kill a running LSF job

`track_job`(job_id)

Tracking is done by requesting each job and then searching for whether the job has one of the following states: - "RUN", - "PEND", - "SSUSP", - "EXIT" based on the LSF documentation

Classes

`LSFJobTask`(*args, **kwargs)

Takes care of uploading and executing an LSF job

`LocalLSFJobTask`(*args, **kwargs)

A local version of JobTask, for easier debugging.

luigi.contrib.lsf.track_job(*job_id*)

Tracking is done by requesting each job and then searching for whether the job
has one of the following states:
- “RUN”,
- “PEND”,
- “SSUSP”,
- “EXIT”
based on the LSF documentation

luigi.contrib.lsf.kill_job(*job_id*)

Kill a running LSF job

class luigi.contrib.lsf.LSFJobTask(**args*, ***kwargs*)

Takes care of uploading and executing an LSF job

n_cpu_flag

Parameter whose value is an `int`.

shared_tmp_dir

Parameter whose value is a `str`, and a base class for other parameter types.

Parameters are objects set on the Task class level to make it possible to parameterize tasks.
For instance:

```
class MyTask(luigi.Task):
    foo = luigi.Parameter()

class RequiringTask(luigi.Task):
    def requires(self):
        return MyTask(foo="hello")

    def run(self):
        print(self.requires().foo)  # prints "hello"

```