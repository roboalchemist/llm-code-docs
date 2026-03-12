# Source: https://docs.pentaho.com/install/pentaho-installation-overview-cp/docker-container-deployment-of-carte-pan-and-kitchen.md

# Docker container deployment of Carte, Pan, and Kitchen

You can use Docker Compose to run Pentaho Data Integration (PDI) command-line tools (Carte, Kitchen, and Pan) within containers in the following supported environments:

* On‑premises
* Amazon Web Services (AWS)
* Google Cloud Platform (GCP)
* Microsoft Azure

## Download PDI Docker files

To run PDI command-line tools (Carte, Kitchen, and Pan) in containers, you must first download both the `.gz` file that contains the PDI Docker image and the ZIP file that contains the configuration files for your environment.

Complete the following steps to download the files that you need for running PDI command-line tools in containers:

1. On the [Support Portal](https://support.pentaho.com/hc/en-us) home page, sign in using the Pentaho Support username and password provided in your Pentaho Welcome Packet.
2. In the Pentaho card, click **Download**. The Downloads page opens.
3. In the **11.x** list, click **Pentaho 11.0 GA Release**.
4. Scroll to the bottom of the Pentaho 11.0 GA Release page.
5. In the file component section, navigate to the `Docker Image Configurator/Images` directory.
6. Download the `pdi-11.0.0.0-<build number>.tar.gz` file.&#x20;
7. In the file component section, navigate to the `Docker Image Configurator/Environment Config` directory.
8. Download one of the following ZIP files that contain the configuration files for your environment:
   * `aws-11.0.0.0-<build number>.zip`
   * `azure-11.0.0.0-<build number>.zip`
   * `gcp-11.0.0.0-<build number>.zip`
   * `on-prem-11.0.0.0-<build number>.zip`

## Running PDI tools in containers on premises

Run Pentaho Data Integration (PDI) command-line tools (Carte, Kitchen, and Pan) in containers on an on‑premises host using Docker and Docker Compose.

#### Prepare to run Carte, Kitchen, and Pan in containers

Before running PDI tools in containers on an on‑premises host, you must complete the following tasks:

* Create a Docker account.

  <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>Note:</strong> For help with Docker and Docker Hub, see the online documentation at <a href="https://docs.docker.com/">https://docs.docker.com/</a>. </p></div>
* On the host, install Docker Engine and Docker Compose.
* Download both the ZIP file that contains the Docker image and the ZIP file that contains the configuration files for your environment. For instructions downloading Docker files, see the previous section, [Download PDI Docker files](#download-pdi-docker-files).

{% hint style="info" %}
**Note:** For help with Docker and Docker Hub, see the online documentation at <https://docs.docker.com/>.&#x20;
{% endhint %}

**Procedure**

1. On your host, extract the `on-prem-11.0.0.0-<build number>.zip` to a working directory.
2. In the working directory, navigate to the `on-prem-11.0.0.0-237/dist/on-prem/pdi` subdirectory.
3. In a text editor, open the `.env` file and configure variables for your environment, including the `PENTAHO_IMAGE_NAME`, which must match the name of image loaded on Docker (example: `pdi-11.0.0.0-<build number>.tar.gz`). You can get the correct image name by using the `docker image -ls` command.

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
4. Save and close the `.env` file.
5. Add PDI files to one or more of the following subdirectories:

   1. `config`: Contains Pentaho files, like `.kettle` and `.pentaho` files, as well as configuration files, such as `.ssh` files.
   2. `softwareOverride`: Contains configuration files that override the default settings in the PDI installation.
   3. `solutionFiles`: Contains project solution files, including transformations (`.ktr`), jobs (`.kjb`), and any related `.kettle` files.

   The host is prepared for running Carte, Kitchen, and Pan in containers.

#### Run Carte, Kitchen, and Pan in containers

Before you begin, verify that you have uploaded your transformation (`.ktr`) files, job (`.kjb`) files,  and any related `.kettle` files to the `on-prem-11.0.0.0-237/dist/on-prem/pdi/solutionFiles` subdirectory.

1. In the `on-prem-11.0.0.0-237/dist/on-prem/pdi` subdirectory, open a command prompt.
2. Run one or more of the following PDI tools in containers:
   * To run the Carte Server in a container, complete the following substeps:
     1. Run the Carte Server using the following command:

        ```shellscript
        docker compose -f carte.yaml up
        ```

        1. To verify that Carte is running, log into the Carte homepage at `http://<host>:<port>/kettle/status` or the external IP address assigned to the deployment.&#x20;
        2. (Optional) To execute a transformation (`.ktr`) or job (`.kjb`) that you added to the `solutionFiles` directory, go to one of the following URLs in your browser:
           1. <pre class="language-html" data-overflow="wrap"><code class="lang-html">http://&#x3C;host>:&#x3C;port>/kettle/executeTrans/?trans=&#x3C;path to transformation>/&#x3C;transformation name>&#x26;level=Basic
              </code></pre>
           2. <pre class="language-html" data-overflow="wrap"><code class="lang-html">http://&#x3C;host>:&#x3C;port>/kettle/executeJob/?job=&#x3C;path to job>/&#x3C;job name>.kjb&#x26;level=Basi
              </code></pre>
   * To run Kitchen in a container, use the following command:

     ```shellscript
     docker compose -f kitchen.yaml up
     ```
   * To run Pan in a container, use the following command:

     ```shellscript
     docker compose -f pan.yaml up
     ```

## Running PDI tools in cloud containers

Run Pentaho Data Integration (PDI) command-line tools (Carte, Kitchen, and Pan) in cloud-based containers. Use a supported cloud platform to deploy, manage, and run the tools with Kubernetes.

### Prepare to run Carte, Kitchen, and Pan in containers

To prepare for running PDI command-line tools (Carte, Kitchen, and Pan) in containers, complete the following tasks:

1. [Tag and push PDI image to the cloud](#tag-and-push-pdi-image-to-the-cloud)
2. [Configure storage in the cloud](#configure-storage-in-the-cloud)
3. [Edit YAML files for deploying to the cloud](#edit-yaml-files-for-deploying-to-the-cloud)
4. [Upload PDI files to the cloud](#upload-pdi-files-to-the-cloud)

#### Before you begin

Before you begin, complete the following tasks:

* Create a Docker account.

  <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>Note:</strong> For help with Docker and Docker Hub, see the online documentation at <a href="https://docs.docker.com/">https://docs.docker.com/</a>. </p></div>
* Install `kubectl`.
* Download both the ZIP file that contains the Docker image and the ZIP file that contains the configuration files for your environment. For instructions downloading Docker files, see the previous section, [Download PDI Docker files](#download-pdi-docker-files).
* Amazon Web Services tasks
  * Verify you have access to a standard Amazon EKS cluster.
  * Verify that you have an approved S3 CSI approach. (Used for configs, logs, and overrides and required if your package YAMLs reference S3 buckets for configuration or storage paths.)
  * If you plan to pull Pentaho images from Amazon Elastic Container Registry (ECR), or a mirrored ECR, confirm that the node instance role or IRSA-enabled service account has permission to pull images.
  * Set up your local `kubeconfig` so that `kubectl` can communicate with the cluster by running the following command, replacing `<name>` and `<region>`:

    ```shellscript
    aws eks update-kubeconfig --<name> --<region>
    ```
  * Install AWS CLI.
* Google Cloud Platform tasks
  * Verify that you have access to a standard mode GKE cluster (Autopilot may have memory constraints).
  * Install and authenticate to `gcloud` CLI.
  * Verify that you have a GCS bucket for persistent storage (mounted via GCS FUSE CSI driver) or an alternative persistent storage class.
* Microsoft Azure tasks
  * Verify you have access to a standard Azure Kubernetes Service (AKS) cluster.
  * Verify that your Azure account has the required permissions to create resource groups, databases, container registries, storage accounts, namespaces, and Kubernetes services.&#x20;
  * If you plan to pull Pentaho images from Azure Container Registry (ACR), or a mirrored ACR, verify that your Azure account is assigned the AcrPull role so it can pull images from ACR.
  * Install Azure CLI.
  * Set up your local `kubeconfig` so that `kubectl` can communicate with the cluster by running the following command:

    <pre class="language-shellscript" data-overflow="wrap"><code class="lang-shellscript">az aks get-credentials --resource-group --name --overwrite-existing
    </code></pre>

#### Tag and push PDI image to the cloud

To tag the PDI image and upload it to the cloud, complete the following steps:

1. Go to your working directory that contains the `pdi-11.0.0.0-<build number>.tar` file and open a command prompt.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>Note:</strong> For instructions on downloading the  <code>pdi-11.0.0.0-&#x3C;build number>.tar.gz</code> file, see the previous section, <a href="#download-pdi-docker-image">Download PDI Docker image</a>.</p></div>
2. (Optional) If you are not logged in, log into Docker Hub using the following command: `docker login`.
3. Authenticate to your cloud provider.&#x20;
   * For AWS, authenticate to ECR by running the following commands, replacing `<aws region>` and `<aws account id>`: &#x20;

     <pre class="language-shellscript" data-overflow="wrap"><code class="lang-shellscript">aws ecr get-login-password --region &#x3C;aws region> \
       | docker login --username AWS --password-stdin &#x3C;aws account id>.dkr.ecr.&#x3C;aws region>.amazonaws.com
     </code></pre>
   * For GCP, authenticate to Google Artifact Registry (GAR) with a specific Artifact Registry host by running the following commands, replacing `<region>` with the value for your region:&#x20;

     ```shellscript
     gcloud auth login
     gcloud auth configure-docker <region>.pkg.dev
     ```
   * For Azure, authenticate to ACR by running the following commands, replacing `<registryName>` with the name of your registry:&#x20;

     ```shellscript
     az login
     az acr login --name <registryName>
     ```
4. Tag and push the PDI Docker image to your cloud provider.

   * For AWS, run the following command, replacing `<build number>`, `<aws account id>`, and `<region>` with the values from the downloaded file and your AWS account:

     <pre class="language-shellscript" data-overflow="wrap"><code class="lang-shellscript">docker tag pentaho/pdi:11.0.0.0-&#x3C;build number>&#x3C;aws account id>.dkr.ecr.&#x3C;region>.amazonaws.com/dockmaker-pdi:&#x3C;build number>                                  
     docker push &#x3C;aws account id>.dkr.ecr.&#x3C;region>.amazonaws.com/dockmaker-pdi:&#x3C;build number>
     </code></pre>
   * For GCP, run the following command, replacing `<build number>`, `<aws account id>`, and `<region>` with the values from the downloaded file and your GAR account:

     <pre class="language-shellscript" data-overflow="wrap"><code class="lang-shellscript">docker tag pentaho/pdi:11.0.0.0-&#x3C;build number> \
       &#x3C;region>-docker.pkg.dev/&#x3C;project id>/&#x3C;repository>/pdi:&#x3C;build number>
     docker push &#x3C;region>-docker.pkg.dev/&#x3C;project id>/&#x3C;repository>/pentaho-server:&#x3C;build number>
     </code></pre>
   * For Azure, run the following commands, replacing `<image name>`, `<registry name>`, and `<image name on acr>` with the values from the downloaded file and your Azure account:

     <pre class="language-shellscript" data-overflow="wrap"><code class="lang-shellscript">docker tag &#x3C;image name> &#x3C;registry name>.azurecr.io/&#x3C;image name on acr>
     docker push &#x3C;registry name>.azurecr.io/&#x3C;image name on acr>
     </code></pre>

   The PDI image for Carte, Kitchen, and Pan is tagged and pushed to your cloud provider.

#### Configure storage in the cloud

To configure storage in the cloud, complete the following steps:&#x20;

1. On your local workstation, extract the ZIP file that contains the configuration files for your environment to a temporary working directory.&#x20;

   * `aws-11.0.0.0-<build number>.zip`&#x20;
   * `gcp-11.0.0.0-<build number>.zip`
   * `azure-11.0.0.0-<build number>.zip`

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>Note:</strong> You downloaded the  <code>aws-11.0.0.0-&#x3C;build number>.zip</code> file in the previous section, <a href="#download-pdi-docker-files">Download PDI Docker files</a>.</p></div>
2. In your working directory, go to the `pdi` directory for your environment:
   * `aws-11.0.0.0-<build number>/dist/aws/pdi` &#x20;
   * `gcp-11.0.0.0-<build number>/dist/gcp/pdi`
   * `azure-11.0.0.0-<build number>/dist/azure/pdi`
3. In a text editor, edit the `volumes.yaml` file with the values for your environment.&#x20;
4. Save and close the `volumes.yaml` file.
5. Create storage for each subdirectory that appears in the `pdi` directory for your environment.&#x20;
   * For AWS, in your EKS cluster, create an S3 bucket for each of the following subdirectories:
     * `config`
     * `logs`
     * `softwareOverride`
     * `solutionFiles`&#x20;
   * For GCP, in your Google Kubernetes Engine (GKE) cluster, create a GCS bucket for&#x20;

     each of the following subdirectories:

     * `config`
     * `logs`
     * `softwareOverride`
     * `solutionFiles`&#x20;
   * For Azure, in your Azure Kubernetes cluster, create a file share for each of the following subdirectories:
     * `config`
     * `logs`
     * `softwareOverride`
     * `solutionFiles`&#x20;
6. Go back to the `pdi` directory and open a command prompt.
7. In the command prompt, create persistent volumes and persistent volume claims by running the following command:

   ```shellscript
   kubectl apply -f volumes.yaml
   ```

   Storage is configured so that you can run Pentaho command-line tools (Carte, Kitchen, and Pan) in containers.

#### Edit YAML files for deploying to the cloud

1. In your working directory, go to the `pdi` directory for your environment:
   * `aws-11.0.0.0-<build number>/dist/aws/pdi` &#x20;
   * `gcp-11.0.0.0-<build number>/dist/gcp/pdi`
   * `azure-11.0.0.0-<build number>/dist/azure/pdi`
2. In a text editor, edit the `carte.yaml`, `kitchen.yaml`, and `pan.yaml` files for your environment.
   * For AWS, you must update the following values before deploying command-line tools in containers:

     <pre class="language-yaml" data-overflow="wrap"><code class="lang-yaml"> # Replace &#x3C;aws account id>, &#x3C;region>, and &#x3C;build number> 
     containers:
         - name: &#x3C;Carte | Kitchen | Pan> # Pre-filled per file, do not modify
           image: &#x3C;aws account id>.dkr.ecr.&#x3C;region>.amazonaws.com/&#x3C;repository>/pdi:11.0.0.0-&#x3C;build number>
     </code></pre>

     <pre class="language-yaml" data-overflow="wrap"><code class="lang-yaml"># Replace &#x3C;your license URL>
     env:
        - name: LICENSE_URL
          value: "&#x3C;your license URL>"
     </code></pre>

     The following code is an example of the `.yaml` file contents used for Carte when deploying to AWS.

     <pre class="language-yaml" data-overflow="wrap" data-full-width="true" data-expandable="true"><code class="lang-yaml"># Service for Carte
     apiVersion: v1
     kind: Service
     metadata:
       name: carte-service
       namespace: pdi
       labels:
         app: carte-service
     spec:
       type: NodePort
       selector:
         app: carte
       ports:
         - port: 8081
           targetPort: 8081
           nodePort: 30081
     ---
     # Deployment with direct mounts (no subPath)
     apiVersion: apps/v1
     kind: Deployment
     metadata:
       name: carte
       namespace: pdi
       labels:
         app: carte
     spec:
       replicas: 1
       selector:
         matchLabels:
           app: carte
       strategy:
         type: RollingUpdate
         rollingUpdate:
           maxSurge: 25%
           maxUnavailable: 25%
       template:
         metadata:
           labels:
             app: carte
         spec:
           serviceAccountName: pdi-s3-access
           securityContext:
             runAsUser: 5000
             runAsGroup: 5000
             runAsNonRoot: true
           volumes:
             - name: softwareoverride
               persistentVolumeClaim:
                 claimName: s3-pvc-softwareoverride
             - name: solutionfiles
               persistentVolumeClaim:
                 claimName: s3-pvc-solutionfiles
             - name: config
               persistentVolumeClaim:
                 claimName: s3-pvc-config
             - name: logs
               emptyDir: {}
           containers:
             - name: carte
               image: 524647911006.dkr.ecr.us-east-2.amazonaws.com/dockmaker-pdi:11.0.0.0-18
               imagePullPolicy: Always
               resources:
                 limits:
                   memory: "2500Mi"
                 requests:
                   memory: "1500Mi"
               ports:
                 - containerPort: 8081
               volumeMounts:
                 - name: softwareoverride
                   mountPath: /docker-entrypoint-init/
                 - name: solutionfiles
                   mountPath: /mnt/solutionfiles
                 - name: config
                   mountPath: /mnt/config
                 - name: logs
                   mountPath: /opt/pentaho/data-integration/logs
               args: ["/opt/pentaho/data-integration/carte.sh", "/mnt/config/carte-config.xml"]
               env:
                 - name: LICENSE_URL
                   value: "&#x3C;your license url>"
             - name: s3-test
               image: amazon/aws-cli:2.15.0
               imagePullPolicy: Always
               command:
                 - /bin/sh
                 - -c
               args:
                 - |
                   while true; do
                     echo "Uploading logs to S3"
                     aws s3 sync /logs s3://ackbar-development/dockmaker/pdi/logs/ --region us-east-2
                     sleep 60
                   done
               env:
                 - name: HOME
                   value: /tmp
               volumeMounts:
                 - name: logs
                   mountPath: /logs

     </code></pre>
   * For GCP, you must update the following values before deploying command-line tools in containers:

     <pre class="language-yaml" data-overflow="wrap"><code class="lang-yaml"># Replace &#x3C;aws account id>, &#x3C;region>, and &#x3C;build number> 
     containers:
         - name: &#x3C;Carte | Kitchen | Pan> # Pre-filled per file, do not modify
           image: &#x3C;region>-docker.pkg.dev/&#x3C;project id>/&#x3C;repository>/pdi:11.0.0.0-&#x3C;build number>
     </code></pre>

     <pre class="language-yaml" data-overflow="wrap"><code class="lang-yaml"># Replace &#x3C;your license URL>
     env:
        - name: LICENSE_URL
          value: "&#x3C;your license URL>"
     </code></pre>

     The following code is an example of the `.yaml` file contents used for Carte when deploying to GCP.

     <pre class="language-yaml" data-overflow="wrap" data-full-width="true" data-expandable="true"><code class="lang-yaml"># Service to expose the Carte server using a LoadBalancer
     apiVersion: v1
     kind: Service
     metadata:
       name: carte-service
       namespace: pdi
       labels:
         app: carte-service
     spec:
       type: LoadBalancer
       selector:
         app: carte-server
       ports:
         - port: 8081
           targetPort: 8080

     ---

     # Deployment to run the Carte server
     apiVersion: apps/v1
     kind: Deployment
     metadata:
       name: carte-server
       namespace: pdi
     spec:
       replicas: 1
       selector:
         matchLabels:
           app: carte-server
       template:
         metadata:
           annotations:
             gke-gcsfuse/volumes: "true"  # Enable GCSFuse volume mounting
           labels:
             app: carte-server
         spec:
           serviceAccountName: gcs-access-pdi
           volumes:
             - name: persistent-storage
               persistentVolumeClaim:
                 claimName: pdia-pv-pdi
             - name: pentaho-license
               secret:
                 secretName: pentaho-license
                 optional: true
           
           containers:
             - name: carte-server
               image: us-east1-docker.pkg.dev/pentaho-lee-cheng/pentaho-docker-repo/pdi:10.3.0.0-353
               imagePullPolicy: Always
               resources:
                 limits:
                   memory: "4500Mi"
                 requests:
                   memory: "2000Mi"
               ports:
                 - containerPort: 8081
               securityContext:
                 runAsUser: 5000
                 runAsGroup: 5000
               volumeMounts:
                 - name: persistent-storage
                   mountPath: /docker-entrypoint-init/
                   subPath: ackbar-dev/pdia-docker-file-share-pdi/carte/softwareOverride
                   readOnly: false
                 - name: persistent-storage
                   mountPath: /opt/pentaho/solution/
                   subPath: ackbar-dev/pdia-docker-file-share-pdi/carte/solutionFiles
                   readOnly: false
                 - name: persistent-storage
                   mountPath: /home/pentaho
                   subPath: ackbar-dev/pdia-docker-file-share-pdi/carte/config
                   readOnly: false
                 - name: persistent-storage
                   mountPath: /opt/pentaho/data-integration/logs
                   subPath: ackbar-dev/pdia-docker-file-share-pdi/carte/logs
                   readOnly: false
               args: ["/opt/pentaho/data-integration/carte.sh", "/home/pentaho/carte-config.xml"]
               env:
                 - name: LICENSE_URL
                   value: "&#x3C;your license URL>"
     </code></pre>
   * For Azure, you must update the following values before deploying command-line tools in containers:

     <pre class="language-yaml" data-overflow="wrap"><code class="lang-yaml"># Replace &#x3C;aws account id>, &#x3C;region>, and &#x3C;build number> 
     containers:
         - name: &#x3C;Carte | Kitchen | Pan> # Pre-filled per file, do not modify
           image: &#x3C;registry>.azurecr.io/pdi:11.0.0.0-&#x3C;build number>
     </code></pre>

     <pre class="language-yaml" data-overflow="wrap"><code class="lang-yaml"># Replace &#x3C;your license URL>
     env:
        - name: LICENSE_URL
          value: "&#x3C;your license URL>"
     </code></pre>

     The following code is an example of the `.yaml` file contents used for Carte when deploying to Azure.

     <pre class="language-yaml" data-overflow="wrap" data-full-width="true" data-expandable="true"><code class="lang-yaml"># LoadBalancer service to expose the application
     apiVersion: v1
     kind: Service
     metadata:
       name: carte-service  # Replace (optional) with your service name
       namespace: pdi  # Must match the namespace
       labels:
         app: carte-service
     spec:
       type: LoadBalancer
       selector:
         app: pdi  # Must match the label in the deployment
       ports:
         - port: 8081
           targetPort: 8080

     ---

     # Deployment for running the Carte server
     apiVersion: apps/v1
     kind: Deployment
     metadata:
       name: carte-server  
       namespace: pdi  # Must match the namespace
     spec:
       replicas: 1  # Modify if you need multiple pods
       selector:
         matchLabels:
           app: pdi
       template:
         metadata:
           labels:
             app: pdi
         spec:
           containers:
             - name: carte
               image: pentahopdia.azurecr.io/pdi:11.0.0.0-xxx  # Replace with your image
               imagePullPolicy: "Always"
               resources:
                 limits:
                   memory: "4500Mi"
                 requests:
                   memory: "2000Mi"
               ports:
                 - containerPort: 8081
               volumeMounts:
                 - name: azure-file-share
                   mountPath: /docker-entrypoint-init/
                   subPath: carte/softwareOverride
                   readOnly: false
                 - name: azure-file-share
                   mountPath: /opt/pentaho/solution/
                   subPath: carte/solutionFiles
                   readOnly: false
                 - name: azure-file-share
                   mountPath: /home/pentaho
                   subPath: carte/config
                   readOnly: false
                 - name: azure-file-share
                   mountPath: /opt/pentaho/data-integration/logs
                   subPath: carte/logs
                   readOnly: false
               args: ["/opt/pentaho/data-integration/carte.sh", "/home/pentaho/carte-config.xml"]
               env:
                 - name: LICENSE_URL
                   value: "&#x3C;your license URL>"  # Replace with your license URL
           volumes:
             - name: azure-file-share
               persistentVolumeClaim:
                 claimName: pdia-pv-pdi  # Must match the PVC name
                 readOnly: false
       
     </code></pre>
3. In the `pan.yaml` file, update the file location for the transformation (.ktr) file that you plan to run. The following code example has the file location for the `Rounding.ktr` sample file:

   <pre class="language-yaml" data-overflow="wrap"><code class="lang-yaml">args:
    - "-file=/opt/pentaho/data-integration/samples/transformations/Rounding.ktr"
   </code></pre>
4. In the `kitchen.yaml` file, update the file location for the job (.kjb) file that you plan to run. The following code example has the file location for the `Set arguments on a transformation.kjb` sample file:

   <pre class="language-yaml" data-overflow="wrap"><code class="lang-yaml">args:
     - "-file=/opt/pentaho/data-integration/samples/jobs/arguments/Set arguments on a transformation.kjb"
   </code></pre>
5. Save and close the `carte.yaml`, `kitchen.yaml`, and `pan.yaml` files for your environment.

#### Upload PDI files to the cloud

1. In your working directory, go to the `pdi` directory for your environment:
   * `aws-11.0.0.0-<build number>/dist/aws/pdi` &#x20;
   * `gcp-11.0.0.0-<build number>/dist/gcp/pdi`
   * `azure-11.0.0.0-<build number>/dist/azure/pdi`
2. Add PDI files to one or more of the following subdirectories:
   * `config`: Contains Pentaho files, like `.kettle` and `.pentaho` files, as well as configuration files, such as `.aws` and `.ssh` files.
   * `softwareOverride`: Contains configuration files that override the default settings in the PDI installation.
   * `solutionFiles`: Contains project solution files, including transformations (`.ktr`), jobs (`.kjb`), and any related `.kettle` files.
3. Upload the contents of each subdirectory to the corresponding bucket or file share in your cloud storage.

### Run Carte in a cloud container

**Before you begin**

* Verify that you have uploaded your transformation (`.ktr`) files, job (`.kjb`) files,  and any related `.kettle` files to the `solutionFiles` bucket or file share in your cloud storage.
* Verify that your `carte.yaml` file is updated with the values for your environment.

**Procedure**

1. In your working directory, go to the `pdi` directory for your environment and open a command prompt:
   * `aws-11.0.0.0-<build number>/dist/aws/pdi` &#x20;
   * `gcp-11.0.0.0-<build number>/dist/gcp/pdi`
   * `azure-11.0.0.0-<build number>/dist/azure/pdi`
2. Run the following commands:

   <pre class="language-shellscript" data-overflow="wrap"><code class="lang-shellscript">kubectl apply -f carte.yaml

   # Replace &#x3C;namespace>
   kubectl get pods -n &#x3C;namespace>

   # Replace &#x3C;pod name> and &#x3C;namespace>
   kubectl logs &#x3C;pod name>  -n &#x3C;namespace>
   </code></pre>
3. To verify that Carte is running, log into the Carte homepage at `http://<host>:<port>/kettle/status` or the external IP address assigned to the deployment. You can obtain the URL by running the following command:

   ```shellscript
   kubectl get nodes -o wide
   ```
4. (Optional) To execute a transformation (`.ktr`) or job (`.kjb`) that you added to the `solutionFiles` directory and uploaded to your cloud storage, go to one of the following URLs in your browser:
   * <pre data-overflow="wrap"><code>http://&#x3C;host>:&#x3C;port>/kettle/executeTrans/?trans=&#x3C;path to transformation>/&#x3C;transformation name>&#x26;level=Basic
     </code></pre>
   * <pre data-overflow="wrap"><code>http://&#x3C;host>:&#x3C;port>/kettle/executeJob/?job=&#x3C;path to job>/&#x3C;job name>.kjb&#x26;level=Basic
     </code></pre>
5. To verify Carte deployment in a container, open a command prompt and run the following command, replacing `<name of carte pod>`:

   ```shellscript
   kubectl logs <name of carte pod> -n pdi --follow
   ```

### Run Kitchen in a cloud container

**Before you begin**

* Verify that you have uploaded your job (`.kjb`) files and any related `.kettle` files to the `solutionFiles` bucket or file share in your cloud storage.
* Verify that your `kitchen.yaml` file is updated with the correct values for your environment, and that it specifies the correct file location for the job (`.kjb`) file you plan to run.

**Procedure**

1. In your working directory, go to the `pdi` directory for your environment and open a command prompt:
   * `aws-11.0.0.0-<build number>/dist/aws/pdi` &#x20;
   * `gcp-11.0.0.0-<build number>/dist/gcp/pdi`
   * `azure-11.0.0.0-<build number>/dist/azure/pdi`
2. Run the following commands:

   <pre class="language-shellscript" data-overflow="wrap"><code class="lang-shellscript">kubectl apply -f kitchen.yaml

   # Replace &#x3C;namespace>
   kubectl get jobs -n &#x3C;namespace>

   # Replace &#x3C;job name> and &#x3C;namespace>
   kubectl describe job &#x3C;job-name> -n &#x3C;namespace>

   # Replace &#x3C;job name> and &#x3C;namespace>
   kubectl logs job/&#x3C;job-name> -n &#x3C;namespace>
   </code></pre>
3. To verify Kitchen deployment in a container, open a command prompt and run the following command, replacing `<name of kitchen pod>`:

   ```shellscript
   kubectl logs <name of kitchen pod> -n pdi --follow
   ```

{% hint style="info" %}
**Notes:**

* To rerun a job with a new parameter, you must delete the existing job, recreate the job with the new parameter, and then and run it again. You can delete a job by running the following command, replacing `<job name>` and `<namespace>`:

  ```shellscript
  kubectl delete job <job name> --namespace <namespace>
  ```
* If the path to the job changes, you must update it in the `pan.yaml` file and apply the YAML file again.
  {% endhint %}

### Run Pan in a cloud container

**Before you begin**

* Verify that you have uploaded your transformation (`.ktr`) files and any related `.kettle` files to the `solutionFiles` bucket or file share in your cloud storage.
* Verify that your `pan.yaml` file is updated with the correct values for your environment, and that it specifies the correct file location for the transformation (`.ktr`) file you plan to run.

**Procedure**

To run Pan in a Docker container, complete the following steps:

1. In your working directory, go to the `pdi` directory for your environment and open a command prompt:
   * `aws-11.0.0.0-<build number>/dist/aws/pdi` &#x20;
   * `gcp-11.0.0.0-<build number>/dist/gcp/pdi`
   * `azure-11.0.0.0-<build number>/dist/azure/pdi`
2. Run the following commands:

   <pre class="language-shellscript" data-overflow="wrap"><code class="lang-shellscript">kubectl apply -f pan.yaml

   # Replace &#x3C;namespace>
   kubectl get jobs -n &#x3C;namespace>

   # Replace &#x3C;job name> and &#x3C;namespace>
   kubectl describe job &#x3C;job-name> -n &#x3C;namespace>

   # Replace &#x3C;job name> and &#x3C;namespace>
   kubectl logs job/&#x3C;job-name> -n &#x3C;namespace>
   </code></pre>
3. To verify Pan deployment in a container, open a command prompt and run the following command, replacing `<name of pan pod>`:

   ```shellscript
   kubectl logs <name of pan pod> -n pdi --follow
   ```
