# Source: https://plivo.com/docs/voice/concepts/callbacks.md

# Source: https://plivo.com/docs/messaging/concepts/callbacks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# SMS Callbacks

> SMS delivery report statuses, DLR callbacks, and troubleshooting failed deliveries

You can create analytics on your SMS and MMS traffic by using event-based webhooks — user-defined HTTP callbacks — to track the delivery status of outgoing and incoming messages.

For every SMS and MMS message you send and receive, Plivo sends a status update to a URL you configure as a callback. You can store the information on your server for delivery status analysis.

<Frame>
    <img src="https://mintcdn.com/plivo/sqGJ0ONkT5kTuesy/images/sms-callbacks.png?fit=max&auto=format&n=sqGJ0ONkT5kTuesy&q=85&s=64a94312c5c0ea3237779f8384a3eb8a" alt="SMS callbacks" width="813" height="232" data-path="images/sms-callbacks.png" />
</Frame>

The webhooks you integrate with Plivo are triggered by incoming messages or calls. Upon one of these events, Plivo makes an HTTP request (POST or GET) to an endpoint URL you’ve configured for the webhook. In the callback, you can send all the information related to the message either in the POST request’s body or the GET request’s [query parameters](/messaging/api/message/#message-status-callbacks). To handle a webhook, you must create a listener (web app) that can accept these HTTP requests from Plivo.

## Webhooks for outbound SMS

Here’s how to use Plivo APIs to send SMS messages from your web application and include a callback URL. Before you get started, you must buy an SMS-enabled Plivo phone number to send messages to the US and Canada. You can purchase numbers from Phone Numbers > [Buy Number](https://cx.plivo.com/phone-numbers) section of the Plivo console, or by using the [Numbers API](/numbers/api/phone-number/).

<Frame>
    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/buy-new-number.png?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=fac7642e83b674522bc93de7a33306db" alt="Buy a New Plivo Number" width="1440" height="402" data-path="images/buy-new-number.png" />
</Frame>

For Plivo to invoke your webhook and send HTTP requests, you must configure the URL parameter with your webhook URL and set the method as either POST or GET, then specify this URL for message status-related callbacks.

See the [send SMS usage guide](/messaging/use-cases/send-an-sms/node/) for more information about how to send SMS messages on a two-way SMS-enabled Plivo phone number.

### Code

<CodeGroup>
  ```py Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>','<auth_token>')
  response = client.messages.create(
      src='<sender_id>',
      dst='<destination_number>',
      text='Hello, this is a sample text',
      url='https://<yourdomain>.com/sms_status/',
  )
  print(response)
  # prints only the message_uuid
  print(response.message_uuid)
  ```

  ```rb Ruby theme={null}
  require "plivo"
  include Plivo

  api = RestClient.new("<auth_id>","<auth_token>")
  response = api.messages.create(
  	src:'<sender_id>', 
  	dst:"<destination_number>", 
  	text:"Hello, this is a sample text",
  	url: "https://<yourdomain>.com/sms_status/",
  )
  puts response
  #Prints only the message_uuid
  puts response.message_uuid
  ```

  ```js Node.js theme={null}
  var plivo = require('plivo');

  (function main() {
      'use strict';
      var client = new plivo.Client("<auth_id>", "<auth_token>");
      client.messages.create({
          src: "+12025550000",
          dst: "+12025551111", 
          text: "Hello, this is a sample message",
          method: "GET",
          url: "https://<yourdomain>.com/sms_status/"
      }, ).then(function(response) {
          console.log(response);
          //Prints only the message_uuid
          console.log(response.messageUuid);
      }, );
  })();
  ```

  ```php PHP theme={null}
  <?php
  require 'vendor/autoload.php';
  use Plivo\RestClient;

  $client = new RestClient("<auth_id>","<auth_token>");
  $response = $client->messages->create(
    [  
      "src" => "<sender_id>",
      "dst" => "<destination_number>",
      "text"  =>"Hello, this is a sample text",
      "url"=>"https://<yourdomain>.com/sms_status/",
   ]
  );
  print_r($response);
  // Prints only the message_uuid
  print_r($response->getmessageUuid(0));
  ?>
  ```

  ```java Java theme={null}
  import java.io.IOException;
  import java.net.URL;
  import java.util.Collections;

  import com.plivo.api.Plivo;
  import com.plivo.api.exceptions.PlivoRestException;
  import com.plivo.api.models.message.Message;
  import com.plivo.api.models.message.MessageCreateResponse;

  class MessageCreate {
      public static void main(String[] args) {
          Plivo.init("<auth_id>", "<auth_token>");
          try {
              MessageCreateResponse response = Message.creator("+12025550000", Collections.singletonList("+12025551111"),
                      "Hello, this is a test message").url(new URL("https://<yourdomain>.com/sms_status/"))
                      .create();
              System.out.println(response);
              // Prints only the message_uuid
              System.out.println(response.getMessageUuid());
          }

          catch (PlivoRestException | IOException e) {
              e.printStackTrace();
          }
      }
  }
  ```

  ```go Go theme={null}
  package main

  import (
  	"fmt"

  	"github.com/plivo/plivo-go/v7"
  )

  func main() {
  	client, err := plivo.NewClient("<auth_id>", "<auth_token>", &plivo.ClientOptions{})
  	if err != nil {
  		fmt.Print("Error", err.Error())
  		return
  	}
  	response, err := client.Messages.Create(
  		plivo.MessageCreateParams{
  			Src:  "<sender_id>",
  			Dst:  "<destination_number>",
  			Text: "Hello, this is a sample text",
  			URL:  "https://<yourdomain>.com/sms_status/",
  		},
  	)
  	if err != nil {
  		fmt.Print("Error", err.Error())
  		return
  	}
  	fmt.Printf("Response: %#v\n", response)
  	// Prints only the message_uuid
  	fmt.Printf("Response: %#v\n", response.MessageUUID)
  }
  ```

  ```cs .NET theme={null}
  using System;
  using System.Collections.Generic;
  using Plivo;

  namespace PlivoExamples
  {
      internal class Program
      {
          public static void Main(string[] args)
          {
              var api = new PlivoApi("<auth_id>","<auth_token>");
              var response = api.Message.Create(
                  src: "+12025550000",
                  dst: "+12025551111",
                  text: "Hello, this is sample text",
                  url: "https://<yourdomain>.com/sms_status/"
                  );
              Console.WriteLine(response);
              // Prints the message_uuid
              Console.WriteLine(response.MessageUuid[0]);
          }
      }
  }
  ```

  ```sh Curl theme={null}
  curl -i --user auth_id:auth_token \
  -H "Content-Type: application/json" \
  -d '{"src": "+12025550000","dst": "+12025551111", "text": "Hello, this is a sample text.", "url":"https://<yourdomain>.com/sms_status/"}' \
  https://api.plivo.com/v1/Account/{auth_id}/Message/
  ```
</CodeGroup>

<Note>
  <strong>Notes:</strong>

  * Replace the `auth_id` and `auth_token` placeholders with your authentication credentials, which you can find on the Overview screen of the <a href="https://cx.plivo.com/home">Plivo console</a>.

  * Replace the `src` placeholder with the phone number you purchased and `dst` with the phone number you’ll be sending SMS messages to. Both should be in <a rel="nofollow" href="https://en.wikipedia.org/wiki/E.164">E.164 format</a>.

  * Replace `https://yourdomain.com/sms_status/` with the webhook URL you’ve set up.

  * If you’re using a Plivo trial account, you can send SMS messages only to phone numbers that have been verified with Plivo. You can verify phone numbers through the Phone Numbers <a href="https://cx.plivo.com/home">Sandbox Numbers</a> page.
</Note>

## Webhooks for inbound SMS

See the [receive SMS usage guide](/messaging/use-cases/receive-sms/node/) for more information about how to receive SMS messages on a two-way SMS-enabled Plivo phone number.

## Handle callbacks in your web app

To handle callbacks in your app, your endpoint should:

* Capture HTTP requests
* Respond to the requests

When Plivo sends the HTTP request callbacks to the webhook during an event, you should capture the request (POST or GET based on the type you’ve defined for the URL) and respond with a 200 OK response. You can store the callback data to your database.

<Note>
  <strong>Note:</strong> Plivo automatically retries webhooks three times if an HTTP 200 status code is not returned:

  * First at 60 seconds after the original attempt.
  * Second at 120 seconds after the first retry attempt.
  * Third at 240 seconds after the second retry attempt.
</Note>

## Test and validate

Let’s take a look at an example. Typically, you would include a URL that points to your web app, but we’ll use a URL from [RequestBin](https://requestbin.com/), a service that lets you collect, analyze, and debug HTTP requests, so we can check the callbacks.

* Create a new bin in RequestBin.
* Replace the “url” placeholder with the URL of the new bin.
* Run the code that appear above. You should receive the SMS message on the phone number defined in destination field, and see callback requests in RequestBin similar to the screenshots below for callback events such as queued, sent, and delivered.

### Queued status callback

<Frame>
    <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/queued-1.png?fit=max&auto=format&n=7-odxN9fJG_Dg1dt&q=85&s=46188026e07272876d8944b3024cb7c7" alt="Queued status event" width="2448" height="1196" data-path="images/queued-1.png" />
</Frame>

### Sent status callback

<Frame>
    <img src="https://mintcdn.com/plivo/sqGJ0ONkT5kTuesy/images/sent-1.png?fit=max&auto=format&n=sqGJ0ONkT5kTuesy&q=85&s=40979ed9f24bafe514834c8de70ae56b" alt="Sent status event" width="2448" height="1218" data-path="images/sent-1.png" />
</Frame>

### Delivered status callback

<Frame>
    <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/delivered-1.png?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=864691f2e16cee36d68a2ea86d1bf997" alt="Delivered status event" width="2448" height="1238" data-path="images/delivered-1.png" />
</Frame>

<Note>
  <strong>Note:</strong>

  * Callbacks for incoming messages work in the same manner as outbound messages.
  * You should also receive statuses such as undelivered or failed, and some messages may remain in the sent state. See more information about our <a href="https://support.plivo.com/hc/en-us/articles/360041315292">different SMS statuses</a>.
</Note>

## Validating callbacks

To avoid spoof attacks, you can validate the callbacks that your server URL receives. All requests made by Plivo to your server URLs include X-Plivo-Signature-V2, X-Plivo-Signature-Ma-V2, and X-Plivo-Signature-V2-Nonce HTTP headers. You can use them to validate that a request is from Plivo, as we discuss in our [signature validation guide](/messaging/concepts/signature-validation/).

## Conversion feedback to Plivo

You can store the data from the message status callbacks in your database for analytics. You can also choose to provide the data to Plivo as message delivery feedback. Plivo’s [Conversion Feedback API](/messaging/concepts/conversion-feedback/) lets you update Plivo on conversions for your critical two-factor authentication (2FA) and one-time password (OTP) messages. Your feedback helps us ensure consistently high delivery rates in countries where carrier networks may be unstable. Plivo’s machine-learning-based dynamic routing engine uses all of our customers’ feedback to ensure that your messages are delivered over the best-performing carrier route to the destination mobile network.
