# Source: https://docs.pentaho.com/pdia-data-integration/extracting-data-into-pdi/define-pdi-database-connection-pooling.md

# Define PDI database connection pooling

You can use the **Pooling** option in the Database Connection dialog box to set up a connection pool and define options like the initial pool size, maximum pool size, and connection pool parameters. By default, a connection remains open for each individual report or set of reports in PUC and for each individual step in a transformation in PDI. For example, you might start by specifying a pool of ten or fifteen connections, and as you run reports in PUC or transformations in PDI, the unused connections drop off. Pooling helps control database access, especially if you have dashboards that contain many reports and require a large number of connections. Pooling can also be implemented when your database licensing restricts the number of active concurrent connections.

Perform the following steps to specify pooling options:

1. Open the Database Connection dialog box in [PUC](https://app.gitbook.com/o/PtpmPYUKgAsUWgv8SVUt/s/dbSFXbJFiObHB299lSSa/) or [PDI](https://docs.pentaho.com/pdia-data-integration/readme).
2. Click **Pooling** in the left pane.

   Options appear for your JDBC driver as shown in the example below:![Pooling options in the PUC and PDI Database Connection dialog boxes](https://773338310-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYwnJ6Fexn4LZwKRHghPK%2Fuploads%2Ff2RB3WrqmbmheOBWBJSo%2FssPUCanPDIDataConnectionPoolingOptions.png?alt=media\&token=10b47382-c3f6-441c-a335-c139f2b0a54c)

   The following table shows an example of **Pooling** options that might be available in a typical JDBC driver. Check your driver documentation for driver-specific pooling details.

| Option                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Enable Connection Pooling** | Enables connection pooling.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **Pool Size**                 | <ul><li><strong>Initial</strong></li></ul><p>Set the initial size of the connection pool.</p><ul><li><strong>Maximum</strong></li></ul><p>Set the maximum number of connections in the connection pool.</p>                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **Parameters**                | <p>You can define additional custom pool parameters. Click on any parameter to view a short description of that parameter. Click <strong>Restore Defaults</strong> when to restore the default values for selected parameters.</p><p>The most commonly-used parameter is <strong>validationQuery</strong>. The parameter differs slightly depending on your RDBMS connection. The basic set of Pentaho databases use the following values for <strong>validationQuery</strong>:</p><ul><li>For Oracle and PostgreSQL, use <strong>Select 1 from dual</strong>.</li><li>For MS SQL Server and MySQL, use <strong>Select 1</strong>.</li></ul> |
| **Description**               | Enter a description for your parameters.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |

3\. Click **Test**.

```
A success message appears if the connection is established.
```

4\. Click **OK** to close the connection test dialog box.

5. To save the connection, click **OK** to close the Database Connection dialog box.
