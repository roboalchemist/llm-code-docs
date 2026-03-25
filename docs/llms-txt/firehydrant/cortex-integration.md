# Source: https://docs.firehydrant.com/docs/cortex-integration.md

# Cortex

Installing the Cortex integration into FireHydrant streamlines service management and incident response for organizations with complex microservice architectures. By synchronizing service and team information from Cortex to FireHydrant, teams can leverage Cortex's comprehensive service catalog while managing incidents and tracking service health within FireHydrant. This integration ensures that service ownership, team structures, and other critical metadata are consistently maintained across both platforms.

This guide outlines the process of integrating Cortex with FireHydrant, allowing you to synchronize team and service information between the two platforms.

## Prerequisites

* An active Cortex account with teams and services configured
* You will need <Glossary>Owner</Glossary> permissions to configure integrations on FireHydrant

## Installing the Cortex integration

### Generate Cortex API Key

1. Log in to your Cortex account
2. Navigate to Settings
3. Click on the "API keys" button
4. Generate a new API key with "Viewer" role permissions

<Image alt="Create API key in Cortex" align="center" width="650px" src="https://files.readme.io/451badfbc74dec8986872fe694d97afdfe720d749ad861fdb5d6c1e3dd6fea96-docus-cortex.jpg">
  Create API key in Cortex
</Image>

> 📘 Note:
>
> It's recommended to use only Viewer permissions for security purposes

### Configure FireHydrant

1. Log in to your FireHydrant account
2. Navigate to the integrations or settings section
3. Locate the Cortex integration configuration
4. Input the Cortex API key that you previously generated
5. If you're using an on-premises version of Cortex:
   * Add the appropriate endpoint in the designated field
   * For cloud-based Cortex users, leave the endpoint field blank
6. Save your changes

<Image alt="Setup Cortex in FireHydrant" align="center" width="650px" src="https://files.readme.io/9a7a49050f8c42c79578708fd249c5911aef5c5442e73e44ef78d6a0d8d8dc0f-docus-cortex-2.jpg">
  Setup Cortex in FireHydrant
</Image>

### Synchronization Process

After saving the configuration:

1. FireHydrant will automatically initiate a synchronization job
2. This job will import your Cortex teams and their associated services into FireHydrant
3. Subsequent updates in Cortex are synchronized with FireHydrant every hour

## What Gets Synchronized

* Teams from Cortex
* Services owned by each team
* Team members

<Image alt="Synchronized team and service from Cortex into FireHydrant" align="center" width="650px" src="https://files.readme.io/7d6a94e5b35b19150c46684b8d99608651c3498e39a667fe0df8b14067321816-docus-cortex-3.jpg">
  Synchronized team and service from Cortex into FireHydrant
</Image>

> 🚧 Note:
>
> FireHydrant expects user email addresses in Cortex to match with a user in FireHydrant. If a user exists in Cortex but not FireHydrant, then the user will automatically be created in FireHydrant with the email obtained from Cortex.

## FAQs

> My Cortex integration doesn't seem to be working. What are some general troubleshooting steps I can take?

1. Verify that the API key has been entered correctly
2. Ensure the API key has at least Viewer permissions in Cortex
3. For on-premises Cortex users, double-check the endpoint URL

> My new services/teams in Cortex aren't showing up in FireHydrant

FireHydrant syncs from Cortex to FireHydrant every hour at the top of the hour.