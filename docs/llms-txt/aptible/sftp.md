# Source: https://www.aptible.com/docs/core-concepts/managed-databases/supported-databases/sftp.md

# SFTP

STFP Databases can be provisioned in the following ways:

* In the Dashboard > Environment > Databases > "New Database"  > SFTP
* Using the [`aptible db:create`](/reference/aptible-cli/cli-commands/cli-db-create) command
  * For example: `aptible db:create "$DB_HANDLE" --type sftp`
* Using the [Aptible Terraform Provider](/reference/terraform)

# Usage

The service is designed to run with an initial, password-protected admin user. The credentials for this user can be viewed in the [Database Credentials](/core-concepts/managed-databases/connecting-databases/database-credentials) section of the database page. Additional users can be provisioned anytime by calling add-sftp-user with a username and SSH public key.

<Warning>
  By default, this SFTP service defaults files to be stored in the given users home directory (in the `/home/%u` format). Files in the `/home/%u` directory structure are located on a persistent volume that will be reliably persisted between any reload/restart/scale/maintenance activity of the SFTP instance. However, the initial `aptible` user is a privileged user which can store files elsewhere in the file system, in areas which are on an ephemeral volume which will be lost during any reload/restart/scale/maintenance activity. Please only store SFTP files in the users' home directory structure!
</Warning>

## Connecting and Adding Users

* Run a db:tunnel in one terminal window: `aptible db:tunnel $DB_HANDLE`
* This will give output of a URL containing the host/password/port
* In another terminal window: `ssh -p PORT aptible@localhost.aptible.in` (where PORT is copied from the port provided in the previous step)
* Use the password provided in the previous step
* Once in the shell, you can use the `add-sftp-user` utility to add additional users to the SFTP instance. Please note that additional users added with this utility must use [ssh key authentication](/core-concepts/security-compliance/authentication/ssh-keys), and the public key is provided as an argument to the command.

```
sudo add-sftp-user regular-user "SSH_PUBLIC_KEY"
```

where `SSH_PUBLIC_KEY` would be the ssh public key for the user. To provide a fictional public key (truncated for readability) as an example:

```
sudo add-sftp-user regular-user "ssh-rsa AAAAB3NzaC1yc2EBAQClKswlTG2MO7YO9wENmf user@example.com"
```
