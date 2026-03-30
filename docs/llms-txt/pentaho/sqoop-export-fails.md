# Source: https://docs.pentaho.com/install/9.3-install/use-hadoop-with-pentaho/big-data-issues/sqoop-export-fails.md

# Source: https://docs.pentaho.com/install/10.2-install/use-hadoop-with-pentaho/big-data-issues/sqoop-export-fails.md

# Sqoop export fails

If executing a Sqoop export job and the system generates the following error because a file already exists at the destination, then Sqoop failed to clear the compile directory:

`Could not rename \tmp\sqoop-devuser\compile\1894e2403c37a663c12c752ab11d8e6a\aggregatehdfs.java to C:\Builds\pdi-ee-client-9.0.0.0-MS-550\data-integration\.\aggregatehdfs.java. Error: Destination 'C:\Builds\pdi-ee-client-9.0.0.0-MS-550\data-integration\.\aggregatehdfs.java' already exists.`

Despite the error message, the job that generated it ended successfully. To stop this error message, you can add a **Delete** step to the job to remove the compile directory before execution of the Sqoop export step.
