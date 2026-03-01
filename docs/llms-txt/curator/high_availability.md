# Source: https://docs.curator.interworks.com/setup/high_availability/high_availability.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# High Availability

> Configure Curator for high availability infrastructure to ensure reliability and handle increased load

Curator can be configured to run in a high availability (HA) infrastructure to ensure better "up time" for your users
as well as handling more concurrent user load.  The standard components of the HA infrastructure are:

* **Load balancer** - Domain name is pointed here.  Routes user traffic to one of the application nodes.
  Example: AWS Elastic Load Balancer (ELB).
* **Application nodes** (2 or more) - Where Curator is installed.
  Example: AWS Elastic Compute Cloud (EC2).
* **Database** - The application nodes will use this to store data.  Having a single database keeps things synchronized.
  Example: AWS Relational Database Service (RDS).
* **Filesystem** - The application nodes will use this to store thumbnails, backups, etc.
  Example: AWS Elastic File System (EFS).
  <img src="https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/high_availability/ha-diagram.png?fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=6290c4129c735addc9223b52c872033b" alt="HA diagram" data-og-width="1456" width="1456" data-og-height="614" height="614" data-path="assets/images/setup/high_availability/ha-diagram.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/high_availability/ha-diagram.png?w=280&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=d1429c4b1b2b6f74630fc9d4542ef27f 280w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/high_availability/ha-diagram.png?w=560&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=c51d12ffa6eace311fb6bb41b87830f0 560w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/high_availability/ha-diagram.png?w=840&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=e1d00f16935c6ae3e0479bc383d74bca 840w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/high_availability/ha-diagram.png?w=1100&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=5a7d0e82e0bf6b8e4b4ff057e285c69d 1100w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/high_availability/ha-diagram.png?w=1650&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=4af6faa44d40f1a1780ade9d8ed74c34 1650w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/high_availability/ha-diagram.png?w=2500&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=4e0c116f0204a004e5395fb1dc634da6 2500w" />
  *Note: the example above shows AWS services but Azure and other cloud providers are viable options.*

## Requirements

Below are the specific requirements for each component of the infrastructure and what needs to be completed prior to the
install.

* **Load Balancer**
  * This is where SSL will need to be handled.  The most common setup is to terminate SSL at the load balancer as
    opposed to having certificates on each application node.
  * **Prior to install:**  You don't need to have the load balancer ready prior to the install.  This can be configured afterwards.
* **Application nodes**
  * The same server requirements for the standard Curator installation exist for each application node.  Those
    requirements can be found here: [https://curator.interworks.com/requirements](https://curator.interworks.com/requirements).
  * **Prior to install:**  The application nodes need to be spun up and have root SSH or admin RDP access.  The SSH or
    RDP access should be tested before the installation.
* **Database**
  * The database should be *separate* from the application nodes.  Although it can be configured inside one of the
    application nodes it defeats the purpose of high availability because if that node goes down none of the others will
    be functional.
  * **Prior to install:**  The database needs to be spun up, an empty database needs to be created (it can be called
    `curator` for simplicity), and it needs to be accessible from each application node.  Test the accessibility from each
    application node with something like this:

    ```bash  theme={null}
    sudo mysql -u $DBUSER--password=$DBPASSWORD -h $DBHOST -e "SHOW DATABASES"
    ```

    Replace variables with your credentials and database host.  You should be able to see the empty database you created
    in the output.
* **Filesystem**
  * Like the database, the filesystem needs to be separate from the application nodes to prevent unnecessary downtime.
    Cloud services (AWS, Azure, etc.) have great options for this that have built in redundancy.  If you aren't using a
    cloud service and are using Windows for the infrastructure you can use the database node for the shared filesystem
    with a network drive.
  * **Prior to install:**  The filesystem needs to be spun up and accessible by each application node.  This should be
    tested by creating a simple text file and ensuring it's visible from each application node.

## Other Infrastructures

There are numerous ways to do high availability that include different patterns with the database and filesystem setups.
What's described above is certainly not the only method but it is the simplest for Curator.  We're happy to help
troubleshoot if you take a different route or run into issues with the infrastructure detailed above.  While we're
fully responsible for errors rising from the application code, the success of the infrastructure will be dependent on
your team that manages it.

## Post Install

Once the install and configuration is complete at the server-level make sure to go to the **Curator backend** >
**Settings** > **Curator** > **Worker Nodes** and add each application node to the list.  This will ensure when a
software upgrade is initiated or the application cache is cleared each node will stay synchronized.

### Worker Nodes

Worker nodes are essential for maintaining high availability and load balancing. Each worker node runs an instance of
Curator and shares the load of incoming requests. This setup ensures that if one node fails, others can continue to
handle the traffic, minimizing downtime and improving reliability.

#### Adding Worker Nodes (Command Line)

To register a worker node to your Curator cluster, you can use the  `distributed:addnode`  console command. This command
registers a new node with the cluster, allowing Curator to properly sync changes with it.

* **Open the terminal**  and navigate to the directory where Curator is installed.

* **Run the command**  with the IP address of the new node:

  ```bash  theme={null}
      php artisan distributed:addnode {Curator Node IP}
  ```

  Replace  `{Curator Node IP}`  with the actual IP address of the node you want to register.

* **Verify the node addition**: The command will output a confirmation message indicating that the node has been
  registered successfully, and you can find the newly added node in the **Curator backend** >**Settings** > **Curator** >
  **Worker Nodes**.

**Example:**

```bash  theme={null}
php artisan distributed:addnode "http://192.168.1.2"
```

This command will register the node with IP address  `192.168.1.2`  to the Curator cluster.

#### Adding Worker Nodes (In the Backend)

You can also register worker nodes directly through the Curator backend interface.

1. **Navigate** to the Curator backend > Settings > Curator > Worker Nodes.
2. **Add a new node**  by entering the URL (e.g.,  `http://192.168.1.2`) in the **URL** field.
3. **Save the changes**  to register the new node with the cluster.
