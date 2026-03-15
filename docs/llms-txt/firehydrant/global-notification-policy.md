# Source: https://docs.firehydrant.com/docs/global-notification-policy.md

# Global Notification Policy

It's important to make sure your on-call engineers are able to be paged when the unexpected happens. Notification policy enforcement is a feature of FireHydrant to define what your on-call engineers must have configured to be considered "**compliant**"

## Setting up a policy

<Image align="center" border={false} width="650px" src="https://files.readme.io/8d37a65165307a63916562e0be2828b916a89693c80b4fa7789e63129fec64bd-image.png" />

1. Navigate to **Signals** > **Global Notification Policy**.
2. The policies are split into the priority levels on FireHydrant alerts: High, Medium, and Low. Any notification methods and timings you define here will be matched against what individual users have configured in their profile settings.
3. To add a new requirement, click "+ Add step" under any category, select a notification type, and then the delay. When you click "Save", the changes apply immediately.

## Viewing a user's compliance

Users with elevated permissions can view a list of all users and whether or not they comply with their organization's policy.

<Image align="center" border={false} width="650px" src="https://files.readme.io/71d9a4f08d0011cced50932ea63f84526be7016197d4670c622392cb8cc7ca38-CleanShot_2025-07-01_at_13.33.492x.png" />

To view the missing preferences (or mistimed ones), you can click the name of the user (or "Out of compliance") as well. We'll display the user's preferences, and what is missing from the policy.

<Image align="center" border={false} width="400px" src="https://files.readme.io/4333b3afa38a02a082adf8fc7a57741da350c046e900b7733cfa9c07cab4d623-CleanShot_2025-07-01_at_13.37.272x.png" />

<br />