# Source: https://docs.anyscale.com/administration/cloud-deployment/manage-aws-cloud.md

# Manage Anyscale clouds on AWS

[View Markdown](/administration/cloud-deployment/manage-aws-cloud.md)

# Manage Anyscale clouds on AWS

The creator or assigned owner of an Anyscale cloud can manage deployed cloud resources. The three main ways to modify an Anyscale cloud are deleting, editing, and setting default resources.

## Delete an Anyscale Cloud[​](#delete-an-anyscale-cloud "Direct link to Delete an Anyscale Cloud")

To delete an Anyscale Cloud, follow these steps to ensure a safe and complete removal of all associated resources. This process involves terminating instances and clusters, running the deletion command, and understanding the post-deletion implications.

### Step 1: Terminate all active instances and clusters[​](#step-1-terminate-all-active-instances-and-clusters "Direct link to Step 1: Terminate all active instances and clusters")

For all clusters with running, pending, and error statuses, follow the instructions in the UI to stop the workload. Verify in your AWS Management Console that these cluster have no running instances.

### Step 2: Delete the cloud[​](#step-2-delete-the-cloud "Direct link to Step 2: Delete the cloud")

Delete the Anyscale cloud with the following command:

```
anyscale cloud delete --name ANYSCALE_CLOUD_NAME
```

Example command and output:

* anyscale cloud setup (auto)
* anyscale cloud register (custom)

```
anyscale cloud delete --name example_cloud_name
```

The following output displays:

```
Authenticating
Loaded Anyscale authentication token from ANYSCALE_CLI_TOKEN.

Output
If the cloud cld_prcjv8jc9tmbv3q54mc2h7dnl6 is deleted, you won't be able to access existing clusters of this cloud.
For more information, please refer to the documentation https://docs.anyscale.com/user-guide/onboard/clouds#cloud-deletion
Continue? [y/N]: y
(anyscale +6.8s)
Track progress of cloudformation at https://ap-southeast-1.console.aws.amazon.com/cloudformation/home?region=ap-southeast-1#/stacks/stackinfo?stackId=arn:aws:cloudformation:ap-southeast-1:123456:stack/cld-prcjv8jc32r89fniuf23/123456789
⠸ Deleting cloud resources through cloudformation...(anyscale +49.1s) Cloudformation stack arn:aws:cloudformation:ap-southeast-1:815664363732:stack/cld-prcjv8jc32r89fniuf23/123456789 is deleted.
(anyscale +49.1s)
The S3 bucket (anyscale-production-data-cld-prcjv8jc32r89fniuf23) associated with this cloud still exists.
If you no longer need the data associated with this bucket, please delete it.
(anyscale +49.4s) Deleted cloud with name example_cloud_name.
```

```
anyscale cloud delete --name example_cloud_name
```

The following output displays:

```
Authenticating
Loaded Anyscale authentication token from ANYSCALE_CLI_TOKEN.

Output
If the cloud cld_gexl9ps7p6szgcgqn4gs1yup28 is deleted, you won't be able to access existing clusters of this cloud.
For more information, please refer to the documentation https://docs.anyscale.com/user-guide/onboard/clouds#cloud-deletion
Continue? [y/N]: y
(anyscale +2.9s) Deleting AWS cross account roles ...
(anyscale +3.8s) AWS cross account roles deletion complete.
(anyscale +3.8s) Delete DataPlane IAM role manually if you aren't using Ray OSS.
(anyscale +4.1s) Deleted cloud with name example_cloud_name.
```

* This operation is only supported if the cloud has no non-terminated clusters associated with it, that means there are no running nor pending instances.

  <!-- -->

  * If the cluster's status is `running`, terminate the cluster.
  * If the cluster has an error status, follow the instructions on the error. Also check your AWS console to ensure that there are no running instances of this cluster.

### Post-deletion implications[​](#post-deletion-implications "Direct link to Post-deletion implications")

* After deleting an Anyscale cloud, you can no longer create clusters, workspaces, jobs, or services using this cloud.
* Any clusters associated with the deleted cloud are no longer accessible.
* If a service was deployed in this cloud, deleting the cloud also removes any Anyscale managed ALB resources and TLS certificates associated with it. In the event that the deletion of ALB resources fails, the cloud deletion process aborts until you properly clean up these resources. Once you resolve them, re-run cloud deletion to remove any remaining resources.

caution

When you delete an Anyscale cloud that you set up using `anyscale cloud setup`, Anyscale also removes all associated resources.

