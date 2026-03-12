# Source: https://docs.acceldata.io/documentation/trino-installation-on-vm-with-openlineage.md

# Trino Installation on VM with OpenLineage

This guide explains how to install **Trino on a Linux virtual machine** and configure **OpenLineage integration** for capturing query lineage events.

The document covers:

- System preparation
- Trino installation

- Trino configuration
- OpenLineage plugin setup

- Starting and validating Trino
- Installing the Trino CLI

Running Trino as a system service.

## 1. System Preparation

Before installing Trino, update the system and install the required dependencies.

### Update the System

```bash
sudo apt update && sudo apt upgrade -y
```



### Install Java (Required for Trino)

```bash
sudo apt install -y openjdk-17-jdk
java -version
```



### Install Additional Utilities

```bash
sudo apt install -y wget curl jq
```



## 2. Install Trino

### Create the installation directory

```bash
sudo mkdir -p /opt/trino
cd /opt/trino
```



### Download the Trino server package

```bash
sudo wget https://repo1.maven.org/maven2/io/trino/trino-server/438/trino-server-438.tar.gz
```



### Extract and organize the installation

```bash
sudo tar -xzf trino-server-438.tar.gz
sudo mv trino-server-438 server
sudo rm trino-server-438.tar.gz
```



### Create required directories

```bash
sudo mkdir -p /var/trino/data
sudo mkdir -p /opt/trino/server/etc
sudo mkdir -p /opt/trino/server/etc/catalog
```



## 3. Configure Trino

Trino requires several configuration files located under:

```none
/opt/trino/server/etc
```



### Create node.properties

This file defines node identity and data directory.

```bash
sudo tee /opt/trino/server/etc/node.properties > /dev/null << 'EOF'
node.environment=production
node.id=trino-single-node
node.data-dir=/var/trino/data
EOF
```



### Create jvm.config

Configure JVM memory settings and adjust the `-Xmx` value according to your VM memory.

Example for an **8GB memory allocation**:

```bash
sudo tee /opt/trino/server/etc/jvm.config > /dev/null << 'EOF'
-server
-Xmx8G
-XX:InitialRAMPercentage=80
-XX:MaxRAMPercentage=80
-XX:+ExplicitGCInvokesConcurrent
-XX:+ExitOnOutOfMemoryError
-XX:+HeapDumpOnOutOfMemoryError
EOF
```



### Create config.properties

Defines Trino server behavior.

```bash
sudo tee /opt/trino/server/etc/config.properties > /dev/null << 'EOF'
coordinator=true
node-scheduler.include-coordinator=true
http-server.http.port=8080
discovery.uri=http://localhost:8080
EOF
```



### Configure Logging

```bash
sudo tee /opt/trino/server/etc/log.properties > /dev/null << 'EOF'
io.trino=INFO
EOF
```



### Configure a Test Catalog (TPC-H)

This creates a sample catalog for testing queries.

```bash
sudo tee /opt/trino/server/etc/catalog/tpch.properties > /dev/null << 'EOF'
connector.name=tpch
EOF
```



## 4. Install the OpenLineage Plugin

The OpenLineage plugin allows Trino to send lineage events to external systems.

### Navigate to the plugin directory

```bash
cd /opt/trino/server/plugin
```



### Create a directory for the OpenLineage plugin

```bash
sudo mkdir -p openlineage
cd openlineage
```



### Download the Plugin

```bash
sudo wget https://repo1.maven.org/maven2/io/openlineage/openlineage-trino/1.23.0/openlineage-trino-1.23.0.jar
```



### Verify the Installation

```bash
ls -lh
```



**Expected Output:** `openlineage-trino-1.23.0.jar`

## 5. Configure OpenLineage Event Listener

Create the **event listener configuration** file.

