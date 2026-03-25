# Source: https://docs.rootly.com/integrations/email.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Email

> Create incidents by sending emails directly to Rootly's email integration endpoint.

## Why

**Email** Integration allows you to:

* Create incidents by sending an email.

## Installation

You can setup this integration as a **logged in admin user** in the integrations page:

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/7PwamMJIAOaYlZ7c/images/integrations/email/images-1.webp?fit=max&auto=format&n=7PwamMJIAOaYlZ7c&q=85&s=0a3f896ab34f483d62dd2532eed173f1" width="862" height="391" data-path="images/integrations/email/images-1.webp" />
</Frame>

## Create an incident

Now you should have a generated **email alias** tied to your team.

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/7PwamMJIAOaYlZ7c/images/integrations/email/images-2.webp?fit=max&auto=format&n=7PwamMJIAOaYlZ7c&q=85&s=770c05b695eb31d28acde3182a05894a" width="864" height="350" data-path="images/integrations/email/images-2.webp" />
</Frame>

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/7PwamMJIAOaYlZ7c/images/integrations/email/images-3.webp?fit=max&auto=format&n=7PwamMJIAOaYlZ7c&q=85&s=37ed3991bb561ae744ec94795879dc10" width="870" height="356" data-path="images/integrations/email/images-3.webp" />
</Frame>

Let's send our email!

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/7PwamMJIAOaYlZ7c/images/integrations/email/images-4.webp?fit=max&auto=format&n=7PwamMJIAOaYlZ7c&q=85&s=0da8f516b96985041bf00c6a4193d559" width="875" height="822" data-path="images/integrations/email/images-4.webp" />
</Frame>

## Specify a severity

Rootly will **automatically detect** the incident **severity** in the mail **subject** and map accordingly:

For example:

* *\[SEV0] Shopping cart is showing empty items* **will be mapped** to severity **SEV0** (if exist in your configuration).
* *\[SEV1] Shopping cart is showing empty items* **will be mapped** to severity **SEV1** (if exist in your configuration).
* *Shopping cart is showing empty items \[SEV0]* **will be mapped** to severity **SEV0** (if exist in your configuration).
* *Shopping cart is showing empty items, this is a sev1* **will be mapped** to severity **SEV1** (if exist in your configuration).
* *Shopping cart is showing empty items* **won't be mapped** to any severity.

## Add emails to the timeline

You can respond to an incident email and we will add it to your timeline for you !

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/7PwamMJIAOaYlZ7c/images/integrations/email/images-5.webp?fit=max&auto=format&n=7PwamMJIAOaYlZ7c&q=85&s=64cd3b11d30ff7088538ab7227d47c72" width="867" height="374" data-path="images/integrations/email/images-5.webp" />
</Frame>


Built with [Mintlify](https://mintlify.com).