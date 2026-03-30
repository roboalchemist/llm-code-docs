# Source: https://plivo.com/docs/messaging/use-cases/mms-autoresponder/mms-autoresponder.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Write an MMS Autoresponder

> Build an automated MMS reply system triggered by incoming messages

<Tabs>
  <Tab title="Node">
    ## Overview

    This guide shows how to write an MMS autoresponder using Plivo's APIs and Node.js. An autoresponder can provide instant, automated replies with media based on keywords in incoming messages.

    ***

    ### How it works

    When Plivo receives an MMS on your number, it sends an HTTP request (webhook) to your application's "Message URL." Your server can then use the REST API to trigger a new outbound MMS in response. Your server should also send a `200 OK` response to Plivo to acknowledge the incoming webhook.

    ***

    ### Prerequisites

    * A Plivo account — [**sign up for free**](https://cx.plivo.com/signup) if you don't have one.
    * An MMS-enabled Plivo phone number. You can [**rent a number**](/numbers/) from the Plivo console.
    * Node.js and the Plivo Node.js SDK installed. See our [**Node.js setup guide**](/sdk/server/set-up-node-dev-environment-api-messaging/).

    ***

    ### Create the autoresponder application

    Create a file called `mms_autoresponder.js` and paste this code into it. This server listens for incoming messages, checks for keywords like "hi" or "bye," and sends back an MMS with text and a GIF.

    ```js  theme={null}
    const express = require('express');
    const bodyParser = require('body-parser');
    const plivo = require('plivo');

    const app = express();
    app.use(bodyParser.urlencoded({ extended: true }));

    app.all('/autoresponder/', async (request, response) => {
        const from_number = request.body.From;
        const to_number = request.body.To;
        const text = request.body.Text;

        console.log(`Message received - From: ${from_number}, To: ${to_number}, Text: ${text}`);

        let reply_text;
        let media_urls;

        if (text && text.toLowerCase() === 'hi') {
            reply_text = "Hello!";
            media_urls = ["[https://media.giphy.com/media/888R35MJTmDxQfRzfS/giphy.gif](https://media.giphy.com/media/888R35MJTmDxQfRzfS/giphy.gif)"];
        } else if (text && text.toLowerCase() === 'bye') {
            reply_text = "Bye and have a nice day!";
            media_urls = ["[https://media.giphy.com/media/QM5lHSyFjz1XW/giphy.gif](https://media.giphy.com/media/QM5lHSyFjz1XW/giphy.gif)"];
        } else {
            reply_text = "I'm glad that we connected";
            media_urls = ["[https://media.giphy.com/media/888R35MJTmDxQfRzfS/giphy.gif](https://media.giphy.com/media/888R35MJTmDxQfRzfS/giphy.gif)"];
        }

        // Acknowledge the webhook from Plivo
        response.status(204).send();

        // Send the MMS reply using the REST API
        const client = new plivo.Client("<auth_id>", "<auth_token>");
        try {
            const msgResponse = await client.messages.create({
                src: to_number,   // The Plivo number
                dst: from_number, // The original sender's number
                text: reply_text,
                type: "mms",
                media_urls: media_urls
            });
            console.log("MMS reply sent:", msgResponse);
        } catch (error) {
            console.error("Error sending MMS:", error);
        }
    });

    app.listen(3000, () => {
        console.log('Node app is running on port 3000');
    });
    ```

    ***

    ### Create and configure a Plivo application

    1. **Create an Application**: Go to Messaging > [Applications](https://cx.plivo.com/xml-applications) and click **Add New Application**.
    2. **Configure the URL**: Name the application (e.g., `MMS Autoresponder`). In the `Message URL` field, enter your server URL (e.g., `https://<yourdomain>.com/autoresponder/`) and set the method to `POST`. Click **Create Application**.
    3. **Assign a Number**: Go to the [Numbers](https://cx.plivo.com/phone-numbers) page, select your number, and link it to the `MMS Autoresponder` application.

    ***

    ### Test it out

    Send an MMS with the text "hi" or "bye" to your Plivo number to see the different GIF responses.
  </Tab>

  <Tab title="Python">
    ## Overview

    This guide shows how to write an MMS autoresponder using Plivo's APIs and Python with Flask. An autoresponder can provide instant, automated replies with media based on keywords in incoming messages.

    ***

    ### How it works

    When Plivo receives an MMS on your number, it sends an HTTP request (webhook) to your application's "Message URL." Your server can then use the REST API to trigger a new outbound MMS in response. Your server should also send a `200 OK` response to Plivo to acknowledge the incoming webhook.

    ***

    ### Prerequisites

    * A Plivo account — [**sign up for free**](https://cx.plivo.com/signup) if you don't have one.
    * An MMS-enabled Plivo phone number. You can [**rent a number**](/numbers/) from the Plivo console.
    * Python and the Plivo Python SDK installed. See our [**Python setup guide**](/sdk/server/set-up-python-dev-environment-api-messaging/).

    ***

    ### Create the autoresponder application

    Create a file called `mms_autoresponder.py` and paste into it this code. This server listens for incoming messages, checks for keywords, and sends back an MMS with text and a GIF.

    ```py  theme={null}
    from flask import Flask, request
    import plivo

    app = Flask(__name__)

    @app.route("/autoresponder/", methods=["POST"])
    def autoresponder():
        from_number = request.values.get("From")
        to_number = request.values.get("To")
        text = request.values.get("Text")

        print(f"MMS message received - From: {from_number}, To: {to_number}, Text: {text}")

        reply_text = ""
        media_urls = []

        if text and text.lower() == "hi":
            reply_text = "Hello!"
            media_urls = ["[https://media.giphy.com/media/888R35MJTmDxQfRzfS/giphy.gif](https://media.giphy.com/media/888R35MJTmDxQfRzfS/giphy.gif)"]
        elif text and text.lower() == "bye":
            reply_text = "Bye and have a nice day!"
            media_urls = ["[https://media.giphy.com/media/QM5lHSyFjz1XW/giphy.gif](https://media.giphy.com/media/QM5lHSyFjz1XW/giphy.gif)"]
        else:
            reply_text = "I'm glad that we connected"
            media_urls = ["[https://media.giphy.com/media/888R35MJTmDxQfRzfS/giphy.gif](https://media.giphy.com/media/888R35MJTmDxQfRzfS/giphy.gif)"]

        client = plivo.RestClient("<auth_id>", "<auth_token>")
        try:
            response = client.messages.create(
                src=to_number,
                dst=from_number,
                text=reply_text,
                media_urls=media_urls,
                type="mms"
            )
            print(response)
        except plivo.exceptions.PlivoRestError as e:
            print(e)

        return "MMS auto-reply sent", 200

    if __name__ == "__main__":
        app.run(host="0.0.0.0")
    ```

    ***

    ### Create and configure a Plivo application

    1. **Create an Application**: Go to Messaging > [Applications](https://cx.plivo.com/xml-applications) and click **Add New Application**.
    2. **Configure the URL**: Name the application (e.g., `MMS Autoresponder`). In the `Message URL` field, enter your server URL (e.g., `https://<yourdomain>.com/autoresponder/`) and set the method to `POST`. Click **Create Application**.
    3. **Assign a Number**: Go to the [Numbers](https://cx.plivo.com/phone-numbers) page, select your number, and link it to the `MMS Autoresponder` application.

    ***

    ### Test it out

    Send an MMS with the text "hi" or "bye" to your Plivo number to see the different GIF responses.
  </Tab>

  <Tab title="PHP">
    ## Overview

    This guide shows how to write an MMS autoresponder using Plivo's APIs and PHP. An autoresponder can provide instant, automated replies with media based on keywords in incoming messages.

    ***

    ### How it works

    When Plivo receives an MMS on your number, it sends an HTTP request (webhook) to your application's "Message URL." Your server can then use the REST API to trigger a new outbound MMS in response. Your server should also send a `200 OK` response to Plivo to acknowledge the incoming webhook.

    ***

    ### Prerequisites

    * A Plivo account — [**sign up for free**](https://cx.plivo.com/signup) if you don't have one.
    * An MMS-enabled Plivo phone number. You can [**rent a number**](/numbers/) from the Plivo console.
    * PHP and the Plivo PHP SDK installed. See our [**PHP setup guide**](/sdk/server/set-up-php-dev-environment-api-messaging/).

    ***

    ### Create the autoresponder application

    Paste this code into your controller. This script listens for incoming messages, checks for keywords, and sends back an MMS with text and a GIF.

    ```php  theme={null}
    <?php
    namespace App\Http\Controllers;

    use Illuminate\Http\Request;
    use Plivo\RestClient;
    use Plivo\Exceptions\PlivoRestError;

    class SMSController extends Controller
    {
        public function autoresponder()
        {
            $from_number = $_POST["From"];
            $to_number = $_POST["To"];
            $text = $_POST["Text"];

            $reply_text = '';
            $media_urls = [];

            if ($text && strtolower($text) == "hi") {
                $reply_text = "Hello!";
                $media_urls = ["[https://media.giphy.com/media/888R35MJTmDxQfRzfS/giphy.gif](https://media.giphy.com/media/888R35MJTmDxQfRzfS/giphy.gif)"];
            } else if ($text && strtolower($text) == "bye") {
                $reply_text = "Bye and have a nice day!";
                $media_urls = ["[https://media.giphy.com/media/QM5lHSyFjz1XW/giphy.gif](https://media.giphy.com/media/QM5lHSyFjz1XW/giphy.gif)"];
            } else {
                $reply_text = "I'm glad that we connected";
                $media_urls = ["[https://media.giphy.com/media/888R35MJTmDxQfRzfS/giphy.gif](https://media.giphy.com/media/888R35MJTmDxQfRzfS/giphy.gif)"];
            }

            try {
                $client = new RestClient("<auth_id>", "<auth_token>");
                $client->messages->create([
                    "src" => $to_number,
                    "dst" => $from_number,
                    "text" => $reply_text,
                    "type" => "mms",
                    "media_urls" => $media_urls
                ]);
            } catch (PlivoRestError $e) {
                error_log("Error: " . $e->getMessage());
            }

            // Acknowledge the webhook
            http_response_code(204);
        }
    }
    ```

    ***

    ### Create and configure a Plivo application

    1. **Create an Application**: Go to Messaging > [Applications](https://cx.plivo.com/xml-applications) and click **Add New Application**.
    2. **Configure the URL**: Name the application (e.g., `MMS Autoresponder`). In the `Message URL` field, enter your server URL (e.g., `https://<yourdomain>.com/autoresponder/`) and set the method to `POST`. Click **Create Application**.
    3. **Assign a Number**: Go to the [Numbers](https://cx.plivo.com/phone-numbers) page, select your number, and link it to the `MMS Autoresponder` application.

    ***

    ### Test it out

    Send an MMS with the text "hi" or "bye" to your Plivo number to see the different GIF responses.
  </Tab>

  <Tab title=".NET">
    ## Overview

    This guide shows how to write an MMS autoresponder using Plivo's APIs and .NET. An autoresponder can provide instant, automated replies with media based on keywords in incoming messages.

    ***

    ### How it works

    When Plivo receives an MMS on your number, it sends an HTTP request (webhook) to your application's "Message URL." Your server can then use the REST API to trigger a new outbound MMS in response. Your server should also send a `200 OK` response to Plivo to acknowledge the incoming webhook.

    ***

    ### Prerequisites

    * A Plivo account — [**sign up for free**](https://cx.plivo.com/signup) if you don't have one.
    * An MMS-enabled Plivo phone number. You can [**rent a number**](/numbers/) from the Plivo console.
    * .NET and the Plivo .NET SDK installed. See our [**.NET setup guide**](/sdk/server/set-up-dotnet-dev-environment-api-messaging/).

    ***

    ### Create the autoresponder application

    In your controller, paste this code. This action listens for incoming messages, checks for keywords, and sends back an MMS with text and a GIF.

    ```csharp  theme={null}
    using System;
    using Plivo;
    using Microsoft.AspNetCore.Mvc;

    namespace Demo.Controllers
    {
        public class Autoresponder : Controller
        {
            [HttpPost]
            public IActionResult Index()
            {
                string from_number = Request.Form["From"];
                string to_number = Request.Form["To"];
                string text = Request.Form["Text"];

                string reply_text;
                string media_url;

                if (text != null && text.ToLower() == "hi")
                {
                    reply_text = "Hello!";
                    media_url = "[https://media.giphy.com/media/888R35MJTmDxQfRzfS/giphy.gif](https://media.giphy.com/media/888R35MJTmDxQfRzfS/giphy.gif)";
                }
                else if (text != null && text.ToLower() == "bye")
                {
                    reply_text = "Bye and have a nice day!";
                    media_url = "[https://media.giphy.com/media/QM5lHSyFjz1XW/giphy.gif](https://media.giphy.com/media/QM5lHSyFjz1XW/giphy.gif)";
                }
                else
                {
                    reply_text = "I'm glad that we connected";
                    media_url = "[https://media.giphy.com/media/888R35MJTmDxQfRzfS/giphy.gif](https://media.giphy.com/media/888R35MJTmDxQfRzfS/giphy.gif)";
                }

                var api = new PlivoApi("<auth_id>", "<auth_token>");
                try {
                    var response = api.Message.Create(
                        src: to_number,
                        dst: from_number,
                        text: reply_text,
                        type: "mms",
                        mediaUrls: new string[] { media_url }
                    );
                    Console.WriteLine(response);
                } catch (Plivo.PlivoRestException e) {
                    Console.WriteLine("Error: " + e.Message);
                }

                return Content("MMS auto-reply sent.");
            }
        }
    }
    ```

    ***

    ### Create and configure a Plivo application

    1. **Create an Application**: Go to Messaging > [Applications](https://cx.plivo.com/xml-applications) and click **Add New Application**.
    2. **Configure the URL**: Name the application (e.g., `MMS Autoresponder`). In the `Message URL` field, enter your server URL (e.g., `https://<yourdomain>.com/autoresponder/`) and set the method to `POST`. Click **Create Application**.
    3. **Assign a Number**: Go to the [Numbers](https://cx.plivo.com/phone-numbers) page, select your number, and link it to the `MMS Autoresponder` application.

    ***

    ### Test it out

    Send an MMS with the text "hi" or "bye" to your Plivo number to see the different GIF responses.
  </Tab>

  <Tab title="Java">
    ## Overview

    This guide shows how to write an MMS autoresponder using Plivo's APIs and Java with Spring. An autoresponder can provide instant, automated replies with media based on keywords in incoming messages.

    ***

    ### How it works

    When Plivo receives an MMS on your number, it sends an HTTP request (webhook) to your application's "Message URL." Your server can then use the REST API to trigger a new outbound MMS in response. Your server should also send a `200 OK` response to Plivo to acknowledge the incoming webhook.

    ***

    ### Prerequisites

    * A Plivo account — [**sign up for free**](https://cx.plivo.com/signup) if you don't have one.
    * An MMS-enabled Plivo phone number. You can [**rent a number**](/numbers/) from the Plivo console.
    * Java and the Plivo Java SDK installed. See our [**Java setup guide**](/sdk/server/set-up-java-dev-environment-api-messaging/).

    ***

    ### Create the autoresponder application

    In your main application file, paste this code. This controller listens for incoming messages, checks for keywords, and sends back an MMS with text and a GIF.

    ```java  theme={null}
    package com.example.demo;

    import com.plivo.api.Plivo;
    import com.plivo.api.exceptions.PlivoRestException;
    import com.plivo.api.models.message.Message;
    import com.plivo.api.models.message.MessageCreateResponse;
    import com.plivo.api.models.message.MessageType;
    import org.springframework.boot.SpringApplication;
    import org.springframework.boot.autoconfigure.SpringBootApplication;
    import org.springframework.http.ResponseEntity;
    import org.springframework.web.bind.annotation.PostMapping;
    import org.springframework.web.bind.annotation.RestController;
    import java.io.IOException;

    @RestController
    @SpringBootApplication
    public class DemoApplication {

        public static void main(String[] args) {
            SpringApplication.run(DemoApplication.class, args);
        }

        @PostMapping(value = "/autoresponder/")
        public ResponseEntity<String> autoresponder(String From, String To, String Text) {
            String reply_text;
            String media_url;

            if (Text != null && Text.toLowerCase().equals("hi")) {
                reply_text = "Hello!";
                media_url = "[https://media.giphy.com/media/888R35MJTmDxQfRzfS/giphy.gif](https://media.giphy.com/media/888R35MJTmDxQfRzfS/giphy.gif)";
            } else if (Text != null && Text.toLowerCase().equals("bye")) {
                reply_text = "Bye and have a nice day!";
                media_url = "[https://media.giphy.com/media/QM5lHSyFjz1XW/giphy.gif](https://media.giphy.com/media/QM5lHSyFjz1XW/giphy.gif)";
            } else {
                reply_text = "I'm glad that we connected";
                media_url = "[https://media.giphy.com/media/888R35MJTmDxQfRzfS/giphy.gif](https://media.giphy.com/media/888R35MJTmDxQfRzfS/giphy.gif)";
            }

            Plivo.init("<auth_id>", "<auth_token>");
            try {
                Message.creator(To, From, reply_text)
                    .type(MessageType.MMS)
                    .mediaUrls(new String[]{media_url})
                    .create();
            } catch (PlivoRestException | IOException e) {
                e.printStackTrace();
            }

            return ResponseEntity.noContent().build();
        }
    }
    ```

    ***

    ### Create and configure a Plivo application

    1. **Create an Application**: Go to Messaging > [Applications](https://cx.plivo.com/xml-applications) and click **Add New Application**.
    2. **Configure the URL**: Name the application (e.g., `MMS Autoresponder`). In the `Message URL` field, enter your server URL (e.g., `https://<yourdomain>.com/autoresponder/`) and set the method to `POST`. Click **Create Application**.
    3. **Assign a Number**: Go to the [Numbers](https://cx.plivo.com/phone-numbers) page, select your number, and link it to the `MMS Autoresponder` application.

    ***

    ### Test it out

    Send an MMS with the text "hi" or "bye" to your Plivo number to see the different GIF responses.
  </Tab>

  <Tab title="Go">
    ## Overview

    This guide shows how to write an MMS autoresponder using Plivo's APIs and Go. An autoresponder can provide instant, automated replies with media based on keywords in incoming messages.

    ***

    ### How it works

    When Plivo receives an MMS on your number, it sends an HTTP request (webhook) to your application's "Message URL." Your server can then use the REST API to trigger a new outbound MMS in response. Your server should also send a `200 OK` response to Plivo to acknowledge the incoming webhook.

    ***

    ### Prerequisites

    * A Plivo account — [**sign up for free**](https://cx.plivo.com/signup) if you don't have one.
    * An MMS-enabled Plivo phone number. You can [**rent a number**](/numbers/) from the Plivo console.
    * Go and the Plivo Go SDK installed. See our [**Go setup guide**](/sdk/server/set-up-go-dev-environment-api-messaging/).

    ***

    ### Create the autoresponder application

    Create a file called `mms_autoresponder.go` and paste into it this code. This server listens for incoming messages, checks for keywords, and sends back an MMS with text and a GIF.

    ```go  theme={null}
    package main

    import (
        "fmt"
        "net/http"
        "strings"
        "[github.com/plivo/plivo-go/v7](https://github.com/plivo/plivo-go/v7)"
    )

    func autoresponder(w http.ResponseWriter, r *http.Request) {
        from_number := r.FormValue("From")
        to_number := r.FormValue("To")
        text := r.FormValue("Text")

        var reply_text string
        var media_url string

        if strings.ToLower(text) == "hi" {
            reply_text = "Hello!"
            media_url = "[https://media.giphy.com/media/888R35MJTmDxQfRzfS/giphy.gif](https://media.giphy.com/media/888R35MJTmDxQfRzfS/giphy.gif)"
        } else if strings.ToLower(text) == "bye" {
            reply_text = "Bye and have a nice day!"
            media_url = "[https://media.giphy.com/media/QM5lHSyFjz1XW/giphy.gif](https://media.giphy.com/media/QM5lHSyFjz1XW/giphy.gif)"
        } else {
            reply_text = "I'm glad that we connected"
            media_url = "[https://media.giphy.com/media/888R35MJTmDxQfRzfS/giphy.gif](https://media.giphy.com/media/888R35MJTmDxQfRzfS/giphy.gif)"
        }

        // Acknowledge the webhook immediately
        w.WriteHeader(http.StatusNoContent)

        // Send the MMS reply in the background
        go func() {
            client, err := plivo.NewClient("<auth_id>", "<auth_token>", &plivo.ClientOptions{})
            if err != nil {
                fmt.Println("Error creating client:", err)
                return
            }
            _, err = client.Messages.Create(plivo.MessageCreateParams{
                Src:       to_number,
                Dst:       from_number,
                Text:      reply_text,
                Type:      "mms",
                MediaUrls: []string{media_url},
            })
            if err != nil {
                fmt.Println("Error sending MMS:", err)
            }
        }()
    }

    func main() {
        http.HandleFunc("/autoresponder/", autoresponder)
        http.ListenAndServe(":8080", nil)
    }
    ```

    ***

    ### Create and configure a Plivo application

    1. **Create an Application**: Go to Messaging > [Applications](https://cx.plivo.com/xml-applications) and click **Add New Application**.
    2. **Configure the URL**: Name the application (e.g., `MMS Autoresponder`). In the `Message URL` field, enter your server URL (e.g., `https://<yourdomain>.com/autoresponder/`) and set the method to `POST`. Click **Create Application**.
    3. **Assign a Number**: Go to the [Numbers](https://cx.plivo.com/phone-numbers) page, select your number, and link it to the `MMS Autoresponder` application.

    ***

    ### Test it out

    Send an MMS with the text "hi" or "bye" to your Plivo number to see the different GIF responses.
  </Tab>
</Tabs>
