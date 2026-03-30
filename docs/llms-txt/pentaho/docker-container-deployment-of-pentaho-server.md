# Source: https://docs.pentaho.com/install/pentaho-installation-overview-cp/docker-container-deployment-of-pentaho-server.md

# Docker container deployment of Pentaho Server

You can use Docker Compose to deploy Pentaho Server as a container and, optionally, to install Pentaho Server plugins during deployment in any of the following supported environments:

* On‑premises
* Amazon Web Services (AWS)
* Google Cloud Platform (GCP)
* Microsoft Azure

## Download Pentaho Server Docker files

To deploy Pentaho Server as a container using Docker Compose, you must first download both the `.gz` file that contains the Docker image and the ZIP file that contains the configuration files for your environment.

Complete the following steps to download the ZIP files that you need for deploying Pentaho Server as a container:

1. On the [Support Portal](https://support.pentaho.com/hc/en-us) home page, sign in using the Pentaho Support username and password provided in your Pentaho Welcome Packet.
2. In the Pentaho card, click **Download**. The Downloads page opens.
3. In the **11.x** list, click **Pentaho 11.0 GA Release**.
4. Scroll to the bottom of the Pentaho 11.0 GA Release page.
5. In the file component section, navigate to the `Docker Image Configurator/Images` directory.
6. Download the `pentaho-server-11.0.0.0-<build number>.tar.gz` file.&#x20;
7. In the file component section, navigate to the `Docker Image Configurator/Environment Config` directory.
8. Download one of the following ZIP files that contain the configuration files for your environment:
   * `aws-11.0.0.0-<build number>.zip`
   * `azure-11.0.0.0-<build number>.zip`
   * `gcp-11.0.0.0-<build number>.zip`
   * `on-prem-11.0.0.0-<build number>.zip`

**What to do next:**&#x20;

* If you want to install Pentaho Server plugins (Dashboard Designer, Interactive Reporting, and Pentaho Analyzer) during deployment, [download the necessary plugin files](#download-plugin-files).
* If you want to deploy the Pentaho Server as a container without installing plugins, go to the instructions for deploying Pentaho Server in your environment:
  * [Deploy Pentaho Server on premises](#deploy-pentaho-server-on-premises)
  * [Deploy Pentaho Server on Kubernetes in the Cloud](#deploy-pentaho-server-on-kubernetes-in-the-cloud)
    * [Amazon Web Services](#deploy-on-amazon-web-services)
    * [Google Cloud Platform](#deploy-on-google-cloud-platform)
    * [Microsoft Azure](#deploy-on-microsoft-azure)

## Download plugin files

To install Pentaho Server plugins you must download the ZIP files that contain the plugin files.

Complete the following steps to download the ZIP files you need for installing plugins:

1. On the [Support Portal](https://support.pentaho.com/hc/en-us) home page, sign in using the Pentaho Support username and password provided in your Pentaho Welcome Packet.
2. In the Pentaho card, click **Download**. The Downloads page opens.
3. In the **11.x** list, click **Pentaho 11.0 GA Release**.
4. Scroll to the bottom of the Pentaho 11.0 GA Release page.
5. In the file component section, navigate to `Pentaho Server/Archive Build (Suggested Installation Method)`.
6. Download the files for one or more of the following plugins:
   * Dashboard Designer Plugin: `pdd-plugin-ee-11.0.0.0-<build number>.zip`
   * Interactive Reporting Plugin: `pir-plugin-ee-11.0.0.0-<build number>.zip`
   * Pentaho Analyzer Plugin: `paz-plugin-ee-11.0.0.0-<build number>.zip`
7. Extract the plugin ZIP files to a temporary directory. The extracted directories contain the following subdirectories are needed for installing the plugins:
   * `pentaho-interactive-reporting`
   * `dashboards`
   * `analyzer`

{% hint style="info" %}
**Note:** If you do not install plugins during the first deployment of the Pentaho Server, you can install them later. For instructions, see [Install Pentaho Server plugins after deployment](#install-pentaho-server-plugins-after-deployment).
{% endhint %}

## Deploy Pentaho Server on premises

You can use Docker Compose to deploy Pentaho Server as a container on a local machine, AWS EC2 instance, Google Cloud Platform virtual machine (VM), or Microsoft Azure VM.

On-premises deployment is suitable for the following environments:

* Evaluation environments.
* Development and test environments.
* Production environments with an external database, persistent volumes, backups, and security hardening.

**Best practices for production environments**

* Use an external, managed database—such as Amazon Relational Database Service, Microsoft Azure Database, Google Cloud SQL, or a corporate-managed database—instead of the bundled database container.
* Mount persistent storage for solutions, data, logs, and licenses.
* Configure HTTPS.
* Regularly back up your volumes and database.
* Monitor your deployment with Docker logs, cloud metrics, and alerts.
* Apply security patches to your operating system and Docker.

**Before you begin**

Before you can deploy to an on-premises host, you must complete the following tasks:

* Create a Docker account.

  <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>Note:</strong> For help with Docker and Docker Hub, see the online documentation at <a href="https://docs.docker.com/">https://docs.docker.com/</a>. </p></div>
* On the host, install Docker Engine and Docker Compose.
* Download both the ZIP file that contains the Docker image and the ZIP file that contains the configuration files for your environment. For instructions downloading Docker files, see the previous section, [Download Docker container files](#download-docker-container-files).
* (Optional) [Download plugin files](#download-plugin-files) for installing the plugins during deployment.

{% hint style="info" %}
**Note:** For help with Docker and Docker Hub, see the online documentation at <https://docs.docker.com/>.&#x20;
{% endhint %}

**Procedure**

Complete the following steps to deploy Pentaho Server as a container, on premises:

1. On your host, extract the `on-prem-11.0.0.0-<build number>.zip` ZIP file to a temporary working directory.
2. In your working directory, open a command prompt.
3. (Optional) If you are not logged in, log into Docker Hub using the following command: `docker login`
4. Load the Pentaho Server Docker image by running the following command, replacing `<build number>` with the build number in the downloaded file:&#x20;

   ```
   docker load -i pentaho-server-11.0.0.0-<build number>.tar.gz
   ```

   You can verify that the Pentaho Server image is loaded in Docker Desktop.
5. In your working directory, go to the `on-prem-11.0.0.0-<build number>/dist/on-prem/pentaho-server` subdirectory.&#x20;
6. Open one of the following directories based on your database type:
   * `pentaho-server-mysql`
   * `pentaho-server-oracle`
   * `pentaho-server-postgres`
   * `pentaho-server-sqlserver`
7. In a text editor, open the `.env` file and configure variables for your environment.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>Important:</strong> You must enter the URL for your Pentaho license.</p></div>

   The contents of the `.env` file vary slightly for each database and include comments to assist you with editing the file. The following code is an example of the `.env` file contents used for a PostgreSQL database.

   <pre data-overflow="wrap" data-expandable="true"><code>#Pentaho version to be used
   PENTAHO_IMAGE_NAME=one.hitachivantara.com/pntprv-docker-dev/pentaho/pdia-image-configurator/pentaho-server
   PENTAHO_VERSION=11.0.0.0-xxx
   INSTALLATION_PATH=/opt/pentaho
   PENTAHO_HOME=/home/pentaho

   #Override subfolder name
   SOFTWARE_OVERRIDE_FOLDER=./softwareOverride
   LOG_FOLDER=./logs
   CONFIG_FOLDER=./config

   #Port number to expose for server
   PORT=8080
   LICENSE_URL=your_Pentaho_license_URL

   #The version of the database to use
   DATABASE_VERSION=
   #The database edition to use, if any
   DATABASE_EDITION=
   #The docker image to use for the database
   DOCKER_DATABASE_IMAGE=postgres:${DATABASE_VERSION}
   </code></pre>
8. Save and close the `.env` file.
9. (Optional) To install Pentaho Server plugins during deployment, place the directory for each plugin in the `softwareOverride\2_repository\pentaho-solutions\system` subdirectory for your database type. The following subdirectories are needed for installing the plugins:

   * `pentaho-interactive-reporting`
   * `dashboards`
   * `analyzer`

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>Note:</strong> For instructions downloading plugin files, see <a href="#download-plugin-files">Download plugin files</a>.</p></div>
10. (Optional) To change the default administrator password before deploying the Pentaho Server and database, go to the in the `softwareOverride\2_repository\pentaho-solutions\system` subdirectory and update the `defaultUser.spring.properties` and `repository.spring.properties` files. For instructions, see [Change the default administrator password](#change-the-default-administrator-password).
11. In your command prompt, change to the directory for your database type.
12. Deploy the Pentaho Server as a container and create the database volume by running one of the following commands based on your database type:&#x20;
    * `docker compose -f docker-compose-mysql.yaml up`
    * `docker compose -f docker-compose-postgres.yaml up`
    * `docker compose -f docker-compose-sqlserver.yaml up`
    * `docker compose -f docker-compose-oracle.yaml up`
13. Verify that Pentaho Server is running by accessing it at `http://localhost:<port>/pentaho` or your proxy URL.

### Troubleshooting on-premises deployment

The following table lists the symptoms, causes, and suggested fixes for common issues related to on-premises deployments of Pentaho Server as a container.

| Symptom                                      | Cause                    | Fix                                                                                                                                                                                                                                                   |
| -------------------------------------------- | ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Pentaho Server container restarts repeatedly | Insufficient memory      | Increase the JVM -Xmx or VM size.                                                                                                                                                                                                                     |
| Cannot access web UI                         | Port blocked by firewall | <p>Open the port for your local host in the security group, Network Security Group, or firewall. </p><div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>Note:</strong> The default port is 8080.</p></div> |
| DB connection errors                         | Wrong `.env` values      | Verify the values for  `DB_HOST`, `DB_USER`, `DB_PASSWORD` in the `.env` file.                                                                                                                                                                        |
| Slow performance                             | Under-powered VM         | Use recommended size, allocate more resources.                                                                                                                                                                                                        |

## Deploy Pentaho Server on Kubernetes in the cloud

You can deploy the Pentaho Server as a container on Kubernetes in any of the following cloud environments:

* [Amazon Web Services](#deploy-on-amazon-web-services)
* [Google Cloud Platform](#deploy-on-google-cloud-platform)
* [Microsoft Azure](#deploy-on-microsoft-azure)

**Before you begin**

Before you can deploy Pentaho Server using Kubernetes, you must create a Docker account.

{% hint style="info" %}
Note: For help with Docker and Docker Hub, see the online documentation at <https://docs.docker.com/>.&#x20;
{% endhint %}

### Deploy on Amazon Web Services

To deploy on Amazon Web Services (AWS) using Elastic Kubernetes Service (EKS), you must complete the following tasks, in order:

1. [Tag and push Pentaho Server Docker image to AWS](#tag-and-push-pentaho-server-docker-image-to-aws)
2. [Create a database instance in AWS](#create-a-database-instance-in-aws)
3. [Configure storage in AWS S3 bucket](#configure-storage-in-aws-s3-bucket)
4. [Check in logs in Kubernetes pods](#check-in-logs-in-kubernetes-pods)

Before you begin, complete the following tasks:

* Create a Docker account.

  <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>Note:</strong> For help with Docker and Docker Hub, see the online documentation at <a href="https://docs.docker.com/">https://docs.docker.com/</a>. </p></div>
* Verify you have access to a standard Amazon EKS cluster.
* Verify that you have an approved S3 CSI or FUSE-based approach. (Used for configs, logs, and overrides and required if your package YAMLs reference S3 buckets for configuration or storage paths.)
* If you plan to pull Pentaho images from Amazon Elastic Container Registry (ECR), or a mirrored ECR, confirm that the node instance role or IRSA-enabled service account has permission to pull images.
* Install `kubectl` and AWS CLI.
* Set up your local `kubeconfig` so that `kubectl` can communicate with the cluster by running the following command, replacing `<name>` and `<region>`:

  ```shellscript
  aws eks update-kubeconfig --<name> --<region>
  ```
* Download both the ZIP file that contains the Docker image and the ZIP file that contains the configuration files for your environment. For instructions downloading Docker files, see the previous section, [Download Docker container files](#download-docker-container-files).

#### Tag and push Pentaho Server Docker image to AWS

To tag the Pentaho Server Docker image and upload it to AWS, complete the following steps:

1. In your working directory, open a command prompt from that subdirectory.
2. (Optional) If you are not logged in, log into Docker Hub using the following command: `docker login`.
3. Authenticate to ECR by running the following command, replacing `<aws region>` and `<aws account id>`: &#x20;

   <pre class="language-shellscript" data-overflow="wrap"><code class="lang-shellscript">aws ecr get-login-password --region &#x3C;aws region> \
     | docker login --username AWS --password-stdin &#x3C;aws account id>.dkr.ecr.&#x3C;aws region>.amazonaws.com
   </code></pre>
4. Tag and push the Pentaho Server Docker image by running the following command, replacing `<build number>`, `<aws account id>`, and `<region>` with the values from the downloaded file and your AWS account:

   <pre class="language-shellscript" data-overflow="wrap"><code class="lang-shellscript">docker tag pentaho/pentaho-server:11.0.0.0-&#x3C;build number>&#x3C;aws account id>.dkr.ecr.&#x3C;region>.amazonaws.com/dockmaker-pentaho-server:&#x3C;build number> 
   docker push &#x3C;aws account id>.dkr.ecr.&#x3C;region>.amazonaws.com/dockmaker-pentaho-server:&#x3C;build number>
   </code></pre>

   The Pentaho Server Docker image is tagged and pushed to AWS.

#### Create a database instance in AWS

To create a database instance in AWS, complete the following steps:

1. On your local workstation, extract the `aws-11.0.0.0-<build number>.zip` file to a temporary working directory.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>Note:</strong> For instructions on downloading the ZIP file, see the previous section, <a href="#download-docker-container-files">Download Docker container files</a>.</p></div>
2. In your working directory, go to the `aws-11.0.0.0-<build number>/dist/aws/pentaho-server` subdirectory.&#x20;
3. Open one of the following directories based on your database type:
   * `pentaho-server-mysql`
   * `pentaho-server-oracle`
   * `pentaho-server-postgres`
   * `pentaho-server-sqlserver`
4. Go to the `db_init_<database type>` subdirectory and open a command prompt from that subdirectory.
5. Send the `.sql` files in the  `db_init_<database type>` subdirectory to your EC2 instance by running the following commands, replacing `<your private key>`, `<database type>`, `<ssh username>`, `<e2c instance public ip>`, and `<region>`:

   <pre class="language-shellscript" data-overflow="wrap"><code class="lang-shellscript">scp -i "&#x3C;your private key>.pem" "1-create_quartz_&#x3C;database type>.sql" "&#x3C;ssh username>@ec2-&#x3C;e2c instance public ip>.&#x3C;region>.compute.amazonaws.com:/home/&#x3C;ssh username>"
   scp -i "&#x3C;your private key>.pem" "2-create_repository_&#x3C;database type>.sql" "&#x3C;ssh username>@ec2-&#x3C;e2c instance public ip>.&#x3C;region>.compute.amazonaws.com:/home/&#x3C;ssh username>"
   scp -i "&#x3C;your private key>.pem" "3-create_jcr_&#x3C;database type>.sql" "&#x3C;ssh username>@ec2-&#x3C;e2c instance public ip>.&#x3C;region>.compute.amazonaws.com:/home/&#x3C;ssh username>"
   scp -i "&#x3C;your private key>.pem" "4-pentaho_mart_&#x3C;database type>.sql" "&#x3C;ssh username>@ec2-&#x3C;e2c instance public ip>.&#x3C;region>.compute.amazonaws.com:/home/&#x3C;ssh username>"
   scp -i "&#x3C;your private key>.pem" "5-pentaho_logging_&#x3C;database type>.sql" "&#x3C;ssh username>@ec2-&#x3C;e2c instance public ip>.&#x3C;region>.compute.amazonaws.com:/home/&#x3C;ssh username>"
   </code></pre>
6. Connect to RDS from EC2. The following command is an example for connecting to RDS from EC2 for a PostgreSQL database.&#x20;

   <pre class="language-shellscript" data-overflow="wrap"><code class="lang-shellscript">psql --host=&#x3C;rds endpoint> --port=&#x3C;database port> --username=&#x3C;database username> --dbname=&#x3C;database name>
   </code></pre>
7. Run the `.sql` files from EC2. The following commands are examples for running .`sql` files from EC2 for a PostgreSQL database.

   <pre class="language-shellscript" data-overflow="wrap"><code class="lang-shellscript">psql -U &#x3C;database username> -d &#x3C;database-name> -h &#x3C;rds endpoint> -v passwd=&#x3C;database password> -f /home/&#x3C;ssh username>/1_create_jcr_&#x3C;database>.sql
   psql -U &#x3C;database username> -d &#x3C;database-name> -h &#x3C;rds endpoint> -v passwd=&#x3C;database password> -f /home/&#x3C;ssh username>/2_create_quartz_&#x3C;database>.sql
   psql -U &#x3C;database username> -d &#x3C;database-name> -h &#x3C;rds endpoint> -v passwd=&#x3C;database password> -f /home/&#x3C;ssh username>/3_create_repository_&#x3C;database>.sql
   psql -U &#x3C;database username> -d &#x3C;database-name> -h &#x3C;rds endpoint> -v passwd=&#x3C;database password> -f /home/&#x3C;ssh username>/4_pentaho_logging_&#x3C;database>.sql
   psql -U &#x3C;database username> -d &#x3C;database-name> -h &#x3C;rds endpoint> -v passwd=&#x3C;database password> -f /home/&#x3C;ssh username>/5_pentaho_mart_&#x3C;database>.sql
   </code></pre>

   The database instance is created in AWS.

#### Configure storage in AWS S3 buckets

To configure storage in AWS S3 buckets, complete the following steps:&#x20;

1. In your working directory, go to the `aws-11.0.0.0-<build number>/dist/aws/pentaho-server` subdirectory.&#x20;

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>Note:</strong> You downloaded and extracted the  <code>aws-11.0.0.0-&#x3C;build number>.zip</code> file in the previous sections, <a href="#download-docker-container-files">Download Docker container files</a> and <a href="#create-a-database-instance-in-aws">Create a database instance in AWS</a>.</p></div>
2. Open one of the following directories based on your database type:
   * `pentaho-server-mysql`
   * `pentaho-server-oracle`
   * `pentaho-server-postgres`
   * `pentaho-server-sqlserver`
3. Open the `.yaml` file in a text editor and configure values for your environment. You must update the following values before deploying the Pentaho Server:

   ```yaml
     # Replace <path to bucket>
     mountOptions:
       - region <path to bucket>
       - prefix <path to bucket>  
   ```

   ```yaml
    # Replace <name of bucket>
    csi:
       volumeAttributes:
         bucketName: <name of bucket>
   ```

   <pre class="language-yaml" data-overflow="wrap"><code class="lang-yaml"># Replace &#x3C;aws account id>, &#x3C;region>, &#x3C;repository>, and &#x3C;build number>
   containers:
           - name: pentaho-server
             image: &#x3C;aws account id>.dkr.ecr.&#x3C;region>.amazonaws.com/&#x3C;repository>/pentaho-server:11.0.0.0-&#x3C;build number>
   </code></pre>

   ```yaml
   # Replace <your license URL>
   env:
      - name: LICENSE_URL
        value: "<your license URL>"
   ```

   The contents of the `.yaml` file vary slightly for each database and include comments to assist you with editing the file. The following code is an example of the `.yaml` file contents used for a PostgreSQL database when deploying to AWS.

   <pre class="language-yaml" data-overflow="wrap" data-full-width="true" data-expandable="true"><code class="lang-yaml">---
   apiVersion: storage.k8s.io/v1
   kind: StorageClass
   metadata:
     name: s3-storage-class
   provisioner: s3.csi.aws.com
   ---
   apiVersion: v1
   kind: Namespace
   metadata:
     name: pentaho-server
   ---
   apiVersion: v1
   kind: ServiceAccount
   metadata:
     name: pentaho-server-s3-access
     namespace: pentaho-server
     annotations:
       eks.amazonaws.com/role-arn: arn:aws:iam::524647911006:role/dockmaker-role-ps
   ---
   # PV + PVC for softwareOverride
   apiVersion: v1
   kind: PersistentVolume
   metadata:
     name: s3-pv-softwareoverride
   spec:
     capacity:
       storage: 1Gi
     accessModes:
       - ReadWriteMany
     storageClassName: s3-storage-class
     claimRef: # To ensure no other PVCs can claim this PV
       namespace: pentaho-server # Namespace is required even though it's in "default" namespace.
       name: s3-pvc-softwareoverride # Name of your PVC
     volumeMode: Filesystem
     mountOptions:
       - allow-other
       - region us-east-1
       - prefix dockmaker/postgresql/softwareOverride/
     csi:
       driver: s3.csi.aws.com
       volumeHandle: s3-softwareoverride
       volumeAttributes:
         bucketName: ackbar-development
         mountOptions: "uid=5000,gid=5000,file-mode=0770,dir-mode=0770"
   ---
   apiVersion: v1
   kind: PersistentVolumeClaim
   metadata:
     name: s3-pvc-softwareoverride
     namespace: pentaho-server
   spec:
     accessModes:
       - ReadWriteMany
     storageClassName: s3-storage-class
     volumeMode: Filesystem
     resources:
       requests:
         storage: 1Gi
     volumeName: s3-pv-softwareoverride
   ---
   # PV + PVC for config
   apiVersion: v1
   kind: PersistentVolume
   metadata:
     name: s3-pv-config
   spec:
     capacity:
       storage: 1Gi
     accessModes:
       - ReadWriteMany
     storageClassName: s3-storage-class
     claimRef: # To ensure no other PVCs can claim this PV
       namespace: pentaho-server # Namespace is required even though it's in "default" namespace.
       name: s3-pvc-config # Name of your PVC
     volumeMode: Filesystem
     mountOptions:
       - allow-other
       - region us-east-1
       - prefix dockmaker/postgresql/config/
     csi:
       driver: s3.csi.aws.com
       volumeHandle: s3-config
       volumeAttributes:
         bucketName: ackbar-development
         mountOptions: "uid=5000,gid=5000,file-mode=0770,dir-mode=0770"
   ---
   apiVersion: v1
   kind: PersistentVolumeClaim
   metadata:
     name: s3-pvc-config
     namespace: pentaho-server
   spec:
     accessModes:
       - ReadWriteMany
     storageClassName: s3-storage-class
     volumeMode: Filesystem
     resources:
       requests:
         storage: 1Gi
     volumeName: s3-pv-config
   ---
   # PV + PVC for logs
   apiVersion: v1
   kind: PersistentVolume
   metadata:
     name: s3-pv-logs
   spec:
     capacity:
       storage: 1Gi
     accessModes:
       - ReadWriteMany
     storageClassName: s3-storage-class
     claimRef: # To ensure no other PVCs can claim this PV
       namespace: pentaho-server # Namespace is required even though it's in "default" namespace.
       name: s3-pvc-logs # Name of your PVC
     volumeMode: Filesystem
     mountOptions:
       - allow-other
       - region us-east-1
       - prefix dockmaker/postgresql/logs/
     csi:
       driver: s3.csi.aws.com
       volumeHandle: s3-logs
       volumeAttributes:
         bucketName: ackbar-development
         mountOptions: "uid=5000,gid=5000,file-mode=0770,dir-mode=0770"
   ---
   apiVersion: v1
   kind: PersistentVolumeClaim
   metadata:
     name: s3-pvc-logs
     namespace: pentaho-server
   spec:
     accessModes:
       - ReadWriteMany
     storageClassName: s3-storage-class
     volumeMode: Filesystem
     resources:
       requests:
         storage: 1Gi
     volumeName: s3-pv-logs
   ---
   apiVersion: v1
   kind: Secret
   metadata:
     name: pentaho-license
     namespace: pentaho-server
   ---
   apiVersion: apps/v1
   kind: Deployment
   metadata:
     name: pentaho-server
     namespace: pentaho-server
   spec:
     replicas: 1
     selector:
       matchLabels:
         app: pentaho-server
     strategy:
       type: RollingUpdate
       rollingUpdate:
         maxSurge: 25%
         maxUnavailable: 25%
     template:
       metadata:
         labels:
           app: pentaho-server
           dinode: active
       spec:
         serviceAccountName: pentaho-server-s3-access
         securityContext:
           runAsUser: 5000
           runAsGroup: 5000
           runAsNonRoot: true
         volumes:
           - name: softwareoverride
             persistentVolumeClaim:
               claimName: s3-pvc-softwareoverride
           - name: config
             persistentVolumeClaim:
               claimName: s3-pvc-config
           - name: logs
             emptyDir: {}
           - name: pentaho-license
             secret:
               secretName: pentaho-license
               optional: true
         containers:
           - name: pentaho-server
             image: 524647911006.dkr.ecr.us-east-2.amazonaws.com/dockmaker/pentaho-server:11.0.0.0-18
             imagePullPolicy: "Always"
             resources:
               limits:
                 memory: "4500Mi"
               requests:
                 memory: "2000Mi"
             ports:
               - containerPort: 8080
             volumeMounts:
               - name: softwareoverride
                 mountPath: /docker-entrypoint-init/
               - name: config
                 mountPath: /mnt/config
               - name: logs
                 mountPath: /opt/pentaho/pentaho-server/tomcat/logs
             env:
               - name: LICENSE_URL
                 value: "your_Pentaho_license_URL"
           - name: s3-ps
             image: amazon/aws-cli:2.15.0
             imagePullPolicy: Always
             command:
               - /bin/sh
               - -c
             args:
               - |
                 while true; do
                   echo "Uploading logs to S3"
                   aws s3 sync /logs s3://ackbar-development/dockmaker/postgresql/logs/ --region us-east-2
                   sleep 60
                 done
             env:
               - name: HOME
                 value: /tmp
             volumeMounts:
               - name: logs
                 mountPath: /logs
   ---
   apiVersion: v1
   kind: Service
   metadata:
     name: pentaho-server-service
     namespace: pentaho-server
     labels:
       app: pentaho-server-service
   spec:
     type: ClusterIP
     selector:
       app: pentaho-server
       dinode: active
     ports:
       - name: http
         port: 8080
         targetPort: 8080
         protocol: TCP
       - name: database
         port: 3306
         targetPort: 3306
         protocol: TCP
   ---
   apiVersion: networking.k8s.io/v1
   kind: Ingress
   metadata:
     namespace: pentaho-server
     name: pentaho-server-ingress
     annotations:
       nginx.ingress.kubernetes.io/affinity: "cookie"
       nginx.ingress.kubernetes.io/affinity-mode: "persistent"
       nginx.ingress.kubernetes.io/session-cookie-name: "http-cookie"
       nginx.ingress.kubernetes.io/session-cookie-expires: "172800"
       nginx.ingress.kubernetes.io/session-cookie-max-age: "172800"
   spec:
     ingressClassName: nginx
     rules:
       - http:
           paths:
             - path: "/"
               pathType: Prefix
               backend:
                 service:
                   name: pentaho-server-service
                   port:
                     number: 8080
   </code></pre>
4. Save and close the `.yaml` file.
5. Go to the `softwareOverride/2_repository/tomcat/webapps/pentaho/META-INF` subdirectory.
6. Open the `context.xml` file in a text editor and update the database URL everywhere it appears. The following code is an example of the content in the `context.xml` file for a PostgreSQL database. In this example, the database instance URL is `jdbc:postgresql://repository:5432/hibernate`.

   <pre class="language-xml" data-overflow="wrap" data-expandable="true"><code class="lang-xml">&#x3C;Context path="/pentaho" docbase="webapps/pentaho/">
     &#x3C;Resource name="jdbc/Hibernate" auth="Container" type="javax.sql.DataSource"
               factory="org.pentaho.di.core.database.util.DecryptingDataSourceFactory" maxActive="20" minIdle="0" maxIdle="5" initialSize="0"
               maxWait="10000" username="hibuser" password="password"
               driverClassName="org.postgresql.Driver" url="jdbc:postgresql://repository:5432/hibernate"
               validationQuery="select 1" jdbcInterceptors="ConnectionState" defaultAutoCommit="true"/>

     &#x3C;Resource name="jdbc/Audit" auth="Container" type="javax.sql.DataSource"
               factory="org.pentaho.di.core.database.util.DecryptingDataSourceFactory" maxActive="20" minIdle="0" maxIdle="5" initialSize="0"
               maxWait="10000" username="hibuser" password="password"
               driverClassName="org.postgresql.Driver" url="jdbc:postgresql://repository:5432/hibernate"
               validationQuery="select 1" />

     &#x3C;Resource name="jdbc/Quartz" auth="Container" type="javax.sql.DataSource"
               factory="org.pentaho.di.core.database.util.DecryptingDataSourceFactory" maxActive="20" minIdle="0" maxIdle="5" initialSize="0"
               maxWait="10000" username="pentaho_user" password="password" testOnBorrow="true"
               driverClassName="org.postgresql.Driver" url="jdbc:postgresql://repository:5432/quartz"
               validationQuery="select 1"/>

     &#x3C;Resource name="jdbc/PDI_Operations_Mart" auth="Container" type="javax.sql.DataSource"
               factory="org.pentaho.di.core.database.util.DecryptingDataSourceFactory" maxActive="20" minIdle="0" maxIdle="5" initialSize="0"
               maxWait="10000" username="hibuser" password="password"
               driverClassName="org.postgresql.Driver" url="jdbc:postgresql://repository:5432/hibernate"
               validationQuery="select 1"/>

     &#x3C;Resource name="jdbc/pentaho_operations_mart" auth="Container" type="javax.sql.DataSource"
               factory="org.pentaho.di.core.database.util.DecryptingDataSourceFactory" maxActive="20" minIdle="0" maxIdle="5" initialSize="0"
               maxWait="10000" username="hibuser" password="password"
               driverClassName="org.postgresql.Driver" url="jdbc:postgresql://repository:5432/hibernate"
               validationQuery="select 1"/>

    &#x3C;Resource name="jdbc/live_logging_info" auth="Container" type="javax.sql.DataSource"
               factory="org.pentaho.di.core.database.util.DecryptingDataSourceFactory" maxActive="20" minIdle="0" maxIdle="5" initialSize="0"
               maxWait="10000" username="hibuser" password="password"
               driverClassName="org.postgresql.Driver" url="jdbc:postgresql://repository:5432/hibernate?searchpath=pentaho_dilogs"
               validationQuery="select 1"/>

     &#x3C;Resource name="jdbc/SampleData" auth="Container" type="javax.sql.DataSource"
               factory="org.pentaho.di.core.database.util.DecryptingDataSourceFactory" maxActive="20" minIdle="0" maxIdle="5" initialSize="0"
               maxWait="10000" username="sa" password=""
               driverClassName="org.hsqldb.jdbcDriver" url="jdbc:hsqldb:hsql://localhost/sampledata"
               validationQuery="select 1"/>

     &#x3C;Resource name="jdbc/SampleDataAdmin" auth="Container" type="javax.sql.DataSource"
               factory="org.pentaho.di.core.database.util.DecryptingDataSourceFactory" maxActive="20" minIdle="0" maxIdle="5" initialSize="0"
               maxWait="10000" username="sa" password=""
               driverClassName="org.hsqldb.jdbcDriver" url="jdbc:hsqldb:hsql://localhost/sampledata"
               validationQuery="select 1"/>

     &#x3C;Resource name="jdbc/jackrabbit" auth="Container" type="javax.sql.DataSource"
               factory="org.pentaho.di.core.database.util.DecryptingDataSourceFactory" maxActive="20" minIdle="0"
               maxIdle="5" initialSize="0"
               maxWait="10000" username="jcr_user" password="password"
               driverClassName="org.postgresql.Driver"
               url="jdbc:postgresql://repository:5432/jackrabbit"
               validationQuery="select 1"/>
               &#x3C;!--
               url="jdbc:mysql://localhost:3306/jackrabbit"/>
               url="jdbc:oracle:thin:@localhost:1521/XE"/>
               url="jdbc:sqlserver://localhost:1433;DatabaseName=jackrabbit"/>
               -->
   &#x3C;/Context>
   </code></pre>
7. (Optional) To install Pentaho Server plugins during deployment, place the directory for each plugin in the `softwareOverride\2_repository\pentaho-solutions\system` subdirectory for your database type. The following subdirectories that are needed for installing the plugins:

   * `pentaho-interactive-reporting`
   * `dashboards`
   * `analyzer`

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>Note:</strong> For instructions downloading plugin files, see <a href="#download-plugin-files">Download plugin files</a>.</p></div>
8. (Optional) To change the default administrator password before deploying the Pentaho Server, go to the in the `softwareOverride\2_repository\pentaho-solutions\system` subdirectory and update the `defaultUser.spring.properties` and `repository.spring.properties` files. For instructions, see [Change the default administrator password](#change-the-default-administrator-password).
9. In your EKS cluster, create an S3 bucket for each of the following subdirectories that appear in the  `aws-11.0.0.0-<build number>/dist/aws/pentaho-server/<database>` directory:
   1. `config`
   2. `logs`
   3. `softwareOverride`
10. Upload the contents of each subdirectory to the corresponding S3 bucket that you created for them.
11. Go back to the `aws-11.0.0.0-<build number>/dist/aws/pentaho-server/<database>` directory, which contains your database `.yaml` file, and open a command prompt from that directory.&#x20;
12. In the command prompt, create the persistent volumes and persistent volume claims, then deploy the Pentaho Server to the Kubernetes cluster by running the following command. Replace `<database>` with the database name defined in the `.yaml` file:

    ```shellscript
    kubectl apply -f pentaho-server-aws-<database>.yaml
    ```

    The Pentaho Server is deployed with the storage you configured in the AWS S3 bucket.

#### Check in logs in Kubernetes pods

To check in logs in Kubernetes pods, complete the following steps:

1. In a command prompt, check in logs in Kubernetes pods by running the following commands, in order:

   ```shellscript
   # List all pods across every namespace
   kubectl get pods --all-namespaces

   # View logs for a specific pod (all containers) in a namespace
   # Replace <pod-name> and <namespace>
   kubectl logs <pod name> -n <namespace> --all-containers

   # Restart a deployment (for example, after updating the image)
   # Replace <deployment name> and <namespace>
   kubectl rollout restart deployment <deployment name> -n <namespace>

   # Open an interactive bash shell inside a running pod
   # Replace <pod name> and <namespace>
   kubectl exec --stdin --tty <pod name> -n <namespace> -- /bin/bash

   # From inside the container, tail Tomcat logs if present
   # (Run this after you are inside the pod’s shell)
   find . -name catalina.out -exec tail -f {} \;

   ```
2. Foward the port for the Pentaho Server by running the following command, replacing the `<pod name>`, `<port>`, and `<namespace>`:

   ```shellscript
   kubectl port-forward <pod name> <port>:<port> -n <namespace>
   ```

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>Note:</strong> The default port is 8080.</p></div>
3. Verify that Pentaho Server is running by accessing it at  `http://<your external ip>:<port>/pentaho` or your Application Load Balancer URL.

### Deploy on Google Cloud Platform

To deploy on Google Cloud Platform (GCP) using Google Artifact Registry (GAR), you must complete the following tasks, in order:

1. [Tag and push Pentaho Server Docker image to GAR](#tag-and-push-pentaho-server-docker-image-to-gar)
2. Create a database
   1. [Create a Google Cloud supported database in GCP](#create-a-google-cloud-supported-database-in-gcp)
   2. [Create an Oracle database instance for GCP](#create-an-oracle-database-instance-for-gcp)
3. [Configure storage in GCS bucket](#configure-storage-in-gcs-bucket)
4. [Verify Pentaho Server deployment to GCP](#verify-pentaho-server-deployment-to-gcp)

Before you begin, complete the following tasks:

* Create a Docker account.

  <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>Note:</strong> For help with Docker and Docker Hub, see the online documentation at <a href="https://docs.docker.com/">https://docs.docker.com/</a>. </p></div>
* Verify that you have access to a standard mode GKE cluster (Autopilot may have memory constraints).
* Install and authenticate to `gcloud` CLI.
* Verify that you have a GCS bucket for persistent storage (mounted via GCS FUSE CSI driver) or an alternative persistent storage class.
* Download both the ZIP file that contains the Docker image and the ZIP file that contains the configuration files for your environment. For instructions downloading Docker files, see the previous section, [Download Docker container files](#download-docker-container-files).

#### Tag and push Pentaho Server Docker image to GAR

To tag and push the Pentaho Server Docker image to GAR, complete the following steps:

1. In your working directory, open a command prompt from that subdirectory.
2. (Optional) If you are not logged in, log into Docker Hub using the following command: `docker login`.
3. Authenticate to GAR with a specific Artifact Registry host by running the following commands, replacing `<region>` with the value for your region:&#x20;

   ```shellscript
   gcloud auth login
   gcloud auth configure-docker <region>.pkg.dev
   ```
4. Tag and push the Pentaho Server Docker image by running the following command, replacing `<build number>`, `<region>`, `<project id>`, and `<repository>` with the values in the downloaded file and your GAR account:

   <pre class="language-shellscript" data-overflow="wrap"><code class="lang-shellscript">docker tag pentaho/pentaho-server:11.0.0.0-&#x3C;build number> \
     &#x3C;region>-docker.pkg.dev/&#x3C;project id>/&#x3C;repository>/pentaho-server:&#x3C;build number>
   docker push &#x3C;region>-docker.pkg.dev/&#x3C;project id>/&#x3C;repository>/pentaho-server:&#x3C;build number>
   </code></pre>

   The Pentaho Server Docker image is tagged and pushed to GAR.

#### Create a Google Cloud supported database in GCP

Create one of the following databases to be managed by Google Cloud: MySQL, PostgreSQL, or SQL Server.

{% hint style="info" %}
**Note:** To use an Oracle database, you must provision and configure a Compute Engine (GCE) VM. For instructions creating an Oracle database, see [Create an Oracle database instance for GCP](#create-an-oracle-database-instance-for-gcp).
{% endhint %}

To create a database for GCP that is managed by Google Cloud, complete the following steps:

1. On your local workstation, extract the `gcp-11.0.0.0-<build number>.zip` file to a temporary working directory.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>Note:</strong> For instructions on downloading the ZIP file, see the previous section, <a href="#download-docker-container-files">Download Docker container files</a>.</p></div>
2. In your working directory, go to the `gcp-11.0.0.0-<build number>/dist/gcp/pentaho-server` subdirectory.&#x20;
3. Open one of the following directories based on your database type:
   * `pentaho-server-mysql`
   * `pentaho-server-postgres`
   * `pentaho-server-sqlserver`
4. Go to the `db_init_<database type>` subdirectory and open a command prompt from that subdirectory.
5. (Optional) If you are not logged in, log into Google Cloud CLI using the following command: `gcloud auth login`.
6. Send the `.sql` files in the  `db_init_<database type>` subdirectory to your GCS bucket by running the following commands, replacing `<database>` and `<bucket>` :

   <pre class="language-shellscript" data-overflow="wrap"><code class="lang-shellscript">gsutil cp ./1-create_quartz_&#x3C;database>.sql gs://&#x3C;bucket>/
   gsutil cp ./2-create_repository_&#x3C;database>.sql gs://&#x3C;bucket>/
   gsutil cp ./3-create_jcr_&#x3C;database>.sql gs://&#x3C;bucket>/
   gsutil cp ./4-pentaho_mart_&#x3C;database>.sql gs://&#x3C;bucket>/
   gsutil cp ./5-pentaho_logging_&#x3C;database>.sql gs://&#x3C;bucket>/
   </code></pre>
7. Run the `.sql` files from the GCS bucket. The following commands are examples for running .`sql` files from the GCS bucket for a PostgreSQL database.

   <pre class="language-shellscript" data-overflow="wrap"><code class="lang-shellscript">gcloud sql import sql &#x3C;instance-id> gs://&#x3C;your-bucket>/1-create_quartz_postgres.sql \
     --database=&#x3C;database-name>
   gcloud sql import sql &#x3C;instance-id> gs://&#x3C;your-bucket>/2-create_repository_postgres.sql \
     --database=&#x3C;database-name>
   gcloud sql import sql &#x3C;instance-id> gs://&#x3C;your-bucket>/3-create_jcr_postgres.sql \
     --database=&#x3C;database-name>
   gcloud sql import sql &#x3C;instance-id> gs://&#x3C;your-bucket>/4-pentaho_mart_postgres.sql \
     --database=&#x3C;database-name>
   gcloud sql import sql &#x3C;instance-id> gs://&#x3C;your-bucket>/5-pentaho_logging_postgres.sql \
     --database=&#x3C;database-name>
   </code></pre>

   The database instance is created and initialized in GCP.

#### Create an Oracle database instance for GCP

To create an Oracle database for use on Google Cloud Platform (GCP), you must deploy an Oracle XE Docker container on a Compute Engine (GCE) VM and then run the required SQL files to create and initialize the Pentaho database schemas and tables.

{% hint style="info" %}
**Note:** If you want to use a MySQL, PostgreSQL, or SQL Server database, see [Create a Google Cloud supported database in GCP](#create-a-google-cloud-supported-database-in-gcp).
{% endhint %}

To create an Oracle database, complete the following steps:

1. Provision a GCE VM with type e2-medium.
2. On your local machine, open a command prompt.
3. Connect to the GCE VM by running the following command, replacing `<instance name>`, `<project>`, and `<zone>`:&#x20;

   ```shellscript
   gcloud compute ssh <instance name> --project=<project id> --zone=<zone>
   ```
4. Install and enable Docker on the VM by running the following commands:

   <pre class="language-shellscript" data-overflow="wrap"><code class="lang-shellscript">sudo apt update
   sudo apt install -y docker.io
   sudo systemctl enable docker
   sudo systemctl start docker
   sudo usermod -aG docker $USER
   </code></pre>
5. Download the Oracle XE image and start the Oracle XE container in the VM by running the following commands, replacing `<password>`:

   <pre class="language-shellscript" data-overflow="wrap"><code class="lang-shellscript">sudo docker pull gvenzl/oracle-xe
   docker run -d --name oracle-xe -p 1521:1521 -e ORACLE_PASSWORD=&#x3C;password>
   gvenzl/oracle-xe
   </code></pre>
6. Verify that SQL\*Plus can connect from inside the container to the Oracle XE database in the same container by running the following command, replacing `<username>`, `<password>`, and `<service name>`:

   ```shellscript
   docker exec -it <container name> sqlplus <username>/<password>@localhost/<service name>
   ```
7. Create a firewall rule in the Google Cloud project’s VPC network by running the following command:

   ```shellscript
   gcloud compute firewall-rules create allow-oracle-port \
   --allow tcp:1521 \
   --target-tags oracle-db \
   --description="Allow Oracle DB connections" \
   --direction=INGRESS \
   --priority=1000 \
   --network=default
   ```
8. Add a network tag to the VM so that firewall rules targeting that tag apply to it by running the following command, replacing `<zone>`:

   ```shellscript
   gcloud compute instances add-tags pentaho-oracle --tags=oracle-db --zone=<zone> 
   ```

   You can now connect to the Oracle XE database from SQL Developer by using the VM’s external IP address.
9. Upload the `.sql` files to the VM by running the following command, replacing `<vm name>`, `<vm user>`, and `<zone>`:&#x20;

   ```shellscript
   gcloud compute scp *.sql <vm name>:/home/<vm user>/sql --zone=<zone>
   ```
10. Open an SSH session to the VM by running the following command, replacing `<vm name>`, `<project id>`, and `<zone>`:

    ```shellscript
    gcloud compute ssh <vm name> --project=<project id> --zone=<zone>
    ```

    You are connected to the VM’s shell.
11. Copy the uploaded `.sql` files into the Docker container by running the following commands, replacing `<vm user>`:

    ```shellscript
    sudo docker cp /home/<vm user>/1_create_jcr_ora.sql oracle-xe:/tmp/  
    sudo docker cp /home/<vm user>/2_create_quartz_ora.sql oracle-xe:/tmp/  
    sudo docker cp /home/<vm user>/3_create_repository_ora.sql oracle-xe:/tmp  
    sudo docker cp /home/<vm user>/4_pentaho_logging_oracle.sql oracle-xe:/tm  
    sudo docker cp /home/<vm user>/5_pentaho_mart_oracle.sql oracle-xe:/tmp/   
    ```
12. Create and initialize required Pentaho database schemas and tables by running the following command, replacing `<password>`:

    ```shellscript
    sudo docker exec -it oracle-xe bash  
    sqlplus system/<password>@//localhost:1521/xepdb1  
    @/tmp/1_create_jcr_ora.sql  
    @/tmp/2a_create_quartz_ora.sql  
    @/tmp/2b_create_quartz_ora.sql  
    @/tmp/3_create_repository_ora.sql  
    @/tmp/4_pentaho_logging_oracle.sql  
    @/tmp/5_pentaho_mart_oracle.sql
    ```

    The Oracle database is deployed and the Pentaho database schemas and tables are initialized.

#### Configure storage in GCS bucket

To configure storage in your Google Cloud Storage (GCS) bucket, complete the following steps:

1. In your working directory, go to the `gcp-11.0.0.0-<build number>/dist/aws/pentaho-server` subdirectory.&#x20;

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>Note:</strong> You downloaded and extracted the  <code>aws-11.0.0.0-&#x3C;build number>.zip</code> file in the previous sections, <a href="#download-docker-container-files">Download Docker container files</a> and <a href="#create-a-database-instance-in-aws">Create a database instance in AWS</a>.</p></div>
2. Open one of the following directories based on your database type:
   * `pentaho-server-mysql`
   * `pentaho-server-oracle`
   * `pentaho-server-postgres`
   * `pentaho-server-sqlserver`
3. Open the `.yaml` file in a text editor and configure values for your environment. You must update the following values before deploying the Pentaho Server:

   ```yaml
    # Replace <name of bucket>
    csi:
       volumeAttributes:
         bucketName: <name of bucket>
   ```

   <pre class="language-yaml" data-overflow="wrap"><code class="lang-yaml"># Replace &#x3C;region>, &#x3C;project id>, &#x3C;repository>, and &#x3C;build number>
   containers:
           - name: pentaho-server
             image: &#x3C;region>-docker.pkg.dev/&#x3C;project id>/&#x3C;repository>/pentaho-server:11.0.0.0=&#x3C;build number>
   </code></pre>

   ```yaml
   # Replace <your license URL>
   env:
      - name: LICENSE_URL
        value: "<your license URL>"
   ```

   The contents of the `.yaml` file vary slightly for each database and include comments to assist you with editing the file. The following code is an example of the `.yaml` file contents used for a PostgreSQL database when deploying to GCP.

   <pre class="language-yaml" data-overflow="wrap" data-full-width="true" data-expandable="true"><code class="lang-yaml">---
   apiVersion: v1
   kind: Namespace
   metadata:
     name: pentaho-server
   ---
   apiVersion: v1
   kind: PersistentVolume
   metadata:
     name: gcs-pv
   spec:
     capacity:
       storage: 10Gi
     accessModes:
       - ReadWriteMany
     csi:
       driver: gcsfuse.csi.storage.gke.io
       volumeHandle: "pentaho-eng-dev" # this must be globally unique
       volumeAttributes:
         bucketName: "pentaho-eng-dev"
         mountOptions: "implicit-dirs,uid=5000,gid=5000,file-mode=0770,dir-mode=0770"
     persistentVolumeReclaimPolicy: Retain

   ---
   apiVersion: v1
   kind: PersistentVolumeClaim
   metadata:
     name: gcs-pvc
     namespace: pentaho-server
   spec:
     accessModes:
       - ReadWriteMany
     resources:
       requests:
         storage: 10Gi
     volumeName: gcs-pv
     storageClassName: ""  # Empty string because we are using a pre-provisioned PV
   ---
   # ServiceAccount for GCS access with correct IAM binding
   apiVersion: v1
   kind: ServiceAccount
   metadata:
     name: gcs-access-sa
     namespace: pentaho-server
     annotations:
       iam.gke.io/gcp-service-account: 890874994325-compute@developer.gserviceaccount.com
   ---
   apiVersion: v1
   kind: Secret
   metadata:
     name: pentaho-license
     namespace: pentaho-server
   ---
   apiVersion: apps/v1
   kind: Deployment
   metadata:
     name: pentaho-server
     namespace: pentaho-server
   spec:
     replicas: 1
     selector:
       matchLabels:
         app: pentaho-server
     template:
       metadata:
         annotations:
           gke-gcsfuse/volumes: "true"
         labels:
           app: pentaho-server
           dinode: active
       spec:
         serviceAccountName: gcs-access-sa
         volumes:
           - name: persistent-storage
             persistentVolumeClaim:
               claimName: gcs-pvc
           - name: pentaho-license
             secret:
               secretName: pentaho-license
               optional: true
         containers:
         - name: pentaho-server
           image: us-east1-docker.pkg.dev/pentaho-lee-cheng/pentaho-docker-repo/pentaho-server:11.0.0.0-52
           imagePullPolicy: "Always"
           resources:
             limits:
               memory: "4Gi"
               cpu: 500m
               ephemeral-storage: 5Gi
             requests:
               memory: "2Gi"
               cpu: 250m
               ephemeral-storage: 2Gi
           ports:
             - containerPort: 8080
           volumeMounts:
             - name: persistent-storage
               mountPath: /docker-entrypoint-init/
               subPath: ackbar-dev/postgres/softwareOverride
               readOnly: false
             - name: persistent-storage
               mountPath: /opt/pentaho/solution/
               subPath: ackbar-dev/postgres/solutionFiles
               readOnly: false
             - name: persistent-storage
               mountPath: /home/pentaho
               subPath: ackbar-dev/postgres/config
               readOnly: false
             - name: persistent-storage
               mountPath: /opt/pentaho/pentaho-server/tomcat/logs
               subPath: ackbar-dev/postgres/logs
               readOnly: false
           env:
               - name: LICENSE_URL
                 value: "https://flex1826-uat.compliance.flexnetoperations.com/instances/QP5BXJRC2XVM/request"
   ---
   apiVersion: v1
   kind: Service
   metadata:
     name: pentaho-server-service
     namespace: pentaho-server
     labels:
       app: pentaho-server-service
   spec:
     type: LoadBalancer
     selector:
       app: pentaho-server
       dinode: active
     ports:
       - name: http
         port: 8080
         targetPort: 8080
         protocol: TCP
   ---
   apiVersion: networking.k8s.io/v1
   kind: Ingress
   metadata:
     namespace: pentaho-server
     name: pentaho-server-ingress
     annotations:
       nginx.ingress.kubernetes.io/affinity: "cookie"
       nginx.ingress.kubernetes.io/affinity-mode: "persistent"
       nginx.ingress.kubernetes.io/session-cookie-name: "http-cookie"
       nginx.ingress.kubernetes.io/session-cookie-expires: "172800"
       nginx.ingress.kubernetes.io/session-cookie-max-age: "172800"
   spec:
     ingressClassName: nginx
     rules:
       - http:
           paths:
             - path: "/"
               pathType: Prefix
               backend:
                 service:
                   name: pentaho-server-service
                   port:
                     number: 8080

   </code></pre>
4. Save and close the `.yaml` file.
5. Go to the `softwareOverride/2_repository/tomcat/webapps/pentaho/META-INF` subdirectory.
6. Open the `context.xml` file in a text editor and update the database URL everywhere it appears. The following code is an example of the content in the `context.xml` file for a PostgreSQL database. In this example, the database instance URL is `jdbc:postgresql://repository:5432/hibernate`.

   <pre class="language-xml" data-overflow="wrap" data-expandable="true"><code class="lang-xml">&#x3C;?xml version="1.0" encoding="UTF-8"?>
   &#x3C;Context path="/pentaho" docbase="webapps/pentaho/">
     &#x3C;Resource name="jdbc/Hibernate" auth="Container" type="javax.sql.DataSource"
               factory="org.pentaho.di.core.database.util.DecryptingDataSourceFactory" maxActive="20" minIdle="0" maxIdle="5" initialSize="0"
               maxWait="10000" username="hibuser" password="password"
               driverClassName="org.postgresql.Driver" url="jdbc:postgresql://repository:5432/hibernate"
               validationQuery="select 1" jdbcInterceptors="ConnectionState" defaultAutoCommit="true"/>

     &#x3C;Resource name="jdbc/Audit" auth="Container" type="javax.sql.DataSource"
               factory="org.pentaho.di.core.database.util.DecryptingDataSourceFactory" maxActive="20" minIdle="0" maxIdle="5" initialSize="0"
               maxWait="10000" username="hibuser" password="password"
               driverClassName="org.postgresql.Driver" url="jdbc:postgresql://repository:5432/hibernate"
               validationQuery="select 1" />

     &#x3C;Resource name="jdbc/Quartz" auth="Container" type="javax.sql.DataSource"
               factory="org.pentaho.di.core.database.util.DecryptingDataSourceFactory" maxActive="20" minIdle="0" maxIdle="5" initialSize="0"
               maxWait="10000" username="pentaho_user" password="password" testOnBorrow="true"
               driverClassName="org.postgresql.Driver" url="jdbc:postgresql://repository:5432/quartz"
               validationQuery="select 1"/>

     &#x3C;Resource name="jdbc/PDI_Operations_Mart" auth="Container" type="javax.sql.DataSource"
               factory="org.pentaho.di.core.database.util.DecryptingDataSourceFactory" maxActive="20" minIdle="0" maxIdle="5" initialSize="0"
               maxWait="10000" username="hibuser" password="password"
               driverClassName="org.postgresql.Driver" url="jdbc:postgresql://repository:5432/hibernate"
               validationQuery="select 1"/>

     &#x3C;Resource name="jdbc/pentaho_operations_mart" auth="Container" type="javax.sql.DataSource"
               factory="org.pentaho.di.core.database.util.DecryptingDataSourceFactory" maxActive="20" minIdle="0" maxIdle="5" initialSize="0"
               maxWait="10000" username="hibuser" password="password"
               driverClassName="org.postgresql.Driver" url="jdbc:postgresql://repository:5432/hibernate"
               validationQuery="select 1"/>

    &#x3C;Resource name="jdbc/live_logging_info" auth="Container" type="javax.sql.DataSource"
               factory="org.pentaho.di.core.database.util.DecryptingDataSourceFactory" maxActive="20" minIdle="0" maxIdle="5" initialSize="0"
               maxWait="10000" username="hibuser" password="password"
               driverClassName="org.postgresql.Driver" url="jdbc:postgresql://repository:5432/hibernate?searchpath=pentaho_dilogs"
               validationQuery="select 1"/>

     &#x3C;Resource name="jdbc/SampleData" auth="Container" type="javax.sql.DataSource"
               factory="org.pentaho.di.core.database.util.DecryptingDataSourceFactory" maxActive="20" minIdle="0" maxIdle="5" initialSize="0"
               maxWait="10000" username="sa" password=""
               driverClassName="org.hsqldb.jdbcDriver" url="jdbc:hsqldb:hsql://localhost/sampledata"
               validationQuery="select 1"/>

     &#x3C;Resource name="jdbc/SampleDataAdmin" auth="Container" type="javax.sql.DataSource"
               factory="org.pentaho.di.core.database.util.DecryptingDataSourceFactory" maxActive="20" minIdle="0" maxIdle="5" initialSize="0"
               maxWait="10000" username="sa" password=""
               driverClassName="org.hsqldb.jdbcDriver" url="jdbc:hsqldb:hsql://localhost/sampledata"
               validationQuery="select 1"/>

     &#x3C;Resource name="jdbc/jackrabbit" auth="Container" type="javax.sql.DataSource"
               factory="org.pentaho.di.core.database.util.DecryptingDataSourceFactory" maxActive="20" minIdle="0"
               maxIdle="5" initialSize="0"
               maxWait="10000" username="jcr_user" password="password"
               driverClassName="org.postgresql.Driver"
               url="jdbc:postgresql://repository:5432/jackrabbit"
               validationQuery="select 1"/>
               &#x3C;!--
               url="jdbc:mysql://localhost:3306/jackrabbit"/>
               url="jdbc:oracle:thin:@localhost:1521/XE"/>
               url="jdbc:sqlserver://localhost:1433;DatabaseName=jackrabbit"/>
               -->
   &#x3C;/Context>

   </code></pre>
7. (Optional) To install Pentaho Data Integration plugins during deployment, place the directory for each plugin in the `softwareOverride\2_repository\pentaho-solutions\system` subdirectory for your database type. The following subdirectories are needed for installing the plugins:

   * `pentaho-interactive-reporting`
   * `dashboards`
   * `analyzer`

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>Note:</strong> For instructions downloading plugin files, see <a href="#download-plugin-files">Download plugin files</a>.</p></div>
8. (Optional) To change the default administrator password before deploying the Pentaho Server and database, go to the in the `softwareOverride\2_repository\pentaho-solutions\system` subdirectory and update the `defaultUser.spring.properties` and `repository.spring.properties` files. For instructions, see [Change the default administrator password](#change-the-default-administrator-password).
9. Add a firewall rule in the Google Cloud Console allowing the GKE nodes to communicate with the Pentaho Server pod, enabling the pod to reach the external database.
10. In your GKE cluster, create an GCS bucket for each of the following subdirectories that appear in the `gcp-11.0.0.0-<build number>/dist/gcp/pentaho-server/<database>` directory:
    1. `config`
    2. `logs`
    3. `softwareOverride`
11. Upload the contents of each subdirectory to the corresponding GCS bucket that you created for them.
12. Go back to the `gcp-11.0.0.0-<build number>/dist/aws/pentaho-server/<database>` directory, which contains your database `.yaml` file, and open a command prompt from that directory.&#x20;
13. In the command prompt, create the persistent volumes and persistent volume claims, then deploy the Pentaho Server to the Kubernetes cluster by running the following command. Replace `<database>` with the database name defined in the `.yaml` file:

    ```go
    kubectl apply -f pentaho-server-gcp-<database>.yaml
    ```

    The Pentaho Server is deployed with the storage you configured in the GCS bucket.

#### Verify Pentaho Server deployment to GCP

To verify Pentaho Server deployment to GCP, complete the following steps:

1. In a command prompt, run the following commands, in order:

   ```shellscript
   # List all pods in the pentaho-server namespace
   kubectl get pods -o wide -n pentaho-server

   # Stream real-time logs for the Pentaho Server pod
   # Replace <container id>
   kubectl logs <container id> -n pentaho-server --follow

   # List Kubernetes services
   # Get EXTERNAL-IP address to access Pentaho Server
   kubectl get svc -n pentaho-server
   ```
2. Foward the port for the Pentaho Server by running the following command, replacing the `<pod name>`, `<port>`, and `<namespace>`:

   ```shellscript
   kubectl port-forward <pod name> <port>:<port> -n <namespace>
   ```

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>Note:</strong> The default port is 8080.</p></div>
3. Verify that Pentaho Server is running by accessing it at  `http://<your external ip>:<port>/pentaho` or your Application Load Balancer URL.

### Deploy on Microsoft Azure

To deploy on Microsoft Azure using Azure Kubernetes Service (AKS), you must complete the following tasks, in order:

1. [Tag and push Pentaho Server Docker image to Microsoft ACR](#tag-and-push-pentaho-server-docker-image-to-microsoft-acr)
2. [Edit database and storage configuration files for Azure](#edit-database-and-storage-configuration-files-for-azure)
3. [Upload database and storage configuration files to Azure](#upload-database-and-storage-configuration-files-to-azure)
4. [Create a database instance in Azure](#create-a-database-instance-in-azure)
5. [Deploy the Pentaho Server container in Azure](#deploy-the-pentaho-server-container-in-azure)

**Best practices**

* Use Azure Managed Disks or Azure Files to provide persistent storage and mount these volumes into the container.
* Deploy Pentaho Server behind an Azure Application Gateway to enable centralized TLS/SSL termination and traffic routing.
* For production environments, use a managed database service such as Azure Database for PostgreSQL, MySQL, or SQL Server.

**Before you begin**

Before you can deploy to Microsoft Azure, complete the following tasks:

* Create a Docker account.

  <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>Note:</strong> For help with Docker and Docker Hub, see the online documentation at <a href="https://docs.docker.com/">https://docs.docker.com/</a>. </p></div>
* Verify you have access to a standard Azure Kubernetes Service (AKS) cluster.
* Verify that your Azure account has the required permissions to create resource groups, databases, container registries, storage accounts, namespaces, and Kubernetes services.&#x20;
* If you plan to pull Pentaho images from Azure Container Registry (ACR), or a mirrored ACR, verify that your Azure account is assigned the AcrPull role so it can pull images from ACR.
* Install `kubectl` and Azure CLI.
* Set up your local `kubeconfig` so that `kubectl` can communicate with the cluster by running the following command:

  <pre class="language-shellscript" data-overflow="wrap"><code class="lang-shellscript">az aks get-credentials --resource-group --name --overwrite-existing
  </code></pre>
* Download both the ZIP file that contains the Docker image and the ZIP file that contains the configuration files for your environment. For instructions downloading Docker files, see the previous section, [Download Docker container files](#download-docker-container-files).

#### Tag and push Pentaho Server Docker image to Microsoft ACR

To tag the Pentaho Server Docker image and upload it to ACR, complete the following steps:

1. In your working directory, open a command prompt.
2. (Optional) If you are not logged in, log into Docker Hub using the following command: `docker login`.
3. Authenticate to ACR by running the following commands, replacing `<registryName>` with the name of your registry:&#x20;

   ```shellscript
   az login
   az acr login --name <registryName>
   ```
4. Tag and push the Pentaho Server Docker image by running the following commands, replacing `<image name>`, `<registry name>`, and `<image name on acr>` with the values from the downloaded file and your Azure account:

   <pre class="language-shellscript" data-overflow="wrap"><code class="lang-shellscript">docker tag &#x3C;image name> &#x3C;registry name>.azurecr.io/&#x3C;image name on acr>
   docker push &#x3C;registry name>.azurecr.io/&#x3C;image name on acr>
   </code></pre>
5. Verify the Pentaho Server Docker image is uploaded to ACR by using the following command, replacing `<registry name>` and `<repository name>`:

   ```shellscript
   az acr repository show-tags --name <registry name> --repository <repository name>
   ```

   The Pentaho Server Docker image is tagged and pushed to ACR.

#### **Edit database and storage configuration files for Azure**

To edit database and storage configuration files for Azure, complete the following steps:

1. On your local workstation, extract the `azure-11.0.0.0-<build number>.zip` file to a temporary working directory.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>Note:</strong> For instructions on downloading the ZIP file, see the previous section, <a href="#download-docker-container-files">Download Docker container files</a>.</p></div>
2. In your working directory, go to the `azure-11.0.0.0-<build number>/dist/azure/pentaho-server` subdirectory.&#x20;
3. Open one of the following directories based on your database type:
   * `pentaho-server-mysql`
   * `pentaho-server-oracle`
   * `pentaho-server-postgres`
   * `pentaho-server-sqlserver`
4. Open the `.yaml` file in a text editor and configure values for your environment. You must update the following values before deploying the Pentaho Server:

   ```yaml
   # Replace <name of bucket>
    csi:
       volumeAttributes:
         bucketName: <name of bucket>
   ```

   <pre class="language-yaml" data-overflow="wrap"><code class="lang-yaml"># Replace &#x3C;aws account id>, &#x3C;region>, and &#x3C;build number>
   containers:
           - name: pentaho-server
             image: &#x3C;registry-name>.azurecr.io/pentaho-server:11.0.0.0-&#x3C;build number>
   </code></pre>

   ```yaml
   # Replace <your license URL>
   env:
      - name: LICENSE_URL
        value: "<your license URL>"
   ```

   The contents of the `.yaml` file vary slightly for each database and include comments to assist you with editing the file. The following code is an example of the `.yaml` file contents used for a PostgreSQL database when deploying to Azure.

   <pre class="language-yaml" data-overflow="wrap" data-full-width="true" data-expandable="true"><code class="lang-yaml"># Namespace for grouping resources
   apiVersion: v1
   kind: Namespace
   metadata:
     name: pentaho-server  # Replace (optional) with your desired namespace name
   ---
   apiVersion: v1
   kind: PersistentVolume
   metadata:
     annotations:
       pv.kubernetes.io/provisioned-by: file.csi.azure.com
     name: pdia-pv # Must match the name in PersistentVolumeClaim
   spec:
     capacity:
       storage: 10Gi
     accessModes:
       - ReadWriteMany
     persistentVolumeReclaimPolicy: Retain
     storageClassName: azurefile-csi
     csi:
       driver: file.csi.azure.com
       volumeHandle: "{pdia-docker-ackbar}#{pdiadockerstorage}#{pdia-docker-file-share-postgres}"  # replace with your unique volume ID e.g. {resource-group-name}#{storage-account-name}#{file-share-name}
       volumeAttributes:
         shareName: pdia-docker-file-share-postgres # replace with your file share name
       nodeStageSecretRef:
         name: pdia-fileshareaccount-secret # Match the name used in Secret for Azure Storage Account
         namespace: pentaho-server # Must match the namespace
     mountOptions:
       - dir_mode=0777
       - file_mode=0777
       - uid=0
       - gid=0
       - mfsymlinks
       - cache=strict
       - nosharesock
       - nobrl  # disable sending byte range lock requests to the server and for applications which have challenges with posix locks
   ---
   # Secret for Azure Storage Account credentials
   apiVersion: v1
   kind: Secret
   metadata:
     name: pdia-fileshareaccount-secret  # Match the name used in PV
     namespace: pentaho-server  # Must match the namespace
   type: Opaque
   stringData:
     azurestorageaccountname: pdiadockerstorage  # Replace with your Azure Storage Account name
     azurestorageaccountkey: SJp+vN/MhoP5xfCXtg9y7ujTIfUBrO/jXBt7TzTZryZ8BDFZbKpY3XskvbVEbuqdwaAhWv8XmLI4+AStSFB0AA==  # Replace with your Storage Account key

   ---
   apiVersion: v1
   kind: PersistentVolumeClaim
   metadata:
     name: pdia-pv # Must match the name in PersistentVolumeClaim
     namespace: pentaho-server # Must match the namespace
   spec:
     accessModes:
       - ReadWriteMany
     storageClassName: azurefile-csi
     volumeName: pdia-pv # Must match the name in PersistentVolume
     resources:
       requests:
         storage: 10Gi
   ---
   apiVersion: apps/v1
   kind: Deployment
   metadata:
     name: pentaho-server
     namespace: pentaho-server # Must match the namespace
   spec:
     replicas: 1
     selector:
       matchLabels:
         app: pentaho-server
     template:
       metadata:
         labels:
           app: pentaho-server
           dinode: active
       spec:
         containers:
           - name: pentaho-server
             image: pentahopdia.azurecr.io/pentaho-server:11.0.0.0-xxx # Replace with your image
             imagePullPolicy: "Always"
             resources:
               limits:
                 memory: "4500Mi"
               requests:
                 memory: "2000Mi"
             ports:
               - containerPort: 8080
             volumeMounts:
               - name: azure-file-share
                 mountPath: /docker-entrypoint-init/
                 subPath: softwareOverride
                 readOnly: false
               - name: azure-file-share
                 mountPath: /opt/pentaho/pentaho-server/tomcat/logs
                 subPath: logs
                 readOnly: false
               - name: azure-file-share
                 mountPath: /home/pentaho
                 subPath: config
                 readOnly: false
             env:
               - name: LICENSE_URL
                 value: "https://flex1826-uat.compliance.flexnetoperations.com/instances/QP5BXJRC2XVM/request"# Replace with your license URL
         volumes:
           - name: azure-file-share
             persistentVolumeClaim:
               claimName: pdia-pv # Must match the name in PersistentVolumeClaim
   ---
   # LoadBalancer service to expose the application
   apiVersion: v1
   kind: Service
   metadata:
     name: pentaho-loadbalancer-service  # Replace (optional) with your service name
     namespace: pentaho-server  # Must match the namespace
     labels:
       app: pentaho-server
   spec:
     type: LoadBalancer
     selector:
       app: pentaho-server  # Must match the label in the deployment
     ports:
       - port: 8080
         targetPort: 8080

   ---
   apiVersion: networking.k8s.io/v1
   kind: Ingress
   metadata:
     namespace: pentaho-server # Must match the namespace
     name: pentaho-server-ingress
     annotations:
       nginx.ingress.kubernetes.io/affinity: "cookie"
       nginx.ingress.kubernetes.io/affinity-mode: "persistent"
       nginx.ingress.kubernetes.io/session-cookie-name: "http-cookie"
       nginx.ingress.kubernetes.io/session-cookie-expires: "172800"
       nginx.ingress.kubernetes.io/session-cookie-max-age: "172800"
   spec:
     ingressClassName: nginx
     rules:
       - http:
           paths:
             - path: "/"
               pathType: Prefix
               backend:
                 service:
                   name: pentaho-server-service
                   port:
                     number: 8080

   </code></pre>
5. Save and close the `.yaml` file.
6. Go to the `/softwareOverride/2_repository/tomcat/webapps/pentaho/META-INF/` directory.
7. Open the `context.xml` file in a text editor and update the database URL everywhere it appears. The following code is an example of the content in the `context.xml` file for a PostgreSQL database. In this example, the database instance URL is `jdbc:postgresql://repository:5432/hibernate`.

   <pre class="language-xml" data-overflow="wrap" data-expandable="true"><code class="lang-xml">&#x3C;?xml version="1.0" encoding="UTF-8"?>
   &#x3C;Context path="/pentaho" docbase="webapps/pentaho/">
     &#x3C;Resource name="jdbc/Hibernate" auth="Container" type="javax.sql.DataSource"
               factory="org.pentaho.di.core.database.util.DecryptingDataSourceFactory" maxActive="20" minIdle="0" maxIdle="5" initialSize="0"
               maxWait="10000" username="hibuser" password="password"
               driverClassName="org.postgresql.Driver" url="jdbc:postgresql://repository:5432/hibernate"
               validationQuery="select 1" jdbcInterceptors="ConnectionState" defaultAutoCommit="true"/>

     &#x3C;Resource name="jdbc/Audit" auth="Container" type="javax.sql.DataSource"
               factory="org.pentaho.di.core.database.util.DecryptingDataSourceFactory" maxActive="20" minIdle="0" maxIdle="5" initialSize="0"
               maxWait="10000" username="hibuser" password="password"
               driverClassName="org.postgresql.Driver" url="jdbc:postgresql://repository:5432/hibernate"
               validationQuery="select 1" />

     &#x3C;Resource name="jdbc/Quartz" auth="Container" type="javax.sql.DataSource"
               factory="org.pentaho.di.core.database.util.DecryptingDataSourceFactory" maxActive="20" minIdle="0" maxIdle="5" initialSize="0"
               maxWait="10000" username="pentaho_user" password="password" testOnBorrow="true"
               driverClassName="org.postgresql.Driver" url="jdbc:postgresql://repository:5432/quartz"
               validationQuery="select 1"/>

     &#x3C;Resource name="jdbc/PDI_Operations_Mart" auth="Container" type="javax.sql.DataSource"
               factory="org.pentaho.di.core.database.util.DecryptingDataSourceFactory" maxActive="20" minIdle="0" maxIdle="5" initialSize="0"
               maxWait="10000" username="hibuser" password="password"
               driverClassName="org.postgresql.Driver" url="jdbc:postgresql://repository:5432/hibernate"
               validationQuery="select 1"/>

     &#x3C;Resource name="jdbc/pentaho_operations_mart" auth="Container" type="javax.sql.DataSource"
               factory="org.pentaho.di.core.database.util.DecryptingDataSourceFactory" maxActive="20" minIdle="0" maxIdle="5" initialSize="0"
               maxWait="10000" username="hibuser" password="password"
               driverClassName="org.postgresql.Driver" url="jdbc:postgresql://repository:5432/hibernate"
               validationQuery="select 1"/>

    &#x3C;Resource name="jdbc/live_logging_info" auth="Container" type="javax.sql.DataSource"
               factory="org.pentaho.di.core.database.util.DecryptingDataSourceFactory" maxActive="20" minIdle="0" maxIdle="5" initialSize="0"
               maxWait="10000" username="hibuser" password="password"
               driverClassName="org.postgresql.Driver" url="jdbc:postgresql://repository:5432/hibernate?searchpath=pentaho_dilogs"
               validationQuery="select 1"/>

     &#x3C;Resource name="jdbc/SampleData" auth="Container" type="javax.sql.DataSource"
               factory="org.pentaho.di.core.database.util.DecryptingDataSourceFactory" maxActive="20" minIdle="0" maxIdle="5" initialSize="0"
               maxWait="10000" username="sa" password=""
               driverClassName="org.hsqldb.jdbcDriver" url="jdbc:hsqldb:hsql://localhost/sampledata"
               validationQuery="select 1"/>

     &#x3C;Resource name="jdbc/SampleDataAdmin" auth="Container" type="javax.sql.DataSource"
               factory="org.pentaho.di.core.database.util.DecryptingDataSourceFactory" maxActive="20" minIdle="0" maxIdle="5" initialSize="0"
               maxWait="10000" username="sa" password=""
               driverClassName="org.hsqldb.jdbcDriver" url="jdbc:hsqldb:hsql://localhost/sampledata"
               validationQuery="select 1"/>

     &#x3C;Resource name="jdbc/jackrabbit" auth="Container" type="javax.sql.DataSource"
               factory="org.pentaho.di.core.database.util.DecryptingDataSourceFactory" maxActive="20" minIdle="0"
               maxIdle="5" initialSize="0"
               maxWait="10000" username="jcr_user" password="password"
               driverClassName="org.postgresql.Driver"
               url="jdbc:postgresql://repository:5432/jackrabbit"
               validationQuery="select 1"/>
               &#x3C;!--
               url="jdbc:mysql://localhost:3306/jackrabbit"/>
               url="jdbc:oracle:thin:@localhost:1521/XE"/>
               url="jdbc:sqlserver://localhost:1433;DatabaseName=jackrabbit"/>
               -->
   &#x3C;/Context>

   </code></pre>
8. Save and close the `context.xml` file.
9. (Optional) To install Pentaho Data Integration plugins during deployment, place the directory for each plugin in the `softwareOverride\2_repository\pentaho-solutions\system` subdirectory for your database type. The following subdirectories are needed for installing the plugins:

   * `pentaho-interactive-reporting`
   * `dashboards`
   * `analyzer`

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>Note:</strong> For instructions downloading plugin files, see <a href="#download-plugin-files">Download plugin files</a>.</p></div>
10. (Optional) To change the default administrator password before deploying the Pentaho Server and database, go to the in the `softwareOverride\2_repository\pentaho-solutions\system` subdirectory and update the `defaultUser.spring.properties` and `repository.spring.properties` files. For instructions, see [Change the default administrator password](#change-the-default-administrator-password).

#### Upload database and storage configuration files to Azure

In Azure Storage Explorer upload the following directories from your database directory to the file share in your Azure storage account:

* `config`
* `db_init_<database>`
* `logs`
* `softwareOverride`

{% hint style="info" %}
**Note:** For information about working with Azure Storage Explorer, see the online documenation at <https://learn.microsoft.com/azure>.
{% endhint %}

#### Create a database instance in Azure

1. In the Microsoft Azure portal, create a database instance for your database type.
2. Run the `.sql` scripts in the `db_init_<database>` directory that you uploaded in the previous section.

{% hint style="info" %}
**Note:** For information about creating databases in Microsoft Azure, see the online documentation at <https://learn.microsoft.com/azure>.
{% endhint %}

#### Deploy the Pentaho Server as a container in Azure

To deploy the Pentaho Server as a container in Azure, complete the following steps:

1. Create the Pentaho Server container and database volume by running the following command, replacing `<database>`:&#x20;

   ```shellscript
   kubectl apply -f pentaho-server-azure-<database>.yaml
   ```
2. Verify that Pentaho Server is running by accessing it at `http://<vm ip>:<port>/pentaho` or your Azure Application Gateway URL.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>Note:</strong> The default port is 8080.</p></div>

Before the database container and volume are created, you can change the default administrator password by updating properties files that are referenced during deployment.&#x20;

{% hint style="info" %}
**Notes:**&#x20;

* After deployment, you can change the administrator  password in the Pentaho User Console. For instructions, see [Change your password](https://app.gitbook.com/s/dbSFXbJFiObHB299lSSa/pentaho-user-console/log-in-to-the-pentaho-user-console/change-your-password).
* If you have an existing Pentaho Server or Pentaho Data Integration installation, you can use the `encr.bat` command to generate an encrypted password. For details, see [Encrypting a password](https://docs.pentaho.com/install/legacy-redirects/tasks-to-be-performed-by-an-it-administrator-legacy-redirects/use-password-encryption-with-pentaho-legacy-pages/encrypting-a-password).
  {% endhint %}

To change the default administrator password, complete the following steps:

1. In your working directory, go to the `pentaho-server` subdirectory.
2. Open one of the following directories based on your database type:
   * `pentaho-server-mysql`
   * `pentaho-server-oracle`
   * `pentaho-server-postgres`
   * `pentaho-server-sqlserver`
3. Go to the `system` directory: `softwareOverride/4_others/pentaho-solutions/system`.
4. Open the `defaultUser.spring.properties` file in a text editor and edit the `defaultAdminUserPassword` property value.
5. Save and close the `defaultUser.spring.properties` file.
6. Open the `repository.spring.properties` file in a text editor and edit the `systemTenantAdminPassword` property value.
7. Save and close the `repository.spring.properties` file.

   The `defaultUser.spring.properties` and  `repository.spring.properties` files are now ready to upload during cloud deployment.

## Install Pentaho Server plugins after deployment

After deploying the Pentaho Server as a container, the recommended way to install Pentaho Server plugins is to use the Plugin Manager. For instructions using the Plugin Manager to install plugins, see [Step 4: Install Pentaho plugins](https://docs.pentaho.com/install/legacy-redirects/design-tools-installation-redirects/install-pdi-plugins).

However, if you cannot use the Plugin Manager, you can install plugins by placing the plugin files in the appropriate directory for your deployment and restarting the Pentaho Server.&#x20;

Before you begin, you must download the Pentaho Server plugin files. For instructions downloading plugin files, see [Download plugin files](#download-plugin-files).

{% hint style="info" %}
**Note**: Plugins installed outside of the Plugin Manager might not be listed in the Plugin Manager and must be maintained manually.
{% endhint %}

To install Pentaho Server plugins after the Pentaho Server has been deployed as a container, complete the following steps:&#x20;

1. In your cloud deployment, go to the `pentaho-server` directory.
2. Open one of the following subdirectories based on your database type:
   * `pentaho-server-mysql`
   * `pentaho-server-oracle`
   * `pentaho-server-postgres`
   * `pentaho-server-sqlserver`
3. Go to `softwareOverride/4_others/pentaho-solutions/system` subdirectory.
4. Copy one or more of following plugin directories and its contents to the `softwareOverride/2_repository/pentaho-solutions/system` directory in your cloud deployment:
   * `pentaho-interactive-reporting`
   * `dashboards`
   * `analyzer`
5. Restart the Pentaho Server by using the commands for your environment:
   * On-premises

     ```shellscript
     # Stop everything in the container
     docker compose stop
     # Start everything in the container
     docker compose start
     ```
   * Amazon Web Services

     ```shellscript
     # Delete the resources created by the Pentaho Server .yaml file
     kubectl delete -f pentaho-server-aws-<database>.yaml
     # Recreate all Kubernetes objects in the .yaml file
     kubectl apply -f pentaho-server-aws-<database>.yaml
     ```
   * Google Cloud Platform and Microsoft Azure

     <pre class="language-shellscript" data-overflow="wrap"><code class="lang-shellscript"># List pods in namespace
     kubectl get pods -n pentaho-server

     # Delete Pentaho Server pod
     kubectl delete pod -n pentaho-server &#x3C;pod name>

     # List pods in namespace to get new Pentaho Server pod name
     kubectl get pods -n pentaho-server

     # Stream logs from the new Pentaho Server pod to watch Pentaho Server start up
     kubectl logs -n pentaho-server -f &#x3C;pod name>
     </code></pre>

## Software overrides and plugins

The ZIP file that you [download to deploy Pentaho Server](#download-docker-container-files) as a container includes a `softwareOverride` directory that you can use to inject or replace files at container startup.&#x20;

The Pentaho Server `softwareOverride` directory, located at `/path/dist/pentaho-server/<database>/softwareOverride`, contains subdirectories whose contents are copied by the Docker entrypoint into the Pentaho installation directory, in numerical order.

For instance, the `on-prem-11.0.0.0-<build number>/dist/on-prem/pentaho-server/pentaho-server-postgres/softwareOverride` directory contains the following subdirectories:

* `1_drivers`
* `2_repository`
* `3_security`
* `4_others`
* `99_exchange`

Any file placed in one of the subdirectories of the `softwareOverride` directory is layered into the container during startup. For example, if you place Pentaho Server plugin files in the `/path/dist/pentaho-server/<database>/softwareOverride/2_repository/pentaho-solutions/system` subdirectory, those plugins are installed when the Pentaho Server is restarted. You can also use the softwareOverrides directory to [change the default administrator password](#change-the-default-administrator-password) before deployment.

For instructions about software overrides in your specific environment, see the `README.md` file that is included in the `softwareOverride` directory.
