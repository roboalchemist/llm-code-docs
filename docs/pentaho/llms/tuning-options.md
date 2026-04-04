# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/use-carte-clusters/set-up-a-carte-cluster/carte-cluster-configuration/configure-a-dynamic-carte-cluster/tuning-options.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/use-carte-clusters/set-up-a-carte-cluster/carte-cluster-configuration/configure-a-dynamic-carte-cluster/tuning-options.md

# Tuning Options

The table below shows the three configurable settings for schedule and remote execution logging in the `slave-server-config.xml file`.

**Note:** To make modifications to `slave-server-config.xml`, you must stop the Pentaho Server.

| Property                   | Values                                                                  | Description                                                              |
| -------------------------- | ----------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| max\_log\_lines            | Any value of 0 (zero) or greater. 0 indicates that there is no limit.   | Truncates the execution log when it goes beyond this many lines.         |
| max\_log\_timeout\_minutes | Any value of 0 (zero) or greater. 0 indicates that there is no timeout. | Removes lines from each log entry if it is older than this many minutes. |
| object\_timeout\_minutes   | Any value of 0 (zero) or greater. 0 indicates that there is no timeout. | Removes entries from the list if they are older than this many minutes.  |

The following code block is an example of the `slave-server-config.xml` file:

```xml
<slave_config>
  <max_log_lines>0</max_log_lines>
  <max_log_timeout_minutes>0</max_log_timeout_minutes>
  <object_timeout_minutes>0</object_timeout_minutes>
</slave_config>
```
