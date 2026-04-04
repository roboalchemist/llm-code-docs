# Hosted Fields Style Guide

## Important: This JavaScript SDK documentation uses the legacy `HostedFields` component. For the new integration that uses the `CardFields` component, see [Card Fields Style Guide](/docs/checkout/advanced/customize/card-field-style/).

Change the layout, width, height, and outer styling of the card fields. Modify the elements you supply as containers with your current stylesheets. For example, `#card-number { border: 1px solid #333; }`.

Advanced credit and debit card payments elements require explicit height configuration. Style the height of your containers in your stylesheets. The text of the field components is configured with JavaScript.

## Supported CSS properties

- `appearance`
- `color`
- `direction`
- `font-family`
- `font-size-adjust`
- `font-stretch`
- `font-style`
- `font-variant-alternates`
- `font-variant-caps`
- `font-variant-ligatures`
- `font-variant`
- `font`
- `letter-spacing`
- `line-height`
- `opacity`
- `outline`
- `padding`
- `text-shadow`
- `-moz-appearance`
- `-moz-osx-font-smoothing`
- `-moz-tap-highlight-color`
- `-moz-transition`
- `-webkit-appearance`
- `-webkit-font-smoothing`
- `-webkit-tap-highlight-color`
- `-webkit-transition`

The CSS properties listed are the only properties supported in the advanced credit and debit card payments configuration. If you specify an unsupported CSS property, the configuration fails, and a warning shows up in the console.

Define other CSS properties on your page at the page level or in individual sections.

## Custom classes

Use the styles parameter in the `render()` method under `HostedFields` to manage your container style.

The following example shows the `styles` parameter:

```javascript
// ...
  paypal.HostedFields.render({
    createOrder: getOrderId,
    styles: {
      'input': {
        'color': '#3A3A3A',
        'transition': 'color 160ms linear',
        '-webkit-transition': 'color 160ms linear'
      },
      ':focus': {
        'color': '#333333'
      },
      '.invalid': {
        'color': '#FF0000'
      }
      // field configuration here
    }
  });