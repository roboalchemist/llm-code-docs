# Source: https://tyk.io/docs/advanced-configuration/transform-traffic/soap-rest.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Transformation Use Case: SOAP To REST

> How to transform SOAP API to REST API in Tyk

You can transform an existing SOAP service to a JSON REST service. This can be done from the Tyk Dashboard with no coding involved and should take around 10 minutes to perform the transform.

We also have a video which walks you through the SOAP to REST transform.

<iframe width="560" height="315" src="https://www.youtube.com/embed/jeNXLzpKCaA" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

## Prerequisites

An existing SOAP service and the WSDL definition. For this example, we will use:

* Upstream Target - [https://www.dataaccess.com/webservicesserver/numberconversion.wso](https://www.dataaccess.com/webservicesserver/numberconversion.wso)
* The WSDL definition from - [https://www.dataaccess.com/webservicesserver/numberconversion.wso?WSDL](https://www.dataaccess.com/webservicesserver/numberconversion.wso?WSDL)
* Postman Client (or other endpoint testing tool)

## Steps for Configuration

1. **Import the WSDL API**

   1. Select APIs from the System Management menu

      <img src="https://mintcdn.com/tyk/XYIZ0Oo5nzDVrYaM/img/2.10/apis_menu.png?fit=max&auto=format&n=XYIZ0Oo5nzDVrYaM&q=85&s=16ce9ff83b8de9369f31c23099a28be4" alt="APIs Menu" width="244" height="305" data-path="img/2.10/apis_menu.png" />

   2. Click Import API

      <img src="https://mintcdn.com/tyk/m6xbM9kI-xFpaRwr/img/2.10/import_api_button.png?fit=max&auto=format&n=m6xbM9kI-xFpaRwr&q=85&s=cd1d99264ddd0fef2c9167082158419e" alt="Import API" width="339" height="63" data-path="img/2.10/import_api_button.png" />

   3. Select **From WSDL** from the Import an API Definition window

   4. In the **Upstream Target** field, enter `https://www.dataaccess.com/webservicesserver/numberconversion.wso` as listed in the Prerequisites.

   5. Paste the WSDL definition from the link in Prerequisites

   6. Click **Generate API**. You should now have an API named `NumberConversion` in your API list

      <img src="https://mintcdn.com/tyk/m6xbM9kI-xFpaRwr/img/2.10/numberservice_api.png?fit=max&auto=format&n=m6xbM9kI-xFpaRwr&q=85&s=9c4c37127662bbb4b0717ddf748b5be4" alt="NumberService API" width="1191" height="292" data-path="img/2.10/numberservice_api.png" />

2. **Add the transforms to an Endpoint**

   1. From the API list, select Edit from the Actions menu for the `NumberConversion` API

   2. Select the **Endpoint Designer** tab. You should see 2 POST endpoints that were imported. We will apply the transforms to the `NumberToWords` endpoint.

      <img src="https://mintcdn.com/tyk/m6xbM9kI-xFpaRwr/img/2.10/numberservice_endpoints.png?fit=max&auto=format&n=m6xbM9kI-xFpaRwr&q=85&s=cbd283da7840c490a05bd75480cd2ecb" alt="Endpoints" width="1124" height="391" data-path="img/2.10/numberservice_endpoints.png" />

   3. Expand the `NumberToWords` endpoint. The following plugins should have been added as part of the import process.

      * URL rewrite

      * Track endpoint

   <Note>
     To make the URL a little friendlier, we're going to amend the Relative Path to just `/NumberToWords`. Update your API after doing this.
   </Note>

   1. Add the following plugins from the **Plugins** drop-down list:

      * Body transform
      * Modify headers

3. **Modify the Body Transform Plugin**

   **Set up the Request**

   We use the `{{.FieldName}}` Golang template syntax to access the JSON request. For this template we will use `{{.numberToConvert}}`.

   1. Expand the Body transform plugin. From the Request tab, copy the following into the Template section:

   ```xml  theme={null}
   <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:web="http://www.dataaccess.com/webservicesserver/">
   <soapenv:Header/>
   <soapenv:Body>
       <web:NumberToDollars>
           <web:dNum>{{.numberToConvert}}</web:dNum>
       </web:NumberToDollars>
   </soapenv:Body>
   </soapenv:Envelope>
   ```

   1. In the Input field, enter the following:

   ```json  theme={null}
   {
       "numberToConvert": 35
   }
   ```

   <Note>
     The '35' integer can be any number you want to convert
   </Note>

   1. Click **Test**. You should get the following in the Output field:

   ```xml  theme={null}
   <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:web="http://www.dataaccess.com/webservicesserver/">
   <soapenv:Header/>
   <soapenv:Body>
       <web:NumberToDollars>
           <web:dNum>35</web:dNum>
       </web:NumberToDollars>
   </soapenv:Body>
   </soapenv:Envelope>
   ```

   **Set up the Response**

   Again, for the response, we will be using the `{{.FieldName}}` syntax as the following `{{.Envelope.Body.NumberToDollarsResponse.NumberToDollarsResult}}`

   1. For the Input Type, select XML

   <img src="https://mintcdn.com/tyk/rcbuH4FawxAvTx_L/img/2.10/body_trans_response_input.png?fit=max&auto=format&n=rcbuH4FawxAvTx_L&q=85&s=3545b48fd1e396b32108f3baa7d52630" alt="Response Input Type" width="418" height="269" data-path="img/2.10/body_trans_response_input.png" />

   1. In the Template section enter:

   ```yaml  theme={null}
   {
       "convertedNumber": "{{.Envelope.Body.NumberToDollarsResponse.NumberToDollarsResult}}"
   }
   ```

   1. Enter the following into the input field:

   ```xml  theme={null}
   <soap12:Envelope xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
   <soap12:Body>
       <NumberToDollarsResponse xmlns="http://www.dataaccess.com/webservicesserver/">
       <NumberToDollarsResult>thirty five dollars</NumberToDollarsResult>
       </NumberToDollarsResponse>
   </soap12:Body>
   </soap12:Envelope>
   ```

   1. Click Test. You should get the following in the Output field:

   ```json  theme={null}
   {
       "convertedNumber": "thirty five dollars"
   }
   ```

4. **Change the Content-Type Header**

   We now need to change the `content-type` header to allow the SOAP service to receive the payload in XML. We do this by using the **Modify header** plugin

   1. Expand the Modify Header plugin

   2. From the **Request** tab enter the following in the **Add this header** section

      * Header Name: `content-type`
      * Header Value: `text/xml`

   3. Click Add

      <img src="https://mintcdn.com/tyk/XYIZ0Oo5nzDVrYaM/img/2.10/add_header_type.png?fit=max&auto=format&n=XYIZ0Oo5nzDVrYaM&q=85&s=806cff1f6522136f4628d2cede62e3fd" alt="Modify Header Request" width="1033" height="350" data-path="img/2.10/add_header_type.png" />

   4. From the **Response** tab enter the following in the **Add this header** section

      * Header Name: `content-type`
      * Header Value: `application/json`

      <img src="https://mintcdn.com/tyk/m6xbM9kI-xFpaRwr/img/2.10/modify-header-response.png?fit=max&auto=format&n=m6xbM9kI-xFpaRwr&q=85&s=51f370c83fd21c677b0d87db8b6ea3a4" alt="Modify Header Response" width="1239" height="355" data-path="img/2.10/modify-header-response.png" />

   5. Click **Add**

   6. Click **Update**

   <img src="https://mintcdn.com/tyk/_n1j2nedxXfbDX-s/img/2.10/update_number_conversion.png?fit=max&auto=format&n=_n1j2nedxXfbDX-s&q=85&s=ac8080256ec39b4295d76d34d8fb3396" alt="Update API" width="1110" height="134" data-path="img/2.10/update_number_conversion.png" />

## Testing the Endpoint

You now need to test the endpoint. We are going to use Postman.

<Note>
  We have not set up any Authentication for this API, it has defaulted to `Open (Keyless)`.
</Note>

1. Copy the URL for your NumberConversion API with the NumberToWords endpoint - `https://tyk-url/numberconversion/NumberToWords/`
2. Paste it as a POST URL in the Postman URL Request field
3. Enter the following as a raw Body request

```json  theme={null}
{
    "numberToConvert": 35
}
```

Your Postman request should look similar to below (apart from the URL used)

<img src="https://mintcdn.com/tyk/m6xbM9kI-xFpaRwr/img/2.10/postman_soap_rest.png?fit=max&auto=format&n=m6xbM9kI-xFpaRwr&q=85&s=f2f512c3869c691286f0c4bc829f9473" alt="Postman" width="920" height="712" data-path="img/2.10/postman_soap_rest.png" />

Built with [Mintlify](https://mintlify.com).
