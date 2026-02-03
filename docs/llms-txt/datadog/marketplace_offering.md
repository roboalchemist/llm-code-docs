# Source: https://docs.datadoghq.com/developers/integrations/marketplace_offering.md

---
title: Build a Marketplace Offering
description: Learn about the Datadog marketplace.
breadcrumbs: Docs > Developers > Datadog Integrations > Build a Marketplace Offering
---

# Build a Marketplace Offering

## Overview{% #overview %}

The [Datadog Marketplace](https://app.datadoghq.com/marketplace) is a digital marketplace where Technology Partners can list their paid offerings to Datadog users.

While the **Integrations** page includes integrations built by both Datadog and Technology Partners at no cost, the **Marketplace** page is a commercial platform for Datadog customers and Technology Partners to buy and sell a variety of offerings, including Agent-based or API-based integrations, software licenses, and professional services.

{% image
   source="https://datadog-docs.imgix.net/images/developers/marketplace/marketplace_overview.d988e306869e4fb334ab08f95a48a8f5.png?auto=format"
   alt="The Datadog Marketplace page" /%}

## List an offering{% #list-an-offering %}

The following types of offerings are supported on the Datadog Marketplace:

{% dl %}

{% dt %}
Integrations
{% /dt %}

{% dd %}
Marketplace integrations that submit third-party data to (or pull data from) a user's Datadog account through the [Datadog Agent](https://docs.datadoghq.com/developers/integrations/agent_integration) or the [Datadog API](https://docs.datadoghq.com/developers/integrations/api_integration). These integrations can contain a variety of data types, such as metrics, events, logs, traces, and more.
{% /dd %}

{% dt %}
Software licenses
{% /dt %}

{% dd %}
Software licenses enable you to deliver and license software solutions to customers through the Datadog Marketplace.
{% /dd %}

{% dt %}
Professional services
{% /dt %}

{% dd %}
Professional services enable you to offer your team's services for implementation, support, or management for a set period of time.
{% /dd %}

{% /dl %}

## Join the Datadog Marketplace{% #join-the-datadog-marketplace %}

Marketplace Partners have unique benefits that are not available to Technology Partners who list out-of-the-box integrations:

- **Go-to-market collaboration** including a blog post, a quote for a press release, and social media amplification, with access to dedicated sales and marketing resources focused on accelerating partner growth.
- **Training and support** for internal sales enablement.
- **Exclusive opportunities to sponsor** conferences and events (such as [Datadog DASH](https://www.dashcon.io/)) at a discounted rate.
- **Generate new leads** from user discovery.

## Join the Datadog partner network{% #join-the-datadog-partner-network %}

Before listing an offering on the Datadog Marketplace, you first need to apply to the [Datadog Partner Network's](https://partners.datadoghq.com/) **Technology Partner** track. Once your application has been approved, you can begin developing your offering.

## Request a sandbox account{% #request-a-sandbox-account %}

All Technology Partners can request a dedicated Datadog sandbox account to aid in their development.

To request a sandbox account:

1. Login to the [Datadog Partner Portal](https://partners.datadoghq.com/English/).
1. On your personal homepage, click on the **Learn More** button under **Sandbox Access**.
1. Select **Request Sandbox Upgrade**.

{% alert level="info" %}
If you are already a member of a Datadog organization (including a trial org), you may need to switch to your newly created sandbox. For more information, see the [Account Management documentation](https://docs.datadoghq.com/account_management/org_switching/).
{% /alert %}

Creating a developer sandbox may take up to one or two business days. Once your sandbox is created, you can [invite new members from your organization](https://docs.datadoghq.com/account_management/users/#add-new-members-and-manage-invites) to collaborate with.

## Request access to Marketplace{% #request-access-to-marketplace %}

To request access to the private Marketplace repository, email [marketplace@datadoghq.com](mailto:marketplace@datadoghq.com). Once you have been granted access, you can review an [example pull request](https://github.com/DataDog/marketplace/pull/107) in the Marketplace repository with annotations and best practices.

## Coordinate go-to-market (GTM) opportunities{% #coordinate-go-to-market-gtm-opportunities %}

Once a Marketplace tile is live, Technology Partners can meet with Datadog's Partner Marketing team to coordinate a joint go-to-market (GTM) strategy, which includes the following:

- A Datadog quote for partner press releases
- A blog post on the [Datadog Monitor](https://www.datadoghq.com/blog/)
- Amplification of social media posts

## Get started{% #get-started %}

To get started with creating an integration, see [Build an Integration with Datadog](https://docs.datadoghq.com/developers/integrations/build_integration/).

## Further reading{% #further-reading %}

- [Datadog Partner Network](https://www.datadoghq.com/partner/)
- [Expand your monitoring reach with the Datadog Marketplace](https://www.datadoghq.com/blog/datadog-marketplace/)
- [Create an integration](https://docs.datadoghq.com/developers/integrations/)
- [Create an Agent-based Integration](https://docs.datadoghq.com/developers/integrations/agent_integration)
