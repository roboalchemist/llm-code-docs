# Source: https://braintrust.dev/docs/core/organizations.md

# Organizations

> Organizations overview and settings

Organizations in Braintrust represent a collection of projects and users. Most commonly, an organization is a business or team. You can create multiple organizations to organize your projects and collaborators in different ways, and a user can be a member of multiple organizations.

Each organization has settings than can be customized by navigating to **Settings** > **Organization**. You can also customize organization settings using the [API](/api-reference).

## Members

In the **Members** section, you can see all members of your organization and manage their roles and permissions. You can also invite new members by selecting **Invite member** and inputting their email address(es). Each member must be assigned a permission group.

## Permission groups

Permission groups are the core of Braintrust's access control system, and are collections of users that can be granted specific permissions. In the **Permission groups** section, you can find existing and create new permission groups. For more information about permission groups, see the [access control guide](/guides/access-control).

## API keys

In the **API keys** section, you can create and manage your Braintrust API keys. If you're an organization owner, you can also manage API keys for everyone in your organization. API keys are scoped to the organization and inherit permissions from the person who created them.

## Service tokens

In the **Service tokens** section, you can create and manage service accounts and service tokens suitable for system integrations. Service accounts are not tied to users and can be assigned granular permissions.

## AI providers

Braintrust supports most AI providers through the [AI proxy](/guides/proxy), which allows you to use any of the [supported models](/guides/proxy#supported-models). In the **AI providers** section, you can configure API keys for the AI providers on behalf of your organization, or add custom providers.

### Custom AI providers

You can also add custom AI providers. Braintrust supports custom models and endpoint configuration for all providers.

## Environment variables

Environment variables are secrets that are scoped to all functions (prompts, scorers, and tools) in a specific organization. You can set environment variables in the **Env variables** section by saving the key-value pairs.

## API URL

If you are self-hosting Braintrust, you can set the API URL, proxy URL, and real-time URL in your organization settings. You can also find the test commands (with token) for test pinging the API, proxy, and realtime from the command line. For more information about self-hosting Braintrust, see the [self-hosting guide](/guides/self-hosting).

## Git metadata

In the **Logging** section, you can select which git metadata fields to log, if any.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://braintrust.dev/docs/llms.txt