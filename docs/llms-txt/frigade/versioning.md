# Source: https://docs.frigade.com/platform/versioning.md

# Version Control

> Manage the rollout of new Flow updates with built-in version control

## Creating a new version

***

To create a new version of your Flow, open the versions panel on the Flow detail page. Then, click the **New version** button.
The new version will remain a draft until you activate it. Frigade supports one draft version at a time. Tap **View** on a version to view and make changes.

<Frame>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/frigade-docs/images/platform/flow-detail-versions.png" alt="Versioning" />
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
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/frigade-docs/images/platform/flow-detail-versions-restart.png" alt="Transitioning users" />
</Frame>

## Old versions

***

Once a draft has been activated, old versions of the Flow become read-only. Analytics for old versions will be preserved and can be viewed by clicking the **View** button on an old version.
