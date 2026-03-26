# Source: https://docs.api7.ai/enterprise/3.2.16.7/high-availability/cp-outage-dp-resilience.md

# Source: https://docs.api7.ai/enterprise/3.2.16.6/high-availability/cp-outage-dp-resilience.md

# Source: https://docs.api7.ai/enterprise/3.2.16.5/high-availability/cp-outage-dp-resilience.md

# Source: https://docs.api7.ai/enterprise/3.2.16.4.1/high-availability/cp-outage-dp-resilience.md

# Source: https://docs.api7.ai/enterprise/3.2.15.2.1/high-availability/cp-outage-dp-resilience.md

# Source: https://docs.api7.ai/enterprise/3.2.14.6/high-availability/cp-outage-dp-resilience.md

# Source: https://docs.api7.ai/enterprise/3.7.x/high-availability/cp-outage-dp-resilience.md

# Source: https://docs.api7.ai/enterprise/3.6.x/high-availability/cp-outage-dp-resilience.md

# Source: https://docs.api7.ai/enterprise/3.5.x/high-availability/cp-outage-dp-resilience.md

# Source: https://docs.api7.ai/enterprise/3.4.x/high-availability/cp-outage-dp-resilience.md

# Source: https://docs.api7.ai/enterprise/3.3.x/high-availability/cp-outage-dp-resilience.md

# Implement Data Plane Resilience

Resilience refers to a system's ability to withstand and recover from failures, disruptions, or unexpected events.

In this document, you will learn why you should consider data plane (DP) resilience pattern in API7 and how to implement it, such that when the control plane (CP) becomes unavailable, the DP instances can still operate normally. This helps you formulate a disaster recovery plan and quickly resume mission-critical functions when the control plane (CP) becomes unavailable, ensuring the high availability of your system.

Below is an interactive demo providing a hands-on introduction to implementing data plane resilience.

## Why Consider DP Resilience[â](#why-consider-dp-resilience "Direct link to Why Consider DP Resilience")

DP could encounter issues connecting with CP. The following are a few potential causes:

* Poor network connectivity between DP and CP instances
* CP database crash
* CP upgrade
* Resource contention on the CP host
* CP host hardware failure

## DP Resilience Pattern[â](#dp-resilience-pattern "Direct link to DP Resilience Pattern")

API7 Enterprise supports configuring CP to periodically dump configurations to AWS S3 buckets, so that in the event of a CP outage, DP can start in the [standalone mode](https://docs.api7.ai/apisix/production/deployment-modes.md#standalone-mode) and pull the latest gateway configurations from the storage to continue proxying requests.

![solution-diagram](https://static.api7.ai/uploads/2024/07/01/yAwwzGkt_dp-resilience.png)

Once the CP is recovered, DP should continue fetching configurations from the CP.

## Implement DP Resilience[â](#implement-dp-resilience "Direct link to Implement DP Resilience")

### Prerequisites[â](#prerequisites "Direct link to Prerequisites")

* [Install API7 Enterprise](https://docs.api7.ai/enterprise/3.3.x/getting-started/install-api7-ee.md).
* Complete [Start a Sample Upstream Service](https://docs.api7.ai/enterprise/3.3.x/getting-started/launch-your-first-api.md#start-a-sample-upstream-service) and [Create Service and Route](https://docs.api7.ai/enterprise/3.3.x/getting-started/launch-your-first-api.md#create-service-and-route).

### Provision AWS Resources[â](#provision-aws-resources "Direct link to Provision AWS Resources")

1. Create an AWS account and log in as an IAM user.
2. Create [two S3 buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html), one for gateway instance configurations, such as keyring and discovery; and one for gateway resource configurations, such as routes and services.
3. Obtain the [IAM user access key and secret access key](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#Using_CreateAccessKey).
4. Attach the policy that [allows read and write access to objects in S3 buckets](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_s3_rw-bucket.html) to the IAM user.

### Configure CP to Back Up Configurations[â](#configure-cp-to-back-up-configurations "Direct link to Configure CP to Back Up Configurations")

In the working directory where you ran the [quickstart command to install API7 Enterprise](https://docs.api7.ai/enterprise/3.3.x/getting-started/install-api7-ee.md#install-api7-enterprise), you should find a `api7-ee` directory, in which there is a `docker-compose.yaml` and various service configuration files.

Add the `fallback_cp` configuration to the dashboard configuration file:

api7-ee/dashboard\_conf/conf.yaml

```
fallback_cp:
  aws_s3:
    access_key: your-aws-iam-access-key
    region: ap-south-1
    config_bucket: bucket-to-push-config-data
    resource_bucket: bucket-to-push-resource-data
    secret_key: your-aws-iam-secret-access-key
  cron_spec: '@every 1m'
```

â¶ Replace with your AWS IAM user access key.

â· Replace with your AWS region.

â¸ Replace with your S3 bucket name where instance configuration details, such as keyring and discovery, should be pushed.

â¹ Replace with your S3 bucket name where APISIX resource configurations, such as routes and services, should be pushed.

âº Replace with your AWS IAM user secret access key.

â» Configure frequency to push to the S3 buckets every minute.

Restart the dashboard container:

```
docker-compose -f api7-ee/docker-compose.yaml restart api7-ee-dashboard
```

API7 should start pushing CP configurations to the S3 buckets every minute.

### Verify[â](#verify "Direct link to Verify")

In this section, you will first send a request to the route to see the expected upstream response. Then you will restart DP deployment in [standalone mode](https://docs.api7.ai/apisix/production/deployment-modes.md#standalone-mode), so that it starts fetching configurations from S3 buckets, and verify that the DP proxies requests as usual.

Send a request to the route:

```
curl "http://127.0.0.1:9080/ip"
```

You should see a response similar to the following:

```
{
  "origin": "127.0.0.1"
}
```

Suppose the CP has now become unavailable. Update each DP configuration file to start [standalone mode](https://docs.api7.ai/apisix/production/deployment-modes.md#standalone-mode):

config.yaml

```
deployment:
  role: data_plane
  role_data_plane:
    config_provider: yaml
  fallback_cp:
    aws_s3:
      access_key: your-aws-iam-access-key
      secret_key: your-aws-iam-secret-access-key
      config_bucket: bucket-to-push-config-data
      resource_bucket: bucket-to-push-resource-data
      region: ap-south-1
```

Reload DP instances for configuration changes to take effect. The DP instances should start in standalone mode and fetch configurations from the S3 buckets.

Send a request to the route:

```
curl "http://127.0.0.1:9080/ip"
```

You should see a response similar to the following, verifying the DP is routing the request from the configurations in S3:

```
{
  "origin": "127.0.0.1"
}
```

When the CP has recovered, remove the earlier change to the deployment mode and reload DP instances. They should now start synchronizing configurations from the CP.
