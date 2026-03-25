# 
      Bamboo.Adapter behaviour
      (bamboo v2.5.0)

    

      
        **
        View Source
      

  

Behaviour for creating Bamboo adapters

All recipients in the `Bamboo.Email` struct will be normalized to a two item
tuple of `{name, address}` when delivered through your mailer. For example,
`elem(email.from, 0)` would return the name and `elem(email.from, 1)` would
return the email address.

For more in-depth examples check out the
adapters in Bamboo.
## **Example

```
defmodule Bamboo.CustomAdapter do
  @behaviour Bamboo.Adapter

  def deliver(email, config) do
    deliver_the_email_somehow(email)
  end

  def handle_config(config) do
    # Return the config if nothing special is required
    config

    # Or you could require certain config options
    if Map.get(config, :smtp_username) do
      config
    else
      raise "smtp_username is required in config, got #{inspect(config)}"
    end
  end

  def supports_attachments?, do: true
end
```

    

    
# 
      
        **
      
      Summary
    

  
## 
    Types
  

    
      
        error()

      

    

  
## 
    Callbacks
  

    
      
        deliver(%Bamboo.Email{}, map)

      

    

    
      
        handle_config(map)

      

    

    
      
        supports_attachments?()

      

    

  

    
# 
      
        **
      
      Types
    

    

  
    
      **
    
    
      
# error()

        
          **
        

    
  

  

      

          

```
@type error() :: Exception.t() | String.t()
```

      

  

    
# 
      
        **
      
      Callbacks
    

    

  
    
      **
    
    
      
# deliver(%Bamboo.Email{}, map)

        
          **
        

    
  

  

      

          

```
@callback deliver(
  %Bamboo.Email{
    assigns: term(),
    attachments: term(),
    bcc: term(),
    blocked: term(),
    cc: term(),
    from: term(),
    headers: term(),
    html_body: term(),
    private: term(),
    subject: term(),
    text_body: term(),
    to: term()
  },
  map()
) :: {:ok, any()} | {:error, error()}
```

      

  

  
    
      **
    
    
      
# handle_config(map)

        
          **
        

    
  

  

      

          

```
@callback handle_config(map()) :: map()
```

      

  

  
    
      **
    
    
      
# supports_attachments?()

        
          **
        

    
  

  

      

          

```
@callback supports_attachments?() :: boolean()
```