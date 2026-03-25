# Source: https://docs.ghost.org/migration/kit.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.ghost.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Migrating from Kit

> Migrate from Kit and import your subscribers to Ghost with this guide

## Overview

Since Kit manages subscriptions on your behalf, there is no direct migration path to move any paid subscriptions from Kit to other platforms.

The good news: Ghost makes it possible to import all of your existing subscriber emails and give them access to premium content on your custom Ghost publication, or to sync your Kit subscribers with Ghost using an automation.

## Export your subscribers

To get started, export your current subscribers from Kit in CSV format.

<Frame>
  <img src="https://mintcdn.com/ghost/ZMdvGdmwew7ypzvu/images/7f093338-export-convertkit_huc44eb2f23f6040a066f2331419f0a0c1_32934_2336x0_resize_q100_h2_box_3.webp?fit=max&auto=format&n=ZMdvGdmwew7ypzvu&q=85&s=cb13127a1a4861e49be7f6ce8af15e20" width="2336" height="920" data-path="images/7f093338-export-convertkit_huc44eb2f23f6040a066f2331419f0a0c1_32934_2336x0_resize_q100_h2_box_3.webp" />
</Frame>

## Import subscribers to Ghost

Under the Ghost Admin members settings, select the import option from the settings menu.

<Frame>
  <img src="https://mintcdn.com/ghost/5_xpDDjqLTzEezAK/images/2f96f746-import-members-1_huc3d26abd3bec140dac4d1e5fd61f2b53_17353_1000x0_resize_q100_h2_box_3.webp?fit=max&auto=format&n=5_xpDDjqLTzEezAK&q=85&s=1f2f8d5b608e1dd8e7ac1b58960fc752" width="1000" height="167" data-path="images/2f96f746-import-members-1_huc3d26abd3bec140dac4d1e5fd61f2b53_17353_1000x0_resize_q100_h2_box_3.webp" />
</Frame>

Upload your CSV file to Ghost, and map each of the fields contained in your export file to the corresponding fields in Ghost. The **email** field is required in order to create members in Ghost, while the other fields are optional.

It’s recommended to edit your data as required before uploading your CSV file to Ghost.

Once the import has completed, all your subscribers will be migrated to Ghost. There’s nothing else you need to do, members can now log into your site and receive email newsletters.

## Running Ghost alongside Kit

It’s also possible to use Zapier or the Ghost API to keep email subscribers from Kit in sync with a Ghost membership site. This is useful if you’re giving your existing audience in Kit access to premium content on a your Ghost site as an additional perk, or if you’re accepting signups on both platforms.

To find out how to connect Ghost with Kit, check out our [integration](https://ghost.org/integrations/convertkit/).


Built with [Mintlify](https://mintlify.com).