# Source: https://docs.curator.interworks.com/embedding_using_analytics/data_manager/connecting_to_data_manager.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Connecting to Data Manager

> Set up connections and integrate Data Manager with your analytics workflow for data collection and processing.

When using Data Manager you will likely need to connect to the underlying database that stores the data input from your
users.  You can find the connection information on the "Data Group" edit page, but first you'll need to create a
readonly user (if one does not exist in the info.txt/info.json file found in the root directory of the Curator install).

Note: This will allow your readonly user to connect from anywhere.  If you'd like to specify the IP address they can
connect from replace the '%' with your IP address in the examples below to limit where they can query from.

## Creating a Readonly MySQL User

### 1. Log into MySQL

#### Linux

Run the command below on your server to login to mysql:

```bash  theme={null}
mysql -u root -p
```

#### Windows

Navigate into MariaDB/MySQL root directory and then login to MySQL:

```bash  theme={null}
cd C:\InterWorks\Curator\libs\MariaDB\bin
mysql -u root -p
```

### 2. Create a new MySQL user

Run the command below to create a new user that can run a connection from *anywhere* (replacing 'USER' and 'PASSWORD'
with a username and password you'd like to use):

```SQL  theme={null}
CREATE USER 'USER'@'%' IDENTIFIED BY 'PASSWORD';
```

### 3. Grant read-only permission to the MySQL user

Run the command below to create a new user that can read data from *anywhere* (again replacing 'USER' and 'PASSWORD'
with a username and password you'd like to use):

```SQL  theme={null}
GRANT SELECT, SHOW VIEW ON curator.* TO 'USER'@'%' IDENTIFIED BY 'PASSWORD';
FLUSH PRIVILEGES;
```

**Important!** Be sure you keep these credentials secure, but also available for reference as they will be required to
connect to your data.

### Connecting to the Datamanager Database

1. Find the connection information for the table you would like to view in the top section of the edit "Data Group" page

   * Database Name: **Curator**
   * Host Name: **127.0.0.1**
   * Table Name: **a\_reports\_data\_group**

2. Use the connection details from the "Creating a Readonly MySQL User" and the database, hostname, and table name from
   the previous step to connect to your MySQL data source.

### Troubleshooting Connections

1. Ensure your firewall rules allow inbound traffic over port 3306 to allow remote connections to your database.
   If you are having trouble connecting, please contact your hosting team for further help.
2. By default, remote connections are not allowed on some operating systems (e.g. Ubuntu 20).  You can run the commands
   below to set up remote connections:

   Determine the location of your MySQL config file by running the command below:

   ```bash  theme={null}
   mysql --help | grep "Default options" -A 1
   ```

   Open the file that is returned from these commands (i.e. `/etc/my.cnf`):
   Add the following line to the bottom of the file, where `xxx.ip.xxx` is replaced with your IP address, or you can use
   `0.0.0.0` to allow remote connections from anywhere:

   ```conf  theme={null}
   bind-address= xxx.ip.xxx
   ```

   Now save your file and restart mysql to allow remote connections:

   ```bash  theme={null}
   sudo systemctl restart mysql
   ```
