# Source: https://plivo.com/docs/messaging/use-cases/whatsapp/getting-started/inbound-message/inbound-message.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Receive Inbound Messages and Interactions

> Handle inbound WhatsApp messages and user interactions via Plivo

<Tabs>
  <Tab title="Node">
    ## Overview

    This guide shows how to send a non-templated WhatsApp text message to a destination WhatsApp number using our APIs. Follow these instructions:

    ## Prerequisites

    To get started, you need a Plivo account — [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. If this is your first time using Plivo APIs, follow our instructions to [set up a Node.js development environment](/sdk/server/set-up-node-dev-environment-api-messaging/).

    Non-templated WhatsApp messages can be sent as a reply to a user-initiated conversation (Service conversation) or if there is an existing ongoing conversation created previously by sending a templated WhatsApp message.

    ## Create the send WhatsApp application

    Create a file called `send_whatsapp.js` and paste into it this code.

    ```javascript  theme={null}
    var plivo = require('plivo');

    var client = new plivo.Client("<auth_id>", "<auth_token>");
    client.messages.create(
          {
             src:"+14151112221",
             dst:"+14151112222",
             type:"whatsapp",
             text: "Hello, this is sample text",
             url: "https://foo.com/sms_status/"
           }
           ).then(function (response) {
             console.log(response);
            });
    ```

    Replace the auth placeholders with your authentication credentials from the [Plivo console](https://cx.plivo.com/home). Replace the phone number placeholders with actual phone numbers in [E.164 format](https://en.wikipedia.org/wiki/E.164) (for example, +12025551234). `src` should be a phone number registered against your WhatsApp Business Account. `dst` should be the destination WhatsApp number that you want to receive the message.

    Text is passed using the `text` parameter. For details about this param, refer to our [documentation](/messaging/quickstart/node-quickstart/).

    <Note>
      <strong>Note:</strong> We recommend that you store your credentials in the`auth_id` and `auth_token` environment variables to avoid the possibility of accidentally committing them to source control. If you do this, you can initialize the client with no arguments and Plivo will automatically fetch the values from the environment variables. You can use `process.env` to store environment variables and fetch them when initializing the client.
    </Note>

    ## Test

    Save the file and run it.

    <Note>
      <strong>Note:</strong> If you’re using a Plivo Trial account, you can send messages only to phone numbers that have been verified with Plivo. You can verify (sandbox) a number by going to the console’s Phone Numbers > <a href="https://cx.plivo.com/home">Sandbox Numbers</a> page.
    </Note>
  </Tab>

  <Tab title="Ruby">
    ## Overview

    This guide shows how to send a non-templated WhatsApp text message to a destination WhatsApp number using our APIs. Follow these instructions:

    ## Prerequisites

    To get started, you need a Plivo account — [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. If this is your first time using Plivo APIs, follow our instructions to [set up a Ruby development environment](/sdk/server/set-up-ruby-dev-environment-api-messaging/).

    Non-templated WhatsApp messages can be sent as a reply to a user-initiated conversation (Service conversation) or if there is an existing ongoing conversation created previously by sending a templated WhatsApp message.

    ## Create the send WhatsApp application

    Create a file called `send_whatsapp.rb` and paste into it this code.

    ```rb  theme={null}
    require "plivo"
    include Plivo

    api = RestClient.new("<auth_id>","<auth_token>")
    response = api.messages.create(
            src: "+14151112221",
            dst:"+14151112222",
            type:"whatsapp",
            text:"Hello, this is sample text",
            url: "https://<yourdomain>.com/sms status/",
    )
    puts response
    #Prints only the message_uuid
    puts response.message_uuid
    ```

    Replace the auth placeholders with your authentication credentials from the [Plivo console](https://cx.plivo.com/home). Replace the phone number placeholders with actual phone numbers in [E.164 format](https://en.wikipedia.org/wiki/E.164) (for example, +12025551234).

    `src`

    should be a phone number registered against your WhatsApp Business Account.

    `dst`

    should be the destination WhatsApp number that you want to receive the message.

    Text is passed using the

    `text`

    parameter. For details about this param, refer to our [documentation](/messaging/quickstart/node-quickstart/).

    <Note>
      <strong>Note:</strong> We recommend that you store your credentials in the`auth_id` and `auth_token` environment variables to avoid the possibility of accidentally committing them to source control. If you do this, you can initialize the client with no arguments and Plivo will automatically fetch the values from the environment variables. You can use `process.env` to store environment variables and fetch them when initializing the client.
    </Note>

    ## Test

    Save the file and run it.

    <Note>
      <strong>Note:</strong> If you’re using a Plivo Trial account, you can send messages only to phone numbers that have been verified with Plivo. You can verify (sandbox) a number by going to the console’s Phone Numbers > <a href="https://cx.plivo.com/home">Sandbox Numbers</a> page.
    </Note>
  </Tab>

  <Tab title="Python">
    ## Overview

    This guide shows how to send a non-templated WhatsApp text message to a destination WhatsApp number using our APIs. Follow these instructions:

    ## Prerequisites

    To get started, you need a Plivo account — [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. If this is your first time using Plivo APIs, follow our instructions to [set up a Python development environment](/sdk/server/set-up-python-dev-environment-api-messaging/).

    Non-templated WhatsApp messages can be sent as a reply to a user-initiated conversation (Service conversation) or if there is an existing ongoing conversation created previously by sending a templated WhatsApp message.

    ## Create the send WhatsApp application

    Create a file called `send_whatsapp.py` and paste into it this code.

    ```python  theme={null}
    import plivo
    client = plivo.RestClient('<auth_id>','<auth_token>')
    response = client.messages.create(
             src="+14151112221",
             dst="+14151112222",
             type_="whatsapp",
             text="Hello, from Python!"
           )
    print(response)
    #prints only the message_uuid
    print(response.message_uuid)
    ```

    Replace the auth placeholders with your authentication credentials from the [Plivo console](https://cx.plivo.com/home). Replace the phone number placeholders with actual phone numbers in [E.164 format](https://en.wikipedia.org/wiki/E.164) (for example, +12025551234).

    `src`

    should be a phone number registered against your WhatsApp Business Account.

    `dst`

    should be the destination WhatsApp number that you want to receive the message.

    Text is passed using the

    `text`

    parameter. For details about this param, refer to our [documentation](/messaging/quickstart/node-quickstart/).

    <Note>
      <strong>Note:</strong> We recommend that you store your credentials in the `auth_id` and `auth_token` environment variables to avoid the possibility of accidentally committing them to source control. If you do this, you can initialize the client with no arguments and Plivo will automatically fetch the values from the environment variables. You can use `process.env` to store environment variables and fetch them when initializing the client.
    </Note>

    ## Test

    Save the file and run it.

    <Note>
      <strong>Note:</strong> If you’re using a Plivo Trial account, you can send messages only to phone numbers that have been verified with Plivo. You can verify (sandbox) a number by going to the console’s Phone Numbers > <a href="https://cx.plivo.com/home">Sandbox Numbers</a> page.
    </Note>
  </Tab>

  <Tab title="PHP">
    ## Overview

    This guide shows how to send a non-templated WhatsApp text message to a destination WhatsApp number using our APIs. Follow these instructions:

    ## Prerequisites

    To get started, you need a Plivo account — [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. If this is your first time using Plivo APIs, follow our instructions to [set up a PHP development environment](/sdk/server/php-sdk/).

    Non-templated WhatsApp messages can be sent as a reply to a user-initiated conversation (Service conversation) or if there is an existing ongoing conversation created previously by sending a templated WhatsApp message.

    ## Create the send WhatsApp application

    Create a file called `send_whatsapp.php` and paste into it this code.

    ```php  theme={null}
    <?php
    require 'vendor/autoload.php';
    use Plivo\RestClient;

    $client = new RestClient("<auth_id>","<auth_token>");
    $response = $client->messages->create(
    [
    "src" => "+14151112221",
    "dst" => "+14151112222",
    "text" =>"Hello, this is sample text",
    "type"=>"whatsapp",
    "url"=>"https://foo.com/sms_status/"
    ]
    );
    print_r($response);
    // Prints only the message_uuid
    print_r($response->getmessageUuid(0));
    ?>
    ```

    Replace the auth placeholders with your authentication credentials from the [Plivo console](https://cx.plivo.com/home). Replace the phone number placeholders with actual phone numbers in [E.164 format](https://en.wikipedia.org/wiki/E.164) (for example, +12025551234). `src` should be a phone number registered against your WhatsApp Business Account. `dst` should be the destination WhatsApp number that you want to receive the message.

    Text is passed using the `text` parameter. For details about this param, refer to our [documentation](/messaging/quickstart/node-quickstart/).

    <Note>
      <strong>Note:</strong> We recommend that you store your credentials in the`auth_id` and `auth_token` environment variables to avoid the possibility of accidentally committing them to source control. If you do this, you can initialize the client with no arguments and Plivo will automatically fetch the values from the environment variables. You can use `process.env` to store environment variables and fetch them when initializing the client.
    </Note>

    ## Test

    Save the file and run it.

    <Note>
      <strong>Note:</strong> If you’re using a Plivo Trial account, you can send messages only to phone numbers that have been verified with Plivo. You can verify (sandbox) a number by going to the console’s Phone Numbers > <a href="https://cx.plivo.com/home">Sandbox Numbers</a> page.
    </Note>
  </Tab>

  <Tab title=".NET">
    ## Overview

    This guide shows how to send a non-templated WhatsApp text message to a destination WhatsApp number using our APIs. Follow these instructions:

    ## Prerequisites

    To get started, you need a Plivo account — [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. If this is your first time using Plivo APIs, follow our instructions to [set up a .NET development environment](/sdk/server/net-sdk/).

    Non-templated WhatsApp messages can be sent as a reply to a user-initiated conversation (Service conversation) or if there is an existing ongoing conversation created previously by sending a templated WhatsApp message.

    ## Create the send WhatsApp application

    Create a file called `send_whatsapp.net` and paste into it this code.

    ```c#  theme={null}
    "using System;
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
                    src: "+14151112221",
                    dst: "+14151112222",
                    type: "whatsapp",
                    text: "Hello, this is sample text",
                    url: "https://<yourdomain>.com/sms_status/"
                    );
                Console.WriteLine(response);
                // Prints the message_uuid
                Console.WriteLine(response.MessageUuid[0]);
            }
        }
    }
    "
    ```

    Replace the auth placeholders with your authentication credentials from the [Plivo console](https://cx.plivo.com/home). Replace the phone number placeholders with actual phone numbers in [E.164 format](https://en.wikipedia.org/wiki/E.164) (for example, +12025551234).

    `src`

    should be a phone number registered against your WhatsApp Business Account.

    `dst`

    should be the destination WhatsApp number that you want to receive the message.

    Text is passed using the

    `text`

    parameter. For details about this param, refer to our [documentation](/messaging/quickstart/node-quickstart/).

    <Note>
      <strong>Note:</strong> We recommend that you store your credentials in the `auth_id` and `auth_token` environment variables to avoid the possibility of accidentally committing them to source control. If you do this, you can initialize the client with no arguments and Plivo will automatically fetch the values from the environment variables. You can use `process.env` to store environment variables and fetch them when initializing the client.
    </Note>

    ## Test

    Save the file and run it.

    <Note>
      <strong>Note:</strong> If you’re using a Plivo Trial account, you can send messages only to phone numbers that have been verified with Plivo. You can verify (sandbox) a number by going to the console’s Phone Numbers > <a href="https://cx.plivo.com/home">Sandbox Numbers</a> page.
    </Note>
  </Tab>

  <Tab title="Java">
    ## Overview

    This guide shows how to send a non-templated WhatsApp text message to a destination WhatsApp number using our APIs. Follow these instructions:

    ## Prerequisites

    To get started, you need a Plivo account — [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. If this is your first time using Plivo APIs, follow our instructions to [set up a Java development environment](/sdk/server/java-sdk).

    Non-templated WhatsApp messages can be sent as a reply to a user-initiated conversation (Service conversation) or if there is an existing ongoing conversation created previously by sending a templated WhatsApp message.

    ## Create the send WhatsApp application

    Create a file called `send_whatsapp.java` and paste into it this code.

    ```java  theme={null}
    import java.io.IOException;
    import java.net.URL;
    import java.util.Collections;

    import com.plivo.api.Plivo;
    import com.plivo.api.exceptions.PlivoRestException;
    import com.plivo.api.models.message.Message;
    import com.plivo.api.models.message.MessageCreateResponse;
    import com.plivo.api.models.message.MessageType;

    class MessageCreate
    {
    public static void main(String [] args)
    {
    Plivo.init("<auth_id>","<auth_token>");
    try
    {
    MessageCreateResponse response = Message.creator("+14151112221","14151112222",
    "Hello, this is a test message")
    .type(MessageType.WHATSAPP)
    .url(new URL("https://<yourdomain>.com/sms_status/") )
    .create();
    System.out.println(response);
    // Prints only the message_uuid
    System.out.println(response.getMessageUuid());
    }

    catch (PlivoRestException | IOException e)
    {
    e.printStackTrace();
    }
    }
    }
    ```

    Replace the auth placeholders with your authentication credentials from the [Plivo console](https://cx.plivo.com/home). Replace the phone number placeholders with actual phone numbers in [E.164 format](https://en.wikipedia.org/wiki/E.164) (for example, +12025551234).

    `src`

    should be a phone number registered against your WhatsApp Business Account.

    `dst`

    should be the destination WhatsApp number that you want to receive the message.

    Text is passed using the

    `text`

    parameter. For details about this param, refer to our [documentation](/messaging/quickstart/node-quickstart/).

    <Note>
      <strong>Note:</strong> We recommend that you store your credentials in the `auth_id` and `auth_token` environment variables to avoid the possibility of accidentally committing them to source control. If you do this, you can initialize the client with no arguments and Plivo will automatically fetch the values from the environment variables. You can use `process.env` to store environment variables and fetch them when initializing the client.
    </Note>

    ## Test

    Save the file and run it.

    <Note>
      <strong>Note:</strong> If you’re using a Plivo Trial account, you can send messages only to phone numbers that have been verified with Plivo. You can verify (sandbox) a number by going to the console’s Phone Numbers > <a href="https://cx.plivo.com/home">Sandbox Numbers</a> page.
    </Note>
  </Tab>

  <Tab title="Go">
    ## Overview

    This guide shows how to send a non-templated WhatsApp text message to a destination WhatsApp number using our APIs. Follow these instructions:

    ## Prerequisites

    To get started, you need a Plivo account — [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. If this is your first time using Plivo APIs, follow our instructions to [set up a Go development environment](/sdk/server/set-up-go-dev-environment-api-messaging/).

    Non-templated WhatsApp messages can be sent as a reply to a user-initiated conversation (Service conversation) or if there is an existing ongoing conversation created previously by sending a templated WhatsApp message.

    ## Create the send WhatsApp application

    Create a file called `send_whatsapp.go` and paste into it this code.

    ```go  theme={null}
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
                      Src:"+14151112221",
                      Dst:"+14151112222",
                      Type:"whatsapp",
                      Text:"Hello, this is sample text",
                      URL: "https://foo.com/sms_status/"
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

    Replace the auth placeholders with your authentication credentials from the [Plivo console](https://cx.plivo.com/home). Replace the phone number placeholders with actual phone numbers in [E.164 format](https://en.wikipedia.org/wiki/E.164) (for example, +12025551234). `src` should be a phone number registered against your WhatsApp Business Account. `dst` should be the destination WhatsApp number that you want to receive the message.

    Text is passed using the `text` parameter. For details about this param, refer to our [documentation](/messaging/quickstart/node-quickstart/).

    <Note>
      <strong>Note:</strong> We recommend that you store your credentials in the`auth_id` and `auth_token` environment variables to avoid the possibility of accidentally committing them to source control. If you do this, you can initialize the client with no arguments and Plivo will automatically fetch the values from the environment variables. You can use `process.env` to store environment variables and fetch them when initializing the client.
    </Note>

    ## Test

    Save the file and run it.

    <Note>
      <strong>Note:</strong> If you’re using a Plivo Trial account, you can send messages only to phone numbers that have been verified with Plivo. You can verify (sandbox) a number by going to the console’s Phone Numbers > <a href="https://cx.plivo.com/home">Sandbox Numbers</a> page.
    </Note>
  </Tab>
</Tabs>
