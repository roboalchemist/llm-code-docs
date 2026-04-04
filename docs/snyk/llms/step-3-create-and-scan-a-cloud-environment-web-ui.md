# Source: https://docs.snyk.io/scan-with-snyk/snyk-iac/cloud-platform-integrations/aws-integration/aws-integration-web-ui/step-3-create-and-scan-a-cloud-environment-web-ui.md

# Step 3: Create and scan a Cloud Environment (Web UI)

{% hint style="info" %}
**Recap**\
You have created the Snyk IAM role. Now you can create and scan a Cloud Environment.
{% endhint %}

To create and scan a Cloud Environment, you must provide the role’s Amazon Resource Name (ARN). Then you can finish onboarding the environment.

## Find the role ARN

The role ARN should follow this format unless you [changed the name of the role](https://docs.snyk.io/scan-with-snyk/snyk-iac/cloud-platform-integrations/aws-integration/aws-integration-web-ui/step-1-download-iam-role-iac-template-web-ui) in the Terraform or CloudFormation template:

```
arn:aws:iam::YOUR-ACCOUNT-ID:role/snyk-cloud-role
```

If you do not know your Amazon Web Services (AWS) account ID, or if you changed the name of the IAM role in the Terraform or CloudFormation template, you can find the role ARN using the [AWS CLI](#find-the-role-arn-using-the-aws-cli) or the [AWS Management Console](#find-the-role-arn-using-the-aws-management-console).

### Find the role ARN using the AWS CLI

To find the ARN of the Snyk Cloud IAM role using the AWS CLI, retrieve the role details, replacing `snyk-cloud-role` with the name of your role if you changed it:

```
aws iam get-role \
  --role-name snyk-cloud-role \
  --query 'Role.Arn' --output text
```

The output looks like this:

```
arn:aws:iam::123412341234:role/snyk-cloud-role
```

### Find the role ARN using the AWS Management Console

1. Log in to the [AWS Management Console](https://console.aws.amazon.com).
2. Navigate to [Identity and Access Management](https://console.aws.amazon.com/iamv2/home#/home).
3. In the left sidebar, select **Roles**.
4. On the **Roles** page, search for `snyk-cloud-role` or substitute the name of your role if you changed it:

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-50b1eff09ce95c39c044b69afc6530ce7d9898fb%2Fsnyk-cloud-console-find-arn.png?alt=media" alt=""><figcaption><p>Search for the name of your role in the AWS Management Console</p></figcaption></figure>

5\. Select the role.

6\. On the role details page, in the **Summary** section, find and copy the ARN:

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-481d0476ce2605ece72909a3305c5e22d24417d1%2Fsnyk-cloud-console-copy-arn.png?alt=media" alt=""><figcaption><p>Copy the role ARN in the AWS Management Console</p></figcaption></figure>

## Create and scan the AWS Environment

1. In the Snyk Web UI **Add AWS Environment** modal where you downloaded the IAM role template, enter your role ARN in the **IAM role ARN** field.
2. Optionally, enter an environment name. If one is not provided, Snyk will use your AWS account alias.
3. Select **Approve and begin scan**.
4. You will see a confirmation message: "AWS environment successfully added." Select **Add another environment** to return to the **Add AWS Environment** modal and onboard a new account, or select **Go to settings** if you are finished:

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-c327061dfc3408c56aa2436235086c08f5783a34%2Fsnyk-cloud-onboard-aws-ui-success.png?alt=media" alt=""><figcaption><p>Success message after adding an AWS environment in the Snyk Web UI</p></figcaption></figure>

## What's next?

You can now do the following:

* View the cloud configuration issues Snyk finds. See [Manage cloud issues](https://docs.snyk.io/scan-with-snyk/snyk-iac/getting-started-with-cloud-scans/manage-cloud-issues).
* Prioritize your vulnerabilities with cloud context.
