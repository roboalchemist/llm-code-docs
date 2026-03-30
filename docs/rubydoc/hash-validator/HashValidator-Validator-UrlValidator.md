# Class: HashValidator::Validator::UrlValidator
  
  
  

  
  
    Inherits:
    
      Base
      
        

          
- Object
          
            
- Base
          
            
- HashValidator::Validator::UrlValidator
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/hash_validator/validators/url_validator.rb
  
  

  
## Instance Attribute Summary

  
  
### Attributes inherited from Base

  

#name

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**error_message**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**  ⇒ UrlValidator 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of UrlValidator.

  

      
        
- 
  
    
      #**valid?**(value)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from Base

  

#should_validate?, #validate

  
## Constructor Details

  
    
  
### 
  
    #**initialize**  ⇒ UrlValidator 
  

  

  

  
    

Returns a new instance of UrlValidator.

  

  

  
    
      

```

6
7
8
```

    
    
      

```
# File 'lib/hash_validator/validators/url_validator.rb', line 6

def initialize
  super("url")  # The name of the validator
end
```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**error_message**  ⇒ Object 
  

  

  

  
    
      

```

10
11
12
```

    
    
      

```
# File 'lib/hash_validator/validators/url_validator.rb', line 10

def error_message
  "is not a valid URL"
end
```

    
  

    
      
  
### 
  
    #**valid?**(value)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

14
15
16
17
18
19
20
```

    
    
      

```
# File 'lib/hash_validator/validators/url_validator.rb', line 14

def valid?(value)
  return false unless value.is_a?(String)
  uri = URI.parse(value)
  %w[http https ftp].include?(uri.scheme)
rescue URI::InvalidURIError
  false
end
```