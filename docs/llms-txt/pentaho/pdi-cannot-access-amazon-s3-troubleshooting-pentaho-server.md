# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/troubleshooting-overview-cp/pentaho-server-issues/pdi-cannot-access-amazon-s3-troubleshooting-pentaho-server.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/troubleshooting-overview-cp/pentaho-server-issues/pdi-cannot-access-amazon-s3-troubleshooting-pentaho-server.md

# PDI cannot access Amazon S3

When trying to access Amazon S3 from the Pentaho Server using the Amazon Command Line Interface (CLI), you may receive an authentication error message. This message may appear when the Pentaho Server is not located on the same machine as the PDI client.

To resolve this error, verify that you are using the same service account to access S3 using the Amazon CLI as you are using to log in to the Pentaho Server.
