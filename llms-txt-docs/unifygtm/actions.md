# Source: https://docs.unifygtm.com/reference/plays/actions.md

# Play Actions

> Actions are the building blocks of Unify Plays.

## Overview

Plays chain together actions to perform anything from simple automations to
complex and dynamic outbound campaigns. Below are the actions you can choose
from when creating a Play.

## Core actions

### AI qualification

AI agents are powerful tools for researching companies or people and answering
questions about them. In Plays, the answers provided by an agent can be used to
determine whether a company or person is qualified or not.

When you select the agent qualification action, you will be able to choose an
existing agent or create a new one. Every agent has a set of questions that it
will answer about the given record. In the action configuration panel, you can
select which answers are required for the record to be considered qualified.

<Frame caption="The configuration for an agent action.">
  <img src="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/ai-agent-qualification-action.png?fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=ae13f5e001b11b7500a6fcb0e3563515" data-og-width="2880" width="2880" data-og-height="2048" height="2048" data-path="images/reference/plays/ai-agent-qualification-action.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/ai-agent-qualification-action.png?w=280&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=6c6e75de0cac43f95ec2480944e6d6e5 280w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/ai-agent-qualification-action.png?w=560&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=a5d665f93a5d6dcbf87f010876f05002 560w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/ai-agent-qualification-action.png?w=840&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=2b480c2af9001e5b99ca790c054599d0 840w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/ai-agent-qualification-action.png?w=1100&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=6bb7120518b6389e859b2bf535a63d62 1100w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/ai-agent-qualification-action.png?w=1650&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=a33ab414ab9352d5d25aa0b434fb3814 1650w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/ai-agent-qualification-action.png?w=2500&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=6ccc3b038d6111f94c6a3f1baf4df75a 2500w" />
</Frame>

### Assign owner

The owner assignment action allows you to assign a record to a specific owner in
Unify. Every company and person record in Unify has an owner, and this action
allows you to set or change the owner of a record.

<Frame caption="The configuration for an assign owner action.">
  <img src="https://mintcdn.com/unify-19/MyP9qE51P6xDuum4/images/reference/plays/actions/assign-owner-action.png?fit=max&auto=format&n=MyP9qE51P6xDuum4&q=85&s=241efecb2718679e70d2d3bc25a601ae" data-og-width="2880" width="2880" data-og-height="2048" height="2048" data-path="images/reference/plays/actions/assign-owner-action.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/MyP9qE51P6xDuum4/images/reference/plays/actions/assign-owner-action.png?w=280&fit=max&auto=format&n=MyP9qE51P6xDuum4&q=85&s=f7e6187ed7b447c70ddb52356f6d446a 280w, https://mintcdn.com/unify-19/MyP9qE51P6xDuum4/images/reference/plays/actions/assign-owner-action.png?w=560&fit=max&auto=format&n=MyP9qE51P6xDuum4&q=85&s=20fe9b79869563cb7d4f926e78a2b9a2 560w, https://mintcdn.com/unify-19/MyP9qE51P6xDuum4/images/reference/plays/actions/assign-owner-action.png?w=840&fit=max&auto=format&n=MyP9qE51P6xDuum4&q=85&s=31a10c55b9163de8a869d1527a3f90e8 840w, https://mintcdn.com/unify-19/MyP9qE51P6xDuum4/images/reference/plays/actions/assign-owner-action.png?w=1100&fit=max&auto=format&n=MyP9qE51P6xDuum4&q=85&s=91615bfcb17d2961810c73f28494336d 1100w, https://mintcdn.com/unify-19/MyP9qE51P6xDuum4/images/reference/plays/actions/assign-owner-action.png?w=1650&fit=max&auto=format&n=MyP9qE51P6xDuum4&q=85&s=cda13b27155238d5d2d00d8adcff8497 1650w, https://mintcdn.com/unify-19/MyP9qE51P6xDuum4/images/reference/plays/actions/assign-owner-action.png?w=2500&fit=max&auto=format&n=MyP9qE51P6xDuum4&q=85&s=3e754e5f4ec7257534101836a685b671 2500w" />
