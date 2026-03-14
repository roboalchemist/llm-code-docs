# Module: ActionCable::Connection::Assertions
  
  
  

  

  
  
  
  
  

  
  
    Included in:
    TestCase::Behavior
  
  

  
  
    Defined in:
    lib/action_cable/connection/test_case.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**assert_reject_connection**(&block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Asserts that the connection is rejected (via `reject_unauthorized_connection`).

  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**assert_reject_connection**(&block)  ⇒ Object 
  

  

  

  
    

Asserts that the connection is rejected (via `reject_unauthorized_connection`).

```
# Asserts that connection without user_id fails
assert_reject_connection { connect params: { user_id: '' } }

```

  

  

  
    
      

```

28
29
30
```

    
    
      

```
# File 'lib/action_cable/connection/test_case.rb', line 28

def assert_reject_connection(&block)
  assert_raises(Authorization::UnauthorizedError, "Expected to reject connection but no rejection was made", &block)
end
```