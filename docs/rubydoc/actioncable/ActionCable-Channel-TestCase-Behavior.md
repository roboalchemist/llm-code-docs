# Module: ActionCable::Channel::TestCase::Behavior
  
  
  

  

  
  
  
      Extended by:
      ActiveSupport::Concern
  
  
  
  
  
      Includes:
      TestHelper, ActiveSupport::Testing::ConstantLookup
  
  
  

  
  
    Included in:
    ActionCable::Channel::TestCase
  
  

  
  
    Defined in:
    lib/action_cable/channel/test_case.rb
  
  

## Defined Under Namespace

  
    
      **Modules:** ClassMethods
    
  
    
  

  
    
## 
      Constant Summary
      collapse
    

    
      
        CHANNEL_IDENTIFIER =
          
        
        

```
"test_stub"
```

      
    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**assert_broadcast_on**(stream_or_object, *args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**assert_broadcasts**(stream_or_object, *args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Enhance TestHelper assertions to handle non-String broadcastings.

  

      
        
- 
  
    
      #**assert_has_no_stream**(stream)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Asserts that the specified stream has not been started.

  

      
        
- 
  
    
      #**assert_has_no_stream_for**(object)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Asserts that the specified stream for a model has not started.

  

      
        
- 
  
    
      #**assert_has_stream**(stream)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Asserts that the specified stream has been started.

  

      
        
- 
  
    
      #**assert_has_stream_for**(object)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Asserts that the specified stream for a model has started.

  

      
        
- 
  
    
      #**assert_no_streams**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Asserts that no streams have been started.

  

      
        
- 
  
    
      #**perform**(action, data = {})  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Perform action on a channel.

  

      
        
- 
  
    
      #**stub_connection**(identifiers = {})  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Set up test connection with the specified identifiers:.

  

      
        
- 
  
    
      #**subscribe**(params = {})  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Subscribe to the channel under test.

  

      
        
- 
  
    
      #**transmissions**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Returns messages transmitted into channel.

  

      
        
- 
  
    
      #**unsubscribe**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Unsubscribe the subscription under test.

  

      
    

  

  
  
  
  
  
  
  
  
  
  
### Methods included from TestHelper

  

#after_teardown, #assert_no_broadcasts, #before_setup, #capture_broadcasts, #pubsub_adapter

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**assert_broadcast_on**(stream_or_object, *args)  ⇒ Object 
  

  

  

  
    
      

```

282
283
284
```

    
    
      

```
# File 'lib/action_cable/channel/test_case.rb', line 282

def assert_broadcast_on(stream_or_object, *args)
  super(broadcasting_for(stream_or_object), *args)
end
```

    
  

    
      
  
### 
  
    #**assert_broadcasts**(stream_or_object, *args)  ⇒ Object 
  

  

  

  
    

Enhance TestHelper assertions to handle non-String broadcastings

  

  

  
    
      

```

278
279
280
```

    
    
      

```
# File 'lib/action_cable/channel/test_case.rb', line 278

def assert_broadcasts(stream_or_object, *args)
  super(broadcasting_for(stream_or_object), *args)
end
```

    
  

    
      
  
### 
  
    #**assert_has_no_stream**(stream)  ⇒ Object 
  

  

  

  
    

Asserts that the specified stream has not been started.

```
def test_assert_no_started_stream
  subscribe
  assert_has_no_stream 'messages'
end

```

  

  

  
    
      

```

326
327
328
```

    
    
      

```
# File 'lib/action_cable/channel/test_case.rb', line 326

def assert_has_no_stream(stream)
  assert subscription.streams.exclude?(stream), "Stream #{stream} has been started"
end
```

    
  

    
      
  
### 
  
    #**assert_has_no_stream_for**(object)  ⇒ Object 
  

  

  

  
    

Asserts that the specified stream for a model has not started.

```
def test_assert_no_started_stream_for
  subscribe id: 41
  assert_has_no_stream_for User.find(42)
end

```

  

  

  
    
      

```

337
338
339
```

    
    
      

```
# File 'lib/action_cable/channel/test_case.rb', line 337

def assert_has_no_stream_for(object)
  assert_has_no_stream(broadcasting_for(object))
end
```

    
  

    
      
  
### 
  
    #**assert_has_stream**(stream)  ⇒ Object 
  

  

  

  
    

Asserts that the specified stream has been started.

```
def test_assert_started_stream
  subscribe
  assert_has_stream 'messages'
end

```

  

  

  
    
      

```

304
305
306
```

    
    
      

```
# File 'lib/action_cable/channel/test_case.rb', line 304

def assert_has_stream(stream)
  assert subscription.streams.include?(stream), "Stream #{stream} has not been started"
end
```

    
  

    
      
  
### 
  
    #**assert_has_stream_for**(object)  ⇒ Object 
  

  

  

  
    

Asserts that the specified stream for a model has started.

```
def test_assert_started_stream_for
  subscribe id: 42
  assert_has_stream_for User.find(42)
end

```

  

  

  
    
      

```

315
316
317
```

    
    
      

```
# File 'lib/action_cable/channel/test_case.rb', line 315

def assert_has_stream_for(object)
  assert_has_stream(broadcasting_for(object))
end
```

    
  

    
      
  
### 
  
    #**assert_no_streams**  ⇒ Object 
  

  

  

  
    

Asserts that no streams have been started.

```
def test_assert_no_started_stream
  subscribe
  assert_no_streams
end

```

  

  

  
    
      

```

293
294
295
```

    
    
      

```
# File 'lib/action_cable/channel/test_case.rb', line 293

def assert_no_streams
  assert subscription.streams.empty?, "No streams started was expected, but #{subscription.streams.count} found"
end
```

    
  

    
      
  
### 
  
    #**perform**(action, data = {})  ⇒ Object 
  

  

  

  
    

Perform action on a channel.

NOTE: Must be subscribed.

  

  

  
    
      

```

266
267
268
269
```

    
    
      

```
# File 'lib/action_cable/channel/test_case.rb', line 266

def perform(action, data = {})
  check_subscribed!
  subscription.perform_action(data.stringify_keys.merge("action" => action.to_s))
end
```

    
  

    
      
  
### 
  
    #**stub_connection**(identifiers = {})  ⇒ Object 
  

  

  

  
    

Set up test connection with the specified identifiers:

```
class ApplicationCable < ActionCable::Connection::Base
  identified_by :user, :token
end

stub_connection(user: users[:john], token: 'my-secret-token')

```

  

  

  
    
      

```

243
244
245
```

    
    
      

```
# File 'lib/action_cable/channel/test_case.rb', line 243

def stub_connection(identifiers = {})
  @connection = ConnectionStub.new(identifiers)
end
```

    
  

    
      
  
### 
  
    #**subscribe**(params = {})  ⇒ Object 
  

  

  

  
    

Subscribe to the channel under test. Optionally pass subscription parameters as a Hash.

  

  

  
    
      

```

249
250
251
252
253
254
255
```

    
    
      

```
# File 'lib/action_cable/channel/test_case.rb', line 249

def subscribe(params = {})
  @connection ||= stub_connection
  @subscription = self.class.channel_class.new(connection, CHANNEL_IDENTIFIER, params.with_indifferent_access)
  @subscription.singleton_class.include(ChannelStub)
  @subscription.subscribe_to_channel
  @subscription
end
```

    
  

    
      
  
### 
  
    #**transmissions**  ⇒ Object 
  

  

  

  
    

Returns messages transmitted into channel

  

  

  
    
      

```

272
273
274
275
```

    
    
      

```
# File 'lib/action_cable/channel/test_case.rb', line 272

def transmissions
  # Return only directly sent message (via #transmit)
  connection.transmissions.filter_map { |data| data["message"] }
end
```

    
  

    
      
  
### 
  
    #**unsubscribe**  ⇒ Object 
  

  

  

  
    

Unsubscribe the subscription under test.

  

  

  
    
      

```

258
259
260
261
```

    
    
      

```
# File 'lib/action_cable/channel/test_case.rb', line 258

def unsubscribe
  check_subscribed!
  subscription.unsubscribe_from_channel
end
```