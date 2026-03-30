# Source: https://documentation.wazuh.com/current/proof-of-concept-guide/aws-infrastructure-monitoring.md

<!-- Copyright (C) 2015, Wazuh, Inc. -->

# Monitoring AWS infrastructure

This use case shows how the Wazuh module for AWS (aws-s3) enables the log data collection from different AWS sources.

To learn more about monitoring AWS resources, see the [Using Wazuh to monitor AWS](../cloud-security/amazon/index.md) section of the documentation.

## Infrastructure

| Cloud service     | Description                                                                                                                                                                                                                                                                                                                                                                                                 |
|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Amazon CloudTrail | AWS Cloudtrail, like all other supported AWS services, requires setting the [necessary policies](../cloud-security/amazon/services/supported-services/cloudtrail.md#cloudtrail-policy-configuration) for user permissions and providing a valid authentication method. In this PoC, we use the [profile authentication](../cloud-security/amazon/services/prerequisites/credentials.md#aws-profile) method. |

## Configuration

Take the following steps to configure Wazuh to monitor Amazon CloudTrail services and identify security incidents.

### CloudTrail

1. Access the CloudTrail service using the AWS console.
2. Create a new trail.
3. Choose between creating a new S3 bucket or specifying an existing one to store CloudTrail logs. Note down the name of the S3 bucket used as itâs necessary to specify it in the Wazuh configuration.

The image below shows how to create a new CloudTrail service and attach a new S3 bucket.

<a id="wazuh_image-0"></a>
![](images/poc/cloudtrail.gif)

### Wazuh server

1. Enable the Wazuh AWS module in the `/var/ossec/etc/ossec.conf` configuration file on the Wazuh server. Add only the AWS buckets of interest. Read our guide on how to [Configure AWS credentials](../cloud-security/amazon/services/prerequisites/credentials.md):
   ```xml
   <wodle name="aws-s3">
     <disabled>no</disabled>
     <interval>30m</interval>
     <run_on_start>yes</run_on_start>
     <skip_on_error>no</skip_on_error>

     <bucket type="cloudtrail">
       <name><AWS_BUCKET_NAME></name>
       <aws_profile><AWS_PROFILE_NAME></aws_profile>
     </bucket>
   </wodle>
   ```
2. Restart the Wazuh manager to apply the changes:
   ```console
   $ sudo systemctl restart wazuh-manager
   ```

## Test the configuration

Once you configure Cloudtrail, you can generate events by simply creating a new IAM user account using the IAM service. This generates an event that Wazuh processes.

The Wazuh default ruleset parses AWS logs and generates alerts automatically. The alerts appear as soon as Wazuh receives the logs from the AWS S3 bucket.

You can also find additional [CloudTrail use cases](../cloud-security/amazon/services/supported-services/cloudtrail.md#cloudtrail-use-cases) in our documentation.

## Visualize the alerts

You can visualize the alert data in the Wazuh dashboard. To do this, navigate through **Amazon Web Services** module.

<a id="wazuh_image-1"></a>
![](images/poc/AWS-alerts.png)
