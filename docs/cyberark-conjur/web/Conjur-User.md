# Class: Conjur::User
  
    Inherits:
    
      BaseObject
      
        

          
- Object

- BaseObject

- Conjur::User

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      ActsAsUser
  
    Defined in:
    lib/conjur/user.rb
  
## Overview

A Conjur User.

## Instance Attribute Summary

### Attributes inherited from BaseObject

# credentials, #id

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**uidnumber**  ⇒ Fixnum 
    

    
  
  
  
  
  
  
  
  

  
    

Get the user's uidnumber, which can be used by LDAP and SSH login, among other things.

### Methods included from ActsAsUser

# api, #api_key, #rotate_api_key

### Methods inherited from BaseObject

# account, #as_json, #identifier, #initialize, #inspect, #kind, #username

### Methods included from Routing

# parser_for, #url_for

### Methods included from BuildObject

# build_object

### Methods included from LogSource

# log

## Constructor Details

This class inherits a constructor from Conjur::BaseObject
  
## Instance Method Details

###
  
    #**uidnumber**  ⇒ Fixnum 
  

  

  

  
    

Get the user's uidnumber, which can be used by LDAP and SSH login, among other things.

Returns:

-

        (Fixnum)

        —
        

the uidnumber

Raises:

-

        (RestClient::Forbidden)

        —
        

if you don't have permission to `show` the user.

```

30
31
32
```

```
# File 'lib/conjur/user.rb', line 30

def uidnumber
  parser_for(:user_uidnumber, user_attributes)
end
```
