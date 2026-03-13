# Source: https://plivo.com/docs/messaging/use-cases/sms-autoresponder/sms-autoresponder.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Write an SMS Autoresponder

> Build a keyword-based SMS autoresponder for automated replies

<Tabs>
  <Tab title="Node">
    ## Overview

    This guide shows how to write an SMS autoresponder using Plivo's APIs and Node.js. An autoresponder can streamline marketing campaigns and subscription signups by providing instant, keyword-based replies.

    ***

    ### How it works

    When Plivo receives an SMS on your number, it makes an HTTP request to your application's "Message URL." Your server receives the message content and can perform logic based on keywords. To reply, your server must respond to the request with a Plivo XML document containing a `<Message>` element.

    ***

    ### Prerequisites

    * A Plivo account — [**sign up for free**](https://cx.plivo.com/signup) if you don't have one.
    * An SMS-enabled Plivo phone number. You can [**rent a number**](/numbers/) from the Plivo console.
    * Node.js and the Plivo Node.js SDK installed. See our [**Node.js setup guide**](/sdk/server/set-up-node-dev-environment-api-messaging/).

    ***

    ### Create the autoresponder application

    Create a file called `autoresponder.js` and paste this code into it. This server listens for incoming messages, checks for the keyword "interested," and sends back a different reply based on whether the keyword is found.

    ```js  theme={null}
    const plivo = require('plivo');
    const express = require('express');
    const bodyParser = require('body-parser');
    const app = express();

    app.use(bodyParser.urlencoded({ extended: true }));

    app.all('/autoresponder/', (request, response) => {
        const from_number = request.body.From || request.query.From;
        const to_number = request.body.To || request.query.To;
        const text = request.body.Text || request.query.Text;

        let body;
        if (text && text.toLowerCase() === 'interested') {
            body = 'Thank you for showing interest. One of our agents will contact you.'
        } else {
            body = 'Reply "Interested" to connect with our agents'
        }

        const r = plivo.Response();
        const params = {
            'src': to_number, // The Plivo number
            'dst': from_number, // The original sender's number
        };
        r.addMessage(body, params);

        response.type('application/xml');
        response.end(r.toXML());
    });

    app.listen(3000, () => {
        console.log('Node app is running on port 3000');
    });
    ```

    ***

    ### Create and configure a Plivo application

    1. **Create an Application**: Go to Messaging > [Applications](https://cx.plivo.com/xml-applications) and click **Add New Application**.
    2. **Configure the URL**: Name the application (e.g., `Autoresponder`). In the `Message URL` field, enter your server URL (e.g., `https://<yourdomain>.com/autoresponder/`) and set the method to `POST`. Click **Create Application**.
    3. **Assign a Number**: Go to the [Numbers](https://cx.plivo.com/phone-numbers) page, select your number, and link it to the `Autoresponder` application you just created.

    ***

    ### Test it out

    Send any SMS to your Plivo number to get the default reply. Then, send the word "Interested" to get the confirmation message.
  </Tab>

  <Tab title="Ruby">
    ## Overview

    This guide shows how to write an SMS autoresponder using Plivo's APIs and Ruby on Rails. An autoresponder can streamline marketing campaigns and subscription signups by providing instant, keyword-based replies.

    ***

    ### How it works

    When Plivo receives an SMS on your number, it makes an HTTP request to your application's "Message URL." Your server receives the message content and can perform logic based on keywords. To reply, your server must respond to the request with a Plivo XML document containing a `<Message>` element.

    ***

    ### Prerequisites

    * A Plivo account — [**sign up for free**](https://cx.plivo.com/signup) if you don't have one.
    * An SMS-enabled Plivo phone number. You can [**rent a number**](/numbers/) from the Plivo console.
    * Ruby and the Plivo Ruby SDK installed. See our [**Ruby setup guide**](/sdk/server/set-up-ruby-dev-environment-api-messaging/).

    ***

    ### Create the autoresponder application

    In `app/controllers/plivo_controller.rb`, paste this code. This action listens for incoming messages, checks for the keyword "interested," and sends back a different reply based on whether the keyword is found.

    ```rb  theme={null}
    include Plivo
    include Plivo::Exceptions
    include Plivo::XML

    class PlivoController < ApplicationController
      skip_before_action :verify_authenticity_token
      def autoresponder
        from_number = params[:From]
        to_number = params[:To]
        text = params[:Text]

        if text && text.downcase == "interested"
          body = "Thank you for showing interest. One of our agents will contact you."
        else
          body = "Reply 'Interested' to connect with our agents"
        end

        response = Response.new
        params = {
          src: to_number, # The Plivo number
          dst: from_number, # The original sender's number
        }
        response.addMessage(body, params)
        xml = PlivoXML.new(response)
        render xml: xml.to_xml
      end
    end
    ```

    ***

    ### Create and configure a Plivo application

    1. **Create an Application**: Go to Messaging > [Applications](https://cx.plivo.com/xml-applications) and click **Add New Application**.
    2. **Configure the URL**: Name the application (e.g., `Autoresponder`). In the `Message URL` field, enter your server URL (e.g., `https://<yourdomain>.com/autoresponder/`) and set the method to `POST`. Click **Create Application**.
    3. **Assign a Number**: Go to the [Numbers](https://cx.plivo.com/phone-numbers) page, select your number, and link it to the `Autoresponder` application you just created.

    ***

    ### Test it out

    Send any SMS to your Plivo number to get the default reply. Then, send the word "Interested" to get the confirmation message.
  </Tab>

  <Tab title="Python">
    ## Overview

    This guide shows how to write an SMS autoresponder using Plivo's APIs and Python with Flask. An autoresponder can streamline marketing campaigns and subscription signups by providing instant, keyword-based replies.

    ***

    ### How it works

    When Plivo receives an SMS on your number, it makes an HTTP request to your application's "Message URL." Your server receives the message content and can perform logic based on keywords. To reply, your server must respond to the request with a Plivo XML document containing a `<Message>` element.

    ***

    ### Prerequisites

    * A Plivo account — [**sign up for free**](https://cx.plivo.com/signup) if you don't have one.
    * An SMS-enabled Plivo phone number. You can [**rent a number**](/numbers/) from the Plivo console.
    * Python and the Plivo Python SDK installed. See our [**Python setup guide**](/sdk/server/set-up-python-dev-environment-api-messaging/).

    ***

    ### Create the autoresponder application

    Create a file called `autoresponder.py` and paste into it this code. This server listens for incoming messages, checks for the keyword "interested," and sends back a different reply based on the result.

    ```py  theme={null}
    from flask import Flask, request, Response
    from plivo import plivoxml

    app = Flask(__name__)

    @app.route('/autoresponder/', methods=['GET', 'POST'])
    def autoresponder():
        from_number = request.values.get('From')
        to_number = request.values.get('To')
        text = request.values.get('Text')

        if text and text.lower() == 'interested':
            body = "Thank you for showing interest. One of our agents will contact you."
        else:
            body = "Reply 'Interested' to connect with our agents"

        response = plivoxml.ResponseElement()
        response.add(
            plivoxml.MessageElement(
                body,
                src=to_number, # The Plivo number
                dst=from_number # The original sender's number
            )
        )
        return Response(response.to_string(), mimetype='application/xml')

    if __name__ == '__main__':
        app.run(host='0.0.0.0', debug=True)
    ```

    ***

    ### Create and configure a Plivo application

    1. **Create an Application**: Go to Messaging > [Applications](https://cx.plivo.com/xml-applications) and click **Add New Application**.
    2. **Configure the URL**: Name the application (e.g., `Autoresponder`). In the `Message URL` field, enter your server URL (e.g., `https://<yourdomain>.com/autoresponder/`) and set the method to `POST`. Click **Create Application**.
    3. **Assign a Number**: Go to the [Numbers](https://cx.plivo.com/phone-numbers) page, select your number, and link it to the `Autoresponder` application you just created.

    ***

    ### Test it out

    Send any SMS to your Plivo number to get the default reply. Then, send the word "Interested" to get the confirmation message.
  </Tab>

  <Tab title="PHP">
    ## Overview

    This guide shows how to write an SMS autoresponder using Plivo's APIs and PHP. An autoresponder can streamline marketing campaigns and subscription signups by providing instant, keyword-based replies.

    ***

    ### How it works

    When Plivo receives an SMS on your number, it makes an HTTP request to your application's "Message URL." Your server receives the message content and can perform logic based on keywords. To reply, your server must respond to the request with a Plivo XML document containing a `<Message>` element.

    ***

    ### Prerequisites

    * A Plivo account — [**sign up for free**](https://cx.plivo.com/signup) if you don't have one.
    * An SMS-enabled Plivo phone number. You can [**rent a number**](/numbers/) from the Plivo console.
    * PHP and the Plivo PHP SDK installed. See our [**PHP setup guide**](/sdk/server/set-up-php-dev-environment-api-messaging/).

    ***

    ### Create the autoresponder application

    Paste this code into your controller. This script listens for incoming messages, checks for the keyword "interested," and sends back a different reply based on the result.

    ```php  theme={null}
    <?php
    namespace App\Http\Controllers;
    use Illuminate\Http\Request;
    use Plivo\XML\Response;

    class SMSController extends Controller
    {
        public function autoresponder()
        {
            $from_number = $_POST["From"];
            $to_number = $_POST["To"];
            $text = $_POST["Text"];

            if ($text && strtolower($text) == "interested") {
                $body = "Thank you for showing interest. One of our agents will contact you.";
            } else {
                $body = "Reply 'Interested' to connect with our agents";
            }

            $response = new Response();
            $params = [
                'src' => $to_number, // The Plivo number
                'dst' => $from_number  // The original sender's number
            ];
            $response->addMessage($body, $params);

            Header('Content-type: text/xml');
            echo($response->toXML());
        }
    }
    ```

    ***

    ### Create and configure a Plivo application

    1. **Create an Application**: Go to Messaging > [Applications](https://cx.plivo.com/xml-applications) and click **Add New Application**.
    2. **Configure the URL**: Name the application (e.g., `Autoresponder`). In the `Message URL` field, enter your server URL (e.g., `https://<yourdomain>.com/autoresponder/`) and set the method to `POST`. Click **Create Application**.
    3. **Assign a Number**: Go to the [Numbers](https://cx.plivo.com/phone-numbers) page, select your number, and link it to the `Autoresponder` application you just created.

    ***

    ### Test it out

    Send any SMS to your Plivo number to get the default reply. Then, send the word "Interested" to get the confirmation message.
  </Tab>

  <Tab title=".NET">
    ## Overview

    This guide shows how to write an SMS autoresponder using Plivo's APIs and .NET. An autoresponder can streamline marketing campaigns and subscription signups by providing instant, keyword-based replies.

    ***

    ### How it works

    When Plivo receives an SMS on your number, it makes an HTTP request to your application's "Message URL." Your server receives the message content and can perform logic based on keywords. To reply, your server must respond to the request with a Plivo XML document containing a `<Message>` element.

    ***

    ### Prerequisites

    * A Plivo account — [**sign up for free**](https://cx.plivo.com/signup) if you don't have one.
    * An SMS-enabled Plivo phone number. You can [**rent a number**](/numbers/) from the Plivo console.
    * .NET and the Plivo .NET SDK installed. See our [**.NET setup guide**](/sdk/server/set-up-dotnet-dev-environment-api-messaging/).

    ***

    ### Create the autoresponder application

    In your controller, paste this code. This action listens for incoming messages, checks for the keyword "interested," and sends back a different reply based on the result.

    ```csharp  theme={null}
    using System;
    using System.Collections.Generic;
    using Microsoft.AspNetCore.Mvc;

    namespace Demo.Controllers
    {
        public class Autoresponder : Controller
        {
            [HttpPost]
            public IActionResult Index()
            {
                String from_number = Request.Form["From"];
                String to_number = Request.Form["To"];
                String text = Request.Form["Text"];
                String body;

                if (text != null && text.ToLower() == "interested")
                {
                    body = "Thank you for showing interest. One of our agents will contact you.";
                }
                else
                {
                    body = "Reply 'Interested' to connect with our agents";
                }

                Plivo.XML.Response resp = new Plivo.XML.Response();
                resp.AddMessage(body, new Dictionary<string, string>()
                {
                    {"src", to_number}, // The Plivo number
                    {"dst", from_number} // The original sender's number
                });

                return this.Content(resp.ToString(), "text/xml");
            }
        }
    }
    ```

    ***

    ### Create and configure a Plivo application

    1. **Create an Application**: Go to Messaging > [Applications](https://cx.plivo.com/xml-applications) and click **Add New Application**.
    2. **Configure the URL**: Name the application (e.g., `Autoresponder`). In the `Message URL` field, enter your server URL (e.g., `https://<yourdomain>.com/autoresponder/`) and set the method to `POST`. Click **Create Application**.
    3. **Assign a Number**: Go to the [Numbers](https://cx.plivo.com/phone-numbers) page, select your number, and link it to the `Autoresponder` application you just created.

    ***

    ### Test it out

    Send any SMS to your Plivo number to get the default reply. Then, send the word "Interested" to get the confirmation message.
  </Tab>

  <Tab title="Java">
    ## Overview

    This guide shows how to write an SMS autoresponder using Plivo's APIs and Java with Spring. An autoresponder can streamline marketing campaigns and subscription signups by providing instant, keyword-based replies.

    ***

    ### How it works

    When Plivo receives an SMS on your number, it makes an HTTP request to your application's "Message URL." Your server receives the message content and can perform logic based on keywords. To reply, your server must respond to the request with a Plivo XML document containing a `<Message>` element.

    ***

    ### Prerequisites

    * A Plivo account — [**sign up for free**](https://cx.plivo.com/signup) if you don't have one.
    * An SMS-enabled Plivo phone number. You can [**rent a number**](/numbers/) from the Plivo console.
    * Java and the Plivo Java SDK installed. See our [**Java setup guide**](/sdk/server/set-up-java-dev-environment-api-messaging/).

    ***

    ### Create the autoresponder application

    In your main application file, paste this code. This controller listens for incoming messages, checks for the keyword "interested," and sends back a different reply based on the result.

    ```java  theme={null}
    package com.example.demo;

    import com.plivo.api.exceptions.PlivoXmlException;
    import com.plivo.api.xml.Message;
    import com.plivo.api.xml.Response;
    import org.springframework.boot.SpringApplication;
    import org.springframework.boot.autoconfigure.SpringBootApplication;
    import org.springframework.web.bind.annotation.PostMapping;
    import org.springframework.web.bind.annotation.RestController;

    @RestController
    @SpringBootApplication
    public class PlivoSmsApplication {

        public static void main(String[] args) {
            SpringApplication.run(PlivoSmsApplication.class, args);
        }

        @PostMapping(value = "/autoresponder/", produces = {"application/xml"})
        public String autoresponder(String From, String To, String Text) throws PlivoXmlException {
            String body;
            if (Text != null && Text.toLowerCase().equals("interested")) {
                body = "Thank you for showing interest. One of our agents will contact you.";
            } else {
                body = "Reply 'Interested' to connect with our agents";
            }
            Response response = new Response().children(
                    new Message(body, To, From)); // text, src, dst
            return response.toXmlString();
        }
    }
    ```

    ***

    ### Create and configure a Plivo application

    1. **Create an Application**: Go to Messaging > [Applications](https://cx.plivo.com/xml-applications) and click **Add New Application**.
    2. **Configure the URL**: Name the application (e.g., `Autoresponder`). In the `Message URL` field, enter your server URL (e.g., `https://<yourdomain>.com/autoresponder/`) and set the method to `POST`. Click **Create Application**.
    3. **Assign a Number**: Go to the [Numbers](https://cx.plivo.com/phone-numbers) page, select your number, and link it to the `Autoresponder` application you just created.

    ***

    ### Test it out

    Send any SMS to your Plivo number to get the default reply. Then, send the word "Interested" to get the confirmation message.
  </Tab>

  <Tab title="Go">
    ## Overview

    This guide shows how to write an SMS autoresponder using Plivo's APIs and Go. An autoresponder can streamline marketing campaigns and subscription signups by providing instant, keyword-based replies.

    ***

    ### How it works

    When Plivo receives an SMS on your number, it makes an HTTP request to your application's "Message URL." Your server receives the message content and can perform logic based on keywords. To reply, your server must respond to the request with a Plivo XML document containing a `<Message>` element.

    ***

    ### Prerequisites

    * A Plivo account — [**sign up for free**](https://cx.plivo.com/signup) if you don't have one.
    * An SMS-enabled Plivo phone number. You can [**rent a number**](/numbers/) from the Plivo console.
    * Go and the Plivo Go SDK installed. See our [**Go setup guide**](/sdk/server/set-up-go-dev-environment-api-messaging/).

    ***

    ### Create the autoresponder application

    Create a file called `autoresponder.go` and paste into it this code. This server listens for incoming messages, checks for the keyword "interested," and sends back a different reply based on the result.

    ```go  theme={null}
    package main

    import (
        "fmt"
        "net/http"
        "strings"
        "[github.com/plivo/plivo-go/v7/xml](https://github.com/plivo/plivo-go/v7/xml)"
    )

    func autoresponder(w http.ResponseWriter, r *http.Request) {
        from_number := r.FormValue("From")
        to_number := r.FormValue("To")
        text := r.FormValue("Text")
        var body string

        if strings.ToLower(text) == "interested" {
            body = "Thank you for showing interest. One of our agents will contact you."
        } else {
            body = "Reply 'Interested' to connect with our agents"
        }

        response := xml.NewResponse()
        message := xml.NewMessage()
        message.SetText(body)
        message.SetSrc(to_number) // The Plivo number
        message.SetDst(from_number) // The original sender's number
        response.Add(message)

        xmlBytes, _ := response.ToXML()
        w.Header().Set("Content-Type", "application/xml")
        fmt.Fprint(w, string(xmlBytes))
    }

    func main() {
        http.HandleFunc("/autoresponder/", autoresponder)
        http.ListenAndServe(":8080", nil)
    }
    ```

    ***

    ### Create and configure a Plivo application

    1. **Create an Application**: Go to Messaging > [Applications](https://cx.plivo.com/xml-applications) and click **Add New Application**.
    2. **Configure the URL**: Name the application (e.g., `Autoresponder`). In the `Message URL` field, enter your server URL (e.g., `https://<yourdomain>.com/autoresponder/`) and set the method to `POST`. Click **Create Application**.
    3. **Assign a Number**: Go to the [Numbers](https://cx.plivo.com/phone-numbers) page, select your number, and link it to the `Autoresponder` application you just created.

    ***

    ### Test it out

    Send any SMS to your Plivo number to get the default reply. Then, send the word "Interested" to get the confirmation message.
  </Tab>
</Tabs>
