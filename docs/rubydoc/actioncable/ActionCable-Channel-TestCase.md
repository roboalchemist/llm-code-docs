# Class: ActionCable::Channel::TestCase
  
  
  

  
  
    Inherits:
    
      ActiveSupport::TestCase
      
        

          
- Object
          
            
- ActiveSupport::TestCase
          
            
- ActionCable::Channel::TestCase
          
        

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      Behavior
  
  
  

  

  
  
    Defined in:
    lib/action_cable/channel/test_case.rb
  
  

## Overview

  
    

Superclass for Action Cable channel functional tests.

## Basic example

Functional tests are written as follows:

- 

First, one uses the `subscribe` method to simulate subscription creation.

- 

Then, one asserts whether the current state is as expected. “State” can be anything: transmitted messages, subscribed streams, etc.

For example:

```
class ChatChannelTest < ActionCable::Channel::TestCase
  def test_subscribed_with_room_number
    # Simulate a subscription creation
    subscribe room_number: 1

    # Asserts that the subscription was successfully created
    assert subscription.confirmed?

    # Asserts that the channel subscribes connection to a stream
    assert_has_stream "chat_1"

    # Asserts that the channel subscribes connection to a specific
    # stream created for a model
    assert_has_stream_for Room.find(1)
  end

  def test_does_not_stream_with_incorrect_room_number
    subscribe room_number: -1

    # Asserts that not streams was started
    assert_no_streams
  end

  def test_does_not_subscribe_without_room_number
    subscribe

    # Asserts that the subscription was rejected
    assert subscription.rejected?
  end
end

```

You can also perform actions:

```
def test_perform_speak
  subscribe room_number: 1

  perform :speak, message: "Hello, Rails!"

  assert_equal "Hello, Rails!", transmissions.last["text"]
end

```

## Special methods

ActionCable::Channel::TestCase will also automatically provide the following instance methods for use in the tests:

connection :   An ActionCable::Channel::ConnectionStub, representing the current HTTP

```
connection.

```

subscription :   An instance of the current channel, created when you call `subscribe`.

transmissions :   A list of all messages that have been transmitted into the channel.

## Channel is automatically inferred

ActionCable::Channel::TestCase will automatically infer the channel under test from the test class name. If the channel cannot be inferred from the test class name, you can explicitly set it with `tests`.

```
class SpecialEdgeCaseChannelTest < ActionCable::Channel::TestCase
  tests SpecialChannel
end

```

## Specifying connection identifiers

You need to set up your connection manually to provide values for the identifiers. To do this just use:

```
stub_connection(user: users(:john))

```

## Testing broadcasting

ActionCable::Channel::TestCase enhances ActionCable::TestHelper assertions (e.g. `assert_broadcasts`) to handle broadcasting to models:

```
# in your channel
def speak(data)
  broadcast_to room, text: data["message"]
end

def test_speak
  subscribe room_id: rooms(:chat).id

  assert_broadcast_on(rooms(:chat), text: "Hello, Rails!") do
    perform :speak, message: "Hello, Rails!"
  end
end

```

  

  

## Defined Under Namespace

  
    
      **Modules:** Behavior
    
  
    
  

  
## Constant Summary

  
  
### Constants included
     from Behavior

  

Behavior::CHANNEL_IDENTIFIER

  
  
  
  
  
  
  
## Method Summary

  
  
### Methods included from Behavior

  

#assert_broadcast_on, #assert_broadcasts, #assert_has_no_stream, #assert_has_no_stream_for, #assert_has_stream, #assert_has_stream_for, #assert_no_streams, #perform, #stub_connection, #subscribe, #transmissions, #unsubscribe

  
  
  
  
  
  
  
  
  
  
### Methods included from TestHelper

  

#after_teardown, #assert_broadcast_on, #assert_broadcasts, #assert_no_broadcasts, #before_setup, #capture_broadcasts, #pubsub_adapter