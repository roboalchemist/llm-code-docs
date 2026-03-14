# Source: https://buildkite.com/docs/agent/self-hosted/gcp/elastic-ci-stack.md

# Source: https://buildkite.com/docs/agent/self-hosted/aws/elastic-ci-stack.md

# Elastic CI Stack for AWS overview

The Buildkite Elastic CI Stack for AWS gives you a private, autoscaling
[Buildkite agent](/docs/agent) cluster. You can use the Buildkite Elastic CI Stack for AWS to parallelize large test suites across hundreds of nodes, run tests, app deployments, or AWS ops tasks. Each Buildkite Elastic CI Stack for AWS deployment contains an Auto Scaling group and a launch template.

## Architecture

For an overview of the architecture of the Elastic CI Stack for AWS, see [Architecture](/docs/agent/self-hosted/aws/elastic-ci-stack/architecture).

## Features

The Buildkite Elastic CI Stack for AWS supports:

* All AWS regions (except China and US GovCloud)
* Linux and Windows operating systems
* Configurable instance size
* Configurable number of Buildkite agents per instance
* Configurable spot instance bid price
* Configurable auto-scaling based on build activity
* Docker and Docker Compose
* Per-pipeline S3 secret storage (with SSE encryption support)
* Docker registry push/pull
* CloudWatch Logs for system and Buildkite agent events
* CloudWatch metrics from the Buildkite API
* Support for stable, beta or edge Buildkite agent releases
* Multiple stacks in the same AWS Account
* Rolling updates to stack instances to reduce interruption

Most features are supported across both Linux and Windows. The following table provides details of which features are supported by these operating systems:

Feature | Linux | Windows
--- | --- | ---
Docker | ✅ | ✅
Docker Compose | ✅ | ✅
AWS CLI | ✅ | ✅
S3 Secrets Bucket | ✅ | ✅
ECR Login | ✅ | ✅
Docker Login | ✅ | ✅
CloudWatch Logs Agent | ✅ | ✅
Per-Instance Bootstrap Script | ✅ | ✅
🧑‍🔬 git-mirrors experiment | ✅ | ✅
SSM Access | ✅ | ✅
Instance Storage (NVMe) | ✅ |
SSH Access | ✅ |
Periodic `authorized_keys` Refresh | ✅ |
Periodic Instance Health Check | ✅ |
Git LFS | ✅ |
Additional sudo Permissions | ✅ |
RDP Access | | ✅
Pipeline Signing | ✅ | ✅

### Required and recommended skills

The Elastic CI Stack for AWS does not require familiarity with the underlying AWS services to deploy it. However, to run builds, some familiarity with the following services is required:

