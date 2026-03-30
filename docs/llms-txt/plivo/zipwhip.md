# Source: https://plivo.com/docs/messaging/migrate/zipwhip.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Technical Guide: Migrating from Zipwhip to Plivo

> Migrate your SMS integration from Zipwhip to Plivo with API comparisons

Migrating from Zipwhip to Plivo is a seamless and painless process. The two companies’ API structures, implementation mechanisms, SMS message processing, and MMS message processing are similar. We wrote this technical comparison between Zipwhip and Plivo APIs so that you can scope the changes for a seamless migration.

## Understanding the differences between Zipwhip and Plivo development

Most of the APIs and features that are available on Zipwhip are also available on Plivo, and the steps involved are almost identical. This table gives a side-by-side comparison of the two companies’ features and APIs. An added advantage with Plivo is that not only can you code using the old familiar API method, you can also implement your use cases using PHLO (Plivo High Level Objects), a visual workflow builder that lets you create workflows by dragging and dropping components onto a canvas — no coding required.

<table>
  <tr>
    <td><strong>Features and APIs</strong></td>
    <td><strong>Zipwhip</strong></td>
    <td><strong>Plivo</strong></td>
    <td><strong>Similarities</strong></td>
    <td><strong>Implementation Interface</strong></td>
  </tr>

  <tr>
    <td><a href="/messaging/">SMS API</a>: Send SMS messages</td>
    <td>✅</td>
    <td>✅</td>
    <td>Request and response variables’ structure</td>

    <td>
      API<br />
      PHLO<br />
    </td>
  </tr>

  <tr>
    <td><a href="/messaging/">MMS API</a>: Send MMS messages</td>
    <td>✅</td>
    <td>✅</td>
    <td>Request and response variables’ structure</td>

    <td>
      API<br />
      PHLO<br />
    </td>
  </tr>

  <tr>
    <td><a href="https://cx.plivo.com/home">10DLC</a>: 10-digit long code (10DLC) phone numbers</td>
    <td>✅</td>
    <td>✅</td>
    <td>Registration process and usage</td>
    <td><a href="https://cx.plivo.com/home">Console</a></td>
  </tr>

  <tr>
    <td><a href="/messaging/concepts/powerpack/">Managed number pool</a> for US/CA Messaging</td>
    <td>NA</td>
    <td>Powerpack</td>
    <td>Feature parity</td>

    <td>
      API<br />
      Console<br />
    </td>
  </tr>

  <tr>
    <td><a href="/numbers/">Phone number management</a></td>
    <td>✅</td>
    <td>✅</td>
    <td>Feature parity</td>

    <td>
      API<br />
      Console<br />
    </td>
  </tr>

  <tr>
    <td><a href="/messaging/concepts/callbacks/">HTTP callbacks</a></td>
    <td>✅</td>
    <td>✅</td>
    <td>Feature parity</td>

    <td>
      API<br />
      XML<br />
      PHLO<br />
    </td>
  </tr>
</table>

## Plivo account creation

