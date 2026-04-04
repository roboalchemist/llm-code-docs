# Source: https://docs.statsig.com/metrics/user-property.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# User Property

> Break down experiment results by user properties like subscription tier or platform to gain deeper insights.

It is  helpful to be able to break down Pulse results by user properties like Free vs Paid, or OS type. Setting User Property lets you slice data by properties like this.

You set user property when you create the User object you use with the Statsig SDK. These are frozen when a user is first exposed to a feature gate or experiment - in case your experiment ends up changing these properties (e.g. convert a Free user to Paid).

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/mluNydUQT6X4ZpGa/images/metrics/user-property/226679274-01705500-48ee-44d4-8a5c-cbc49d97d0b2.png?fit=max&auto=format&n=mluNydUQT6X4ZpGa&q=85&s=6217f8dd062c9f77a7e6848948ad6a03" alt="User property configuration interface" width="239" height="193" data-path="images/metrics/user-property/226679274-01705500-48ee-44d4-8a5c-cbc49d97d0b2.png" />
</Frame>

You can run custom queries on your Pulse results (Explore tab) to group by or filter by these User Property.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/mluNydUQT6X4ZpGa/images/metrics/user-property/226679816-5c7d393f-80e2-4670-8978-fc607b5fbe1a.png?fit=max&auto=format&n=mluNydUQT6X4ZpGa&q=85&s=c81b12bf667df19309da4a7baf9c9adf" alt="Pulse results custom query interface" width="1721" height="445" data-path="images/metrics/user-property/226679816-5c7d393f-80e2-4670-8978-fc607b5fbe1a.png" />
</Frame>


Built with [Mintlify](https://mintlify.com).