# Source: https://plivo.com/docs/messaging/use-cases/receive-mms/receive-mms.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Receive MMS Messages

> Handle inbound MMS multimedia messages on a Plivo phone number

This guide shows how to receive MMS messages on a Plivo phone number. You can do this using Plivo's APIs.

<Tabs>
  <Tab title="Using API">
    Here’s how to use Plivo APIs to receive MMS multimedia messages.

    ## How it works

    When someone sends an MMS to your Plivo number, Plivo forwards the message details, including the media URL, to a web server you control. Your server can then process this information.

        <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/receive-mms-api.jpg?fit=max&auto=format&n=7-odxN9fJG_Dg1dt&q=85&s=1acf1d91ec85934808b313f0c7f1e40f" alt="Receive MMS API workflow" width="1446" height="774" data-path="images/receive-mms-api.jpg" />

    ***

    ## Prerequisites

    To get started, you need a Plivo account — [sign up](https://cx.plivo.com/signup) if you don’t have one. You must also have a **Plivo phone number that supports MMS**. You can rent one from the [Numbers page](https://cx.plivo.com/phone-numbers) in the console or by using the [Numbers API](/numbers/).

    ***

    ## 1. Create a server to receive MMS messages

    First, create a web server that can receive POST requests from Plivo. The code below shows how to start a basic server that logs the `From` and `To` numbers, the `Text` body, and the `Media0` URL from an incoming MMS.

    Select your programming language to see the specific code.

    <Tabs>
      <Tab title="Node.js">
        If this is your first time using Plivo APIs with Node.js, follow our instructions to [set up your development environment](/sdk/server/set-up-node-dev-environment-api-messaging/).

        Create a file called `receive_mms.js` and paste this code into it.

        ```js  theme={null}
        const express = require('express');
        const bodyParser = require('body-parser');
        const app = express();

        app.use(bodyParser.urlencoded({ extended: true }));

        app.all('/receive_mms/', (request, response) => {
            const from_number = request.body.From;
            const to_number = request.body.To;
            const text = request.body.Text;
            const media_url = request.body.Media0;
            console.log('Message received - From: %s, To: %s, Text: %s, Media: %s', from_number, to_number, text, media_url);
            response.status(200).send('Message received');
        });

        app.listen(3000, () => {
            console.log('Server is running on port 3000');
        });
        ```
      </Tab>

      <Tab title="Ruby">
        If this is your first time using Plivo APIs with Ruby, follow our instructions to [set up your development environment](/sdk/server/set-up-ruby-dev-environment-api-messaging/).

        Create a Rails controller for inbound messages.

        ```shell  theme={null}
        $ rails generate controller Plivo receive_mms
        ```

        Edit `app/controllers/plivo_controller.rb` and paste in this code.

        ```rb  theme={null}
        class PlivoController < ApplicationController
          def receive_mms
            from_number = params[:From]
            to_number = params[:To]
            text = params[:Text]
            media_url = params[:Media0]
            puts "Message received - From: #{from_number}, To: #{to_number}, Text: #{text}, Media: #{media_url}"
            head :ok
          end
        end
        ```
      </Tab>

      <Tab title="Python">
        If this is your first time using Plivo APIs with Python, follow our instructions to [set up your development environment](/sdk/server/set-up-python-dev-environment-api-messaging/).

        Create a file called `receive_mms.py` and paste this code into it.

        ```py  theme={null}
        from flask import Flask, request

        app = Flask(__name__)

        @app.route('/receive_mms/', methods=['GET', 'POST'])
        def inbound_mms():
            from_number = request.values.get('From')
            to_number = request.values.get('To')
            text = request.values.get('Text')
            media_url = request.values.get('Media0')
            print(f'Message received - From: {from_number}, To: {to_number}, Text: {text}, Media: {media_url}')
            return 'Message Received'

        if __name__ == '__main__':
            app.run(host='0.0.0.0', port=3000)
        ```
      </Tab>

      <Tab title="PHP">
        If this is your first time using Plivo APIs with PHP, follow our instructions to [set up your development environment](/sdk/server/set-up-php-dev-environment-api-messaging/).

        Create a Laravel controller.

        ```shell  theme={null}
        $ php artisan make:controller MMSController
        ```

        Edit `app/Http/Controllers/MMSController.php` and paste in this code.

        ```php  theme={null}
        <?php
        namespace App\Http\Controllers;
        use Illuminate\Http\Request;
        use Illuminate\Http\Response;

        class MMSController extends Controller
        {
            public function receiveMms(Request $request)
            {
                $from_number = $request->input('From');
                $to_number = $request->input('To');
                $text = $request->input('Text');
                $media_url = $request->input('Media0');
                error_log("Message received - From: $from_number, To: $to_number, Text: $text, Media: $media_url");
                return new Response('Message received', 200);
            }
        }
        ```
      </Tab>

      <Tab title=".NET">
        If this is your first time using Plivo APIs with .NET, follow our instructions to [set up your development environment](/sdk/server/set-up-dotnet-dev-environment-api-messaging/).

        Create a new ASP.NET Core controller named `ReceiveMmsController.cs`.

        ```csharp  theme={null}
        using System;
        using Microsoft.AspNetCore.Mvc;

        namespace ReceiveMms.Controllers
        {
            [ApiController]
            public class ReceiveMmsController : ControllerBase
            {
                [HttpPost]
                [Route("/receive_mms/")]
                public IActionResult Index()
                {
                    string from_number = Request.Form["From"];
                    string to_number = Request.Form["To"];
                    string text = Request.Form["Text"];
                    string media_url = Request.Form["Media0"];
                    Console.WriteLine($"Message received - From: {from_number}, To: {to_number}, Text: {text}, Media: {media_url}");
                    return Ok("Message received");
                }
            }
        }
        ```
      </Tab>

      <Tab title="Java">
        If this is your first time using Plivo APIs with Java, follow our instructions to [set up your development environment](/sdk/server/set-up-java-dev-environment-api-messaging/).

        Create a new Spring Boot application and add this controller class.

        ```java  theme={null}
        package com.example.Plivo.MMS;
        import org.springframework.boot.SpringApplication;
        import org.springframework.boot.autoconfigure.SpringBootApplication;
        import org.springframework.web.bind.annotation.PostMapping;
        import org.springframework.web.bind.annotation.RequestParam;
        import org.springframework.web.bind.annotation.RestController;

        @RestController
        @SpringBootApplication
        public class ReceiveMmsApplication {
            public static void main(String[] args) {
                SpringApplication.run(ReceiveMmsApplication.class, args);
            }
            @PostMapping(value = "/receive_mms/")
            public String receiveMms(
                @RequestParam("From") String from, 
                @RequestParam("To") String to,
                @RequestParam("Text") String text, 
                @RequestParam(value="Media0", required=false) String mediaUrl
            ) {
                System.out.println("Message received - From: " + from + ", To: " + to + ", Text: " + text + ", Media: " + mediaUrl);
                return "Message received";
            }
        }
        ```
      </Tab>

      <Tab title="Go">
        If this is your first time using Plivo APIs with Go, follow our instructions to [set up your development environment](/sdk/server/set-up-go-dev-environment-api-messaging/).

        Create a file called `receive_mms.go` and paste this code into it.

        ```go  theme={null}
        package main
        import (
            "fmt"
            "net/http"
        )
        func receiveMmsHandler(w http.ResponseWriter, r *http.Request) {
            fromNumber := r.FormValue("From")
            toNumber := r.FormValue("To")
            text := r.FormValue("Text")
            mediaUrl := r.FormValue("Media0")
            fmt.Println("Message Received - From:", fromNumber, ", To:", toNumber, ", Text:", text, ", Media:", mediaUrl)
            w.WriteHeader(http.StatusOK)
        }
        func main() {
            http.HandleFunc("/receive_mms/", receiveMmsHandler)
            fmt.Println("Server listening on port 8080...")
            http.ListenAndServe(":8080", nil)
        }
        ```
      </Tab>
    </Tabs>

    ***

    ## 2. Expose your local server to the internet

    Once your server is running, make it accessible from the public internet so Plivo can send requests to it. We recommend using a tunneling service like [ngrok](https://ngrok.com/docs/getting-started/) for development.

    ```shell  theme={null}
    $ ngrok http 3000 
    # The port number should match the port your server is running on
    ```

    Ngrok will provide a public URL (e.g., `https://<unique-id>.ngrok-free.app`) that forwards traffic to your local server.

    ***

    ## 3. Create a Plivo application

    A Plivo application tells Plivo how to handle events like incoming messages.

    1. Navigate to Messaging > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click **Add New Application**.
    2. Give the application a name, like `Receive MMS App`.
    3. Enter your server's public URL into the `Message URL` field (e.g., `https://<unique-id>.ngrok-free.app/receive_mms/`) and set the method to `POST`.
    4. Click **Create Application**.

        <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/create_mms_app.png?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=b967acc01aa2ec91137bd7c7c70308fc" alt="Create Plivo Application for MMS" width="1440" height="821" data-path="images/create_mms_app.png" />

    ***

    ## 4. Assign a Plivo number to your application

    To start receiving messages, you must assign a Plivo phone number to the application.

    1. Go to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the number you want to use.
    2. In the **Application Type** drop-down, select `XML Application`.
    3. From the **Plivo Application** drop-down, select `Receive MMS App`.
    4. Click **Update Number**.

        <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign_MMS_app.jpg?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=9e96d822c99610dae36d1c2b19db377d" alt="Assign Phone Number to MMS App" width="1440" height="785" data-path="images/assign_MMS_app.jpg" />

    ***

    ## 5. Test it out

    Send an MMS message from your mobile phone to the Plivo number you assigned to the application. Your local server's console should print a log with the message details.
  </Tab>
</Tabs>
