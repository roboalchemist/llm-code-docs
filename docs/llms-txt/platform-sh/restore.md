# Source: https://docs.upsun.com/environments/restore.md

# Restore an environment from a backup

Once you have [backups of your environment](https://docs.upsun.com/environments/backup.md), you can restore data from a previous point.

To restore an environment, you need an [Admin role for that environment type](https://docs.upsun.com../administration/users.md).

## 1. List available backups

To restore an environment, first select one of the available backups:

You get a response similar to the following:

```bash {}
Backups on the project My Project (1234567abcdef), environment main (type: production):
+---------------------------+----------------------------+------------+
| Created                   | Backup ID                  | Restorable |
+---------------------------+----------------------------+------------+
| {{ now.Year }}-08-15T09:48:58+01:00 | 5ouvtgo4v75axijww7sqnftste | true       |
| {{ now.Year }}-07-09T14:17:17+01:00 | 7jks7dru5xpx5p5id5wtypur2y | true       |
| {{ now.Year }}-06-22T18:33:29+01:00 | f3jbyxlhtmalco67fmfoxs7n4m | true       |
+---------------------------+----------------------------+------------+
```

Select one of the backups marked as **Restorable** and copy its **Backup ID**.

 - Navigate to the environment where you want to see backups.
 - Click **Backups**.

Select one of the backups marked as having completed successfully .

## 2. Restore from a backup

To restore the backup you've selected, follow these steps:

 - Press ``enter`` to agree with the consequences and continue.

 - Next to the backup you’ve selected, click **More** More.
 - Click **Restore**.
 - Read through the consequences and click **Yes, Restore**.

The data is restored and your backed-up environment is deployed.
This deployment uses the built app, including variables, from when the backup was taken.

**Warning**: 

The code is also initially restored, but Upsun doesn’t modify your Git repository.
So any future (re)deployments use the current Git repository to build the environment.

To restore your code to its previous state when the backup was taken,
use Git commands such as [revert](https://git-scm.com/docs/git-revert).
Note that you can also opt out of restoring the code entirely by using the ``--no-code`` flag.
For more information, see [how backup and restore works on Upsun](https://docs.upsun.com/environments/backup.md#how-backup-and-restore-works).
Also, see [how resource allocation works](https://docs.upsun.com/manage-resources/resource-init.md#backup-restoration) when you restore a backup.

## Restore to a different environment

You can restore backups to a different environment than they were created on using the CLI:

1. Switch to the branch where the backup was created.
2. To restore your backup to an existing environment, run the following command:

   ```bash
   upsun backup:restore --target=<TARGET_ENVIRONMENT_NAME> <BACKUP_ID>
   ```

   If your target environment doesn't exist yet, you can create it by [branching an existing environment](https://docs.upsun.com/glossary.md#branch).
   The new target environment will be an exact copy of the existing (parent) environment.

   To do so, use the `--branch-from` option to specify the parent of your new target environment:

   ```bash
   upsun backup:restore --target=<TARGET_ENVIRONMENT_NAME> --branch-from=<PARENT_ENVIRONMENT_NAME> <BACKUP_ID>
   ```