However, deleting a cloud created using `anyscale cloud register` doesn't automatically remove any AWS resources you created. To revoke Anyscale's access to these AWS resources, you should either delete the cross account access role or remove Anyscale from the trust policy.

You can revoke Anyscale's access to your AWS account by deleting the Anyscale IAM role in your account, which has the following format: `anyscale-iam-role` or `anyscale-iam-role-<8 hex digits>`.

## Set a default Anyscale cloud[​](#set-a-default-anyscale-cloud "Direct link to Set a default Anyscale cloud")

Anyscale launches clusters in the default Cloud if you don't specify one specified in the [compute configs](/configuration/compute.md). You can set a default Anyscale Cloud with this command:

```
 anyscale cloud set-default ANYSCALE_CLOUD_NAME
```

## Update custom resources[​](#update-resources "Direct link to Update custom resources")

For Anyscale clouds deployed with `anyscale cloud register`, you can modify the EFS and S3 configuration. Prior to updating, Anyscale performs a static verification of cloud resources. If errors occur during this validation, review and resolve any issues.

To update cloud resources, download your current cloud configuration, modify the resources file, then use `anyscale cloud update` to apply the changes. See [Update multiple resources for a cloud](/admin/cloud/multi-cloud.md#update).

### EFS[​](#efs "Direct link to EFS")

To update the EFS ID or mount target, download your current cloud configuration and modify the resources file. See [Update multiple resources for a cloud](/admin/cloud/multi-cloud.md#update).

The following example shows the structure of a cloud resource with updated file storage configuration:

```
- name: vm-aws-us-west-2
  provider: AWS
  compute_stack: VM
  region: us-west-2
  file_storage:  # Update this section
    file_storage_id: <your_new_aws_efs_id>
    mount_targets:
      - address: <your_new_aws_efs_mount_target_ip>
```

### S3 bucket[​](#s3-bucket "Direct link to S3 bucket")

To update the S3 bucket, download your current cloud configuration and modify the resources file. See [Update multiple resources for a cloud](/admin/cloud/multi-cloud.md#update).

The following example shows the structure of a cloud resource with updated object storage configuration:

```
- name: vm-aws-us-west-2
  provider: AWS
  compute_stack: VM
  region: us-west-2
  object_storage:  # Update this section
    bucket_name: s3://<your_new_bucket_name>
```

🏁Verify an Anyscale cloud

To ensure that the updated Anyscale cloud meets the requirements, add the optional flag `--functional-verify` to launch a test workspace and service.

🧹Clean up resources

Updating and replacing resources doesn't automatically delete unused entities. You must separately delete any unwanted resources.

### Additional options[​](#additional-options "Direct link to Additional options")

* Use `--cloud-id` as an alternative to cloud name.
* Add the `--functional-verify` flag to automatically launch a workspace or service from your cloud and verify that your updated cloud is functional.

### Important notes[​](#important-notes "Direct link to Important notes")

* Before the update, Anyscale executes a static cloud verification and requests confirmation. Ensure you review any warnings or errors in the verification results.
* Resource updates apply only to `anyscale cloud register` clouds, not `anyscale cloud setup` clouds.
* If there are running workloads utilizing the old resources, you may want to retain them. Note that this update doesn't automatically remove any old resources. If you wish to delete them, you need to handle it manually.

## Update IAM role[​](#update-iam-role "Direct link to Update IAM role")

For `anyscale cloud setup` clouds, you can use the `cloud update` command keep your cross-account IAM role up to date. The cross-account IAM role looks like `anyscale-iam-role-<random chars>`. See [Virtual machine deployments: Cross-account IAM](/iam.md#cross-account-iam).

First make sure to run `pip install -U anyscale` to upgrade your Anyscale CLI to the latest version. Then update the cloud:

```
anyscale cloud update <cloud_name>
```

You can also update the cloud using cloud ID:

```
anyscale cloud update --id <cloud_id>
```

Anyscale maintains 3 inline policies: `Anyscale_IAM_Policy_Steady_State`, `Anyscale_IAM_Policy_Service_Steady_State`, `Anyscale_IAM_Policy_Initial_Setup`. Running `cloud update` will create or overwrite these policies.

caution

If you edit these policies before, you'll see [**drifts**](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html) on your cross account IAM role. We will resolve the drifts by appending the drifted statements to an inline policy `Customer_Drifts_Policy`. If you remove some permissions or restrict the resources in the policy, you may want to reapply the changes manually after cloud update completes.
