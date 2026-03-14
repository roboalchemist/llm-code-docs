# Module: ActionCable::TestHelper
  
  
  

  

  
  
  
  
  

  
  
    Included in:
    Channel::TestCase::Behavior, TestCase
  
  

  
  
    Defined in:
    lib/action_cable/test_helper.rb
  
  

## Overview

  
    

Provides helper methods for testing Action Cable broadcasting

  

  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**after_teardown**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:nodoc:.

  

      
        
- 
  
    
      #**assert_broadcast_on**(stream, data, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Asserts that the specified message has been sent to the stream.

  

      
        
- 
  
    
      #**assert_broadcasts**(stream, number, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Asserts that the number of broadcasted messages to the stream matches the given number.

  

      
        
- 
  
    
      #**assert_no_broadcasts**(stream, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Asserts that no messages have been sent to the stream.

  

      
        
- 
  
    
      #**before_setup**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:nodoc:.

  

      
        
- 
  
    
      #**capture_broadcasts**(stream, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Returns the messages that are broadcasted in the block.

  

      
        
- 
  
    
      #**pubsub_adapter**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:nodoc:.

  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**after_teardown**  ⇒ Object 
  

  

  

  
    

:nodoc:

  

  

  
    
      

```

18
19
20
21
```

    
    
      

```
# File 'lib/action_cable/test_helper.rb', line 18

def after_teardown # :nodoc:
  super
  ActionCable.server.instance_variable_set(:@pubsub, @old_pubsub_adapter)
end
```

    
  

    
      
  
### 
  
    #**assert_broadcast_on**(stream, data, &block)  ⇒ Object 
  

  

  

  
    

Asserts that the specified message has been sent to the stream.

```
def test_assert_transmitted_message
  ActionCable.server.broadcast 'messages', text: 'hello'
  assert_broadcast_on('messages', text: 'hello')
end

```

If a block is passed, that block should cause a message with the specified data to be sent.

```
def test_assert_broadcast_on_again
  assert_broadcast_on('messages', text: 'hello') do
    ActionCable.server.broadcast 'messages', text: 'hello'
  end
end

```

  

  

  
    
      

```

116
117
118
119
120
121
122
123
124
125
126
127
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
```

    
    
      

```
# File 'lib/action_cable/test_helper.rb', line 116

def assert_broadcast_on(stream, data, &block)
  # Encode to JSON and back–we want to use this value to compare with decoded
  # JSON. Comparing JSON strings doesn't work due to the order if the keys.
  serialized_msg =
    ActiveSupport::JSON.decode(ActiveSupport::JSON.encode(data))

  new_messages = broadcasts(stream)
  if block_given?
    new_messages = new_broadcasts_from(new_messages, stream, "assert_broadcast_on", &block)
  end

  message = new_messages.find { |msg| ActiveSupport::JSON.decode(msg) == serialized_msg }

  error_message = "No messages sent with #{data} to #{stream}"

  if new_messages.any?
    error_message = new_messages.inject("#{error_message}\nMessage(s) found:\n") do |error_message, new_message|
      error_message + "#{ActiveSupport::JSON.decode(new_message)}\n"
    end
  else
    error_message = "#{error_message}\nNo message found for #{stream}"
  end

  assert message, error_message
end
```

    
  

    
      
  
### 
  
    #**assert_broadcasts**(stream, number, &block)  ⇒ Object 
  

  

  

  
    

Asserts that the number of broadcasted messages to the stream matches the given number.

```
def test_broadcasts
  assert_broadcasts 'messages', 0
  ActionCable.server.broadcast 'messages', { text: 'hello' }
  assert_broadcasts 'messages', 1
  ActionCable.server.broadcast 'messages', { text: 'world' }
  assert_broadcasts 'messages', 2
end

```

If a block is passed, that block should cause the specified number of messages to be broadcasted.

```
def test_broadcasts_again
  assert_broadcasts('messages', 1) do
    ActionCable.server.broadcast 'messages', { text: 'hello' }
  end

  assert_broadcasts('messages', 2) do
    ActionCable.server.broadcast 'messages', { text: 'hi' }
    ActionCable.server.broadcast 'messages', { text: 'how are you?' }
  end
end

```

  

  

  
    
      

```

48
49
50
51
52
53
54
55
56
57
58
```

    
    
      

```
# File 'lib/action_cable/test_helper.rb', line 48

def assert_broadcasts(stream, number, &block)
  if block_given?
    new_messages = new_broadcasts_from(broadcasts(stream), stream, "assert_broadcasts", &block)

    actual_count = new_messages.size
    assert_equal number, actual_count, "#{number} broadcasts to #{stream} expected, but #{actual_count} were sent"
  else
    actual_count = broadcasts(stream).size
    assert_equal number, actual_count, "#{number} broadcasts to #{stream} expected, but #{actual_count} were sent"
  end
end
```

    
  

    
      
  
### 
  
    #**assert_no_broadcasts**(stream, &block)  ⇒ Object 
  

  

  

  
    

Asserts that no messages have been sent to the stream.

```
def test_no_broadcasts
  assert_no_broadcasts 'messages'
  ActionCable.server.broadcast 'messages', { text: 'hi' }
  assert_broadcasts 'messages', 1
end

```

If a block is passed, that block should not cause any message to be sent.

```
def test_broadcasts_again
  assert_no_broadcasts 'messages' do
    # No job messages should be sent from this block
  end
end

```

Note: This assertion is simply a shortcut for:

```
assert_broadcasts 'messages', 0, &block

```

  

  

  
    
      

```

80
81
82
```

    
    
      

```
# File 'lib/action_cable/test_helper.rb', line 80

def assert_no_broadcasts(stream, &block)
  assert_broadcasts stream, 0, &block
end
```

    
  

    
      
  
### 
  
    #**before_setup**  ⇒ Object 
  

  

  

  
    

:nodoc:

  

  

  
    
      

```

8
9
10
11
12
13
14
15
16
```

    
    
      

```
# File 'lib/action_cable/test_helper.rb', line 8

def before_setup # :nodoc:
  server = ActionCable.server
  test_adapter = ActionCable::SubscriptionAdapter::Test.new(server)

  @old_pubsub_adapter = server.pubsub

  server.instance_variable_set(:@pubsub, test_adapter)
  super
end
```

    
  

    
      
  
### 
  
    #**capture_broadcasts**(stream, &block)  ⇒ Object 
  

  

  

  
    

Returns the messages that are broadcasted in the block.

```
def test_broadcasts
  messages = capture_broadcasts('messages') do
    ActionCable.server.broadcast 'messages', { text: 'hi' }
    ActionCable.server.broadcast 'messages', { text: 'how are you?' }
  end
  assert_equal 2, messages.length
  assert_equal({ text: 'hi' }, messages.first)
  assert_equal({ text: 'how are you?' }, messages.last)
end

```

  

  

  
    
      

```

96
97
98
```

    
    
      

```
# File 'lib/action_cable/test_helper.rb', line 96

def capture_broadcasts(stream, &block)
  new_broadcasts_from(broadcasts(stream), stream, "capture_broadcasts", &block).map { |m| ActiveSupport::JSON.decode(m) }
end
```

    
  

    
      
  
### 
  
    #**pubsub_adapter**  ⇒ Object 
  

  

  

  
    

:nodoc:

  

  

  
    
      

```

142
143
144
```

    
    
      

```
# File 'lib/action_cable/test_helper.rb', line 142

def pubsub_adapter # :nodoc:
  ActionCable.server.pubsub
end
```