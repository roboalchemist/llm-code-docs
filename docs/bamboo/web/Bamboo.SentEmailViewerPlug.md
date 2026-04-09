# 
      Bamboo.SentEmailViewerPlug 
      (bamboo v2.5.0)

    

      
        **
        View Source
      

  

A plug that can be used in your router to see delivered emails.

This plug allows you to view all delivered emails. To see emails you must use
the `Bamboo.LocalAdapter`.
## **Using with Plug or Phoenix

```
# Make sure you are using Bamboo.LocalAdapter in your config
config :my_app, MyApp.Mailer,
  adapter: Bamboo.LocalAdapter

# In your Router
defmodule MyApp.Router do
  use Phoenix.Router # or use Plug.Router if you're not using Phoenix

  if Mix.env == :dev do
    # If using Phoenix
    forward "/sent_emails", Bamboo.SentEmailViewerPlug

    # If using Plug.Router, make sure to add the `to`
    forward "/sent_emails", to: Bamboo.SentEmailViewerPlug
  end
end
```

Now if you visit your app at `/sent_emails` you will see a list of delivered
emails.
    

    
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