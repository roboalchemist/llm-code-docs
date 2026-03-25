# Source: https://docs.ox.security/ox-integrations/3rd-party-integrations/cloud-security/aws.md

# AWS

**AWS (Amazon Web Services**) is a comprehensive, evolving cloud computing platform provided by Amazon that includes a mixture of infrastructure as a service (IaaS), platform as a service (PaaS) and packaged software as a service (SaaS) offerings.

**Amazon Elastic Container Registry (ECR**) is a fully-managed Docker container registry that makes it easy for developers to store, manage, and deploy Docker container images. Amazon ECR is integrated with Amazon Elastic Container Service (ECS), simplifying development to production workflow.

**Amazon CloudWatch** is a monitoring and management service that provides data and actionable insights for AWS, hybrid, and on-premises applications and infrastructure resources.

Connecting your AWS account to our system will allow us to analyze it and find vulnerabilities regarding IaC and Artifact integrity, using our own tools as well as other security tools such as Prowler.

The connection is being established by giving us (and only us) permissions for specific, carefully picked resources/ policies that will enable us to run the tools on them.

For a description of the supported Kubernetes connection models, including direct cloud integration and Inspector-based access, see [Kubernetes Reachability](https://docs.ox.security/ox-integrations/3rd-party-integrations/cloud-security/kubernetes-reachability).

### Connection options

#### Automatic

A sort of "plug-and-play" to connect a single AWS account, everything is pre-configured to what we need in order to run our tools, it will automatically create for you the user, role, and policies that we require, all you have to do is follow the instructions.

1. Log in to your AWS console.
2. Under the Automatic tab, click the 'Cloud Formation Assume Role' button.
3. On the CloudFormation page: 3.1. Check the two acknowledgment boxes at the bottom. 3.2. Click Create stack. Note: if you have already created a Cloud Formation stack before for ox-security you will need to rename the stack name, otherwise it will issue an error (Stack \[ox-security] already exists)
4. Once the stack has been created, open CloudFormation outputs and copy the OxRoleArn value
5. In the OX Connector below paste the value in the field AWS Role ARN.
6. Click Connect.
7. You should receive a message that the connection was successful, if not please repeat the steps above.

#### Manual

This is a more advanced way of configuration for companies who want to create all the user/ roles/ policies that we need themselves.

1. Log in to your AWS console.
2. Create a new role in the AWS IAM Console.
3. Select Another AWS account for the Role Type.
4. For Account ID, enter 351456651185 (OX's account ID). This means that you are granting OX read only access to your AWS data.
5. Select Require external ID and enter the one generated in the OX AWS integration tile. Make sure you leave Require MFA disabled.
6. Click Next: Permissions.
7. In the Attach permissions policies screen Filter policies search and include the following policies:
   1. ViewOnlyAccess
   2. SecurityAudit
8. Click Next: Tags and Next: Review.
9. Name the Role OxAWSIntegrationRole or one of your own choosing, and provide an appropriate description.
10. Click Create Role
11. Once the Role creation is complete, open the Role and copy the Role ARN value.
12. In the OX Connector below paste the value in the field AWS Role ARN.
13. Click Connect.
14. You should receive a message that the connection was successful, if not please repeat the steps above.

#### Organization

In case you have multiple AWS accounts, this configuration is the right one for you. By connecting your AWS management account to our system we will be able to scan all of the accounts under it for vulnerabilities.

The way we do it is similar to the automatic connection (meaning we do the heavy lifting for you by creating all the assets needed), with an extra step to connect your management account with all of the accounts under it.

1. Log into your AWS console and navigate to the **CloudFormation** service.
2. Click on **StackSets** and then **Create StackSet**.
3. In the **Choose a template** page:\
   a. Under **Permissions**, select the **Service-managed permissions** option.\
   b. Under **Prerequisite – Prepare template**, make sure the **Template is ready** option is selected.\
   c. Under **Specify template**, select the **Amazon S3 URL** option.\
   d. Under **Amazon S3 URL**, paste the following link:\
   <https://ox-cloudformation-template.s3.eu-west-1.amazonaws.com/aws/ox_aws_integration_stackset_template_k8s.yml>\
   e. Click **Next**.
4. In the **Specify StackSet details** page:\
   a. Set StackSet name **ox-security** (must be unique).\
   b. Change the description if you want.\
   c. Set **External Id** – paste the **AWS External ID** generated below.\
   d. Ensure **IAMRoleName** and **OxAWSAccountId** are already filled.\
   e. Click **Next**.
5. In the **Configure StackSet options** page:\
   a. Under **Execution configuration**, make sure **Managed execution** is set to **Inactive**.\
   b. Click **Next**.
6. In the **Set deployment options** page:\
   a. Set **Add stacks to stack set** to **Deploy new stacks**.\
   b. Set **Deployment targets** to **Deploy to organization**.\
   c. Set **Automatic deployment** to **Enabled**.\
   d. Set **Account removal behavior** to **Delete stacks**.\
   e. In the **Specify regions** section, select the region your organization is in.

   > **Note:** Select only one region. Choosing multiple regions will cause the deployment to fail.\
   > f. In the **Deployment options** section, set:\
   > i. Maximum concurrent accounts – 1\
   > ii. Failure tolerance – 0\
   > iii. Region Concurrency – Sequential\
   > g. Click **Next**.
7. **Review the configuration:**\
   a. Check that everything is correct and adjust if necessary.\
   b. Check the **I acknowledge that AWS CloudFormation...** checkbox under **Capabilities**.\
   c. Click **Submit**.
8. You have now successfully deployed the StackSet.
9. Click the **Cloud Formation Assume Role** button below.
10. On the **CloudFormation** page:\
    a. Check the acknowledgment box at the bottom.\
    b. Click **Create stack**.\
    **Note:** if you already created a Cloud Formation stack for ox-security you will need to rename the stack name, otherwise it will issue an error (Stack \[ox-security] already exists).
11. Once the stack has been created, open **CloudFormation outputs**, copy the **OxRoleArn** value, and paste it in the **AWS Role ARN** below.
12. Click **Connect**.
13. You should receive a message that the connection was successful; if not, please repeat the steps above.

When using “**Service-managed permissions**” (Enabled in AWS Organizations), the parent/admin account has a stack set admin role named AWSServiceRoleForCloudFormationStackSetsOrgAdmin, while the child/target accounts have the stack set execution role named stacksets-exec-\<id>. As the name suggests, the CloudFormation service automatically adds both roles to their respective accounts to establish the trust relationship. However, this method only adds the default trust and permission policies (administrative access), and does not allow the user to customize the IAM roles when they are created. Please note that some CSPM Tools might flag this role as a violation, thus it is recommended to remove the stacksets-exec-\<id> role from the target accounts.
