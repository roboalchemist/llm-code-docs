# Class: ActionCable::Channel::Base
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- ActionCable::Channel::Base
          
        

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      Broadcasting, Callbacks, Naming, PeriodicTimers, Streams, ActiveSupport::Rescuable
  
  
  

  

  
  
    Defined in:
    lib/action_cable/channel/base.rb
  
  

## Overview

  
    

# Action Cable Channel Base

The channel provides the basic structure of grouping behavior into logical units when communicating over the WebSocket connection. You can think of a channel like a form of controller, but one that’s capable of pushing content to the subscriber in addition to simply responding to the subscriber’s direct requests.

Channel instances are long-lived. A channel object will be instantiated when the cable consumer becomes a subscriber, and then lives until the consumer disconnects. This may be seconds, minutes, hours, or even days. That means you have to take special care not to do anything silly in a channel that would balloon its memory footprint or whatever. The references are forever, so they won’t be released as is normally the case with a controller instance that gets thrown away after every request.

Long-lived channels (and connections) also mean you’re responsible for ensuring that the data is fresh. If you hold a reference to a user record, but the name is changed while that reference is held, you may be sending stale data if you don’t take precautions to avoid it.

The upside of long-lived channel instances is that you can use instance variables to keep reference to objects that future subscriber requests can interact with. Here’s a quick example:

```
class ChatChannel < ApplicationCable::Channel
  def subscribed
    @room = Chat::Room[params[:room_number]]
  end

  def speak(data)
    @room.speak data, user: current_user
  end
end

```

The #speak action simply uses the Chat::Room object that was created when the channel was first subscribed to by the consumer when that subscriber wants to say something in the room.

## Action processing

Unlike subclasses of ActionController::Base, channels do not follow a RESTful constraint form for their actions. Instead, Action Cable operates through a remote-procedure call model. You can declare any public method on the channel (optionally taking a `data` argument), and this method is automatically exposed as callable to the client.

Example:

```
class AppearanceChannel < ApplicationCable::Channel
  def subscribed
    @connection_token = generate_connection_token
  end

  def unsubscribed
    current_user.disappear @connection_token
  end

  def appear(data)
    current_user.appear @connection_token, on: data['appearing_on']
  end

  def away
    current_user.away @connection_token
  end

  private
    def generate_connection_token
      SecureRandom.hex(36)
    end
end

```

In this example, the subscribed and unsubscribed methods are not callable methods, as they were already declared in ActionCable::Channel::Base, but `#appear` and `#away` are. `#generate_connection_token` is also not callable, since it’s a private method. You’ll see that appear accepts a data parameter, which it then uses as part of its model call. `#away` does not, since it’s simply a trigger action.

Also note that in this example, `current_user` is available because it was marked as an identifying attribute on the connection. All such identifiers will automatically create a delegation method of the same name on the channel instance.

## Rejecting subscription requests

A channel can reject a subscription request in the #subscribed callback by invoking the #reject method:

```
class ChatChannel < ApplicationCable::Channel
  def subscribed
    @room = Chat::Room[params[:room_number]]
    reject unless current_user.can_access?(@room)
  end
end

```

In this example, the subscription will be rejected if the `current_user` does not have access to the chat room. On the client-side, the ‘Channel#rejected` callback will get invoked when the server rejects the subscription request.

  

  

  
## Constant Summary

  
  
### Constants included
     from Callbacks

  

Callbacks::INTERNAL_METHODS

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**connection**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute connection.

  

    
      
- 
  
    
      #**identifier**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute identifier.

  

    
      
- 
  
    
      #**params**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute params.

  

    
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**action_methods**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

A list of method names that should be considered actions.

  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**initialize**(connection, identifier, params = {})  ⇒ Base 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Base.

  

      
        
- 
  
    
      #**perform_action**(data)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Extract the action name from the passed data and process it via the channel.

  

      
        
- 
  
    
      #**subscribe_to_channel**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

This method is called after subscription has been added to the connection and confirms or rejects the subscription.

  

      
        
- 
  
    
      #**unsubscribe_from_channel**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Called by the cable connection when it’s cut, so the channel has a chance to cleanup with callbacks.

  

      
        
- 
  
    
      #**unsubscribed?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

:nodoc:.

  

      
    

  

  
  
  
  
  
  
  
  
  
  
### Methods included from Broadcasting

  

#broadcast_to, #broadcasting_for

  
  
  
  
  
  
  
  
  
  
### Methods included from Naming

  

#channel_name

  
  
  
  
  
  
  
  
  
  
### Methods included from Streams

  

