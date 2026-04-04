# Source: https://developers.cash.app/cash-app-afterpay/guides/welcome/migrate-from-afterpay-to-cash-app-afterpay/migration-fa-qs.mdx

***

## stoplight-id: ssr6d6xko9o03

# FAQs for the Migration

<Warning title="Important">
  If your app uses an explicit allowlist of Afterpay domains, you 

  *must*

   add 

  `api.cash.app`

   and 

  `cash.app`

   to the allowlist.
</Warning>

## Migration Requirements

<AccordionGroup>
  <Accordion title="Why is Afterpay changing its checkout experience?">
    Afterpay is becoming more easily accessible to Cash App users as part of Afterpay's integration with Cash App.

    This means we're changing the Afterpay logo where it appears on your site to attract the 50M Cash App users\* who do not use Afterpay while retaining your current Afterpay shoppers.

    The new Afterpay assets for your site incorporate proven messaging and design to acquire Cash App users and continue transacting with Afterpay users.

    Merchants who update Afterpay throughout their site will benefit from incremental sales and new customers from our total network.

    *\* Definitions & Source: A Cash App active is defined as a monthly transacting active user with at least one transaction monthly. Actives eligible for Afterpay include account owners who are 18+ and non-business accounts as of 2024.*
  </Accordion>

  <Accordion title="Is this change related to Cash App for Business?">
    No. Cash App for Business is a product that enables small, often single proprietor businesses to set up a business profile  to accept Cash App payments.
  </Accordion>

  <Accordion title="Do I need a new Cash App Pay merchant account?">
    No. This update gives you access to Cash App customers through the existing Afterpay experience. You just need to update the brand - no other changes are needed.
  </Accordion>

  <Accordion title="Will my integration need to be recertified?">
    Merchants with existing integrations will receive seamless updates, and Afterpay will complete all certifications before updates are made. We expect merchants will have minimal or no involvement with these changes, depending on how merchants displayed Afterpay.
  </Accordion>

  <Accordion title="Are my existing Afterpay customers automatically enrolled into the experience change?">
    The checkout experience will not change for the existing Afterpay customers. These customers will use the same login credentials, see the same checkout experience, and continue to service all orders via Afterpay.
  </Accordion>

  <Accordion title="Are updates to my &#x22;learn more&#x22; lightbox asset necessary? What do I need to update in order to remain in compliance?">
    Yes, we will make the necessary changes on your behalf if you use [Afterpay Messaging](/cash-app-afterpay/guides/afterpay-messaging/getting-started). Please contact your Account Manager for specific questions.
  </Accordion>

  <Accordion title="I haven't been able to transact with Afterpay, as the Afterpay Messaging is no longer visible on my website. What can I do before I can take advantage of attracting new Cash App users?">
    Our Support Hub is available to help you take advantage of the new brand. Please view our Support Hub [here](https://help.business.afterpay.com/hc/en-us).
  </Accordion>

  <Accordion title="I'm interested in using Afterpay On-Site Messaging. Should I migrate to On-Site Messaging as part of this change?">
    Yes, we recommend coupling any site rebranding work with implementing Dynamic Messaging. Please speak to your Merchant Delivery partner for guidance.
  </Accordion>
</AccordionGroup>

## Customer Support Questions

Customers are the people that buy your goods or services. These are some questions they may ask.

<AccordionGroup>
  <Accordion title="As a customer, if I sign up for Cash App Afterpay do I get a Cash App account automatically?">
    No, customers won't automatically get a Cash App account when they sign up for Cash App Afterpay.
  </Accordion>

  <Accordion title="Can customers combine payments from their Cash App wallet and their Cash App Afterpay payment instrument (card)?">
    No. When you pay with Cash App, you can use your balance. If you do not have enough money then you can pay with a linked debit card instead.

    Cash App Afterpay customers' payment instruments (cards) are unchanged.
  </Accordion>

  <Accordion title="Is normal Cash App functionality still available such as paying with Bitcoin and buying shares?">
    Yes, this change does not change the way Cash App's customers use Cash App to send, bank, and invest.
  </Accordion>

  <Accordion title="Can teenagers with Cash App accounts use Cash App Afterpay?">
    No, Cash App Afterpay is only available to customers over the age of 18.
  </Accordion>

  <Accordion title="What is the customer experience before placing an order (UX flows)?">
    There are three key touchpoints to show your customers:

    * Product details

    * Shopping cart

    * Checkout pages

    See our [Cash App Afterpay Merchant Guidelines](https://www.figma.com/deck/yC8BbsBfhxkSnxrw8VtYna/Cash-App-Afterpay-%E2%80%93-Merch\[…]kF1jqQt-1\&scaling=min-zoom\&content-scaling=fixed\&page-id=0%3A1) guidelines to learn about the customer experience.
  </Accordion>

  <Accordion title="What is the customer experience after placing an order (notifications, emails, servicing)?">
    See our [Cash App Afterpay Merchant Guidelines](https://www.figma.com/deck/yC8BbsBfhxkSnxrw8VtYna/Cash-App-Afterpay-%E2%80%93-Merch\[…]kF1jqQt-1\&scaling=min-zoom\&content-scaling=fixed\&page-id=0%3A1) guidelines to learn about the customer experience.
  </Accordion>

  <Accordion title="When are you informing your customer base of this change?">
    Throughout 2025, both Afterpay and Cash App will make this update clear to our combined 58M monthly transacting active customers. We will also launch scaled awareness campaigns to excite and attract even more customers for our merchants.
  </Accordion>
</AccordionGroup>

## Merchant Support Questions

This section has questions that merchants may ask.

<AccordionGroup>
  <Accordion title="I already have both Afterpay and Cash App Pay, how does this affect my integration?">
    Cash App Pay and Cash App Afterpay will remain two separate products and integrations. See the [What is Cash App Pay and What is Cash App Afterpay?](/cash-app-afterpay/guides/welcome/getting-started/cash-app-pay-vs-cash-app-afterpay) page for details about the two products.

    Cash App Pay is not affected by this change.

    If you currently use Afterpay, your branding changes to Cash App Afterpay. See the [Migrate from Afterpay to Cash App Afterpay](/cash-app-afterpay/guides/welcome/migrate-from-afterpay-to-cash-app-afterpay) page for specific information about your integration method and how to update your branding from Afterpay to Cash App Afterpay.
  </Accordion>

  <Accordion title="Can I still use the Afterpay Business Hub?">
    Yes. All orders are still being processed by Afterpay and will be reflected in the Business Hub.
  </Accordion>

  <Accordion title="I support Afterpay in other countries outside the US.  How will this change affect those regions?">
    The change is only applicable to the US (not inclusive of US territories). The experience will not change outside of the US, and the existing Afterpay brand will remain in place outside the US.
  </Accordion>

  <Accordion title="Will the Afterpay SDKs be updated with Cash App related assets?">
    Yes.
  </Accordion>

  <Accordion title="How do I access analytic data?">
    There is access to the same analytics that you have today. All Afterpay orders are captured and reported in Hub/Portal/IQ.
  </Accordion>

  <Accordion title="With the influx of new customers, do you expect a decline in Average Order Value (AOV)?">
    No, we do not expect a decline in AOV thanks to our proprietary data and underwriting.
  </Accordion>

  <Accordion title="Will there be an updated Cash eCommerce Implementation guide?">
    See our [Migration Guides](/cash-app-afterpay/guides/welcome/migrate-from-afterpay-to-cash-app-afterpay) for all integration details related to this update.
  </Accordion>

  <Accordion title="How can I find out about future Cash App Afterpay or Cash App changes or new features?">
    You'll receive emails about important updates on what is changing and when. Please make sure your contact information is up to date in your Merchant Hub.
  </Accordion>

  <Accordion title="How will this change affect my conversion rates?">
    We're making this change to serve the total customer network of Afterpay and Cash App. Today, 50 million *Cash App actives* do not use Afterpay. This change allows Afterpay's merchants to seamlessly transact with meaningfully more customers than ever before.

    This change has been thoroughly tested and proven to attract new Cash App users while also retaining existing Afterpay users.

    *\* Definitions & Source: A Cash App active is defined as a monthly transacting active user with at least one transaction monthly. Actives eligible for Afterpay include account owners who are 18+ and non-business accounts as of 2024.*
  </Accordion>

  <Accordion title="How will Cross Border Trade (CBT) work with Cash App Afterpay? For example, Clearpay to Cash App, Cash App to Cash App Afterpay or Cash App Afterpay to Cash App">
    Cash App Afterpay customers can still make CBT purchases. Cash App customers that are new to Cash App Afterpay will not see options to use CBT.
  </Accordion>

  <Accordion title="Are Disputes affected by this change?">
    No, there is no effect on disputes.
  </Accordion>

  <Accordion title="Is Express Checkout supported with Cash App Afterpay?">
    Yes. Express Checkout continues to work the same as before.
  </Accordion>

  <Accordion title="Will the Merchant Hub URL change?">
    No, the URL stays the same: [https://portal.afterpay.com/us/login-email](https://portal.afterpay.com/us/login-email)
  </Accordion>

  <Accordion title="I'm currently using OAuth with Afterpay - how will this affect my integration?">
    OAuth continues to work the same as before.
  </Accordion>

  <Accordion title="I support Afterpay in other countries outside the US.  How will this change affect those regions?">
    The change is only applicable to the US (not inclusive of US territories). The experience will not change outside of the US, and the existing Afterpay brand will remain in place outside the US.
  </Accordion>

  <Accordion title="Are there any changes to Afterpay's Monthly Payments availability?">
    No. Pay Monthly continues to be available to Cash App Afterpay customers.
  </Accordion>

  <Accordion title="I'm re-platforming my e-comm front end in the next quarter – what is Block's guidance?">
    We recommend moving to the new brand as soon as possible.
  </Accordion>

  <Accordion title="Are refunds affected by this change?">
    No, there is no effect on refunds.
  </Accordion>

  <Accordion title="Are settlements affected by this change?">
    No, there is no effect on settlements.
  </Accordion>

  <Accordion title="How will Cash App and Afterpay handle version releases/rollouts?">
    This depends on your integration method. See the documentation specific to your integration method to learn about the rollout.
  </Accordion>

  <Accordion title="Will merchants be able to differentiate which orders are from Cash App customers?">
    No, this is not possible today.
  </Accordion>

  <Accordion title="How do you know whether to direct the customer to Cash App or Afterpay if they haven't logged in yet?">
    We use the customer data provided during the Create Checkout API call.
  </Accordion>

  <Accordion title="Is there a hard cutover date?">
    We recommend making any changes needed by March 17, 2025.
  </Accordion>
</AccordionGroup>
