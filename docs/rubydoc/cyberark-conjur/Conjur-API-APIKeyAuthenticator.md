# Class: Conjur::API::APIKeyAuthenticator
  
    Inherits:
    
      Object
      
        

          
- Object

- Conjur::API::APIKeyAuthenticator

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      TokenExpiration
  
    Defined in:
    lib/conjur/base.rb
  
## Overview

When the API is constructed with an API key, the token can be refreshed using
the username and API key. This authenticator assumes that the token was
minted immediately before the API instance was created.

## Constant Summary

### Constants included

     from TokenExpiration

TokenExpiration::TOKEN_STALE

## Instance Attribute Summary collapse

-
  
      #**account**  ⇒ Object 

      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute account.

-
  
      #**api_key**  ⇒ Object 

      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute api_key.

-
  
      #**username**  ⇒ Object 

      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute username.

### Attributes included from TokenExpiration

# token_born

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**initialize**(account, username, api_key)  ⇒ APIKeyAuthenticator 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of APIKeyAuthenticator.

-
  
      #**refresh_token**  ⇒ Object 

### Methods included from TokenExpiration

# gettime, #needs_token_refresh?, #token_age, #update_token_born

## Constructor Details

###
  
    #**initialize**(account, username, api_key)  ⇒ APIKeyAuthenticator 
  

  

  

  
    

Returns a new instance of APIKeyAuthenticator.

```

214
215
216
217
218
219
220
```

```
# File 'lib/conjur/base.rb', line 214

def initialize account, username, api_key
  @account = account
  @username = username
  @api_key = api_key

  update_token_born
end
```

## Instance Attribute Details

###
  
    #**account**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute account.

```

212
213
214
```

```
# File 'lib/conjur/base.rb', line 212

def account
  @account
end
```

###
  
    #**api_key**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute api_key.

```

212
213
214
```

```
# File 'lib/conjur/base.rb', line 212

def api_key
  @api_key
end
```

###
  
    #**username**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute username.

```

212
213
214
```

```
# File 'lib/conjur/base.rb', line 212

def username
  @username
end
```

## Instance Method Details

###
  
    #**refresh_token**  ⇒ Object 
  

  

  

  
    
      

```

222
223
224
225
226
```

```
# File 'lib/conjur/base.rb', line 222

def refresh_token
  Conjur::API.authenticate(username, api_key, account: account).tap do
    update_token_born
  end
end
```
