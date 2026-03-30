# Class: Capybara::Queries::AncestorQuery
  
  
  Private

  
  
    Inherits:
    
      SelectorQuery
      
        

          
- Object
          
            
- BaseQuery
          
            
- SelectorQuery
          
            
- Capybara::Queries::AncestorQuery
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/capybara/queries/ancestor_query.rb
  
  

  
    

  **This class is part of a private API.**
  You should avoid using this class if possible, as it may be removed or be changed in the future.

  

  

  
## Constant Summary

  
  
### Constants inherited
     from SelectorQuery

  

SelectorQuery::SPATIAL_KEYS, SelectorQuery::VALID_KEYS, SelectorQuery::VALID_MATCH

  
  
  
### Constants inherited
     from BaseQuery

  

BaseQuery::COUNT_KEYS

  
## Instance Attribute Summary

  
  
### Attributes inherited from SelectorQuery

  

#expression, #locator, #options, #selector

  
  
  
### Attributes inherited from BaseQuery

  

#options, #session_options

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**description**(applied = false)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  private

  
    

rubocop:disable Style/OptionalBooleanParameter.

  

      
        
- 
  
    
      #**resolve_for**(node, exact = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  private

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from SelectorQuery

  

#applied_description, #css, #exact?, #failure_message, #initialize, #label, #match, #matches_filters?, #name, #negative_failure_message, #supports_exact?, #visible, #xpath

  
  
  
  
  
  
  
  
  
### Methods inherited from BaseQuery

  

#expects_none?, #failure_message, #initialize, #matches_count?, #negative_failure_message, #wait, wait

  
## Constructor Details

  
    

This class inherits a constructor from Capybara::Queries::SelectorQuery
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**description**(applied = false)  ⇒ Object 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

rubocop:disable Style/OptionalBooleanParameter

  

  

  
    
      

```

20
21
22
23
24
25
```

    
    
      

```
# File 'lib/capybara/queries/ancestor_query.rb', line 20

def description(applied = false) # rubocop:disable Style/OptionalBooleanParameter
  child_query = @child_node&.instance_variable_get(:@query)
  desc = super
  desc += " that is an ancestor of #{child_query.description}" if child_query
  desc
end
```

    
  

    
      
  
### 
  
    #**resolve_for**(node, exact = nil)  ⇒ Object 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

  

  

  
    
      

```

7
8
9
10
11
12
13
14
15
16
17
18
```

    
    
      

```
# File 'lib/capybara/queries/ancestor_query.rb', line 7

def resolve_for(node, exact = nil)
  @child_node = node

  node.synchronize do
    scope = node.respond_to?(:session) ? node.session.current_scope : node.find(:xpath, '/*')
    match_results = super(scope, exact)
    ancestors = node.find_xpath(XPath.ancestor.to_s)
                    .map(&method(:to_element))
                    .select { |el| match_results.include?(el) }
    Capybara::Result.new(ordered_results(ancestors), self)
  end
end
```