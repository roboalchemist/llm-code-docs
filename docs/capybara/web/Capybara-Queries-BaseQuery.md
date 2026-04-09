# Class: Capybara::Queries::BaseQuery
  
  
  Private

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Capybara::Queries::BaseQuery
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/capybara/queries/base_query.rb
  
  

  
    

  **This class is part of a private API.**
  You should avoid using this class if possible, as it may be removed or be changed in the future.

  

  

  
## Direct Known Subclasses

  

ActiveElementQuery, CurrentPathQuery, SelectorQuery, StyleQuery, TextQuery, TitleQuery

  
    
## 
      Constant Summary
      collapse
    

    
      
        COUNT_KEYS =
          
  
    

  **This constant is part of a private API.**
  You should avoid using this constant if possible, as it may be removed or be changed in the future.

  

  

        
        

```
%i[count minimum maximum between].freeze
```

      
    
  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**options**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  private

  
    
  

    
      
- 
  
    
      #**session_options**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  private

  
    
  

    
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**wait**(options, default = Capybara.default_max_wait_time)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  private

  
    
  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**expects_none?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  private

  
    

Checks if a count of 0 is valid for the query Returns false if query does not have any count options specified.

  

      
        
- 
  
    
      #**failure_message**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  private

  
    

Generates a failure message from the query description and count options.

  

      
        
- 
  
    
      #**initialize**(options)  ⇒ BaseQuery 
    

    
  
  
  
    constructor
  
  
  
  
  
  private

  
    

A new instance of BaseQuery.

  

      
        
- 
  
    
      #**matches_count?**(count)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  private

  
    

Checks if the given count matches the query count options.

  

      
        
- 
  
    
      #**negative_failure_message**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  private

  
    
  

      
        
- 
  
    
      #**wait**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  private

  
    
  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(options)  ⇒ BaseQuery 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Returns a new instance of BaseQuery.

  

  

  
    
      

```

12
13
14
```

    
    
      

```
# File 'lib/capybara/queries/base_query.rb', line 12

def initialize(options)
  @session_options = options.delete(:session_options)
end
```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**options**  ⇒ Object  (readonly)
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

  

  

  
    
      

```

9
10
11
```

    
    
      

```
# File 'lib/capybara/queries/base_query.rb', line 9

def options
  @options
end
```

    
  

    
      
      
      
  
### 
  
    #**session_options**  ⇒ Object 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

  

  

  
    
      

```

16
17
18
```

    
    
      

```
# File 'lib/capybara/queries/base_query.rb', line 16

def session_options
  @session_options || Capybara.session_options
end
```

    
  

    
  

  
    
## Class Method Details

    
      
  
### 
  
    .**wait**(options, default = Capybara.default_max_wait_time)  ⇒ Object 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

  

  

  
    
      

```

24
25
26
27
28
29
```

    
    
      

```
# File 'lib/capybara/queries/base_query.rb', line 24

def self.wait(options, default = Capybara.default_max_wait_time)
  # if no value or nil for the :wait option is passed it should default to the default
  wait = options.fetch(:wait, nil)
  wait = default if wait.nil?
  wait || 0
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**expects_none?**  ⇒ Boolean 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Checks if a count of 0 is valid for the query
Returns false if query does not have any count options specified.

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

36
37
38
```

    
    
      

```
# File 'lib/capybara/queries/base_query.rb', line 36

def expects_none?
  count_specified? ? matches_count?(0) : false
end
```

    
  

    
      
  
### 
  
    #**failure_message**  ⇒ Object 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Generates a failure message from the query description and count options.

  

  

  
    
      

```

62
63
64
```

    
    
      

```
# File 'lib/capybara/queries/base_query.rb', line 62

def failure_message
  +"expected to find #{description}" << count_message
end
```

    
  

    
      
  
### 
  
    #**matches_count?**(count)  ⇒ Boolean 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Checks if the given count matches the query count options.
Defaults to true if no count options are specified. If multiple
count options exist, it tests that all conditions are met;
however, if :count is specified, all other options are ignored.

  

  

Parameters:

  
    
- 
      
        count
      
      
        (Integer)
      
      
      
        —
        

The actual number. Should be coercible via Integer()

      
    
  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

49
50
51
52
53
54
55
56
```

    
    
      

```
# File 'lib/capybara/queries/base_query.rb', line 49

def matches_count?(count)
  return (Integer(options[:count]) == count) if options[:count]
  return false if options[:maximum] && (Integer(options[:maximum]) < count)
  return false if options[:minimum] && (Integer(options[:minimum]) > count)
  return false if options[:between] && !options[:between].include?(count)

  true
end
```

    
  

    
      
  
### 
  
    #**negative_failure_message**  ⇒ Object 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

  

  

  
    
      

```

66
67
68
```

    
    
      

```
# File 'lib/capybara/queries/base_query.rb', line 66

def negative_failure_message
  +"expected not to find #{description}" << count_message
end
```

    
  

    
      
  
### 
  
    #**wait**  ⇒ Object 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

  

  

  
    
      

```

20
21
22
```

    
    
      

```
# File 'lib/capybara/queries/base_query.rb', line 20

def wait
  self.class.wait(options, session_options.default_max_wait_time)
end
```