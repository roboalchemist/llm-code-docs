# luigi.date_interval

`luigi.date_interval` provides convenient classes for date algebra.
Everything uses ISO 8601 notation, i.e. YYYY-MM-DD for dates, etc.
There is a corresponding `luigi.parameter.DateIntervalParameter` that you can use to parse date intervals.

Example:

```
class MyTask(luigi.Task):
    date_interval = luigi.DateIntervalParameter()

```