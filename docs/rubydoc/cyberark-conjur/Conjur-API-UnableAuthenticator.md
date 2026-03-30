# Class: Conjur::API::UnableAuthenticator
  
    Inherits:
    
      Object
      
        

          
- Object

- Conjur::API::UnableAuthenticator

        show all
      

    Defined in:
    lib/conjur/base.rb
  
## Overview

When the API is constructed with a token, the token cannot be refreshed.

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**needs_token_refresh?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**refresh_token**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Method Details

###
  
    #**needs_token_refresh?**  ⇒ Boolean 
  

  

  

  
    

Returns:

-

        (Boolean)

```

257
258
259
```

```
# File 'lib/conjur/base.rb', line 257

def needs_token_refresh?
  false
end
```

###
  
    #**refresh_token**  ⇒ Object 
  

  

  

  
    
      

```

253
254
255
```

```
# File 'lib/conjur/base.rb', line 253

def refresh_token
  raise "Unable to re-authenticate using an access token"
end
```
