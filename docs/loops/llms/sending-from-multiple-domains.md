# Source: https://loops.so/docs/deliverability/sending-from-multiple-domains.md

> ## Documentation Index
> Fetch the complete documentation index at: https://loops.so/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Sending from multiple domains

> The pros and cons of sending from multiple domains and how to do so in Loops

Much of the information online about email best practices is outdated. Email is a very old industry, and while filtering technology has evolved, much of the guidance still referenced has not.

In our experience, sending from a **single domain** offers far more benefits than using multiple domains. Here’s why:

1. **Consistent sender history**

   The hardest part of email sending is building and maintaining a positive sender reputation. This requires steady, high-quality sending volume over time. Splitting traffic across multiple domains fragments this history, making it much harder to maintain consistency.
2. **Avoiding weak or “cold” domains**

   When a domain is only used occasionally, say, just for product updates, it lacks a sending history. As a result, when you suddenly send a large campaign from that domain, it is far more likely to land in spam. Using a single domain avoids this problem as sending history is shared and consistent.
3. **Modern filtering methods**

   In the past, spam filtering focused heavily on the sending domain or IP address. This made splitting domains a defensive strategy in case one was blocklisted.

   Today (2025 and beyond), most inbox filtering is powered by large language models (LLMs). These systems evaluate content quality and sender reputation over time, not just the domain name. That means if you consistently send high-quality content from one well-established domain, your deliverability will be far stronger than spreading efforts across many domains.

If you do want to separate different types of communication, such as product updates vs. newsletters, we recommend using our [**Mailing List**](/contacts/mailing-lists) feature. It allows subscribers to manage their preferences and opt into specific types of emails, all from a single domain. This avoids domain fragmentation while still giving your users choice.

If you truly need to send from multiple domains, you can create a separate team in Loops and switch between them easily. Just note that settings, audience records, and other data are not shared across teams.
