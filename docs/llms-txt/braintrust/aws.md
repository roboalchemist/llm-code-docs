# Source: https://braintrust.dev/docs/guides/self-hosting/aws.md

# Self-host on AWS

This guide shows you how to deploy the Braintrust data plane in your AWS account using the Braintrust [Terraform module](https://github.com/braintrustdata/terraform-aws-braintrust-data-plane). This is the recommended way to self-host Braintrust on AWS.

## Set up the data plane

Deploy the Braintrust data plane infrastructure in your AWS account.

<Note>
  Braintrust recommends deploying in a dedicated AWS account. AWS enforces account-level [Lambda concurrency limits](https://docs.aws.amazon.com/lambda/latest/dg/lambda-concurrency.html), and since Braintrust's API runs on Lambda, sharing an account with other workloads can lead to throttling and service disruptions. A dedicated account also aligns with AWS best practices for workload isolation and security.
</Note>

<Steps>
  <Step title="Configure the Terraform module">
    The Braintrust [Terraform module](https://github.com/braintrustdata/terraform-aws-braintrust-data-plane) contains all the necessary resources for a self-hosted Braintrust data plane.

    1. Copy the entire contents of the [`examples/braintrust-data-plane`](https://github.com/braintrustdata/terraform-aws-braintrust-data-plane/tree/main/examples/braintrust-data-plane) directory from the [terraform-aws-braintrust-data-plane](https://github.com/braintrustdata/terraform-aws-braintrust-data-plane) repository into your own repository.

    2. In `provider.tf`, configure your AWS account and region.

       Supported regions: `us-east-1`, `us-east-2`, `us-west-2`, `eu-west-1`, `ca-central-1`, and `ap-southeast-2`. If you require support for a different region, contact Braintrust.

    3. In `terraform.tf`, set up your remote backend (typically S3 and DynamoDB).

    4. In `main.tf`, customize the Braintrust deployment settings.

       The defaults are for suitable for a large production-sized deployment. Adjust them based on your needs, but keep in mind the [hardware requirements](/guides/self-hosting/index#hardware-requirements).
  </Step>

  <Step title="Initialize AWS account">
    Braintrust recommends a dedicated AWS account for your Braintrust deployment.

    If you're using a new AWS account, run the [`create-service-linked-roles.sh`](https://github.com/braintrustdata/terraform-aws-braintrust-data-plane/blob/main/scripts/create-service-linked-roles.sh) script to create all necessary IAM service-linked roles for the deployment:
  </Step>

  <Step title="Configure Brainstore license">
    Your deployment includes Brainstore, a high-performance query engine for real-time trace ingestion.
    Brainstore requires a license key.

    1. In the Braintrust UI, go to **Settings** > **Data plane**.
    2. Copy your Brainstore license.

       <Note>
         If you don't see your data plane configuration, [contact Braintrust](mailto:support@braintrust.dev) to enable self-hosting.
       </Note>
    3. Pass the key to Terraform in one of the following ways:

       * Set `TF_VAR_brainstore_license_key=your-key` in your environment.
       * Pass it via command line: `terraform apply -var 'brainstore_license_key=your-key'`.
       * Add it to an uncommitted `terraform.tfvars` or `.auto.tfvars` file.
       * Store it in AWS Secrets Manager and load it at runtime using the `aws_secretsmanager_secret_version_source` data source.

       <Warning>
         Do not commit the license key to your git repository.
       </Warning>
  </Step>

  <Step title="Deploy the module">
    Initialize and apply the Terraform configuration:

    ```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
    terraform init
    terraform apply
    ```

    This will create all necessary AWS resources including:

    * Two isolated VPCs:
      * **Main VPC**: Hosts Braintrust services (API, database, Redis, Brainstore)
      * **Quarantine VPC**: Isolated environment where user-defined functions execute
    * Lambda functions for the Braintrust API
    * Public CloudFront endpoint and API Gateway
    * EC2 Auto-scaling group for Brainstore
    * PostgreSQL database, Redis cache, and S3 buckets
    * KMS key for encryption
  </Step>

  <Step title="Get your API URL">
    After the deployment completes, get your API URL from the Terraform outputs:

    ```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
    terraform output
    ```

    You should see output similar to:

    ```
    api_url = "https://dx6atff6gocr6.cloudfront.net"
    ```

    Save this URL - you'll need it to configure your Braintrust organization.
  </Step>
</Steps>

## Configure your organization

Connect your Braintrust organization to your newly deployed data plane.

<Warning>
  Changing your live organization's API URL can disrupt access for existing users. If you are testing, create a new Braintrust organization for your data plane instead of updating your live environment.
</Warning>

<Steps>
  <Step title="Point your organization to your data plane">
    1. In the Braintrust UI, go to **Settings** > **Data plane**.
    2. In **API URL** area, select **Edit**.
    3. Enter the API URL from the last step.
    4. Leave the other fields blank.
    5. Select **Save**.
  </Step>

  <Step title="Verify the connection">
    The UI will automatically test the connection to your new data plane. Verify that the ping to each endpoint is successful.

        <img src="https://mintcdn.com/braintrust/vRnsqWnu5sp0FN9X/images/guides/self-hosting/aws/Braintrust-API-URL-verify.png?fit=max&auto=format&n=vRnsqWnu5sp0FN9X&q=85&s=a3d73fd28eb1b5e7999962094786dd0b" alt="Verify Successful Ping" data-og-width="2040" width="2040" data-og-height="1026" height="1026" data-path="images/guides/self-hosting/aws/Braintrust-API-URL-verify.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/vRnsqWnu5sp0FN9X/images/guides/self-hosting/aws/Braintrust-API-URL-verify.png?w=280&fit=max&auto=format&n=vRnsqWnu5sp0FN9X&q=85&s=12d5222932ea9d9c2bf5fdf9d8ca9c8a 280w, https://mintcdn.com/braintrust/vRnsqWnu5sp0FN9X/images/guides/self-hosting/aws/Braintrust-API-URL-verify.png?w=560&fit=max&auto=format&n=vRnsqWnu5sp0FN9X&q=85&s=fbfddc6440d35b97502b01269ce7df0f 560w, https://mintcdn.com/braintrust/vRnsqWnu5sp0FN9X/images/guides/self-hosting/aws/Braintrust-API-URL-verify.png?w=840&fit=max&auto=format&n=vRnsqWnu5sp0FN9X&q=85&s=c9264196a6e01e9f92c54735d23c346a 840w, https://mintcdn.com/braintrust/vRnsqWnu5sp0FN9X/images/guides/self-hosting/aws/Braintrust-API-URL-verify.png?w=1100&fit=max&auto=format&n=vRnsqWnu5sp0FN9X&q=85&s=0ba20b9f54a339e5c51c0bb81331223b 1100w, https://mintcdn.com/braintrust/vRnsqWnu5sp0FN9X/images/guides/self-hosting/aws/Braintrust-API-URL-verify.png?w=1650&fit=max&auto=format&n=vRnsqWnu5sp0FN9X&q=85&s=20b708db0402f32e2844aa6abd56b1b7 1650w, https://mintcdn.com/braintrust/vRnsqWnu5sp0FN9X/images/guides/self-hosting/aws/Braintrust-API-URL-verify.png?w=2500&fit=max&auto=format&n=vRnsqWnu5sp0FN9X&q=85&s=55b3869d71c4f4342ddc69a6fcdedba3 2500w" />
  </Step>
</Steps>

## Update the deployment

Run `terraform apply` to update your deployment. This will apply any infrastructure changes and update the Lambda functions while preserving your data.

```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
terraform apply
```

<Warning>
  Carefully review the output of `terraform plan` before applying any changes to your deployment. If you see something unexpected, like deletion of a database or S3 bucket, [contact Braintrust](mailto:support@braintrust.dev) for help.
</Warning>

To pin to a specific Terraform module version, add a `?ref=<version>` to the module source:

```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
module "braintrust-data-plane" {
  source = "github.com/braintrustdata/terraform-braintrust-data-plane?ref=vX.Y.Z"

  # ... other configuration ...
}
```

Terraform releases: [GitHub Releases](https://github.com/braintrustdata/terraform-braintrust-data-plane/releases)

## Debug issues

If you encounter issues, you can use the [`dump-logs.sh`](https://github.com/braintrustdata/terraform-aws-braintrust-data-plane/blob/main/scripts/dump-logs.sh) script to collect logs:

```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
./scripts/dump-logs.sh <deployment_name> [--minutes N] [--service <svc1,svc2,...|all>]
```

For example, to dump 60 minutes of logs for the `bt-sandbox` deployment, run:

```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
./scripts/dump-logs.sh bt-sandbox
```

This will save logs for all services to a `logs-<deployment_name>` directory, which you can share with the Braintrust team for debugging.

## Customize the deployment

### Use an existing VPC

To integrate with an existing VPC, set `create_vpc = false` and provide your existing VPC identifiers. Your VPC must meet these prerequisites:

* Minimum 3 private subnets across different availability zones
* At least 1 public subnet
* Properly configured internet and NAT gateways with route tables

The module will manage security groups independently. Pass your existing VPC's ID, subnets, and security group IDs to the `services`, `database`, and `redis` modules.

### Use custom tags

To apply custom tags to all resources, pass the `custom_tags` parameter to the Braintrust module:

```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
module "braintrust-data-plane" {
  source = "github.com/braintrustdata/terraform-aws-braintrust-data-plane"

  custom_tags = {
    Environment = "production"
    Team        = "ml-platform"
    CostCenter  = "engineering"
  }

  # ... other configuration ...
}
```

These tags will be applied to all resources including Brainstore EC2 instances, volumes, and ENIs. The deployment name variable automatically prefixes resource names and applies a `BraintrustDeploymentName` tag across all resources.

<Note>
  Use the `custom_tags` parameter instead of the AWS provider's `default_tags` configuration. Due to a Terraform limitation, `default_tags` are not applied to resources that use launch templates, such as Brainstore instances.
</Note>

### Redis instance sizing

<Warning>
  **Important for AWS**: Avoid using burstable Redis instances (t-family instances like `cache.t4g.micro`) in production. These instances use CPU credits that can be exhausted during high-load periods, leading to performance throttling.

  Instead, use non-burstable instances like `cache.r7g.large`, `cache.r6g.medium`, or `cache.r5.large` for predictable performance. Even if these instances seem oversized initially, they provide consistent performance without the risk of CPU credit exhaustion.
</Warning>

### VPC connectivity

To connect Braintrust's VPC to other internal resources (like an LLM gateway), use one of the following approaches:

* Create a VPC Endpoint Service for your internal resource, then create a VPC Interface Endpoint inside of the Braintrust "Quarantine" VPC
* Set up VPC peering with the Braintrust "Quarantine" VPC


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://braintrust.dev/docs/llms.txt