# Source: https://docs.deepconverse.com/product-docs/conversational-flow-builder/conversation-blocks/http-request.md

# HTTP Request

The HTTP Request block allows you to make request to any external Rest API. The primary use case for this in chat is to fetch data from a customized external system and also to send collected information out to an external system such as an order update.&#x20;

### How to make a API Request?

1. Start by selecting extensions in the flow palette on the left in the flow builder

2. Drag an Add On node on to the flow builder\ <br>

   <figure><img src="https://534431549-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FbO3m8ycFG8xg77R5w9dH%2Fuploads%2FrgPp6sheCP86Le5HakJf%2Fimage.png?alt=media&#x26;token=41fb9ad8-5939-40dc-a49a-c10a56b73d46" alt=""><figcaption></figcaption></figure>

3. In the properties add the details of the API you are calling.&#x20;
   1. You can choose the url or specify a parameter that holds the url&#x20;
   2. Specify headers, payloads and HTTP method

4. Save the properties and then connect your node in your flow

### How to use the API Response?

When your HTTP Request gets a response back it is available in a parameter called **actionOutput**. This parameter will contain the response sent by the external system.

To use this you can make use of templating language to access any fields inside the response. For example if this is the response and we wanted to show order details:

API Response

```
{"order": {"id": 12, "name": "blue tshirt", "price": 10, "count" 1}}
```

Template

```
Order Id: {{ actionOutput.order.id }}
Product: {{ actionOutput.order.name }} ${{ actionOutput.order.price }} 
Quantity: {{ actionOutput.order.count }}
```

The templates can be used in any messages being sent to customers.

<figure><img src="https://534431549-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FbO3m8ycFG8xg77R5w9dH%2Fuploads%2F5tw1AM6ivr4JSkumASmW%2Fimage.png?alt=media&#x26;token=dd9678fa-4a39-4934-bee4-5ba64ba1bb81" alt=""><figcaption></figcaption></figure>
