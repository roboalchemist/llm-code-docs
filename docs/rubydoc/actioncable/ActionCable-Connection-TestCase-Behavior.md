# Module: ActionCable::Connection::TestCase::Behavior
  
  
  

  

  
  
  
      Extended by:
      ActiveSupport::Concern
  
  
  
  
  
      Includes:
      Assertions, ActiveSupport::Testing::ConstantLookup
  
  
  

  
  
    Included in:
    ActionCable::Connection::TestCase
  
  

  
  
    Defined in:
    lib/action_cable/connection/test_case.rb
  
  

## Defined Under Namespace

  
    
      **Modules:** ClassMethods
    
  
    
  

  
    
## 
      Constant Summary
      collapse
    

    
      
        DEFAULT_PATH =
          
        
        

```
"/cable"
```

      
    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**connect**(path = ActionCable.server.config.mount_path, **request_params)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Performs connection attempt to exert #connect on the connection under test.

  

      
        
- 
  
    
      #**cookies**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**disconnect**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Exert #disconnect on the connection under test.

  

      
    

  

  
  
  
  
  
  
  
  
  
  
### Methods included from Assertions

  

#assert_reject_connection

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**connect**(path = ActionCable.server.config.mount_path, **request_params)  ⇒ Object 
  

  

  

  
    

Performs connection attempt to exert #connect on the connection under test.

Accepts request path as the first argument and the following request options:

- 

params – URL parameters (Hash)

- 

headers – request headers (Hash)

- 

session – session data (Hash)

- 

env – additional Rack env configuration (Hash)

  

  

  
    
      

```

192
193
194
195
196
197
198
199
200
201
202
```

    
    
      

```
# File 'lib/action_cable/connection/test_case.rb', line 192

def connect(path = ActionCable.server.config.mount_path, **request_params)
  path ||= DEFAULT_PATH

  connection = self.class.connection_class.allocate
  connection.singleton_class.include(TestConnection)
  connection.send(:initialize, build_test_request(path, **request_params))
  connection.connect if connection.respond_to?(:connect)

  # Only set instance variable if connected successfully
  @connection = connection
end
```

    
  

    
      
  
### 
  
    #**cookies**  ⇒ Object 
  

  

  

  
    
      

```

212
213
214
```

    
    
      

```
# File 'lib/action_cable/connection/test_case.rb', line 212

def cookies
  @cookie_jar ||= TestCookieJar.new
end
```

    
  

    
      
  
### 
  
    #**disconnect**  ⇒ Object 
  

  

  

  
    

Exert #disconnect on the connection under test.

  

  

  
    
      

```

205
206
207
208
209
210
```

    
    
      

```
# File 'lib/action_cable/connection/test_case.rb', line 205

def disconnect
  raise "Must be connected!" if connection.nil?

  connection.disconnect if connection.respond_to?(:disconnect)
  @connection = nil
end
```