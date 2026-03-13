infobip
      
      **
        v0.2.0
      **
    

  

  

    
- Pages

      
- Modules

  

  
  

  
    

      
# 
Infobip (infobip v0.2.0)

      

        

A simple Infobip REST API client for Elixir.

You can find the hex package here, and the
docs here.
## 
  
  Usage

```
def deps do
  [{:infobip, "~> 0.2"}]
end
```

Then run `$ mix do deps.get, compile` to download and compile your
dependencies.

You'll need to set a few config parameters, take a look in the
`dev.exs.sample` file for an example of what is required.

Then sending a text message is as easy as:

```
:ok = Infobip.send("27820001111", "Test message")
```

You can optionally specify a message ID if you want to fetch delivery
reports:

```
:ok = Infobip.send("27820001111", "Test message", "123")
```

You need to pass a valid international mobile number to the `send` method.

To fetch a delivery report, just use the message ID you assigned in `send/3`:

```
Infobip.delivery_report("123")
```

        

          
# 
            
              
              Link to this section
            
            Summary
          

  
    
## 
      Functions
    

  
    delivery_report(message_id)

  

    

Fetches a text message delivery report.

  
    send(recipient, message)

  

    

Sends a text message.

  
    send(recipient, message, message_id)

  

  

        

          
# 
            
              
              Link to this section
            
Functions
          

          

  
    
      
      Link to this function
    
    
# delivery_report(message_id)

  

  

      
## Specs

      

          

```
delivery_report(any()) :: Infobip.DeliveryReport.fetch_response()
```

      

Fetches a text message delivery report.
  

  
    
      
      Link to this function
    
    
# send(recipient, message)

  

  

      
## Specs

      

          

```
send(binary(), binary()) :: Infobip.TextMessage.send_response()
```

      

Sends a text message.
  

  
    
      
      Link to this function
    
    
# send(recipient, message, message_id)

  

  

      
## Specs

      

          

```
send(binary(), binary(), any()) :: Infobip.TextMessage.send_response()
```