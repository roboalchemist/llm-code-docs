# Source: https://docs.pentaho.com/pdc-10.2-install/install-pentaho-data-catalog/install-data-catalog-on-openshift-ocp-okd.md

# Install Data Catalog on OpenShift (OCP/OKD)

Installing Data Catalog on OpenShift enables administrators to deploy and manage Data Catalog in a secure, enterprise Kubernetes environment while using OpenShift features such as project isolation, routes for external access, and enforced security controls. This topic describes how to install Data Catalog on an OpenShift Container Platform (OCP) or OKD cluster using Helm and Helmfile.

**Before you begin**

Ensure that the following requirements are met:

* kubectl v1.34.2, Helm v3.17.2, and Helmfile v1.1.2 are installed.
* You can access the OpenShift cluster from your system.
* You have permissions to create namespaces and manage Security Context Constraints (SCC).
* The OpenShift cluster has a Filesystem-based storage class with ReadWriteExecute (RWX) access.
* You have Pentaho JFrog Artifactory credentials.
* You have a valid Data Catalog license server URL.

This procedure applies to PDC 10.2.9 and later and uses the bundled metadata stores and the default self-signed certificate.

**Procedure**

1. Download the PDC Helm deployment package from the Pentaho JFrog repository.

   ```
   curl -u<jfrog_username>:<jfrog_token> -L -O \
   "https://one.hitachivantara.com/artifactory/pdc-generic-dev/pentaho/pdc-docker-deployment/release-v10.2.10/pdc-full-release-[build_number]-k8s.tgz"
   ```
2. Extract the downloaded archive to the /opt directory.

   ```
   tar -xvf pdc-full-release-[build_number]-k8s.tgz -C /opt
   ```

   The extraction creates the pentaho/pdc-helm-charts directory.
3. Change to the Helm charts directory.

   ```
   cd /opt/pentaho/pdc-helm-charts
   ```
4. Create a custom values file by copying the example file.

   ```
   cp conf/default/example.custom-values.yaml conf/default/custom-values.yaml
   ```
5. Open the custom values file for editing.

   ```
   vi conf/default/custom-values.yaml
   ```
6. Update the following configuration values, and then save the file.
   1. globalOverrides.applicationFqdn: The fully qualified domain name (DNS) of your OpenShift cluster.
   2. globalOverrides.imageRegistryUserName: Provided JFrog username.
   3. globalOverrides.imageRegistryUserPassword: Provided JFrog token.
   4. cat.licensing-api.licenseServerUrl: Provided Data Catalog license server URL.
   5. cat.fe-workers.persistence.storageClass: OpenShift Cluster’s storage class.

      ```
      globalOverrides:
        applicationFqdn: <fqdn to access the application>
        imageRegistryName: one.hitachivantara.com/docker
        imageRegistryUserName: <hitachi jfrog username>
        imageRegistryUserPassword: <hitachi jfrog token>

      opensearch:
        sysctlImage:
          enabled: false
        volumePermissions:
          enabled: false

      oc-routes:
        enabled: true

      cat:
        licensing-api:
          licenseServerUrl: <pdc license server url>
        
        fe-workers:
          persistence:
            storageClass: <storage class>     # Replace with the storage class available in your cluster
      ```
7. Create a namespace to deploy Data Catalog.

   ```
   kubectl create ns <namespace>
   ```
8. Assign the required Security Context Constraints to the PDC service accounts.

   ```
   oc adm policy add-scc-to-group anyuid system:serviceaccounts:<namespace>
   oc adm policy add-scc-to-user privileged -z pdso-data-service -n <namespace>
   ```
9. Deploy Data Catalog using Helmfile.

   ```
   helmfile sync -n <namespace>
   ```

   This deploys the PDC components to your OpenShift cluster based on the configurations defined in your custom-values.yaml.
10. Once the helmfile sync is successful, verify that the pods and services are running.

    ```
    kubectl get pods,svc -n <namespace>
    ```
11. Access Data Catalog from a browser using the configured DNS name.

    ```
    https://<applicationFqdn>
    ```

    **Caution**: Because the deployment uses a self-signed certificate, your browser may display a certificate warning.

**Result**

Data Catalog is installed and running on the OpenShift (OCP/OKD) cluster and is accessible through an OpenShift Route.

**What’s next**

After installing Data Catalog, you can perform additional configuration tasks based on your environment and requirements. These tasks include configuring security, authentication, SSL certificates, external services, storage, and other advanced settings.

For more information, see the [Advanced configuration](https://app.gitbook.com/s/cUaDtyTop3vo8cjqgjGk/ldc-advanced-configuration-ut_cp) section in [Administer Pentaho Data Catalog](https://app.gitbook.com/s/cUaDtyTop3vo8cjqgjGk/).
