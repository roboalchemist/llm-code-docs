# Module: ActionCable::Channel::Callbacks::ClassMethods
  
  
  

  

  
  
  
  
  

  

  
  
    Defined in:
    lib/action_cable/channel/callbacks.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**after_subscribe**(*methods, &block)  ⇒ Object 
    

    
      (also: #on_subscribe)
    
  
  
  
  
  
  
  
  

  
    

This callback will be triggered after the Base#subscribed method is called, even if the subscription was rejected with the Base#reject method.

  

      
        
- 
  
    
      #**after_unsubscribe**(*methods, &block)  ⇒ Object 
    

    
      (also: #on_unsubscribe)
    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**before_subscribe**(*methods, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**before_unsubscribe**(*methods, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**after_subscribe**(*methods, &block)  ⇒ Object 
  

  
    Also known as:
    on_subscribe
    
  

  

  
    

This callback will be triggered after the Base#subscribed method is called, even if the subscription was rejected with the Base#reject method.

To trigger the callback only on successful subscriptions, use the Base#subscription_rejected? method:

```
after_subscribe :my_method, unless: :subscription_rejected?

```

  

  

  
    
      

```

62
63
64
```

    
    
      

```
# File 'lib/action_cable/channel/callbacks.rb', line 62

def after_subscribe(*methods, &block)
  set_callback(:subscribe, :after, *methods, &block)
end
```

    
  

    
      
  
### 
  
    #**after_unsubscribe**(*methods, &block)  ⇒ Object 
  

  
    Also known as:
    on_unsubscribe
    
  

  

  
    
      

```

71
72
73
```

    
    
      

```
# File 'lib/action_cable/channel/callbacks.rb', line 71

def after_unsubscribe(*methods, &block)
  set_callback(:unsubscribe, :after, *methods, &block)
end
```

    
  

    
      
  
### 
  
    #**before_subscribe**(*methods, &block)  ⇒ Object 
  

  

  

  
    
      

```

50
51
52
```

    
    
      

```
# File 'lib/action_cable/channel/callbacks.rb', line 50

def before_subscribe(*methods, &block)
  set_callback(:subscribe, :before, *methods, &block)
end
```

    
  

    
      
  
### 
  
    #**before_unsubscribe**(*methods, &block)  ⇒ Object 
  

  

  

  
    
      

```

67
68
69
```

    
    
      

```
# File 'lib/action_cable/channel/callbacks.rb', line 67

def before_unsubscribe(*methods, &block)
  set_callback(:unsubscribe, :before, *methods, &block)
end
```