# luigi.contrib.sparkey

Classes

`SparkeyExportTask`(*args, **kwargs)

A luigi task that writes to a local sparkey log file.

class luigi.contrib.sparkey.SparkeyExportTask(**args*, ***kwargs*)

A luigi task that writes to a local sparkey log file.

Subclasses should implement the requires and output methods. The output
must be a luigi.LocalTarget.

The resulting sparkey log file will contain one entry for every line in
the input, mapping from the first value to a tab-separated list of the
rest of the line.

To generate a simple key-value index, yield “key”, “value” pairs from the input(s) to this task.

separator = '\t'

run()

The task run method, to be overridden in a subclass.

See Task.run