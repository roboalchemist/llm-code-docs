# Source: https://docs.wiremock.io/soap-stubbing.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wiremock.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Simulating SOAP services

> Matching SOAP requests and sending SOAP responses

Stubbing a SOAP response is similar in most respects to stubbing a REST response. The main difference is that the HTTP method
and URL alone are not enough to differentiate requests since these are always the same for a given endpoint.

In addition, we need to match on the `SOAPAction` header and the request body XML.

## Using the SOAPAction header

SOAP APIs typically use the `SOAPAction` header to select the appropriate action for the call.
Although you can sometimes avoid this, it's usually a good idea to add a header match for `SOAPAction` as it's more
efficient and faster than relying exclusively on the XML body.

<img src="https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/soap-action-header.png?fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=52dcc91f21d52d935bcedcdbff07e5ae" title="Matching the SOAPAction header" data-og-width="792" width="792" data-og-height="176" height="176" data-path="images/screenshots/soap-action-header.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/soap-action-header.png?w=280&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=b35ce0f775f5b0965be69030a5bc9470 280w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/soap-action-header.png?w=560&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=5f08b5a319f316cb787dc129371ac5b8 560w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/soap-action-header.png?w=840&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=ff6b12ac8d9c5d8215d2b9bd6c7569df 840w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/soap-action-header.png?w=1100&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=b7fda10dcba129e030d39ec03e7003ab 1100w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/soap-action-header.png?w=1650&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=cdcca62bbf27e866c3a3f9dc1365779e 1650w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/soap-action-header.png?w=2500&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=f72504f967411b77a9e691547764d226 2500w" />

## Matching the request body with XML equality

