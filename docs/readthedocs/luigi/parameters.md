# Parameters

Parameters is the Luigi equivalent of creating a constructor for each Task.
Luigi requires you to declare these parameters by instantiating
`Parameter` objects on the class scope:

```
class DailyReport(luigi.contrib.hadoop.JobTask):
    date = luigi.DateParameter(default=datetime.date.today())
    # ...

```