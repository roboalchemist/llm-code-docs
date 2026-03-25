# Source: https://docs.jit.io/docs/troubleshooting-aws-integration.md

# AWS Integration Troubleshooting

## Overview

In the event that your AWS integration fails, follow the steps below to re-integrate.

## Re-integrating with AWS after integration failure

**To re-integrate with AWS after integration failure—**

1. Go to the repository on GitHub that contains Jit's primary configuration files, edit the `jit-integration.yml` file, and remove your AWS integration. If you have multiple AWS integrations, only remove the faulty one; otherwise, remove the entire AWS block. You can confirm that the integration has been removed from the [Integrations page](https://docs.jit.io/docs/integrations-page).
2. (Only required for organization-based integration) From the AWS console, navigate to the **StackSets** tab in **CloudFormation** and select **JitOrganizationsStacksSet**. Using the **Actions** menu, select **delete stacks from stack set**. This process may take a few minutes.
3. Navigate to the **Stacks** tab, and delete the relevant Jit stacks: for organization— *JitOrganizationsStacksSet*, for account— *JitControlsStack*.
4. To ensure successful re-integration, navigate to the IAM management console and verify that the role *JitRole* no longer exists.
5. Return to the Jit platform and perform the [integration procedure](https://docs.jit.io/docs/integrating-with-aws).