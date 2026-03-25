# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/installation-and-upgrade-issues/missing-quartz-library-database-error.md

# Missing Quartz library database error

During installation of 10.2.0.1 or later, the Quartz library database was not created. Pentaho 10.2.0.0 and previous versions use the Quartz 1.x library, which is created within the database with a `QRTZ5_` prefix. The more recent versions, starting with Pentaho 10.2.0.1, use the Quartz 2.x library, which is created within the database with a `QRTZ6_` prefix.

To fix this problem, you must create a scheduling database or migrate an existing scheduling database for use by Quartz and then restart the server. See [Mandatory Quartz upgrade for versions 10.2.0.1 and later](https://docs.pentaho.com/install/10.2-install/pentaho-upgrade-cp/mandatory-quartz-upgrade-for-versions-10.2.0.1-and-later).
