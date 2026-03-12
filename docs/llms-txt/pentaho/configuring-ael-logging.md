# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/adaptive-execution-layer-cp-landing-page/ael-logging-cp/configuring-ael-logging.md

# Configuring AEL logging

When a log file reaches its maximum size, a new log file is created and the logging data is written to the new file. When the maximum number of log files is reached, the oldest log file is deleted and a new one is created.

The maximum log size is 10MB by default and the maximum number of stored logs is 10 by default. You can modify the log rotation parameters in the `logback.xml` file.
