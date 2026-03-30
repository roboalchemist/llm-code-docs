# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/installation-and-upgrade-issues/cannot-create-jackrabbit-tables-in-mysql.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/installation-and-upgrade-issues/cannot-create-jackrabbit-tables-in-mysql.md

# Cannot create Jackrabbit tables in MySQL

The Pentaho solution repository uses long text strings that require a longer maximum character limit than the default UTF-8 configuration allows. Using UTF-8 will prevent the MySQL initialization scripts from running during installation.

If your MySQL character set is configured to use UTF-8, you must change it to ASCII to use it as a Pentaho solution database.
