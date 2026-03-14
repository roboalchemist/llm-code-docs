# Module: ActionCable::Server::Broadcasting
  
  
  

  

  
  
  
  
  

  
  
    Included in:
    Base
  
  

  
  
    Defined in:
    lib/action_cable/server/broadcasting.rb
  
  

## Overview

  
    

# Action Cable Server Broadcasting

Broadcasting is how other parts of your application can send messages to a channel’s subscribers. As explained in Channel, most of the time, these broadcastings are streamed directly to the clients subscribed to the named broadcasting. Let’s explain with a full-stack example:

```
class WebNotificationsChannel < ApplicationCable::Channel
  def subscribed
    stream_from "web_notifications_#{current_user.id}"
  end
end

# Somewhere in your app this is called, perhaps from a NewCommentJob:
ActionCable.server.broadcast \
  "web_notifications_1", { title: "New things!", body: "All that's fit for print" }

# Client-side JavaScript, which assumes you've already requested the right to send web notifications:
App.cable.subscriptions.create("WebNotificationsChannel", {
  received: function(data) {
    new Notification(data['title'], { body: data['body'] })
  }
})

```

  

  

## Defined Under Namespace

  
    
  
    
      **Classes:** Broadcaster
    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**broadcast**(broadcasting, message, coder: ActiveSupport::JSON)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Broadcast a hash directly to a named `broadcasting`.

  

      
        
- 
  
    
      #**broadcaster_for**(broadcasting, coder: ActiveSupport::JSON)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Returns a broadcaster for a named `broadcasting` that can be reused.

  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**broadcast**(broadcasting, message, coder: ActiveSupport::JSON)  ⇒ Object 
  

  

  

  
    

Broadcast a hash directly to a named `broadcasting`. This will later be JSON encoded.

  

  

  
    
      

```

33
34
35
```

    
    
      

```
# File 'lib/action_cable/server/broadcasting.rb', line 33

def broadcast(broadcasting, message, coder: ActiveSupport::JSON)
  broadcaster_for(broadcasting, coder: coder).broadcast(message)
end
```

    
  

    
      
  
### 
  
    #**broadcaster_for**(broadcasting, coder: ActiveSupport::JSON)  ⇒ Object 
  

  

  

  
    

Returns a broadcaster for a named `broadcasting` that can be reused. Useful when you have an object that may need multiple spots to transmit to a specific broadcasting over and over.

  

  

  
    
      

```

40
41
42
```

    
    
      

```
# File 'lib/action_cable/server/broadcasting.rb', line 40

def broadcaster_for(broadcasting, coder: ActiveSupport::JSON)
  Broadcaster.new(self, String(broadcasting), coder: coder)
end
```