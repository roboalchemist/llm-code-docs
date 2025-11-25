# Source: https://smartcar.com/docs/api-reference/about-brand-specific.md

# Make Specific Endpoints

<Warning>
  The Vehicles API v2.0 will be deprecated by **Q3 of 2026**. We recommend migrating to the [latest version](/api-reference/vehicles-api-intro) as soon as possible to ensure continued support and access to new features.
</Warning>

In cases where there are many differences in how each OEM provides the same data, Smartcar would provide you with a make-specific endpoint before making it widely available to all supported makes.

This allowed customers to take advantage of these endpoints and share feedback with Smartcar. Based on the feedback, we realized that these endpoints often required customers to write make-specific code, which is not ideal for a standardized API.

These endpoints will be deprecated along with API V2.0.

<Info>When using make specific endpoints, please ensure to specify the [make](/api-reference/makes) in lower case format. Using upper case letters will result in a PERMISSION error.</Info>
