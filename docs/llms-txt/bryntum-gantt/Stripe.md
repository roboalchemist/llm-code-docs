# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/feature/Stripe.md

# [Stripe](https://bryntum.com/docs/gantt/api/Grid/feature/Stripe)

Stripes rows by adding alternating CSS classes to all row elements (`b-even` and `b-odd`).

This feature is **disabled** by default.

```
let grid = new Grid({
  features: {
    stripe: true
  }
});
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isStripe](https://bryntum.com/docs/gantt/api/Grid/feature/Stripe#property-isStripe)
Identifies an object as an instance of [Stripe](https://bryntum.com/docs/gantt/api/#Grid/feature/Stripe) class, or subclass thereof.

[isStripe](https://bryntum.com/docs/gantt/api/Grid/feature/Stripe#property-isStripe-static)
Identifies an object as an instance of [Stripe](https://bryntum.com/docs/gantt/api/#Grid/feature/Stripe) class, or subclass thereof.

## Functions

Functions are methods available for calling on the class

[beforeRenderRow](https://bryntum.com/docs/gantt/api/Grid/feature/Stripe#function-beforeRenderRow)
Applies even/odd CSS when row is rendered
