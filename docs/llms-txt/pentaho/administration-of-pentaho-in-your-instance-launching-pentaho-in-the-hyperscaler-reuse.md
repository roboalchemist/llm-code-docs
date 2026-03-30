# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/hyperscalers-landing-page/launching-pentaho-ami-in-aws-cp/see-also-launch-pentaho-in-the-hyperscaler-reuse/administration-of-pentaho-in-your-instance-launching-pentaho-in-the-hyperscaler-reuse.md

# Administration of Pentaho in your instance

The Pentaho software is owned by the `pentaho` user. A PostgreSQL repository is also installed on this instance and owned by the `postgres` user. Neither user has a password. You can only access these users via the `sudo` command.

The Pentaho software and the PostgreSQL data files are installed on the second volume (`/install`). The `/install/pentaho` directory is symlinked to the`/opt/pentaho` directory.
