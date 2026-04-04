# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/use-context/get-domain-entity-details.md

# Get slot details

You can get the slot details using **context.entities.<\<slot\_name>>** from the [context](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/reference-library/context) object.

Consider that you wish to get the status of your pizza order. You can start by asking the order number, and then display that order number back to the user for confirmation. Consider that you have created a regular expression entity for the order number. See [Entity type with regular expression](https://docs.avaamo.com/user-guide/build-agents/add-entity-types-to-agent/example-pizza-agent#entity-type-with-regular-expression), for the complete example.

In the JS response node, you can use the **slot name** to display the order number as follows:

```markup
return "Checking the status of your order - "+ context.entities.order_number + ". 
Will update you in a moment.";
```

In the agent, the following response is displayed:&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Fr8By5T0A0t4ENLeQeaGH%2Fimage.png?alt=media\&token=bdaf34fc-dadf-45da-9f23-060520deebc6)

{% content-ref url="" %}
[](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/use-context)
{% endcontent-ref %}

{% content-ref url=".." %}
[..](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to)
{% endcontent-ref %}
