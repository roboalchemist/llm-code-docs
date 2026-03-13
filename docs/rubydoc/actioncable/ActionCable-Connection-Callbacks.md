# Module: ActionCable::Connection::Callbacks
  
  
  

  

  
  
  
      Extended by:
      ActiveSupport::Concern
  
  
  
  
  
      Includes:
      ActiveSupport::Callbacks
  
  
  

  
  
    Included in:
    Base
  
  

  
  
    Defined in:
    lib/action_cable/connection/callbacks.rb
  
  

## Overview

  
    

# Action Cable Connection Callbacks

The [before_command](ClassMethods#before_command), [after_command](ClassMethods#after_command), and [around_command](ClassMethods#around_command) callbacks are invoked when sending commands to the client, such as when subscribing, unsubscribing, or performing an action.

#### Example

```
module ApplicationCable
  class Connection < ActionCable::Connection::Base
    identified_by :user

    around_command :set_current_account

    private

    def set_current_account
      # Now all channels could use Current.account
      Current.set(account: user.account) { yield }
    end
  end
end

```

  

  

## Defined Under Namespace

  
    
      **Modules:** ClassMethods