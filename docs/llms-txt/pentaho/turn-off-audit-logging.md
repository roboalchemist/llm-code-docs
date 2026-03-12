# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/optimize-the-pentaho-system/performance-tuning/pentaho-server-performance-tips/turn-off-audit-logging.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/optimize-the-pentaho-system/performance-tuning/pentaho-server-performance-tips/turn-off-audit-logging.md

# Turn off audit logging

While audit logging can be useful for monitoring Pentaho Server activity and performance, the act of collecting the necessary audit data can introduce significant memory overhead with the solution database. Your Pentaho Server must be stopped before performing this procedure. Follow the instructions below to disable audit logging in the Pentaho Server.

**Note:** Performing this task will disable all audit functions in the Pentaho Server's administration interface.

1. Open the `/pentaho-solutions/system/pentahoObjects-spring.xml` file with a text editor.
2. Locate the following line:

   ```
   <bean id="IAuditEntry" class="org.pentaho.platform.engine.services.audit.AuditSQLEntry" scope="singleton" />

   ```
3. Replace that line with the following one:

   ```
   <bean id="IAuditEntry" class="org.pentaho.platform.engine.core.audit.NullAuditEntry" scope="singleton" />

   ```
4. Save and close the file
5. Using a database management tool or command line interface, connect to the Pentaho Hibernate database.
6. Truncate (but do not drop) the following table:
   * PRO\_AUDIT
7. Exit your database utility and restart the Pentaho Server.
