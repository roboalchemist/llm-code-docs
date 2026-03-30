# 
      Bamboo.LocalAdapter 
      (bamboo v2.5.0)

    

      
        **
        View Source
      

  

Stores emails locally. Can be queried to see sent emails.

Use this adapter for storing emails locally instead of sending them. Emails
are stored and can be read from `Bamboo.SentEmail`. Typically this adapter is
used in the dev environment so emails are not delivered to real email
addresses.

You can use this adapter along with `Bamboo.SentEmailViewerPlug` to view
emails in the browser.

If you want to open a new browser window for every new email, set the option
`open_email_in_browser_url` to your preview path.
## **Example config

```
# In config/config.exs, or config/dev.exs, etc.
config :my_app, MyApp.Mailer,
  adapter: Bamboo.LocalAdapter,
  open_email_in_browser_url: "http://localhost:4000/sent_emails" # optional

# Define a Mailer. Maybe in lib/my_app/mailer.ex
defmodule MyApp.Mailer do
  use Bamboo.Mailer, otp_app: :my_app
end
```

    

    
# 
      
        **
      
      Summary
    

  
## 
    Functions
  

    
      
        deliver(email, arg2)

      

        

Adds email to `Bamboo.SentEmail`, can automatically open it in new browser tab

    

    
      
        handle_config(config)

      

        

Callback implementation for `Bamboo.Adapter.handle_config/1`.

    

    
      
        supports_attachments?()

      

        

Callback implementation for `Bamboo.Adapter.supports_attachments?/0`.

    

  

    
# 
      
        **
      
      Functions
    

    

  
    
      **
    
    
      
# deliver(email, arg2)

        
          **
        

    
  

  

Adds email to `Bamboo.SentEmail`, can automatically open it in new browser tab
  

  
    
      **
    
    
      
# handle_config(config)

        
          **
        

    
  

  

Callback implementation for `Bamboo.Adapter.handle_config/1`.
  

  
    
      **
    
    
      
# supports_attachments?()

        
          **
        

    
  

  

Callback implementation for `Bamboo.Adapter.supports_attachments?/0`.