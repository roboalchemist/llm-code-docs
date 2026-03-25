# luigi.contrib.scalding

Module Attributes

`logger`

Scalding support for Luigi.

Classes

`ScaldingJobRunner`()

JobRunner for pyscald commands.

`ScaldingJobTask`(*args, **kwargs)

A job task for Scalding that define a scala source and (optional) main method.

luigi.contrib.scalding.logger = <Logger luigi-interface (WARNING)>

Scalding support for Luigi.

Example configuration section in luigi.cfg:

```
[scalding]
# scala home directory, which should include a lib subdir with scala jars.
scala-home: /usr/share/scala

# scalding home directory, which should include a lib subdir with
# scalding-*-assembly-* jars as built from the official Twitter build script.
scalding-home: /usr/share/scalding

# provided dependencies, e.g. jars required for compiling but not executing
# scalding jobs. Currently required jars:
# org.apache.hadoop/hadoop-core/0.20.2
# org.slf4j/slf4j-log4j12/1.6.6
# log4j/log4j/1.2.15
# commons-httpclient/commons-httpclient/3.1
# commons-cli/commons-cli/1.2
# org.apache.zookeeper/zookeeper/3.3.4
scalding-provided: /usr/share/scalding/provided

# additional jars required.
scalding-libjars: /usr/share/scalding/libjars

```