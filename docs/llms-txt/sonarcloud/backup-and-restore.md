# Source: https://docs.sonarsource.com/sonarqube-community-build/server-update-and-maintenance/maintenance/backup-and-restore.md

# Source: https://docs.sonarsource.com/sonarqube-server/8.9/instance-administration/backup-and-restore.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.8/instance-administration/backup-and-restore.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/instance-administration/backup-and-restore.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/instance-administration/backup-and-restore.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/instance-administration/backup-and-restore.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/instance-administration/backup-and-restore.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/instance-administration/backup-and-restore.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/instance-administration/backup-and-restore.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/instance-administration/backup-and-restore.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/instance-administration/backup-and-restore.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/server-upgrade-and-maintenance/maintenance/backup-and-restore.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/server-upgrade-and-maintenance/maintenance/backup-and-restore.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/server-update-and-maintenance/maintenance/backup-and-restore.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/server-update-and-maintenance/maintenance/backup-and-restore.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/server-update-and-maintenance/maintenance/backup-and-restore.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/server-update-and-maintenance/maintenance/backup-and-restore.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/server-update-and-maintenance/maintenance/backup-and-restore.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/server-update-and-maintenance/maintenance/backup-and-restore.md

# Source: https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/maintenance/backup-and-restore.md

# Backup and restore

### Backing up data <a href="#backing-up-data" id="backing-up-data"></a>

Most databases come with backup tools. We recommend using these tools to back up your data.

Hot database backups are supported.

### Restoring data <a href="#restoring-data" id="restoring-data"></a>

To restore data from the backup and or trigger a full [reindexing](https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/maintenance/reindexing "mention"), follow these steps:

1. Stop the server.
2. Restore the backup.
3. Drop the Elasticsearch indexes by deleting the contents of `<sonarqubeHome>/data/es8` directory.
4. Restart the server.
