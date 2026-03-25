# Running Luigi

## Running from the Command Line

The preferred way to run Luigi tasks is through the `luigi` command line tool
that will be installed with the pip package.

```
# my_module.py, available in your sys.path
import luigi

class MyTask(luigi.Task):
    x = luigi.IntParameter()
    y = luigi.IntParameter(default=45)

    def run(self):
        print(self.x + self.y)

```