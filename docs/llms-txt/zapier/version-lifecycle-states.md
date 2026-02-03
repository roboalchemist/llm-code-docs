# Source: https://docs.zapier.com/platform/manage/version-lifecycle-states.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zapier.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Version lifecycle states

> Learn about the different lifecycle states an integration version can go through, including private, promoted, available, legacy, deprecating, and deprecated versions.

When you create a new integration version in Zapier, it goes through different lifecycle states. Understanding these states is crucial for managing your integration effectively. They are as follows:

* Private
* Promoted
* Available
* Legacy
* Deprecating
* Deprecated

<Frame>
  <img src="https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/d01e24e8-227f-4530-8ca7-956c5164d235.webp?fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=2c6b310070a1add4abeb7f214b308373" data-og-width="1504" width="1504" data-og-height="850" height="850" data-path="images/d01e24e8-227f-4530-8ca7-956c5164d235.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/d01e24e8-227f-4530-8ca7-956c5164d235.webp?w=280&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=b0942e25503fd5b0cc991074499190bc 280w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/d01e24e8-227f-4530-8ca7-956c5164d235.webp?w=560&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=a830128d45860242fb79afc6fc0cbbe1 560w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/d01e24e8-227f-4530-8ca7-956c5164d235.webp?w=840&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=9e1860c0d6f47e2f283d6fb937d290fe 840w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/d01e24e8-227f-4530-8ca7-956c5164d235.webp?w=1100&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=3c9a800281e9df9f78a0c5c57adc439c 1100w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/d01e24e8-227f-4530-8ca7-956c5164d235.webp?w=1650&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=3853d80f2f8cd75f612ecb71ea2ce7d3 1650w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/d01e24e8-227f-4530-8ca7-956c5164d235.webp?w=2500&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=b23f2481f50c6a3dff9f732ca2567a0f 2500w" />
</Frame>

## Private

When you first create a new integration version, it automatically starts in a **private** state. This is the default state for all new versions.

In the private state:

* Only you and your team members can access and test the version
* You can make changes and updates to this version
* You can [share the version](/platform/manage/sharing) with specific users for testing
* The version remains private until you take further action

## Promoted

If your integration is public or intended to go public, you can promote a version to make it available to all Zapier users. When a version is promoted:

* It becomes the default version for all new automations
* It is visible in the Zapier app directory (for public integrations)
* Existing Zap templates may be automatically updated to use this version
* You must always have one promoted version for public integrations
* This version is no longer editable

Important notes for promotion:

* Only one version can be promoted at a time
* When you promote a new version, the previously promoted version will be automatically demoted and be set to "Available"
* All [validation checks](/platform/publish/integration-checks-reference) must pass before promotion

## Available

If a version is promoted, the previous promoted version automatically becomes "Available".
Available versions continue to work for automations that use them.

## Legacy

A version can be marked as legacy when you no longer recommend it for new automations, but it is expected to continue working for any current automations. To set a version as legacy:

* The version must be in a private or available state
* You cannot mark a currently promoted version as legacy
* Legacy versions can still be used by existing automations but are not available for new automations

Important considerations for legacy versions:

* You cannot migrate automations to a legacy version

## Deprecating

When you mark a version as deprecated with a deprecation date, it will automatically be set to "Deprecating" until the deprecation date.
While a version is in the deprecating state, it will continue to work for existing automations, but it will not be available for new automations.

See [Deprecated](#deprecated) below for deprecation details.

## Deprecated

Deprecation is the final state in a version's lifecycle. When you deprecate a version:

* Users will be notified that they should migrate to a newer version
* The version will continue to work for a specified time period
* After the deprecation date, the version will no longer function
* You must deprecate a private, demoted or legacy version, not a currently promoted version

Important notes about deprecation:

* Set a future deprecation date to give users time to migrate
* Ensure you have a newer version available for users to migrate to
* Consider the impact on existing users before deprecating a version

See [Deprecate or delete a version](/platform/manage/deprecate) for more information.

## State Transitions

Here's how versions typically move through states:

1. **Private** - Every new version starts here, allowing you to build and test without affecting users.

2. **Promoted** - When your version is ready for public use, you promote it, making it the default for all new automations. The previously promoted version automatically becomes **Available**.

3. **Legacy** - When you release a newer version with significant improvements, you may mark older versions as legacy. These versions still function for existing automations but aren't recommended or available for new ones.

4. **Deprecating/Deprecated** - When a version will no longer be supported (e.g., due to API changes from the service provider), you deprecate it with a future end date. This gives users time to migrate their automations before the version stops working.

Remember that you must always have a promoted version if your integration is public, and you should carefully plan version transitions to minimize disruption to your users' automations.

For more information on managing versions, see:

* [Promote a version](/platform/manage/promote)
* [Migrate users to a new version](/platform/manage/migrate)
* [Deprecate or delete a version](/platform/manage/deprecate)

***

*Need help? [Tell us about your problem](https://developer.zapier.com/contact) and we'll connect you with the right resource or contact support.*
