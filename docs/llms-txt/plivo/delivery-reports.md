# Source: https://plivo.com/docs/messaging/use-cases/delivery-reports/delivery-reports.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Delivery Reports

> Track SMS delivery status with message delivery report callbacks

<Tabs>
  <Tab title="Node">
    ## Overview

    This guide shows how to receive delivery reports for your SMS messages using Plivo's APIs and Node.js. Delivery reports are webhooks Plivo sends to your application to notify you of the status of inbound or outbound messages.

    ***

    ### How it works

    * **Outbound Messages**: When you send an SMS using Plivo's API, you can include a `url` parameter. Plivo will send a POST request to this URL with the status of the message (`sent`, `delivered`, `failed`, etc.).
    * **Inbound Messages**: When you receive an SMS on a Plivo number, Plivo sends the message details to the `Message URL` configured on your Plivo Application.

    In both cases, your application should be set up to receive these POST requests, log the data, and return a `200 OK` response to acknowledge receipt.

    ***

    ### Prerequisites

    * A Plivo account — [**sign up for free**](https://cx.plivo.com/signup).
    * An SMS-enabled Plivo phone number. You can [**rent a number**](/numbers/).
    * Node.js and ngrok. See our [**Node.js setup guide**](/sdk/server/set-up-node-dev-environment-api-messaging/).

    ***

    ### Create a server to receive delivery reports

    Create a file named `delivery_reports.js` and paste this code into it. This Express server has a single endpoint that logs the body of incoming POST requests to the console.

    ```js  theme={null}
    const express = require('express');
    const bodyParser = require('body-parser');
    const app = express();

    app.use(bodyParser.urlencoded({ extended: true }));
    app.set('port', (process.env.PORT || 5000));

    app.all('/delivery_report/', (request, response) => {
        console.log("Delivery Report Received:");
        console.log(request.body);
        response.status(204).send(); // Acknowledge receipt
    });

    app.listen(app.get('port'), () => {
        console.log('Node app is running on port', app.get('port'));
    });
    ```

    ***

    ### Test

    1. Run your server: `node delivery_reports.js`.
    2. Expose your local server to the internet using ngrok: `ngrok http 5000`.

    **For Outbound Reports:**

    * Use the following script to send a message. Replace the placeholders and use your ngrok URL for the `url` parameter.

      ```js  theme={null}
      const plivo = require('plivo');
      const client = new plivo.Client("<auth_id>", "<auth_token>");

      client.messages.create({
          src: "<sender_id>",
          dst: "<destination_number>",
          text: "Hello, this is a test for delivery reports!",
          url: "https://<your-ngrok-url>.ngrok.io/delivery_report/"
      }).then(response => console.log(response));
      ```
    * Check your terminal. You should see the delivery status updates logged by your server.

    **For Inbound Reports:**

    * Create a Plivo Application with the `Message URL` set to `https://<your-ngrok-url>.ngrok.io/delivery_report/`.
    * Assign a Plivo number to the application.
    * Send an SMS to your Plivo number. The message details will appear in your terminal.
  </Tab>

  <Tab title="Ruby">
    ## Overview

    This guide shows how to receive delivery reports for your SMS messages using Plivo's APIs and Ruby on Rails. Delivery reports are webhooks Plivo sends to your application to notify you of the status of inbound or outbound messages.

    ***

    ### How it works

    * **Outbound Messages**: When you send an SMS, include a `url` parameter. Plivo will POST the delivery status to this URL.
    * **Inbound Messages**: When you receive an SMS, Plivo sends the message details to your `Message URL`.

    Your Rails application needs a route and controller action to receive these POST requests, log the data, and return a `200 OK` response.

    ***

    ### Prerequisites

    * A Plivo account — [**sign up for free**](https://cx.plivo.com/signup).
    * An SMS-enabled Plivo phone number. You can [**rent a number**](/numbers/).
    * Ruby on Rails and ngrok. See our [**Ruby setup guide**](/sdk/server/set-up-ruby-dev-environment-api-messaging/).

    ***

    ### Create a controller to receive delivery reports

    In your controller (e.g., `app/controllers/plivo_controller.rb`), add this action. It will log all parameters from the incoming webhook.

    ```rb  theme={null}
    class PlivoController < ApplicationController
      skip_before_action :verify_authenticity_token

      def delivery_report
        puts "Delivery Report Received:"
        puts params.inspect
        head :ok # Acknowledge receipt with 200 OK
      end
    end
    ```

    In `config/routes.rb`, add a route for this action:

    ```ruby  theme={null}
    Rails.application.routes.draw do
      post 'plivo/delivery_report' => 'plivo#delivery_report'
    end
    ```

    ***

    ### Test

    1. Run your server: `rails server`.
    2. Expose your server to the internet using ngrok: `ngrok http 3000`.

    **For Outbound Reports:**

    * Use the following script to send a message. Replace the placeholders and use your ngrok URL.

      ```rb  theme={null}
      require "plivo"
      include Plivo

      api = RestClient.new("<auth_id>", "<auth_token>")
      response = api.messages.create(
          src: "<sender_id>",
          dst: "<destination_number>",
          text: "Hello from Ruby!",
          url: "https://<your-ngrok-url>.ngrok.io/plivo/delivery_report",
      )
      puts response
      ```
    * Check your terminal for the delivery status logs.

    **For Inbound Reports:**

    * Create a Plivo Application with the `Message URL` set to `https://<your-ngrok-url>.ngrok.io/plivo/delivery_report`.
    * Assign a Plivo number to it.
    * Send an SMS to your Plivo number and check your terminal for the message details.
  </Tab>

  <Tab title="Python">
    ## Overview

    This guide shows how to receive delivery reports for your SMS messages using Plivo's APIs and Python with Flask. Delivery reports are webhooks Plivo sends to your application to notify you of the status of inbound or outbound messages.

    ***

    ### How it works

    * **Outbound Messages**: When you send an SMS, include a `url` parameter. Plivo will POST the delivery status to this URL.
    * **Inbound Messages**: When you receive an SMS, Plivo sends the message details to your `Message URL`.

    Your Flask application needs an endpoint to receive these POST requests, log the data, and return a `200 OK` response.

    ***

    ### Prerequisites

    * A Plivo account — [**sign up for free**](https://cx.plivo.com/signup).
    * An SMS-enabled Plivo phone number. You can [**rent a number**](/numbers/).
    * Python and ngrok. See our [**Python setup guide**](/sdk/server/set-up-python-dev-environment-api-messaging/).

    ***

    ### Create a server to receive delivery reports

    Create a file named `delivery_reports.py` and paste this code into it.

    ```py  theme={null}
    from flask import Flask, request

    app = Flask(__name__)

    @app.route('/delivery_report/', methods=['POST'])
    def delivery_report():
        print("Delivery Report Received:")
        print(request.form.to_dict())
        return ('Report Received', 200)

    if __name__ == '__main__':
        app.run(host='0.0.0.0', debug=True)
    ```

    ***

    ### Test

    1. Run your server: `python delivery_reports.py`.
    2. Expose your server to the internet using ngrok: `ngrok http 5000`.

    **For Outbound Reports:**

    * Use this script to send a message. Replace placeholders and use your ngrok URL.

      ```py  theme={null}
      import plivo
      client = plivo.RestClient('<auth_id>', '<auth_token>')
      response = client.messages.create(
          src='<sender_id>',
          dst='<destination_number>',
          text='Hello from Python!',
          url='https://<your-ngrok-url>.ngrok.io/delivery_report/',
      )
      print(response)
      ```
    * Check your terminal for delivery status logs.

    **For Inbound Reports:**

    * Create a Plivo Application with the `Message URL` set to `https://<your-ngrok-url>.ngrok.io/delivery_report/`.
    * Assign a Plivo number to it.
    * Send an SMS to your Plivo number and check your terminal for the message details.
  </Tab>

  <Tab title="PHP">
    ## Overview

    This guide shows how to receive delivery reports for your SMS messages using Plivo's APIs and PHP. Delivery reports are webhooks Plivo sends to your application to notify you of the status of inbound or outbound messages.

    ***

    ### How it works

    * **Outbound Messages**: When you send an SMS, include a `url` parameter. Plivo will POST the delivery status to this URL.
    * **Inbound Messages**: When you receive an SMS, Plivo sends the message details to your `Message URL`.

    Your PHP application needs a script to receive these POST requests, log the data, and return a `200 OK` response.

    ***

    ### Prerequisites

    * A Plivo account — [**sign up for free**](https://cx.plivo.com/signup).
    * An SMS-enabled Plivo phone number. You can [**rent a number**](/numbers/).
    * PHP, Composer, and ngrok. See our [**PHP setup guide**](/sdk/server/set-up-php-dev-environment-api-messaging/).

    ***

    ### Create a script to receive delivery reports

    Create a file named `delivery_report.php` and paste this code into it.

    ```php  theme={null}
    <?php
    // Log all POST data to a file
    $post_data = file_get_contents('php://input');
    $log_file = 'delivery_reports.log';
    file_put_contents($log_file, "--- Delivery Report ---\n", FILE_APPEND);
    file_put_contents($log_file, $post_data . "\n\n", FILE_APPEND);

    // Acknowledge the webhook
    http_response_code(204);
    ?>
    ```

    ***

    ### Test

    1. Start your PHP server in the directory with your file.
    2. Expose your server to the internet using ngrok.

    **For Outbound Reports:**

    * Use this script to send a message. Replace placeholders and use your ngrok URL.

      ```php  theme={null}
      <?php
      require 'vendor/autoload.php';
      use Plivo\RestClient;
      $client = new RestClient("<auth_id>", "<auth_token>");
      $response = $client->messages->create([
          "src" => "<sender_id>",
          "dst" => "<destination_number>",
          "text" => "Hello from PHP!",
          "url" => "https://<your-ngrok-url>.ngrok.io/delivery_report.php"
      ]);
      print_r($response);
      ?>
      ```
    * Check the `delivery_reports.log` file for status updates.

    **For Inbound Reports:**

    * Create a Plivo Application with the `Message URL` set to `https://<your-ngrok-url>.ngrok.io/delivery_report.php`.
    * Assign a Plivo number to it.
    * Send an SMS to your Plivo number and check the log file.
  </Tab>

  <Tab title=".NET">
    ## Overview

    This guide shows how to receive delivery reports for your SMS messages using Plivo's APIs and .NET. Delivery reports are webhooks Plivo sends to your application to notify you of the status of inbound or outbound messages.

    ***

    ### How it works

    * **Outbound Messages**: When you send an SMS, include a `url` parameter. Plivo will POST the delivery status to this URL.
    * **Inbound Messages**: When you receive an SMS, Plivo sends the message details to your `Message URL`.

    Your .NET application needs a controller action to receive these POST requests, log the data, and return a `200 OK` response.

    ***

    ### Prerequisites

    * A Plivo account — [**sign up for free**](https://cx.plivo.com/signup).
    * An SMS-enabled Plivo phone number. You can [**rent a number**](/numbers/).
    * .NET and ngrok. See our [**.NET setup guide**](/sdk/server/set-up-dotnet-dev-environment-api-messaging/).

    ***

    ### Create a controller to receive delivery reports

    In your controller (e.g., `DeliveryReportController.cs`), add this action. It will log all form fields from the incoming webhook.

    ```csharp  theme={null}
    using System;
    using Microsoft.AspNetCore.Mvc;

    namespace Demo.Controllers
    {
        public class DeliveryReport : Controller
        {
            [HttpPost]
            public IActionResult Index()
            {
                Console.WriteLine("--- Delivery Report Received ---");
                foreach (var key in Request.Form.Keys)
                {
                    Console.WriteLine($"{key}: {Request.Form[key]}");
                }
                return Ok("Report Received");
            }
        }
    }
    ```

    ***

    ### Test

    1. Run your project.
    2. Expose your server to the internet using ngrok.

    **For Outbound Reports:**

    * Use this code to send a message. Replace placeholders and use your ngrok URL.

      ```csharp  theme={null}
      var api = new PlivoApi("<auth_id>", "<auth_token>");
      var response = api.Message.Create(
          src: "<sender_id>",
          dst: new List<string> { "<destination_number>" },
          text: "Hello from .NET!",
          url: "https://<your-ngrok-url>.ngrok.io/DeliveryReport"
      );
      Console.WriteLine(response);
      ```
    * Check your console for delivery status logs.

    **For Inbound Reports:**

    * Create a Plivo Application with the `Message URL` set to `https://<your-ngrok-url>.ngrok.io/DeliveryReport`.
    * Assign a Plivo number to it.
    * Send an SMS to your Plivo number and check your console.
  </Tab>

  <Tab title="Java">
    ## Overview

    This guide shows how to receive delivery reports for your SMS messages using Plivo's APIs and Java with Spring. Delivery reports are webhooks Plivo sends to your application to notify you of the status of inbound or outbound messages.

    ***

    ### How it works

    * **Outbound Messages**: When you send an SMS, include a `url` parameter. Plivo will POST the delivery status to this URL.
    * **Inbound Messages**: When you receive an SMS, Plivo sends the message details to your `Message URL`.

    Your Spring application needs an endpoint to receive these POST requests, log the data, and return a `200 OK` response.

    ***

    ### Prerequisites

    * A Plivo account — [**sign up for free**](https://cx.plivo.com/signup).
    * An SMS-enabled Plivo phone number. You can [**rent a number**](/numbers/).
    * Java and ngrok. See our [**Java setup guide**](/sdk/server/set-up-java-dev-environment-api-messaging/).

    ***

    ### Create a controller to receive delivery reports

    In your main application file, paste this code.

    ```java  theme={null}
    package com.example.demo;

    import org.springframework.boot.SpringApplication;
    import org.springframework.boot.autoconfigure.SpringBootApplication;
    import org.springframework.http.ResponseEntity;
    import org.springframework.util.MultiValueMap;
    import org.springframework.web.bind.annotation.PostMapping;
    import org.springframework.web.bind.annotation.RequestBody;
    import org.springframework.web.bind.annotation.RestController;

    @RestController
    @SpringBootApplication
    public class DemoApplication {

        public static void main(String[] args) {
            SpringApplication.run(DemoApplication.class, args);
        }

        @PostMapping(value = "/delivery_report/")
        public ResponseEntity<String> deliveryReport(@RequestBody MultiValueMap<String, String> body) {
            System.out.println("--- Delivery Report Received ---");
            System.out.println(body);
            return ResponseEntity.ok("Report Received");
        }
    }
    ```

    ***

    ### Test

    1. Run your application.
    2. Expose your server to the internet using ngrok.

    **For Outbound Reports:**

    * Use this code to send a message. Replace placeholders and use your ngrok URL.

      ```java  theme={null}
      Plivo.init("<auth_id>", "<auth_token>");
      Message.creator(
              "<sender_id>",
              "<destination_number>",
              "Hello from Java!"
          )
          .url("https://<your-ngrok-url>.ngrok.io/delivery_report/")
          .create();
      ```
    * Check your console for delivery status logs.

    **For Inbound Reports:**

    * Create a Plivo Application with the `Message URL` set to `https://<your-ngrok-url>.ngrok.io/delivery_report/`.
    * Assign a Plivo number to it.
    * Send an SMS to your Plivo number and check your console.
  </Tab>

  <Tab title="Go">
    ## Overview

    This guide shows how to receive delivery reports for your SMS messages using Plivo's APIs and Go. Delivery reports are webhooks Plivo sends to your application to notify you of the status of inbound or outbound messages.

    ***

    ### How it works

    * **Outbound Messages**: When you send an SMS, include a `url` parameter. Plivo will POST the delivery status to this URL.
    * **Inbound Messages**: When you receive an SMS, Plivo sends the message details to your `Message URL`.

    Your Go application needs an HTTP handler to receive these POST requests, log the data, and return a `200 OK` response.

    ***

    ### Prerequisites

    * A Plivo account — [**sign up for free**](https://cx.plivo.com/signup).
    * An SMS-enabled Plivo phone number. You can [**rent a number**](/numbers/).
    * Go and ngrok. See our [**Go setup guide**](/sdk/server/set-up-go-dev-environment-api-messaging/).

    ***

    ### Create a server to receive delivery reports

    Create a file named `delivery_report.go` and paste this code into it.

    ```go  theme={null}
    package main

    import (
        "fmt"
        "net/http"
    )

    func deliveryReport(w http.ResponseWriter, r *http.Request) {
        r.ParseForm()
        fmt.Println("--- Delivery Report Received ---")
        for key, values := range r.Form {
            fmt.Printf("%s: %s\n", key, values[0])
        }
        w.WriteHeader(http.StatusNoContent) // Acknowledge receipt
    }

    func main() {
        http.HandleFunc("/delivery_report/", deliveryReport)
        http.ListenAndServe(":8080", nil)
    }
    ```

    ***

    ### Test

    1. Run your server: `go run delivery_report.go`.
    2. Expose your server to the internet using ngrok: `ngrok http 8080`.

    **For Outbound Reports:**

    * Use this code to send a message. Replace placeholders and use your ngrok URL.

      ```go  theme={null}
      client, _ := plivo.NewClient("<auth_id>", "<auth_token>", &plivo.ClientOptions{})
      client.Messages.Create(
          plivo.MessageCreateParams{
              Src:  "<sender_id>",
              Dst:  "<destination_number>",
              Text: "Hello from Go!",
              URL:  "https://<your-ngrok-url>.ngrok.io/delivery_report/",
          },
      )
      ```
    * Check your terminal for delivery status logs.

    **For Inbound Reports:**

    * Create a Plivo Application with the `Message URL` set to `https://<your-ngrok-url>.ngrok.io/delivery_report/`.
    * Assign a Plivo number to it.
    * Send an SMS to your Plivo number and check your terminal.
  </Tab>
</Tabs>
