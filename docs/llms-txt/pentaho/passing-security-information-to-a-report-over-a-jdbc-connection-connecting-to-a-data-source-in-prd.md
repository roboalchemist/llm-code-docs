# Source: https://docs.pentaho.com/pba-report-designer/connect-report-designer-to-a-data-source-cp/jdbc-connecting-to-a-data-source-in-prd/passing-security-information-to-a-report-over-a-jdbc-connection-connecting-to-a-data-source-in-prd.md

# Source: https://docs.pentaho.com/pba-report-designer/9.3-report-designer/connect-report-designer-to-a-data-source-cp/jdbc-connecting-to-a-data-source-in-prd/passing-security-information-to-a-report-over-a-jdbc-connection-connecting-to-a-data-source-in-prd.md

# Source: https://docs.pentaho.com/pba-report-designer/10.2-report-designer/connect-report-designer-to-a-data-source-cp/jdbc-connecting-to-a-data-source-in-prd/passing-security-information-to-a-report-over-a-jdbc-connection-connecting-to-a-data-source-in-prd.md

# Passing security information to a report over a JDBC connection

You can use one of two options when you want to pass security-related information, (such as user name and password), associated with a report over a JDBC connection:

* Choose from the list of predefined environment variables; for example, *env::username* or *env::roles*
* Define your own specific environment variables to pass to the connection, (session or global), using the formula function, ENV, inside a hidden parameter. For example, `=ENV("session:xaction_parameter_password")` or `=ENV("global:xaction_parameter_password")` where *xaction\_parameter\_password* is the parameter defined in an .xaction.

![Passing security information a JDBC connection](https://550079190-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FwlpCEXkXNwNKB6O9BgU8%2Fuploads%2Fgit-blob-b0ca437744c1f6a9a06ae03133fb40e6cfddfa6e%2Frd_pswd_parm_security_config.png?alt=media)

The available selections appear as drop-down options under JDBC Security Configuration when you click **Edit Security** in the JDBC Data Source dialog box.