* [AWS CloudFormation](https://aws.amazon.com/cloudformation/) if using the AWS CloudFormation deployment method
* [Terraform](https://developer.hashicorp.com/terraform) if using the Terraform deployment method
* [Amazon EC2](https://aws.amazon.com/ec2/) (to select an EC2 `InstanceTypes` stack parameter appropriate for your workload)
* [Amazon S3](https://aws.amazon.com/s3/) (to copy your git clone secret for cloning and building private repositories)

Elastic CI Stack for AWS provides defaults and pre-configurations suited for most use cases without the need for additional customization. Still, you'll benefit from familiarity with VPCs, availability zones, subnets, and security groups for custom instance networking.

For post-deployment diagnostic purposes, deeper familiarity with EC2 is recommended to be able to access the instances launched to execute Buildkite Pipelines jobs over SSH or [AWS Systems Manager Sessions](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html).

### Billable services

Elastic CI Stack for AWS creates its own VPC (virtual private cloud) by default. Best practice is to set up a separate development AWS account and use role switching and consolidated billing. You can check out this external tutorial for more information on how to ["Delegate Access Across AWS Accounts"](http://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_cross-account-with-roles.html).

The Elastic CI Stack for AWS deploys several billable Amazon services that do not require upfront payment and operate on a pay-as-you-go principle, with the bill proportional to usage.

<table>
  <thead>
    <tr>
      <th style="width:30%">Service name</th>
      <th style="width:60%">Purpose</th>
      <th style="width:10%">Required</th>
    </tr>
  </thead>
  <tbody>

      <tr>
        <td>
          <p>EC2</p>
        </td>
        <td>
          <p>Deployment of instances</p>
        </td>
        <td>
          <p>☑️</p>
        </td>
      </tr>
    
      <tr>
        <td>
          <p>EBS</p>
        </td>
        <td>
          <p>Root disk storage of EC2 instances</p>
        </td>
        <td>
          <p>☑️</p>
        </td>
      </tr>
    
      <tr>
        <td>
          <p>Lambda</p>
        </td>
        <td>
          <p>Scaling of Auto Scaling group and modifying Auto Scaling group's properties</p>
        </td>
        <td>
          <p>☑️</p>
        </td>
      </tr>
    
      <tr>
        <td>
          <p>Systems Manager Parameter Store</p>
        </td>
        <td>
          <p>Storing the Buildkite agent token</p>
        </td>
        <td>
          <p>☑️</p>
        </td>
      </tr>
    
      <tr>
        <td>
          <p>CloudWatch Logs</p>
        </td>
        <td>
          <p>Logs for instances and Lambda scaler</p>
        </td>
        <td>
          <p>☑️</p>
        </td>
      </tr>
    
      <tr>
        <td>
          <p>CloudWatch Metrics</p>
        </td>
        <td>
          <p>Metrics recorded by Lambda scaler</p>
        </td>
        <td>
          <p>☑️</p>
        </td>
      </tr>
    
      <tr>
        <td>
          <p>S3</p>
        </td>
        <td>
          <p>Charging based on storage and transfers in/and out of the secrets bucket (on by default)</p>
        </td>
        <td>
          <p>❌</p>
        </td>
      </tr>
    
  </tbody>
</table>

Buildkite services are billed according to your [plan](https://buildkite.com/pricing).

### Supported builds

This stack is designed to run your builds in a shared-nothing pattern similar to the [Twelve-Factor App methodology](http://12factor.net):

* Each project should encapsulate its dependencies through Docker and Docker Compose.
* Build pipeline steps should assume no state on the machine (and instead rely on [build meta-data](/docs/pipelines/configure/build-meta-data), [build artifacts](/docs/pipelines/configure/artifacts), or S3).
* Secrets are configured using environment variables exposed using the S3 secrets bucket.

By following these conventions, you get a scalable, repeatable, and source-controlled CI environment that any team within your organization can use.

## Running your first build

You can use a [bash-parallel-example sample pipeline](https://github.com/buildkite/bash-parallel-example) to test with your new autoscaling stack. Click the **Add to Buildkite** button below (or on the [GitHub README](https://github.com/buildkite/bash-parallel-example)):

<a class="inline-block" href="https://buildkite.com/new?template=https://github.com/buildkite/bash-parallel-example" target="_blank" rel="nofollow"><img src="https://buildkite.com/button.svg" alt="Add Bash Example to Buildkite" class="no-decoration" width="160" height="30"></a>

Click **Create Pipeline**. Depending on your organization's settings, the next step will vary slightly:

* If your organization uses the web-based steps editor (default), your pipeline is now ready for its first build. You can skip to the next step.
* If your organization has been upgraded to the [YAML steps editor](/docs/pipelines/tutorials/pipeline-upgrade), you should see a **Choose a Starting Point** wizard. Select **Pipeline Upload** from the list:
  <div style="max-width: 391px"><div class="responsive-image-container"><img alt="Upload Pipeline from Version Control" src="/docs/assets/buildkite-pipeline-upload-KlI-lR_J.png" /></div></div>

Click **New Build** in the top right and choose a build message (perhaps a little party `\:partyparrot\:`?):

<div style="max-width: 570px"><div class="responsive-image-container"><img alt="Triggering Buildkite Build" src="/docs/assets/buildkite-new-build-IJGuNozv.png" /></div></div>

Once your build is created, head back to the [AWS EC2 Auto Scaling Groups](https://console.aws.amazon.com/ec2/v2/home?#AutoScalingGroups) to watch the Elastic CI Stack for AWS creating new EC2 instances:

<div style="max-width: 200px"><div class="responsive-image-container"><img alt="AWS EC2 Auto Scaling Group Menu" src="/docs/assets/ec2-asg-Dhn62JVq.png" /></div></div>

Select the **buildkite-AgentAutoScaleGroup-xxxxxxxxxxxx** group and then the **Instances** tab. You'll see instances starting up to run your new build and after a few minutes they'll transition from **Pending** to **InService**:

<div style="max-width: 1633px"><div class="responsive-image-container"><img alt="AWS Auto Scaling Group launching" src="/docs/assets/buildkite-demo-instances-XwUyCytw.png" /></div></div>

Once the instances are ready, they will appear on your Buildkite agents page:

<div style="max-width: 792px"><div class="responsive-image-container"><img alt="Buildkite Connected Agents" src="/docs/assets/buildkite-connected-agents-Bo6DeXW1.png" /></div></div>

And then your build will start running on your new agents:

<div style="max-width: 1178px"><div class="responsive-image-container"><img alt="Your First Build" src="/docs/assets/build-BGX2oBB5.png" /></div></div>

Congratulations on running your first Elastic CI Stack for AWS build on Buildkite! :tada:

## Get started with the Elastic CI Stack for AWS

Get started with Buildkite Elastic CI Stack for AWS for:

* Linux and Windows
  * [Setup with CloudFormation](/docs/agent/self-hosted/aws/elastic-ci-stack/ec2-linux-and-windows/setup)
  * [Setup with Terraform](/docs/agent/self-hosted/aws/elastic-ci-stack/ec2-linux-and-windows/terraform)
* Mac
  * [Setup with CloudFormation](/docs/agent/self-hosted/aws/elastic-ci-stack/ec2-mac/setup)