Start by [signing up for a free trial account](https://cx.plivo.com/signup) that you can use to experiment with and learn about our services. The free trial account comes with free credits, and you can [add more](https://cx.plivo.com/billing/payment-methods) as you go along. You can also [add a phone number](https://cx.plivo.com/phone-numbers) to your account to start testing the full range of our voice and SMS features. A page in our support portal [walks you through the signup process](https://support.plivo.com/hc/en-us/articles/360041203772).

You can also port your numbers from Zipwhip to Plivo, as we explain in [this guide](/messaging/migrate/twilio/#porting-your-existing-numbers-from-twilio-to-plivo).

## Migrating your SMS application

You can migrate your existing application from Zipwhip to Plivo by refactoring the code, or you can try our intuitive visual workflow builder [PHLO](https://cx.plivo.com/agents). To continue working with the APIs, use one of the quickstart guides to set up a development environment for your preferred language. Plivo offers server SDKs in seven languages: [PHP](/messaging/quickstart/php-quickstart/), [Node.js](/messaging/quickstart/node-quickstart/), [.NET](/messaging/quickstart/dotnet-quickstart/), [Java](/messaging/quickstart/java-quickstart/), [Python](/messaging/quickstart/python-quickstart/), [Ruby](/messaging/quickstart/ruby-quickstart/), and [Go](/messaging/quickstart/go-quickstart/). For another alternative that lets you evaluate Plivo’s SMS APIs and their request and response structure, use our [Postman collections](/messaging/quickstart/postman/).

### How to send an SMS message

Let’s take a look at the process of refactoring the code to migrate your app from Zipwhip to Plivo to set up a simple cURL application to send an SMS message by changing just a few lines of code.

<CodeGroup>
  ```sh Zipwhip theme={null}
  curl -X POST \
  "https://api.zipwhip.com/message/send" \
  -d "session=$ZIPWHIP_SESSION_KEY" \
  -d "contacts=$MOBILE_PHONE_NUMBER" \
  -d "body=Hello from Zipwhip API"
  ```

  ```sh Plivo theme={null}
  curl -i --user auth_id:auth_token \
      -H "Content-Type: application/json" \
      -d '{"src": "<sender_id>","dst": "<destination_number>", "text": "Hello from Plivo API"}' \
  https://api.plivo.com/v1/Account/{auth_id}/Message/
  ```
</CodeGroup>

Alternatively, you can implement the same functionality using one of our [PHLO templates](https://cx.plivo.com/agents). For example, if you want to send an SMS message, your PHLO would look like this.

<Frame>
  <img src="https://mintcdn.com/plivo/sqGJ0ONkT5kTuesy/images/send_sms.gif?s=12a69e7e8d9a8ed97671dd9889927a6f" alt="Create PHLO for outbound SMS" width="1024" height="540" data-path="images/send_sms.gif" />
</Frame>

## Migrating your MMS application

### How to send an MMS message

Let’s take a look at the process of refactoring the code to migrate another application from Zipwhip to Plivo — a simple cURL application to send an MMS message — by changing just a few lines of code.

<CodeGroup>
  ```sh Zipwhip theme={null}
  curl -X POST \
  "https://api.zipwhip.com/messaging/send" \
  -H "Content-Type: multipart/form-data" \
  -F "session=$ZIPWHIP_SESSION_KEY" \
  -F "to=$MOBILE_PHONE_NUMBER" \
  -F "file=@owl.png;type=image/png"
  ```

  ```sh Plivo theme={null}
  curl -i --user auth_id:auth_token \
      -H "Content-Type: application/json" \
      -d '{"src": "<sender_id>","dst": "<destination_number>", "text": "Hello from Plivo", "type": "mms","media_urls": ["https://media.giphy.com/media/26gscSULUcfKU7dHq/source.gif"],"url":"https://<yourdomain></yourdomain>.com/sms_status/"}' \
      https://api.plivo.com/v1/Account/{auth_id}/Message/
  ```
</CodeGroup>

Alternatively, you can implement the same functionality using one of our [PHLO templates](https://cx.plivo.com/agents). For example, if you want to send an MMS message, your PHLO would look like this.

<Frame>
  <img src="https://mintcdn.com/plivo/sqGJ0ONkT5kTuesy/images/send_mms.gif?s=4a6dbc8c32d380d62826ba54973dc6f3" alt="Create PHLO for outbound MMS" width="1024" height="583" data-path="images/send_mms.gif" />
</Frame>

### More use cases

You can migrate applications for other use cases too:

* [Reply to incoming SMS messages](/messaging/use-cases/reply-to-incoming-sms/node/)
* [Two-factor authentication](/messaging/use-cases/2-factor-authentication/node/)
* [Forward incoming SMS messages](/messaging/use-cases/forward-incoming-sms/node/)
* [Delivery reports](/messaging/use-cases/delivery-reports/node/)
* [SMS alerts](/messaging/use-cases/sms-alert/node/)
* [SMS marketing](/messaging/use-cases/sms-marketing/node/)
* [SMS notifications](/messaging/use-cases/sms-notification/node/)
* [SMS survey](/messaging/use-cases/sms-survey/node/)
* [SMS autoresponder](/messaging/use-cases/sms-autoresponder/node/)
* [Forward SMS to email](/messaging/use-cases/forward-sms-to-email/node/)
* [Receive MMS](/messaging/use-cases/receive-mms/python/)

## Porting your existing numbers from Zipwhip to Plivo

If you want to continue using your phone numbers from Zipwhip, you can port the numbers to Plivo painlessly without having any downtime on your services for your customers. Our [number porting guide](/numbers/number-porting/) shows you how to initiate the process.

## Buy new phone numbers for your migrated app

You can buy new phone numbers on the Plivo platform for your migrated applications as well. Plivo provides a self-serve [console](https://cx.plivo.com/phone-numbers) to buy new numbers and to manage them. You can also use the [Phone Numbers API](/numbers/api/overview/) for number management. You can check this [guide](/numbers/guides/buy-a-number/) to learn more.
