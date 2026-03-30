# Source: https://plivo.com/docs/messaging/use-cases/forward-sms-to-email/forward-sms-to-email.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Forward SMS Messages to Email

> Route incoming SMS messages to an email address for centralized archiving

<Tabs>
  <Tab title="Node">
    ## Overview

    This guide shows how to forward incoming SMS messages to an email address using Node.js, Express, and Nodemailer. This is a great way to centralize communications and create a searchable archive.

    ***

    ### Prerequisites

    * A Plivo account — [**sign up for free**](https://cx.plivo.com/signup).
    * An SMS-enabled Plivo phone number. You can [**rent a number**](/numbers/).
    * A Gmail account with an [**App Password**](https://support.google.com/mail/answer/185833?hl=en) enabled.
    * Node.js and ngrok. See our [**Node.js setup guide**](/sdk/server/set-up-node-dev-environment-api-messaging/).

    ***

    ### Create the email forwarding application

    Create a file named `smsemail.js`. This code sets up an Express server that listens for incoming SMS webhooks from Plivo. When a message is received, it uses Nodemailer to send its contents to your email address.

    Replace all the placeholder values in the `<...>` brackets with your actual information.

    ```js  theme={null}
    const express = require('express');
    const nodemailer = require("nodemailer");
    const app = express();

    app.use(express.urlencoded({ extended: true }));
    app.set('port', (process.env.PORT || 5000));

    app.all('/email_sms/', async (request, response) => {
        const from_number = request.body.From;
        const text = request.body.Text;
        console.log(`Message from: ${from_number}, Text: ${text}`);

        // Acknowledge the webhook from Plivo immediately
        response.status(204).send();

        const transporter = nodemailer.createTransport({
            service: 'gmail',
            auth: {
                user: "<your_gmail_address>",
                pass: "<your_gmail_app_password>"
            }
        });

        const mailOptions = {
            from: "<your_from_email_address>", // e.g., no-reply@yourdomain.com
            to: "<your_recipient_email_address>",
            subject: `New SMS from ${from_number}`,
            text: text
        };

        try {
            let info = await transporter.sendMail(mailOptions);
            console.log('Email sent: ' + info.response);
        } catch (error) {
            console.error('Error sending email:', error);
        }
    });

    app.listen(app.get('port'), () => {
        console.log('Node app is running on port', app.get('port'));
    });
    ```

    ***

    ### Create and configure a Plivo application

    1. **Create an Application**: Go to Messaging > [Applications](https://cx.plivo.com/xml-applications) and click **Add New Application**.
    2. **Configure the URL**: Name the application (e.g., `Forward SMS to Email`). In the `Message URL` field, enter your ngrok URL (e.g., `https://<yourdomain>.ngrok.io/email_sms/`). Set the method to `POST`. Click **Create Application**.
    3. **Assign a Number**: Go to the [Numbers](https://cx.plivo.com/phone-numbers) page, select your number, and link it to the `Forward SMS to Email` application.

    ***

    ### Test

    Send an SMS to your Plivo number. The message content should arrive in your email inbox shortly.
  </Tab>

  <Tab title="Ruby">
    ## Overview

    This guide shows how to forward incoming SMS messages to an email address using Ruby on Rails and the Mail gem. This is a great way to centralize communications and create a searchable archive.

    ***

    ### Prerequisites

    * A Plivo account — [**sign up for free**](https://cx.plivo.com/signup).
    * An SMS-enabled Plivo phone number. You can [**rent a number**](/numbers/).
    * A Gmail account with an [**App Password**](https://support.google.com/mail/answer/185833?hl=en) enabled.
    * Ruby on Rails and ngrok. See our [**Ruby setup guide**](/sdk/server/set-up-ruby-dev-environment-api-messaging/).
    * The Mail gem (`gem install mail`).

    ***

    ### Create the email forwarding application

    In your Rails controller (e.g., `app/controllers/plivo_controller.rb`), paste this code. This action receives the SMS webhook, sends the email, and then responds to Plivo to acknowledge receipt.

    Replace all the placeholder values in the `<...>` brackets with your actual information.

    ```rb  theme={null}
    require 'mail'

    class PlivoController < ApplicationController
      skip_before_action :verify_authenticity_token

      def forward_sms_to_email
        from_number = params[:From]
        text = params[:Text]
        puts "Message received from #{from_number}: #{text}"

        options = {
          address: "smtp.gmail.com",
          port: 587,
          user_name: '<your_gmail_address>',
          password: '<your_gmail_app_password>',
          authentication: 'plain',
          enable_starttls_auto: true
        }

        Mail.defaults do
          delivery_method :smtp, options
        end

        begin
          Mail.deliver do
            to '<your_recipient_email_address>'
            from '<your_from_email_address>'
            subject "New SMS from #{from_number}"
            body text
          end
          puts "Email sent successfully."
        rescue => e
          puts "Error sending email: #{e.message}"
        end

        # Acknowledge the webhook from Plivo
        head :ok
      end
    end
    ```

    ***

    ### Create and configure a Plivo application

    1. **Create an Application**: Go to Messaging > [Applications](https://cx.plivo.com/xml-applications) and click **Add New Application**.
    2. **Configure the URL**: Name the application (e.g., `Forward SMS to Email`). In your `Message URL`, enter your ngrok URL (e.g., `https://<yourdomain>.ngrok.io/your_route/`). Set the method to `POST`. Click **Create Application**.
    3. **Assign a Number**: Go to the [Numbers](https://cx.plivo.com/phone-numbers) page, select your number, and link it to the `Forward SMS to Email` application.

    ***

    ### Test

    Send an SMS to your Plivo number. The message content should arrive in your email inbox shortly.
  </Tab>

  <Tab title="Python">
    ## Overview

    This guide shows how to forward incoming SMS messages to an email address using Python, Flask, and the `smtplib` library. This is a great way to centralize communications and create a searchable archive.

    ***

    ### Prerequisites

    * A Plivo account — [**sign up for free**](https://cx.plivo.com/signup).
    * An SMS-enabled Plivo phone number. You can [**rent a number**](/numbers/).
    * A Gmail account with an [**App Password**](https://support.google.com/mail/answer/185833?hl=en) enabled.
    * Python and ngrok. See our [**Python setup guide**](/sdk/server/set-up-python-dev-environment-api-messaging/).

    ***

    ### Create the email forwarding application

    Create a file named `smsemail.py` and paste this code into it. This app listens for SMS webhooks and forwards the message content to your email.

    Replace all the placeholder values in the `<...>` brackets with your actual information.

    ```py  theme={null}
    from flask import Flask, request
    import smtplib
    from email.mime.text import MIMEText

    app = Flask(__name__)

    @app.route("/email_sms/", methods=['POST'])
    def forward_sms_to_email():
        from_number = request.values.get('From')
        text = request.values.get('Text')
        print(f'Message from: {from_number}, Text: {text}')

        user_name = '<your_gmail_address>'
        password = '<your_gmail_app_password>'
        from_email = '<your_from_email_address>'
        to_email = '<your_recipient_email_address>'

        msg = MIMEText(text)
        msg['Subject'] = f"New SMS from {from_number}"
        msg['From'] = from_email
        msg['To'] = to_email

        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(user_name, password)
                server.send_message(msg)
                print('Successfully sent email')
        except Exception as e:
            print(f'Failed to send email: {e}')

        return 'Webhook received', 200

    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000, debug=True)
    ```

    ***

    ### Create and configure a Plivo application

    1. **Create an Application**: Go to Messaging > [Applications](https://cx.plivo.com/xml-applications) and click **Add New Application**.
    2. **Configure the URL**: Name the application (e.g., `Forward SMS to Email`). In the `Message URL` field, enter your ngrok URL (e.g., `https://<yourdomain>.ngrok.io/email_sms/`). Set the method to `POST`. Click **Create Application**.
    3. **Assign a Number**: Go to the [Numbers](https://cx.plivo.com/phone-numbers) page, select your number, and link it to the `Forward SMS to Email` application.

    ***

    ### Test

    Send an SMS to your Plivo number. The message content should arrive in your email inbox shortly.
  </Tab>

  <Tab title="PHP">
    ## Overview

    This guide shows how to forward incoming SMS messages to an email address using PHP and the PHPMailer library. This is a great way to centralize communications and create a searchable archive.

    ***

    ### Prerequisites

    * A Plivo account — [**sign up for free**](https://cx.plivo.com/signup).
    * An SMS-enabled Plivo phone number. You can [**rent a number**](/numbers/).
    * A Gmail account with an [**App Password**](https://support.google.com/mail/answer/185833?hl=en) enabled.
    * PHP, Composer, and ngrok. See our [**PHP setup guide**](/sdk/server/set-up-php-dev-environment-api-messaging/).
    * PHPMailer (`composer require phpmailer/phpmailer`).

    ***

    ### Create the email forwarding application

    In your controller, paste this code. This action receives the SMS webhook, uses PHPMailer to send the email, and then responds to Plivo to acknowledge receipt.

    Replace all the placeholder values in the `<...>` brackets with your actual information.

    ```php  theme={null}
    <?php
    namespace App\Http\Controllers;

    use Illuminate\Http\Request;
    use PHPMailer\PHPMailer\PHPMailer;
    use PHPMailer\PHPMailer\Exception;

    class EmailController extends Controller
    {
        public function forward_sms_to_email()
        {
            $from_number = $_REQUEST["From"];
            $text = $_REQUEST["Text"];

            $mail = new PHPMailer(true);
            try {
                //Server settings
                $mail->isSMTP();
                $mail->Host       = 'smtp.gmail.com';
                $mail->SMTPAuth   = true;
                $mail->Username   = '<your_gmail_address>';
                $mail->Password   = '<your_gmail_app_password>';
                $mail->SMTPSecure = PHPMailer::ENCRYPTION_STARTTLS;
                $mail->Port       = 587;

                //Recipients
                $mail->setFrom('<your_from_email_address>', 'SMS Notifier');
                $mail->addAddress('<your_recipient_email_address>');

                //Content
                $mail->Subject = 'New SMS from ' . $from_number;
                $mail->Body    = $text;
                $mail->AltBody = $text;

                $mail->send();
                error_log('Message has been sent');
            } catch (Exception $e) {
                error_log("Message could not be sent. Mailer Error: {$mail->ErrorInfo}");
            }

            // Acknowledge the webhook from Plivo
            http_response_code(204);
        }
    }
    ```

    ***

    ### Create and configure a Plivo application

    1. **Create an Application**: Go to Messaging > [Applications](https://cx.plivo.com/xml-applications) and click **Add New Application**.
    2. **Configure the URL**: Name the application (e.g., `Forward SMS to Email`). In your `Message URL`, enter your ngrok URL (e.g., `https://<yourdomain>.ngrok.io/your_route/`). Set the method to `POST`. Click **Create Application**.
    3. **Assign a Number**: Go to the [Numbers](https://cx.plivo.com/phone-numbers) page, select your number, and link it to the `Forward SMS to Email` application.

    ***

    ### Test

    Send an SMS to your Plivo number. The message content should arrive in your email inbox shortly.
  </Tab>

  <Tab title=".NET">
    ## Overview

    This guide shows how to forward incoming SMS messages to an email address using .NET. This is a great way to centralize communications and create a searchable archive.

    ***

    ### Prerequisites

    * A Plivo account — [**sign up for free**](https://cx.plivo.com/signup).
    * An SMS-enabled Plivo phone number. You can [**rent a number**](/numbers/).
    * A Gmail account with an [**App Password**](https://support.google.com/mail/answer/185833?hl=en) enabled.
    * .NET and ngrok. See our [**.NET setup guide**](/sdk/server/set-up-dotnet-dev-environment-api-messaging/).

    ***

    ### Create the email forwarding application

    In your controller, paste this code. This action receives the SMS webhook, sends the email, and then responds to Plivo to acknowledge receipt.

    Replace all the placeholder values in the `<...>` brackets with your actual information.

    ```cs  theme={null}
    using System;
    using Microsoft.AspNetCore.Mvc;
    using System.Net;
    using System.Net.Mail;

    namespace EmailSms.Controllers
    {
        public class EmailSmsController : Controller
        {
            [HttpPost]
            public IActionResult Index()
            {
                string from_number = Request.Form["From"];
                string text = Request.Form["Text"];
                Console.WriteLine($"Message from: {from_number}, Text: {text}");

                string smtp_user = "<your_gmail_address>";
                string smtp_password = "<your_gmail_app_password>";
                string from_email = "<your_from_email_address>";
                string to_email = "<your_recipient_email_address>";

                try
                {
                    SmtpClient smtp = new SmtpClient
                    {
                        Host = "smtp.gmail.com",
                        Port = 587,
                        EnableSsl = true,
                        DeliveryMethod = SmtpDeliveryMethod.Network,
                        Credentials = new NetworkCredential(smtp_user, smtp_password)
                    };

                    MailMessage message = new MailMessage(from_email, to_email, $"New SMS from {from_number}", text);
                    smtp.Send(message);
                    Console.WriteLine("Email sent successfully.");
                }
                catch (Exception ex)
                {
                    Console.WriteLine("Error sending email: " + ex.Message);
                }

                return Ok("Webhook received.");
            }
        }
    }
    ```

    ***

    ### Create and configure a Plivo application

    1. **Create an Application**: Go to Messaging > [Applications](https://cx.plivo.com/xml-applications) and click **Add New Application**.
    2. **Configure the URL**: Name the application (e.g., `Forward SMS to Email`). In the `Message URL` field, enter your ngrok URL (e.g., `https://<yourdomain>.ngrok.io/EmailSms/`). Set the method to `POST`. Click **Create Application**.
    3. **Assign a Number**: Go to the [Numbers](https://cx.plivo.com/phone-numbers) page, select your number, and link it to the `Forward SMS to Email` application.

    ***

    ### Test

    Send an SMS to your Plivo number. The message content should arrive in your email inbox shortly.
  </Tab>

  <Tab title="Java">
    ## Overview

    This guide shows how to forward incoming SMS messages to an email address using Java with Spring and JavaMail. This is a great way to centralize communications and create a searchable archive.

    ***

    ### Prerequisites

    * A Plivo account — [**sign up for free**](https://cx.plivo.com/signup).
    * An SMS-enabled Plivo phone number. You can [**rent a number**](/numbers/).
    * A Gmail account with an [**App Password**](https://support.google.com/mail/answer/185833?hl=en) enabled.
    * Java and ngrok. See our [**Java setup guide**](/sdk/server/set-up-java-dev-environment-api-messaging/).
    * The JavaMail dependency (`javax.mail:mail`).

    ***

    ### Create the email forwarding application

    In your main application file, paste this code. This controller receives the SMS webhook, sends the email, and then responds to Plivo to acknowledge receipt.

    Replace all the placeholder values in the `<...>` brackets with your actual information.

    ```java  theme={null}
    package com.example.plivo;

    import org.springframework.boot.SpringApplication;
    import org.springframework.boot.autoconfigure.SpringBootApplication;
    import org.springframework.http.ResponseEntity;
    import org.springframework.web.bind.annotation.*;
    import javax.mail.*;
    import javax.mail.internet.InternetAddress;
    import javax.mail.internet.MimeMessage;
    import java.util.Properties;

    @SpringBootApplication
    @RestController
    public class PlivoApplication {
        public static void main(String[] args) {
            SpringApplication.run(PlivoApplication.class, args);
        }

        @PostMapping("/email_sms/")
        public ResponseEntity<Void> forwardSmsToEmail(String From, String Text) {
            System.out.println("Message from: " + From + ", Text: " + Text);

            final String username = "<your_gmail_address>";
            final String password = "<your_gmail_app_password>";

            Properties prop = new Properties();
            prop.put("mail.smtp.host", "smtp.gmail.com");
            prop.put("mail.smtp.port", "587");
            prop.put("mail.smtp.auth", "true");
            prop.put("mail.smtp.starttls.enable", "true");

            Session session = Session.getInstance(prop, new javax.mail.Authenticator() {
                protected PasswordAuthentication getPasswordAuthentication() {
                    return new PasswordAuthentication(username, password);
                }
            });

            try {
                Message message = new MimeMessage(session);
                message.setFrom(new InternetAddress("<your_from_email_address>"));
                message.setRecipients(Message.RecipientType.TO, InternetAddress.parse("<your_recipient_email_address>"));
                message.setSubject("New SMS from " + From);
                message.setText(Text);
                Transport.send(message);
                System.out.println("Email sent successfully.");
            } catch (MessagingException e) {
                e.printStackTrace();
            }

            return ResponseEntity.noContent().build();
        }
    }
    ```

    ***

    ### Create and configure a Plivo application

    1. **Create an Application**: Go to Messaging > [Applications](https://cx.plivo.com/xml-applications) and click **Add New Application**.
    2. **Configure the URL**: Name the application (e.g., `Forward SMS to Email`). In the `Message URL` field, enter your ngrok URL (e.g., `https://<yourdomain>.ngrok.io/email_sms/`). Set the method to `POST`. Click **Create Application**.
    3. **Assign a Number**: Go to the [Numbers](https://cx.plivo.com/phone-numbers) page, select your number, and link it to the `Forward SMS to Email` application.

    ***

    ### Test

    Send an SMS to your Plivo number. The message content should arrive in your email inbox shortly.
  </Tab>

  <Tab title="Go">
    ## Overview

    This guide shows how to forward incoming SMS messages to an email address using Go and its standard `net/smtp` library. This is a great way to centralize communications and create a searchable archive.

    ***

    ### Prerequisites

    * A Plivo account — [**sign up for free**](https://cx.plivo.com/signup).
    * An SMS-enabled Plivo phone number. You can [**rent a number**](/numbers/).
    * A Gmail account with an [**App Password**](https://support.google.com/mail/answer/185833?hl=en) enabled.
    * Go and ngrok. See our [**Go setup guide**](/sdk/server/set-up-go-dev-environment-api-messaging/).

    ***

    ### Create the email forwarding application

    Create a file named `smsemail.go` and paste this code into it. This server listens for SMS webhooks and forwards the message content to your email.

    Replace all the placeholder values in the `<...>` brackets with your actual information.

    ```go  theme={null}
    package main

    import (
        "fmt"
        "net/smtp"
        "net/http"
    )

    func forwardSmsToEmail(w http.ResponseWriter, r *http.Request) {
        from_number := r.FormValue("From")
        text := r.FormValue("Text")
        fmt.Printf("Message from: %s, Text: %s\n", from_number, text)

        from_email := "<your_from_email_address>"
        password := "<your_gmail_app_password>"
        to_email := []string{"<your_recipient_email_address>"}

        smtpHost := "smtp.gmail.com"
        smtpPort := "587"

        subject := "Subject: New SMS from " + from_number + "\r\n"
        body := text
        message := []byte(subject + "\r\n" + body)

        auth := smtp.PlainAuth("", from_email, password, smtpHost)

        err := smtp.SendMail(smtpHost+":"+smtpPort, auth, from_email, to_email, message)
        if err != nil {
            fmt.Println(err)
        } else {
            fmt.Println("Email sent successfully")
        }

        w.WriteHeader(http.StatusNoContent)
    }

    func main() {
        http.HandleFunc("/email_sms/", forwardSmsToEmail)
        http.ListenAndServe(":8080", nil)
    }
    ```

    ***

    ### Create and configure a Plivo application

    1. **Create an Application**: Go to Messaging > [Applications](https://cx.plivo.com/xml-applications) and click **Add New Application**.
    2. **Configure the URL**: Name the application (e.g., `Forward SMS to Email`). In the `Message URL` field, enter your ngrok URL (e.g., `https://<yourdomain>.ngrok.io/email_sms/`). Set the method to `POST`. Click **Create Application**.
    3. **Assign a Number**: Go to the [Numbers](https://cx.plivo.com/phone-numbers) page, select your number, and link it to the `Forward SMS to Email` application.

    ***

    ### Test

    Send an SMS to your Plivo number. The message content should arrive in your email inbox shortly.
  </Tab>
</Tabs>
