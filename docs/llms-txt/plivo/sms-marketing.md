# Source: https://plivo.com/docs/messaging/use-cases/sms-marketing/sms-marketing.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Send Bulk SMS

> Send bulk SMS messages to multiple recipients for marketing campaigns

<Tabs>
  <Tab title="Node">
    ## Overview

    This guide shows how to send an SMS message to multiple phone numbers at once using Plivo's APIs and the Node.js SDK.

    ***

    ### Prerequisites

    * A Plivo account — [**sign up for free**](https://cx.plivo.com/signup) if you don't have one.
    * An SMS-enabled Plivo phone number. You can [**rent a number**](/numbers/) from the Plivo console.
    * Node.js and the Plivo Node.js SDK installed. See our [**Node.js setup guide**](/sdk/server/set-up-node-dev-environment-api-messaging/).

    ***

    ### Create and run the application

    Create a file named `send_bulk_sms.js` and paste this code into it. To send a message to multiple numbers, join the destination numbers with the delimiter `<`.

    Replace the `<auth_id>`, `<auth_token>`, and `<sender_id>` placeholders with your actual values, and add the destination numbers to the `destinations` array.

    ```js  theme={null}
    const plivo = require('plivo');

    async function sendBulkSms() {
      const client = new plivo.Client("<auth_id>", "<auth_token>");

      const destinations = [
        "<destination_number_1>", // E.g., "+14155551234"
        "<destination_number_2>"  // E.g., "+14155555678"
      ];

      try {
        const response = await client.messages.create({
          src: "<sender_id>",
          dst: destinations.join("<"), // Delimiter is '<'
          text: "Flash sale — half price on all products — offer expires at midnight. Use code 50OFF at checkout"
        });
        console.log("Message sent successfully:", response);
      } catch (error) {
        console.error("Error sending message:", error);
      }
    }

    sendBulkSms();
    ```

    ***

    ### Test

    Save the file and run it from your terminal.

    ```shell  theme={null}
    node send_bulk_sms.js
    ```

    You should receive the SMS on all destination phones.
  </Tab>

  <Tab title="Ruby">
    ## Overview

    This guide shows how to send an SMS message to multiple phone numbers at once using Plivo's APIs and the Ruby SDK.

    ***

    ### Prerequisites

    * A Plivo account — [**sign up for free**](https://cx.plivo.com/signup) if you don't have one.
    * An SMS-enabled Plivo phone number. You can [**rent a number**](/numbers/) from the Plivo console.
    * Ruby and the Plivo Ruby SDK installed. See our [**Ruby setup guide**](/sdk/server/set-up-ruby-dev-environment-api-messaging/).

    ***

    ### Create and run the application

    Create a file named `send_bulk_sms.rb` and paste this code into it. To send a message to multiple numbers, join the destination numbers with the delimiter `<`.

    Replace the `<auth_id>`, `<auth_token>`, and `<sender_id>` placeholders with your actual values, and add the destination numbers to the `destinations` array.

    ```rb  theme={null}
    require "plivo"
    include Plivo

    destinations = [
      "<destination_number_1>", # E.g., "+14155551234"
      "<destination_number_2>"  # E.g., "+14155555678"
    ]

    begin
      api = RestClient.new("<auth_id>", "<auth_token>")
      response = api.messages.create(
        src: "<sender_id>",
        dst: destinations.join("<"), # Delimiter is '<'
        text: "Flash sale — half price on all products — offer expires at midnight. Use code 50OFF at checkout",
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
    ruby send_bulk_sms.rb
    ```

    You should receive the SMS on all destination phones.
  </Tab>

  <Tab title="Python">
    ## Overview

    This guide shows how to send an SMS message to multiple phone numbers at once using Plivo's APIs and the Python SDK.

    ***

    ### Prerequisites

    * A Plivo account — [**sign up for free**](https://cx.plivo.com/signup) if you don't have one.
    * An SMS-enabled Plivo phone number. You can [**rent a number**](/numbers/) from the Plivo console.
    * Python and the Plivo Python SDK installed. See our [**Python setup guide**](/sdk/server/set-up-python-dev-environment-api-messaging/).

    ***

    ### Create and run the application

    Create a file named `send_bulk_sms.py` and paste this code into it. To send a message to multiple numbers, join the destination numbers with the delimiter `<`.

    Replace the `<auth_id>`, `<auth_token>`, and `<sender_id>` placeholders with your actual values, and add the destination numbers to the `destinations` list.

    ```py  theme={null}
    import plivo
    from plivo.exceptions import PlivoRestError

    destinations = [
        "<destination_number_1>",  # E.g., "+14155551234"
        "<destination_number_2>"   # E.g., "+14155555678"
    ]

    try:
        client = plivo.RestClient('<auth_id>', '<auth_token>')
        response = client.messages.create(
            src='<sender_id>',
            dst='<'.join(destinations),  # Delimiter is '<'
            text='Flash sale — half price on all products — offer expires at midnight. Use code 50OFF at checkout',
        )
        print(response)
    except PlivoRestError as e:
        print(e)
    ```

    ***

    ### Test

    Save the file and run it from your terminal.

    ```shell  theme={null}
    python send_bulk_sms.py
    ```

    You should receive the SMS on all destination phones.
  </Tab>

  <Tab title="PHP">
    ## Overview

    This guide shows how to send an SMS message to multiple phone numbers at once using Plivo's APIs and the PHP SDK.

    ***

    ### Prerequisites

    * A Plivo account — [**sign up for free**](https://cx.plivo.com/signup) if you don't have one.
    * An SMS-enabled Plivo phone number. You can [**rent a number**](/numbers/) from the Plivo console.
    * PHP and the Plivo PHP SDK installed. See our [**PHP setup guide**](/sdk/server/set-up-php-dev-environment-api-messaging/).

    ***

    ### Create and run the application

    Create a file named `SendBulkSMS.php` and paste this code into it. To send a message to multiple numbers, join the destination numbers with the delimiter `<`.

    Replace the `<auth_id>`, `<auth_token>`, and `<sender_id>` placeholders with your actual values, and add the destination numbers to the `$destinations` array.

    ```php  theme={null}
    <?php
    require 'vendor/autoload.php';
    use Plivo\RestClient;
    use Plivo\Exceptions\PlivoRestException;

    $destinations = [
        "<destination_number_1>", // E.g., "+14155551234"
        "<destination_number_2>"  // E.g., "+14155555678"
    ];

    try {
        $client = new RestClient("<auth_id>", "<auth_token>");
        $response = $client->messages->create(
            [
                "src" => "<sender_id>",
                "dst" => implode("<", $destinations), // Delimiter is '<'
                "text" => "Flash sale — half price on all products — offer expires at midnight. Use code 50OFF at checkout",
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
    php SendBulkSMS.php
    ```

    You should receive the SMS on all destination phones.
  </Tab>

  <Tab title=".NET">
    ## Overview

    This guide shows how to send an SMS message to multiple phone numbers at once using Plivo's APIs and the .NET SDK.

    ***

    ### Prerequisites

    * A Plivo account — [**sign up for free**](https://cx.plivo.com/signup) if you don't have one.
    * An SMS-enabled Plivo phone number. You can [**rent a number**](/numbers/) from the Plivo console.
    * .NET and the Plivo .NET SDK installed. See our [**.NET setup guide**](/sdk/server/set-up-dotnet-dev-environment-api-messaging/).

    ***

    ### Create and run the application

    In your `Program.cs` file, paste this code. To send to multiple numbers, join the destination numbers with the delimiter `<`.

    Replace the `<auth_id>`, `<auth_token>`, and `<sender_id>` placeholders with your actual values, and add the destination numbers to the `destinations` list.

    ```cs  theme={null}
    using System;
    using System.Collections.Generic;
    using Plivo;

    namespace PlivoExamples
    {
        class Program
        {
            static void Main(string[] args)
            {
                var destinations = new List<string> {
                    "<destination_number_1>", // E.g., "+14155551234"
                    "<destination_number_2>"  // E.g., "+14155555678"
                };

                var api = new PlivoApi("<auth_id>", "<auth_token>");
                try
                {
                    var response = api.Message.Create(
                        src: "<sender_id>",
                        dst: string.Join("<", destinations), // Delimiter is '<'
                        text: "Flash sale — half price on all products — offer expires at midnight. Use code 50OFF at checkout"
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

    Save the file and run it. You should receive the SMS on all destination phones.
  </Tab>

  <Tab title="Java">
    ## Overview

    This guide shows how to send an SMS message to multiple phone numbers at once using Plivo's APIs and the Java SDK.

    ***

    ### Prerequisites

    * A Plivo account — [**sign up for free**](https://cx.plivo.com/signup) if you don't have one.
    * An SMS-enabled Plivo phone number. You can [**rent a number**](/numbers/) from the Plivo console.
    * Java and the Plivo Java SDK installed. See our [**Java setup guide**](/sdk/server/set-up-java-dev-environment-api-messaging/).

    ***

    ### Create and run the application

    Create a Java class named `SendBulkSMS` and paste this code into it. To send to multiple numbers, join the destination numbers with the delimiter `<`.

    Replace the `<auth_id>`, `<auth_token>`, and `<sender_id>` placeholders with your actual values, and add the destination numbers to the `destinations` list.

    ```java  theme={null}
    import com.plivo.api.Plivo;
    import com.plivo.api.exceptions.PlivoRestException;
    import com.plivo.api.models.message.Message;
    import com.plivo.api.models.message.MessageCreateResponse;
    import java.io.IOException;
    import java.util.Arrays;
    import java.util.List;

    class SendBulkSMS {
        public static void main(String [] args) {
            List<String> destinations = Arrays.asList(
                "<destination_number_1>", // E.g., "+14155551234"
                "<destination_number_2>"  // E.g., "+14155555678"
            );

            Plivo.init("<auth_id>", "<auth_token>");
            try {
                MessageCreateResponse response = Message.creator(
                    "<sender_id>",
                    String.join("<", destinations), // Delimiter is '<'
                    "Flash sale — half price on all products — offer expires at midnight. Use code 50OFF at checkout"
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

    Save the file, compile, and run it. You should receive the SMS on all destination phones.
  </Tab>

  <Tab title="Go">
    ## Overview

    This guide shows how to send an SMS message to multiple phone numbers at once using Plivo's APIs and the Go SDK.

    ***

    ### Prerequisites

    * A Plivo account — [**sign up for free**](https://cx.plivo.com/signup) if you don't have one.
    * An SMS-enabled Plivo phone number. You can [**rent a number**](/numbers/) from the Plivo console.
    * Go and the Plivo Go SDK installed. See our [**Go setup guide**](/sdk/server/set-up-go-dev-environment-api-messaging/).

    ***

    ### Create and run the application

    Create a file named `SendBulkSMS.go` and paste this code into it. To send to multiple numbers, join the destination numbers with the delimiter `<`.

    Replace the `<auth_id>`, `<auth_token>`, and `<sender_id>` placeholders with your actual values, and add the destination numbers to the `destinations` slice.

    ```go  theme={null}
    package main

    import (
        "fmt"
        "strings"
        "[github.com/plivo/plivo-go/v7](https://github.com/plivo/plivo-go/v7)"
    )

    func main() {
        destinations := []string{
            "<destination_number_1>", // E.g., "+14155551234"
            "<destination_number_2>",  // E.g., "+14155555678"
        }

        client, err := plivo.NewClient("<auth_id>", "<auth_token>", &plivo.ClientOptions{})
        if err != nil {
            panic(err)
        }
        response, err := client.Messages.Create(
            plivo.MessageCreateParams{
                Src:  "<sender_id>",
                Dst:  strings.Join(destinations, "<"), // Delimiter is '<'
                Text: "Flash sale — half price on all products — offer expires at midnight. Use code 50OFF at checkout",
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
    go run SendBulkSMS.go
    ```

    You should receive the SMS on all destination phones.
  </Tab>
</Tabs>
