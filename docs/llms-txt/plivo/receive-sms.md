# Source: https://plivo.com/docs/messaging/use-cases/receive-sms/receive-sms.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Receive SMS Messages

> Handle incoming SMS text messages on a Plivo phone number

<Tabs>
  <Tab title="Node">
    ## Overview

    This guide shows how to receive incoming SMS messages on a Plivo number using Plivo APIs and Node.js.

    ***

    ### How it works

    When Plivo receives an SMS on your Plivo number, it makes an HTTP request to the "Message URL" you configure in your Plivo Application. Your server receives this request, and you can process the data from the message (such as the sender's number, the recipient's number, and the text). Your server should respond with a `200 OK` status code to acknowledge receipt.

    ***

    ### Prerequisites

    To get started, you need a Plivo account — [**sign up**](https://cx.plivo.com/signup) if you don't have one. You'll also need a Plivo phone number that supports SMS. If you're new to Plivo APIs, follow our instructions to [**set up a Node.js development environment**](/sdk/server/set-up-node-dev-environment-api-messaging/).

    ***

    ### Create an Express server to receive messages

    Create a file named `receive_sms.js` and paste this code into it. This server listens for POST requests at the `/receive_sms/` endpoint and logs the message details to the console.

    ```js  theme={null}
    const express = require('express');
    const bodyParser = require('body-parser');
    const app = express();

    app.use(bodyParser.urlencoded({ extended: true }));

    app.all('/receive_sms/', (request, response) => {
        const from_number = request.body.From || request.query.From;
        const to_number = request.body.To || request.query.To;
        const text = request.body.Text || request.query.Text;

        console.log(`Message received - From: ${from_number}, To: ${to_number}, Text: ${text}`);

        // A 200 OK response is sent by default
        response.send("Message received");
    });

    app.listen(3000, () => {
        console.log('Node app is running on port 3000');
    });
    ```

    ***

    ### Create and configure a Plivo application

    1. **Create an Application**: Go to Messaging > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click **Add New Application**.
    2. **Configure the URL**: Give the application a name (e.g., `Receive SMS`). In the `Message URL` field, enter your server URL (e.g., `https://<yourdomain>.com/receive_sms/`) and set the method to `POST`. Click **Create Application**.
    3. **Assign a Number**: Navigate to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the phone number you want to use. In the "Application Type" dropdown, select `XML Application`, and in the "Plivo Application" dropdown, select the app you just created. Click **Update Number**.

    ***

    ### Test it out

    Send a text message to your Plivo number. Your console where the Node.js app is running should print the details of the message.
  </Tab>

  <Tab title="Ruby">
    ## Overview

    This guide shows how to receive incoming SMS messages on a Plivo number using Plivo APIs and Ruby on Rails.

    ***

    ### How it works

    When Plivo receives an SMS on your Plivo number, it makes an HTTP request to the "Message URL" you configure in your Plivo Application. Your server receives this request, and you can process the data from the message (such as the sender's number, the recipient's number, and the text). Your server should respond with a `200 OK` status code to acknowledge receipt.

    ***

    ### Prerequisites

    To get started, you need a Plivo account — [**sign up**](https://cx.plivo.com/signup) if you don't have one. You'll also need a Plivo phone number that supports SMS. If you're new to Plivo APIs, follow our instructions to [**set up a Ruby development environment**](/sdk/server/set-up-ruby-dev-environment-api-messaging/).

    ***

    ### Create a Rails controller to receive messages

    In `app/controllers/plivo_controller.rb`, paste this code. The `receivesms` action logs the message details and sends back a `200 OK` response to Plivo.

    ```rb  theme={null}
    class PlivoController < ApplicationController
      skip_before_action :verify_authenticity_token

      def receivesms
        from_number = params[:From]
        to_number = params[:To]
        text = params[:Text]

        puts "Message received - From: #{from_number}, To: #{to_number}, Text: #{text}"

        head :ok
      end
    end
    ```

    ***

    ### Create and configure a Plivo application

    1. **Create an Application**: Go to Messaging > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click **Add New Application**.
    2. **Configure the URL**: Give the application a name (e.g., `Receive SMS`). In the `Message URL` field, enter your server URL (e.g., `https://<yourdomain>.com/receive_sms/`) and set the method to `POST`. Click **Create Application**.
    3. **Assign a Number**: Navigate to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the phone number you want to use. In the "Application Type" dropdown, select `XML Application`, and in the "Plivo Application" dropdown, select the app you just created. Click **Update Number**.

    ***

    ### Test it out

    Send a text message to your Plivo number. Your console where the Rails app is running should print the details of the message.
  </Tab>

  <Tab title="Python">
    ## Overview

    This guide shows how to receive incoming SMS messages on a Plivo number using Plivo APIs with Python and Flask.

    ***

    ### How it works

    When Plivo receives an SMS on your Plivo number, it makes an HTTP request to the "Message URL" you configure in your Plivo Application. Your server receives this request, and you can process the data from the message (such as the sender's number, the recipient's number, and the text). Your server should respond with a `200 OK` status code to acknowledge receipt.

    ***

    ### Prerequisites

    To get started, you need a Plivo account — [**sign up**](https://cx.plivo.com/signup) if you don't have one. You'll also need a Plivo phone number that supports SMS. If you're new to Plivo APIs, follow our instructions to [**set up a Python development environment**](/sdk/server/set-up-python-dev-environment-api-messaging/).

    ***

    ### Create a Flask application to receive messages

    Create a file called `receive_sms.py` and paste into it this code. This app listens at `/receive_sms/`, logs message details, and returns a confirmation.

    ```py  theme={null}
    from flask import Flask, request

    app = Flask(__name__)

    @app.route('/receive_sms/', methods=['GET', 'POST'])
    def inbound_sms():
        from_number = request.values.get('From')
        to_number = request.values.get('To')
        text = request.values.get('Text')

        print(f'Message received - From: {from_number}, To: {to_number}, Text: {text}')

        return 'Message Received'

    if __name__ == '__main__':
        app.run(host='0.0.0.0', debug=True)
    ```

    ***

    ### Create and configure a Plivo application

    1. **Create an Application**: Go to Messaging > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click **Add New Application**.
    2. **Configure the URL**: Give the application a name (e.g., `Receive SMS`). In the `Message URL` field, enter your server URL (e.g., `https://<yourdomain>.com/receive_sms/`) and set the method to `POST`. Click **Create Application**.
    3. **Assign a Number**: Navigate to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the phone number you want to use. In the "Application Type" dropdown, select `XML Application`, and in the "Plivo Application" dropdown, select the app you just created. Click **Update Number**.

    ***

    ### Test it out

    Send a text message to your Plivo number. Your console where the Flask app is running should print the details of the message.
  </Tab>

  <Tab title="PHP">
    ## Overview

    This guide shows how to receive incoming SMS messages on a Plivo number using Plivo APIs with PHP.

    ***

    ### How it works

    When Plivo receives an SMS on your Plivo number, it makes an HTTP request to the "Message URL" you configure in your Plivo Application. Your server receives this request, and you can process the data from the message (such as the sender's number, the recipient's number, and the text). Your server should respond with a `200 OK` status code to acknowledge receipt.

    ***

    ### Prerequisites

    To get started, you need a Plivo account — [**sign up**](https://cx.plivo.com/signup) if you don't have one. You'll also need a Plivo phone number that supports SMS. If you're new to Plivo APIs, follow our instructions to [**set up a PHP development environment**](/sdk/server/set-up-php-dev-environment-api-messaging/).

    ***

    ### Create a server to receive messages

    Create a file and paste this code into it. This script will log the details of the incoming message.

    ```php  theme={null}
    <?php
    namespace App\Http\Controllers;
    require 'vendor/autoload.php';

    class SMSController extends Controller
    {
        public function receivesms()
        {
            $from_number = $_REQUEST["From"];
            $to_number = $_REQUEST["To"];
            $text = $_REQUEST["Text"];

            // For logging purposes
            error_log("Message received - From: $from_number, To: $to_number, Text: $text");

            // A 200 OK response is sent by default by the web server
        }
    }
    ```

    ***

    ### Create and configure a Plivo application

    1. **Create an Application**: Go to Messaging > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click **Add New Application**.
    2. **Configure the URL**: Give the application a name (e.g., `Receive SMS`). In the `Message URL` field, enter your server URL (e.g., `https://<yourdomain>.com/receive_sms/`) and set the method to `POST`. Click **Create Application**.
    3. **Assign a Number**: Navigate to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the phone number you want to use. In the "Application Type" dropdown, select `XML Application`, and in the "Plivo Application" dropdown, select the app you just created. Click **Update Number**.

    ***

    ### Test it out

    Send a text message to your Plivo number. The details of the message will be logged by your server.
  </Tab>

  <Tab title=".NET">
    ## Overview

    This guide shows how to receive incoming SMS messages on a Plivo number using Plivo APIs with .NET.

    ***

    ### How it works

    When Plivo receives an SMS on your Plivo number, it makes an HTTP request to the "Message URL" you configure in your Plivo Application. Your server receives this request, and you can process the data from the message (such as the sender's number, the recipient's number, and the text). Your server should respond with a `200 OK` status code to acknowledge receipt.

    ***

    ### Prerequisites

    To get started, you need a Plivo account — [**sign up**](https://cx.plivo.com/signup) if you don't have one. You'll also need a Plivo phone number that supports SMS. If you're new to Plivo APIs, follow our instructions to [**set up a .NET development environment**](/sdk/server/set-up-dotnet-dev-environment-api-messaging/).

    ***

    ### Create an MVC controller to receive messages

    In your controller, add an action to handle the incoming message. This code will log the message details and return a confirmation string.

    ```cs  theme={null}
    using System;
    using Microsoft.AspNetCore.Mvc;

    namespace ReceiveSms.Controllers
    {
        public class ReceiveSmsController : Controller
        {
            [HttpPost]
            public String Index()
            {
                String from_number = Request.Form["From"];
                String to_number = Request.Form["To"];
                String text = Request.Form["Text"];

                Console.WriteLine("Message received - From: {0}, To: {1}, Text: {2}", from_number, to_number, text);

                return "Message received";
            }
        }
    }
    ```

    ***

    ### Create and configure a Plivo application

    1. **Create an Application**: Go to Messaging > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click **Add New Application**.
    2. **Configure the URL**: Give the application a name (e.g., `Receive SMS`). In the `Message URL` field, enter your server URL (e.g., `https://<yourdomain>.com/receive_sms/`) and set the method to `POST`. Click **Create Application**.
    3. **Assign a Number**: Navigate to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the phone number you want to use. In the "Application Type" dropdown, select `XML Application`, and in the "Plivo Application" dropdown, select the app you just created. Click **Update Number**.

    ***

    ### Test it out

    Send a text message to your Plivo number. Your console where the .NET app is running should print the details of the message.
  </Tab>

  <Tab title="Java">
    ## Overview

    This guide shows how to receive incoming SMS messages on a Plivo number using Plivo APIs with Java and Spring.

    ***

    ### How it works

    When Plivo receives an SMS on your Plivo number, it makes an HTTP request to the "Message URL" you configure in your Plivo Application. Your server receives this request, and you can process the data from the message (such as the sender's number, the recipient's number, and the text). Your server should respond with a `200 OK` status code to acknowledge receipt.

    ***

    ### Prerequisites

    To get started, you need a Plivo account — [**sign up**](https://cx.plivo.com/signup) if you don't have one. You'll also need a Plivo phone number that supports SMS. If you're new to Plivo APIs, follow our instructions to [**set up a Java development environment**](/sdk/server/set-up-java-dev-environment-api-messaging/).

    ***

    ### Create a Spring application to receive messages

    In your main application file, paste this code to handle requests at the `/receive_sms/` endpoint.

    ```java  theme={null}
    package com.example.Plivo.SMS;

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

        @RequestMapping(value = "/receive_sms/")
        public String receiveSms(String From, String To, String Text) {
            System.out.println("Message received - From: " + From + ", To: " + To + ", Text: " + Text);
            return "Message received";
        }
    }
    ```

    ***

    ### Create and configure a Plivo application

    1. **Create an Application**: Go to Messaging > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click **Add New Application**.
    2. **Configure the URL**: Give the application a name (e.g., `Receive SMS`). In the `Message URL` field, enter your server URL (e.g., `https://<yourdomain>.com/receive_sms/`) and set the method to `POST`. Click **Create Application**.
    3. **Assign a Number**: Navigate to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the phone number you want to use. In the "Application Type" dropdown, select `XML Application`, and in the "Plivo Application" dropdown, select the app you just created. Click **Update Number**.

    ***

    ### Test it out

    Send a text message to your Plivo number. Your console where the Java app is running should print the details of the message.
  </Tab>

  <Tab title="Go">
    ## Overview

    This guide shows how to receive incoming SMS messages on a Plivo number using Plivo APIs with Go.

    ***

    ### How it works

    When Plivo receives an SMS on your Plivo number, it makes an HTTP request to the "Message URL" you configure in your Plivo Application. Your server receives this request, and you can process the data from the message (such as the sender's number, the recipient's number, and the text). Your server should respond with a `200 OK` status code to acknowledge receipt.

    ***

    ### Prerequisites

    To get started, you need a Plivo account — [**sign up**](https://cx.plivo.com/signup) if you don't have one. You'll also need a Plivo phone number that supports SMS. If you're new to Plivo APIs, follow our instructions to [**set up a Go development environment**](/sdk/server/set-up-go-dev-environment-api-messaging/).

    ***

    ### Create a Go server to receive messages

    Create a file called `receive_sms.go` and paste into it this code. The handler logs message details and sends a `204 No Content` response to acknowledge receipt.

    ```go  theme={null}
    package main

    import (
    	"fmt"
    	"net/http"
    )

    func receiveSms(w http.ResponseWriter, r *http.Request) {
    	from_number := r.FormValue("From")
    	to_number := r.FormValue("To")
    	text := r.FormValue("Text")

    	fmt.Printf("Message received - From: %s, To: %s, Text: %s\n", from_number, to_number, text)

    	w.WriteHeader(http.StatusNoContent)
    }

    func main() {
    	http.HandleFunc("/receive_sms/", receiveSms)
    	http.ListenAndServe(":8080", nil)
    }
    ```

    ***

    ### Create and configure a Plivo application

    1. **Create an Application**: Go to Messaging > [Applications](https://cx.plivo.com/xml-applications) in the Plivo console and click **Add New Application**.
    2. **Configure the URL**: Give the application a name (e.g., `Receive SMS`). In the `Message URL` field, enter your server URL (e.g., `https://<yourdomain>.com/receive_sms/`) and set the method to `POST`. Click **Create Application**.
    3. **Assign a Number**: Navigate to the [Numbers](https://cx.plivo.com/phone-numbers) page and select the phone number you want to use. In the "Application Type" dropdown, select `XML Application`, and in the "Plivo Application" dropdown, select the app you just created. Click **Update Number**.

    ***

    ### Test it out

    Send a text message to your Plivo number. Your console where the Go app is running should print the details of the message.
  </Tab>
</Tabs>
