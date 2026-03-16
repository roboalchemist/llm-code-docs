# Class: Capybara::RSpecMatchers::Matchers::Base
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Capybara::RSpecMatchers::Matchers::Base
          
        

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      Compound
  
  
  

  

  
  
    Defined in:
    lib/capybara/rspec/matchers/base.rb
  
  

  
## Direct Known Subclasses

  

WrappedElementMatcher

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**failure_message**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute failure_message.

  

    
      
- 
  
    
      #**failure_message_when_negated**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute failure_message_when_negated.

  

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**initialize**(*args, **kw_args, &filter_block)  ⇒ Base 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Base.

  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods included from Compound

  

#and, #and_then, #or

  
  
## Constructor Details

  
    
  
### 
  
    #**initialize**(*args, **kw_args, &filter_block)  ⇒ Base 
  

  

  

  
    

Returns a new instance of Base.

  

  

  
    
      

```

15
16
17
18
19
```

    
    
      

```
# File 'lib/capybara/rspec/matchers/base.rb', line 15

def initialize(*args, **kw_args, &filter_block)
  @args = args.dup
  @kw_args = kw_args || {}
  @filter_block = filter_block
end
```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**failure_message**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute failure_message.

  

  

  
    
      

```

13
14
15
```

    
    
      

```
# File 'lib/capybara/rspec/matchers/base.rb', line 13

def failure_message
  @failure_message
end
```

    
  

    
      
      
      
  
### 
  
    #**failure_message_when_negated**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute failure_message_when_negated.

  

  

  
    
      

```

13
14
15
```

    
    
      

```
# File 'lib/capybara/rspec/matchers/base.rb', line 13

def failure_message_when_negated
  @failure_message_when_negated
end
```