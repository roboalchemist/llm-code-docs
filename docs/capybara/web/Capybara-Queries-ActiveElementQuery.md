# Class: Capybara::Queries::ActiveElementQuery
  
  
  Private

  
  
    Inherits:
    
      BaseQuery
      
        

          
- Object
          
            
- BaseQuery
          
            
- Capybara::Queries::ActiveElementQuery
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/capybara/queries/active_element_query.rb
  
  

  
    

  **This class is part of a private API.**
  You should avoid using this class if possible, as it may be removed or be changed in the future.

  

  

  
## Constant Summary

  
  
### Constants inherited
     from BaseQuery

  

BaseQuery::COUNT_KEYS

  
## Instance Attribute Summary

  
  
### Attributes inherited from BaseQuery

  

#options, #session_options

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**initialize**(**options)  ⇒ ActiveElementQuery 
    

    
  
  
  
    constructor
  
  
  
  
  
  private

  
    

A new instance of ActiveElementQuery.

  

      
        
- 
  
    
      #**resolve_for**(session)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  private

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from BaseQuery

  

#expects_none?, #failure_message, #matches_count?, #negative_failure_message, wait, #wait

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(**options)  ⇒ ActiveElementQuery 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Returns a new instance of ActiveElementQuery.

  

  

  
    
      

```

7
8
9
10
```

    
    
      

```
# File 'lib/capybara/queries/active_element_query.rb', line 7

def initialize(**options)
  @options = options
  super(@options)
end
```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**resolve_for**(session)  ⇒ Object 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

  

  

  
    
      

```

12
13
14
15
```

    
    
      

```
# File 'lib/capybara/queries/active_element_query.rb', line 12

def resolve_for(session)
  node = session.driver.active_element
  [Capybara::Node::Element.new(session, node, nil, self)]
end
```