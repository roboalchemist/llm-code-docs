# Source: https://docs.pentaho.com/pdc-10.2-data-optimizer/pdso-install-landing-page/pdso-install-in-hadoop-cluster/pdso-maintain-landing-page/troubleshoot-data-storage-optimizer-fs/data-storage-optimizer-logging/pdso-log-levels.md

# Log levels

By default, the Data Optimizer logs events at the INFO level. This level logs rare events such as startup and shutdown, and events that should not occur, such as errors or warnings. You can adjust the logging level as necessary based on the following levels:

* `ALERT`: Internal API Violated, Possibly a Bug.
* `ERROR`: An Error Occurred, Immediate Action Required.
* `WARNING`: A Significant Event, No Immediate Action Required.
* `INFO`: Notable Events in Normal Product Flow, No Action Required.
* `DEBUG`: Verbose Logging, Useful for Troubleshooting.

Each log level includes itself and all the levels above it in the list. For example, WARNING includes ALERT, ERROR, and WARNING messages. DEBUG includes all levels.

The desired logging level is specified by setting the `LOG_LEVEL` parameter in the configuration file. When Data Optimizer starts up it reads this parameter and sets its logging level accordingly. Typically, you would not want to set this level to anything more than WARNING or INFO, as that might result in unnecessarily verbose logging to your systemd journal.

## Adjusting log level at run time

In order to troubleshoot an issue, you might want to increase the logging level without restarting the software, as a restart might resolve the issue before you have an opportunity to determine the cause. In this case, the `ldoctl` can be used to get and set the log level of a live running instance:

```
ldoctl -m <mount_pont> get
ldoctl -m <mount_point> set <log_level>
```

**Note:** Setting the logl level through ldoctl will not persist if ldo is restarted.
