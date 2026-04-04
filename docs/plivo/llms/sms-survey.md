# Source: https://plivo.com/docs/messaging/use-cases/sms-survey/sms-survey.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Conduct SMS Survey

> Conduct interactive SMS surveys to collect customer feedback

<Tabs>
  <Tab title="Node">
    ## Overview

    This guide shows how to conduct an SMS survey using Plivo's APIs and Node.js. This involves two parts: sending an initial question via the REST API, and then handling the user's reply via a webhook.

    ***

    ### How it works

    1. **Initiate Survey**: Your application makes a POST request to a `/send-survey/` endpoint. This triggers Plivo's Send Message API to send the first survey question to the user.
    2. **Handle Response**: The user replies to the SMS. Plivo sends a webhook with their reply to a `/survey-response/` endpoint. Your application processes their answer ("Yes" or "No") and replies with a thank-you message using Plivo XML.

    ***

    ### Prerequisites

    * A Plivo account — [**sign up for free**](https://cx.plivo.com/signup).
    * An SMS-enabled Plivo phone number. You can [**rent a number**](/numbers/).
    * Node.js and ngrok. See our [**Node.js setup guide**](/sdk/server/set-up-node-dev-environment-api-messaging/).

    ***

    ### Create the survey application

    Create a file named `survey.js` and paste in this code. It sets up an Express server with two endpoints: one to start the survey and one to handle replies.

    ```js  theme={null}
    const express = require('express');
    const plivo = require('plivo');
    const app = express();
    const port = 3000;

    app.use(express.json());
    app.use(express.urlencoded({ extended: true }));

    // This endpoint triggers the initial survey question via the REST API
    app.post('/send-survey/', async (req, res) => {
        const client = new plivo.Client('<auth_id>', '<auth_token>');
        try {
            const response = await client.messages.create({
                src: '<sender_id>',
                dst: '<destination_number>',
                text: 'Did you find out all the information you needed? Please reply "Yes" or "No"'
            });
            res.status(200).send(response);
        } catch (error) {
            console.error(error);
            res.status(500).send(error);
        }
    });

    // This endpoint handles the user's reply via a webhook
    app.post('/survey-response/', (req, res) => {
        const from_number = req.body.From;
        const to_number = req.body.To;
        const text = req.body.Text;
        console.log(`Message received - From: ${from_number}, To: ${to_number}, Text: ${text}`);

        let message_body;
        if (text && text.toLowerCase() === "yes") {
            message_body = "Thank you for your feedback";
        } else if (text && text.toLowerCase() === "no") {
            message_body = "We apologize for the inconvenience. A representative will contact you to assist you";
        } else {
            message_body = `Response received was "${text}", which is invalid. Please reply with either "Yes" or "No"`;
        }

        const plivoxml = plivo.Response();
        const params = { 'src': to_number, 'dst': from_number };
        plivoxml.addMessage(message_body, params);

        res.type('application/xml');
        res.status(200).send(plivoxml.toXML());
    });

    app.listen(port, () => {
        console.log(`SMS survey app listening on port ${port}`);
    });
    ```

    ***

    ### Test

    1. Run the application: `node survey.js`.
    2. Expose your local server to the internet using ngrok: `ngrok http 3000`.
    3. Create a Plivo Application with the Message URL set to `https://<your-ngrok-url>.ngrok.io/survey-response/`.
    4. Assign a Plivo number to the application.
    5. Use a tool like Postman to send a POST request to `http://localhost:3000/send-survey/` to start the survey.
    6. Reply "Yes" or "No" from the destination phone to see the auto-response.
  </Tab>

  <Tab title="Ruby">
    ## Overview

    This guide shows how to conduct an SMS survey using Plivo's APIs and Ruby on Rails. This involves two parts: sending an initial question via the REST API, and then handling the user's reply via a webhook.

    ***

    ### How it works

    1. **Initiate Survey**: Your application receives a POST request at a `/send-survey/` route. This triggers Plivo's Send Message API to send the first survey question to the user.
    2. **Handle Response**: The user replies to the SMS. Plivo sends a webhook with their reply to a `/survey-response/` route. Your application processes their answer ("Yes" or "No") and replies with a thank-you message using Plivo XML.

    ***

    ### Prerequisites

    * A Plivo account — [**sign up for free**](https://cx.plivo.com/signup).
    * An SMS-enabled Plivo phone number. You can [**rent a number**](/numbers/).
    * Ruby on Rails and ngrok. See our [**Ruby setup guide**](/sdk/server/set-up-ruby-dev-environment-api-messaging/).

    ***

    ### Create the survey application

    In `app/controllers/plivo_controller.rb`, paste this code. It defines two actions: one to start the survey and one to handle replies.

    ```rb  theme={null}
    include Plivo
    include Plivo::Exceptions
    include Plivo::XML

    class PlivoController < ApplicationController
        skip_before_action :verify_authenticity_token

        def send_survey
            api = RestClient.new("<auth_id>", "<auth_token>")
            begin
                response = api.messages.create(
                    src: '<sender_id>',
                    dst: '<destination_number>',
                    text: 'Did you find out all the information you needed? Please reply "Yes" or "No"'
                )
                render json: response
            rescue PlivoRESTError => e
                render json: { error: e.message }, status: :internal_server_error
            end
        end

        def survey_response
            from_number = params[:From]
            to_number = params[:To]
            text = params[:Text]

            if text&.downcase == "yes"
                message_body = "Thank you for your feedback"
            elsif text&.downcase == "no"
                message_body = "We apologize for the inconvenience. A representative will contact you to assist you"
            else
                message_body = "Response received was \"#{text}\", which is invalid. Please reply with either Yes or No"
            end

            response = Response.new
            params = { src: to_number, dst: from_number }
            response.addMessage(message_body, params)
            xml = PlivoXML.new(response)

            render xml: xml.to_xml
        end
    end
    ```

    In `config/routes.rb`, define the routes for these actions:

    ```ruby  theme={null}
    Rails.application.routes.draw do
      post 'plivo/send_survey' => 'plivo#send_survey'
      post 'plivo/survey_response' => 'plivo#survey_response'
    end
    ```

    ***

    ### Test

    1. Run the application: `rails server`.
    2. Expose your local server to the internet using ngrok: `ngrok http 3000`.
    3. Create a Plivo Application with the Message URL set to `https://<your-ngrok-url>.ngrok.io/plivo/survey_response`.
    4. Assign a Plivo number to the application.
    5. Use a tool like Postman to send a POST request to `http://localhost:3000/plivo/send_survey` to start the survey.
    6. Reply "Yes" or "No" from the destination phone to see the auto-response.
  </Tab>

  <Tab title="Python">
    ## Overview

    This guide shows how to conduct an SMS survey using Plivo's APIs and Python with Flask. This involves two parts: sending an initial question via the REST API, and then handling the user's reply via a webhook.

    ***

    ### How it works

    1. **Initiate Survey**: Your application receives a POST request at a `/send-survey/` endpoint. This triggers Plivo's Send Message API to send the first survey question to the user.
    2. **Handle Response**: The user replies to the SMS. Plivo sends a webhook with their reply to a `/survey-response/` endpoint. Your application processes their answer ("Yes" or "No") and replies with a thank-you message using Plivo XML.

    ***

    ### Prerequisites

    * A Plivo account — [**sign up for free**](https://cx.plivo.com/signup).
    * An SMS-enabled Plivo phone number. You can [**rent a number**](/numbers/).
    * Python and ngrok. See our [**Python setup guide**](/sdk/server/set-up-python-dev-environment-api-messaging/).

    ***

    ### Create the survey application

    Create a file called `survey.py` and paste into it this code.

    ```py  theme={null}
    from flask import Flask, request, Response, jsonify
    import plivo
    from plivo import plivoxml

    app = Flask(__name__)

    @app.post("/send-survey/")
    def send_survey():
        try:
            client = plivo.RestClient("<auth_id>", "<auth_token>")
            response = client.messages.create(
                src="<sender_id>",
                dst="<destination_number>",
                text='Did you find out all the information you needed? Please reply "Yes" or "No"',
            )
            return jsonify(response.to_dict()), 200
        except plivo.exceptions.PlivoRestError as e:
            return jsonify({"error": str(e)}), 500

    @app.post("/survey-response/")
    def survey_response():
        from_number = request.values.get("From")
        to_number = request.values.get("To")
        text = request.values.get("Text")

        if text and text.lower() == "yes":
            message_body = "Thank you for your feedback"
        elif text and text.lower() == "no":
            message_body = "We apologize for the inconvenience. A representative will contact you to assist you"
        else:
            message_body = f'Response received was "{text}", which is invalid. Please reply with either "Yes" or "No"'

        response = plivoxml.ResponseElement()
        response.add(plivoxml.MessageElement(message_body, src=to_number, dst=from_number))
        return Response(response.to_string(), mimetype="application/xml")

    if __name__ == "__main__":
        app.run(host="0.0.0.0", debug=True)
    ```

    ***

    ### Test

    1. Run the application: `python survey.py`.
    2. Expose your local server to the internet using ngrok: `ngrok http 5000`.
    3. Create a Plivo Application with the Message URL set to `https://<your-ngrok-url>.ngrok.io/survey-response/`.
    4. Assign a Plivo number to the application.
    5. Use a tool like Postman to send a POST request to `http://localhost:5000/send-survey/` to start the survey.
    6. Reply "Yes" or "No" from the destination phone to see the auto-response.
  </Tab>

  <Tab title="PHP">
    ## Overview

    This guide shows how to initiate an SMS survey using Plivo's APIs and PHP. This code covers sending the initial question.

    > **Note:** This example is incomplete. It only covers the first step of sending the survey question. You would need to build a second endpoint to receive and process the user's reply, similar to the other language examples on this page.

    ***

    ### Prerequisites

    * A Plivo account — [**sign up for free**](https://cx.plivo.com/signup).
    * An SMS-enabled Plivo phone number. You can [**rent a number**](/numbers/).
    * PHP, Composer, and ngrok. See our [**PHP setup guide**](/sdk/server/set-up-php-dev-environment-api-messaging/).

    ***

    ### Create the survey application

    Create a file called `send_survey.php` and paste this code into it.

    ```php  theme={null}
    <?php
    require 'vendor/autoload.php';
    use Plivo\RestClient;
    use Plivo\Exceptions\PlivoRestError;

    try {
        $client = new RestClient("<auth_id>", "<auth_token>");
        $response = $client->messages->create([
            "src" => "<sender_id>",
            "dst" => "<destination_number>",
            "text" => "Did you find out all the information you needed? Please reply \"Yes\" or \"No\""
        ]);
        print_r($response);
    } catch (PlivoRestError $e) {
        echo "Error: " . $e->getMessage();
    }
    ?>
    ```

    ***

    ### Test

    Save the file and run it from your terminal to send the initial survey question.

    ```shell  theme={null}
    php send_survey.php
    ```
  </Tab>

  <Tab title=".NET">
    ## Overview

    This guide shows how to conduct an SMS survey using Plivo's APIs and .NET. This involves two parts: sending an initial question via the REST API, and then handling the user's reply via a webhook.

    ***

    ### How it works

    1. **Initiate Survey**: Your application receives a request at a `/Survey/Send` route. This triggers Plivo's Send Message API to send the first survey question.
    2. **Handle Response**: The user replies. Plivo sends a webhook to a `/Survey/Response` route. Your application processes their answer and replies with a thank-you message using Plivo XML.

    ***

    ### Prerequisites

    * A Plivo account — [**sign up for free**](https://cx.plivo.com/signup).
    * An SMS-enabled Plivo phone number. You can [**rent a number**](/numbers/).
    * .NET and ngrok. See our [**.NET setup guide**](/sdk/server/set-up-dotnet-dev-environment-api-messaging/).

    ***

    ### Create the survey application

    In `Controllers/SurveyController.cs`, paste this code. It defines two actions: one to start the survey and one to handle replies.

    ```csharp  theme={null}
    using System;
    using Plivo;
    using System.Collections.Generic;
    using Microsoft.AspNetCore.Mvc;

    namespace Demo.Controllers
    {
        public class Survey : Controller
        {
            [HttpPost]
            public IActionResult Send()
            {
                var api = new PlivoApi("<auth_id>", "<auth_token>");
                try {
                    var response = api.Message.Create(
                        src: "<sender_id>",
                        dst: new List<string> { "<destination_number>" },
                        text: "Did you find out all the information you needed? Please reply 'Yes' or 'No'"
                    );
                    return Content(response.ToString());
                } catch (Plivo.PlivoRestException e) {
                    return Content("Error: " + e.Message);
                }
            }

            [HttpPost]
            public IActionResult Response()
            {
                string from_number = Request.Form["From"];
                string to_number = Request.Form["To"];
                string text = Request.Form["Text"];
                string body;

                if (text != null && text.ToLower() == "yes")
                {
                    body = "Thank you for your feedback";
                }
                else if (text != null && text.ToLower() == "no")
                {
                    body = "We apologize for the inconvenience. A representative will contact you to assist you";
                }
                else
                {
                    body = $"Response received was '{text}', which is invalid. Please reply with either 'Yes' or 'No'";
                }

                var resp = new Plivo.XML.Response();
                resp.AddMessage(body, new Dictionary<string, string>()
                {
                    {"src", to_number},
                    {"dst", from_number}
                });

                return Content(resp.ToString(), "text/xml");
            }
        }
    }
    ```

    ***

    ### Test

    1. Run the application.
    2. Expose your local server to the internet using ngrok.
    3. Create a Plivo Application with the Message URL set to `https://<your-ngrok-url>.ngrok.io/Survey/Response`.
    4. Assign a Plivo number to the application.
    5. Use a tool like Postman to send a POST request to `https://<your-ngrok-url>.ngrok.io/Survey/Send` to start the survey.
    6. Reply "Yes" or "No" from the destination phone.
  </Tab>

  <Tab title="Java">
    ## Overview

    This guide shows how to conduct an SMS survey using Plivo's APIs and Java with Spring. This involves two parts: sending an initial question, and then handling the user's reply.

    ***

    ### How it works

    1. **Initiate Survey**: Your application receives a POST request at a `/send-survey/` endpoint. This triggers Plivo's Send Message API to send the first survey question.
    2. **Handle Response**: The user replies. Plivo sends a webhook to a `/survey-response/` endpoint. Your application processes their answer and replies with a thank-you message using Plivo XML.

    ***

    ### Prerequisites

    * A Plivo account — [**sign up for free**](https://cx.plivo.com/signup).
    * An SMS-enabled Plivo phone number. You can [**rent a number**](/numbers/).
    * Java and ngrok. See our [**Java setup guide**](/sdk/server/set-up-java-dev-environment-api-messaging/).

    ***

    ### Create the survey application

    In your main application file, paste this code. It defines two endpoints.

    ```java  theme={null}
    package com.example.demo;

    import com.plivo.api.Plivo;
    import com.plivo.api.exceptions.PlivoRestException;
    import com.plivo.api.exceptions.PlivoXmlException;
    import com.plivo.api.models.message.Message;
    import com.plivo.api.models.message.MessageCreateResponse;
    import com.plivo.api.xml.Response;
    import org.springframework.boot.SpringApplication;
    import org.springframework.boot.autoconfigure.SpringBootApplication;
    import org.springframework.http.MediaType;
    import org.springframework.http.ResponseEntity;
    import org.springframework.web.bind.annotation.PostMapping;
    import org.springframework.web.bind.annotation.RestController;
    import java.io.IOException;

    @SpringBootApplication
    @RestController
    public class SurveyApplication {

        public static void main(String[] args) {
            SpringApplication.run(SurveyApplication.class, args);
        }

        @PostMapping(value = "/send-survey/", produces = {MediaType.APPLICATION_JSON_VALUE})
        public ResponseEntity<MessageCreateResponse> sendSurvey() throws IOException, PlivoRestException {
            Plivo.init("<auth_id>", "<auth_token>");
            MessageCreateResponse response = Message.creator(
                    "<sender_id>",
                    "<destination_number>",
                    "Did you find out all the information you needed? Please reply \"Yes\" or \"No\"").create();
            return ResponseEntity.ok(response);
        }

        @PostMapping(value = "/survey-response/", produces = {MediaType.APPLICATION_XML_VALUE})
        public String handleSurveyResponse(String From, String To, String Text) throws PlivoXmlException {
            String message_body;
            if (Text != null && Text.toLowerCase().equals("yes")) {
                message_body = "Thank you for your feedback";
            } else if (Text != null && Text.toLowerCase().equals("no")) {
                message_body = "We apologize for the inconvenience. A representative will contact you to assist you";
            } else {
                message_body = String.format("Response received was %s, which is invalid. Please reply with either \"Yes\" or \"No\"", Text);
            }

            Response response = new Response().children(
                    new com.plivo.api.xml.Message(message_body, To, From));
            return response.toXmlString();
        }
    }
    ```

    ***

    ### Test

    1. Run the application.
    2. Expose your local server to the internet using ngrok.
    3. Create a Plivo Application with the Message URL set to `https://<your-ngrok-url>.ngrok.io/survey-response/`.
    4. Assign a Plivo number to the application.
    5. Use a tool like Postman to send a POST request to `http://localhost:8080/send-survey/` to start the survey.
    6. Reply "Yes" or "No" from the destination phone.
  </Tab>

  <Tab title="Go">
    ## Overview

    This guide shows how to conduct an SMS survey using Plivo's APIs and Go. This involves two parts: sending an initial question via the REST API, and then handling the user's reply via a webhook.

    ***

    ### How it works

    1. **Initiate Survey**: Your application receives a POST request at a `/send-survey/` endpoint. This triggers Plivo's Send Message API to send the first survey question.
    2. **Handle Response**: The user replies. Plivo sends a webhook to a `/survey-response/` endpoint. Your application processes their answer and replies with a thank-you message using Plivo XML.

    ***

    ### Prerequisites

    * A Plivo account — [**sign up for free**](https://cx.plivo.com/signup).
    * An SMS-enabled Plivo phone number. You can [**rent a number**](/numbers/).
    * Go and ngrok. See our [**Go setup guide**](/sdk/server/set-up-go-dev-environment-api-messaging/).

    ***

    ### Create the survey application

    Create a file called `survey.go` and paste this code into it.

    ```go  theme={null}
    package main

    import (
        "encoding/json"
        "fmt"
        "net/http"
        "strings"
        "[github.com/plivo/plivo-go/v7](https://github.com/plivo/plivo-go/v7)"
        "[github.com/plivo/plivo-go/v7/xml](https://github.com/plivo/plivo-go/v7/xml)"
    )

    func sendSurvey(w http.ResponseWriter, r *http.Request) {
        client, err := plivo.NewClient("<auth_id>", "<auth_token>", &plivo.ClientOptions{})
        if err != nil {
            http.Error(w, err.Error(), http.StatusInternalServerError)
            return
        }
        response, err := client.Messages.Create(
            plivo.MessageCreateParams{
                Src:  "<sender_id>",
                Dst:  "<destination_number>",
                Text: "Did you find out all the information you needed? Please reply 'Yes' or 'No'",
            },
        )
        if err != nil {
            http.Error(w, err.Error(), http.StatusInternalServerError)
            return
        }

        w.Header().Set("Content-Type", "application/json")
        json.NewEncoder(w).Encode(response)
    }

    func surveyResponse(w http.ResponseWriter, r *http.Request) {
        from_number := r.FormValue("From")
        to_number := r.FormValue("To")
        text := r.FormValue("Text")
        var message_body string

        if strings.ToLower(text) == "yes" {
            message_body = "Thank you for your feedback"
        } else if strings.ToLower(text) == "no" {
            message_body = "We apologize for the inconvenience. A representative will contact you to assist you"
        } else {
            message_body = fmt.Sprintf("Response received was %s, which is invalid. Please reply with either 'Yes' or 'No'", text)
        }

        response := xml.NewResponse()
        message := xml.NewMessage()
        message.SetText(message_body)
        message.SetSrc(to_number)
        message.SetDst(from_number)
        response.Add(message)

        xmlBytes, _ := response.ToXML()
        w.Header().Set("Content-Type", "application/xml")
        fmt.Fprint(w, string(xmlBytes))
    }

    func main() {
        http.HandleFunc("/send-survey/", sendSurvey)
        http.HandleFunc("/survey-response/", surveyResponse)
        http.ListenAndServe(":8080", nil)
    }
    ```

    ***

    ### Test

    1. Run the application: `go run survey.go`.
    2. Expose your local server to the internet using ngrok: `ngrok http 8080`.
    3. Create a Plivo Application with the Message URL set to `https://<your-ngrok-url>.ngrok.io/survey-response/`.
    4. Assign a Plivo number to the application.
    5. Use a tool like Postman to send a POST request to `http://localhost:8080/send-survey/` to start the survey.
    6. Reply "Yes" or "No" from the destination phone.
  </Tab>
</Tabs>
