# luigi.contrib.redis_store

Classes

`RedisTarget`(host, port, db, update_id[, ...])

Target for a resource in Redis.

class luigi.contrib.redis_store.RedisTarget(*host*, *port*, *db*, *update_id*, *password=None*, *socket_timeout=None*, *expire=None*)

Target for a resource in Redis.

Parameters:

- 

**host** (*str*) – Redis server host

- 

**port** (*int*) – Redis server port

- 

**db** (*int*) – database index

- 

**update_id** (*str*) – an identifier for this data hash

- 

**password** (*str*) – a password to connect to the redis server

- 

**socket_timeout** (*int*) – client socket timeout

- 

**expire** (*int*) – timeout before the target is deleted

marker_prefix

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