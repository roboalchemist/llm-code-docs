# luigi.contrib.sge_runner

The SunGrid Engine runner

The main() function of this module will be executed on the
compute node by the submitted job. It accepts as a single
argument the shared temp folder containing the package archive
and pickled task to run, and carries out these steps:

- 

extract tarfile of package dependencies and place on the path

- 

unpickle SGETask instance created on the master node

- 

run SGETask.work()

On completion, SGETask on the master node will detect that
the job has left the queue, delete the temporary folder, and
return from SGETask.run()

Functions

`main`([args])

Run the work() method from the class instance in the file "job-instance.pickle".

luigi.contrib.sge_runner.main(*args=['/home/docs/checkouts/readthedocs.org/user_builds/luigi/envs/latest/lib/python3.13/site-packages/sphinx/__main__.py', '-T', '-b', 'html', '-d', '_build/doctrees', '-D', 'language=en', '.', '/home/docs/checkouts/readthedocs.org/user_builds/luigi/checkouts/latest/_readthedocs//html']*)

Run the work() method from the class instance in the file “job-instance.pickle”.