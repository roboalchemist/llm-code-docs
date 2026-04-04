# Source: https://docs.curator.interworks.com/curator_api/custom_integration/subscription_routing.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Subscription Routing

> Configure subscription email routing to direct users through Curator instead of Tableau Server

Curator integrates nicely with Tableau's native subscription system.
When users receive a subscription email, however, you may not wish the users to be routed to Tableau Server.

If you would rather users be routed to the appropriate Dashboard on Curator, [update Tableau Server's "subscription url"](https://kb.tableau.com/articles/issue/subscription-link-in-email-broken).

Point this url to your Curator website with /subscription/ appended.
For example, `https://examplecurator.interworks.com/subscription`.

***Note:** At the time of this writing, updating this value in Tableau Server requires a Tableau Server reboot.*
