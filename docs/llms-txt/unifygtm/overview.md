# Source: https://docs.unifygtm.com/reference/signals/overview.md

# Source: https://docs.unifygtm.com/reference/sequences/send-schedules/overview.md

# Source: https://docs.unifygtm.com/reference/sequences/overview.md

# Source: https://docs.unifygtm.com/reference/plays/overview.md

# Source: https://docs.unifygtm.com/reference/overview.md

# Source: https://docs.unifygtm.com/reference/notifications/overview.md

# Source: https://docs.unifygtm.com/reference/integrations/salesforce/overview.md

# Source: https://docs.unifygtm.com/reference/integrations/overview.md

# Source: https://docs.unifygtm.com/reference/integrations/orum/overview.md

# Source: https://docs.unifygtm.com/reference/integrations/nooks/overview.md

# Source: https://docs.unifygtm.com/reference/integrations/hubspot/overview.md

# Source: https://docs.unifygtm.com/reference/ai-research/overview.md

# Source: https://docs.unifygtm.com/reference/agents/overview.md

# Source: https://docs.unifygtm.com/developers/intent-client/overview.md

# Source: https://docs.unifygtm.com/reference/signals/overview.md

# Source: https://docs.unifygtm.com/reference/sequences/send-schedules/overview.md

# Source: https://docs.unifygtm.com/reference/sequences/overview.md

# Source: https://docs.unifygtm.com/reference/plays/overview.md

# Source: https://docs.unifygtm.com/reference/overview.md

# Source: https://docs.unifygtm.com/reference/notifications/overview.md

# Source: https://docs.unifygtm.com/reference/integrations/salesforce/overview.md

# Source: https://docs.unifygtm.com/reference/integrations/overview.md

# Source: https://docs.unifygtm.com/reference/integrations/orum/overview.md

# Source: https://docs.unifygtm.com/reference/integrations/nooks/overview.md

# Source: https://docs.unifygtm.com/reference/integrations/hubspot/overview.md

# Source: https://docs.unifygtm.com/reference/ai-research/overview.md

# Source: https://docs.unifygtm.com/reference/agents/overview.md

# Source: https://docs.unifygtm.com/developers/intent-client/overview.md

# Source: https://docs.unifygtm.com/reference/signals/overview.md

# Source: https://docs.unifygtm.com/reference/sequences/send-schedules/overview.md

# Source: https://docs.unifygtm.com/reference/sequences/overview.md

# Source: https://docs.unifygtm.com/reference/plays/overview.md

# Source: https://docs.unifygtm.com/reference/overview.md

# Source: https://docs.unifygtm.com/reference/notifications/overview.md

# Source: https://docs.unifygtm.com/reference/integrations/salesforce/overview.md

# Source: https://docs.unifygtm.com/reference/integrations/overview.md

# Source: https://docs.unifygtm.com/reference/integrations/orum/overview.md

# Source: https://docs.unifygtm.com/reference/integrations/nooks/overview.md

# Source: https://docs.unifygtm.com/reference/integrations/hubspot/overview.md

# Source: https://docs.unifygtm.com/reference/deliverability/overview.md

# Source: https://docs.unifygtm.com/reference/ai-research/overview.md

# Source: https://docs.unifygtm.com/reference/agents/overview.md

# Source: https://docs.unifygtm.com/developers/intent-client/overview.md

# Intent Client Overview

> Learn how to start collecting website intent data in Unify.

Buyer intent data is at the core of what makes Unify tick. The easiest way to
start collecting this data is by installing the Unify Intent client on your
marketing website or web app.

# How it works

The Unify Intent client is a JavaScript library that allows you to collect
events from your website and send them to Unify. It currently supports Page and
Identify events. Track events are coming soon.

<CardGroup cols={3}>
  <Card title="Page Events" icon="memo-pad" iconType="duotone" color="#3378B8">
    e.g. a user visits the pricing page of your marketing website
  </Card>

  <Card title="Identify Events" icon="user-check" iconType="duotone" color="#22811A">
    e.g. a user logs into your web application with their email address
  </Card>

  <Card title="Track Events (coming soon)" icon="bullseye-pointer" iconType="duotone" color="#D23434">
    e.g. a user clicks a button to open a pricing calculator modal
  </Card>
</CardGroup>

When you install the Unify Intent client on your website, it can automatically
start collecting these events and sending them to Unify. You can also customize
this behavior by sending events manually using the client's API.

The Unify Intent client is fully open source and available on [GitHub](https://github.com/unifygtm/intent-js-client).

# Installation

There are several different ways to install the Unify Intent client on your
website. Choose the one that best suits your use case:

<CardGroup cols={1}>
  <Card title="Website Tag" icon="code" iconType="duotone" href="/developers/intent-client/website-tag" horizontal>
    Quickly set up the Unify Intent client on a static marketing website.
  </Card>

  <Card title="React Library" icon="react" iconType="solid" color="#4AB8D4" href="/developers/intent-client/react" horizontal>
    Install the Unify Intent client in a React app.
  </Card>

  <Card title="JavaScript Client" icon="square-js" iconType="solid" color="#E2CD3E" href="/developers/intent-client/js-client" horizontal>
    Install the Unify Intent client in a different frontend web application
    framework.
  </Card>
</CardGroup>

If you aren't sure, we recommend starting with the **Website Tag** installation
method. This is the simplest way to get started and all you need for most
marketing websites.

# Usage

If you install the client using the **React Library** or **JavaScript Client**
methods, see our [Usage Guide](/developers/intent-client/client-spec) to learn
how to use the client and start adding events.
