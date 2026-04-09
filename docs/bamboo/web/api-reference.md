# API Reference bamboo v#2.5.0

      
        **
        View Source
      

  

      
## Modules

      

  
    Bamboo.Adapter

  

    

Behaviour for creating Bamboo adapters

  
    Bamboo.AdapterHelper

  

  
    Bamboo.ApiError

  

    

Error used to represent a problem when sending emails through an external email service API.

  
    Bamboo.Attachment

  

    

  
    Bamboo.DeliverLaterStrategy

  

    

Behaviour for delivering emails with `Bamboo.Mailer.deliver_later/1`.

  
    Bamboo.Email

  

    

Contains functions for composing emails.

  
    Bamboo.EmptyFromAddressError

  

  
    Bamboo.Formatter

  

    

Converts data to email addresses.

  
    Bamboo.ImmediateDeliveryStrategy

  

    

Strategy for `Bamboo.Mailer.deliver_later/1` that sends the email
immediately.

  
    Bamboo.Interceptor

  

    

Behaviour for creating an Interceptor.

  
    Bamboo.LocalAdapter

  

    

Stores emails locally. Can be queried to see sent emails.

  
    Bamboo.Mailer

  

    

Functions for delivering emails using adapters and delivery strategies.

  
    Bamboo.MailgunAdapter

  

    

Sends email using Mailgun's API.

  
    Bamboo.MailgunHelper

  

    

Functions for using features specific to Mailgun
(e.g. tagging, templates).

  
    Bamboo.MandrillAdapter

  

    

Sends email using Mandrill's JSON API.

  
    Bamboo.MandrillHelper

  

    

Functions for using features specific to Mandrill (e.g. tagging, merge vars,
templates).

  
    Bamboo.NilRecipientsError

  

  
    Bamboo.SendGridAdapter

  

    

Sends email using SendGrid's JSON API.

  
    Bamboo.SendGridHelper

  

    

Functions for using features specific to Sendgrid.

  
    Bamboo.SentEmail

  

    

Used for storing and retrieving sent emails when used with `Bamboo.LocalAdapter`.

  
    Bamboo.SentEmail.DeliveriesError

  

  
    Bamboo.SentEmail.NoDeliveriesError

  

  
    Bamboo.SentEmailApiPlug

  

    

A plug that exposes delivered emails over a JSON API.

  
    Bamboo.SentEmailViewerPlug

  

    

A plug that can be used in your router to see delivered emails.

  
    Bamboo.TaskSupervisorStrategy

  

    

Default strategy. Sends an email in the background using `Task.Supervisor`.

  
    Bamboo.Template

  

    

Render emails with layouts, view modules, and templates.

  
    Bamboo.Test

  

    

Helpers for testing email delivery.

  
    Bamboo.TestAdapter

  

    

Used for testing email delivery.

  
    Bamboo.View

  

    

Compiles and renders templates defined in a given path.

  
    Bamboo.View.UndefinedTemplateError

  

    

Exception raised when a template cannot be found.