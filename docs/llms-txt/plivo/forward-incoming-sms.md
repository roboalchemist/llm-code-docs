# Source: https://plivo.com/docs/messaging/use-cases/forward-incoming-sms/forward-incoming-sms.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Forward Incoming SMS Messages

> Forward incoming SMS messages from a Plivo number to another number

<Tabs>
  <Tab title="Node">
    ## Overview

    This guide shows how to forward incoming SMS messages from a Plivo phone number to another number using Plivo APIs and Node.js.

    ***

    ### How it works

    When Plivo receives an SMS on your Plivo number, it makes an HTTP request to the "Message URL" configured in your Plivo application. Your server receives this request and must respond with an XML document that contains instructions for Plivo. In this case, the XML instructs Plivo to send a new message containing the original text to a different destination number.

    ***

    ### Prerequisites

    To get started, you need a Plivo account — [**sign up**](https://cx.plivo.com/signup) if you don't have one. You'll also need a Plivo phone number that supports SMS. If you're new to Plivo APIs, follow our instructions to [**set up a Node.js development environment**](/sdk/server/set-up-node-dev-environment-api-messaging/).

    ***

    ### Create an Express server to forward messages

    Create a file named `forward_sms.js` and paste this code into it. Remember to replace the `<destination_number>` placeholder with the actual number you want to forward messages to, in E.164 format (e.g., `+12025551234`).

    ```js  theme={null}
    const plivo = require('plivo');
    const express = require('express');
    const bodyParser = require('body-parser');
    const app = express();

    app.use(bodyParser.urlencoded({ extended: true }));

    app.all('/forwardsms/', (request, response) => {
        const to_number = request.body.To || request.query.To;
        const text = request.body.Text || request.query.Text;

        const r = plivo.Response();
        const params = {
            'src': to_number, // The Plivo number the original message was sent to
            'dst': "<destination_number>", // The number to forward the message to
        };

        r.addMessage(text, params);

        response.type('application/xml');
        response.end(r.toXML());
    });

    app.listen(3000, () => {
        console.log('Node app is running on port 3000');
    });
    ```

    ***

    ### Create and configure a Plivo application

    1. **Create an Application**: Go to Messaging > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click **Add New Application**.
    2. **Configure the URL**: Give the application a name (e.g., `Forward SMS`). In the `Message URL` field, enter your server URL (e.g., `https://<yourdomain>.com/forwardsms/`) and set the method to `POST`. Click **Create Application**.
    3. **Assign a Number**: Navigate to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the phone number you want to use. In the "Application Type" dropdown, select `XML Application`, and in the "Plivo Application" dropdown, select the app you just created. Click **Update Number**.

    ***

    ### Test it out

    Send a text message to your Plivo number. The content of your message should be forwarded to the destination number you specified in the code.
  </Tab>

  <Tab title="Ruby">
    ## Overview

    This guide shows how to forward incoming SMS messages from a Plivo phone number to another number using Plivo APIs and Ruby on Rails.

    ***

    ### How it works

    When Plivo receives an SMS on your Plivo number, it makes an HTTP request to the "Message URL" configured in your Plivo application. Your server receives this request and must respond with an XML document that contains instructions for Plivo. In this case, the XML instructs Plivo to send a new message containing the original text to a different destination number.

    ***

    ### Prerequisites

    To get started, you need a Plivo account — [**sign up**](https://cx.plivo.com/signup) if you don't have one. You'll also need a Plivo phone number that supports SMS. If you're new to Plivo APIs, follow our instructions to [**set up a Ruby development environment**](/sdk/server/set-up-ruby-dev-environment-api-messaging/).

    ***

    ### Create a Rails controller to forward messages

    In your project directory, generate a controller and then add the forwarding logic. Remember to replace the `<destination_number>` placeholder with the actual number you want to forward messages to, in E.164 format (e.g., `+12025551234`).

    ```rb  theme={null}
    include Plivo
    include Plivo::Exceptions
    include Plivo::XML

    class PlivoController < ApplicationController
      skip_before_action :verify_authenticity_token
      def forwardsms
        to_number = params[:To]
        text = params[:Text]

        response = Response.new
        params = {
          src: to_number, # The Plivo number the original message was sent to
          dst: "<destination_number>", # The number to forward the message to
        }
        response.addMessage(text, params)
        xml = PlivoXML.new(response)

        render xml: xml.to_xml
      end
    end
    ```

    ***

    ### Create and configure a Plivo application

    1. **Create an Application**: Go to Messaging > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click **Add New Application**.
    2. **Configure the URL**: Give the application a name (e.g., `Forward SMS`). In the `Message URL` field, enter your server URL (e.g., `https://<yourdomain>.com/forwardsms/`) and set the method to `POST`. Click **Create Application**.
    3. **Assign a Number**: Navigate to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the phone number you want to use. In the "Application Type" dropdown, select `XML Application`, and in the "Plivo Application" dropdown, select the app you just created. Click **Update Number**.

    ***

    ### Test it out

    Send a text message to your Plivo number. The content of your message should be forwarded to the destination number you specified in the code.
  </Tab>

  <Tab title="Python">
    ## Overview

    This guide shows how to forward incoming SMS messages from a Plivo phone number to another number using Plivo APIs with Python and Flask.

    ***

    ### How it works

    When Plivo receives an SMS on your Plivo number, it makes an HTTP request to the "Message URL" configured in your Plivo application. Your server receives this request and must respond with an XML document that contains instructions for Plivo. In this case, the XML instructs Plivo to send a new message containing the original text to a different destination number.

    ***

    ### Prerequisites

    To get started, you need a Plivo account — [**sign up**](https://cx.plivo.com/signup) if you don't have one. You'll also need a Plivo phone number that supports SMS. If you're new to Plivo APIs, follow our instructions to [**set up a Python development environment**](/sdk/server/set-up-python-dev-environment-api-messaging/).

    ***

    ### Create a Flask server to forward messages

    Create a file called `forward_sms.py` and paste into it this code. Remember to replace the `<destination_number>` placeholder with an actual phone number in E.164 format (e.g., `+12025551234`).

    ```py  theme={null}
    from flask import Flask, request, Response
    from plivo import plivoxml

    app = Flask(__name__)

    @app.route('/forwardsms/', methods=['GET', 'POST'])
    def forward_sms():
        to_number = request.values.get('To')
        text = request.values.get('Text')

        response = plivoxml.ResponseElement()
        response.add(
            plivoxml.MessageElement(
                text,
                src=to_number,  # The Plivo number the original message was sent to
                dst="<destination_number>" # The number to forward the message to
            )
        )
        return Response(response.to_string(), mimetype='application/xml')

    if __name__ == '__main__':
        app.run(host='0.0.0.0', debug=True)
    ```

    ***

    ### Create and configure a Plivo application

    1. **Create an Application**: Go to Messaging > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click **Add New Application**.
    2. **Configure the URL**: Give the application a name (e.g., `Forward SMS`). In the `Message URL` field, enter your server URL (e.g., `https://<yourdomain>.com/forwardsms/`) and set the method to `POST`. Click **Create Application**.
    3. **Assign a Number**: Navigate to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the phone number you want to use. In the "Application Type" dropdown, select `XML Application`, and in the "Plivo Application" dropdown, select the app you just created. Click **Update Number**.

    ***

    ### Test it out

    Send a text message to your Plivo number. The content of your message should be forwarded to the destination number you specified in the code.
  </Tab>

  <Tab title="PHP">
    ## Overview

    This guide shows how to forward incoming SMS messages from a Plivo phone number to another number using Plivo APIs with PHP.

    ***

    ### How it works

    When Plivo receives an SMS on your Plivo number, it makes an HTTP request to the "Message URL" configured in your Plivo application. Your server receives this request and must respond with an XML document that contains instructions for Plivo. In this case, the XML instructs Plivo to send a new message containing the original text to a different destination number.

    ***

    ### Prerequisites

    To get started, you need a Plivo account — [**sign up**](https://cx.plivo.com/signup) if you don't have one. You'll also need a Plivo phone number that supports SMS. If you're new to Plivo APIs, follow our instructions to [**set up a PHP development environment**](/sdk/server/set-up-php-dev-environment-api-messaging/).

    ***

    ### Create a server to forward messages

    Create a file and paste this code into it. Remember to replace the `<destination_number>` placeholder with an actual phone number in E.164 format (e.g., `+12025551234`).

    ```php  theme={null}
    <?php
    require 'vendor/autoload.php';
    use Plivo\XML\Response;

    $to = $_REQUEST["To"];
    $text = $_REQUEST["Text"];

    $response = new Response();
    $params = array(
        'src' => $to, // The Plivo number the original message was sent to
        'dst' => "<destination_number>" // The number to forward the message to
    );

    $response->addMessage($text, $params);

    Header('Content-type: text/xml');
    echo($response->toXML());
    ```

    ***

    ### Create and configure a Plivo application

    1. **Create an Application**: Go to Messaging > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click **Add New Application**.
    2. **Configure the URL**: Give the application a name (e.g., `Forward SMS`). In the `Message URL` field, enter your server URL (e.g., `https://<yourdomain>.com/forwardsms/`) and set the method to `POST`. Click **Create Application**.
    3. **Assign a Number**: Navigate to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the phone number you want to use. In the "Application Type" dropdown, select `XML Application`, and in the "Plivo Application" dropdown, select the app you just created. Click **Update Number**.

    ***

    ### Test it out

    Send a text message to your Plivo number. The content of your message should be forwarded to the destination number you specified in the code.
  </Tab>

  <Tab title=".NET">
    ## Overview

    This guide shows how to forward incoming SMS messages from a Plivo phone number to another number using Plivo APIs with .NET MVC.

    ***

    ### How it works

    When Plivo receives an SMS on your Plivo number, it makes an HTTP request to the "Message URL" configured in your Plivo application. Your server receives this request and must respond with an XML document that contains instructions for Plivo. In this case, the XML instructs Plivo to send a new message containing the original text to a different destination number.

    ***

    ### Prerequisites

    To get started, you need a Plivo account — [**sign up**](https://cx.plivo.com/signup) if you don't have one. You'll also need a Plivo phone number that supports SMS. If you're new to Plivo APIs, follow our instructions to [**set up a .NET development environment**](/sdk/server/set-up-dotnet-dev-environment-api-messaging/).

    ***

    ### Create an MVC controller to forward messages

    In your controller, add an action to handle the incoming message. Remember to replace the `<destination_number>` placeholder with an actual phone number in E.164 format (e.g., `+12025551234`).

    ```cs  theme={null}
    using System;
    using System.Collections.Generic;
    using Microsoft.AspNetCore.Mvc;

    namespace Forwardsms.Controllers
    {
        public class ForwardsmsController : Controller
        {
            [HttpPost]
            public IActionResult Index()
            {
                String to_number = Request.Form["To"];
                String text = Request.Form["Text"];

                Plivo.XML.Response resp = new Plivo.XML.Response();
                resp.AddMessage(text, new Dictionary<string, string>()
                {
                    {"src", to_number}, // The Plivo number the original message was sent to
                    {"dst", "<destination_number>"}, // The number to forward the message to
                });

                return this.Content(resp.ToString(), "text/xml");
            }
        }
    }
    ```

    ***

    ### Create and configure a Plivo application

    1. **Create an Application**: Go to Messaging > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click **Add New Application**.
    2. **Configure the URL**: Give the application a name (e.g., `Forward SMS`). In the `Message URL` field, enter your server URL (e.g., `https://<yourdomain>.com/forwardsms/`) and set the method to `POST`. Click **Create Application**.
    3. **Assign a Number**: Navigate to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the phone number you want to use. In the "Application Type" dropdown, select `XML Application`, and in the "Plivo Application" dropdown, select the app you just created. Click **Update Number**.

    ***

    ### Test it out

    Send a text message to your Plivo number. The content of your message should be forwarded to the destination number you specified in the code.
  </Tab>

  <Tab title="Java">
    ## Overview

    This guide shows how to forward incoming SMS messages from a Plivo phone number to another number using Plivo APIs with Java and Spring.

    ***

    ### How it works

    When Plivo receives an SMS on your Plivo number, it makes an HTTP request to the "Message URL" configured in your Plivo application. Your server receives this request and must respond with an XML document that contains instructions for Plivo. In this case, the XML instructs Plivo to send a new message containing the original text to a different destination number.

    ***

    ### Prerequisites

    To get started, you need a Plivo account — [**sign up**](https://cx.plivo.com/signup) if you don't have one. You'll also need a Plivo phone number that supports SMS. If you're new to Plivo APIs, follow our instructions to [**set up a Java development environment**](/sdk/server/set-up-java-dev-environment-api-messaging/).

    ***

    ### Create a Spring application to forward messages

    Use [Spring Initializr](https://start.spring.io/) to create a project. In your main application file, paste this code to handle requests. Remember to replace the `<destination_number>` placeholder with an actual phone number in E.164 format (e.g., `+12025551234`).

    ```java  theme={null}
    package com.example.Plivo.SMS;

    import com.plivo.api.exceptions.PlivoXmlException;
    import com.plivo.api.xml.Message;
    import com.plivo.api.xml.Response;
    import org.springframework.boot.SpringApplication;
    import org.springframework.boot.autoconfigure.SpringBootApplication;
    import org.springframework.web.bind.annotation.RequestMapping;
    import org.springframework.web.bind.annotation.RestController;

    @RestController
    @SpringBootApplication
    public class PlivoSmsApplication {

        public static void main(String[] args) {
            SpringApplication.run(PlivoSmsApplication.class, args);
        }

        @RequestMapping(value = "/forwardsms/", produces = {"application/xml"})
        public String forwardSms(String To, String Text) throws PlivoXmlException {
            Response res = new Response().children(
                    new Message(Text, To, "<destination_number>")); // text, src, dst
            return res.toXmlString();
        }
    }
    ```

    ***

    ### Create and configure a Plivo application

    1. **Create an Application**: Go to Messaging > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click **Add New Application**.
    2. **Configure the URL**: Give the application a name (e.g., `Forward SMS`). In the `Message URL` field, enter your server URL (e.g., `https://<yourdomain>.com/forwardsms/`) and set the method to `POST`. Click **Create Application**.
    3. **Assign a Number**: Navigate to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the phone number you want to use. In the "Application Type" dropdown, select `XML Application`, and in the "Plivo Application" dropdown, select the app you just created. Click **Update Number**.

    ***

    ### Test it out

    Send a text message to your Plivo number. The content of your message should be forwarded to the destination number you specified in the code.
  </Tab>

  <Tab title="Go">
    ## Overview

    This guide shows how to forward incoming SMS messages from a Plivo phone number to another number using Plivo APIs with Go.

    ***

    ### How it works

    When Plivo receives an SMS on your Plivo number, it makes an HTTP request to the "Message URL" configured in your Plivo application. Your server receives this request and must respond with an XML document that contains instructions for Plivo. In this case, the XML instructs Plivo to send a new message containing the original text to a different destination number.

    ***

    ### Prerequisites

    To get started, you need a Plivo account — [**sign up**](https://cx.plivo.com/signup) if you don't have one. You'll also need a Plivo phone number that supports SMS. If you're new to Plivo APIs, follow our instructions to [**set up a Go development environment**](/sdk/server/set-up-go-dev-environment-api-messaging/).

    ***

    ### Create a Go server to forward messages

    Create a file called `forward_sms.go` and paste this code into it. Remember to replace the `<destination_number>` placeholder with an actual phone number in E.164 format (e.g., `+12025551234`).

    ```go  theme={null}
    package main

    import (
    	"fmt"
    	"net/http"
    	"[github.com/plivo/plivo-go/v7/xml](https://github.com/plivo/plivo-go/v7/xml)"
    )

    func forwardSms(w http.ResponseWriter, r *http.Request) {
    	tonumber := r.FormValue("To")
    	text := r.FormValue("Text")

    	response := xml.NewResponse()
    	message := xml.NewMessage()
    	message.SetText(text)
    	message.SetSrc(tonumber) // The Plivo number the original message was sent to
    	message.SetDst("<destination_number>") // The number to forward the message to

    	response.Add(message)

    	xmlBytes, _ := response.ToXML()
        w.Header().Set("Content-Type", "application/xml")
    	fmt.Fprint(w, string(xmlBytes))
    }

    func main() {
    	http.HandleFunc("/forwardsms/", forwardSms)
    	http.ListenAndServe(":8080", nil)
    }
    ```

    ***

    ### Create and configure a Plivo application

    1. **Create an Application**: Go to Messaging > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click **Add New Application**.
    2. **Configure the URL**: Give the application a name (e.g., `Forward SMS`). In the `Message URL` field, enter your server URL (e.g., `https://<yourdomain>.com/forwardsms/`) and set the method to `POST`. Click **Create Application**.
    3. **Assign a Number**: Navigate to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the phone number you want to use. In the "Application Type" dropdown, select `XML Application`, and in the "Plivo Application" dropdown, select the app you just created. Click **Update Number**.

    ***

    ### Test it out

    Send a text message to your Plivo number. The content of your message should be forwarded to the destination number you specified in the code.
  </Tab>
</Tabs>
