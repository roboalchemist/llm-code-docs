# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/integrate-with-api-1/rest-and-soap-api.md

# REST and SOAP API

You can seamlessly integrate skill response with API using:

* REST API response block
* SOAP service call within a Javascript response block

## REST API

You can integrate skill response with REST API using a simple fetch call. In the node where you require to integrate with REST API, use the fetch API with required methods such as POST, GET. See [fetch](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/reference-library/advanced-js-libraries#fetch), for more information.

Consider that you wish to get the status of your pizza order:

1. Get the order number from the user
2. Send an API request to an external application (Mac Pizza Application) to get the order status.

The following is a simple GET call to get the order status:

```javascript
let query = "<<order_number>>";
let api_url = "<<API_URL>>&q="+query;
return fetch(api_url, {
 method: 'GET',
 headers: {
 'Content-Type': 'application/json'
 }
 }).then(res => res.json()).then(json => {
…..process the JSON
```

## SOAP API

You can also integrate skill response with SOAP API. The following is a sample SOAP API block that can be used as a reference:

```javascript
const DOMParser = xmldom.DOMParser;

var url = 'http://demo8362428.mockable.io/stockprice?wsdl';
var args = {name: 'value'};
var auth = "Basic " + new Buffer("admin;60" + ":" + "123456").toString("base64");
var clientOptions = {
  
};
return Soap.createClient(url, clientOptions, function(err, client) {
  client.setSecurity(new Soap.BasicAuthSecurity('admin;60', '123456789'));
    return client.getprice({arg0: '3'},function(err, result) {   //1-8 items are available - keys: Price
      console.log(JSON.stringify(result.body));
      //return JSON.stringify(result.body.body);
      let xmlDoc = new DOMParser().parseFromString(result.body, 'text/xml');

      var priceResponse = xmlDoc.getElementsByTagName("m:GetStockPriceResponse")[0];
      console.log("priceResponse: "+ priceResponse);
      
      var priceNode = priceResponse.getElementsByTagName("m:Price")[0];
      console.log("priceNode: "+ priceNode.getValue());
      return "value: "+ priceNode;

    });
    //console.log(client.lastRequest);
});

```

See [SOAP](https://en.wikipedia.org/wiki/SOAP), for more information.
