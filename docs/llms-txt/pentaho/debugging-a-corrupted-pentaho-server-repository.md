# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/troubleshooting-overview-cp/pentaho-repository-issues/debugging-a-corrupted-pentaho-server-repository.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/troubleshooting-overview-cp/pentaho-repository-issues/debugging-a-corrupted-pentaho-server-repository.md

# Debugging a corrupted Pentaho Server repository

A corrupted Pentaho Repository will become unresponsive resulting in missing content, inaccessibility, and the following error message that appears in the `/pentaho-server/tomcat/logs/catalina.out` log file:

`ERROR [ConnectionRecoveryManager] could not execute statement, reason: File corrupted while reading record: "page[48970] data leaf table:8 entries:1 parent:49157 keys:[118547] offsets:[737]". Possible solution: use the recovery tool [90030-131], state/code: 90030/90030`

If this error occurs, shut down the Pentaho Server and restore your solution repository from a recent backup.

If you do not have a viable backup, you may be able to minimize data loss by identifying the exact file that is corrupt. Enable debug logging by adding the following XML snippet above the `<root>` element in the `/WEB-INF/classes/log4j2.xml` inside your deployed `pentaho.war`:

```xml
<Logger name="org.pentaho.platform" level=”DEBUG>
```

Restart the Pentaho Server and retry the action that caused the original error. If it occurs again, shut down the Pentaho Server and open the `catalina.out` log file in Tomcat. The last line that appears before the error usually contains the name of the file that has been damaged.

When you have finished investigating, remove the extra logging capabilities so that your Pentaho Server log files do not become large and unmanageable.

## Using the H2 database recovery tool

The Pentaho Server includes a third-party H2 database recovery tool that enables you to extract raw data from your Pentaho Repository. This recovery tool is primarily useful in situations where the repository has become corrupt and you do not have any relevant backups.

**Note:** If the database has become corrupt, the corrupted rows will not be exported. Any information contained in corrupted rows is unrecoverable through this method.

The recovery tool is a JAR you run via the Java command. The output is a SQL dump that you can then attempt to import after you have re-initialized your Pentaho Server database.

Read more about the recovery tool on the H2 Web site: <http://www.h2database.com/html/advanced.html#using_recover_tool>.

Follow these directions to use the recovery tool:

1. Open a terminal on (or establish an SSH connection to) your Pentaho Server.
2. Navigate to the `/pentaho-solutions/system/jackrabbit/repository/version/` folder.

   ```
   cd pentaho-server/pentaho-solutions/system/jackrabbit/repository/version/
   ```
3. Run the `h2-1.2.131.jar` H2 database JAR with the recovery tool option.

   ```java
   java -cp h2-1.2.131.jar org.h2.tools.Recover
   ```
4. Create a directory to move your old database files.

   ```
   mkdir old
   ```
5. Move the old database files to the directory created in the previous step.

   ```
   mv db.h2.db db.trace.db old
   ```
6. Re-initialize the repository with the **RunScript** option using the salvaged SQL dump as the source.

   ```java
   java -cp h2-1.2.131.jar org.h2.tools.RunScript -url jdbc:h2:./db -user sa -script db.h2.sql
   ```
7. The backup directory you created earlier (`old` in the above example) can be removed after you are sure that you no longer need the corrupted database files.
8. Start the Pentaho Server and check for further errors. If repository errors persist, contact Pentaho support.
