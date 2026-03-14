# Module: Conjur::ActsAsUser
  
    Included in:
    Host, User
  
  

  
  
    Defined in:
    lib/conjur/acts_as_user.rb
  
## Overview

This module provides methods for things that are like users (specifically, those that have
api keys).

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**api**  ⇒ Conjur::API 
    

    
  
  
  
  
  
  
  
  

  
    

Create an api logged in as this user-like thing.

-
  
      #**api_key**  ⇒ String 

Returns a newly created user's api_key.

-
  
      #**rotate_api_key**  ⇒ String 

Rotate this role's API key.

## Instance Method Details

###
  
    #**api**  ⇒ Conjur::API 
  

  

  

  
    
  
    **Note:**
    

As with #api_key, this method only works on newly created instances.

Create an api logged in as this user-like thing.

Returns:

-

        (Conjur::API)

        —
        

an api logged in as this user-like thing.

See Also:
  
- #api_key

```

46
47
48
```

```
# File 'lib/conjur/acts_as_user.rb', line 46

def api
  Conjur::API.new_from_key login, api_key, account: account
end

```

###
  
    #**api_key**  ⇒ String 
  

  

  

  
    
  
    **Note:**
    

The API key is not returned by Conjur::API#resource. It is only available

Returns a newly created user's api_key.

via Conjur::API.login, when the object is newly created, and when the API key is rotated.

Returns:

-

        (String)

        —
        

the api key

Raises:

-

        (Exception)

        —
        

when the object isn't newly created.

```

37
38
39
```

```
# File 'lib/conjur/acts_as_user.rb', line 37

def api_key
  attributes['api_key'] or raise "api_key is only available on a newly created #{kind}"
end

```

###
  
    #**rotate_api_key**  ⇒ String 
  

  

  

  
    
  
    **Note:**
    

You will not be able to access the API key returned by this method later, so you should
probably hang onto it it.

    **Note:**
    

You cannot rotate your own API key with this method. To do so, use `Conjur::API.rotate_api_key`.

    **Note:**
    

This feature requires a Conjur appliance running version 4.6 or higher.

Rotate this role's API key. You must have `update` permission on the user to do so.

Returns:

-

        (String)

        —
        

the new API key for this user.

```

60
61
62
63
64
65
66
```

```
# File 'lib/conjur/acts_as_user.rb', line 60

def rotate_api_key
  if login == username
    raise 'You cannot rotate your own API key via this method. To do so, use `Conjur::API.rotate_api_key`'
  end

  url_for(:authn_rotate_api_key, credentials, account, id).put("").body
end

```
