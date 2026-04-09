# Module: Dry::Validation::Hints::ResultExtensions
  
    Included in:
    Result
  
  

  
  
    Defined in:
    lib/dry/validation/extensions/hints.rb
  
## Overview

Hints extensions for Result

API:

-

public

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**errors**(new_options = EMPTY_HASH)  ⇒ MessageSet 
    

    
  
  
  
  
  
  
  
  

  
    

Return error messages excluding hints.

-
  
      #**hints**(new_options = EMPTY_HASH)  ⇒ MessageSet 

Return hint messages.

-
  
      #**messages**(new_options = EMPTY_HASH)  ⇒ MessageSet 

Return errors and hints.

## Instance Method Details

###
  
    #**errors**(new_options = EMPTY_HASH)  ⇒ MessageSet 
  

  

  

  
    

Return error messages excluding hints

Parameters:

-

        *(defaults to: EMPTY_HASH)*

Options Hash (new_options):

-
          :locale
          (Symbol)
          
            
          
          
            — 

Set locale for messages

-
          :hints
          (Boolean)
          
            
          
          
            — 

Enable/disable hints

-
          :full
          (Boolean)
          
            
          
          
            — 

Get messages that include key names

Returns:

-

API:

-

public

```

34
35
36
37
```

```
# File 'lib/dry/validation/extensions/hints.rb', line 34

def errors(new_options = EMPTY_HASH)
  opts = new_options.merge(hints: false)
  @errors.with(schema_errors(opts), opts)
end

```

###
  
    #**hints**(new_options = EMPTY_HASH)  ⇒ MessageSet 
  

  

  

  
    

Return hint messages

Parameters:

-

        *(defaults to: EMPTY_HASH)*

Options Hash (new_options):

-
          :locale
          (Symbol)
          
            
          
          
            — 

Set locale for messages

-
          :hints
          (Boolean)
          
            
          
          
            — 

Enable/disable hints

-
          :full
          (Boolean)
          
            
          
          
            — 

Get messages that include key names

Returns:

-

API:

-

public

```

57
58
59
```

```
# File 'lib/dry/validation/extensions/hints.rb', line 57

def hints(new_options = EMPTY_HASH)
  schema_result.hints(new_options)
end

```

###
  
    #**messages**(new_options = EMPTY_HASH)  ⇒ MessageSet 
  

  

  

  
    

Return errors and hints

Parameters:

-

        *(defaults to: EMPTY_HASH)*

Options Hash (new_options):

-
          :locale
          (Symbol)
          
            
          
          
            — 

Set locale for messages

-
          :hints
          (Boolean)
          
            
          
          
            — 

Enable/disable hints

-
          :full
          (Boolean)
          
            
          
          
            — 

Get messages that include key names

Returns:

-

API:

-

public

```

46
47
48
```

```
# File 'lib/dry/validation/extensions/hints.rb', line 46

def messages(new_options = EMPTY_HASH)
  errors.with(hints(new_options).to_a, options.merge(**new_options))
end

```
