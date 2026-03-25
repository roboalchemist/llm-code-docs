# Source: https://plivo.com/docs/voice/concepts/sip-endpoint.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Plivo SIP endpoints

> Register SIP phones and softphones with Plivo for voice calls

Plivo endpoints expand the capabilities of your existing SIP phones, allowing you to add custom business logic when you make or receive calls. Traditionally, SIP phones had very basic functionality and needed to be connected to a PBX to bring them to life. With Plivo endpoints, you no longer need to set up and manage your phone system. Any Plivo application can implement the business logic needed to control your SIP phone, using any of your favorite coding languages without any need to understand the telecommunications details. Plivo supports all common SIP-based softphones and hardware phones.

With Plivo and your SIP phones, you can implement:

* **Instant conferencing** — You can add calls made via a SIP phone registered with Plivo directly to a conference bridge.
* **Access control** — With a few lines of code, you can add the ability to restrict calls made from SIP phones or limit a phone to only accept calls.
* **Monitoring and reporting** — You can monitor all calls made or received on a SIP phone, and create custom dashboards and reports to analyze the data you get from the APIs.
* **Smart routing** — You can add intelligent extensions and shortcuts to route calls to and from traditional phone networks and WebRTC-enabled devices.

## How it works

Once you configure and set up your SIP phone, register it with Plivo. When you initiate a call using the SIP phone, you don’t connect directly to another phone or extension. Instead, you instruct Plivo to fetch XML from the attached application on your server to handle the call request. This is similar to the way that Plivo handles incoming calls from a regular phone number. You can use all Plivo XML elements to handle a call request. You can also use the Dial element to dial out to a regular phone, WebRTC device, or another SIP phone.

## Getting started

1. Sign up for a [Plivo account](https://cx.plivo.com/signup).

2. Create an endpoint by visiting Voice > [Endpoints](https://cx.plivo.com/endpoints), clicking on Add New Endpoint, and filling in the required details. The Username should be a unique ID for the endpoint.

3. Plivo adds random numbers after the username you enter. If, for instance, you choose “obiwan” as your username, Plivo might set it up as “obiwan01356015703850523884." Specify a password you can use to authenticate the endpoint. Set an alias (maybe “ben” in this case) which Plivo uses when it displays all your endpoints, and optionally a subaccount to associate the endpoint with.

## Using a default dialer application

To start making calls, attach Plivo’s default direct dial application to the endpoint you created.

* If you already created the endpoint, go to the Endpoints page and click on the endpoint username. This will open an endpoint edit window. Select Direct Dial from the Application drop-down list.

<Frame>
    <img src="https://mintcdn.com/plivo/kC7RdeaQ9U2h_t61/images/Directdial.jpg?fit=max&auto=format&n=kC7RdeaQ9U2h_t61&q=85&s=58cfd62359434c02647971913360c1e7" alt="SIP Endpoint" width="1440" height="705" data-path="images/Directdial.jpg" />
</Frame>

* If you’re creating a new endpoint, select Direct Dial from the Application drop-down list.

## Customizing the endpoint application

When you make a call from a softphone, Plivo sends a request to the answer URL of the application attached to the endpoint with call-related parameters. To process the call, Plivo requires a valid XML response from the answer URL. Let’s say, in our case, that we want to create a quick dial application and make an outbound call to the number entered from the softphone. The answer URL will receive a request with the From and To parameters. Our application needs to parse these parameters and return a Dial XML element with the correct attributes.

```xml  theme={null}
<Response>
  <Dial callerid="18004321321">
  <Number>18003231234</Number>
</Dial>
</Response>
```

When this XML is returned to the request, Plivo will make an outbound call to 18003231234 and connect it to the softphone.

For technical information, see our [Endpoint API reference documentation](/voice/api/endpoints/).

## Configure your SIP phone

Once you have an endpoint set up you can associate a SIP phone with it. The way to do that varies depending on the phone. Here‘s how the process works with a Bria Solo softphone.

* Create an account using the [Bria portal](https://www.counterpath.com/bria-solo/).

* To configure a voice account, use the details of the Plivo SIP endpoint you created.

<Frame>
    <img src="https://mintcdn.com/plivo/kC7RdeaQ9U2h_t61/images/account_creation.png?fit=max&auto=format&n=kC7RdeaQ9U2h_t61&q=85&s=7c91d7a8e1d73708ccad597523c28892" alt="X-lite preference" width="3360" height="1878" data-path="images/account_creation.png" />
</Frame>

* Download and install the softphone software. If you’re on Mac or Windows, download [Bria Solo](https://www.counterpath.com/bria-solo/) (formerly X-Lite). On Linux, download [Blink](https://icanblink.com/). For this tutorial, we use Bria Solo.

* Open the application and enable auto import voice account details to import the SIP account details and credentials.

<Note>
  <strong>Note:</strong> Field names may vary based on make and model of the SIP phone, but the configuration will still work.
</Note>

<Frame>
    <img src="https://mintcdn.com/plivo/sqGJ0ONkT5kTuesy/images/sipaccountdetails.png?fit=max&auto=format&n=sqGJ0ONkT5kTuesy&q=85&s=e02596081b9da78ffacc27b21d9e7f03" alt="X-lite account" width="808" height="761" data-path="images/sipaccountdetails.png" />
</Frame>

* Click on OK when you’re done.

* Your endpoint entry in the list should show as Enabled, indicating that your SIP phone successfully registered with Plivo.

## Examples

We have examples of a direct dial application written in multiple languages on [GitHub](https://github.com/plivo/directdial) that you can customize based on your needs.
