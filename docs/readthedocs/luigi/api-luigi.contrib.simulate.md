# luigi.contrib.simulate

A module containing classes used to simulate certain behaviors

Classes

`RunAnywayTarget`(task_obj)

A target used to make a task run every time it is called.

class luigi.contrib.simulate.RunAnywayTarget(*task_obj*)

A target used to make a task run every time it is called.

Usage:

Pass self as the first argument in your task’s output:

And then mark it as done in your task’s run:

temp_dir = '/tmp/luigi-simulate'

temp_time = 86400

unique = <Synchronized wrapper for c_int(0)>

get_path()

Returns a temporary file path based on a MD5 hash generated with the task’s name and its arguments

exists()

Checks if the file exists

done()

Creates temporary file to mark the task as done