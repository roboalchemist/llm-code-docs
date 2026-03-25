# Source: https://posthog.com/docs/libraries/capacitor.md

# Capacitor - Docs

PostHog makes it easy to capture data from your Capacitor app, no matter the platform. You can find out more in the [plugin's documentation](https://capawesome.io/plugins/posthog/).

## Installation

Run the following command to install the package:

Terminal

PostHog AI

```bash
npm install @capawesome/capacitor-posthog posthog-js
```

After installing the package, you need to update your Capacitor project:

Terminal

PostHog AI

```bash
npx cap update
```

### Configuration

To use the plugin, you need to call the `setup(...)` method with your PostHog project token and host which you can find in [your project settings](https://us.posthog.com/settings/project):

TypeScript

PostHog AI

```typescript
import { Posthog } from '@capawesome/capacitor-posthog';
const setup = async () => {
  await Posthog.setup({
    apiKey: '<ph_project_token>',
    host: 'https://us.i.posthog.com',
  });
};
```

You pass in a `host` key to specify the PostHog instance you want to send events to. The default host is `https://us.i.posthog.com`.

## Capturing events

You can send custom events using `capture`:

JavaScript

PostHog AI

```javascript
await Posthog.capture({
    event: 'test-event',
});
```

> **Tip:** We recommend using a `[object] [verb]` format for your event names, where `[object]` is the entity that the behavior relates to, and `[verb]` is the behavior itself. For example, `project created`, `user signed up`, or `invite sent`.

### Setting event properties

Optionally, you can include additional information with the event by including a [properties](/docs/data/events.md#event-properties) object:

JavaScript

PostHog AI

```javascript
await Posthog.capture({
    event: 'test-event',
    properties: {
        key: 'value',
    },
});
```

## Feature flags

PostHog's [feature flags](/docs/feature-flags.md) enable you to safely deploy and roll back new features as well as target specific users and groups with them.

Feature flags are not yet supported by this library, but you can still use them [via the API](/docs/api/flags.md). If you would like to contribute, please check out the [GitHub repository](https://github.com/capawesome-team/capacitor-plugins/tree/main/packages/posthog).

## Group analytics

Group analytics enable you to associate the events for that person's session with a group (e.g. teams, organizations, etc.). Read the [group analytics docs](/docs/product-analytics/group-analytics.md) guide for more information.

> **Note:** This is a paid feature and is not available on the open-source or free cloud plan. Learn more on the [pricing page](/pricing.md).

To associate the events for this session with a group, call `group()`:

JavaScript

PostHog AI

```javascript
import { Posthog } from '@capawesome/capacitor-posthog';
const group = async () => {
  await Posthog.group({
    type: 'company',
    key: 'company_id_in_your_db',
  });
};
```

To associate the events for this session with a group **and** update the properties of that group, include the `groupProperties` property:

JavaScript

PostHog AI

```javascript
import { Posthog } from '@capawesome/capacitor-posthog';
const group = async () => {
  await Posthog.group({
    type: 'company',
    key: 'company_id_in_your_db',
    groupProperties: {
      name: 'Awesome Inc.',
    },
  });
};
```

The `name` is a special property which is used in the PostHog UI for the name of the group. If you don't specify a `name` property, the group ID will be used instead.

## Credits

This library was built by the [Capawesome team](https://capawesome.io/). It is not maintained by the PostHog core team. If you have any questions or issues, please create a discussion or an issue in the [GitHub repository](https://github.com/capawesome-team/capacitor-plugins).

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better