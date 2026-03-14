# Source: https://plivo.com/docs/messaging/use-cases/whatsapp/getting-started/templated-message/send-authentication-template/send-authentication-template.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Send Authentication Templated Messages

> Send WhatsApp authentication templates for OTP and 2FA verification

<Tabs>
  <Tab title="Node">
    ## **Overview**

    This guide shows how to send [authentication templates](https://developers.facebook.com/docs/whatsapp/business-management-api/authentication-templates/) to any destination WhatsApp numbers. Authentication templates are critical to fulfil your 2FA or OTP authentication use case. You can start sending authentication templates using our APIs. Follow the instructions below.

    ## **Prerequisites**

    To get started, you need a Plivo account — [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. If this is your first time using Plivo APIs, follow our instructions to [set up a Node.js development environment](/sdk/server/set-up-node-dev-environment-api-messaging/).

    Once you have a Plivo account, follow our [WhatsApp guide](https://www.plivo.com/_posts/docs/messaging-api/privatebeta/whatsapp-guides/2023-08-03-whatsapp-guides.markdown) to onboard your WhatsApp account, register a number against your WABA and have a template in an approved state.

    If your phone number is in connected state and your authentication template is in approved state, you can send your first message.

    ## **Create Send WhatsApp application**

    Create a file called send\_authentication\_whatsapp.js and paste into it this code.

    ```json  theme={null}
    "var plivo = require('plivo');

    var client = new plivo.Client("<auth_id>", "<auth_token>");

    const template = {
      "name": "plivo_authentication_template",
      "language": "en_US",
      "components": [
        {
          "type": "body",
          "parameters": [
            {
              "type": "text",
              "text": "33422388"
            }
          ]
        }
      ]
    }
    client.messages.create(
          {
            src:"+14151112221",
            dst:"+14151112222",
            type:"whatsapp",
            template:template,
            url: "https://foo.com/sms_status/"
          }
          ).then(function (response) {
            console.log(response);
            });"
    ```

    Replace the “auth” placeholders with your authentication credentials found on the [Plivo console](https://cx.plivo.com/home). 

    Replace the phone number placeholders with the phone numbers you wish to use in [E.164 format](https://en.wikipedia.org/wiki/E.164) (for example, +12025551234). src is the phone number registered against your WABA.  dst  refers to the WhatsApp number that will receive the message. 

    WhatsApp templates support four components: header,  body,  footer,  buttons. When sending messages, the template object you see in the code acts as a way to pass the dynamic parameters.  header can accommodate text or media (images, audio, video, documents) content. body can accommodate text content.  footer cannot have any dynamic variables. Plivo does not support sending dynamic parameters in buttons yet. 

    We recommend that you store your credentials in the auth\_id and auth\_token environment variables to avoid the possibility of accidentally committing them to source control. If you do this, you can initialize the client with no arguments and Plivo will automatically fetch the values from the environment variables. You can use process.env to store environment variables and fetch them when initializing the client.

    ## **Test**

    Save the file and run it.

    ```json  theme={null}
    send_authentication_whatsapp.js node
    ```

    <Note>
      Note: If you’re using a Plivo Trial account, you can send messages only to phone numbers that have been verified with Plivo. You can verify (sandbox) a number by going to the console’s Phone Numbers > <a href="https://cx.plivo.com/home">Sandbox Numbers</a> page.
    </Note>
  </Tab>

  <Tab title="Ruby">
    ## **Overview**

    This guide shows how to send [authentication templates](https://developers.facebook.com/docs/whatsapp/business-management-api/authentication-templates/) to any destination WhatsApp numbers. Authentication templates are critical to fulfill your 2FA or OTP authentication use case. You can start sending authentication templates using our APIs. Follow the instructions below.

    ## **Prerequisites**

    To get started, you need a Plivo account — [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. If this is your first time using Plivo APIs, follow our instructions to [set up a Ruby development environment](/sdk/server/set-up-ruby-dev-environment-api-messaging/).

    Once you have a Plivo account, follow our [WhatsApp guide](https://www.plivo.com/_posts/docs/messaging-api/privatebeta/whatsapp-guides/2023-08-03-whatsapp-guides.markdown) to onboard your WhatsApp account, register a number against your WABA and have a template in an approved state.

    If your phone number is in connected state and your authentication template is in approved state, you can send your first message.

    ## **Create Send WhatsApp application**

    Create a file called WhatsappAuthenticationMessagheCreate.rb and paste into it this code.

    ```ruby  theme={null}
    require "plivo"
    include Plivo

    api = RestClient.new("<auth_id>","<auth_token>")

    template={
      "name": "plivo_authentication_template",
      "language": "en_US",
      "components": [
        {
          "type": "body",
          "parameters": [
            {
              "type": "text",
              "text": "33422388"
            }
          ]
        }
      ]
    }

    response = api.messages.create(
            src: "+14151112221",
            dst:"+14151112222",
            type:"whatsapp",
            template:template,
            url: "https://<yourdomain>.com/sms status/",
    )
    puts response
    #Prints only the message_uuid
    puts response.message_uuid
    ```

    Replace the “auth” placeholders with your authentication credentials found on the [Plivo console](https://cx.plivo.com/home). 

    Replace the phone number placeholders with the phone numbers you wish to use in [E.164 format](https://en.wikipedia.org/wiki/E.164) (for example, +12025551234). src is the phone number registered against your WABA.  dst  refers to the WhatsApp number that will receive the message. 

    WhatsApp templates support four components: header,  body,  footer,  buttons. When sending messages, the template object you see in the code acts as a way to pass the dynamic parameters.  header can accommodate text or media (images, audio, video, documents) content. body can accommodate text content.  footer cannot have any dynamic variables. Plivo does not support sending dynamic parameters in buttons yet. 

    We recommend that you store your credentials in the auth\_id and auth\_token environment variables to avoid the possibility of accidentally committing them to source control. If you do this, you can initialize the client with no arguments and Plivo will automatically fetch the values from the environment variables. You can use process.env to store environment variables and fetch them when initializing the client.

    ## **Test**

    Save the file and run it.

    ```ruby  theme={null}
    $ WhatsappAuthenticationMessageCreate.rb
    ```

    <Note>
      Note: If you’re using a Plivo Trial account, you can send messages only to phone numbers that have been verified with Plivo. You can verify (sandbox) a number by going to the console’s Phone Numbers > <a href="https://cx.plivo.com/home">Sandbox Numbers</a> page.
    </Note>
  </Tab>

  <Tab title="Python">
    ## **Overview**

    This guide shows how to send [authentication templates](https://developers.facebook.com/docs/whatsapp/business-management-api/authentication-templates/) to any destination WhatsApp numbers. Authentication templates are critical to fulfil your 2FA or OTP authentication use case. You can start sending authentication templates using our APIs. Follow the instructions below.

    ## **Prerequisites**

    To get started, you need a Plivo account — [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. If this is your first time using Plivo APIs, follow our instructions to [set up a Python development environment](/sdk/server/set-up-python-dev-environment-api-messaging/).

    Once you have a Plivo account, follow our [WhatsApp guide](https://www.plivo.com/_posts/docs/messaging-api/privatebeta/whatsapp-guides/2023-08-03-whatsapp-guides.markdown) to onboard your WhatsApp account, register a number against your WABA and have a template in an approved state.

    If your phone number is in connected state and your authentication template is in approved state, you can send your first message.

    ## **Create Send WhatsApp application**

    Create a file called send\_authentication\_whatsapp.py and paste into it this code.

    ```python  theme={null}
    import plivo
    from plivo.utils.template import Template

    client = plivo.RestClient('<auth_id>','<auth_token>')

    template=Template(**{
            "name"": "plivo_authentication_template",
            "language": "en_US",
            "components": [
                    {
                            "type": "body",
                            "parameters": [
                                    {
                                            "type": "text",
                                            "text": "33422388"
                                    }
                            ]
                    }
            ]
    } )
    response = client.messages.create(
            src="+14151112221",
            dst="+14151112222",
            type="whatsapp",
            template=template,
            url="https://foo.com/sms_status/"
        )
    print(response)
    #prints only the message_uuid
    print(response.message_uuid)
    ```

    Replace the “auth” placeholders with your authentication credentials found on the [Plivo console](https://cx.plivo.com/home). 

    Replace the phone number placeholders with the phone numbers you wish to use in [E.164 format](https://en.wikipedia.org/wiki/E.164) (for example, +12025551234). src is the phone number registered against your WABA.  dst  refers to the WhatsApp number that will receive the message. 

    WhatsApp templates support four components: header,  body,  footer,  buttons. When sending messages, the template object you see in the code acts as a way to pass the dynamic parameters.  header can accommodate text or media (images, audio, video, documents) content. body can accommodate text content.  footer cannot have any dynamic variables. Plivo does not support sending dynamic parameters in buttons yet. 

    We recommend that you store your credentials in the auth\_id and auth\_token environment variables to avoid the possibility of accidentally committing them to source control. If you do this, you can initialize the client with no arguments and Plivo will automatically fetch the values from the environment variables. You can use process.env to store environment variables and fetch them when initializing the client.

    ## **Test**

    Save the file and run it.

    ```python  theme={null}
    $ python send_whatsappauthentication.py
    ```

    <Note>
      Note: If you’re using a Plivo Trial account, you can send messages only to phone numbers that have been verified with Plivo. You can verify (sandbox) a number by going to the console’s Phone Numbers > <a href="https://cx.plivo.com/home">Sandbox Numbers</a> page.
    </Note>
  </Tab>

  <Tab title="PHP">
    ## **Overview**

    This guide shows how to send [authentication templates](https://developers.facebook.com/docs/whatsapp/business-management-api/authentication-templates/) to any destination WhatsApp numbers. Authentication templates are critical to fulfill your 2FA or OTP authentication use case. You can start sending authentication templates using our APIs. Follow the instructions below.

    ## **Prerequisites**

    To get started, you need a Plivo account — [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. If this is your first time using Plivo APIs, follow our instructions to [set up a PHP development environment](/sdk/server/set-up-php-dev-environment-api-messaging/).

    Once you have a Plivo account, follow our [WhatsApp guide](https://www.plivo.com/_posts/docs/messaging-api/privatebeta/whatsapp-guides/2023-08-03-whatsapp-guides.markdown) to onboard your WhatsApp account, register a number against your WABA and have a template in approved state.

    If you phone number is in connected state and your authentication template is in approved state, you can send your first message.

    ## **Create the send WhatsApp application**

    Create a file called send\_authentication\_whatsapp.php and paste into it this code.

    ```php  theme={null}
    "<?php
    require 'vendor/autoload.php';
    use Plivo\RestClient;

    $client = new RestClient("<auth_id>","<auth_token>");

    $template = '{
      "name": "plivo_authentication_template",
      "language": "en_US",
      "components": [
        {
          "type": "body",
          "parameters": [
            {
              "type": "text",
              "text": "33422388"
            }
          ]
        }
      ]
    }';

    $response = $client->messages->create(
      [
        "src" => "+14151112221",
        "dst" => "+14151112222",
        "type"=>"whatsapp",
        "template"  =>$template,
        "url"=>"https://foo.com/sms_status/"
    ]
    );
    print_r($response);
    // Prints only the message_uuid
    print_r($response->getmessageUuid(0));
    ?>"
    ```

    Replace the “auth” placeholders with your authentication credentials found on the [Plivo console](https://cx.plivo.com/home). 

    Replace the phone number placeholders with the phone numbers you wish to use in [E.164 format](https://en.wikipedia.org/wiki/E.164) (for example, +12025551234). src is the phone number registered against your WABA.  dst  refers to the WhatsApp number that will receive the message. 

    WhatsApp templates support four components: header,  body,  footer,  buttons. When sending messages, the template object you see in the code acts as a way to pass the dynamic parameters.  header can accommodate text or media (images, audio, video, documents) content. body can accommodate text content.  footer cannot have any dynamic variables. Plivo does not support sending dynamic parameters in buttons yet. 

    We recommend that you store your credentials in the auth\_id and auth\_token environment variables to avoid the possibility of accidentally committing them to source control. If you do this, you can initialize the client with no arguments and Plivo will automatically fetch the values from the environment variables. You can use process.env to store environment variables and fetch them when initializing the client.

    ## **Test**

    Save the file and run it.

    ```php  theme={null}
    $ php send_whatsappauthentication.php
    ```

    <Note>
      Note: If you’re using a Plivo Trial account, you can send messages only to phone numbers that have been verified with Plivo. You can verify (sandbox) a number by going to the console’s Phone Numbers > <a href="https://cx.plivo.com/home">Sandbox Numbers</a> page.
    </Note>
  </Tab>

  <Tab title=".NET">
    ## **Overview**

    This guide shows how to send [authentication templates](https://developers.facebook.com/docs/whatsapp/business-management-api/authentication-templates/) to any destination WhatsApp numbers. Authentication templates are critical to fulfil your 2FA or OTP authentication use case. You can start sending authentication templates using our APIs. Follow the instructions below.

    ## **Prerequisites**

    To get started, you need a Plivo account — [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. If this is your first time using Plivo APIs, follow our instructions to [set up a .Net development environment](/sdk/server/set-up-dotnet-dev-environment-api-messaging/).

    Once you have a Plivo account, follow our [WhatsApp guide](https://www.plivo.com/_posts/docs/messaging-api/privatebeta/whatsapp-guides/2023-08-03-whatsapp-guides.markdown) to onboard your WhatsApp account, register a number against your WABA and have a template in an approved state.

    If your phone number is in connected state and your authentication template is in approved state, you can send your first message.

    ## **Create Send WhatsApp application**

    Create a file called WhatsappAuthenticationMessageCreate.NET and paste into it this code.

    ```cs  theme={null}
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

              String templateJson = "{
                "\name\": "\plivo_authentication_template\",
                "\language\": "\en_US\",
                "\components\": [
                    {
                        "\type\": "\body\",
                        "\parameters\": [
                            {
                                "\type\": "\text\",
                                "\text\": "\33422388\"
                            }
                        ]
                    }
                ]
              }";

                var response = api.Message.Create(
                    src: "+14151112221",
                    dst: "+14151112222",
                    type: "whatsapp",
                    template_json_string: templateJson,
                    url: "https://<yourdomain>.com/sms_status/"
                    );
                Console.WriteLine(response);
                // Prints the message_uuid
                Console.WriteLine(response.MessageUuid[0]);
            }
        }
    }"
    ```

    Replace the “auth” placeholders with your authentication credentials found on the [Plivo console](https://cx.plivo.com/home). 

    Replace the phone number placeholders with the phone numbers you wish to use in [E.164 format](https://en.wikipedia.org/wiki/E.164) (for example, +12025551234). src is the phone number registered against your WABA.  dst  refers to the WhatsApp number that will receive the message. 

    WhatsApp templates support four components: header,  body,  footer,  buttons. When sending messages, the template object you see in the code acts as a way to pass the dynamic parameters.  header can accommodate text or media (images, audio, video, documents) content. body can accommodate text content.  footer cannot have any dynamic variables. Plivo does not support sending dynamic parameters in buttons yet. 

    We recommend that you store your credentials in the auth\_id and auth\_token environment variables to avoid the possibility of accidentally committing them to source control. If you do this, you can initialize the client with no arguments and Plivo will automatically fetch the values from the environment variables. You can use process.env to store environment variables and fetch them when initializing the client.

    ## **Test**

    Save the file and run it.

    ```dot  theme={null}
    $ WhatsappAuthenticationMessageCreate.NET
    ```

    <Note>
      Note: If you’re using a Plivo Trial account, you can send messages only to phone numbers that have been verified with Plivo. You can verify (sandbox) a number by going to the console’s Phone Numbers > <a href="https://cx.plivo.com/home">Sandbox Numbers</a> page.
    </Note>
  </Tab>

  <Tab title="Java">
    ## **Overview**

    This guide shows how to send [authentication templates](https://developers.facebook.com/docs/whatsapp/business-management-api/authentication-templates/) to any destination WhatsApp numbers. Authentication templates are critical to fulfill your 2FA or OTP authentication use case. You can start sending authentication templates using our APIs. Follow the instructions below.

    ## **Prerequisites**

    To get started, you need a Plivo account — [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. If this is your first time using Plivo APIs, follow our instructions to [set up a Java development environment](/sdk/server/set-up-java-dev-environment-api-messaging/).

    Once you have a Plivo account, follow our [WhatsApp guide](https://www.plivo.com/_posts/docs/messaging-api/privatebeta/whatsapp-guides/2023-08-03-whatsapp-guides.markdown) to onboard your WhatsApp account, register a number against your WABA and have a template in approved state.

    If you phone number is in connected state and your authentication template is in approved state, you can send your first message.

    ## **Create the send WhatsApp application**

    Create a file called send\_authentication\_whatsapp.js and paste into it this code.

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

    class MessageCreate
    {
        public static void main(String [] args)
        {
            Plivo.init('<auth_id>','<auth_token>');
            try
            {

            String templateJson = "{
                "\name\": "\plivo_authentication_template\",
                "\language\": "\en_US\",
                "\components\": [
                    {
                        "\type\": "\body\",
                        "\parameters\": [
                            {
                                "\type\": "\text\",
                                "\text\": "\33422388\"
                            }
                        ]
                    }
                ]
              }";

    MessageCreateResponse response = Message.creator("+14151112221","14151112222")
                        .template_json_string(templateJson)
                        .type(MessageType.WHATSAPP)
                        .url(new URL("https://<yourdomain>.com/sms_status/") )
                        .create();
              ObjectMapper ow = new ObjectMapper();
              String output = ow.writeValueAsString(response);
              System.out.println(output);
            }

            catch (PlivoRestException | IOException e)
            {
                e.printStackTrace();
            }
        }
    }
    ```

    Replace the “auth” placeholders with your authentication credentials found on the [Plivo console](https://cx.plivo.com/home). 

    Replace the phone number placeholders with the phone numbers you wish to use in [E.164 format](https://en.wikipedia.org/wiki/E.164) (for example, +12025551234). src is the phone number registered against your WABA.  dst  refers to the WhatsApp number that will receive the message. 

    WhatsApp templates support four components: header,  body,  footer,  buttons. When sending messages, the template object you see in the code acts as a way to pass the dynamic parameters.  header can accommodate text or media (images, audio, video, documents) content. body can accommodate text content.  footer cannot have any dynamic variables. Plivo does not support sending dynamic parameters in buttons yet. 

    We recommend that you store your credentials in the auth\_id and auth\_token environment variables to avoid the possibility of accidentally committing them to source control. If you do this, you can initialize the client with no arguments and Plivo will automatically fetch the values from the environment variables. You can use process.env to store environment variables and fetch them when initializing the client.

    ## **Test**

    Save the file and run it.

    ```java  theme={null}
    send_authentication_whatsapp.js node
    ```

    <Note>
      Note: If you’re using a Plivo Trial account, you can send messages only to phone numbers that have been verified with Plivo. You can verify (sandbox) a number by going to the console’s Phone Numbers > <a href="https://cx.plivo.com/home">Sandbox Numbers</a> page.
    </Note>
  </Tab>

  <Tab title="Go">
    ## **Overview**

    This guide shows how to send [authentication templates](https://developers.facebook.com/docs/whatsapp/business-management-api/authentication-templates/) to any destination WhatsApp numbers. Authentication templates are critical to fulfill your 2FA or OTP authentication use case. You can start sending authentication templates using our APIs. Follow the instructions below.

    ## **Prerequisites**

    To get started, you need a Plivo account — [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. If this is your first time using Plivo APIs, follow our instructions to [set up a Go development environment](/sdk/server/set-up-go-dev-environment-api-messaging/).

    Once you have a Plivo account, follow our [WhatsApp guide](/messaging/concepts/whatsapp/) to onboard your WhatsApp account, register a number against your WABA and have a template in approved state.

    If you phone number is in connected state and your authentication template is in approved state, you can send your first message.

    ## **Create the send WhatsApp application**

    Create a file called WhatsappAuthenticationMessageCreate.go and paste into it this code.

    ```go  theme={null}
    package main

    import (
            "fmt"
            "github.com/plivo/plivo-go/v7"
    )

    func main() {
            client, err := plivo.NewClient("<auth_id>", "<auth_token>", &plivo.ClientOptions{})
            if err != nil {
                    fmt.Print(""Error"", err.Error())
                    return
            }

            template, err := plivo.CreateWhatsappTemplate(`{
            "name": "plivo_authentication_template",
            "language": "en_US",
            "components": [
                    {
                            "type": "body",
                            "parameters": [
                                    {
                                            "type": "text",
                                            "text": "33422388"
                                    }
                            ]
                    }
            ]
    }`)
            if err != nil {
                fmt.Print("Error", err.Error())
                return
            }

            response, err := client.Messages.Create(
            plivo.MessageCreateParams{
                      Src:"+14151112221",
                      Dst:"+14151112222",
                      Type:"whatsapp",
                      Template:&template,
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

    Replace the “auth” placeholders with your authentication credentials found on the [Plivo console](https://cx.plivo.com/home). 

    Replace the phone number placeholders with the phone numbers you wish to use in [E.164 format](https://en.wikipedia.org/wiki/E.164) (for example, +12025551234). src is the phone number registered against your WABA.  dst  refers to the WhatsApp number that will receive the message. 

    WhatsApp templates support four components: header,  body,  footer,  buttons. When sending messages, the template object you see in the code acts as a way to pass the dynamic parameters.  header can accommodate text or media (images, audio, video, documents) content. body can accommodate text content.  footer cannot have any dynamic variables. Plivo does not support sending dynamic parameters in buttons yet. 

    We recommend that you store your credentials in the auth\_id and auth\_token environment variables to avoid the possibility of accidentally committing them to source control. If you do this, you can initialize the client with no arguments and Plivo will automatically fetch the values from the environment variables. You can use process.env to store environment variables and fetch them when initializing the client.

    ## **Test**

    Save the file and run it.

    ```go  theme={null}
    go run WhatsappAuthenticationMessageCreate.go
    ```

    <Note>
      Note: If you’re using a Plivo Trial account, you can send messages only to phone numbers that have been verified with Plivo. You can verify (sandbox) a number by going to the console’s Phone Numbers > <a href="https://cx.plivo.com/home">Sandbox Numbers</a> page.
    </Note>
  </Tab>
</Tabs>
