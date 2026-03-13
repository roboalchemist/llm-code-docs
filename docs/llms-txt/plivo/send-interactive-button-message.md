# Source: https://plivo.com/docs/messaging/use-cases/whatsapp/getting-started/interactive-message/send-interactive-button-message/send-interactive-button-message.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Send Button Messages

> Send interactive WhatsApp button messages with reply options

<Tabs>
  <Tab title="Node">
    ## Overview

    This guide shows how to send non-templated [interactive button](https://developers.facebook.com/docs/whatsapp/cloud-api/messages/interactive-reply-buttons-messages) messages to recipients using Plivo’s APIs. You can only send a non-templated WhatsApp message as a reply to a user-initiated conversation or as part of an existing ongoing conversation that started with a templated WhatsApp message.

    ## Prerequisites

    To get started, you need a Plivo account — [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. If this is your first time using Plivo’s APIs, follow our instructions to [set up a Node.js development environment](/sdk/server/set-up-node-dev-environment-api-messaging/).

    ## Create the send WhatsApp application

    Create a file called `send_whatsapp.js` and paste into it this code.

    ```javascript  theme={null}
    let plivo = require('plivo');

    var client = new plivo.Client("<auth_id>","<auth_token>");

    const interactive = {
            "type": "button",
            "header": {
                "type": "media",
                "media": "https://media.geeksforgeeks.org/wp-content/uploads/20190712220639/ybearoutput-300x225.png"
            },
            "body": {
                "text": "Make your selection"
            },
            "action": {
                "buttons": [
                    {
                        "title": "Click here",
                        "id": "bt1j1k2j"
                    },
                    {
                        "title": "Know More",
                        "id": "bt1j1k2jkjk"
                    },
                    {
                        "title": "Request Callback",
                        "id": "bt1j1kfd2jkjk"
                    }
                ]
            }
        }

    client.messages.create({src:"+14151112221",dst:"+14151112222",type:"whatsapp",interactive:interactive})
    .then(function (response) {
        console.log(response);
      });
    ```

    Replace the auth placeholders with your authentication credentials from the [Plivo console](https://cx.plivo.com/home). Replace the phone number placeholders with your phone numbers in [E.164 format](https://en.wikipedia.org/wiki/E.164) (for example, +12025551234).

    `src`

    should be a phone number registered to your WhatsApp Business Account.

    `dst`

    should be the recipient’s WhatsApp number.

    <Note>
      <strong>Note:</strong> We recommend that you store your credentials in the `auth_id` and `auth_token` environment variables to avoid accidentally committing them to source control. If you do this, you can initialize the client with no arguments and Plivo will automatically fetch the values from the environment variables. You can use `process.env` to store environment variables and fetch them when initializing the client.
    </Note>

    ## Test

    Save the file and run it.

    <Note>
      <strong>Note:</strong> If you’re using a Plivo trial account, you can only send messages to phone numbers that have been verified with Plivo. You can verify (sandbox) a number by going to the console’s Phone Numbers > <a href="https://cx.plivo.com/home">Sandbox Numbers</a> page.
    </Note>
  </Tab>

  <Tab title="Ruby">
    ## Overview

    This guide shows how to send non-templated [interactive button](https://developers.facebook.com/docs/whatsapp/cloud-api/messages/interactive-reply-buttons-messages) messages to recipients using Plivo’s APIs. You can only send a non-templated WhatsApp message as a reply to a user-initiated conversation or as part of an existing ongoing conversation that started with a templated WhatsApp message.

    ## Prerequisites

    To get started, you need a Plivo account — [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. If this is your first time using Plivo APIs, follow our instructions to [set up a Ruby development environment](/sdk/server/ruby-sdk/).

    ## Create the send WhatsApp application

    Create a file called `send_whatsapp.rb` and paste into it this code.

    ```rb  theme={null}
    require ""rubygems""
    require ""/usr/src/app/lib/plivo.rb""
    include Plivo

    api = RestClient.new(""<auth_id>"",""<auth_token>"")

    interactive= {
            ""type"": ""button"",
            ""header"": {
                ""type"": ""media"",
                ""media"": ""https://media.geeksforgeeks.org/wp-content/uploads/20190712220639/ybearoutput-300x225.png""
            },
            ""body"": {
                ""text"": ""Make your selection""
            },
            ""action"": {
                ""buttons"": [
                    {
                        ""title"": ""Click here"",
                        ""id"": ""bt1j1k2j""
                    },
                    {
                        ""title"": ""Know More"",
                        ""id"": ""bt1j1k2jkjk""
                    },
                    {
                        ""title"": ""Request Callback"",
                        ""id"": ""bt1j1kfd2jkjk""
                    }
                ]
            }
        }

    response = api.messages.create( src: ""+14151112221"",dst:""+14151112222"",type:""whatsapp"", interactive:interactive)
    puts response
    ```

    Replace the auth placeholders with your authentication credentials from the [Plivo console](https://cx.plivo.com/home). Replace the phone number placeholders with your phone numbers in [E.164 format](https://en.wikipedia.org/wiki/E.164) (for example, +12025551234).

    `src`

    should be a phone number registered to your WhatsApp Business Account.

    `dst`

    should be the recipient’s WhatsApp number.

    <Note>
      <strong>Note:</strong> We recommend that you store your credentials in the `auth_id` and `auth_token` environment variables to avoid accidentally committing them to source control. If you do this, you can initialize the client with no arguments and Plivo will automatically fetch the values from the environment variables. You can use `process.env` to store environment variables and fetch them when initializing the client.
    </Note>

    ## Test

    Save the file and run it.

    <Note>
      <strong>Note:</strong> If you’re using a Plivo trial account, you can only send messages to phone numbers that have been verified with Plivo. You can verify (sandbox) a number by going to the console’s Phone Numbers > <a href="https://cx.plivo.com/home">Sandbox Numbers</a> page.
    </Note>
  </Tab>

  <Tab title="Python">
    ## Overview

    This guide shows how to send non-templated [interactive button](https://developers.facebook.com/docs/whatsapp/cloud-api/messages/interactive-reply-buttons-messages) messages to recipients using Plivo’s APIs. You can only send a non-templated WhatsApp message as a reply to a user-initiated conversation or as part of an existing ongoing conversation that started with a templated WhatsApp message.

    ## Prerequisites

    To get started, you need a Plivo account — [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. If this is your first time using Plivo APIs, follow our instructions to [set up a Python development environment](/sdk/server/set-up-python-dev-environment-api-messaging/).

    ## Create the send WhatsApp application

    Create a file called `send_whatsapp.py` and paste into it this code.

    ```python  theme={null}
    import plivo
    from plivo.utils.interactive import Interactive

    client = plivo.RestClient('<auth_id>','<auth_token>')

    interactive=Interactive(**{
            "type": "button",
            "header": {
                "type": "media",
                "media": "https://media.geeksforgeeks.org/wp-content/uploads/20190712220639/ybearoutput-300x225.png"
            },
            "body": {
                "text": "Make your selection"
            },
            "action": {
                "buttons": [
                    {
                        "title": "Click here",
                        "id": "bt1j1k2j"
                    },
                    {
                        "title": "Know More",
                        "id": "bt1j1k2jkjk"
                    },
                    {
                        "title": "Request Callback",
                        "id": "bt1j1kfd2jkjk"
                    }
                ]
            }
        })

    response= client.messages.create(src="+14151112221",dst="+14151112222",type_="whatsapp", interactive=interactive)
    print(response)
    ```

    Replace the auth placeholders with your authentication credentials from the [Plivo console](https://cx.plivo.com/home). Replace the phone number placeholders with your phone numbers in [E.164 format](https://en.wikipedia.org/wiki/E.164) (for example, +12025551234).

    `src`

    should be a phone number registered to your WhatsApp Business Account.

    `dst`

    should be the recipient’s WhatsApp number.

    <Note>
      <strong>Note:</strong> We recommend that you store your credentials in the `auth_id` and `auth_token` environment variables to avoid accidentally committing them to source control. If you do this, you can initialize the client with no arguments and Plivo will automatically fetch the values from the environment variables. You can use `process.env` to store environment variables and fetch them when initializing the client.
    </Note>

    ## Test

    Save the file and run it.

    <Note>
      <strong>Note:</strong> If you’re using a Plivo trial account, you can only send messages to phone numbers that have been verified with Plivo. You can verify (sandbox) a number by going to the console’s Phone Numbers > <a href="https://cx.plivo.com/home">Sandbox Numbers</a> page.
    </Note>
  </Tab>

  <Tab title="PHP">
    ## Overview

    This guide shows how to send non-templated [interactive button](https://developers.facebook.com/docs/whatsapp/cloud-api/messages/interactive-reply-buttons-messages) messages to recipients using Plivo’s APIs. You can only send a non-templated WhatsApp message as a reply to a user-initiated conversation or as part of an existing ongoing conversation that started with a templated WhatsApp message.

    ## Prerequisites

    To get started, you need a Plivo account — [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. If this is your first time using Plivo APIs, follow our instructions to [set up a PHP development environment](/sdk/server/php-sdk/).

    ## Create the send WhatsApp application

    Create a file called `send_whatsapp.php` and paste into it this code.

    ```php  theme={null}
    <?php
    require '/usr/src/app/vendor/autoload.php';
    use Plivo\RestClient;

    $client = new RestClient(""<auth_id>"",""<auth_token>"");

    $interactive = '{
            ""type"": ""button"",
            ""header"": {
                ""type"": ""media"",
                ""media"": ""https://media.geeksforgeeks.org/wp-content/uploads/20190712220639/ybearoutput-300x225.png""
            },
            ""body"": {
                ""text"": ""Make your selection""
            },
            ""action"": {
                ""buttons"": [
                    {
                        ""title"": ""Click here"",
                        ""id"": ""bt1j1k2j""
                    },
                    {
                        ""title"": ""Know More"",
                        ""id"": ""bt1j1k2jkjk""
                    },
                    {
                        ""title"": ""Request Callback"",
                        ""id"": ""bt1j1kfd2jkjk""
                    }
                ]
            }
        }';

    $response = $client->messages->create([""src""=>""+14151112221"",""dst""=>""+14151112222"",""type""=>""whatsapp"",""interactive""=>$interactive]);
    print_r($response);
    ?>
    ```

    Replace the auth placeholders with your authentication credentials from the [Plivo console](https://cx.plivo.com/home). Replace the phone number placeholders with your phone numbers in [E.164 format](https://en.wikipedia.org/wiki/E.164) (for example, +12025551234). `src` should be a phone number registered to your WhatsApp Business Account. `dst` should be the recipient’s WhatsApp number.

    <Note>
      <strong>Note:</strong> We recommend that you store your credentials in the `auth_id` and `auth_token` environment variables to avoid accidentally committing them to source control. If you do this, you can initialize the client with no arguments and Plivo will automatically fetch the values from the environment variables. You can use `process.env` to store environment variables and fetch them when initializing the client.
    </Note>

    ## **Test**

    Save the file and run it.

    <Note>
      <strong>Note:</strong> If you’re using a Plivo trial account, you can only send messages to phone numbers that have been verified with Plivo. You can verify (sandbox) a number by going to the console’s Phone Numbers > <a href="https://cx.plivo.com/home">Sandbox Numbers</a> page.
    </Note>
  </Tab>

  <Tab title=".NET">
    ## Overview

    This guide shows how to send non-templated [interactive button](https://developers.facebook.com/docs/whatsapp/cloud-api/messages/interactive-reply-buttons-messages) messages to recipients using Plivo’s APIs. You can only send a non-templated WhatsApp message as a reply to a user-initiated conversation or as part of an existing ongoing conversation that started with a templated WhatsApp message.

    ## Prerequisites

    To get started, you need a Plivo account — [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. If this is your first time using Plivo APIs, follow our instructions to [set up a .NET development environment](/sdk/server/set-up-dotnet-dev-environment-api-messaging/).

    ## Create the send WhatsApp application

    Create a file called `send_whatsapp.net` and paste into it this code.

    ```c#  theme={null}
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

               string jsonString = "{\"type\":\"button\",\"header\":{\"type\":\"media\",\"media\":\"https://media.geeksforgeeks.org/wp-content/uploads/20190712220639/ybearoutput-300x225.png\"},\"body\":{\"text\":\"Make your selection\"},\"action\":{\"buttons\":[{\"title\":\"Click here\",\"id\":\"bt1j1k2j\"},{\"title\":\"Know More\",\"id\":\"bt1j1k2jkjk\"},{\"title\":\"Request Callback\",\"id\":\"bt1j1kfd2jkjk\"}]}}";

                var response = api.Message.Create(src: "+14151112221", dst: "+14151112222", type: "whatsapp", interactive_json_string: jsonString);
                Console.WriteLine(response);
            }
        }
    }
    ```

    Replace the auth placeholders with your authentication credentials from the [Plivo console](https://cx.plivo.com/home). Replace the phone number placeholders with your phone numbers in [E.164 format](https://en.wikipedia.org/wiki/E.164) (for example, +12025551234).

    `src`

    should be a phone number registered to your WhatsApp Business Account.

    `dst`

    should be the recipient’s WhatsApp number.

    <Note>
      <strong>Note:</strong> We recommend that you store your credentials in the `auth_id` and `auth_token` environment variables to avoid accidentally committing them to source control. If you do this, you can initialize the client with no arguments and Plivo will automatically fetch the values from the environment variables. You can use `process.env` to store environment variables and fetch them when initializing the client.
    </Note>

    ## Test

    Save the file and run it.

    <Note>
      <strong>Note:</strong> If you’re using a Plivo trial account, you can only send messages to phone numbers that have been verified with Plivo. You can verify (sandbox) a number by going to the console’s Phone Numbers > <a href="https://cx.plivo.com/home">Sandbox Numbers</a> page.
    </Note>
  </Tab>

  <Tab title="Java">
    ## Overview

    This guide shows how to send non-templated [interactive button](https://developers.facebook.com/docs/whatsapp/cloud-api/messages/interactive-reply-buttons-messages) messages to recipients using Plivo’s APIs. You can only send a non-templated WhatsApp message as a reply to a user-initiated conversation or as part of an existing ongoing conversation that started with a templated WhatsApp message.

    ## Prerequisites

    To get started, you need a Plivo account — [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. If this is your first time using Plivo APIs, follow our instructions to [set up a Java development environment](/sdk/server/java-sdk).

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
    import com.fasterxml.jackson.databind.ObjectMapper;

    class Test
    {
        public static void main(String [] args)
        {
            Plivo.init(""<auth_id>"",""<auth_token>"");
            try
            {
                String interactiveJson = ""{\""type\"":\""button\"",\""header\"":{\""type\"":\""media\"",\""media\"":\""https://media.geeksforgeeks.org/wp-content/uploads/20190712220639/ybearoutput-300x225.png\""},\""body\"":{\""text\"":\""Make your selection\""},\""action\"":{\""buttons\"":[{\""title\"":\""Click here\"",\""id\"":\""bt1j1k2j\""},{\""title\"":\""Know More\"",\""id\"":\""bt1j1k2jkjk\""},{\""title\"":\""Request Callback\"",\""id\"":\""bt1j1kfd2jkjk\""}]}}"";

              MessageCreateResponse response = Message.creator(""+14151112221"",""+14151112222"").interactive_json_string(interactiveJson).type(MessageType.WHATSAPP).create();
              ObjectMapper ow = new ObjectMapper();
              String json_output = ow.writeValueAsString(response);
              System.out.println(json_output);

            }
            catch (PlivoRestException | IOException e)
            {
                e.printStackTrace();
            }
        }
    }
    ```

    Replace the auth placeholders with your authentication credentials from the [Plivo console](https://cx.plivo.com/home). Replace the phone number placeholders with your phone numbers in [E.164 format](https://en.wikipedia.org/wiki/E.164) (for example, +12025551234).

    `src`

    should be a phone number registered to your WhatsApp Business Account.

    `dst`

    should be the recipient’s WhatsApp number.

    <Note>
      <strong>Note:</strong> We recommend that you store your credentials in the `auth_id` and `auth_token` environment variables to avoid accidentally committing them to source control. If you do this, you can initialize the client with no arguments and Plivo will automatically fetch the values from the environment variables. You can use `process.env` to store environment variables and fetch them when initializing the client.
    </Note>

    ## **Test**

    Save the file and run it.

    <Note>
      <strong>Note:</strong> If you’re using a Plivo trial account, you can only send messages to phone numbers that have been verified with Plivo. You can verify (sandbox) a number by going to the console’s Phone Numbers > <a href="https://cx.plivo.com/home">Sandbox Numbers</a> page.
    </Note>
  </Tab>

  <Tab title="Go">
    ## Overview

    This guide shows how to send non-templated [interactive button](https://developers.facebook.com/docs/whatsapp/cloud-api/messages/interactive-reply-buttons-messages) messages to recipients using Plivo’s APIs. You can only send a non-templated WhatsApp message as a reply to a user-initiated conversation or as part of an existing ongoing conversation that started with a templated WhatsApp message.

    ## Prerequisites

    To get started, you need a Plivo account — [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. If this is your first time using Plivo APIs, follow our instructions to [set up a Go development environment](/sdk/server/set-up-go-dev-environment-api-messaging/).

    ## Create the send WhatsApp application

    Create a file called `send_whatsapp.go` and paste into it this code.

    ```go  theme={null}
    package main

    import (
            "fmt"
            "github.com/plivo/plivo-go"
    )

    func main() {
            client, err := plivo.NewClient("<auth_id>","<auth_token>", &plivo.ClientOptions{})
            if err != nil {
                    fmt.Print("Error", err.Error())
                    return
            }

            interactive, err := plivo.CreateWhatsappInteractive(`{
            "type": "button",
            "header": {
                "type": "media",
                "media": "https://media.geeksforgeeks.org/wp-content/uploads/20190712220639/ybearoutput-300x225.png"
            },
            "body": {
                "text": "Make your selection"
            },
            "action": {
                "buttons": [
                    {
                        "title": "Click here",
                        "id": "bt1j1k2j"
                    },
                    {
                        "title": "Know More",
                        "id": "bt1j1k2jkjk"
                    },
                    {
                        "title": "Request Callback",
                        "id": "bt1j1kfd2jkjk"
                    }
                ]
            }
        }`)
             if err != nil {
                panic(err)
             }

            response, err := client.Messages.Create(
            plivo.MessageCreateParams{Src:"+14151112221",Dst:"+14151112222",Type:"whatsapp", Interactive:&interactive},
             )
             if err != nil {
                    fmt.Print("Error", err.Error())
                    return
            }
            fmt.Printf("Response: %#v\n", response)
    }
    ```

    Replace the auth placeholders with your authentication credentials from the [Plivo console](https://cx.plivo.com/home). Replace the phone number placeholders with your phone numbers in [E.164 format](https://en.wikipedia.org/wiki/E.164) (for example, +12025551234).

    `src`

    should be a phone number registered to your WhatsApp Business Account.

    `dst`

    should be the recipient’s WhatsApp number.

    <Note>
      <strong>Note:</strong> We recommend that you store your credentials in the `auth_id` and `auth_token` environment variables to avoid accidentally committing them to source control. If you do this, you can initialize the client with no arguments and Plivo will automatically fetch the values from the environment variables. You can use `process.env` to store environment variables and fetch them when initializing the client.
    </Note>

    ## Test

    Save the file and run it.

    <Note>
      <strong>Note:</strong> If you’re using a Plivo trial account, you can only send messages to phone numbers that have been verified with Plivo. You can verify (sandbox) a number by going to the console’s Phone Numbers > <a href="https://cx.plivo.com/home">Sandbox Numbers</a> page.
    </Note>
  </Tab>
</Tabs>