</Frame>

When you connect a CRM to Unify, the owner of the corresponding records in the
CRM will be synced into Unify. For records that don't yet have an owner or don't
yet exist in the CRM, you can use this action to assign an owner. You can also
choose to update the owner if desired.

### Prospect

One of the most common use cases for Plays is to find new people to reach out
to. The prospecting action takes a company record as input and finds new people
at the company matching specific personas and criteria.

When you select the prospecting action, you can specify one or more personas to
search for. The personas are considered in order, so the first persona will be
preferred over the second, and so on.

<Frame caption="The configuration for a prospecting action.">
  <img src="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/prospect-for-people-action.png?fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=cdf115e4f29086a6afd0f0987d3dcdc5" data-og-width="2880" width="2880" data-og-height="2048" height="2048" data-path="images/reference/plays/prospect-for-people-action.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/prospect-for-people-action.png?w=280&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=8ed8122b0527b0c3f6ab8f4115405d01 280w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/prospect-for-people-action.png?w=560&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=89c7177cf547bca510be40851d41ac60 560w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/prospect-for-people-action.png?w=840&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=85602b0d1ab14f2d61e835f00c0aa8e5 840w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/prospect-for-people-action.png?w=1100&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=1022f088bda1a428784cade350923ddb 1100w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/prospect-for-people-action.png?w=1650&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=80ea4f009983525ff923898c150e104a 1650w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/prospect-for-people-action.png?w=2500&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=be09c0c6438ceb3184d7a64b4678ffe1 2500w" />
</Frame>

You can also specify a limit on the number of people to find per company. If the
**Include existing people** option is enabled, existing people at the company
already in Unify will count towards this limit. This can be useful if you want
to save prospecting credits on companies you already have relevant contacts for.

### Sequence

The sequence enrollment action makes building automated outbound campaigns
easier than ever. You can choose which sequences to send people to based on
which personas they match.

<Frame caption="The configuration for an sequence enrollment action.">
  <img src="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/sequence-enrollment-action.png?fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=1b5d3852b0b12dc65e30b9cd7ed6ad51" data-og-width="2880" width="2880" data-og-height="2048" height="2048" data-path="images/reference/plays/sequence-enrollment-action.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/sequence-enrollment-action.png?w=280&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=c7b2d1bfcb3c6e146d0155d5b220c96c 280w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/sequence-enrollment-action.png?w=560&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=aae9877c386d1ed79c333a0f35cab8f1 560w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/sequence-enrollment-action.png?w=840&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=a06e8690ce9e30895d90844bcbb222ce 840w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/sequence-enrollment-action.png?w=1100&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=30cae8d0624e827b01121be4808794a9 1100w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/sequence-enrollment-action.png?w=1650&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=dc475a4e95775b2b303e9c764cd80e8c 1650w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/sequence-enrollment-action.png?w=2500&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=71f1ad0f8ab6917c243068da63acc00a 2500w" />
</Frame>

