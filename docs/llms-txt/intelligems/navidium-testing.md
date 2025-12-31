# Source: https://docs.intelligems.io/integrations/navidium-testing.md

# Navidium Testing

## Introduction

Intelligems' [Navidium](https://navidiumapp.com/) integration allows merchants to test Navidium's shipping protection (including the upsell at checkout) via an Intelligems content test. You can test:

* Widget on vs. off (both the cart widget and the upsell at checkout)
* Auto add-to-cart
* The minimum fee offered
* The fee percent

## How It Works

To set up a Navidium checkout test:

1. Create a new Intelligems Onsite Edit content test
2. For the groups for which you want to test different settings than the current defaults, inject the following Javascript:

```javascript

// change the configurations below to what you want to test
// you only need to specify configurations that you want
// to behave differently than your current Navidium settings
window._igNavidiumConfig = {
    isOn: true,
    autoAddToCart: true,
    pctFee: 5, // 5 here means 5%
    minFee: 3,
}

  const res = fetch("/cart/update.js", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      attributes: {
        '_igNavidiumConfig': JSON.stringify(window._igNavidiumConfig)
      },
    }),
  })


```

3. Enable "Use Intelligems App Config" in the Navidium settings Extensions page. If this setting is not available to you, reach out to Navidium to enable it