```bash
sudo tee /opt/trino/server/etc/event-listener.properties > /dev/null << 'EOF'
event-listener.name=openlineage

# Trino server URI
openlineage-event-listener.trino.uri=http://<YOUR_TRINO_HOST>:8080

# Transport configuration
openlineage-event-listener.transport.type=http
openlineage-event-listener.transport.url=https://<TENANT_NAME>.acceldata.app/torch-pipeline/api/v1/lineage

# Authentication headers
openlineage-event-listener.transport.headers=accessKey:<YOUR_ACCESS_KEY>,secretKey:<YOUR_SECRET_KEY>

# Query types to capture
openlineage-event-listener.trino.include-query-types=INSERT,MERGE,DELETE,UPDATE

# Namespace for lineage events
openlineage-event-listener.namespace=trino-production
EOF
```



Replace the following placeholders with your environment values:

| **Place Holder** | **Description** | 
| ---- | ---- | 
| `<YOUR_TRINO_HOST>` | Hostname or IP of the Trino server | 
| `<TENANT_NAME>` | Acceldata tenant name | 
| `<YOUR_ACCESS_KEY>` | Acceldata access key | 
| `<YOUR_SECRET_KEY>` | Acceldata secret key | 


## 6. Set Directory Ownership

Ensure the correct user owns the directories.

```bash
sudo chown -R $USER:$USER /opt/trino
sudo chown -R $USER:$USER /var/trino
```



## 7. Start Trino

**Navigate to the Trino installation**

```bash
cd /opt/trino/server
```



**Start the server**

```bash
./bin/launcher start
```



**Check the server status**

```bash
./bin/launcher status
```



Wait for the server to initialize.

```bash
sleep 30
```



## 8. Verify OpenLineage Initialization

Check logs to confirm the OpenLineage listener is registered.

```bash
grep -i "openlineage" /var/trino/data/var/log/server.log
```



Expected log message:

```none
Registered event listener openlineage
```



## 9. Verify Trino is Running

```bash
sudo netstat -tlnp | grep 8080
```



If successful, the output should show port **8080** listening.

## 10. Install Trino CLI

The CLI allows you to run queries from the command line.

### Download the CLI

```bash
cd /tmp
wget https://repo1.maven.org/maven2/io/trino/trino-cli/438/trino-cli-438-executable.jar
```



### Install the CLI

```bash
sudo mv trino-cli-438-executable.jar /usr/local/bin/trino
sudo chmod +x /usr/local/bin/trino
```



### Verify installation

```bash
trino --version
```



## 11. Connect to Trino

Run the following command to connect to the server.

```bash
trino --server localhost:8080 --catalog tpch --schema tiny
```



You can now run SQL queries.

Example:

```sql
SELECT * FROM nation;
```



## 12. Run Trino as a systemd Service (Recommended)

Running Trino as a system service ensures it **automatically starts after system reboot**.

### Create a Trino Service User

```bash
sudo useradd -r -s /bin/false trin
```



### Assign Ownership

```bash
sudo chown -R trino:trino /opt/trino
sudo chown -R trino:trino /var/trino
```



### Stop the Manually Running Instance

```bash
cd /opt/trino/server
./bin/launcher stop
```



### Create the systemd Service File

```bash
sudo tee /etc/systemd/system/trino.service > /dev/null << 'EOF'
[Unit]
Description=Trino Server
After=network.target

[Service]
Type=forking
User=trino
Group=trino
ExecStart=/opt/trino/server/bin/launcher start
ExecStop=/opt/trino/server/bin/launcher stop
Restart=on-failure
RestartSec=10

[Install]
WantedBy=multi-user.target
EOF
```



### Enable and Start the Service

**Reload systemd:**

```bash
sudo systemctl daemon-reload
```



**Enable Trino at boot:**

```bash
sudo systemctl enable trino
```



**Start the service:**

```bash
sudo systemctl start trino
```



### Verify Service Status

```bash
sudo systemctl status trino
```



## Installation Complete

You have successfully:

- Installed **Trino**
 

- Configured **TPC-H test catalog**
 

- Integrated **OpenLineage**
 

- Installed the **Trino CLI**
 

- Configured Trino as a **system service**
 

Trino is now ready for running queries and emitting lineage events to your configured OpenLineage endpoint.