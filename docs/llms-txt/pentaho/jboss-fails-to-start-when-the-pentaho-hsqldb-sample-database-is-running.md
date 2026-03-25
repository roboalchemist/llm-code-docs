# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/installation-and-upgrade-issues/jboss-fails-to-start/jboss-fails-to-start-when-the-pentaho-hsqldb-sample-database-is-running.md

# JBoss fails to start when the Pentaho HSQLDB sample database is running

**Note:** This problem can also manifest as the Pentaho sample database refusing to start when the Pentaho Server is deployed to JBoss.

The Pentaho-supplied HSQLDB sample database operates on the default HSQLDB port of 9001. JBoss has its own HSQLDB instance running on the same port. This port collision will prevent the JBoss version from starting and cause the startup process to halt.

You can change the Pentaho sample database port by editing the `start_hypersonic` script and adding the `-port 9002` switch to the last line, as shown in the following code sample:

```java
"$_PENTAHO_JAVA" -cp $THE_CLASSPATH org.hsqldb.Server -port 9002 -database.0 $DIR_REL/hsqldb/sampledata -dbname.0 sampledata -database.1 $DIR_REL/hsqldb/hibernate -dbname.1 hibernate -database.2 $DIR_REL/hsqldb/quartz -dbname.2 quartz
```
