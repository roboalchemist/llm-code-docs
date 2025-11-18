# Source: https://www.plain.com/docs/ui-components.md

# UI Components

UI components are a way of describing some UI when creating threads or [events](https://plain.support.site/article/events) or building [customer cards](https://plain.support.site/article/customer-cards).

For example - this is a button that links to Stripe.

```json  theme={null}
{
  "componentLinkButton": {
    "linkButtonUrl": "http://stripe.com/",
    "linkButtonLabel": "View in Stripe"
  }
}
```

and it looks like this:

<Frame>
    <img src="https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-link-button-stripe.png?fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=5a0db8257af49456ee808657eb879aa1" alt="Example button linking to stripe" data-og-width="1664" width="1664" data-og-height="300" height="300" data-path="public/images/ui-component-link-button-stripe.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-link-button-stripe.png?w=280&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=c4f5a9fb7cd1357583e6f68c9afa251b 280w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-link-button-stripe.png?w=560&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=75c3c76d540688cb7276261d2c0ecdcc 560w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-link-button-stripe.png?w=840&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=ad7deba75cbc80982acc0b7150bd4431 840w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-link-button-stripe.png?w=1100&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=bef34edd15d3df00fd541e7a9d665731 1100w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-link-button-stripe.png?w=1650&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=a2c3a5e142c9424b86aa3749a1525701 1650w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-link-button-stripe.png?w=2500&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=e7660842d3d6ed1fcbec384b252a8575 2500w" />
</Frame>

In the GraphQL API schema, we have two separate unions for Custom Timeline Entry Components and Customer Card
Components, but both unions share the same types therefore they can be treated as the same.

To see UI components in action you can experiment with them in the [UI components playground](https://app.plain.com/developer/ui-components-playground/)
