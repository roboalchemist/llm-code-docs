# Module: ActionCable::Channel::TestCase::Behavior::ClassMethods
  
  
  

  

  
  
  
  
  

  

  
  
    Defined in:
    lib/action_cable/channel/test_case.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**channel_class**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**determine_default_channel**(name)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**tests**(channel)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**channel_class**  ⇒ Object 
  

  

  

  
    
      

```

219
220
221
222
223
224
225
```

    
    
      

```
# File 'lib/action_cable/channel/test_case.rb', line 219

def channel_class
  if channel = self._channel_class
    channel
  else
    tests determine_default_channel(name)
  end
end
```

    
  

    
      
  
### 
  
    #**determine_default_channel**(name)  ⇒ Object 
  

  

  

  
    

  

  

Raises:

  
    
- 
      
      
        (NonInferrableChannelError)
      
      
      
    
  

  
    
      

```

227
228
229
230
231
232
233
```

    
    
      

```
# File 'lib/action_cable/channel/test_case.rb', line 227

def determine_default_channel(name)
  channel = determine_constant_from_test_name(name) do |constant|
    Class === constant && constant < ActionCable::Channel::Base
  end
  raise NonInferrableChannelError.new(name) if channel.nil?
  channel
end
```

    
  

    
      
  
### 
  
    #**tests**(channel)  ⇒ Object 
  

  

  

  
    
      

```

208
209
210
211
212
213
214
215
216
217
```

    
    
      

```
# File 'lib/action_cable/channel/test_case.rb', line 208

def tests(channel)
  case channel
  when String, Symbol
    self._channel_class = channel.to_s.camelize.constantize
  when Module
    self._channel_class = channel
  else
    raise NonInferrableChannelError.new(channel)
  end
end
```