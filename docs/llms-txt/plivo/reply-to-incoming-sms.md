# Source: https://plivo.com/docs/messaging/use-cases/reply-to-incoming-sms/reply-to-incoming-sms.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Reply to Incoming SMS

> Receive and send automated replies to incoming SMS text messages

<Tabs>
  <Tab title="Node">
    ## Overview

    This guide shows how to receive and reply to SMS text messages on a Plivo phone number using Plivo APIs and Node.js.

    ***

    ### Prerequisites

    To get started, you need a Plivo account — [**sign up**](https://cx.plivo.com/signup) if you don't have one. You'll also need a Plivo phone number that supports SMS. If you're new to Plivo APIs, follow our instructions to [**set up a Node.js development environment**](/sdk/server/set-up-node-dev-environment-api-messaging/) and expose your web server to the internet.

    ***

    ### Create an Express server to reply to messages

    Create a file named `reply_sms.js` and paste this code into it. This server listens for incoming messages at the `/replysms/` endpoint and replies with a thank you message using Plivo's XML.

    ```js  theme={null}
    const plivo = require('plivo');
    const express = require('express');
    const bodyParser = require('body-parser');
    const app = express();

    app.use(bodyParser.urlencoded({ extended: true }));
    app.use((req, response, next) => {
        response.contentType('application/xml');
        next();
    });

    app.set('port', (process.env.PORT || 3000));

    app.all('/replysms/', (request, response) => {
        const from_number = request.body.From || request.query.From;
        const to_number = request.body.To || request.query.To;
        const text = request.body.Text || request.query.Text;
        console.log(`Message received - From: ${from_number}, To: ${to_number}, Text: ${text}`);

        const r = plivo.Response();
        const params = {
            'src': to_number,
            'dst': from_number,
        };
        const message_body = "Thank you, we received your request";
        r.addMessage(message_body, params);

        response.end(r.toXML());
    });

    app.listen(app.get('port'), () => {
        console.log('Node app is running on port', app.get('port'));
    });
    ```

    ***

    ### Create and configure a Plivo application

    1. **Create an Application**: Go to Messaging > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click **Add New Application**.
    2. **Configure the URL**: Give the application a name (e.g., `Reply Incoming SMS`). In the `Message URL` field, enter your server URL (e.g., `https://<yourdomain>.com/replysms/`) and set the method to `POST`. Click **Create Application**.
    3. **Assign a Number**: Navigate to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the phone number you want to use. In the "Application Type" dropdown, select `XML Application`, and in the "Plivo Application" dropdown, select the app you just created. Click **Update Number**.

    ***

    ### Test it out

    Send a text message to your Plivo number. You should receive an automated reply saying, "Thank you, we received your request."
  </Tab>

  <Tab title="Ruby">
    ## Overview

    This guide shows how to receive and reply to SMS text messages on a Plivo phone number using Plivo APIs and Ruby on Rails.

    ***

    ### Prerequisites

    To get started, you need a Plivo account — [**sign up**](https://cx.plivo.com/signup) if you don't have one. You'll also need a Plivo phone number that supports SMS. If you're new to Plivo APIs, follow our instructions to [**set up a Ruby development environment**](/sdk/server/set-up-ruby-dev-environment-api-messaging/) and expose your web server to the internet.

    ***

    ### Create a Rails controller to reply to messages

    1. **Generate Controller**: In your project directory, run this command to create a controller and an `sms` action.

       ```shell  theme={null}
       $ rails generate controller Plivo sms
       ```

       You can delete the generated view file at `app/views/plivo/sms.html.erb`.
    2. **Add Code**: Edit the new file at `app/controllers/plivo_controller.rb` and paste in this code.

       ```rb  theme={null}
       include Plivo
       include Plivo::Exceptions
       include Plivo::XML

       class PlivoController < ApplicationController
         skip_before_action :verify_authenticity_token
         def replysms
           from_number = params[:From]
           to_number = params[:To]
           text = params[:Text]
           response = Response.new
           params = {
             src: to_number,
             dst: from_number,
           }
           message_body = "Thank you, we received your request"
           response.addMessage(message_body, params)
           xml = PlivoXML.new(response)
           puts xml.to_xml
           render xml: xml.to_xml
         end
       end
       ```
    3. **Add Route**: Edit `config/routes.rb` to route POST requests for `/plivo/replysms/` to your new controller action.

       ```ruby  theme={null}
       Rails.application.routes.draw do
         post 'plivo/replysms/' => 'plivo#replysms'
       end
       ```
    4. **Run Server**: Start the Rails server.

       ```shell  theme={null}
       $ rails server
       ```

       <Note>
         For ngrok testing, add this line to `config/environments/development.rb`:\
         `config.hosts << /[a-z0-9-]+\.ngrok\.io/`
       </Note>

    ***

    ### Create and configure a Plivo application

    1. **Create an Application**: Go to Messaging > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click **Add New Application**.
    2. **Configure the URL**: Give the application a name (e.g., `Reply Incoming SMS`). In the `Message URL` field, enter your server URL (e.g., `https://<yourdomain>.com/plivo/replysms/`) and set the method to `POST`. Click **Create Application**.
    3. **Assign a Number**: Navigate to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the phone number you want to use. In the "Application Type" dropdown, select `XML Application`, and in the "Plivo Application" dropdown, select the app you just created. Click **Update Number**.

    ***

    ### Test it out

    Send a text message to your Plivo number. You should receive an automated reply saying, "Thank you, we received your request."
  </Tab>

  <Tab title="Python">
    ## Overview

    This guide shows how to receive and reply to SMS text messages on a Plivo phone number using Plivo APIs with Python and Flask.

    ***

    ### Prerequisites

    To get started, you need a Plivo account — [**sign up**](https://cx.plivo.com/signup) if you don't have one. You'll also need a Plivo phone number that supports SMS. If you're new to Plivo APIs, follow our instructions to [**set up a Python development environment**](/sdk/server/set-up-python-dev-environment-api-messaging/) and expose your web server to the internet.

    ***

    ### Create a Flask application to reply to messages

    Create a file named `reply_sms.py` and paste this code into it. This Flask app listens for incoming messages at `/replysms/` and uses Plivo's XML library to generate a reply.

    ```py  theme={null}
    from flask import Flask, request, Response
    from plivo import plivoxml

    app = Flask(__name__)

    @app.route('/replysms/', methods=['GET', 'POST'])
    def reply_sms():
        from_number = request.values.get('From')
        to_number = request.values.get('To')

        response = plivoxml.ResponseElement()
        response.add(
            plivoxml.MessageElement(
                "Thank you, we received your request",
                src=to_number,
                dst=from_number
            )
        )
        return Response(response.to_string(), mimetype='application/xml')

    if __name__ == '__main__':
        app.run(host='0.0.0.0', debug=True)
    ```

    ***

    ### Create and configure a Plivo application

    1. **Create an Application**: Go to Messaging > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click **Add New Application**.
    2. **Configure the URL**: Give the application a name (e.g., `Reply Incoming SMS`). In the `Message URL` field, enter your server URL (e.g., `https://<yourdomain>.com/replysms/`) and set the method to `POST`. Click **Create Application**.
    3. **Assign a Number**: Navigate to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the phone number you want to use. In the "Application Type" dropdown, select `XML Application`, and in the "Plivo Application" dropdown, select the app you just created. Click **Update Number**.

    ***

    ### Test it out

    Send a text message to your Plivo number. You should receive an automated reply saying, "Thank you, we received your request."
  </Tab>

  <Tab title="PHP">
    ## Overview

    This guide shows how to receive and reply to SMS text messages on a Plivo phone number using Plivo APIs with PHP and Laravel.

    ***

    ### Prerequisites

    To get started, you need a Plivo account — [**sign up**](https://cx.plivo.com/signup) if you don't have one. You'll also need a Plivo phone number that supports SMS. If you're new to Plivo APIs, follow our instructions to [**set up a PHP development environment**](/sdk/server/set-up-php-dev-environment-api-messaging/) and expose your web server to the internet.

    ***

    ### Create a Laravel controller to reply to messages

    1. **Generate Controller**: In your project directory, run this command:

       ```shell  theme={null}
       php artisan make:controller SMSController
       ```
    2. **Add Code**: Edit the new file at `app/Http/Controllers/SMSController.php` and paste in this code. It defines the `replysms` method that handles incoming messages.

       ```php  theme={null}
       <?php
       namespace App\Http\Controllers;

       require_once 'vendor/autoload.php';
       use Plivo\XML\Response;

       class SMSController extends Controller
       {
           public function replysms()
           {
               $from_number = $_REQUEST["From"];
               $to_number = $_REQUEST["To"];

               $response = new Response();
               $params = array(
                   'src' => $to_number,
                   'dst' => $from_number,
               );
               $message_body = "Thank you, we received your request";
               $response->addMessage($message_body, $params);

               header('Content-Type: text/xml');
               echo($response->toXML());
           }
       }
       ```
    3. **Add a route** for the `replysms` function in your Laravel application.

    ***

    ### Create and configure a Plivo application

    1. **Create an Application**: Go to Messaging > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click **Add New Application**.
    2. **Configure the URL**: Give the application a name (e.g., `Reply Incoming SMS`). In the `Message URL` field, enter your server URL (e.g., `https://<yourdomain>.com/replysms/`) and set the method to `POST`. Click **Create Application**.
    3. **Assign a Number**: Navigate to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the phone number you want to use. In the "Application Type" dropdown, select `XML Application`, and in the "Plivo Application" dropdown, select the app you just created. Click **Update Number**.

    ***

    ### Test it out

    Send a text message to your Plivo number. You should receive an automated reply saying, "Thank you, we received your request."
  </Tab>

  <Tab title=".NET">
    ## Overview

    This guide shows how to receive and reply to SMS text messages on a Plivo phone number using Plivo APIs with .NET MVC.

    ***

    ### Prerequisites

    To get started, you need a Plivo account — [**sign up**](https://cx.plivo.com/signup) if you don't have one. You'll also need a Plivo phone number that supports SMS. If you're new to Plivo APIs, follow our instructions to [**set up a .NET development environment**](/sdk/server/set-up-dotnet-dev-environment-api-messaging/) and expose your web server to the internet.

    ***

    ### Create an MVC controller to reply to messages

    1. **Create Project**: In Visual Studio, create a new **ASP.NET Web Application (.NET Framework)** and select the **MVC** template.
    2. **Add Controller**: In the `Controllers` directory, create a new controller named `ReplysmsController.cs`.
    3. **Add Code**: Paste this code into your new controller. It reads the `From` and `To` numbers from the incoming request and builds a Plivo XML response to send a message back.

       ```cs  theme={null}
       using System;
       using System.Collections.Generic;
       using Microsoft.AspNetCore.Mvc;

       namespace Replysms.Controllers
       {
           public class ReplysmsController : Controller
           {
               [HttpPost]
               public IActionResult Index()
               {
                   String from_number = Request.Form["From"];
                   String to_number = Request.Form["To"];

                   Plivo.XML.Response resp = new Plivo.XML.Response();
                   resp.AddMessage("Thank you, we received your request", new Dictionary<string, string>()
                   {
                       {"src", to_number},
                       {"dst", from_number}
                   });

                   return this.Content(resp.ToString(), "text/xml");
               }
           }
       }
       ```

    ***

    ### Create and configure a Plivo application

    1. **Create an Application**: Go to Messaging > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click **Add New Application**.
    2. **Configure the URL**: Give the application a name (e.g., `Reply Incoming SMS`). In the `Message URL` field, enter your server URL (e.g., `https://<yourdomain>.com/replysms/`) and set the method to `POST`. Click **Create Application**.
    3. **Assign a Number**: Navigate to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the phone number you want to use. In the "Application Type" dropdown, select `XML Application`, and in the "Plivo Application" dropdown, select the app you just created. Click **Update Number**.

    ***

    ### Test it out

    Send a text message to your Plivo number. You should receive an automated reply saying, "Thank you, we received your request."
  </Tab>

  <Tab title="Java">
    ## Overview

    This guide shows how to receive and reply to SMS text messages on a Plivo phone number using Plivo APIs with Java and Spring.

    ***

    ### Prerequisites

    To get started, you need a Plivo account — [**sign up**](https://cx.plivo.com/signup) if you don't have one. You'll also need a Plivo phone number that supports SMS. If you're new to Plivo APIs, follow our instructions to [**set up a Java development environment**](/sdk/server/set-up-java-dev-environment-api-messaging/) and expose your web server to the internet.

    ***

    ### Create a Spring application to reply to messages

    Use [Spring Initializr](https://start.spring.io/) to create a boilerplate project. In your main application file, paste this code to handle incoming requests at the `/replysms/` endpoint.

    ```java  theme={null}
    package com.example.Plivo.SMS;

    import com.plivo.api.exceptions.PlivoXmlException;
    import com.plivo.api.xml.Message;
    import com.plivo.api.xml.Response;
    import org.springframework.boot.SpringApplication;
    import org.springframework.boot.autoconfigure.SpringBootApplication;
    import org.springframework.web.bind.annotation.GetMapping;
    import org.springframework.web.bind.annotation.RestController;

    @RestController
    @SpringBootApplication
    public class PlivoSmsApplication {

        public static void main(String[] args) {
            SpringApplication.run(PlivoSmsApplication.class, args);
        }

        @GetMapping(value = "/replysms/", produces = {"application/xml"})
        public String replySms(String From, String To, String Text) throws PlivoXmlException {
            Response res = new Response().children(
                    new Message("Thank you, we received your request", To, From)
            );
            return res.toXmlString();
        }

    }
    ```

    ***

    ### Create and configure a Plivo application

    1. **Create an Application**: Go to Messaging > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click **Add New Application**.
    2. **Configure the URL**: Give the application a name (e.g., `Reply Incoming SMS`). In the `Message URL` field, enter your server URL (e.g., `https://<yourdomain>.com/replysms/`) and set the method to `POST`. Click **Create Application**.
    3. **Assign a Number**: Navigate to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the phone number you want to use. In the "Application Type" dropdown, select `XML Application`, and in the "Plivo Application" dropdown, select the app you just created. Click **Update Number**.

    ***

    ### Test it out

    Send a text message to your Plivo number. You should receive an automated reply saying, "Thank you, we received your request."
  </Tab>
</Tabs>
