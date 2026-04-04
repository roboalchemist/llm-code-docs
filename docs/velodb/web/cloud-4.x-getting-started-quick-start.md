# Source: https://docs.velodb.io/cloud/4.x/getting-started/quick-start

Version: 4.x

On this page

# Getting Started

## New User Registration and Organization Creation​

### Register and Login​

Click <https://www.velodb.cloud/> to enter the VeloDB Cloud registration and
trial page and fill in the relevant information to complete the registration.

![user register](/assets/images/user-
register-f4bf7408e0671addc942afba8a108c54.png)

> **Tip** VeloDB Cloud includes two independent account systems: One is used
> for logging into the console, as described in this topic. The other one is
> used to connect to the warehouse, which is described in the Connections
> topic.

### Change Password​

After login, click **User Menu** > **User Center** to change the login
password for the VeloDB Cloud console.

![change user password](/assets/images/change-user-
password-9531a1cd03598f385130a912a4035ef2.png)

Once you have successfully changed the password for the first time, you can
use the password for subsequent logins.

## Warehouse and Cluster Creation​

In VeloDB Cloud, the warehouse is a logical concept that includes physical
objects such as warehouse metadata, clusters, and data storage.

Under each organization, you can create multiple warehouses to meet the needs
of different business systems, and the resources and data between these
warehouses are isolated.

### Create Warehouse​

A wizard page will be displayed if the organization does not have a warehouse.
You can create the first warehouse following the prompts.

![create warehouse](/assets/images/create-
warehouse-1556c66eb56b8e952c634f5852ed8361.jpg)

You can use a ​free-tier warehouse​ or directly ​purchase a paid warehouse​
based on your analytical requirements.

> **Tip:**
>
>   1. For more information about SaaS and BYOC, see [Overview of
> Warehouses](/cloud/4.x/management-guide/warehouse-management/).
>   2. If you need to activate a free BYOC, please refer to [Create a BYOC
> Warehouse](/cloud/4.x/management-guide/warehouse-management/create-byoc-
> warehouse).
>

### Create Cluster​

If you have activated the trial warehouse, you will see a trial cluster in
that warehouse.

In the trial warehouse, you may try the features by importing small amounts of
data. You may not create paid clusters under the trial warehouse. If you are
happy with the trial experience, you can upgrade the trial warehouse to a paid
one, and then you can create paid clusters under the paid warehouse.

## Change Warehouse Password​

The username and password are required when connecting to a warehouse. VeloDB
Cloud initializes the username ('admin') and password for you. You can change
the password on the **Settings** page.

![change warehouse password](/assets/images/change-warehouse-
password-8396e74cfced892bcbd51ac6faa52764.png)

> **Warning** The password only supports uppercase letters, lowercase letters,
> numbers and special characters ~!@#$%^&*()_+|&lt&gt,.?/:;'[]", need to
> contain at least 3 of them, length 8-20 characters.

## Connect to Warehouse​

Click **Query** in the left navigation bar, open the login page, enter the
username and password, and enter the WebUI interface after completing the
login.

![webui query](/assets/images/webui-
query-8183389b1bfccb8dd4715c6a996dbdca.png)

### Create Database​

Execute the following statement in the query editor:

    
    
    create database demo;  
    

### Create Data Table​

Execute the following statement in the query editor:

    
    
    use demo;  
      
    create table mytable  
    (  
    k1 TINYINT,  
    k2 DECIMAL(10, 2) DEFAULT "10.05",  
    k3 CHAR(10) COMMENT "string column",  
    k4 INT NOT NULL DEFAULT "1" COMMENT "int column"  
    )  
    COMMENT "my first table"  
    DISTRIBUTED BY HASH(k1) BUCKETS 1;  
    

You can see the fields of mytable through desc mytable.

### Insert Data​

Execute the following statement in the query editor:

    
    
    INSERT INTO mytable (k1, k2, k3, k4) VALUES  
    (1, 0.14, 'a1', 20),  
    (2, 1.04, 'b2', 21),  
    (3, 3.14, 'c3', 22),  
    (4, 4.35, 'd4', 23);  
    

### Query Data​

The table creation and data import are completed above, and the query can be
performed below.

    
    
    select * from mytable;  
    

![webui query result](/assets/images/webui-query-
result-956dff83857ffeb18421f3758085ac44.png)

## （OPTIONAL）Connect to Warehouse Using MySQL Client​

### IP Whitelist Management​

On the **Connections** page, switch to the **Public Link** tab to manage IP
whitelist. Click **Add IP Whitelist** to add new IP addresses.

![public link ip whitelist](/assets/images/public-link-ip-
whitelist-40498cfa0943672f009fb66c31d213d5.png)

In the IP whitelist, users can add or delete IP addresses to enable or disable
their access to the warehouse.

### MySQL Client​

You may download MySQL Client from the official website of MySQL. Here we
provide a Linux-free version of [MySQL Client](https://doris-build-hk.oss-cn-
hongkong.aliyuncs.com/mysql-client/mysql-5.7.22-linux-
glibc2.12-x86_64.tar.gz). If you need MySQL Client for Mac and Windows, please
go to the MySQL official website.

