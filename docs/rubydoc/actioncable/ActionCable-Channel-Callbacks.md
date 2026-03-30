# Module: ActionCable::Channel::Callbacks
  
  
  

  

  
  
  
      Extended by:
      ActiveSupport::Concern
  
  
  
  
  
      Includes:
      ActiveSupport::Callbacks
  
  
  

  
  
    Included in:
    Base
  
  

  
  
    Defined in:
    lib/action_cable/channel/callbacks.rb
  
  

## Overview

  
    

# Action Cable Channel Callbacks

Action Cable Channel provides callback hooks that are invoked during the life cycle of a channel:

- 

[before_subscribe](ClassMethods#before_subscribe)

- 

[after_subscribe](ClassMethods#after_subscribe) (aliased as [on_subscribe](ClassMethods#on_subscribe))

- 

[before_unsubscribe](ClassMethods#before_unsubscribe)

- 

[after_unsubscribe](ClassMethods#after_unsubscribe) (aliased as [on_unsubscribe](ClassMethods#on_unsubscribe))

#### Example

```
class ChatChannel < ApplicationCable::Channel
  after_subscribe :send_welcome_message, unless: :subscription_rejected?
  after_subscribe :track_subscription

  private
    def send_welcome_message
      broadcast_to(...)
    end

    def track_subscription
      # ...
    end
end

```

  

  

## Defined Under Namespace

  
    
      **Modules:** ClassMethods
    
  
    
  

  
    
## 
      Constant Summary
      collapse
    

    
      
        INTERNAL_METHODS =
          
  
    

:nodoc:

  

  

        
        

```
[:_run_subscribe_callbacks, :_run_unsubscribe_callbacks]
```