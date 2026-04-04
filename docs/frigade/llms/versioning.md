# Source: https://docs.frigade.com/platform/versioning.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.frigade.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Version Control

> Manage the rollout of new Flow updates with built-in version control

## Creating a new version

***

To create a new version of your Flow, open the versions panel on the Flow detail page. Then, click the **New version** button.
The new version will remain a draft until you activate it. Frigade supports one draft version at a time. Tap **View** on a version to view and make changes.

<Frame>
  <img src="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-versions.png?fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=1e70232b5fd3e693c31acfcc1b2eb902" alt="Versioning" data-og-width="3013" width="3013" data-og-height="1718" height="1718" data-path="images/platform/flow-detail-versions.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-versions.png?w=280&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=cd6a3874acbf230f0c4d0d328998165e 280w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-versions.png?w=560&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=89387955b4eb9246e1f8e89d23819957 560w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-versions.png?w=840&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=8bf42358bf316a4fccb578e08ab09733 840w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-versions.png?w=1100&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=ba60cbb46bde545cb678cbb02779c108 1100w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-versions.png?w=1650&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=355d0db45c96ab5b35ccc5da6220178d 1650w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-versions.png?w=2500&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=9ae2120c68617a60bbb9aae764a57656 2500w" />
</Frame>

## Activating a draft version

***

Once your draft version is ready to go live, click **Activate** to publish it. If there are existing users in your Flow, you will have a choice on how to transition users:

<AccordionGroup>
  <Accordion title="Restart in-progress users in new version">
    This option will restart all users currently in the Flow in the new version. Users who have already completed the Flow will not see the new version.
  </Accordion>

  <Accordion title="Exit in-progress users from the Flow">
    This option will exit all users currently in the Flow. Only new users who enter the Flow moving forward will see the new version.
  </Accordion>

  <Accordion title="Restart all users in new version">
    This option will restart all users in the Flow in the new version regardless of their state. This means that users who have already completed the Flow will also see the new version, too.
  </Accordion>
</AccordionGroup>

<Frame>
  <img src="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-versions-restart.png?fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=4fc4bcf053d618a4a9081b632eb6ff61" alt="Transitioning users" data-og-width="3008" width="3008" data-og-height="1720" height="1720" data-path="images/platform/flow-detail-versions-restart.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-versions-restart.png?w=280&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=22dbfec271757a01f1a787d7776f654a 280w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-versions-restart.png?w=560&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=603451fb860f5c7c8390233e5ba664cc 560w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-versions-restart.png?w=840&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=a4ecc2e2ea5a5e6f212eec48182a004c 840w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-versions-restart.png?w=1100&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=edecfd836828cd03a0b5a28586c20e50 1100w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-versions-restart.png?w=1650&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=47b966a865868bf6060915c49a4e7b31 1650w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-versions-restart.png?w=2500&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=ea237dfc003622a5c43f759285069aa2 2500w" />
</Frame>

## Old versions

***

Once a draft has been activated, old versions of the Flow become read-only. Analytics for old versions will be preserved and can be viewed by clicking the **View** button on an old version.