#stop_all_streams, #stop_stream_for, #stop_stream_from, #stream_for, #stream_from, #stream_or_reject_for

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
## Constructor Details

  
    
  
### 
  
    #**initialize**(connection, identifier, params = {})  ⇒ Base 
  

  

  

  
    

Returns a new instance of Base.

  

  

  
    
      

```

163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
```

    
    
      

```
# File 'lib/action_cable/channel/base.rb', line 163

def initialize(connection, identifier, params = {})
  @connection = connection
  @identifier = identifier
  @params     = params

  # When a channel is streaming via pubsub, we want to delay the confirmation
  # transmission until pubsub subscription is confirmed.
  #
  # The counter starts at 1 because it's awaiting a call to #subscribe_to_channel
  @defer_subscription_confirmation_counter = Concurrent::AtomicFixnum.new(1)

  @reject_subscription = nil
  @subscription_confirmation_sent = nil
  @unsubscribed = false

  delegate_connection_identifiers
end
```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**connection**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute connection.

  

  

  
    
      

```

117
118
119
```

    
    
      

```
# File 'lib/action_cable/channel/base.rb', line 117

def connection
  @connection
end
```

    
  

    
      
      
      
  
### 
  
    #**identifier**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute identifier.

  

  

  
    
      

```

117
118
119
```

    
    
      

```
# File 'lib/action_cable/channel/base.rb', line 117

def identifier
  @identifier
end
```

    
  

    
      
      
      
  
### 
  
    #**params**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute params.

  

  

  
    
      

```

117
118
119
```

    
    
      

```
# File 'lib/action_cable/channel/base.rb', line 117

def params
  @params
end
```

    
  

    
  

  
    
## Class Method Details

    
      
  
### 
  
    .**action_methods**  ⇒ Object 
  

  

  

  
    

A list of method names that should be considered actions. This includes all public instance methods on a channel, less any internal methods (defined on Base), adding back in any methods that are internal, but still exist on the class itself.

#### Returns

- 

`Set` - A set of all methods that should be considered actions.

  

  

  
    
      

```

128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
```

    
    
      

```
# File 'lib/action_cable/channel/base.rb', line 128

def action_methods
  @action_methods ||= begin
    # All public instance methods of this class, including ancestors
    methods = (public_instance_methods(true) -
      # Except for public instance methods of Base and its ancestors
      ActionCable::Channel::Base.public_instance_methods(true) +
      # Be sure to include shadowed public instance methods of this class
      public_instance_methods(false) -
      # Except the internal methods
      internal_methods).uniq

    methods.map!(&:name)
    methods.to_set
  end
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**perform_action**(data)  ⇒ Object 
  

  

  

  
    

Extract the action name from the passed data and process it via the channel. The process will ensure that the action requested is a public method on the channel declared by the user (so not one of the callbacks like #subscribed).

  

  

  
    
      

```

184
185
186
187
188
189
190
191
192
193
194
195
```

    
    
      

```
# File 'lib/action_cable/channel/base.rb', line 184

def perform_action(data)
  action = extract_action(data)

  if processable_action?(action)
    payload = { channel_class: self.class.name, action: action, data: data }
    ActiveSupport::Notifications.instrument("perform_action.action_cable", payload) do
      dispatch_action(action, data)
    end
  else
    logger.error "Unable to process #{action_signature(action, data)}"
  end
end
```

    
  

    
      
  
### 
  
    #**subscribe_to_channel**  ⇒ Object 
  

  

  

  
    

This method is called after subscription has been added to the connection and confirms or rejects the subscription.

  

  

  
    
      

```

199
200
201
202
203
204
205
206
```

    
    
      

```
# File 'lib/action_cable/channel/base.rb', line 199

def subscribe_to_channel
  run_callbacks :subscribe do
    subscribed
  end

  reject_subscription if subscription_rejected?
  ensure_confirmation_sent
end
```

    
  

    
      
  
### 
  
    #**unsubscribe_from_channel**  ⇒ Object 
  

  

  

  
    

Called by the cable connection when it’s cut, so the channel has a chance to cleanup with callbacks. This method is not intended to be called directly by the user. Instead, override the #unsubscribed callback.

  

  

  
    
      

```

211
212
213
214
215
216
```

    
    
      

```
# File 'lib/action_cable/channel/base.rb', line 211

def unsubscribe_from_channel # :nodoc:
  @unsubscribed = true
  run_callbacks :unsubscribe do
    unsubscribed
  end
end
```

    
  

    
      
  
### 
  
    #**unsubscribed?**  ⇒ Boolean 
  

  

  

  
    

:nodoc:

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

218
219
220
```

    
    
      

```
# File 'lib/action_cable/channel/base.rb', line 218

def unsubscribed? # :nodoc:
  @unsubscribed
end
```