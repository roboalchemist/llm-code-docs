# 
      Bamboo.Mailer 
      (bamboo v2.5.0)

    

      
        **
        View Source
      

  

Functions for delivering emails using adapters and delivery strategies.

Adds `deliver_now/1`, `deliver_now!/1`, `deliver_later/1` and
`deliver_later!/1` functions to the mailer module in which it is used.

Bamboo ships with several adapters. It is also possible
to create your own adapter.

See the "Getting Started" section of the README for an
example of how to set up and configure a mailer for use.
## **Example

Creating a Mailer is as simple as defining a module in your application and
using the `Bamboo.Mailer`.

```
# some/path/within/your/app/mailer.ex
defmodule MyApp.Mailer do
  use Bamboo.Mailer, otp_app: :my_app
end
```

The mailer requires some configuration within your application.

```
# config/config.exs
config :my_app, MyApp.Mailer,
  adapter: Bamboo.MandrillAdapter, # Specify your preferred adapter
  api_key: "my_api_key" # Specify adapter-specific configuration
```

Also you will want to define an email module for building email structs that
your mailer can send. See [`Bamboo.Email`] for more information.

```
# some/path/within/your/app/email.ex
defmodule MyApp.Email do
  import Bamboo.Email

  def welcome_email do
    new_email(
      to: "john@example.com",
      from: "support@myapp.com",
      subject: "Welcome to the app.",
      html_body: "<strong>Thanks for joining!</strong>",
      text_body: "Thanks for joining!"
    )
  end
end
```

You are now able to send emails with your mailer module where you see fit
within your application.
    

    
# 
      
        **
      
      Summary
    

  
## 
    Functions
  

    
      
        build_config(mailer, otp_app, optional_overrides \\ %{})

      

    

    
      
        deliver_later(email, opts \\ [])

      

        

Deliver an email in the background.

    

    
      
        deliver_later!(email, opts \\ [])

      

        

Deliver an email in the background.

    

    
      
        deliver_now(email, opts \\ [])

      

        

Deliver an email right away.

    

    
      
        deliver_now!(email, opts \\ [])

      

        

Deliver an email right away.

    

    
      
        normalize_addresses(email)

      

        

Wraps to, cc and bcc addresses in a list and normalizes email addresses.

    

  

    
# 
      
        **
      
      Functions
    

    

    

  
    
      **
    
    
      
# build_config(mailer, otp_app, optional_overrides \\ %{})

        
          **
        

    
  

  

  

    

  
    
      **
    
    
      
# deliver_later(email, opts \\ [])

        
          **
        

    
  

  

Deliver an email in the background.

Call your mailer with `deliver_later/1` to send an email using the configured
`deliver_later_strategy`. If no `deliver_later_strategy` is set,
`Bamboo.TaskSupervisorStrategy` will be used. See
`Bamboo.DeliverLaterStrategy` to learn how to change how emails are delivered
with `deliver_later/1`.

If the email is successfully scheduled for delivery, this function will return
an `{:ok, email}`.

If the email is invalid, this function will return an `{:error, error}` tuple.
  

    

  
    
      **
    
    
      
# deliver_later!(email, opts \\ [])

        
          **
        

    
  

  

Deliver an email in the background.

Same as `deliver_later/2` but does not return an ok tuple and raises on
errors.

If successful, this function only returns the `Email` struct.

If the email is invalid, this function raises an error.
  

    

  
    
      **
    
    
      
# deliver_now(email, opts \\ [])

        
          **
        

    
  

  

Deliver an email right away.

Call your mailer with `deliver_now/1` to send an email right away. Call
`deliver_later/1` if you want to send in the background.

Pass in an argument of `response: true` if you need access to the response
from delivering the email.

A successful email delivery returns an ok tuple with the `Email` struct and
the response (if `response: true`) from calling `deliver` with your adapter.

A failure returns `{:error, error}` tuple.

Having the response returned from your adapter is useful if you need access to
any data sent back from your email provider in the response.

```
{:ok, email, response} = Email.welcome_email |> Mailer.deliver_now(response: true)
```

Pass in an argument of `config: %{}` if you would like to dynamically override
any keys in your application's default Mailer configuration.

```
Email.welcome_email
|> Mailer.deliver_now(config: %{username: "Emma", smtp_port: 2525})
```

  

    

  
    
      **
    
    
      
# deliver_now!(email, opts \\ [])

        
          **
        

    
  

  

Deliver an email right away.

Same as `deliver_now/2` but does not return an ok/error tuple.

If successful, this function returns the `Email` struct or an `Email`,
response tuple when setting `response: true`.

On failure, this function raises an error.
  

  
    
      **
    
    
      
# normalize_addresses(email)

        
          **
        

    
  

  

Wraps to, cc and bcc addresses in a list and normalizes email addresses.

Also formats the from address. Email normalization/formatting is done by
implementations of the [Bamboo.Formatter] protocol.