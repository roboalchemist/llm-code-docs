# Source: https://docs.pentaho.com/pdc-admin/backup-and-restore-in-amazon-eks.md

# Backup and restore in Amazon EKS

n Pentaho Data Catalog deployments running on Amazon Elastic Kubernetes Service (EKS), administrators can configure and manage backups to protect critical system data and metadata. The backup and restore framework helps ensure business continuity by enabling recovery of Data Catalog components, such as PostgreSQL, MongoDB, OpenSearch, FE-Workers, and Kubernetes objects.

Data Catalog supports multiple storage options for storing backup data:

* Amazon Simple Storage Service (S3) for scalable, cloud-based backups.
* Amazon Elastic Block Store (EBS) and Amazon Elastic File System (EFS) for persistent storage within the Amazon EKS cluster.

This section includes detailed procedures to:

* [#configure-a-backup-in-amazon-eks](#configure-a-backup-in-amazon-eks "mention")
* [#run-a-backup-in-amazon-eks](#run-a-backup-in-amazon-eks "mention")
* [#verify-backups-in-amazon-eks](#verify-backups-in-amazon-eks "mention")
* [#restore-data-from-backup-in-amazon-eks](#restore-data-from-backup-in-amazon-eks "mention")

{% hint style="info" %}
Backup and restore operations must be performed by administrators with access to the EKS cluster and the configured storage backend.
{% endhint %}

## **Configure a backup in Amazon EKS** <a href="#configure-a-backup-in-amazon-eks" id="configure-a-backup-in-amazon-eks"></a>

In Data Catalog deployments running on Amazon EKS, administrators can configure automated or manual backups for key Data Catalog components. The configuration specifies which services to back up, how often backups run, and where backup data is stored. You can store backups in Amazon Simple Storage Service (Amazon S3), Amazon Elastic Block Store (Amazon EBS), or Amazon Elastic File System (Amazon EFS). Data

Catalog supports multiple storage configurations that let you choose how backups are created and managed. Depending on your environment, you can either use an existing PersistentVolumeClaim (PVC) or let Helm automatically create and manage the PVC during deployment. After setup, backups run automatically through a CronJob in Amazon EKS or can be triggered manually when needed. Retention policies, backup frequency, and storage locations are defined in the Helm configuration.

{% hint style="info" %}
If your Data Catalog deployment uses an external PostgreSQL database such as Amazon Aurora, Data Catalog doesn’t back up that external database. In this case, set the `postgres.enabled` parameter to `false` in the backup configuration, and manage the external database backup separately.
{% endhint %}

### **Configure a backup using Amazon S3 with the existing PVC** <a href="#configure-a-backup-using-amazon-s3-with-the-existing-pvc" id="configure-a-backup-using-amazon-s3-with-the-existing-pvc"></a>

In Data Catalog deployments running on Amazon EKS, administrators can store backup data in Amazon S3 using a pre-existing PersistentVolumeClaim (PVC). This configuration allows you to use an existing PVC that is already linked to an S3 bucket through the Amazon S3 Container Storage Interface (CSI) driver. By referencing this PVC in the backup configuration, Data Catalog writes backup data directly to the configured S3 bucket.

When using an existing PVC for S3 storage, ensure that the PVC and its associated StorageClass are correctly configured with the AWS S3 CSI driver and the target S3 bucket.

Perform the following steps to configure a backup using Amazon S3 with the existing PVC:

**Before you begin**

* Verify that the Amazon S3 CSI driver is installed in your Amazon EKS cluster.
* Ensure that an S3 bucket is available for storing backup data.
* Confirm that the PersistentVolumeClaim (PVC) for S3 is pre-created and bound to the S3 StorageClass.
* Verify that the PDC namespace and Helm deployment are accessible.
* Ensure that worker nodes have the required IAM permissions to access the S3 bucket.
* Locate the `custom-values.yaml` file used for your PDC Helm deployment.

**Procedure**

1. Open the custom-values.yaml file for your PDC deployment in a text editor.
2. Add or update the following backup configuration block:

   ```
   # custom-values.yaml
   backup:
     storage:
       requiresTempStorage: true
       tmpStorage:
         sizeLimit: 2Gi
     persistence:
       enabled: false
       existingClaim: "s3-pdc-backup-pvc"  # User-created S3 PVC
   ```
3. Save the configuration file.
4. Apply the configuration to the Amazon EKS cluster.

   ```
   helmfile -n <PDC_NAMESPACE> sync
   ```

   or

   ```
   helm upgrade --install pdc ./pdc-chart -n <PDC_NAMESPACE>
   ```
5. Verify that the backup CronJob is created in the EKS cluster.

   ```
   kubectl get cronjobs -n <PDC_NAMESPACE>
   ```
6. Review the CronJob details to confirm the schedule, storage configuration, and PVC reference.

   ```
   kubectl describe cronjob pdc-backup -n <PDC_NAMESPACE>
   ```

   The CronJob specification should reference the PVC name s3-pdc-backup-pvc.

**Example: S3 StorageClass and PersistentVolume**

The underlying PV must have S3 specifications, such as `bucket-name` and `aws-region` and PV and PVC size must match to '`backup.persistence.size`'.

```
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: s3-csi
provisioner: s3.csi.aws.com
reclaimPolicy: Retain
volumeBindingMode: Immediate

---

apiVersion: v1
kind: PersistentVolume
metadata:
  name: s3-pv
spec:
  capacity:
    storage: 50Gi
  accessModes:
    - ReadWriteMany
  storageClassName: s3-csi
  mountOptions:
    - region=$<aws_region>
    - allow-other
  persistentVolumeReclaimPolicy: Retain
  csi:
    driver: s3.csi.aws.com
    volumeHandle: $<pdc-backup-bucket>
    volumeAttributes:
      bucketName: $<pdc-backup-bucket>
      region: $<aws_region>
```

{% hint style="info" %}
The PVC name `s3-pdc-backup-pvc` must match the value specified in the backup configuration block.
{% endhint %}

**Result**

Data Catalog is configured to store backups in Amazon S3 using the existing PVC. The backup CronJob runs automatically according to the configured schedule and writes backup files directly to the S3 bucket linked with the PVC.

### **Configure a backup using Amazon S3 with the Helm-managed PVC**

In Data Catalog deployments running on Amazon EKS, administrators can configure backups to use Amazon S3 through a Helm-managed PersistentVolumeClaim (PVC). In this configuration, the Data Catalog Helm chart automatically creates the PVC and connects it to the S3 bucket using the Amazon S3 Container Storage Interface (CSI) driver. This method simplifies setup because the PVC does not need to be created manually before deployment.

The Amazon S3 CSI driver must be installed in the EKS cluster, and the specified StorageClass must be compatible with the S3 driver.

Perform the following steps to configure a backup using Amazon S3 with the Helm-managed PVC:

**Before you begin**

* Verify that the Amazon S3 CSI driver is installed in the Amazon EKS cluster.
* Ensure that an S3 bucket is available and accessible to the EKS worker nodes.
* Confirm that Helm 3.0 or later and kubectl are installed.
* Verify that the PDC namespace is accessible.
* Identify or create a StorageClass compatible with S3.
* Confirm that the `custom-values.yaml` file for your Helm deployment is available for editing.

**Procedure**

1. Open the `custom-values.yaml` file used for your PDC Helm deployment.
2. Add or update the following backup configuration block:

   ```
   # values.yaml
   backup:
     storage:
       requiresTempStorage: true
       tmpStorage:
         sizeLimit: 2Gi
     persistence:
       enabled: true
       existingClaim: ""
       storageClass: "s3-csi"  # Available S3-compatible StorageClass; if not defined, default will be used
       volumeName: "s3-pv"     # This PV must be pre-existing
   ```

   In this case, if the customer wants the PVC to be created by Helmfile, the storageClass and volumeName must be pre-existing and specified in the configuration, as shown above.
3. Save the configuration file.
4. Apply the configuration to the Amazon EKS cluster.

   ```
   helmfile -n <PDC_NAMESPACE> sync
   ```

   or

   ```
   helm upgrade --install pdc ./pdc-chart -n <PDC_NAMESPACE>
   ```
5. Verify that the backup CronJob is created successfully.

   ```
   kubectl get cronjobs -n <PDC_NAMESPACE>
   ```
6. Review the CronJob details to confirm that the schedule and the storageClass reference match your configuration.

   ```
   kubectl describe cronjob pdc-backup -n <PDC_NAMESPACE>
   ```
7. Verify that the Helm deployment automatically created the backup PVC.

   ```
   kubectl get pvc -n <PDC_NAMESPACE> | grep backup
   ```

**Example: S3 StorageClass and PersistentVolume**

The underlying PV must have S3 specifications, such as `bucket-name` and `aws-region` and PV and PVC size must match to '`backup.persistence.size`'.

```
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: s3-csi
provisioner: s3.csi.aws.com
parameters:
  mounter: fuse
  bucket: <S3_BUCKET_NAME>
  region: <AWS_REGION>
---
apiVersion: v1
kind: PersistentVolume
metadata:
  name: s3-pv
spec:
  capacity:
    storage: 50Gi
  accessModes:
    - ReadWriteOnce
  storageClassName: s3-csi
  csi:
    driver: s3.csi.aws.com
    volumeHandle: s3-pv
```

{% hint style="info" %}
The Helm deployment automatically creates the PVC using the storageClass and volumeName values defined in the backup configuration block. The volumeName must match the existing PersistentVolume that points to the S3 bucket.
{% endhint %}

**Result**

The PDC backup configuration is updated to use Amazon S3 with a Helm-managed PVC. When the backup CronJob runs, it automatically mounts the PVC and stores all backup files directly in the configured S3 bucket.

### **Configure a backup using Amazon EBS or EFS with the existing PVC**

In Data Catalog deployments running on Amazon EKS, administrators can configure backups to use Amazon EBS or Amazon EFS through an existing PersistentVolumeClaim (PVC). This configuration allows you to use a pre-created PVC that points to an EBS or EFS volume already available in your Amazon EKS cluster. The PDC backup process writes all backup data to this PVC, which is mounted as persistent storage within the cluster.

{% hint style="info" %}
When using an existing PVC, ensure the PVC and its associated StorageClass are configured properly and have sufficient capacity to store the backup files.
{% endhint %}

Perform the following steps to configure a backup using Amazon EBS or EFS with the existing PVC:

**Before you begin**

* Verify that the EBS or EFS StorageClass is configured in your Amazon EKS cluster.
* Ensure that a PersistentVolumeClaim (PVC) is pre-created and bound to the desired EBS or EFS volume.
* Confirm that the PDC namespace and Helm deployment are accessible.
* Ensure that you have Helm 3.0 or later and kubectl installed.
* Locate the `custom-values.yaml` file used for your PDC Helm deployment.

**Procedure**

1. Open the `custom-values.yaml` file for your PDC deployment in a text editor.
2. Add or update the following backup configuration block:

   ```
   # values.yaml
   backup:
     storage:
       requiresTempStorage: false
       tmpStorage:
         sizeLimit: 2Gi
     persistence:
       enabled: false
       existingClaim: "pdc-backup-pvc"  # User-created EBS/EFS PVC
   ```

   In this case, if the customer has their own PVC, the name of the PVC must be specified in the configuration as shown above.
3. Save the configuration file.
4. Apply the configuration to the Amazon EKS cluster.

   ```
   helmfile -n <PDC_NAMESPACE> sync
   ```

   or

   ```
   helm upgrade --install pdc ./pdc-chart -n <PDC_NAMESPACE>
   ```
5. Verify that the backup CronJob is created in the EKS cluster.

   ```
   kubectl get cronjobs -n <PDC_NAMESPACE>
   ```
6. Review the CronJob details to confirm the schedule, PVC reference, and component backup targets.

   ```
   kubectl describe cronjob pdc-backup -n <PDC_NAMESPACE>
   ```

   The CronJob should reference the existing PVC pdc-backup-pvc.
7. Verify that the PVC is correctly mounted and available in the cluster.

   ```
   kubectl get pvc -n <PDC_NAMESPACE>
   ```

**Example: EBS or EFS PersistentVolume and PVC**

```
apiVersion: v1
kind: PersistentVolume
metadata:
  name: pdc-backup-pv
spec:
  capacity:
    storage: 100Gi
  accessModes:
    - ReadWriteOnce
  storageClassName: ebs-sc
  awsElasticBlockStore:
    volumeID: <EBS_VOLUME_ID>
    fsType: ext4
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: pdc-backup-pvc
  namespace: <PDC_NAMESPACE>
spec:
  accessModes:
    - ReadWriteOnce
  storageClassName: ebs-sc
  resources:
    requests:
      storage: 100Gi
```

{% hint style="info" %}
If using Amazon EFS, replace the `awsElasticBlockStore` section with an `efs.csi.aws.com` driver configuration.
{% endhint %}

**Result**

The PDC backup configuration is updated to use Amazon EBS or Amazon EFS storage through the specified existing PVC. When the backup CronJob runs, it stores all backup files on the mounted persistent volume, enabling quick recovery from local cluster storage.

### **Configure a backup using Amazon EBS or EFS with Helm-managed PVC**

In Data Catalog deployments running on Amazon EKS, administrators can configure backups to use Amazon EBS or Amazon EFS through a Helm-managed PersistentVolumeClaim (PVC). In this configuration, the Helm deployment automatically creates and manages the PVC based on the provided StorageClass configuration. This approach is recommended when administrators prefer automated storage management and do not want to manually create PVCs before deployment.

{% hint style="info" %}
Ensure that the StorageClass used for EBS or EFS is available and properly configured in your Amazon EKS cluster before enabling Helm-managed PVC creation.
{% endhint %}

Perform the following steps to configure a backup using Amazon EBS or EFS with Helm-managed PVC:

**Before you begin**

* Verify that the EBS or EFS StorageClass is configured in your Amazon EKS cluster.
* Confirm that Helm 3.0 or later and kubectl are installed.
* Ensure that the PDC namespace and Helm deployment are accessible.
* Verify that the `custom-values.yaml` file used for the PDC Helm deployment is available.
* Ensure that the EBS volume or EFS mount target is accessible from the cluster nodes.

**Procedure**

1. Open the `custom-values.yaml` file used for your PDC Helm deployment.
2. Add or update the following backup configuration block:

   ```
   # values.yaml
   backup:
     storage:
       requiresTempStorage: false
       tmpStorage:
         sizeLimit: 2Gi
     persistence:
       enabled: true
       existingClaim: ""
       storageClass: "ebs/efs-sc"  # Available StorageClass; if not defined, default will be used
       volumeName: "s3-pv"
   ```

   In this case, if the customer wants the PVC to be created by Helmfile, the `storageClass` and `volumeName` must be pre-existing and specified in the configuration, as shown above.\
   The volumeName field is optional and can be left empty if you want Helm to automatically assign one.
3. Save the configuration file.
4. Apply the configuration to the Amazon EKS cluster.

   ```
   helmfile -n <PDC_NAMESPACE> sync
   ```

   or

   ```
   helm upgrade --install pdc ./pdc-chart -n <PDC_NAMESPACE>
   ```
5. Verify that the backup CronJob is created successfully.

   ```
   kubectl get cronjobs -n <PDC_NAMESPACE>
   ```
6. Review the CronJob details to confirm that the schedule, StorageClass, and volume configuration are correctly referenced.

   ```
   kubectl describe cronjob pdc-backup -n <PDC_NAMESPACE>
   ```
7. Verify that the Helm deployment automatically created the backup PVC.

   ```
   kubectl get pvc -n <PDC_NAMESPACE> | grep backup
   ```

**Example: EBS or EFS StorageClass and PersistentVolume**

```
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: ebs-sc
provisioner: ebs.csi.aws.com
parameters:
  type: gp3
  fsType: ext4
---
apiVersion: v1
kind: PersistentVolume
metadata:
  name: pdc-backup-pv
spec:
  capacity:
    storage: 100Gi
  accessModes:
    - ReadWriteOnce
  storageClassName: ebs-sc
  csi:
    driver: ebs.csi.aws.com
    volumeHandle: <EBS_VOLUME_ID>
```

{% hint style="info" %}
Replace ebs-sc with your EFS StorageClass if you are using Amazon EFS (efs.csi.aws.com).\
The volumeName in the backup configuration can be left blank if Helm should generate it automatically.
{% endhint %}

**Result**

The PDC backup configuration is updated to use Amazon EBS or Amazon EFS with a Helm-managed PVC. When the backup CronJob runs, it automatically mounts the newly created PVC and stores backup data on the corresponding EBS or EFS volume.

### **Configure backup targets**

In Data Catalog deployments running on Amazon EKS, administrators can control which PDC components are included in each backup. Backup targets represent the core services and configuration objects that store catalog metadata, application settings, and operational data.

Each backup target corresponds to a specific PDC service or metadata store. You can include or exclude services as needed and optionally define individual Kubernetes objects.

<table><thead><tr><th width="148">Target</th><th>Description</th></tr></thead><tbody><tr><td><strong>PostgreSQL</strong></td><td>Stores configuration and metadata for user management, settings, and workflows.</td></tr><tr><td><strong>MongoDB</strong></td><td>Stores data asset, profiling, and relationship metadata collected from source systems.</td></tr><tr><td><strong>OpenSearch</strong></td><td>Stores indexed metadata used for catalog search, glossary, and lineage visualization.</td></tr><tr><td><strong>FE-Workers</strong></td><td>Stores dictionaries, patterns, and system-defined data used for data profiling and discovery.</td></tr><tr><td><strong>Objects</strong></td><td>Stores Kubernetes objects such as Secrets and ConfigMaps used by PDC services. You can define these objects by specifying the <code>kind</code> (for example, <code>secret</code>, <code>configmap</code>) and <code>name</code> (for example, <code>cat-key</code>).</td></tr></tbody></table>

You can define these backup targets in the Helm configuration to enable or disable backups for specific components at deployment time. This flexibility allows administrators to back up only the required services, exclude external databases, or include custom Kubernetes objects that need to be preserved during recovery.

Perform the following steps to configure backup targets:

**Before you begin**

* Verify that you have access to the PDC Helm deployment and the `custom-values.yaml` file.
* Confirm that Helm 3.0 or later and kubectl are installed on the administrator workstation.
* Ensure that the backup configuration for your selected storage type (Amazon S3, EBS, or EFS) is already defined.
* Identify which components and objects you want to include in the backup.

**Procedure**

1. Open the `custom-values.yaml` file for your PDC deployment in a text editor.
2. Locate the backup configuration block under the pdc-backup section.
3. Define the backup targets by setting the enabled parameter to true or false for each service:

   ```
   pdc-backup:
     backup:
       targets:
         opensearch:
           enabled: true
         mongodb:
           enabled: true
         postgres:
           enabled: true
         fe-workers:
           enabled: false
         objects:
           enabled: true
           object:
             - kind: secret
               name: cat-key
   ```

   **Note:**

   * You can list multiple Kubernetes objects under the object section. Common examples include:
     * `kind: secret`, `name: cat-key`
     * `kind: configmap`, `name: pdc-settings`
     * `kind: secret`, `name: pdc-license`
     * `kind: configmap`, `name: jobserver-config`
   * Enable `FE-Workers` and `Objects` backup only if these components or resources are part of your recovery plan. For external databases such as Amazon Aurora PostgreSQL, set `postgres.enabled` to `false` and manage backups externally.
4. Save the configuration file.
5. Apply the configuration to the Amazon EKS cluster.

   ```
   helmfile -n <PDC_NAMESPACE> sync
   ```

   or

   ```
   helm upgrade --install pdc ./pdc-chart -n <PDC_NAMESPACE>
   ```
6. Verify that the backup CronJob includes the selected targets.

   ```
   kubectl describe cronjob pdc-backup -n <PDC_NAMESPACE>
   ```

   The job definition lists only the enabled components and specified objects as backup targets.

**Result**

Backup targets are configured successfully. When the backup CronJob runs, it includes only the enabled components and any defined Kubernetes objects, and stores their backups in the configured storage location.

## **Run a backup in Amazon EKS**

In Data Catalog deployments running on Amazon EKS, administrators can perform both automated and manual backups of key Data Catalog components. Each backup captures data and configuration from PostgreSQL, MongoDB, OpenSearch, FE-Workers, and related Kubernetes objects.

After you apply the backup configuration, a CronJob is automatically created in the Amazon EKS cluster. The CronJob runs daily at midnight by default. You can also trigger a manual backup at any time, for example, before performing an upgrade or configuration change.

{% hint style="info" %}
If your deployment uses an external PostgreSQL database such as Amazon Aurora, Data Catalog doesn’t back up that database. Set the `postgres.enabled` parameter to false in the `custom-values.yaml` configuration file.
{% endhint %}

Perform the following steps to run a backup in Amazon EKS:

**Before you begin**

Before you run a backup, make sure the following requirements are met:

* The Data Catalog backup CronJob is configured in the Amazon EKS cluster.
* kubectl and Helm are installed and configured to access the cluster.
* You have administrator access to the PDC namespace.
* The configured storage backend, Amazon S3 storage, Amazon EBS volumes, or Amazon EFS file systems, is accessible from the cluster.

**Procedure**

1. Verify that the backup CronJob exists in the PDC namespace.

   ```
   kubectl get cronjobs -n <PDC_NAMESPACE>
   ```

   The CronJob named `pdc-backup` should be listed.
2. Check the CronJob schedule.

   ```
   kubectl describe cronjob pdc-backup -n <PDC_NAMESPACE> | grep "Schedule"
   ```

   The default schedule is `0 0 * * *`, which runs daily at midnight.
3. Trigger a manual backup when needed.

   ```
   kubectl create job --from=cronjob/pdc-backup pdc-backup-manual-$(date +%Y%m%d-%H%M%S) -n <PDC_NAMESPACE>
   ```
4. View all backup jobs in the PDC namespace.

   ```
   kubectl get jobs -n <PDC_NAMESPACE>
   ```
5. View backup logs for each component.

   ```
   kubectl logs -l job-name=pdc-backup-manual-<timestamp> -n <PDC_NAMESPACE> -c postgres-backup
   kubectl logs -l job-name=pdc-backup-manual-<timestamp> -n <PDC_NAMESPACE> -c mongodb-backup
   kubectl logs -l job-name=pdc-backup-manual-<timestamp> -n <PDC_NAMESPACE> -c opensearch-backup
   kubectl logs -l job-name=pdc-backup-manual-<timestamp> -n <PDC_NAMESPACE> -c fe-workers-backup
   kubectl logs -l job-name=pdc-backup-manual-<timestamp> -n <PDC_NAMESPACE> -c objects-backup
   ```

   Each log confirms whether the backup completed successfully for that component.
6. Verify backup files in Amazon S3 storage.

   ```
   aws s3 ls s3://<BUCKET_NAME>/
   ```

   The command lists all backup folders organized by service and timestamp.
7. Create a temporary pod to verify backup files in Amazon EBS volumes or Amazon EFS file systems.\
   Save the following YAML as backup-checker.yaml:

   ```
   apiVersion: v1
   kind: Pod
   metadata:
     name: backup-checker
     namespace: <PDC_NAMESPACE>
   spec:
     restartPolicy: Never
     containers:
       - name: backup-checker
         image: $<customer-artifactory>/cat-toolbox:debian-12
         command: ["sleep", "3600"]
         volumeMounts:
           - name: backup-pvc
             mountPath: /backups
     volumes:
       - name: backup-pvc
         persistentVolumeClaim:
           claimName: backup-pvc
   ```

   Replace `$<customer-artifactory>` with the actual artifactory path, like ECR or any private artifactory.
8. Apply the pod specification.

   ```
   kubectl apply -f backup-checker.yaml
   ```
9. List backup files inside the pod.

   ```
   kubectl exec -it backup-checker -n <PDC_NAMESPACE> -- ls -lrt /backups/
   ```

   The command lists all backup folders by component and timestamp.
10. Delete the temporary pod after verification.

    ```
    kubectl delete pod backup-checker -n <PDC_NAMESPACE>
    ```

**Result**

The backup job completes successfully and stores the data in the configured Amazon S3 bucket or Amazon EBS or Amazon EFS persistent volume. The CronJob continues to run automatically according to the defined schedule. Container logs confirm that all components were backed up successfully.

## **Verify backups in Amazon EKS**

In Data Catalog deployments running on Amazon EKS, administrators can verify that backup jobs are running successfully and that backup files are stored correctly in the configured storage backend.\
Verifying backups ensures that the scheduled or manual backup operations complete without errors and that data for all Data Catalog components is available for recovery when needed.

Data Catalog supports multiple storage options for backup data. The verification steps differ depending on the storage backend used in your deployment:

* **Amazon S3 storage:** Backups are written to an S3 bucket, and verification is performed by inspecting the bucket contents and checking job logs. For more information, see [#verify-backups-in-amazon-s3-storage](#verify-backups-in-amazon-s3-storage "mention").
* **Amazon EBS volumes or Amazon EFS file systems:** Backups are written directly to a persistent volume claim (PVC) mounted in the EKS cluster, and verification involves inspecting files stored inside the PVC. For more information, see [#verify-backups-in-amazon-ebs-volumes-or-amazon-efs-file-systems](#verify-backups-in-amazon-ebs-volumes-or-amazon-efs-file-systems "mention").

### **Verify backups in Amazon S3 storage**

In Data Catalog deployments running on Amazon EKS with Amazon S3 as the backup storage, administrators can verify that backups are successfully created and stored in the configured S3 bucket. Verification ensures that the pdc-backup CronJob is running correctly, that each backup job completes successfully, and that the backup data for all Data Catalog components is available in S3.

Perform the following steps to verify the backups in Amazon S3 storage:

**Before you begin**

Make sure the following requirements are met:

* Data Catalog backups are configured to use Amazon S3 in the Helm configuration file.
* kubectl and AWS CLI are installed and configured.
* The AWS credentials or IAM role attached to the Amazon EKS worker nodes provide access to the Amazon S3 bucket.
* You have the Amazon S3 bucket name used for storing Data Catalog backups.
* You have administrator access to the PDC namespace in the Amazon EKS cluster.

**Procedure**

1. Check that the backup CronJob exists in the PDC namespace.

   ```
   kubectl get cronjobs -n <PDC_NAMESPACE>
   ```

   The pdc-backup CronJob should appear in the list.
2. Verify that the most recent backup job completed successfully.

   ```
   kubectl get jobs -n <PDC_NAMESPACE>
   ```

   The **Completed** status indicates that the backup job finished without errors.
3. Check the logs of each backup container to confirm completion.

   ```
   kubectl logs -l job-name=pdc-backup-manual-<timestamp> -n <PDC_NAMESPACE> -c postgres-backup
   kubectl logs -l job-name=pdc-backup-manual-<timestamp> -n <PDC_NAMESPACE> -c mongodb-backup
   kubectl logs -l job-name=pdc-backup-manual-<timestamp> -n <PDC_NAMESPACE> -c opensearch-backup
   kubectl logs -l job-name=pdc-backup-manual-<timestamp> -n <PDC_NAMESPACE> -c fe-workers-backup
   kubectl logs -l job-name=pdc-backup-manual-<timestamp> -n <PDC_NAMESPACE> -c objects-backup
   ```

   Each container log should display a “Backup completed successfully” message for its corresponding component.
4. Verify that new backup folders are created in the S3 bucket.

   ```
   aws s3 ls s3://<BUCKET_NAME>/
   ```

   The command lists backup folders grouped by component and timestamp.\
   Confirm that the latest timestamp corresponds to the last backup job run.
5. Drill down into a component folder to verify detailed backup files.

   ```
   aws s3 ls s3://<BUCKET_NAME>/postgres/
   aws s3 ls s3://<BUCKET_NAME>/mongodb/
   aws s3 ls s3://<BUCKET_NAME>/opensearch/
   aws s3 ls s3://<BUCKET_NAME>/fe-workers/
   aws s3 ls s3://<BUCKET_NAME>/objects/
   ```

   Each directory should contain files such as .pgdump, .tar.gz, or .yaml representing backed-up data.
6. Verify that backup timestamps in S3 align with the CronJob schedule.\
   For example, if the schedule is set to midnight (0 0 \* \* \*), confirm that new backup folders appear daily at approximately that time.
7. Optionally, download and inspect one backup file to confirm data integrity.

   ```
   aws s3 cp s3://<BUCKET_NAME>/postgres/<TIMESTAMP>/postgres_full_<TIMESTAMP>.pgdump .
   ls -lh postgres_full_<TIMESTAMP>.pgdump
   ```

   The file size and timestamp confirm that the dump file was generated during the latest backup run.

**Result**

The backups are verified successfully in Amazon S3 storage. Each Data Catalog component’s data is available in the S3 bucket, and the folder structure reflects the latest backup job timestamp.\
The CronJob and job logs confirm that all backup operations completed without errors.

### **Verify backups in Amazon EBS volumes or Amazon EFS file systems**

In Data Catalog deployments running on Amazon EKS, administrators can verify backups stored on Amazon EBS or Amazon EFS volumes. These backups are written directly to a persistent volume claim (PVC) mounted in the EKS cluster. Verification ensures that backup jobs run successfully, that backup files are created in the /backups directory of the PVC, and that each Data Catalog component is included in the backup.

Perform the following steps to verify backups in Amazon EBS volumes or Amazon EFS file systems:

**Before you begin**&#x20;

Make sure the following requirements are met:

* Backups are configured to use Amazon EBS or Amazon EFS in the Helm configuration file.
* The Data Catalog backup CronJob is running in the Amazon EKS cluster.
* kubectl is installed and configured to access the Amazon EKS cluster.
* You have administrator access to the PDC namespace.
* You have the PersistentVolumeClaim (PVC) name used for storing backups.

**Procedure**

1. Check that the `pdc-backup` CronJob exists in the PDC namespace.

   ```
   kubectl get cronjobs -n <PDC_NAMESPACE>
   ```

   The CronJob named `pdc-backup` should appear in the list.
2. Verify that the most recent backup job completed successfully.

   ```
   kubectl get jobs -n <PDC_NAMESPACE>
   ```

   The **Completed** status confirms that the backup job ran without errors.
3. Review the logs for each backup container to confirm successful completion.

   ```
   kubectl logs -l job-name=pdc-backup-manual-<timestamp> -n <PDC_NAMESPACE> -c postgres-backup
   kubectl logs -l job-name=pdc-backup-manual-<timestamp> -n <PDC_NAMESPACE> -c mongodb-backup
   kubectl logs -l job-name=pdc-backup-manual-<timestamp> -n <PDC_NAMESPACE> -c opensearch-backup
   kubectl logs -l job-name=pdc-backup-manual-<timestamp> -n <PDC_NAMESPACE> -c fe-workers-backup
   kubectl logs -l job-name=pdc-backup-manual-<timestamp> -n <PDC_NAMESPACE> -c objects-backup
   ```

   Each log should confirm that the backup completed successfully for that component.
4. Create a temporary verification pod to inspect backup files in the PVC.\
   Save the following YAML file as `backup-verifier.yaml`.

   ```
   apiVersion: v1
   kind: Pod
   metadata:
     name: backup-verifier
     namespace: <PDC_NAMESPACE>
   spec:
     restartPolicy: Never
     containers:
       - name: backup-verifier
         image: $<customer-artifactory>/cat-toolbox:debian-12
         command: ["sleep", "3600"]
         volumeMounts:
           - name: backup-pvc
             mountPath: /backups
     volumes:
       - name: backup-pvc
         persistentVolumeClaim:
           claimName: backup-pvc
   ```

   Replace `$<customer-artifactory>` with the actual artifactory path, like ECR or any private artifactory.
5. Apply the pod specification to the EKS cluster.

   ```
   kubectl apply -f backup-verifier.yaml
   ```
6. Connect to the verification pod.

   ```
   kubectl exec -it backup-verifier -n <PDC_NAMESPACE> -- bash
   ```
7. List the backup folders stored in the mounted PVC.

   ```
   ls -lrt /backups/
   ```

   Backup directories should be organized by timestamp and contain subfolders for PostgreSQL, MongoDB, OpenSearch, FE-Workers, and Kubernetes objects.
8. Verify that backup folders are updated according to the CronJob schedule.\
   Confirm that a new folder exists for each backup cycle (for example, daily if the schedule is `0 0 * * *`).
9. Exit the pod session after verification.

   ```
   exit
   ```
10. Delete the temporary verification pod.

    ```
    kubectl delete pod backup-verifier -n <PDC_NAMESPACE>
    ```

**Result**

The backup files are verified successfully in the Amazon EBS volumes or Amazon EFS file systems persistent volume. Backup folders for each Data Catalog component are available under the /backups directory, organized by timestamp. The job status and logs confirm that the backup CronJob is running successfully in the EKS cluster.

## **Verify retention in Amazon EKS**

In Data Catalog deployments running on Amazon EKS, administrators can verify that backup retention policies are working correctly. Retention ensures that older backups are automatically deleted or archived based on the configured duration, preventing unnecessary storage consumption and maintaining compliance with data governance requirements.

Retention behavior depends on the type of storage used for backups:

* **Amazon EBS volumes or Amazon EFS file systems:** Retention is managed through the Data Catalog configuration parameters defined in the `custom-values.yaml` file. The `backup.retention.days` setting specifies how long backups are retained before being automatically deleted.&#x20;
* **Amazon S3:** Retention is managed externally through AWS S3 lifecycle policies, which automatically delete or transition older backups according to the lifecycle rules defined in the bucket.

## **Restore data from backup in Amazon EKS**

In Data Catalog deployments running on Amazon EKS, administrators can restore data and configurations from previously created backups. Restoring data helps recover Data Catalog components after system failures, data corruption, or configuration issues.\
PDC supports restoration from two storage types:

* [Amazon S3](#restore-from-amazon-s3-storage), where backups are stored in S3 buckets.
* [Amazon EBS or Amazon EFS](#restore-from-amazon-ebs-volumes-or-amazon-efs-file-systems), where backups are stored in persistent volume claims (PVCs) inside the EKS cluster.

Each Data Catalog component, PostgreSQL, MongoDB, OpenSearch, FE-Workers, and Kubernetes objects, has its own restore procedure. Administrators can restore individual services or the complete Data Catalog environment, depending on the recovery requirement.

{% hint style="warning" %}
Before performing any restore procedure, stop all active Data Catalog processes that connect to the target databases or services to prevent conflicts.
{% endhint %}

### **Restore from Amazon S3 storage**

When backups are stored in Amazon S3, each Data Catalog component must be restored separately from the data in the Amazon S3 bucket. The following guides describe how to download backup files, connect to service pods, and restore data for each component.

* [#restore-postgresql-data-from-amazon-s3](#restore-postgresql-data-from-amazon-s3 "mention")\
  Learn how to drop existing PostgreSQL databases, restore data using `.pgdump` files, and verify database creation.
* [#restore-mongodb-data-from-amazon-s3](#restore-mongodb-data-from-amazon-s3 "mention")\
  Learn how to unpack MongoDB backup files, run mongorestore, and confirm successful restoration.
* [#restore-opensearch-data-from-amazon-s3](#restore-opensearch-data-from-amazon-s3 "mention")\
  Learn how to use the OpenSearch restore script to restore indexes and restart services.
* [#restore-fe-workers-data-from-amazon-s3](#restore-fe-workers-data-from-amazon-s3 "mention")\
  Learn how to extract and copy FE-Worker backup files, including dictionaries and patterns, to the appropriate directories.
* [#restore-kubernetes-objects-from-amazon-s3](#restore-kubernetes-objects-from-amazon-s3 "mention")\
  Learn how to restore Kubernetes secrets and configuration files using YAML manifests stored in the S3 bucket.

#### **Restore PostgreSQL data from Amazon S3**

In Data Catalog deployments running on Amazon EKS, administrators can restore PostgreSQL data from backups stored in Amazon S3. PostgreSQL stores configuration and metadata for Data Catalog, so restoring it is a critical step in recovering the environment after data loss or system failure.

Before restoring PostgreSQL data, stop all Data Catalog services that connect to the database to avoid conflicts during restoration.

Perform the following steps to restore PostgreSQL data from Amazon S3 storage:

**Before you begin**

Make sure the following requirements are met:

* The PostgreSQL backup is available in the Amazon S3 bucket.
* AWS CLI and kubectl are installed and configured to access the Amazon EKS cluster.
* You have the following information:
  * The Amazon S3 bucket name and the timestamp of the backup you want to restore.
  * The PostgreSQL pod name and PDC namespace.
  * The PostgreSQL username and password.
* The PostgreSQL pod is in a **Running** state.

  ```
  kubectl get pods -n <PDC_NAMESPACE> | grep postgres
  ```

**Procedure**

1. Download the PostgreSQL backup files from the S3 bucket.

   ```
   aws s3 cp s3://<BUCKET_NAME>/postgres/<TIMESTAMP>/ <LOCAL_PATH>/<TIMESTAMP>/
   ```
2. Drop existing databases in PostgreSQL.

   ```
   kubectl exec -i <POSTGRES_POD> -n <PDC_NAMESPACE> -- env PGPASSWORD="<POSTGRES_PASSWORD>" bash -c '
   DBS=$(psql -U "<POSTGRES_USER>" -h postgresql -p 5432 -d postgres -t -A -c "SELECT datname FROM pg_database WHERE datallowconn AND datname NOT IN ('\''postgres'\'','\''template0'\'','\''template1'\'');")
   for db in $DBS; do
       echo "Terminating connections for: $db"
       psql -U "postgres" -h postgresql -p 5432 -d postgres -c "SELECT pg_terminate_backend(pid) FROM pg_stat_activity WHERE datname = '\''$db'\'';"
       echo "Dropping database: $db"
       psql -U "<POSTGRES_USER>" -h postgresql -p 5432 -d postgres -c "DROP DATABASE IF EXISTS \"$db\";"
   done'
   ```
3. Restore the PostgreSQL database from the downloaded dump file.

   ```
   kubectl exec -i <POSTGRES_POD> -n <PDC_NAMESPACE> -- bash -c "PGPASSWORD=<POSTGRES_PASSWORD> psql -U postgres" < <LOCAL_PATH>/<TIMESTAMP>/postgres_full_<TIMESTAMP>.pgdump
   ```
4. Verify the restore by listing all databases.

   ```
   kubectl exec -it <POSTGRES_POD> -n <PDC_NAMESPACE> -- psql -U postgres -c "\l"
   ```

**Result**

The PostgreSQL data is restored successfully from the backup stored in Amazon S3 storage. After the PostgreSQL service restarts, all related Data Catalog databases are available and ready for use.

#### **Restore MongoDB Data from Amazon S3**

In Data Catalog deployments running on Amazon EKS, administrators can restore MongoDB data from backups stored in Amazon S3. MongoDB stores operational and user metadata for Data Catalog, so restoring it is an essential step in recovering a functional catalog environment.

{% hint style="warning" %}
Before restoring MongoDB data, stop all Data Catalog services that connect to the database to avoid conflicts during restoration.
{% endhint %}

Perform the following steps to restore MongoDB data from Amazon S3 storage:

**Before you begin**

Make sure the following requirements are met:

* The MongoDB backup files are available in the Amazon S3 bucket.
* AWS CLI and kubectl are installed and configured to access the Amazon EKS cluster.
* You have the following information:
  * The Amazon S3 bucket name and timestamp of the backup you want to restore.
  * The MongoDB pod name and PDC namespace.
  * The MongoDB username and password.
* The MongoDB pod is in the **Running** state.

  `kubectl get pods -n <PDC_NAMESPACE> | grep mongo`

**Procedure**

1. Download the MongoDB backup files from the S3 bucket.

   ```
   aws s3 cp s3://<BUCKET_NAME>/mongodb/<TIMESTAMP>/ <LOCAL_PATH>/<TIMESTAMP>/ --recursive
   ```
2. Restore the MongoDB data to the cluster.

   ```
   tar -C <LOCAL_PATH>/<TIMESTAMP> -cf - . | \
   kubectl exec -i <MONGO_POD> -n <PDC_NAMESPACE> -- bash -c "
   rm -rf /tmp/mongorestore && mkdir -p /tmp/mongorestore && \
   tar -C /tmp/mongorestore -xf - && \
   mongorestore --host mongodb --username <MONGO_USER> --password '<MONGO_PASS>' --authenticationDatabase admin --drop /tmp/mongorestore"
   ```
3. Verify the restore by listing databases.

   ```
   kubectl exec -it <MONGO_POD> -n <PDC_NAMESPACE> -- mongo --authenticationDatabase admin -u <MONGO_USER> -p <MONGO_PASS> --eval "show dbs"
   ```
4. After restoring from the existing backup, it is necessary to restart the licensing-api deployment for the data to take effect.

   ```
   kubectl rollout restart deployment cat-licensing-api -n <PDC_NAMESPACE>
   ```

**Result**

The MongoDB data is restored successfully from the backup stored in Amazon S3. All operational and user metadata for PDC is available once the MongoDB service restarts and reconnects to the application.

***

#### **Restore OpenSearch data from Amazon S3**

In Data Catalog deployments running on Amazon EKS, administrators can restore OpenSearch data from backups stored in Amazon S3. OpenSearch stores indexed metadata used for search and discovery in PDC. Restoring OpenSearch ensures that catalog search results, entity references, and metadata associations are available after a recovery or redeployment.

{% hint style="warning" %}
Before performing the restore, stop any PDC services that query OpenSearch to prevent indexing conflicts.
{% endhint %}

Perform the following steps to import the data from Amazon S3 storage into the OpenSearch service running in the Amazon EKS cluster:

Before you restore, make sure `curl` and `jq` are installed.

**Procedure**

1. Download the OpenSearch backup files from the S3 bucket.

   ```
   aws s3 cp s3://<BUCKET_NAME>/opensearch/<TIMESTAMP>/ <LOCAL_PATH>/<TIMESTAMP>/ --recursive
   ```
2. Create an opensearch\_restore.sh file with the below content.\
   Replace variables, `<LOCAL_PATH>/<TIMESTAMP>` and `<PDC_NAMESPACE>`)

   ```
   #!/bin/bash
   BACKUP_DIR="$<LOCAL_PATH>/<TIMESTAMP>"
   NAMESPACE="$<PDC_NAMESPACE>"
   echo "=== OpenSearch Restore ==="
   echo
   # Check tools
   for tool in kubectl curl jq; do
       if ! command -v $tool &> /dev/null; then
           echo "ERROR: Required tool not found: $tool"
           exit 1
       fi
   done
   # Check backup files
   if [ ! -d "$BACKUP_DIR" ] || [ -z "$(find "$BACKUP_DIR" -name "*_info.json" -type f)" ]; then
       echo "ERROR: No backup files found in $BACKUP_DIR"
       exit 1
   fi
   # Start port-forwarding in background
   echo "Starting port-forwarding..."
   kubectl port-forward -n $NAMESPACE svc/opensearch 9200:9200 > /tmp/port-forward.log 2>&1 &
   PF_PID=$!
   echo "Port-forward PID: $PF_PID"
   sleep 8
   # Set connection details
   HOST="localhost"
   PORT="9200"
   # Check connection
   echo "Testing OpenSearch connection..."
   if ! curl -s "http://$HOST:$PORT/_cluster/health" > /dev/null; then
       echo "ERROR: Cannot connect to OpenSearch"
       kill $PF_PID 2>/dev/null
       exit 1
   fi
   echo "✓ Connected to OpenSearch"
   # Safety check
   echo "Checking existing indexes..."
   existing=$(curl -s "http://$HOST:$PORT/_cat/indices/pdc_*?h=index" | tr '\n' ' ')
   if [ -n "$existing" ]; then
       echo "WARNING: These indexes will be DELETED:"
       for idx in $existing; do
           count=$(curl -s "http://$HOST:$PORT/$idx/_count" | jq -r '.count')
           echo "  - $idx ($count docs)"
       done
       read -p "Continue? (type 'yes'): " confirm
       [ "$confirm" != "yes" ] && { kill $PF_PID; exit 0; }
       echo
   fi
   # Get timestamp from first backup file
   first_info_file=$(find "$BACKUP_DIR" -name "*_info.json" | head -1)
   timestamp=$(grep "backup_timestamp" "$first_info_file" | cut -d':' -f2 | tr -d ' "')
   echo "Restoring from backup: $timestamp"
   echo
   success=0
   fail=0
   # Function for fast parallel bulk processing
   process_bulk_fast() {
       local data_file="$1"
       local index="$2"
       local chunk_size=5000  # Larger chunks - 5000 documents
       local parallel_jobs=5  # Process 4 chunks in parallel
       echo "  Processing $chunk_size documents per chunk with $parallel_jobs parallel jobs..."
       total_lines=$(wc -l < "$data_file")
       total_docs=$((total_lines / 2))
       total_chunks=$(( (total_docs + chunk_size - 1) / chunk_size ))
       echo "  Total: $total_docs documents in $total_chunks chunks"
       # Create all chunks first
       echo "  Preparing chunks..."
       for ((chunk=1; chunk<=total_chunks; chunk++)); do
           start_line=$(( (chunk - 1) * chunk_size * 2 + 1 ))
           end_line=$(( chunk * chunk_size * 2 ))
           sed -n "${start_line},${end_line}p" "$data_file" > "/tmp/bulk_chunk_${chunk}.ndjson"
       done
       # Process chunks in parallel
       echo "  Starting parallel processing..."
       (
           for ((chunk=1; chunk<=total_chunks; chunk++)); do
               ((i=i%parallel_jobs)); ((i++==0)) && wait
               (
                   chunk_file="/tmp/bulk_chunk_${chunk}.ndjson"
                   if [ -s "$chunk_file" ]; then
                       lines_in_chunk=$(wc -l < "$chunk_file")
                       docs_in_chunk=$((lines_in_chunk / 2))
                       # Send bulk request with timeout
                       response=$(curl -s --max-time 60 -X POST "http://$HOST:$PORT/_bulk" \
                           -H 'Content-Type: application/x-ndjson' \
                           --data-binary @"$chunk_file")
                       if echo "$response" | jq -e '.errors == false' > /dev/null 2>&1; then
                           echo "    ✓ Chunk $chunk/$total_chunks ($docs_in_chunk docs)"
                       else
                           error_count=$(echo "$response" | jq -r '[.items[] | select(.index.error)] | length' 2>/dev/null || echo "?")
                           if [ "$error_count" = "0" ] 2>/dev/null; then
                               echo "    ✓ Chunk $chunk/$total_chunks ($docs_in_chunk docs)"
                           else
                               echo "    ⚠ Chunk $chunk/$total_chunks - $error_count errors"
                           fi
                       fi
                       # Clean up chunk file
                       rm -f "$chunk_file"
                   fi
               ) &
           done
           wait
       )
       echo "  Parallel processing completed"
   }
   # Function for very fast single-threaded processing (alternative)
   process_bulk_very_fast() {
       local data_file="$1"
       local index="$2"
       local chunk_size=10000  # Very large chunks - 10,000 documents
       echo "  Processing $chunk_size documents per chunk..."
       total_lines=$(wc -l < "$data_file")
       total_docs=$((total_lines / 2))
       total_chunks=$(( (total_docs + chunk_size - 1) / chunk_size ))
       echo "  Total: $total_docs documents in $total_chunks chunks"
       for ((chunk=1; chunk<=total_chunks; chunk++)); do
           start_line=$(( (chunk - 1) * chunk_size * 2 + 1 ))
           end_line=$(( chunk * chunk_size * 2 ))
           # Extract chunk
           sed -n "${start_line},${end_line}p" "$data_file" > /tmp/bulk_chunk.ndjson
           lines_in_chunk=$(wc -l < /tmp/bulk_chunk.ndjson)
           if [ $lines_in_chunk -eq 0 ]; then
               break
           fi
           docs_in_chunk=$((lines_in_chunk / 2))
           # Show progress every 10 chunks or for the first/last chunks
           if [ $((chunk % 10)) -eq 0 ] || [ $chunk -eq 1 ] || [ $chunk -eq $total_chunks ]; then
               echo "    Chunk $chunk/$total_chunks ($docs_in_chunk documents)..."
           fi
           # Send bulk request without waiting for detailed response
           curl -s -X POST "http://$HOST:$PORT/_bulk" \
               -H 'Content-Type: application/x-ndjson' \
               --data-binary @/tmp/bulk_chunk.ndjson > /dev/null
           # Show progress indicator
           if [ $((chunk % 50)) -eq 0 ]; then
               echo "    Progress: $chunk/$total_chunks chunks completed"
           fi
       done
       rm -f /tmp/bulk_chunk.ndjson
       echo "  Bulk data ingestion completed"
   }
   # Function for direct file processing (fastest)
   process_bulk_direct() {
       local data_file="$1"
       local index="$2"
       echo "  Direct bulk ingestion..."
       total_lines=$(wc -l < "$data_file")
       total_docs=$((total_lines / 2))
       echo "  Ingesting $total_docs documents directly..."
       # Send the entire file at once with longer timeout
       response=$(curl -s --max-time 300 -X POST "http://$HOST:$PORT/_bulk" \
           -H 'Content-Type: application/x-ndjson' \
           --data-binary @"$data_file")
       if echo "$response" | jq -e '.errors == false' > /dev/null 2>&1; then
           echo "  ✓ All $total_docs documents ingested successfully"
       else
           error_count=$(echo "$response" | jq -r '[.items[] | select(.index.error)] | length' 2>/dev/null || echo "?")
           if [ "$error_count" = "0" ] 2>/dev/null; then
               echo "  ✓ All $total_docs documents processed"
           else
               echo "  ⚠ Ingested with $error_count errors out of $total_docs documents"
           fi
       fi
   }
   # Restore each index
   for info_file in $(find "$BACKUP_DIR" -name "*_info.json"); do
       # Extract info from simple format
       index=$(grep "index_name" "$info_file" | cut -d':' -f2 | tr -d ' ')
       ts=$(grep "backup_timestamp" "$info_file" | cut -d':' -f2 | tr -d ' "')
       settings="$BACKUP_DIR/${index}_${ts}_settings.json"
       mapping="$BACKUP_DIR/${index}_${ts}_mapping.json"
       data="$BACKUP_DIR/${index}_${ts}_data.bulk"
       echo "Restoring: $index"
       # Check if backup files exist
       if [[ ! -f "$settings" || ! -f "$mapping" ]]; then
           echo "  ✗ Missing backup files for $index"
           ((fail++))
           continue
       fi
       # Delete if exists
       echo "  Deleting existing index..."
       curl -s -X DELETE "http://$HOST:$PORT/$index" > /dev/null
       sleep 2
       # Create index
       echo "  Creating index..."
       # Extract settings
       if jq -e '.[]' "$settings" > /dev/null 2>&1; then
           jq '.[] | .settings.index | del(.creation_date, .uuid, .version, .provided_name)' "$settings" > /tmp/settings.json 2>/dev/null
       elif jq -e '.settings' "$settings" > /dev/null 2>&1; then
           jq '.settings.index | del(.creation_date, .uuid, .version, .provided_name)' "$settings" > /tmp/settings.json 2>/dev/null
       else
           jq '.index | del(.creation_date, .uuid, .version, .provided_name)' "$settings" > /tmp/settings.json 2>/dev/null
       fi
       # Use defaults if settings extraction failed
       if [ ! -s /tmp/settings.json ] || ! jq -e '.' /tmp/settings.json > /dev/null 2>&1; then
           echo '{"number_of_shards": 1, "number_of_replicas": 1}' > /tmp/settings.json
       fi
       # Extract mappings
       if jq -e '.mappings' "$mapping" > /dev/null 2>&1; then
           jq '.mappings' "$mapping" > /tmp/mappings.json
       elif jq -e '.[]' "$mapping" > /dev/null 2>&1; then
           jq '.[] | .mappings' "$mapping" > /tmp/mappings.json
       else
           jq '.' "$mapping" > /tmp/mappings.json
       fi
       # Create the final payload
       jq -n --argjson settings "$(cat /tmp/settings.json)" --argjson mappings "$(cat /tmp/mappings.json)" '{
           settings: {index: $settings},
           mappings: $mappings
       }' > /tmp/payload.json
       # Create the index
       response=$(curl -s -X PUT "http://$HOST:$PORT/$index" -H 'Content-Type: application/json' -d @/tmp/payload.json)
       if echo "$response" | jq -e '.acknowledged == true' > /dev/null; then
           echo "  ✓ Index created"
           # Restore data - try different methods based on file size
           if [ -f "$data" ] && [ -s "$data" ]; then
               lines=$(wc -l < "$data")
               expected_docs=$((lines/2))
               echo "  ↳ Restoring $expected_docs documents..."
               # Choose method based on file size
               if [ $expected_docs -le 50000 ]; then
                   # Small files - direct upload
                   process_bulk_direct "$data" "$index"
               elif [ $expected_docs -le 200000 ]; then
                   # Medium files - large chunks
                   process_bulk_very_fast "$data" "$index"
               else
                   # Large files - parallel processing
                   process_bulk_fast "$data" "$index"
               fi
               # Final refresh
               echo "  Refreshing index..."
               curl -s -X POST "http://$HOST:$PORT/$index/_refresh" > /dev/null
               # Quick verification
               count_response=$(curl -s "http://$HOST:$PORT/$index/_count")
               if echo "$count_response" | jq -e '.count' > /dev/null; then
                   actual_count=$(echo "$count_response" | jq -r '.count')
                   echo "  📊 Document count: $actual_count"
               fi
           else
               echo "  ⓘ No data to restore"
           fi
           ((success++))
       else
           echo "  ✗ Failed to create index"
           error_type=$(echo "$response" | jq -r '.error.type // "unknown_error"' 2>/dev/null)
           error_reason=$(echo "$response" | jq -r '.error.reason // "unknown reason"' 2>/dev/null)
           echo "  Error: $error_type - $error_reason"
           ((fail++))
       fi
       echo
   done
   # Restore aliases
   alias_file=$(find "$BACKUP_DIR" -name "aliases_*.json" | head -1)
   if [ -f "$alias_file" ]; then
       echo "Restoring aliases..."
       jq -r 'to_entries[] | select(.value.aliases) | .key as $idx | .value.aliases | keys[] | "\(.) \($idx)"' "$alias_file" | while read alias idx; do
           if curl -s -I "http://$HOST:$PORT/$idx" | grep -q "200 OK"; then
               curl -s -X POST "http://$HOST:$PORT/_aliases" -H 'Content-Type: application/json' -d "{\"actions\":[{\"add\":{\"index\":\"$idx\",\"alias\":\"$alias\"}}]}" > /dev/null
               echo "  ✓ Alias: $alias → $idx"
           fi
       done
       echo
   fi
   # Cleanup
   rm -f /tmp/settings.json /tmp/mappings.json /tmp/payload.json /tmp/bulk_chunk*.ndjson
   # Final verification
   echo "=== Final Verification ==="
   echo "Index status:"
   curl -s "http://$HOST:$PORT/_cat/indices/pdc_*?h=index,docs.count,store.size&s=index" | while read line; do
       if [ -n "$line" ]; then
           index=$(echo $line | awk '{print $1}')
           count=$(echo $line | awk '{print $2}')
           size=$(echo $line | awk '{print $3}')
           echo "  $index: $count documents, $size"
       fi
   done
   # Kill port-forward
   kill $PF_PID 2>/dev/null
   # Summary
   echo
   echo "=== Summary ==="
   echo "Successful: $success"
   echo "Failed: $fail"
   echo "Total: $((success + fail))"
   if [ $fail -eq 0 ]; then
       echo "✓ Restore completed successfully!"
   else
       echo "⚠ Restore completed with errors"
   fi
   ```
3. Give executable permission to `opensearch_restore.sh` file.

   ```
   chmod +x opensearch_restore.sh
   ```
4. Execute the following script.

   ```
   ./opensearch_restore.sh
   ```
5. Verify that all indexes are restored.

   ```
   curl -s "http://opensearch:9200/_cat/indices/pdc_*?h=index"
   ```
6. Restart the OpenSearch deployment to apply the restored data.

   ```
   kubectl rollout restart deployment opensearch -n <PDC_NAMESPACE>
   ```

**Result**

OpenSearch data is restored successfully from the backup stored in Amazon S3. All indexed metadata used for search and discovery in Data Catalog is available once the OpenSearch service restarts and completes indexing.

#### **Restore FE-Workers data from Amazon S3**

In Data Catalog deployments running on Amazon EKS, administrators can restore FE-Workers data from backups stored in Amazon S3 storage. The FE-Workers component stores system-defined data patterns, dictionaries, and processed datasets that are essential for profiling and data analysis within Data Catalog. Restoring FE-Workers ensures that these reference files are recovered and available for downstream data discovery and governance tasks.

{% hint style="warning" %}
Stop any active Data Catalog jobs or services that access FE-Workers data before performing the restore to prevent file-level conflicts.
{% endhint %}

Perform the following steps to restore FE-Workers data from Amazon S3 storage:

**Before you begin**

Make sure the following requirements are met:

* The FE-Workers backup files are available in the Amazon S3 bucket.
* AWS CLI and kubectl are installed and configured to access your Amazon EKS cluster.
* You have the Amazon S3 bucket name and the timestamp of the backup information.

**Procedure**

1. Download the FE-Workers backup files from the S3 bucket.

   ```
   aws s3 cp s3://<BUCKET_NAME>/fe-workers/<TIMESTAMP>/ <LOCAL_PATH>/<TIMESTAMP>/
   ```
2. Restore the FE-Workers data to the target pod.

   ```
   cat <LOCAL_PATH>/<TIMESTAMP>/fe-worker-backup-<TIMESTAMP>.tar.gz | \
   kubectl exec -i <FE_WORKER_POD> -n <PDC_NAMESPACE> -- bash -c '
   mkdir -p /tmp/fe-worker-restore && \
   tar -xzvf - -C /tmp/fe-worker-restore && \
   cp -a /tmp/fe-worker-restore/data/* /home/node/data/ && \
   cp -a /tmp/fe-worker-restore/patterns-systemdefined /home/node/data/ && \
   cp -a /tmp/fe-worker-restore/dictionaries-* /home/node/data/ && \
   rm -rf /tmp/fe-worker-restore'
   ```
3. Verify that files are extracted successfully.

   ```
   kubectl exec -it <FE_WORKER_POD> -n <PDC_NAMESPACE> -- ls -la /home/node/data/
   ```

**Result**

FE-Workers data is restored successfully from the backup stored in Amazon S3. All dictionaries, system-defined patterns, and processed datasets are available in the FE-Workers container and ready for use by the PDC application.

#### **Restore Kubernetes objects from Amazon S3**

In Data Catalog deployments running on Amazon EKS, administrators can restore Kubernetes objects such as Secrets and ConfigMaps from backups stored in Amazon S3. These objects contain configuration data and credentials required for Data Catalog components to operate correctly. Restoring Kubernetes objects ensures that secure keys, connection information, and application configuration are recovered after a cluster rebuild or configuration loss.

{% hint style="info" %}
Ensure that the target PDC namespace exists before restoring Kubernetes objects. Restoring Secrets or ConfigMaps with the same name will overwrite existing resources in the namespace.
{% endhint %}

Perform the following steps to restore Kubernetes objects from Amazon S3:

**Before you begin**

Make sure the following requirements are met:

* The Kubernetes object backup files are available in the Amazon S3 bucket.
* AWS CLI and kubectl are installed and configured to access your Amazon EKS cluster.
* You have the following information:
  * The Amazon S3 bucket name and timestamp of the backup.
  * The PDC namespace where the secrets must be restored.
* You have cluster administrator privileges in the Amazon EKS cluster.

**Procedure**

1. Download the object backup files from the Amazon S3 bucket.

   ```
   aws s3 cp s3://<BUCKET_NAME>/objects/<TIMESTAMP>/ <LOCAL_PATH>/<TIMESTAMP>/ --recursive
   ```
2. Restore the Kubernetes objects from the downloaded YAML files.

   ```
   kubectl apply -f <LOCAL_PATH>/<TIMESTAMP>/secret_cat-key_<TIMESTAMP>.yaml -n <PDC_NAMESPACE>
   ```
3. Verify the restored Kubernetes secrets.

   ```
   kubectl get secrets -n <PDC_NAMESPACE>
   ```

**Result**

Kubernetes objects are restored successfully from the backup stored in Amazon S3. All restored objects are re-applied to the specified PDC namespace, ensuring that the required credentials and configuration settings are available for Data Catalog services.

### **Restore from Amazon EBS volumes or Amazon EFS file systems**

In Data Catalog deployments running on Amazon EKS, administrators can restore backup data stored in Amazon EBS or Amazon EFS volumes. When Data Catalog backups are configured to use persistent storage, all backup files are stored in a PersistentVolumeClaim (PVC) that remains available within the EKS cluster.&#x20;

{% hint style="info" %}
Each Data Catalog component can be restored individually by creating a temporary restore pod that mounts the same PVC used during the backup process.
{% endhint %}

Restoration from EBS or EFS storage allows administrators to recover component data such as PostgreSQL databases, MongoDB collections, OpenSearch indexes, FE-Workers data, and Kubernetes objects directly from the cluster without downloading backup files externally.

{% hint style="info" %}
Use the same PVC that was used for the backup. Restoring data from an incorrect or outdated PVC may result in partial or inconsistent data recovery.
{% endhint %}

Each Data Catalog component has its own restore procedure that runs from within the EKS cluster.\
Select the appropriate guide based on the component you want to restore.

* [#restore-postgresql-data-from-amazon-ebs-volumes-or-amazon-efs-file-systems](#restore-postgresql-data-from-amazon-ebs-volumes-or-amazon-efs-file-systems "mention")\
  Restore PostgreSQL databases using the psql command from backup files available in the mounted PVC.
* [#restore-mongodb-data-from-amazon-ebs-volumes-or-amazon-efs-file-systems](#restore-mongodb-data-from-amazon-ebs-volumes-or-amazon-efs-file-systems "mention")\
  Restore MongoDB collections using the mongorestore utility from the backup data stored in the PVC.
* [#restore-opensearch-data-from-amazon-ebs-volumes-or-amazon-efs-file-systems](#restore-opensearch-data-from-amazon-ebs-volumes-or-amazon-efs-file-systems "mention")\
  Restore OpenSearch indexes, mappings, and aliases using the provided restore script executed within a temporary restore pod.
* [#restore-fe-workers-data-from-amazon-ebs-volumes-or-amazon-efs-file-systems](#restore-fe-workers-data-from-amazon-ebs-volumes-or-amazon-efs-file-systems "mention")\
  Restore FE-Workers dictionaries, patterns, and system-defined data by extracting archived backups into the FE-Workers PVC.
* [#restore-kubernetes-objects-from-amazon-ebs-volumes-or-amazon-efs-file-systems](#restore-kubernetes-objects-from-amazon-ebs-volumes-or-amazon-efs-file-systems "mention")\
  Restore Kubernetes Secrets and ConfigMaps by applying YAML manifests backed up to the PVC.

#### **Restore PostgreSQL data from Amazon EBS volumes or Amazon EFS file systems**

In Data Catalog deployments running on Amazon EKS, administrators can restore PostgreSQL data from backups stored in Amazon EBS or Amazon EFS. When Data Catalog backups are configured to use persistent storage, backup data is written directly to a PersistentVolumeClaim (PVC) in the EKS cluster. You can restore PostgreSQL data by creating a temporary restore pod that mounts the same PVC and running PostgreSQL commands to import data from the backup files.

{% hint style="info" %}
Use the same PVC that was used during the backup process. Restoring from an incorrect or outdated volume may cause data inconsistency.
{% endhint %}

Perform the following steps to restore data from PostgreSQL:

**Before you begin**

Make sure the following requirements are met:

* The backup data exists in the /backups/postgres/ directory of the PVC used for Data Catalog backups.
* kubectl is installed and configured to access the Amazon EKS cluster.
* The PostgreSQL service is running in the same PDC namespace.
* You have identified the PVC name, PDC namespace, and PostgreSQL credentials.
* All active PDC services that connect to PostgreSQL are stopped before the restore process begins.

**Procedure**

1. Save the following pod configuration as `pg-restore.yaml`.

   ```
   apiVersion: v1
   kind: Pod
   metadata:
     name: pg-restore
     namespace: <PDC_NAMESPACE>
   spec:
     restartPolicy: Never
     containers:
     - name: pg-restore
       image: $<customer-artifactory>/pdm-postgres:release-v10.2.9.   # Use a version that matches your PDC deployment
       command: [ "sleep", "3600" ]
       volumeMounts:
       - name: backup-pvc
         mountPath: /backups
     volumes:
     - name: backup-pvc
       persistentVolumeClaim:
         claimName: backup-pvc
   ```

   Replace `$<customer-artifactory>` with the actual artifactory path, like ECR or any private artifactory.
2. Apply the pod specification in the EKS cluster.

   ```
   kubectl apply -f pg-restore.yaml
   ```
3. Verify that the restore pod is running in the specified namespace.

   ```
   kubectl get pods -n <PDC_NAMESPACE>
   ```
4. Access the restore pod.

   ```
   kubectl exec -it -n <PDC_NAMESPACE> pg-restore -c pg-restore -- bash
   ```
5. List the available backup files in the mounted directory.

   ```
   ls /backups/postgres/<TIMESTAMP>
   ```

   The directory should contain a file such as postgres\_full\_\<TIMESTAMP>.pgdump.
6. Set the PostgreSQL password as an environment variable.

   ```
   export PGPASSWORD="<POSTGRES_PASSWORD>"
   ```
7. Drop existing PostgreSQL databases to avoid conflicts during restoration.

   ```
   DBS=$(psql -U "postgres" -h postgresql -p 5432 -d postgres -t -A -c "SELECT datname FROM pg_database WHERE datallowconn AND datname NOT IN ('postgres','template0','template1');")
   for db in $DBS; do
       echo "Terminating connections for: $db"
       psql -U "postgres" -h postgresql -p 5432 -d postgres -c "SELECT pg_terminate_backend(pid) FROM pg_stat_activity WHERE datname = '$db';"
       echo "Dropping database: $db"
       psql -U "postgres" -h postgresql -p 5432 -d postgres -c "DROP DATABASE IF EXISTS \"$db\";"
   done
   ```
8. Restore the PostgreSQL database from the backup file.

   ```
   PGPASSWORD=$POSTGRES_PASSWORD psql \
     -h postgresql -p 5432 -U postgres \
     -f /backups/postgres/<TIMESTAMP>/postgres_full_<TIMESTAMP>.pgdump
   ```
9. Verify that the databases are restored successfully.

   ```
   PGPASSWORD=$POSTGRES_PASSWORD psql -h postgresql -p 5432 -U postgres -c "\l"
   ```

   The restored databases should appear in the list.
10. Exit the restore pod.

    ```
    exit
    ```
11. Delete the temporary restore pod after the restore process is complete.

    ```
    kubectl delete pod pg-restore -n <PDC_NAMESPACE>
    ```

**Result**

PostgreSQL data is restored successfully from the Amazon EBS or Amazon EFS storage used for Data Catalog backups. The restored databases are available and accessible once the PostgreSQL service restarts and reconnects with the PDC application.

#### **Restore MongoDB data from Amazon EBS volumes or Amazon EFS file systems**

In Data Catalog deployments running on Amazon EKS, administrators can restore MongoDB data from backups stored in Amazon EBS or Amazon EFS. When Data Catalog backups are configured to use persistent storage, backup data is stored in a PersistentVolumeClaim (PVC) in the EKS cluster.\
You can restore MongoDB data by creating a temporary restore pod that mounts the same PVC and importing the data using the mongorestore utility.

{% hint style="info" %}
Use the same PVC that was used for backups. Restoring from an incorrect PVC may result in incomplete or outdated data.
{% endhint %}

Perform the following steps to restore the MongoDB data from backups:

**Before you begin**

Make sure the following requirements are met:

* The backup files exist in the /backups/mongodb/ directory of the PersistentVolumeClaim (PVC) used for Data Catalog backups.
* kubectl is installed and configured to access your Amazon EKS cluster.
* The MongoDB service is running in the same PDC namespace.
* You have identified the PVC name, PDC namespace, and MongoDB credentials.
* All active PDC services that connect to MongoDB are stopped before restoring data.

**Procedure**

1. Save the following pod configuration as `mongo-restore.yaml`.

   ```
   apiVersion: v1
   kind: Pod
   metadata:
     name: mongo-restore
     namespace: <PDC_NAMESPACE>
   spec:
     restartPolicy: Never
     containers:
     - name: mongo-restore
       image: $<customer-artifactory>/mongodb/mongodb-enterprise-server:6.0.23-ubuntu2204   # Use a version matching your MongoDB cluster
       command: [ "sleep", "3600" ]
       volumeMounts:
       - name: backup-pvc
         mountPath: /backups
     volumes:
     - name: backup-pvc
       persistentVolumeClaim:
         claimName: backup-pvc
   ```

   Replace `$<customer-artifactory>` with the actual artifactory path, like ECR or any private artifactory.
2. Apply the pod specification to the EKS cluster.

   ```
   kubectl apply -f mongo-restore.yaml
   ```
3. Verify that the restore pod is running.

   ```
   kubectl get pods -n <PDC_NAMESPACE>
   ```
4. Access the restore pod.

   ```
   kubectl exec -it -n <PDC_NAMESPACE> mongo-restore -c mongo-restore -- bash
   ```
5. List the available backup files in the mounted directory.

   ```
   ls /backups/mongodb/<TIMESTAMP>
   ```

   The directory should contain MongoDB backup folders or BSON files representing each database.
6. Restore the MongoDB data from the backup.

   ```
   mongorestore \
       --host mongodb --port 27017 \
       --username root --password $MONGO_PASSWORD \
       --authenticationDatabase admin \
       --drop \
       /backups/mongodb/<TIMESTAMP>
   ```

   This command drops existing collections and restores data from the specified backup directory.
7. Verify that the data has been restored successfully.

   ```
   mongo --host <MONGO_HOST> --port <MONGO_PORT> \
     -u <MONGO_USER> -p <MONGO_PASSWORD> --authenticationDatabase admin
   show dbs
   ```

   The restored databases should appear in the list.
8. Exit the restore pod.

   ```
   exit
   ```
9. Delete the temporary restore pod.

   ```
   kubectl delete pod mongo-restore -n <PDC_NAMESPACE>
   ```
10. Restart the licensing-api deployment to apply the restored data.

    ```
    kubectl rollout restart deployment licensing-api -n <PDC_NAMESPACE>
    ```

**Result**

MongoDB data is restored successfully from the Amazon EBS or Amazon EFS storage used for Data Catalog backups. All MongoDB collections are recovered, and the licensing-api deployment is refreshed to reflect the restored data.

#### **Restore FE-Workers data from Amazon EBS volumes or Amazon EFS file systems**

In Data Catalog deployments running on Amazon EKS, administrators can restore FE-Workers data from backups stored in Amazon EBS or Amazon EFS. When Data Catalog backups are configured to use persistent storage, FE-Workers data, including patterns, dictionaries, and temporary profiling results, is stored in a PersistentVolumeClaim (PVC).\
You can restore this data by creating a temporary restore pod that mounts both the backup PVC and the FE-Workers data PVC, then extracting the backup files into the target directory.

{% hint style="info" %}
Use the same backup PVC that was used during the backup. Restoring data from an incorrect PVC may result in missing or inconsistent worker files.
{% endhint %}

Perform the following steps to restore FE-Workers data from backups stored in Amazon EBS or Amazon EFS.

**Before you begin**

Make sure the following requirements are met:

* The backup files exist in the `/backups/fe-workers/` directory of the backup PersistentVolumeClaim (PVC).
* kubectl is installed and configured to access the Amazon EKS cluster.
* You have identified the PVC name used for the backup and the PVC name used for FE-Workers data.
* The PDC namespace is correct.
* All active FE-Worker jobs or services are stopped before the restore is performed.

**Procedure**

1. Save the following pod configuration as `fe-worker-restore.yaml`.

   ```
   apiVersion: v1
   kind: Pod
   metadata:
     name: fe-worker-restore
     namespace: <PDC_NAMESPACE>
   spec:
     restartPolicy: Never
     containers:
     - name: fe-worker-restore
       image: $<customer-artifactory>/PDC_TOOLBOX:debian-12   # Lightweight image with basic tools
       command: [ "sleep", "3600" ]
       volumeMounts:
       - name: backup-pvc
         mountPath: /backups
       - name: fe-data
         mountPath: /home/node/data
     volumes:
     - name: backup-pvc
       persistentVolumeClaim:
         claimName: backup-pvc
     - name: fe-data
       persistentVolumeClaim:
         claimName: fe-worker-pvc     # Target PVC for FE data
   ```

   Replace `$<customer-artifactory>` with the actual artifactory path, like ECR or any private artifactory.
2. Apply the restore pod specification to the EKS cluster.

   ```
   kubectl apply -f fe-worker-restore.yaml
   ```
3. Verify that the restore pod is running.

   ```
   kubectl get pods -n <PDC_NAMESPACE>
   ```
4. Access the restore pod.

   ```
   kubectl exec -it -n <PDC_NAMESPACE> fe-worker-restore -c fe-worker-restore -- sh
   ```
5. List the available FE-Workers backup files.

   ```
   ls /backups/fe-workers/<TIMESTAMP>
   ```

   The directory should contain an archive file such as fe-worker-backup-\<TIMESTAMP>.tar.gz.
6. Extract the FE-Workers backup files into the target directory.

   ```
   tar xzf /backups/fe-workers/<TIMESTAMP>/fe-worker-backup-<TIMESTAMP>.tar.gz -C /home/node/data/
   ```
7. Verify that the files have been extracted successfully.

   ```
   ls -la /home/node/data/
   ```

   The directory should include data folders such as patterns-systemdefined, dictionaries-en, and data.
8. Exit the restore pod.

   ```
   exit
   ```
9. Delete the temporary restore pod.

   ```
   kubectl delete pod fe-worker-restore -n <PDC_NAMESPACE>
   ```

**Result**

FE-Workers data is restored successfully from the Amazon EBS or Amazon EFS storage used for Data Catalog backups. The restored dictionaries, patterns, and data files are available in the FE-Workers data directory and ready for use by the PDC application.

#### **Restore Kubernetes objects from Amazon EBS volumes or Amazon EFS file systems**

In Data Catalog deployments running on Amazon EKS, administrators can restore Kubernetes objects such as Secrets and ConfigMaps from backups stored in Amazon EBS or Amazon EFS. When Data Catalog backups are configured to use persistent storage, these objects are saved in a PersistentVolumeClaim (PVC) in the EKS cluster.\
You can restore Kubernetes objects by creating a temporary restore pod that mounts the same PVC and applies the backed-up manifests.

{% hint style="info" %}
Use the same backup PVC that was used during the backup process. Restoring from an incorrect PVC may result in missing or outdated configurations. The restore pod must use the pdc-backup-sa service account to access and apply Kubernetes objects.
{% endhint %}

Perform the following steps to restore Kubernetes objects, such as Secrets and ConfigMaps, from backups stored in Amazon EBS or Amazon EFS.

**Before you begin**

Make sure the following requirements are met:

* The object backup files exist in the `/backups/objects/` directory of the backup PersistentVolumeClaim (PVC).
* `kubectl` is installed and configured to access the Amazon EKS cluster.
* The `pdc-backup-sa` service account is configured with permissions to create and update Kubernetes objects.
* You have identified the PDC namespace and the PVC name used for storing the backup.
* You have cluster administrator access to apply `Secrets` and `ConfigMaps`.

**Procedure**

1. Save the following pod configuration as `object-restore.yaml`.

   ```
   apiVersion: v1
   kind: Pod
   metadata:
     name: object-restore
     namespace: <PDC_NAMESPACE>
   spec:
     restartPolicy: Never
     serviceAccountName: pdc-backup-sa   # Required for object restore
     containers:
     - name: object-restore
       image: $<customer-artifactory>/PDC_TOOLBOX:debian-12      # Image with kubectl installed
       command: [ "sleep", "3600" ]
       volumeMounts:
       - name: backup-pvc
         mountPath: /backups
     volumes:
     - name: backup-pvc
       persistentVolumeClaim:
         claimName: backup-pvc
   ```

   Replace `$<customer-artifactory>` with the actual artifactory path, like ECR or any private artifactory.
2. Apply the pod specification to the EKS cluster.

   ```
   kubectl apply -f object-restore.yaml
   ```
3. Verify that the restore pod is running.

   ```
   kubectl get pods -n <PDC_NAMESPACE>
   ```
4. Access the restore pod.

   ```
   kubectl exec -it -n <PDC_NAMESPACE> object-restore -c object-restore -- bash
   ```
5. List the available Kubernetes object backup files.

   ```
   ls /backups/objects/<TIMESTAMP>
   ```

   The directory should contain YAML manifest files for `Secrets` or `ConfigMaps`, such as `secret_cat-key_<TIMESTAMP>.yaml`.
6. Apply the backed-up object manifests to restore them in the cluster.

   ```
   kubectl apply -f /backups/objects/<TIMESTAMP>/secret_cat-key_<TIMESTAMP>.yaml -n <PDC_NAMESPACE>
   ```
7. Verify that the objects have been restored.

   ```
   kubectl get secrets -n <PDC_NAMESPACE>
   ```

   The restored secret (for example, `cat-key`) should appear in the list.
8. Exit the restore pod.

   ```
   exit
   ```
9. Delete the temporary restore pod.

   ```
   kubectl delete pod object-restore -n <PDC_NAMESPACE>
   ```

**Result**

Kubernetes Secrets and ConfigMaps are restored successfully from the Amazon EBS or Amazon EFS storage used for Data Catalog backups. The restored objects are available in the PDC namespace, allowing Data Catalog components to access their required configuration and credentials.

#### **Restore OpenSearch data from Amazon EBS volumes or Amazon EFS file systems**

In Data Catalog deployments running on Amazon EKS, administrators can restore backup data stored in Amazon EBS Volumes or Amazon EFS File Systems. When Data Catalog backups use persistent storage, all backup files are stored in a PersistentVolumeClaim (PVC) that remains available in the Amazon EKS cluster. Each Data Catalog component can be restored individually by creating a temporary restore pod that mounts the same PVC used during the backup process.

Restoring from Amazon EBS or Amazon EFS allows administrators to recover component data, such as PostgreSQL databases, MongoDB collections, OpenSearch indexes, FE-Workers data, and Kubernetes objects, directly within the cluster, without downloading backup files externally.

Use the same PVC that was used for backups. Restoring from an incorrect PVC can lead to missing or outdated search indexes. The restore process requires the jq utility in the container to process JSON data.

**Before you begin**

* Confirm that backup files exist in the `/backups/opensearch/` directory of the backup PVC.
* Verify that kubectl is installed and configured to access the Amazon EKS cluster.
* Ensure that the OpenSearch service is running in the same namespace.
* Identify the PVC name used for the backup and the PDC namespace.
* Confirm that the jq package is available in the container image (`PDC_TOOLBOX:debian-12`).

Perform the following steps to OpenSearch data from Amazon EBS Volumes or Amazon EFS file systems:

1. Save the following pod configuration as `opensearch-restore.yaml`.

   ```
   apiVersion: v1
   kind: Pod
   metadata:
     name: opensearch-restore
     namespace: <PDC_NAMESPACE>
   spec:
     restartPolicy: Never
     containers:
     - name: opensearch-restore
       image: $<customer-artifactory>/PDC_TOOLBOX:debian-12   # Includes curl and jq
       command: [ "sleep", "3600" ]
       volumeMounts:
       - name: backup-pvc
         mountPath: /backups
     volumes:
     - name: backup-pvc
       persistentVolumeClaim:
         claimName: backup-pvc
   ```

   Replace `$<customer-artifactory>` with the actual artifactory path, like ECR or any private artifactory.
2. Apply the restore pod specification to the EKS cluster.

   ```
   kubectl apply -f opensearch-restore.yaml
   ```
3. Verify that the restore pod is running.

   ```
   kubectl get pods -n <PDC_NAMESPACE>
   ```
4. Create the OpenSearch restore script locally and save it as opensearch\_restore.sh.\
   This script automates restoring all OpenSearch indexes from the PVC backup directory.

   ```
   #!/bin/bash
   # Configuration
   BACKUP_BASE="/backups/opensearch"
   OPENSEARCH_HOST="opensearch"
   OPENSEARCH_PORT="9200"
   echo "=== OpenSearch PVC Restore (Chunked) ==="
   echo
   # Check if we're in the right environment
   if [ ! -d "$BACKUP_BASE" ]; then
       echo "ERROR: Backup directory not found: $BACKUP_BASE"
       echo "Make sure PVC is mounted correctly"
       exit 1
   fi
   # List available backups
   echo "Available backups:"
   backups=$(find "$BACKUP_BASE" -maxdepth 1 -type d -name "202*" | sort -r)
   if [ -z "$backups" ]; then
       echo "  No backups found"
       exit 1
   fi
   for backup in $backups; do
       count=$(find "$backup" -name "*_info.json" -type f | wc -l)
       echo "  $(basename $backup) ($count indexes)"
   done
   echo
   read -p "Enter backup timestamp to restore: " timestamp
   BACKUP_DIR="$BACKUP_BASE/$timestamp"
   if [ ! -d "$BACKUP_DIR" ] || [ -z "$(find "$BACKUP_DIR" -name "*_info.json" -type f)" ]; then
       echo "ERROR: No backup files found for: $timestamp"
       exit 1
   fi
   # Safety check
   echo
   echo "Checking existing indexes..."
   existing=$(curl -s "http://$OPENSEARCH_HOST:$OPENSEARCH_PORT/_cat/indices/pdc_*?h=index" | tr '\n' ' ')
   if [ -n "$existing" ]; then
       echo "WARNING: These indexes will be DELETED:"
       for idx in $existing; do
           count=$(curl -s "http://$OPENSEARCH_HOST:$OPENSEARCH_PORT/$idx/_count" | jq -r '.count')
           echo "  - $idx ($count docs)"
       done
       read -p "Continue? (type 'yes'): " confirm
       [ "$confirm" != "yes" ] && exit 0
       echo
   fi
   # Get timestamp from first backup file using the simple format
   first_info_file=$(find "$BACKUP_DIR" -name "*_info.json" | head -1)
   backup_timestamp=$(grep "backup_timestamp" "$first_info_file" | cut -d':' -f2 | tr -d ' "')
   echo "Restoring from backup: $backup_timestamp"
   echo
   success=0
   fail=0
   # Function for fast parallel bulk processing
   process_bulk_fast() {
       local data_file="$1"
       local index="$2"
       local chunk_size=5000  # Larger chunks - 5000 documents
       local parallel_jobs=4  # Process 4 chunks in parallel
       echo "  Processing $chunk_size documents per chunk with $parallel_jobs parallel jobs..."
       total_lines=$(wc -l < "$data_file")
       total_docs=$((total_lines / 2))
       total_chunks=$(( (total_docs + chunk_size - 1) / chunk_size ))
       echo "  Total: $total_docs documents in $total_chunks chunks"
       # Create all chunks first
       echo "  Preparing chunks..."
       for ((chunk=1; chunk<=total_chunks; chunk++)); do
           start_line=$(( (chunk - 1) * chunk_size * 2 + 1 ))
           end_line=$(( chunk * chunk_size * 2 ))
           sed -n "${start_line},${end_line}p" "$data_file" > "/tmp/bulk_chunk_${chunk}.ndjson"
       done
       # Process chunks in parallel
       echo "  Starting parallel processing..."
       (
           for ((chunk=1; chunk<=total_chunks; chunk++)); do
               ((i=i%parallel_jobs)); ((i++==0)) && wait
               (
                   chunk_file="/tmp/bulk_chunk_${chunk}.ndjson"
                   if [ -s "$chunk_file" ]; then
                       lines_in_chunk=$(wc -l < "$chunk_file")
                       docs_in_chunk=$((lines_in_chunk / 2))
                       # Send bulk request with timeout
                       response=$(curl -s --max-time 60 -X POST "http://$OPENSEARCH_HOST:$OPENSEARCH_PORT/_bulk" \
                           -H 'Content-Type: application/x-ndjson' \
                           --data-binary @"$chunk_file")
                       if echo "$response" | jq -e '.errors == false' > /dev/null 2>&1; then
                           echo "    ✓ Chunk $chunk/$total_chunks ($docs_in_chunk docs)"
                       else
                           error_count=$(echo "$response" | jq -r '[.items[] | select(.index.error)] | length' 2>/dev/null || echo "?")
                           if [ "$error_count" = "0" ] 2>/dev/null; then
                               echo "    ✓ Chunk $chunk/$total_chunks ($docs_in_chunk docs)"
                           else
                               echo "    ⚠ Chunk $chunk/$total_chunks - $error_count errors"
                           fi
                       fi
                       # Clean up chunk file
                       rm -f "$chunk_file"
                   fi
               ) &
           done
           wait
       )
       echo "  Parallel processing completed"
   }
   # Function for very fast single-threaded processing (alternative)
   process_bulk_very_fast() {
       local data_file="$1"
       local index="$2"
       local chunk_size=10000  # Very large chunks - 10,000 documents
       echo "  Processing $chunk_size documents per chunk..."
       total_lines=$(wc -l < "$data_file")
       total_docs=$((total_lines / 2))
       total_chunks=$(( (total_docs + chunk_size - 1) / chunk_size ))
       echo "  Total: $total_docs documents in $total_chunks chunks"
       for ((chunk=1; chunk<=total_chunks; chunk++)); do
           start_line=$(( (chunk - 1) * chunk_size * 2 + 1 ))
           end_line=$(( chunk * chunk_size * 2 ))
           # Extract chunk
           sed -n "${start_line},${end_line}p" "$data_file" > /tmp/bulk_chunk.ndjson
           lines_in_chunk=$(wc -l < /tmp/bulk_chunk.ndjson)
           if [ $lines_in_chunk -eq 0 ]; then
               break
           fi
           docs_in_chunk=$((lines_in_chunk / 2))
           # Show progress every 10 chunks or for the first/last chunks
           if [ $((chunk % 10)) -eq 0 ] || [ $chunk -eq 1 ] || [ $chunk -eq $total_chunks ]; then
               echo "    Chunk $chunk/$total_chunks ($docs_in_chunk documents)..."
           fi
           # Send bulk request without waiting for detailed response
           curl -s -X POST "http://$OPENSEARCH_HOST:$OPENSEARCH_PORT/_bulk" \
               -H 'Content-Type: application/x-ndjson' \
               --data-binary @/tmp/bulk_chunk.ndjson > /dev/null
           # Show progress indicator
           if [ $((chunk % 50)) -eq 0 ]; then
               echo "    Progress: $chunk/$total_chunks chunks completed"
           fi
       done
       rm -f /tmp/bulk_chunk.ndjson
       echo "  Bulk data ingestion completed"
   }
   # Function for direct file processing (fastest)
   process_bulk_direct() {
       local data_file="$1"
       local index="$2"
       echo "  Direct bulk ingestion..."
       total_lines=$(wc -l < "$data_file")
       total_docs=$((total_lines / 2))
       echo "  Ingesting $total_docs documents directly..."
       # Send the entire file at once with longer timeout
       response=$(curl -s --max-time 300 -X POST "http://$OPENSEARCH_HOST:$OPENSEARCH_PORT/_bulk" \
           -H 'Content-Type: application/x-ndjson' \
           --data-binary @"$data_file")
       if echo "$response" | jq -e '.errors == false' > /dev/null 2>&1; then
           echo "  ✓ All $total_docs documents ingested successfully"
       else
           error_count=$(echo "$response" | jq -r '[.items[] | select(.index.error)] | length' 2>/dev/null || echo "?")
           if [ "$error_count" = "0" ] 2>/dev/null; then
               echo "  ✓ All $total_docs documents processed"
           else
               echo "  ⚠ Ingested with $error_count errors out of $total_docs documents"
           fi
       fi
   }
   # Restore each index using info files (same as your working script)
   for info_file in $(find "$BACKUP_DIR" -name "*_info.json"); do
       # Extract info from simple format (not JSON)
       index=$(grep "index_name" "$info_file" | cut -d':' -f2 | tr -d ' ')
       ts=$(grep "backup_timestamp" "$info_file" | cut -d':' -f2 | tr -d ' "')
       settings="$BACKUP_DIR/${index}_${ts}_settings.json"
       mapping="$BACKUP_DIR/${index}_${ts}_mapping.json"
       data="$BACKUP_DIR/${index}_${ts}_data.bulk"
       echo "Restoring: $index"
       # Check if backup files exist
       if [[ ! -f "$settings" || ! -f "$mapping" ]]; then
           echo "  ✗ Missing backup files for $index"
           ((fail++))
           continue
       fi
       # Delete if exists
       curl -s -X DELETE "http://$OPENSEARCH_HOST:$OPENSEARCH_PORT/$index" > /dev/null
       sleep 1
       # Create index
       echo "  Creating index..."
       # Extract settings - handle different formats
       if jq -e '.[]' "$settings" > /dev/null 2>&1; then
           # Format: {"index": {"settings": {...}}}
           jq '.[] | .settings.index | del(.creation_date, .uuid, .version, .provided_name)' "$settings" > /tmp/settings.json 2>/dev/null
       elif jq -e '.settings' "$settings" > /dev/null 2>&1; then
           # Format: {"settings": {...}}
           jq '.settings.index | del(.creation_date, .uuid, .version, .provided_name)' "$settings" > /tmp/settings.json 2>/dev/null
       else
           # Format: direct settings
           jq '.index | del(.creation_date, .uuid, .version, .provided_name)' "$settings" > /tmp/settings.json 2>/dev/null
       fi
       # If settings extraction failed, use defaults
       if [ ! -s /tmp/settings.json ] || ! jq -e '.' /tmp/settings.json > /dev/null 2>&1; then
           echo '{"number_of_shards": 1, "number_of_replicas": 1}' > /tmp/settings.json
       fi
       # Extract mappings
       if jq -e '.mappings' "$mapping" > /dev/null 2>&1; then
           jq '.mappings' "$mapping" > /tmp/mappings.json
       elif jq -e '.[]' "$mapping" > /dev/null 2>&1; then
           jq '.[] | .mappings' "$mapping" > /tmp/mappings.json
       else
           jq '.' "$mapping" > /tmp/mappings.json
       fi
       # Create the final payload
       jq -n --argjson settings "$(cat /tmp/settings.json)" --argjson mappings "$(cat /tmp/mappings.json)" '{
           settings: {index: $settings},
           mappings: $mappings
       }' > /tmp/payload.json
       # Debug: Show payload size
       payload_size=$(wc -c < /tmp/payload.json)
       echo "  Payload size: $payload_size bytes"
       # Create the index
       response=$(curl -s -X PUT "http://$OPENSEARCH_HOST:$OPENSEARCH_PORT/$index" -H 'Content-Type: application/json' -d @/tmp/payload.json)
       if echo "$response" | jq -e '.acknowledged == true' > /dev/null; then
           echo "  ✓ Index created"
           # Restore data with chunking based on file size
           if [ -f "$data" ] && [ -s "$data" ]; then
               lines=$(wc -l < "$data")
               expected_docs=$((lines/2))
               echo "  ↳ Restoring $expected_docs documents..."
               # Choose method based on file size (same as your working script)
               if [ $expected_docs -le 50000 ]; then
                   # Small files - direct upload
                   process_bulk_direct "$data" "$index"
               elif [ $expected_docs -le 200000 ]; then
                   # Medium files - large chunks
                   process_bulk_very_fast "$data" "$index"
               else
                   # Large files - parallel processing
                   process_bulk_fast "$data" "$index"
               fi
               # Final refresh
               echo "  Refreshing index..."
               curl -s -X POST "http://$OPENSEARCH_HOST:$OPENSEARCH_PORT/$index/_refresh" > /dev/null
               # Quick verification
               count_response=$(curl -s "http://$OPENSEARCH_HOST:$OPENSEARCH_PORT/$index/_count")
               if echo "$count_response" | jq -e '.count' > /dev/null; then
                   actual_count=$(echo "$count_response" | jq -r '.count')
                   echo "  📊 Document count: $actual_count"
               fi
           else
               echo "  ⓘ No data to restore"
           fi
           ((success++))
       else
           echo "  ✗ Failed to create index"
           error_type=$(echo "$response" | jq -r '.error.type // "unknown_error"' 2>/dev/null)
           error_reason=$(echo "$response" | jq -r '.error.reason // "unknown reason"' 2>/dev/null)
           echo "  Error: $error_type - $error_reason"
           # Debug: Show first 200 chars of payload for troubleshooting
           echo "  Payload preview: $(head -c 200 /tmp/payload.json)..."
           ((fail++))
       fi
       echo
   done
   # Restore aliases
   alias_file=$(find "$BACKUP_DIR" -name "aliases_*.json" | head -1)
   if [ -f "$alias_file" ]; then
       echo "Restoring aliases..."
       jq -r 'to_entries[] | select(.value.aliases) | .key as $idx | .value.aliases | keys[] | "\(.) \($idx)"' "$alias_file" | while read alias idx; do
           if curl -s -I "http://$OPENSEARCH_HOST:$OPENSEARCH_PORT/$idx" | grep -q "200 OK"; then
               curl -s -X POST "http://$OPENSEARCH_HOST:$OPENSEARCH_PORT/_aliases" -H 'Content-Type: application/json' -d "{\"actions\":[{\"add\":{\"index\":\"$idx\",\"alias\":\"$alias\"}}]}" > /dev/null
               echo "  ✓ Alias: $alias → $idx"
           fi
       done
       echo
   fi
   # Cleanup
   rm -f /tmp/settings.json /tmp/mappings.json /tmp/payload.json /tmp/bulk_chunk*.ndjson
   # Final verification
   echo "=== Verification ==="
   echo "Restored indexes:"
   curl -s "http://$OPENSEARCH_HOST:$OPENSEARCH_PORT/_cat/indices/pdc_*?h=index,docs.count&s=index" | while read line; do
       if [ -n "$line" ]; then
           index=$(echo $line | awk '{print $1}')
           count=$(echo $line | awk '{print $2}')
           echo "  ✓ $index ($count documents)"
       fi
   done
   # Summary
   echo
   echo "=== Summary ==="
   echo "Successful: $success"
   echo "Failed: $fail"
   echo "Total: $((success + fail))"
   if [ $fail -eq 0 ]; then
       echo "✓ Restore completed"
   else
       echo "⚠ Restore completed with errors"
   fi
   ```
5. Assign executable permissions to the restore script.

   ```
   chmod +x opensearch_restore.sh
   ```
6. Copy the restore script to the OpenSearch restore pod.

   ```
   kubectl cp opensearch_restore.sh <PDC_NAMESPACE>/opensearch-restore:/tmp/opensearch_restore.sh
   ```
7. Access the restore pod.

   ```
   kubectl exec -it -n <PDC_NAMESPACE> opensearch-restore -c opensearch-restore -- bash
   ```
8. Navigate to the script directory.

   ```
   cd /tmp
   ```
9. Run the OpenSearch restore script.

   ```
   ./opensearch_restore.sh
   ```

   The script restores OpenSearch indexes, mappings, and data from the backup directory and automatically re-creates aliases.\
   It processes indexes in chunks, using parallel ingestion for large data sets to speed up restoration.
10. Confirm that the indexes are restored successfully.

    ```
    curl -s "http://opensearch:9200/_cat/indices/pdc_*?h=index" | tr -d ' '
    ```

    The list should display all PDC-related indexes, such as `pdc_entity`, `pdc_policy`, and `pdc_glossary`.
11. Exit the restore pod.

    ```
    exit
    ```
12. Delete the temporary restore pod after completing the process.

    ```
    kubectl delete pod opensearch-restore -n <PDC_NAMESPACE>
    ```

**Result**

OpenSearch data is restored successfully from the Amazon EBS or Amazon EFS storage used for Data Catalog backups. All indexes, mappings, and aliases are re-created, and search functionality is available in Data Catalog once the OpenSearch service completes synchronization.

***
