# Source: https://loops.so/docs/deliverability/sending-reputation.md

> ## Documentation Index
> Fetch the complete documentation index at: https://loops.so/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Building your sender reputation

> Understanding how to build your sender reputation.

This is a high-level guide, mostly based on our experience as the makers of Loops. We're going to touch on some industry terms and best practices, but ultimately we're focusing on how successful SaaS companies have built their sender reputation using Loops.

You might be reading this guide because you're trying to understand if migrating to Loops and changing your domain is a good idea, if you need to warm up your IP or domain, or if you're just curious about how it all works.

Your sender reputation, as defined by us, is a calculated value based on your domain and your sending IP. This calculation also considers factors like engagement rates, sending volume, and email content quality. We reference this throughout our documentation, and in our support chats, so it's important to understand how it works.

Email clients, such as Gmail, Outlook, and others, also judge sender reputation using largely opaque algorithms. Each factor, such as engagement rates and sending consistency, contributes to whether your email will be successfully delivered.

## Sending Domain

Your domain is the url (e.g., example.com) that you use to send emails. For example, [chris@loops.so](mailto:chris@loops.so) is my personal email address, but we send from [chris@mail.loops.so](mailto:chris@mail.loops.so). Using a subdomain like 'mail.loops.so' is part of our best practice and is also what we would refer to as your sending domain.

A key rule in email sending is that a domain with a strong sending history—consistent volume and high engagement—helps your sender reputation. Conversely, a domain with a weak history can harm it. This can be frustrating when trying to improve your reputation, but if your current sender reputation is good, there’s no need to change your domain.

Changing domains or IP addresses can lead to a reset of your sender reputation, requiring you to rebuild your score from scratch.

This process can be risky and time-consuming, often without significant benefit if your current sender reputation is strong. It’s generally advisable to stick with your existing domain and IP unless you're facing significant deliverability issues.

Other factors can also play a role:

* The volume of emails you send
* The type of content you send
* The users receiving your emails

Beyond that, factors like your subdomain, your domain's age, and even the TLD of the domain matter because they contribute to the perceived trustworthiness of your emails.

## Sending IP

Your IP reputation is largely based on its sending history. If you send from an IP that has a strong sending history, it will help your sender reputation. If you send from an IP that has a weak sending history, it will hurt your sender reputation. Additionally, factors like email frequency, volume, content quality, and recipient engagement play important roles.

If you change either your domain or IP, your sender reputation will need to be rebuilt, which requires following best practices and potentially reducing email volume until a strong reputation is established.

Keep in mind that your sender reputation is made up of both your domain and IP.

## Wrapping Up

Follow the best practices listed in our docs, send relevant content to engaged users, and maintain a consistent sending volume to keep your reputation strong.

If you're starting fresh, consider using a subdomain for sending emails and keep your sending volume conservative initially.

For any questions, just ping [chris@loops.so](mailto:chris@loops.so).

## Read more

<CardGroup>
  <Card title="Improve your inbox placement" icon="inbox" href="/deliverability/improving-inbox-placement" />

  <Card title="Understand email open rates" icon="envelope-open-text" href="/deliverability/understanding-email-open-rates" />

  <Card title="Delivery optimization" icon="chart-line" href="/deliverability/optimization" />
</CardGroup>
