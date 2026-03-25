# Class: Conjur::API::LocalAuthenticator
  
    Inherits:
    
      Object
      
        

          
- Object

- Conjur::API::LocalAuthenticator

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      TokenExpiration
  
    Defined in:
    lib/conjur/base.rb
  
## Overview

Obtains access tokens from the +authn-local+ service.

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
  
      #**cidr**  ⇒ Object 

      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute cidr.

-
  
      #**expiration**  ⇒ Object 

      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute expiration.

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
  
      #**initialize**(account, username, expiration, cidr)  ⇒ LocalAuthenticator 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of LocalAuthenticator.

-
  
      #**refresh_token**  ⇒ Object 

### Methods included from TokenExpiration

# gettime, #needs_token_refresh?, #token_age, #update_token_born

## Constructor Details

###
  
    #**initialize**(account, username, expiration, cidr)  ⇒ LocalAuthenticator 
  

  

  

  
    

Returns a new instance of LocalAuthenticator.

```

235
236
237
238
239
240
241
242
```

```
# File 'lib/conjur/base.rb', line 235

def initialize account, username, expiration, cidr
  @account = account
  @username = username
  @expiration = expiration
  @cidr = cidr

  update_token_born
end

```

## Instance Attribute Details

###
  
    #**account**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute account.

```

233
234
235
```

```
# File 'lib/conjur/base.rb', line 233

def account
  @account
end

```

###
  
    #**cidr**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute cidr.

```

233
234
235
```

```
# File 'lib/conjur/base.rb', line 233

def cidr
  @cidr
end

```

###
  
    #**expiration**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute expiration.

```

233
234
235
```

```
# File 'lib/conjur/base.rb', line 233

def expiration
  @expiration
end

```

###
  
    #**username**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute username.

```

233
234
235
```

```
# File 'lib/conjur/base.rb', line 233

def username
  @username
end

```

## Instance Method Details

###
  
    #**refresh_token**  ⇒ Object 
  

  

  

  
    
      

```

244
245
246
247
248
```

```
# File 'lib/conjur/base.rb', line 244

def refresh_token
  Conjur::API.authenticate_local(username, account: account, expiration: expiration, cidr: cidr).tap do
    update_token_born
  end
end

```
