# Source: https://docs.intelligems.io/general-features/targeting/targeting-by-customer-parameters.md

# Targeting By Customer Parameters

You can target experiments and personalizations by Shopify customer parameters for logged in customers. To get started, first, expose the parameter(s) you're interested in targeting via theme Liquid. For example, if you want to target by customer tags, you could add (above the Intelligems script in the `theme.liquid`file):

```liquid
{% if customer %}
<script>
window.customerTags = '{{ customer.tags }}';
</script>
{% endif %}
```

Then, in Intelligems, use JS audience or page targeting to target specific customer tags, with an expression like:

```javascript
window.customerTags?.includes("my-tag")
```

This example shows how to target based on customer tags, but you could use a similar method to target any parameter made available by the [Liquid customer object](https://shopify.dev/docs/api/liquid/objects/customer).
