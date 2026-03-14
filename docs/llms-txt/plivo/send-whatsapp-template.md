# Source: https://plivo.com/docs/messaging/use-cases/whatsapp/getting-started/templated-message/send-whatsapp-template/send-whatsapp-template.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Send Templated Messages

> Send pre-approved WhatsApp templated messages to initiate conversations

<Tabs>
  <Tab title="Node">
    ## Overview

    This guide shows how to send a templated WhatsApp message to any destination WhatsApp numbers. Templated messages are a crucial to your WhatsApp messaging experience, as businesses can only initiate WhatsApp conversation with their customers using templated messages.

    WhatsApp templates support 4 components:  `header` ,  `body`,  `footer`  and `button`. At the point of sending messages, the template object you see in the code acts as a way to pass the dynamic values within these components.  `header`  can accomodate `text` or `media` (images, video, documents) content.  `body`  can accomodate `text` content.  `button`  can support dynamic values in a `url` button or to specify a developer-defined payload which will be returned when the WhatsApp user clicks on the `quick_reply` button. `footer`  cannot have any dynamic variables.

    You can start sending templated WhatsApp message using our APIs. Follow the instructions below.

    ## Prerequisites

    To get started, you need a Plivo account — [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. If this is your first time using Plivo APIs, follow our instructions to [set up a Node.js development environment](/sdk/server/set-up-node-dev-environment-api-messaging/).

    Once you have a Plivo account, follow our [WhatsApp guide](/_posts/docs/messaging-api/privatebeta/whatsapp-guides/2023-08-03-whatsapp-guides.markdown) to onboard your WhatsApp account, register a number against your WABA and have a template in an approved state.

    If your phone number is in `connected` state and a template is in `approved` state, you can send your first message.

    ## Create send WhatsApp application

    Create a file called `send_whatsapp.js` and paste into it this code.

    ```javascript  theme={null}
    var plivo = require('plivo');

    var client = new plivo.Client("<auth_id>", "<auth_token>");

    const template = {
                "name": "sample_purchase_feedback",
                "language": "en_US",
                "components": [
                    {
                        "type": "header",
                        "parameters": [
                            {
                                "type": "media",
                                "media": "https:'//'plivo.com/s3/img1.jpg"
                            }
                        ]
                    },
                    {
                        "type": "body",
                        "parameters": [
                            {
                                "type": "text",
                                "text": "John Doe"
                            }
                        ]
                    },
                    {
                        "type": "button", 
                        "sub_type":"quick_reply",
                        "index": "0",
                        "parameters": [
                          {
                            "type": "payload",
                            "payload": "Payload sent in inbound webhook response"}]
                    },
                    {
                        "type": "button", 
                        "sub_type":"url",
                        "index": "1",
                        "parameters": [
                          {
                            "type": "text",
                            "text": "replacement text which will append to url"}]
                     }   
                 ]
              }



    client.messages.create(
          {
             src:"+14151112221",
             dst:"+14151112222",
             type:"whatsapp",
             template:template,
             url: "https:'//'foo.com/sms_status/"
           }
           ).then(function (response) {
             console.log(response);
            });
    ```

    Replace the auth placeholders with your authentication credentials from the [Plivo console](https://cx.plivo.com/home). Replace the phone number placeholders with actual phone numbers in [E.164 format](https://en.wikipedia.org/wiki/E.164) (for example, +12025551234). `src` should be your phone number registered against your WhatsApp Business Account. `dst` should be the destination WhatsApp number that you want to receive the message. 

    <Note>
      <strong>Note:</strong> We recommend that you store your credentials in the `auth_id` and `auth_token` environment variables to avoid the possibility of accidentally committing them to source control. If you do this, you can initialize the client with no arguments and Plivo will automatically fetch the values from the environment variables. You can use `process.env` to store environment variables and fetch them when initializing the client.
    </Note>

    ## Test

    Save the file and run it.

    <Note>
      <strong>Note:</strong> If you’re using a Plivo Trial account, you can send messages only to phone numbers that have been verified with Plivo. You can verify (sandbox) a number by going to the console’s Phone Numbers > <a href="https://cx.plivo.com/home">Sandbox Numbers</a> page.
    </Note>
  </Tab>

  <Tab title="Ruby">
    ## **Overview**

    This guide shows how to send a templated WhatsApp message to any destination WhatsApp number. Templated messages are crucial to your WhatsApp messaging experience, as businesses can only initiate WhatsApp conversations using templated messages. 

    WhatsApp templates support 4 components:  `header` ,  `body`,  `footer`  and `button`. At the point of sending messages, the template object you see in the code acts as a way to pass the dynamic values within these components.  `header`  can accomodate `text` or `media` (images, video, documents) content.  `body`  can accomodate `text` content.  `button`  can support dynamic values in a `url` button or to specify a developer-defined payload which will be returned when the WhatsApp user clicks on the `quick_reply` button. `footer`  cannot have any dynamic variables.

    You can start sending templated WhatsApp messages using our APIs. Follow these instructions.

    ## **Prerequisites**

    To get started, you need a Plivo account — [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. If this is your first time using Plivo APIs, follow our instructions to [set up a Ruby development environment](/sdk/server/set-up-ruby-dev-environment-api-messaging/).

    Once you have a Plivo account, follow our [WhatsApp guide](/messaging/concepts/whatsapp/) to onboard your WhatsApp account, register a number against your WABA, and have a template in an approved state.

    If you phone number is in `connected` state and template is in `approved` state, you can send your first message.

    ## **Create the send WhatsApp application**

    Create a file called `WhatsappMessageCreate.rb` and paste into it this code.

    ```rb  theme={null}
    require "plivo" 
    include Plivo 

    api = RestClient.new("<auth_id>","<auth_token>") 

    template={ 
     "name": "sample_purchase_feedback", 
     "language": "en_US", 
     "components": [ 
      { 
       "type": "header", 
       "parameters": [ 
        { 
         "type": "media", 
         "media": "https://plivo.com/s3/img1.jpg" 
        } 
       ] 
      }, 
      { 
       "type": "body", 
       "parameters": [ 
        { 
         "type": "text", 
         "text": "John Doe" 
        } 
       ] 
      }, 
      {
       "type": "button", 
       "sub_type":"quick_reply",
       "index": "0",
       "parameters": [
         {
          "type": "payload",
          "payload": "Payload sent in inbound webhook response"
         }
       ]
      },
      {
       "type": "button", 
       "sub_type":"url",
       "index": "1",
       "parameters": [
        {
          "type": "text",
          "text": "replacement text which will append to url"
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
     url: "https://<yourdomain>.com/sms status/") 

    puts response #Prints only the message_uuid puts response.message_uuid"
    #Prints only the message_uuid
    puts response.message_uuid
    ```

    Replace the auth placeholders with your authentication credentials from the [Plivo console](https://cx.plivo.com/home). Replace the phone number placeholders with actual phone numbers in [E.164 format](https://en.wikipedia.org/wiki/E.164) (for example, +12025551234).  `src` would be your phone number registered against your WhatsApp business account.  `dst`   would be the destination WhatsApp number that would receive the message. 

    <Note>
      <strong>Note:</strong> We recommend that you store your credentials in the `auth_id` and `auth_token` environment variables to avoid the possibility of accidentally committing them to source control. If you do this, you can initialize the client with no arguments and Plivo will automatically fetch the values from the environment variables. You can use process.env to store environment variables and fetch them when initializing the client.
    </Note>

    ## **Test**

    Save the file and run it.

    <Note>
      <strong>Note:</strong> If you’re using a Plivo Trial account, you can send messages only to phone numbers that have been verified with Plivo. You can verify (sandbox) a number by going to the console’s Phone Numbers > <a href="https://cx.plivo.com/home">Sandbox Numbers</a> page.
    </Note>
  </Tab>

  <Tab title="Python">
    ## Overview

    This guide shows how to send a templated WhatsApp message to any destination WhatsApp numbers. Templated messages are a crucial to your WhatsApp messaging experience, as businesses can only initiate WhatsApp conversation with their customers using templated messages. 

    WhatsApp templates support 4 components:  `header` ,  `body`,  `footer`  and `button`. At the point of sending messages, the template object you see in the code acts as a way to pass the dynamic values within these components.  `header`  can accomodate `text` or `media` (images, video, documents) content.  `body`  can accomodate `text` content.  `button`  can support dynamic values in a `url` button or to specify a developer-defined payload which will be returned when the WhatsApp user clicks on the `quick_reply` button. `footer`  cannot have any dynamic variables.

    You can start sending templated WhatsApp messages using our APIs. Follow the instructions below.

    ## Prerequisites

    To get started, you need a Plivo account — [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. If this is your first time using Plivo APIs, follow our instructions to [set up a Python development environment](/sdk/server/set-up-python-dev-environment-api-messaging/).

    Once you have a Plivo account, follow our [WhatsApp guide](/_posts/docs/messaging-api/privatebeta/whatsapp-guides/2023-08-03-whatsapp-guides.markdown) to onboard your WhatsApp account, register a number against your WABA and have a template in approved state.

    If you phone number is in `connected` state and template is in `approved` state, you can send your first message.

    ## Create send WhatsApp application

    Create a file called `send_whatsapp.py` and paste into it this code.

    ```python  theme={null}
    import plivo from plivo.utils.template import Template 

    client = plivo.RestClient('<auth_id>','<auth_token>') 

    template=Template(**{ 
    "name": "sample_purchase_feedback", 
    "language": "en_US", 
    "components": [ 
    { 
    "type": "header", 
    "parameters": [ 
          { 
           "type": "media", 
           "media": "https://plivo.com/s3/img1.jpg" 
          } 
       ] 
      }, 
    { 
    "type": "body", 
    "parameters": [ 
          { 
           "type"": "text", 
           "text"": "John Doe" 
          } 
      	  ]
      	}, 
    {
    "type": "button", 
    "sub_type":"quick_reply",
    "index": "0",
    "parameters": [
          {
           "type": "payload",
           "payload": "Payload sent in inbound webhook response"
          }
       ]
    },
    {
    "type": "button", 
    "sub_type":"url",
    "index": "1",
    "parameters": [
          {
           "type": "text",
           "text": "replacement text which will append to url"
          }
       ]
    }	
       ]
     }
    )


    response = client.messages.create( 
    src="+14151112221", 
    dst="+14151112222",
    type="whatsapp", 
    template=template,
     url="https://foo.com/sms_status/" ) 

    print(response) #prints only the message_uuid print(response.message_uuid)
    ```

    Replace the auth placeholders with your authentication credentials from the [Plivo console](https://cx.plivo.com/home). Replace the phone number placeholders with actual phone numbers in [E.164 format](https://en.wikipedia.org/wiki/E.164) (for example, +12025551234). src should be your phone number registered against your WhatsApp Business Account. dst should be the destination WhatsApp number that you want to receive the message. 

    <Note>
      <strong>Note:</strong> We recommend that you store your credentials in the auth\_id and auth\_token environment variables to avoid the possibility of accidentally committing them to source control. If you do this, you can initialize the client with no arguments and Plivo will automatically fetch the values from the environment variables. You can use process.env to store environment variables and fetch them when initializing the client.
    </Note>

    ## Test

    Save the file and run it.

    <Note>
      <strong>Note:</strong> If you’re using a Plivo Trial account, you can make calls only to phone numbers that have been verified with Plivo. You can verify (sandbox) a number by going to the console’s Phone Numbers > <a href="https://cx.plivo.com/home">Sandbox Numbers</a> page.
    </Note>
  </Tab>

  <Tab title="PHP">
    ## **Overview**

    This guide shows how to send a templated WhatsApp message to any destination WhatsApp number. Templated messages are crucial to your WhatsApp messaging experience, as businesses can only initiate WhatsApp conversations using templated messages. 

    WhatsApp templates support 4 components:  `header` ,  `body`,  `footer`  and `button`. At the point of sending messages, the template object you see in the code acts as a way to pass the dynamic values within these components.  `header`  can accomodate `text` or `media` (images, video, documents) content.  `body`  can accomodate `text` content.  `button`  can support dynamic values in a `url` button or to specify a developer-defined payload which will be returned when the WhatsApp user clicks on the `quick_reply` button. `footer`  cannot have any dynamic variables.

    You can start sending templated WhatsApp messages using our APIs. Follow these instructions.

    ## **Prerequisites**

    To get started, you need a Plivo account — [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. If this is your first time using Plivo APIs, follow our instructions to [set up a PHP development environment](/sdk/server/php-sdk/).

    Once you have a Plivo account, follow our [WhatsApp guide](/messaging/concepts/whatsapp/) to onboard your WhatsApp account, register a number against your WABA, and have a template in an approved state.

    If you phone number is in `connected` state and template is in `approved` state, you can send your first message.

    ## **Create the send WhatsApp application**

    Create a file called `send_whatsapp.php` and paste into it this code.

    ```php  theme={null}
    <?php
    require 'vendor/autoload.php';
    use Plivo\RestClient;

    $client = new RestClient("<auth_id>","<auth_token>");

    $template = '{
      "name": "sample_purchase_feedback",
      "language": "en_US",
      "components": [
        {
          "type": "header",
          "parameters": [
            {
              "type": "media",
              "media": "https://plivo.com/s3/img1.jpg"
            }
          ]
        },
        {
          "type": "body",
          "parameters": [
            {
              "type": "text",
              "text": "John Doe"
            }
          ]
        },
        {
    	"type": "button", 
    	"sub_type":"quick_reply",
          "index": "0",
          "parameters": [
            {
              "type": "payload",
              "payload": "Payload sent in inbound webhook response"
            }
          ]
        },
        {
          "type": "button", 
          "sub_type":"url",
          "index": "1",
          "parameters": [
            {
              "type": "text",
              "text": "replacement text which will append to url"
            }
          ]
        },   
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
    ?>
    ```

    Replace the auth placeholders with your authentication credentials from the [Plivo console](https://cx.plivo.com/home). Replace the phone number placeholders with actual phone numbers in [E.164 format](https://en.wikipedia.org/wiki/E.164) (for example, +12025551234).  `src` would be your phone number registered against your WhatsApp business account.  `dst`   would be the destination WhatsApp number that would receive the message. 

    <Note>
      <strong>Note:</strong> We recommend that you store your credentials in the `auth_id` and `auth_token` environment variables to avoid the possibility of accidentally committing them to source control. If you do this, you can initialize the client with no arguments and Plivo will automatically fetch the values from the environment variables. You can use process.env to store environment variables and fetch them when initializing the client.
    </Note>

    ## **Test**

    Save the file and run it.

    <Note>
      <strong>Note:</strong> If you’re using a Plivo Trial account, you can send messages only to phone numbers that have been verified with Plivo. You can verify (sandbox) a number by going to the console’s Phone Numbers > <a href="https://cx.plivo.com/home">Sandbox Numbers</a> page.
    </Note>
  </Tab>

  <Tab title=".NET">
    ## **Overview**

    This guide shows how to send a templated WhatsApp message to any destination WhatsApp number. Templated messages are crucial to your WhatsApp messaging experience, as businesses can only initiate WhatsApp conversations using templated messages. 

    You can start sending templated WhatsApp messages using our APIs. Follow these instructions.

    ## **Prerequisites**

    To get started, you need a Plivo account — [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. If this is your first time using Plivo APIs, follow our instructions to [set up a .NET development environment](/sdk/server/net-sdk/).

    Once you have a Plivo account, follow our [WhatsApp guide](/messaging/concepts/whatsapp/) to onboard your WhatsApp account, register a number against your WABA, and have a template in an approved state.

    If your phone number is in connected state and a template is in approved state, you can send your first message.

    ## **Create the send WhatsApp application**

    Create a file called WhatsappMessageCreate.NET and paste into it this code.

    ```cs  theme={null}
    "using System;
    using System.Collections.Generic;
    using Plivo;
    using Plivo.Resource.Message;

    namespace PlivoExamples
    {
        internal class Program
        {
            public static void Main(string[] args)
            {
                var api = new PlivoApi("<auth_id>","<auth_token>");

                var template = new Template
                {
                    Name = "sample_purchase_feedback",
                    Language = "en_US",
                    Components = new List<Component>
                    {
                        new Component
                        {
                            Type = "header",
                            Parameters = new List<Parameter>
                            {
                                new Parameter
                                {
                                    Type = "media",
                                    Media = "https://plivo.com/s3/img1.jpg"
                                }
                            }
                        },
                        new Component
                        {
                            Type = "body",
                            Parameters = new List<Parameter>
                            {
                                new Parameter
                                {
                                    Type = "text",
                                    Text = "Livpure Water Purifierr"
                                }
                            }
                        }
                    }
                };

                var response = api.Message.Create(
                    src: "+14151112221",
                    dst: "+14151112222",
                    type: "whatsapp",
                    template: template,
                    url: "https://<yourdomain>.com/sms_status/"
                    );
                Console.WriteLine(response);
                // Prints the message_uuid
                Console.WriteLine(response.MessageUuid[0]);
            }
        }
    }"
    ```

    Replace the auth placeholders with your authentication credentials from the [Plivo console](https://cx.plivo.com/home). Replace the phone number placeholders with actual phone numbers in [E.164 format](https://en.wikipedia.org/wiki/E.164) (for example, +12025551234). src should be your phone number registered against your WhatsApp Business Account. dst should be the destination WhatsApp number that you want to receive the message. 

    WhatsApp templates support four components: header, body, footer, and buttons. When you send messages, the template object you see in the code acts as a way to pass the dynamic parameters. header  can accommodate text or media (images, video, documents) content. body  can accommodate text content. footer  cannot have any dynamic variables. Plivo does not support sending dynamic parameters in buttons yet. 

    Note: We recommend that you store your credentials in the auth\_id and auth\_token environment variables to avoid the possibility of accidentally committing them to source control. If you do this, you can initialize the client with no arguments and Plivo will automatically fetch the values from the environment variables. You can use process.env to store environment variables and fetch them when initializing the client.

    ## **Test**

    Save the file and run it.

    ```java  theme={null}
    $ WhatsappMessageCreate.NET
    ```

    <Note>
      Note: If you’re using a Plivo Trial account, you can send messages only to phone numbers that have been verified with Plivo. You can verify (sandbox) a number by going to the console’s Phone Numbers > <a href="https://cx.plivo.com/home">Sandbox Numbers</a> page.
    </Note>
  </Tab>

  <Tab title="Java">
    ## **Overview**

    This guide shows how to send a templated WhatsApp message to any destination WhatsApp number. Templated messages are crucial to your WhatsApp messaging experience, as businesses can only initiate WhatsApp conversations using templated messages. 

    WhatsApp templates support 4 components:  `header` ,  `body`,  `footer`  and `button`. At the point of sending messages, the template object you see in the code acts as a way to pass the dynamic values within these components.  `header`  can accomodate `text` or `media` (images, video, documents) content.  `body`  can accomodate `text` content.  `button`  can support dynamic values in a `url` button or to specify a developer-defined payload which will be returned when the WhatsApp user clicks on the `quick_reply` button. `footer`  cannot have any dynamic variables.

    You can start sending templated WhatsApp messages using our APIs. Follow these instructions.

    ## **Prerequisites**

    To get started, you need a Plivo account — [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. If this is your first time using Plivo APIs, follow our instructions to [set up a Java development environment](/sdk/server/java-sdk).

    Once you have a Plivo account, follow our [WhatsApp guide](/messaging/concepts/whatsapp/) to onboard your WhatsApp account, register a number against your WABA, and have a template in an approved state.

    If you phone number is in `connected` state and template is in `approved` state, you can send your first message.

    ## **Create the send WhatsApp application**

    Create a file called `WhatsappMessageCreate.java` and paste into it this code.

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
                "\name\": "\sample_purchase_feedback\",
                "\language\": "\en_US\",
                "\components\": [
                    {
                        "\type\": "\header\",
                        "\parameters\": [
                            {
                                "\type\": "\media\",
                                "\text\": "\https://plivo.com/s3/img1.jpg\"
                            }
                        ]
                    },
                    {
                        "\type\": "\body\",
                        "\parameters\": [
                            {
                                "\type\": "\text\",
                                "\text\": "\John Doe\"
                            }
                        ]
                    },
                   {
                        "\type\": "\button\",
                        "\sub_type\": "\quick_reply\",
                        "\index\": "\0\",
                        "\parameters\": [
                            {
                                "\type\": "\payload\",
                                "\payload\": "\Payload sent in inbound webhook response\"
                            }
                        ]
                    },
                    {
                        "\type\": "\button\",
                        "\sub_type\": "\url\",
                        "\index\": "\1\",
                        "\parameters\": [
                            {
                                "\type\": "\text\",
                                "\text\": "\replacement text which will append to url\"
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

    Replace the auth placeholders with your authentication credentials from the [Plivo console](https://cx.plivo.com/home). Replace the phone number placeholders with actual phone numbers in [E.164 format](https://en.wikipedia.org/wiki/E.164) (for example, +12025551234).  `src` would be your phone number registered against your WhatsApp business account.  `dst`   would be the destination WhatsApp number that would receive the message. 

    <Note>
      <strong>Note:</strong> We recommend that you store your credentials in the `auth_id` and `auth_token` environment variables to avoid the possibility of accidentally committing them to source control. If you do this, you can initialize the client with no arguments and Plivo will automatically fetch the values from the environment variables. You can use process.env to store environment variables and fetch them when initializing the client.
    </Note>

    ## **Test**

    Save the file and run it.

    <Note>
      Note: If you’re using a Plivo Trial account, you can send messages only to phone numbers that have been verified with Plivo. You can verify (sandbox) a number by going to the console’s Phone Numbers > <a href="https://cx.plivo.com/home">Sandbox Numbers</a> page.
    </Note>
  </Tab>

  <Tab title="Go">
    ## Overview

    This guide shows how to send a templated WhatsApp message to any destination WhatsApp numbers. Templated messages are a crucial to your WhatsApp messaging experience, as businesses can only initiate WhatsApp conversation with their customers using templated messages. 

    WhatsApp templates support 4 components:  `header` ,  `body`,  `footer`  and `button`. At the point of sending messages, the template object you see in the code acts as a way to pass the dynamic values within these components.  `header`  can accomodate `text` or `media` (images, video, documents) content.  `body`  can accomodate `text` content.  `button`  can support dynamic values in a `url` button or to specify a developer-defined payload which will be returned when the WhatsApp user clicks on the `quick_reply` button. `footer`  cannot have any dynamic variables.

    You can start sending templated WhatsApp message messages using our APIs. Follow the instructions below.

    ## Prerequisites

    To get started, you need a Plivo account — [sign up](https://cx.plivo.com/signup) with your work email address if you don’t have one already. If this is your first time using Plivo APIs, follow our instructions to [set up a Go development environment](/sdk/server/set-up-go-dev-environment-api-messaging/).

    Once you have a Plivo account, follow our [WhatsApp guide](/_posts/docs/messaging-api/privatebeta/whatsapp-guides/2023-08-03-whatsapp-guides.markdown) to onboard your WhatsApp account, register a number against your WABA and have a template in approved state.

    If you phone number is in `connected` state and template is in `approved` state, you can send your first message.

    ## Create the send WhatsApp application

    Create a file called `SendWhatsApp.go` and paste into it this code.

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

            template, err := plivo.CreateWhatsappTemplate(`{
            "name": "sample_purchase_feedback",
            "language": "en_US",
            "components": [
                    {
                            "type": "header",
                            "parameters": [
                                    {
                                            "type": "media",
                                            "media": "https://plivo.com/i1.jpg"
                                    }
                            ]
                    },
                    {
                            "type": "body",
                            "parameters": [
                                    {
                                            "type": "text",
                                            "text": "John Doe"
                                    }
                            ]
                    },
                    {
                            "type": "button",
                            "sub_type": "quick_reply",
                            "index": "0",
                            "parameters": [
                                    {
                                            "type": "payload",
                                            "payload": "Payload sent in inbound webhook response"
                                    }
                            ]
                    },
                    {
                            "type": "button",
                            "sub_type": "url",
                            "index": "1",
                            "parameters": [
                                    {
                                            "type": "text",
                                            "text": "replacement text which will append to url"
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

    Replace the auth placeholders with your authentication credentials from the [Plivo console](https://cx.plivo.com/home). Replace the phone number placeholders with actual phone numbers in [E.164 format](https://en.wikipedia.org/wiki/E.164) (for example, +12025551234).  `src` would be your phone number registered against your WhatsApp business account.  `dst`   would be the destination WhatsApp number that would receive the message. 

    <Note>
      <strong>Note:</strong> We recommend that you store your credentials in the `auth_id` and `auth_token` environment variables to avoid the possibility of accidentally committing them to source control. If you do this, you can initialize the client with no arguments and Plivo will automatically fetch the values from the environment variables. You can use `os.Setenv` and `os.Getenv` functions to store environment variables and fetch them when initializing the client.
    </Note>

    ## Test

    Save the file and run it.

    <Note>
      <strong>Note:</strong> If you’re using a Plivo Trial account, you can send messages only to phone numbers that have been verified with Plivo. You can verify (sandbox) a number by going to the console’s Phone Numbers > <a href="https://cx.plivo.com/home">Sandbox Numbers</a> page.
    </Note>
  </Tab>
</Tabs>
