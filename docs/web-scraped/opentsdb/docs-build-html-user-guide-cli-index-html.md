# Source: https://opentsdb.net/docs/build/html/user_guide/cli/index.html

Title: CLI Tools — OpenTSDB 2.4 documentation

URL Source: https://opentsdb.net/docs/build/html/user_guide/cli/index.html

Markdown Content:
OpenTSDB consists of a single JAR file that uses a shell script to determine what actiosn the user wants to take. While the most common action is to start the TSD with the `tsd` command so that it can run all the time and process RPCs, other commands are available to work with OpenTSDB data. These commands include:

* [uid](https://opentsdb.net/docs/build/html/user_guide/cli/uid.html)
* [mkmetric](https://opentsdb.net/docs/build/html/user_guide/cli/mkmetric.html)
* [import](https://opentsdb.net/docs/build/html/user_guide/cli/import.html)
* [query](https://opentsdb.net/docs/build/html/user_guide/cli/query.html)
* [fsck](https://opentsdb.net/docs/build/html/user_guide/cli/fsck.html)
* [scan](https://opentsdb.net/docs/build/html/user_guide/cli/scan.html)
* [search](https://opentsdb.net/docs/build/html/user_guide/cli/search.html)
* [tsd](https://opentsdb.net/docs/build/html/user_guide/cli/tsd.html)

Accessing a CLI tool is performed from the location of the `tsdb` file, built after compiling OpenTSDB. By default the tsdb file will be located in the `build` directory so you may access it via `./build/tsdb`. Provide the name of the CLI utility as in `./build/tsdb tsd`.

Common Parameters[¶](https://opentsdb.net/docs/build/html/user_guide/cli/index.html#common-parameters "Permalink to this heading")
----------------------------------------------------------------------------------------------------------------------------------

All command line utilities share some common command line parameters:

| Name | Data Type | Description | Default | Example |
| --- | --- | --- | --- | --- |
| –config | String | The full or relative path to an OpenTSDB [Configuration](https://opentsdb.net/docs/build/html/user_guide/configuration.html) file. If this parameter is not provided, the command will attempt to load the default config file. | See [Configuration](https://opentsdb.net/docs/build/html/user_guide/configuration.html) | –config=/usr/local/tempconfig.conf |
| –table | String | Name of the HBase table where datapoints are stored | tsdb | –table=prod-tsdb |
| –uidtable | String | Name of the HBase table where UID information is stored | tsdb-uid | –uidtable=prod-tsdb-uid |
| –verbose | Boolean | For some CLI tools, this command will allow for INFO and above logging per the logback.xml config. Otherwise without this flag, some tools may only log WARNing messages. |  |  |
| –zkbasedir | String | Path under which is the znode for the -ROOT- region | /hbase | –zkbasedir=/prod/hbase |
| –read-only | Boolean | Sets the mode for OpenTSDB | false | –read-only |
| –zkquorum | String | Specification of the ZooKeeper quorum to use, i.e. a list of servers and/or ports in the ZooKeeper cluster | localhost | –zkquorum=zkhost1,zkhost2,zkhost3 |

Site-specific Configuration[¶](https://opentsdb.net/docs/build/html/user_guide/cli/index.html#site-specific-configuration "Permalink to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------

The common parameters above are required by all the CLI commands. It can be tedious to manually type them over and over again. You can instead store typically used values in a file `./tsdb.local`. This file is expected to be a shell script and will be sourced by `./tsdb` if it exists.

_Setting default values for common parameters_

If, for example, your ZooKeeper quorum is behind the DNS name “zookeeper.example.com” (a name with 5 A records), instead of always passing `--zkquorum=zookeeper.example.com` to the CLI tool each time you use it, you can create `./tsdb.local` with the following contents:

# !/bin/bash
MY_ARGS='--zkquorum=zookeeper'
set x $MY_ARGS "$@"
shift

_Overriding the timezone of the TSD_

Servers are frequently using UTC as their timezone. By default, the TSD renders graphs using the local timezone of the server. You can override this to have graphs in your local time by specifying a timezone in `./tsdb.local`. For example, if you’re in California, this will force the TSD to use your timezone:

echo export TZ=PST8PDT >>tsdb.local

On most Linux and BSD systems, you can look under `/usr/share/zoneinfo` for names of timezones supported on your system.

_Changing JVM parameters_

You might want to adjust JVM parameters, for instance to turn on GC activity logging or to set the size of various memory regions. In order to do so, simply set the variable JVMARGS in `./tsdb.local`.

Here is an example that is recommended for production use:

GCARGS="-XX:+PrintGCDetails -XX:+PrintGCTimeStamps -XX:+PrintGCDateStamps\
 -XX:+PrintTenuringDistribution -Xloggc:/tmp/tsd-gc-`date +%s`.log"
if test -t 0; then # if stdin is a tty, don't turn on GC logging.
 GCARGS=
fi

# The Sun JDK caches all name resolution results forever, which is stupid

# This forces you to restart your application if any of the backends change

# IP. Instead tell it to cache names for only 10 minutes at most

FIX_DNS='-Dsun.net.inetaddr.ttl=600'
JVMARGS="$JVMARGS $GCARGS $FIX_DNS"