When dealing with request bodies that are small and have no data of a transient nature (e.g. transaction IDs or today's date)
`equalToXml` is a straightforward way to specify a match.

For instance given a SOAP service for managing a to do list, you may wish to mock an interaction matching a specific request to add an item:

<img src="https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/soap-request.png?fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=2bcef9ed536db7fff7893c6361c12f46" title="SOAP request" data-og-width="1984" width="1984" data-og-height="1566" height="1566" data-path="images/screenshots/soap-request.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/soap-request.png?w=280&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=6c9220893732c352a275be2a023cd075 280w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/soap-request.png?w=560&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=1f1b1bf2f86a600d71dc82679a98aef3 560w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/soap-request.png?w=840&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=3cb8ba9395021f5f4b5d34a25d651415 840w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/soap-request.png?w=1100&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=bfc28e64a81bd2e5551256e958d3fb5b 1100w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/soap-request.png?w=1650&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=83e913ddc46246b18b1fa609b7725db5 1650w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/soap-request.png?w=2500&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=3e417a1636b2506e04879b36038c6bc2 2500w" />

Which returns a success response:

<img src="https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/soap-response.png?fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=202bd95ca2e769d2b19685c049f4024d" title="SOAP response" data-og-width="1986" width="1986" data-og-height="970" height="970" data-path="images/screenshots/soap-response.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/soap-response.png?w=280&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=56bfe95c66947c3658b3a2d6921ea113 280w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/soap-response.png?w=560&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=9be691703e0b7e2e89693c1567242fc8 560w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/soap-response.png?w=840&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=e9edd4ac6b54c14907ca5a14d72f388f 840w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/soap-response.png?w=1100&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=de025792c2f77a395a3f32ffec1ecf4f 1100w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/soap-response.png?w=1650&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=9710d6e18e53dcd7054ed2bf32d6e420 1650w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/soap-response.png?w=2500&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=e8779cc92a7ca3aa0a6909ca8fc41210 2500w" />

Testing this returns the expected XML response:

```
$ curl -X POST -d '<?xml version="1.0"?>
<soap-env:Envelope xmlns:soap-env="http://www.w3.org/2001/12/soap-envelope" soap-env:encodingStyle="http://www.w3.org/2001/12/soap-encoding">

   <soap-env:Body xmlns:m="http://example.company/todo" >
      <m:AddToDoItem>
         <m:ToDoItem>Have a wash</m:ToDoItem>
      </m:AddToDoItem>
   </soap-env:Body>

</soap-env:Envelope>' -H 'SOAPAction: "http://example.company/todo/AddToDoItem"' http://example.wiremockapi.cloud/soap-example -v

> POST /soap-example HTTP/1.1
> Host: example.wiremockapi.cloud
> User-Agent: curl/7.54.0
> Accept: */*
> SOAPAction: "http://example.company/todo/AddToDoItem"
> Content-Length: 355
> Content-Type: application/x-www-form-urlencoded
>
* upload completely sent off: 355 out of 355 bytes
< HTTP/1.1 200 OK
< Transfer-Encoding: chunked
<
<?xml version="1.0"?>
<soap-env:Envelope xmlns:soap-env="http://www.w3.org/2001/12/soap-envelope" soap-env:encodingStyle="http://www.w3.org/2001/12/soap-encoding">

   <soap-env:Body xmlns:m="http://example.company/todo" >
      <m:AddToDoResult>Item "Have a wash" successfully added</m:AddToDoResult>
   </soap-env:Body>

</soap-env:Envelope>
```

### Using placeholders to ignore transient values

The above example works fine when the request body doesn't contain any transient data
such as transaction IDs or the current date. However, if data that changes on each
request is introduced it will be necessary allow a match to occur regardless of the
actual value received.

One way to do this is to use [placeholders](./advanced-stubbing/#xml-placeholders).
Let's assume the request body of our API now contains a `TransactionId` element, which
must be a unique value for each request e.g.:

```xml  theme={null}
<?xml version="1.0"?>
<soap-env:Envelope xmlns:soap-env="http://www.w3.org/2001/12/soap-envelope"
  soap-env:encodingStyle="http://www.w3.org/2001/12/soap-encoding">

   <soap-env:Body xmlns:m="http://example.company/todo">
      <m:TransactionId>1ea094dd-9548-4a79-a43c-b44670f955c6</m:TransactionId>
      <m:AddToDoItem>
         <m:ToDoItem>Have a wash</m:ToDoItem>
      </m:AddToDoItem>
   </soap-env:Body>

</soap-env:Envelope>
```

We can ignore this value by ticking the "Enable XMLUnit placeholders" box and
putting an ignore token into the expected XML in the form:

```xml  theme={null}
<m:TransactionId>${xmlunit.ignore}</m:TransactionId>
```

<img src="https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/soap-placeholders.png?fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=dc87c675a8221f43f322f55b2610ff96" title="SOAP request XML with placeholders" data-og-width="1948" width="1948" data-og-height="570" height="570" data-path="images/screenshots/soap-placeholders.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/soap-placeholders.png?w=280&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=7c3978fd501b4bda42e74a2f1f79b8ab 280w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/soap-placeholders.png?w=560&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=0a7cd2d7da50d29b200c8a5178e06078 560w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/soap-placeholders.png?w=840&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=921f2a132261508c563cdd3fc89cad1f 840w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/soap-placeholders.png?w=1100&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=0d0c3ea26969b0c10acd2752d9467440 1100w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/soap-placeholders.png?w=1650&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=143c1872ca71480ce7f22f2aa47a3094 1650w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/soap-placeholders.png?w=2500&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=1ac1a78fedcdaf3bb77c6a247e4f72d7 2500w" />

## Matching the request body with XPath

When working with large SOAP requests `equalToXml` can become quite slow as it must perform a comparison on every node in the XML document.

It's often faster to match specific elements within the document using the `matchesXPath` operator,
and since this is a much looser approach to matching it's another way to solve
the problem described above where frequently changing values are present.

When matching using XPath, your aim should be to target as few elements/attributes as possible while being able
to reliably distinguish between requests.

Given the same request body as in the previous section, we could use the following
XPath to match just on the value of the `m:ToDoItem` element:

```xpath  theme={null}
//AddToDoItem/ToDoItem[text()='Have a wash']
```

<img src="https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/xpath-soap-match.png?fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=a20616411f2e889a3f51684374e94b93" title="Matching with XPath" data-og-width="1954" width="1954" data-og-height="312" height="312" data-path="images/screenshots/xpath-soap-match.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/xpath-soap-match.png?w=280&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=162200c92cd7fd5390c6822786617d2d 280w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/xpath-soap-match.png?w=560&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=05e60d8897c346b8babe6ebd7738237b 560w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/xpath-soap-match.png?w=840&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=6447e487db2a4cca3f80076e17ece97a 840w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/xpath-soap-match.png?w=1100&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=7a1e9560577b7c7754d9763dcc2ad112 1100w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/xpath-soap-match.png?w=1650&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=6d6e5edbf16b4acb7fea4dea2f2d77f6 1650w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/xpath-soap-match.png?w=2500&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=6c24273b29d9625dfe1a1105f24a3ead 2500w" />

### Using multiple XPath expressions

Sometimes you need to match on more than one XML element to be able to adequately
distinguish between requests. Although XPath supports multiple predicates with logical and/or,
often it can be easier to use multiple body matchers each targeting a single element.

Suppose we added a `UserId` field that we also wanted to target:

```xml  theme={null}
<?xml version="1.0"?>
<soap-env:Envelope xmlns:soap-env="http://www.w3.org/2001/12/soap-envelope"
  soap-env:encodingStyle="http://www.w3.org/2001/12/soap-encoding">

   <soap-env:Body xmlns:m="http://example.company/todo">
      <m:TransactionId>1ea094dd-9548-4a79-a43c-b44670f955c6</m:TransactionId>
      <m:UserId>abc123</m:UserId>
      <m:AddToDoItem>
         <m:ToDoItem>Have a wash</m:ToDoItem>
      </m:AddToDoItem>
   </soap-env:Body>

</soap-env:Envelope>
```

We could add one `matchesXPath` body pattern for each of the elements we
care about:

<img src="https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/multiple-xpath-soap-match.png?fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=4ab6dd288262ecf6907742ce02a34dc8" title="Matching with multiple XPaths" data-og-width="1912" width="1912" data-og-height="616" height="616" data-path="images/screenshots/multiple-xpath-soap-match.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/multiple-xpath-soap-match.png?w=280&fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=c10aca80788bacb5b4aca67a8c8824ed 280w, https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/multiple-xpath-soap-match.png?w=560&fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=ce1b7dc9a33aeeef4834b72e4132762f 560w, https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/multiple-xpath-soap-match.png?w=840&fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=6a9409e44aa5af7a05b34e21fb8fb173 840w, https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/multiple-xpath-soap-match.png?w=1100&fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=ebcdadcce11ab437c6aaabd47f104b20 1100w, https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/multiple-xpath-soap-match.png?w=1650&fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=f042edad47f2499a45ac424f2cb0fcba 1650w, https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/multiple-xpath-soap-match.png?w=2500&fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=fbb99eebd417d9b83fcfa620f2bd6cd9 2500w" />

### A gotcha - the recursive selector: //

Given the above XML document, you might expect the following XPath expression to
produce a match:

```xpath  theme={null}
//UserId[text()='abc123']
```

However, due to a quirk of how XML documents with namespaces are evaluated this won't work.
Ensuring that you select at least one node beneath the element searched for recursively
will fix this, so the above XPath can be corrected like this:

```xpath  theme={null}
//UserId/text()[.='abc123']
```