Currently, VeloDB is compatible with MySQL Client 5.7 and above.

You may read details about connections by clicking "Connections" on the target
warehouse on the VeloDB Cloud console.

> Note:
>
>   1. The warehouse supports public network connection and private network
> (PrivateLink) connection. Different connection methods require different
> connection information.
>
>   2. The public network connection is open by default, and the IP whitelist
> is also open to the public by default. If you no longer need to connect to
> the warehouse from the public network, please close it.
>
>   3. For the first connection, please use the user admin and its password.
> You can initialize or reset it in the **Setting** page on VeloDB Cloud
> console.
>
>

Supposing that you are connecting to a warehouse using the following public
link:

![public link connection info](/assets/images/public-link-connection-
info-4fb06e922bb490fb95fe191255fdfea0.png)

Download MySQL Client and unzip the file, find the `mysql` command line tool
under the `bin/` directory. Execute the folowing command to connect to VeloDB.

    
    
    mysql -h 34.199.74.195 -P 33641 -u admin -p  
    

After login, if you see the following snippet, that usually means that your
Client IP address has not been added to the connection whitelist on the
console.

    
    
    ERROR 2013 (HY000): Lost connection to MySQL server at 'reading initial communication packet', system error: 2  
    

If the following is displayed, that means the connection succeeds.

    
    
    Welcome to the MySQL monitor.  Commands end with ; or \g.  
    Your MySQL connection id is 119952  
    Server version: 5.7.37 VeloDB Core version: 3.0.4  
      
    Copyright (c) 2000, 2022, Oracle and/or its affiliates.  
      
    Oracle is a registered trademark of Oracle Corporation and/or its  
    affiliates. Other names may be trademarks of their respective  
    owners.  
      
    Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.  
      
    mysql>  
    

### Create Database and Table​

#### Create Database​

    
    
    create database demo;  
    

#### Create Table​

    
    
    use demo;  
      
    create table mytable  
    (  
        k1 TINYINT,  
        k2 DECIMAL(10, 2) DEFAULT "10.05",  
        k3 CHAR(10) COMMENT "string column",  
        k4 INT NOT NULL DEFAULT "1" COMMENT "int column"  
    )  
    COMMENT "my first table"  
    DISTRIBUTED BY HASH(k1) BUCKETS 1;  
    

You may check details of `mytable` via `desc mytable`.

#### Load Data​

Save the following sample data in the local data.csv:

    
    
    1,0.14,a1,20  
    2,1.04,b2,21  
    3,3.14,c3,22  
    4,4.35,d4,23  
    

**Upload data via HTTP protocol** :

    
    
    curl -u admin:admin_123 -H "fileName:dir1/data.csv" -T data.csv -L '34.199.74.195:39173/copy/upload'  
    

You can call and upload multiple files be repeating this command.

**Load data by the copy into command:**

* * *
    
    
    curl -u admin:admin_123 -H "Content-Type: application/json" '34.199.74.195:39173/copy/query' -d '{"sql": "copy into demo.mytable from @~(\"dir1/data.csv\") PROPERTIES (\"file.column_separator\"=\",\", \"copy.async\"=\"false\")"}'  
    

`dir1/data.csv` refers to the file uploaded in the previous step. Wildcard and
glob pattern matching are supported here.

The service side can automatically identify general formats such as csv.

`file.column_separator=","` specifies comma as the separator in the csv
format.

Since the copy into command is submitted asychronously by default,
`"copy.async"="false"` is specified here to implement synchronous submission.
That is, the command will only return after the data are loaded successfully.

If you see the following response, that means the data are successfully
loaded.

    
    
    {  
        "msg": "success",  
        "code": 0,  
        "data": {  
            "result": {  
                "msg": "",  
                "loadedRows": "4",  
                "id": "d33e62f655c4a1a-9827d5561adfb93d",  
                "state": "FINISHED",  
                "type": "",  
                "filterRows": "0",  
                "unselectRows": "0",  
                "url": null  
            },  
            "time": 5007,  
            "type": "result_set"  
        },  
        "count": 0  
    }  
    

### Query Data​

After table creation and data loading, you may execute queries on the data.

    
    
    mysql> use demo;  
    Reading table information for completion of table and column names  
    You can turn off this feature to get a quicker startup with -A  
      
    Database changed  
    mysql> select * from mytable;  
    +------+------+------+------+  
    | k1   | k2   | k3   | k4   |  
    +------+------+------+------+  
    |    1 | 0.14 | a1   |   20 |  
    |    2 | 1.04 | b2   |   21 |  
    |    3 | 3.14 | c3   |   22 |  
    |    4 | 4.35 | d4   |   23 |  
    +------+------+------+------+  
    4 rows in set (0.15 sec)  
    

On This Page

  * New User Registration and Organization Creation
    * Register and Login
    * Change Password
  * Warehouse and Cluster Creation
    * Create Warehouse
    * Create Cluster
  * Change Warehouse Password
  * Connect to Warehouse
    * Create Database
    * Create Data Table
    * Insert Data
    * Query Data
  * （OPTIONAL）Connect to Warehouse Using MySQL Client
    * IP Whitelist Management
    * MySQL Client
    * Create Database and Table
    * Query Data

