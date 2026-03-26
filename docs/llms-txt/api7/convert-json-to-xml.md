# Source: https://docs.api7.ai/apisix/how-to-guide/transformation/convert-json-to-xml.md

# Convert JSON to XML

XML (eXtensible Markup Language) is a widely adopted standard for representing and organizing structured data. With its flexibility and human-readable syntax, XML provides a versatile solution for data interchange and storage across diverse systems and platforms. It is also used by SOAP protocol as its message format.

This guide will show you how to convert between JSON and XML SOAP using the `body-transformer` plugin, which allows client to send and receive JSON data while interacting with the SOAP service.

<br />

![JSON to XML Diagram](https://static.api7.ai/uploads/2024/02/07/EcjN9wIT_json-xml.png)

<br />

## Prerequisite(s)[â](#prerequisites "Direct link to Prerequisite(s)")

* Install [Docker](https://docs.docker.com/get-docker/).
* Install [cURL](https://curl.se/) to send requests to APISIX for validation.
* Install [Java 17](https://www.oracle.com/java/technologies/javase/jdk17-archive-downloads.html) for the example SOAP server.
* Follow the [Getting Started tutorial](https://docs.api7.ai/apisix/getting-started/.md) to start a new APISIX instance in Docker or on Kubernetes.

## Deploy an Example SOAP Server[â](#deploy-an-example-soap-server "Direct link to Deploy an Example SOAP Server")

Start an [example SOAP server](https://github.com/spring-guides/gs-soap-service) that exposes data from various European countries:

```
cd /tmp
git clone https://github.com/spring-guides/gs-soap-service.git
cd gs-soap-service/complete
./mvnw spring-boot:run
```

## Create Transformation Templates[â](#create-transformation-templates "Direct link to Create Transformation Templates")

The transformation template mainly uses [lua-resty-template](https://github.com/bungle/lua-resty-template) syntax. See [template syntax](https://github.com/bungle/lua-resty-template#template-syntax) for more information.

Additionally, there are a few auxiliary functions which you can use in templates:

* `_escape_json()` and `_escape_xml()` - used to escape special characters, such as double quotes
* `_body` - used to access request body
* `_ctx` - used to access context variables

Create request and response transformation templates, which are customized and to be configured in the `body-transformer` plugin to instruct on how to transcode between XML and JSON:

```
req_template=$(cat <<EOF | awk '{gsub(/"/,"\\\"");};1' | awk '{$1=$1};1' | tr -d '\r\n'
<?xml version="1.0"?>
<soap-env:Envelope xmlns:soap-env="http://schemas.xmlsoap.org/soap/envelope/">
 <soap-env:Body>
  <ns0:getCountryRequest xmlns:ns0="http://spring.io/guides/gs-producing-web-service">
   <ns0:name>{{_escape_xml(name)}}</ns0:name>
  </ns0:getCountryRequest>
 </soap-env:Body>
</soap-env:Envelope>
EOF
)

rsp_template=$(cat <<EOF | awk '{gsub(/"/,"\\\"");};1' | awk '{$1=$1};1' | tr -d '\r\n'
{% if Envelope.Body.Fault == nil then %}
{
  "status":"{{_ctx.var.status}}",
  "currency":"{{Envelope.Body.getCountryResponse.country.currency}}",
  "population":{{Envelope.Body.getCountryResponse.country.population}},
  "capital":"{{Envelope.Body.getCountryResponse.country.capital}}",
  "name":"{{Envelope.Body.getCountryResponse.country.name}}"
}
{% else %}
{
  "message":{*_escape_json(Envelope.Body.Fault.faultstring[1])*},
  "code":"{{Envelope.Body.Fault.faultcode}}"
  {% if Envelope.Body.Fault.faultactor ~= nil then %}
  , "actor":"{{Envelope.Body.Fault.faultactor}}"
  {% end %}
}
{% end %}
EOF
)
```

## Configure APISIX[â](#configure-apisix "Direct link to Configure APISIX")

Create a route with `body-transformer` referencing the transformation templates created previously:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "body-transformer-route",
    "methods": ["POST"],
    "uri": "/ws",
    "plugins": {
      "body-transformer": {
        "request": {
          "template": "'"$req_template"'",
          "input_format": "json"
        },
        "response": {
          "template": "'"$rsp_template"'",
          "input_format": "xml"
        }
      },
      "proxy-rewrite": {
        "headers": {
          "set": {
            "Content-Type": "text/xml"
          }
        }
      }
    },
    "upstream": {
      "type": "roundrobin",
      "nodes": {
        "localhost:8080": 1
      }
    }
  }'
```

â¶ Set the request input format as JSON, so that the plugin will apply the JSON decoder internally.

â· Set the response input format as XML, so that the plugin will apply the XML decoder internally.

â¸ Set the `Content-Type` header to `text/xml` for the upstream service to respond properly.

â¹ Update the connection address for your SOAP service.

tip

If it is cumbersome to adjust complex text files to be valid transformation templates, you can use the base64 utility to encode the files, such as the following:

```
"body-transformer": {
  "request": {
    "template": "'"$(base64 -w0 /path/to/request_template_file)"'"
  },
  "response": {
    "template": "'"$(base64 -w0 /path/to/response_template_file)"'"
  }
}
```

## Verify[â](#verify "Direct link to Verify")

Send a request to the route with a valid JSON body:

```
curl "http://127.0.0.1:9080/ws" -X POST -d '{"name": "Spain"}'
```

You should see a response similar to the following:

```
{
  "status": "200",
  "currency": "EUR",
  "population": 46704314,
  "capital": "Madrid",
  "name": "Spain"
}
```

This shows that the JSON body sent in the request has been transformed into XML and forwarded to the upstream SOAP service, and the response body was transformed back from XML to JSON.

## Next Steps[â](#next-steps "Direct link to Next Steps")

The `body-transformer` plugin can also be used for transformation between YAML and JSON, or modification of the request bodies. See the [plugin doc](https://docs.api7.ai/hub/body-transformer.md) for more information.
