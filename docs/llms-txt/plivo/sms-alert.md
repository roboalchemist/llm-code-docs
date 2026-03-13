# Source: https://plivo.com/docs/messaging/use-cases/sms-alert/sms-alert.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Send SMS Alerts

> Send SMS alert and notification messages to phone numbers via Plivo

<Tabs>
  <Tab title="Node">
    ## Overview

    This guide shows how to send an SMS alert or notification using Plivo's APIs and the Node.js SDK.

    ***

    ### Prerequisites

    * A Plivo account — [**sign up for free**](https://cx.plivo.com/signup) if you don't have one.
    * An SMS-enabled Plivo phone number to send messages to the US and Canada. You can [**rent a number**](/numbers/) from the Plivo console.
    * Node.js and the Plivo Node.js SDK installed. See our [**Node.js setup guide**](/sdk/server/set-up-node-dev-environment-api-messaging/).

    ***

    ### Create and run the application

    Create a file named `send_sms.js` and paste this code into it. This script initializes the Plivo client and sends a message using the `messages.create` function.

    Replace the `<auth_id>`, `<auth_token>`, `<sender_id>`, and `<destination_number>` placeholders with your actual values.

    ```js  theme={null}
    const plivo = require('plivo');

    async function sendSmsAlert() {
      const client = new plivo.Client("<auth_id>", "<auth_token>");
      try {
        const response = await client.messages.create({
          src: "<sender_id>",
          dst: "<destination_number>",
          text: "Your package TWLO-484-555 was delivered to 742 Evergreen Terrace, Springfield"
        });
        console.log("Message sent successfully:", response);
      } catch (error) {
        console.error("Error sending message:", error);
      }
    }

    sendSmsAlert();
    ```

    ***

    ### Test

    Save the file and run it from your terminal.

    ```shell  theme={null}
    node send_sms.js
    ```

    You should receive the SMS alert on your destination phone.
  </Tab>

  <Tab title="Ruby">
    ## Overview

    This guide shows how to send an SMS alert or notification using Plivo's APIs and the Ruby SDK.

    ***

    ### Prerequisites

    * A Plivo account — [**sign up for free**](https://cx.plivo.com/signup) if you don't have one.
    * An SMS-enabled Plivo phone number to send messages to the US and Canada. You can [**rent a number**](/numbers/) from the Plivo console.
    * Ruby and the Plivo Ruby SDK installed. See our [**Ruby setup guide**](/sdk/server/set-up-ruby-dev-environment-api-messaging/).

    ***

    ### Create and run the application

    Create a file named `send_sms.rb` and paste this code into it. This script initializes the Plivo client and sends a message using the `messages.create` function.

    Replace the `<auth_id>`, `<auth_token>`, `<sender_id>`, and `<destination_number>` placeholders with your actual values.

    ```rb  theme={null}
    require "plivo"
    include Plivo

    begin
      api = RestClient.new("<auth_id>", "<auth_token>")
      response = api.messages.create(
        src: "<sender_id>",
        dst: "<destination_number>",
        text: "Your package TWLO-484-555 was delivered to 742 Evergreen Terrace, Springfield",
      )
      puts response
    rescue PlivoRESTError => e
      puts "Error: " + e.message
    end
    ```

    ***

    ### Test

    Save the file and run it from your terminal.

    ```shell  theme={null}
    ruby send_sms.rb
    ```

    You should receive the SMS alert on your destination phone.
  </Tab>

  <Tab title="Python">
    ## Overview

    This guide shows how to send an SMS alert or notification using Plivo's APIs and the Python SDK.

    ***

    ### Prerequisites

    * A Plivo account — [**sign up for free**](https://cx.plivo.com/signup) if you don't have one.
    * An SMS-enabled Plivo phone number to send messages to the US and Canada. You can [**rent a number**](/numbers/) from the Plivo console.
    * Python and the Plivo Python SDK installed. See our [**Python setup guide**](/sdk/server/set-up-python-dev-environment-api-messaging/).

    ***

    ### Create and run the application

    Create a file named `send_sms.py` and paste this code into it. This script initializes the Plivo client and sends a message using the `messages.create` function.

    Replace the `<auth_id>`, `<auth_token>`, `<sender_id>`, and `<destination_number>` placeholders with your actual values.

    ```py  theme={null}
    import plivo
    from plivo.exceptions import PlivoRestError

    try:
        client = plivo.RestClient('<auth_id>', '<auth_token>')
        response = client.messages.create(
            src='<sender_id>',
            dst='<destination_number>',
            text='Your package TWLO-484-555 was delivered to 742 Evergreen Terrace, Springfield',
        )
        print(response)
    except PlivoRestError as e:
        print(e)
    ```

    ***

    ### Test

    Save the file and run it from your terminal.

    ```shell  theme={null}
    python send_sms.py
    ```

    You should receive the SMS alert on your destination phone.
  </Tab>

  <Tab title="PHP">
    ## Overview

    This guide shows how to send an SMS alert or notification using Plivo's APIs and the PHP SDK.

    ***

    ### Prerequisites

    * A Plivo account — [**sign up for free**](https://cx.plivo.com/signup) if you don't have one.
    * An SMS-enabled Plivo phone number to send messages to the US and Canada. You can [**rent a number**](/numbers/) from the Plivo console.
    * PHP and the Plivo PHP SDK installed. See our [**PHP setup guide**](/sdk/server/set-up-php-dev-environment-api-messaging/).

    ***

    ### Create and run the application

    Create a file named `SendSMS.php` and paste this code into it. This script initializes the Plivo client and sends a message using the `messages->create` function.

    Replace the `<auth_id>`, `<auth_token>`, `<sender_id>`, and `<destination_number>` placeholders with your actual values.

    ```php  theme={null}
    <?php
    require 'vendor/autoload.php';
    use Plivo\RestClient;
    use Plivo\Exceptions\PlivoRestException;

    try {
        $client = new RestClient("<auth_id>", "<auth_token>");
        $response = $client->messages->create(
            [
                "src" => "<sender_id>",
                "dst" => "<destination_number>",
                "text" => "Your package TWLO-484-555 was delivered to 742 Evergreen Terrace, Springfield",
            ]
        );
        print_r($response);
    } catch (PlivoRestException $e) {
        echo "Error: " . $e->getMessage();
    }
    ?>
    ```

    ***

    ### Test

    Save the file and run it from your terminal.

    ```shell  theme={null}
    php SendSMS.php
    ```

    You should receive the SMS alert on your destination phone.
  </Tab>

  <Tab title=".NET">
    ## Overview

    This guide shows how to send an SMS alert or notification using Plivo's APIs and the .NET SDK.

    ***

    ### Prerequisites

    * A Plivo account — [**sign up for free**](https://cx.plivo.com/signup) if you don't have one.
    * An SMS enabled Plivo phone number to send messages to the US and Canada. You can [**rent a number**](/numbers/) from the Plivo console.
    * .NET and the Plivo .NET SDK installed. See our [**.NET setup guide**](/sdk/server/set-up-dotnet-dev-environment-api-messaging/).

    ***

    ### Create and run the application

    In your `Program.cs` file, paste this code. This script initializes the Plivo client and sends a message using the `api.Message.Create` function.

    Replace the `<auth_id>`, `<auth_token>`, `<sender_id>`, and `<destination_number>` placeholders with your actual values.

    ```cs  theme={null}
    using System;
    using Plivo;

    namespace PlivoExamples
    {
        class Program
        {
            static void Main(string[] args)
            {
                var api = new PlivoApi("<auth_id>", "<auth_token>");
                try
                {
                    var response = api.Message.Create(
                        src: "<sender_id>",
                        dst: new List<string> { "<destination_number>" },
                        text: "Your package TWLO-484-555 was delivered to 742 Evergreen Terrace, Springfield"
                    );
                    Console.WriteLine(response);
                }
                catch (Plivo.PlivoRestException e)
                {
                    Console.WriteLine("Error: " + e.Message);
                }
            }
        }
    }
    ```

    ***

    ### Test

    Save the file and run it. Your application will send the SMS alert to your destination phone.
  </Tab>

  <Tab title="Java">
    ## Overview

    This guide shows how to send an SMS alert or notification using Plivo's APIs and the Java SDK.

    ***

    ### Prerequisites

    * A Plivo account — [**sign up for free**](https://cx.plivo.com/signup) if you don't have one.
    * An SMS-enabled Plivo phone number to send messages to the US and Canada. You can [**rent a number**](/numbers/) from the Plivo console.
    * Java and the Plivo Java SDK installed. See our [**Java setup guide**](/sdk/server/set-up-java-dev-environment-api-messaging/).

    ***

    ### Create and run the application

    Create a Java class named `SendSMS` and paste this code into it. This script initializes the Plivo client and sends a message using the `Message.creator` function.

    Replace the `<auth_id>`, `<auth_token>`, `<sender_id>`, and `<destination_number>` placeholders with your actual values.

    ```java  theme={null}
    import com.plivo.api.Plivo;
    import com.plivo.api.exceptions.PlivoRestException;
    import com.plivo.api.models.message.Message;
    import com.plivo.api.models.message.MessageCreateResponse;
    import java.io.IOException;

    class SendSMS {
        public static void main(String [] args) {
            Plivo.init("<auth_id>", "<auth_token>");
            try {
                MessageCreateResponse response = Message.creator(
                    "<sender_id>",
                    "<destination_number>",
                    "Your package TWLO-484-555 was delivered to 742 Evergreen Terrace, Springfield"
                ).create();
                System.out.println(response);
            } catch (PlivoRestException | IOException e) {
                e.printStackTrace();
            }
        }
    }
    ```

    ***

    ### Test

    Save the file, compile, and run it. You should receive the SMS alert on your destination phone.
  </Tab>

  <Tab title="Go">
    ## Overview

    This guide shows how to send an SMS alert or notification using Plivo's APIs and the Go SDK.

    ***

    ### Prerequisites

    * A Plivo account — [**sign up for free**](https://cx.plivo.com/signup) if you don't have one.
    * An SMS-enabled Plivo phone number to send messages to the US and Canada. You can [**rent a number**](/numbers/) from the Plivo console.
    * Go and the Plivo Go SDK installed. See our [**Go setup guide**](/sdk/server/set-up-go-dev-environment-api-messaging/).

    ***

    ### Create and run the application

    Create a file named `SendSMS.go` and paste this code into it. This script initializes the Plivo client and sends a message using the `client.Messages.Create` function.

    Replace the `<auth_id>`, `<auth_token>`, `<sender_id>`, and `<destination_number>` placeholders with your actual values.

    ```go  theme={null}
    package main

    import (
        "fmt"
        "[github.com/plivo/plivo-go/v7](https://github.com/plivo/plivo-go/v7)"
    )

    func main() {
        client, err := plivo.NewClient("<auth_id>", "<auth_token>", &plivo.ClientOptions{})
        if err != nil {
            panic(err)
        }
        response, err := client.Messages.Create(
            plivo.MessageCreateParams{
                Src:  "<sender_id>",
                Dst:  "<destination_number>",
                Text: "Your package TWLO-484-555 was delivered to 742 Evergreen Terrace, Springfield",
            },
        )
        if err != nil {
            panic(err)
        }
        fmt.Printf("Response: %#v\n", response)
    }
    ```

    ***

    ### Test

    Save the file and run it from your terminal.

    ```shell  theme={null}
    go run SendSMS.go
    ```

    You should receive the SMS alert on your destination phone.
  </Tab>
</Tabs>
