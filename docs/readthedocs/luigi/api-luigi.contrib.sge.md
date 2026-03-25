# luigi.contrib.sge

SGE batch system Tasks.

Adapted by Jake Feala (@jfeala) from
LSF extension [https://github.com/dattalab/luigi/blob/lsf/luigi/lsf.py]
by Alex Wiltschko (@alexbw)
Maintained by Jake Feala (@jfeala)

SunGrid Engine is a job scheduler used to allocate compute resources on a
shared cluster. Jobs are submitted using the `qsub` command and monitored
using `qstat`. To get started, install luigi on all nodes.

To run luigi workflows on an SGE cluster, subclass
`luigi.contrib.sge.SGEJobTask` as you would any `luigi.Task`,
but override the `work()` method, instead of `run()`, to define the job
code. Then, run your Luigi workflow from the master node, assigning > 1
`workers` in order to distribute the tasks in parallel across the cluster.

The following is an example usage (and can also be found in `sge_tests.py`)

```
import logging
import luigi
import os
from luigi.contrib.sge import SGEJobTask

logger = logging.getLogger('luigi-interface')

class TestJobTask(SGEJobTask):

    i = luigi.Parameter()

    def work(self):
        logger.info('Running test job...')
        with open(self.output().path, 'w') as f:
            f.write('this is a test')

    def output(self):
        return luigi.LocalTarget(os.path.join('/home', 'testfile_' + str(self.i)))

if __name__ == '__main__':
    tasks = [TestJobTask(i=str(i), n_cpu=i+1) for i in range(3)]
    luigi.build(tasks, local_scheduler=True, workers=3)

```