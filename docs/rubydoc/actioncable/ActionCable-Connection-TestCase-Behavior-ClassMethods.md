# Module: ActionCable::Connection::TestCase::Behavior::ClassMethods
  
  
  

  

  
  
  
  
  

  

  
  
    Defined in:
    lib/action_cable/connection/test_case.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**connection_class**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**determine_default_connection**(name)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**tests**(connection)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**connection_class**  ⇒ Object 
  

  

  

  
    
      

```

167
168
169
170
171
172
173
```

    
    
      

```
# File 'lib/action_cable/connection/test_case.rb', line 167

def connection_class
  if connection = self._connection_class
    connection
  else
    tests determine_default_connection(name)
  end
end
```

    
  

    
      
  
### 
  
    #**determine_default_connection**(name)  ⇒ Object 
  

  

  

  
    

  

  

Raises:

  
    
- 
      
      
        (NonInferrableConnectionError)
      
      
      
    
  

  
    
      

```

175
176
177
178
179
180
181
```

    
    
      

```
# File 'lib/action_cable/connection/test_case.rb', line 175

def determine_default_connection(name)
  connection = determine_constant_from_test_name(name) do |constant|
    Class === constant && constant < ActionCable::Connection::Base
  end
  raise NonInferrableConnectionError.new(name) if connection.nil?
  connection
end
```

    
  

    
      
  
### 
  
    #**tests**(connection)  ⇒ Object 
  

  

  

  
    
      

```

156
157
158
159
160
161
162
163
164
165
```

    
    
      

```
# File 'lib/action_cable/connection/test_case.rb', line 156

def tests(connection)
  case connection
  when String, Symbol
    self._connection_class = connection.to_s.camelize.constantize
  when Module
    self._connection_class = connection
  else
    raise NonInferrableConnectionError.new(connection)
  end
end
```