The routing configuration provides a way to specify which mailboxes and
sequences should be used for people this action runs on. You can specify a
set of mailboxes to use or choose to use a mailbox associated with the [company
or person record owner](/reference/plays/actions#assign-owner-action).

<Frame caption="The routing configuration for a sequence enrollment action.">
  <img src="https://mintcdn.com/unify-19/MyP9qE51P6xDuum4/images/reference/plays/actions/sequence-enrollment-action-routing.png?fit=max&auto=format&n=MyP9qE51P6xDuum4&q=85&s=90333760d59b78640f562e1cd5701d24" data-og-width="2880" width="2880" data-og-height="2048" height="2048" data-path="images/reference/plays/actions/sequence-enrollment-action-routing.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/MyP9qE51P6xDuum4/images/reference/plays/actions/sequence-enrollment-action-routing.png?w=280&fit=max&auto=format&n=MyP9qE51P6xDuum4&q=85&s=eea09adac7e723f93374c8169504d327 280w, https://mintcdn.com/unify-19/MyP9qE51P6xDuum4/images/reference/plays/actions/sequence-enrollment-action-routing.png?w=560&fit=max&auto=format&n=MyP9qE51P6xDuum4&q=85&s=c716166a7e7b6dbd62faeee62898deae 560w, https://mintcdn.com/unify-19/MyP9qE51P6xDuum4/images/reference/plays/actions/sequence-enrollment-action-routing.png?w=840&fit=max&auto=format&n=MyP9qE51P6xDuum4&q=85&s=3e5a27e0c59ce240e9001fa0a3acf6a1 840w, https://mintcdn.com/unify-19/MyP9qE51P6xDuum4/images/reference/plays/actions/sequence-enrollment-action-routing.png?w=1100&fit=max&auto=format&n=MyP9qE51P6xDuum4&q=85&s=4848b55de15584a80757e3eb784f0e64 1100w, https://mintcdn.com/unify-19/MyP9qE51P6xDuum4/images/reference/plays/actions/sequence-enrollment-action-routing.png?w=1650&fit=max&auto=format&n=MyP9qE51P6xDuum4&q=85&s=d7702690348026a55eaeef086d7f8d07 1650w, https://mintcdn.com/unify-19/MyP9qE51P6xDuum4/images/reference/plays/actions/sequence-enrollment-action-routing.png?w=2500&fit=max&auto=format&n=MyP9qE51P6xDuum4&q=85&s=183776511118dc8ff3e92ca95feaece8 2500w" />
</Frame>

You also have the option to set a limit on how many people to enroll per
company, which is generally recommended to avoid overtargeting a single company.
This limit applies globally across play runs, so if multiple Plays run on the
same company, this limit will be shared across all of them.

### Slack alert

The Slack alert action allows you to send a customized Slack message at any
point in a Play. You can send messages to any public channels or DM any users in
your workspace.

<Frame caption="The configuration for a Slack alert action.">
  <img src="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/slack-alert-action.png?fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=14bf74a7d4b2f7c74e3f0e08a911591b" data-og-width="2304" width="2304" data-og-height="1639" height="1639" data-path="images/reference/plays/slack-alert-action.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/slack-alert-action.png?w=280&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=505cbd1557634e7e5ec57c60136930de 280w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/slack-alert-action.png?w=560&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=2263b06235fe83b4638abd810a6253bf 560w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/slack-alert-action.png?w=840&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=c79abd0edb48f14903b552709e629308 840w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/slack-alert-action.png?w=1100&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=75e0956f1a36707faab6d7a938c525d0 1100w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/slack-alert-action.png?w=1650&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=1c5daf22f8547f8d01cd253cf520f6f6 1650w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/slack-alert-action.png?w=2500&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=7eba5f36bc4016b3263cd0bba4f74881 2500w" />
</Frame>

The contents of the messages can be customized with template variables, so you
can include information about the record that triggered the action.

<Note>
  If the value for a template variable is missing, the message will still be sent,
  but the variable will be replaced with `Unknown`.
</Note>

You may optionally tag the owner of the account (e.g. `@John Doe`), so they can
be easily notified of the alert. You can also include intent signal information
containing recent website visitors, G2 page views, and more.

This action is available when Slack connected to Unify. See the [Slack Integration Guide](/reference/integrations/slack)
for information on integrating Slack with Unify.

### Sync to HubSpot

The HubSpot sync action allows you to create or update a record in HubSpot based
on a company or person record in Unify. This action will use the settings you've
configured for HubSpot in the Unify settings.

You also have the option to specify additional default field values. These will
be written to HubSpot unless a different Unify field is already mapped to the
HubSpot field.

<Frame caption="The configuration for a HubSpot sync action.">
  <img src="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/sync-to-hubspot-action.png?fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=f621f35815f62e850ca80e55f4443364" data-og-width="2880" width="2880" data-og-height="2048" height="2048" data-path="images/reference/plays/sync-to-hubspot-action.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/sync-to-hubspot-action.png?w=280&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=9825e826601053748d87d9de59d7e0f5 280w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/sync-to-hubspot-action.png?w=560&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=20d0bc07a5b05a115441faa323c1082b 560w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/sync-to-hubspot-action.png?w=840&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=041ec6ccbdaa35058aad35e148b6cf34 840w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/sync-to-hubspot-action.png?w=1100&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=f54849a5b3d7de68afef3fe32e296913 1100w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/sync-to-hubspot-action.png?w=1650&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=012298f9c0a85c1a517159a3ed35e6eb 1650w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/sync-to-hubspot-action.png?w=2500&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=80594bc4970af042e2e2ec74b440d803 2500w" />
</Frame>

### Sync to Salesforce

The Salesforce sync action allows you to create or update a record in Salesforce
based on a company or person record in Unify. This action will use the settings
you've configured for Salesforce in the Unify settings.

You also have the option to specify additional default field values. These will
be written to Salesforce unless a different Unify field is already mapped to the
Salesforce field.

<Frame caption="The configuration for a Salesforce sync action.">
  <img src="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/sync-to-salesforce-action.png?fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=8f10439466d6f16b8241a250fefca8a4" data-og-width="2880" width="2880" data-og-height="2048" height="2048" data-path="images/reference/plays/sync-to-salesforce-action.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/sync-to-salesforce-action.png?w=280&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=720643418a4794f35560eb724531eaaa 280w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/sync-to-salesforce-action.png?w=560&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=b7d432d3c2077e0739f4a061694529bb 560w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/sync-to-salesforce-action.png?w=840&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=35a75ba86229884c8afe9098e89a7460 840w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/sync-to-salesforce-action.png?w=1100&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=480e4d11717e82ab6b7217365a0ba9d4 1100w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/sync-to-salesforce-action.png?w=1650&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=3e55ede04afce22bdab8baa3005f9b0b 1650w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/sync-to-salesforce-action.png?w=2500&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=77eb4e5d5e2e48fe891d1a78e41e334a 2500w" />
</Frame>

## Utility actions

### Loop

<Note>
  In order to fully understand the purpose of loops and how to use them
  effectively, it's recommended that you read about action [inputs and outputs](/reference/plays/building-a-play#inputs-and-outputs) first.
</Note>

Most actions run on one record at a time. Loops are a simple way to run one or
more actions on every record in a list.

For example, a **Prospect for new People** action will return a list of people.
You can connect a loop action to the prospecting action and then add actions
within the loop. The first action in the loop will receive one person at a time.

### If / Else

The if-else action creates a branch in a Play, evaluates some conditions for
records, and sends them down a specific path based on the result. This allows
you to perform different actions on different records based on criteria that you
specify.

<Frame caption="The branch created by an if-else action in a Play.">
  <img src="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/if-else-action.png?fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=6e5ecbd41ecd17ae34dc1b98665cc3a2" data-og-width="2880" width="2880" data-og-height="2048" height="2048" data-path="images/reference/plays/if-else-action.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/if-else-action.png?w=280&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=c93964321c4134bddc9da21447ea2377 280w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/if-else-action.png?w=560&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=83db77977ed3077ca874d2b0adda6ae0 560w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/if-else-action.png?w=840&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=650061bb55f4b6a7126f337dfc1828e8 840w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/if-else-action.png?w=1100&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=9a784963a3528229f4a442a41a9a4383 1100w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/if-else-action.png?w=1650&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=dd573137658adf0eae57e5c03e79726a 1650w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/if-else-action.png?w=2500&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=1adf6d638fe085769bb1404a69043bbf 2500w" />
</Frame>

This action enables you to solve a wide variety of more complex use cases using
Plays. For example, you can enroll people into different sequences based on
their company firmographics, exact job title, or custom CRM field values.

### A/B Test

The A/B test action allows you to route records down a specific path based on a set probability.
This is useful for testing different sequences or actions.

<Frame caption="The branch created by an A/B test action in a Play.">
  <img src="https://mintcdn.com/unify-19/MyP9qE51P6xDuum4/images/reference/plays/actions/ab-test-action.png?fit=max&auto=format&n=MyP9qE51P6xDuum4&q=85&s=f63444050b67c693f47c36a5b78f3ccd" data-og-width="2880" width="2880" data-og-height="2048" height="2048" data-path="images/reference/plays/actions/ab-test-action.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/MyP9qE51P6xDuum4/images/reference/plays/actions/ab-test-action.png?w=280&fit=max&auto=format&n=MyP9qE51P6xDuum4&q=85&s=4c8625d2c4dfa8c249adcafbb9c0cad4 280w, https://mintcdn.com/unify-19/MyP9qE51P6xDuum4/images/reference/plays/actions/ab-test-action.png?w=560&fit=max&auto=format&n=MyP9qE51P6xDuum4&q=85&s=ccc851d8662083b1efaeb74c2a0d4216 560w, https://mintcdn.com/unify-19/MyP9qE51P6xDuum4/images/reference/plays/actions/ab-test-action.png?w=840&fit=max&auto=format&n=MyP9qE51P6xDuum4&q=85&s=2cdf8c1d984cd05ef9f5137ad431cd90 840w, https://mintcdn.com/unify-19/MyP9qE51P6xDuum4/images/reference/plays/actions/ab-test-action.png?w=1100&fit=max&auto=format&n=MyP9qE51P6xDuum4&q=85&s=907017a18c2426add57f331952413d66 1100w, https://mintcdn.com/unify-19/MyP9qE51P6xDuum4/images/reference/plays/actions/ab-test-action.png?w=1650&fit=max&auto=format&n=MyP9qE51P6xDuum4&q=85&s=ecb4be051168d36ad0246488c6c93fb2 1650w, https://mintcdn.com/unify-19/MyP9qE51P6xDuum4/images/reference/plays/actions/ab-test-action.png?w=2500&fit=max&auto=format&n=MyP9qE51P6xDuum4&q=85&s=69cd2bba618fa4243432729f08e57f41 2500w" />
</Frame>

### Delay

The Delay action waits for a specified amount of time before continuing to the
next action in a Play. This can be useful for spacing out actions in a Play and
ensuring that actions are performed at the right time.

<Frame caption="You can customize the amount of time to wait before the next action.">
  <img src="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/delay-action.png?fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=b7884bf007fb2519a3308b3291e13961" data-og-width="2304" width="2304" data-og-height="1639" height="1639" data-path="images/reference/plays/delay-action.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/delay-action.png?w=280&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=4a5018ca59f685324dcefbe2eb2ee997 280w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/delay-action.png?w=560&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=ded13504affdc8118dca88fd75ddb606 560w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/delay-action.png?w=840&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=96469084c423ebf4ed3f222c20a70db0 840w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/delay-action.png?w=1100&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=900d4337940335212f29b7a9fa41884e 1100w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/delay-action.png?w=1650&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=71cdca69756ac257d742dc1679834000 1650w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/delay-action.png?w=2500&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=7557c2a42ddf75c799a79fc005636890 2500w" />
</Frame>

This action is particularly useful when combined with if-else actions. For
example, when a person visitors your website, it can be useful to wait a few
minutes before taking action to see which pages they end up visitor or whether
they fill out a form.

### Get Company

If you have a person record, you can use this action to fetch the company that
the person works at. If the person does not have a company associated with them,
this action will not return any result.

### Get People

If you have a company record, you can use this action to fetch people that work
at the company. Unlike the **Prospect for new People** action, this action only
looks for people that already exist in Unify rather than prspect for new people.

## Coming soon

There are lots of additional actions in the works including more powerful AI
features and deep integrations with third-party tools. If you're interested in
an action that isn't available yet, [let us know](mailto:support@unifygtm.com)!
We'll get you in the beta as soon as it's ready.
