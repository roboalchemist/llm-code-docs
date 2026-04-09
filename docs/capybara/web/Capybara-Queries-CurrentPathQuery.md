# Class: Capybara::Queries::CurrentPathQuery
  
  
  Private

  
  
    Inherits:
    
      BaseQuery
      
        

          
- Object
          
            
- BaseQuery
          
            
- Capybara::Queries::CurrentPathQuery
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/capybara/queries/current_path_query.rb
  
  

  
    

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
  
    
      #**failure_message**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  private

  
    
  

      
        
- 
  
    
      #**initialize**(expected_path, **options, &optional_filter_block)  ⇒ CurrentPathQuery 
    

    
  
  
  
    constructor
  
  
  
  
  
  private

  
    

A new instance of CurrentPathQuery.

  

      
        
- 
  
    
      #**negative_failure_message**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  private

  
    
  

      
        
- 
  
    
      #**resolves_for?**(session)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  private

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from BaseQuery

  

#expects_none?, #matches_count?, wait, #wait

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(expected_path, **options, &optional_filter_block)  ⇒ CurrentPathQuery 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Returns a new instance of CurrentPathQuery.

  

  

  
    
      

```

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
# File 'lib/capybara/queries/current_path_query.rb', line 9

def initialize(expected_path, **options, &optional_filter_block)
  super(options)
  @expected_path = expected_path
  @options = {
    url: !@expected_path.is_a?(Regexp) && !::Addressable::URI.parse(@expected_path || '').hostname.nil?,
    ignore_query: false
  }.merge(options)
  @filter_block = optional_filter_block
  assert_valid_keys
end
```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**failure_message**  ⇒ Object 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

  

  

  
    
      

```

35
36
37
```

    
    
      

```
# File 'lib/capybara/queries/current_path_query.rb', line 35

def failure_message
  failure_message_helper
end
```

    
  

    
      
  
### 
  
    #**negative_failure_message**  ⇒ Object 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

  

  

  
    
      

```

39
40
41
```

    
    
      

```
# File 'lib/capybara/queries/current_path_query.rb', line 39

def negative_failure_message
  failure_message_helper(' not')
end
```

    
  

    
      
  
### 
  
    #**resolves_for?**(session)  ⇒ Boolean 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

20
21
22
23
24
25
26
27
28
29
30
31
32
33
```

    
    
      

```
# File 'lib/capybara/queries/current_path_query.rb', line 20

def resolves_for?(session)
  uri = ::Addressable::URI.parse(session.current_url)
  @actual_path = (options[:ignore_query] ? uri&.omit(:query) : uri).then do |u|
    options[:url] ? u&.to_s : u&.request_uri
  end

  res = if @expected_path.is_a? Regexp
    @actual_path.to_s.match?(@expected_path)
  else
    ::Addressable::URI.parse(@expected_path) == ::Addressable::URI.parse(@actual_path)
  end

  res && matches_filter_block?(uri)
end
```