# 
      Bamboo.SentEmailApiPlug 
      (bamboo v2.5.0)

    

      
        **
        View Source
      

  

A plug that exposes delivered emails over a JSON API.

This is useful for an integration test runner that doesn't have
access to the `Bamboo.Test` helpers, but needs to be able to assert that
emails have been delivered.

You must use the `Bamboo.LocalAdapter` or no emails will be available.
## **Using with Plug or Phoenix

```
# Make sure you are using Bamboo.LocalAdapter in your config
config :my_app, MyApp.Mailer,
  adapter: Bamboo.LocalAdapter

# In your Router
defmodule MyApp.Router do
  use Phoenix.Router # or use Plug.Router if you're not using Phoenix

  if Mix.env == :e2e do
    # If using Phoenix
    forward "/sent_emails_api", Bamboo.SentEmailApiPlug

    # If using Plug.Router, make sure to add the `to`
    forward "/sent_emails_api", to: Bamboo.SentEmailApiPlug
  end
end
```

## **API endpoints

There are two endpoints:

- `GET /emails.json` exposes the list of sent emails
- `POST /reset.json` resets the sent emails back to an empty list

Usually, you would `POST` to `/reset.json` at the beginning of a test run,
and `GET` from `/emails.json` as you need to during an integration test to
make assertions. The details of how you make assertions is left up to your
integration test runner.
## **Email response JSON

Sent emails are returned in the following format:

```
{
  "to": [[null, "to@example.com"], ["Alice", "alice@example.com"]],
  "text_body": "hello world",
  "subject": "This is a test email",
  "html_body": "<p>hello world</p>",
  "headers": {},
  "from": [null, "from@example.com"],
  "cc": [[null, "cc@example.com"]],
  "bcc": [["Bob", "bob@example.com"]],
  "attachments": []
}
```

Email addresses are returned in array pairs, with the first element as the
name, and the second as the email address. The first element can be `null`
if the address didn't specify a name. The `to`, `cc` and `bcc` fields are
returned as arrays of these pairs.
    

    
# 
      
        **
      
      Summary
    

  
## 
    Functions
  

    
      
        call(conn, opts)

      

        

Callback implementation for `Plug.call/2`.

    

    
      
        init(opts)

      

        

Callback implementation for `Plug.init/1`.

    

  

    
# 
      
        **
      
      Functions
    

    

  
    
      **
    
    
      
# call(conn, opts)

        
          **
        

    
  

  

Callback implementation for `Plug.call/2`.
  

  
    
      **
    
    
      
# init(opts)

        
          **
        

    
  

  

Callback implementation for `Plug.init/1`.