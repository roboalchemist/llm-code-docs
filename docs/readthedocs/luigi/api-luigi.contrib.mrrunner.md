# luigi.contrib.mrrunner

Since after Luigi 2.5.0, this is a private module to Luigi. Luigi users should
not rely on that importing this module works.  Furthermore, “luigi mr streaming”
have been greatly superseeded by technologies like Spark, Hive, etc.

The hadoop runner.

This module contains the main() method which will be used to run the
mapper, combiner, or reducer on the Hadoop nodes.

Functions

`main`([args, stdin, stdout, print_exception])

Run either the mapper, combiner, or reducer from the class instance in the file "job-instance.pickle".

`print_exception`(exc)

Classes

`Runner`([job])

Run the mapper, combiner, or reducer on hadoop nodes.

class luigi.contrib.mrrunner.Runner(*job=None*)

Run the mapper, combiner, or reducer on hadoop nodes.

run(*kind*, *stdin=<_io.TextIOWrapper name='<stdin>' mode='r' encoding='utf-8'>*, *stdout=<_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'>*)

extract_packages_archive()

luigi.contrib.mrrunner.print_exception(*exc*)

luigi.contrib.mrrunner.main(*args=None*, *stdin=<_io.TextIOWrapper name='<stdin>' mode='r' encoding='utf-8'>*, *stdout=<_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'>*, *print_exception=<function print_exception>*)

Run either the mapper, combiner, or reducer from the class instance in the file “job-instance.pickle”.

Arguments:

kind – is either map, combiner, or reduce