# Using the Central Scheduler

While the `--local-scheduler` flag is useful for development purposes,
it’s not recommended for production usage.
The centralized scheduler serves two purposes:

- 

Make sure two instances of the same task are not running simultaneously

- 

Provide visualization of everything that’s going on.

Note that the central scheduler does not execute anything for you or
help you with job parallelization.
For running tasks periodically,
the easiest thing to do is to trigger a Python script from cron or
from a continuously running process.
There is no central process that automatically triggers jobs.
This model may seem limited, but
we believe that it makes things far more intuitive and easy to understand.

## The luigid server

To run the server as a daemon run:

```
$ luigid --background --pidfile <PATH_TO_PIDFILE> --logdir <PATH_TO_LOGDIR> --state-path <PATH_TO_STATEFILE>

```