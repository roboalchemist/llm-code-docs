# Source: https://docs.klarna.com/platform-solutions/acquiring-partners/stripe/payments/post-purchase-management.md

# Stripe post purchase management

## Order management

Order management occurs entirely within Stripe. Here are some best practices we recommend you follow when managing orders:

- Stripe has automatic capture at order placement enabled by default, which is a capability of limited usage for specific merchant categories. To ensure you’re compliant with our [shipping policies](https://www.klarna.com/international/shipping-policies/) and fraud policies, we recommend you issue a [separate authorization and capture](https://stripe.com/docs/payments/klarna/accept-a-payment?platform=web&ui=API#manual-capture).
- Stripe supports only one capture per order. Any value remaining on the customer's order is released after the first capture, meaning you can’t recover any remaining value on that order.
- When the order is captured, you should add the shipping tracking information. It will be helpful for the customer and is considered a best practice to ensure that the customer can track the status of their order. It also allows Klarna access to relevant dispute data without further contact with your agents.

**Usage of automatic capture is restricted to specific business rules and categories.** Please refer to out [guidelines](https://docs.klarna.com/klarna-payments/in-depth-knowledge/automatic-capture) before enabling this functionality.

## Support errands

All operations specific to your Klarna orders should occur in the Stripe dashboard or with the help of Stripe support. If you have general questions about Klarna, direct them to Klarna support.

## Disputes

Sometimes, simple errors or miscommunication can cause problems with an order. As a result, the customer might open a dispute with us. If that happens, Klarna will email you with regards to a dispute so you can handle it directly. For more information about how to handle disputes, see [Klarna FAQ](https://support.stripe.com/questions/klarna-faq#how-to-manage-disputes-on-klarna-payments). Responding to these disputes quickly and with all relevant and requested information is essential in avoiding unnecessary chargebacks or delays. Please ensure that the email addresses you provide to Stripe when onboarding Klarna are checked and actioned daily. [Learn more about Klarna's dispute process.](https://docs.klarna.com/disputes)

## Customer support

If your customers have questions regarding their experience checking out with Klarna, refer them to Klarna customer support directly. To help your customers find the answers they need without involving customer support, you can include a link to the [Klarna FAQs](https://www.klarna.com/customer-service/) or a [small FAQ page](https://docs.klarna.com/on-site-messaging/in-depth-knowledge/placements) about Klarna on your website.