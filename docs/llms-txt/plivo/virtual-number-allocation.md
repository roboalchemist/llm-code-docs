# Source: https://plivo.com/docs/number-masking/concepts/virtual-number-allocation.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Virtual Number Allocation

> Learn how virtual numbers are allocated for number masking sessions and how to calculate the inventory you need.

## Virtual number allocation

The Number Masking API allocates one virtual number from your account for each session and maintains this mapping for the duration of the session. Plivo optimizes virtual number allocation to consume the least possible number of virtual numbers across several sessions.

A single virtual number can host several thousand sessions and interactions. Hosting several sessions on a virtual number does not impact the quality of the phone calls, as the phone number is only an identifier. The actual call media flows through dedicated calling channels for each parallel interaction.

### Virtual number inventory

The number of virtual numbers you need for hosting masking sessions at scale depends on how many concurrent sessions you create with a unique first-party or second-party phone number, whichever number is larger. To calculate the number of virtual numbers you should purchase, use this formula.

> **Virtual Number Count = 2 x `{Count Concurrent Session}` - 1**

`{Count Concurrent Session}` is the maximum number of concurrent sessions a unique phone number can create.

### Example: Food delivery application

Suppose your business offers a food delivery application. Each customer order can take up to one hour to be serviced, and a customer (the first party in this session) can place up to **10 active orders** in that time. Meanwhile, a single delivery person (the second party) can serve up to **four orders** at once. Since the higher concurrency is from the customer, we should consider this for our calculation.

> **Virtual Number Count = 2 x 10 - 1**

The total number of virtual numbers the food delivery application needs to rent is **19**. This assumes that the same customer and delivery agent combination will never repeat during an active order.

### Example: Astrology hotline application

Let's consider an astrology hotline application. Each astrologer can talk to one caller at a time, and each caller can talk to only one astrologer at a time. In this case, the calculation is simple:

> **Virtual Number Count = 2 x 1 - 1**

The astrology application needs to rent only one number. It can host several thousand parallel sessions and interactions with a single virtual number.

## Next steps

* [Number Masking Overview](/number-masking/concepts/overview) - Learn about the core concepts of number masking.
* [Session API](/number-masking/api/session) - Create and manage masking sessions using the API.
