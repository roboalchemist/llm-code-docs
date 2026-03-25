# Class: Conjur::HostFactory
  
    Inherits:
    
      BaseObject
      
        

          
- Object

- BaseObject

- Conjur::HostFactory

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      ActsAsRolsource
  
    Defined in:
    lib/conjur/host_factory.rb
  
## Overview

A Host Factory is a way to allow clients to create Conjur hosts without giving them
any other access to Conjur.

Each Host Factory can have 0 or more tokens, each of which is a random string that
has an associated expiration and optional CIDR restriction. A user or machine who has
a host factory token can use it to create new hosts, or to rotate the API keys of
existing hosts.

See Also:
  
- API.host_factory_create_host

- HostFactoryToken

## Instance Attribute Summary

### Attributes inherited from BaseObject

# credentials, #id

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**create_token**(expiration, cidr: nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Create a new token.

-
  
      #**create_tokens**(expiration, count: 1, cidr: nil)  ⇒ Array<HostFactoryToken> 

Create one or more host factory tokens.

-
  
      #**tokens**  ⇒ Array<HostFactoryToken> 

Enumerate the tokens on the host factory.

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
  
    #**create_token**(expiration, cidr: nil)  ⇒ Object 
  

  

  

  
    

Create a new token.

See Also:
  
- #create_tokens

```

59
60
61
```

```
# File 'lib/conjur/host_factory.rb', line 59

def create_token expiration, cidr: nil
  create_tokens(expiration, cidr: cidr).first
end
```

###
  
    #**create_tokens**(expiration, count: 1, cidr: nil)  ⇒ Array<HostFactoryToken> 
  

  

  

  
    

Create one or more host factory tokens. Each token can be used to create
hosts, using API.host_factory_create_host.

Parameters:

-

        expiration

        (Time)
      
      
      
        —
        

the future time at which the token will stop working.

-

        count

        (Integer)
      
      
        *(defaults to: 1)*
      
      
        —
        

the number of (identical) tokens to create (default: 1).

-

        cidr

        (String)
      
      
        *(defaults to: nil)*
      
      
        —
        

a CIDR restriction on the usage of the token.

Returns:

-

        (Array<HostFactoryToken>)

        —
        

the token or tokens.

```

44
45
46
47
48
49
50
51
52
53
54
```

```
# File 'lib/conjur/host_factory.rb', line 44

def create_tokens expiration, count: 1, cidr: nil
  options = {}
  options[:expiration] = expiration.iso8601
  options[:host_factory] = id
  options[:count] = count
  options[:cidr] = cidr if cidr
  response = JSON.parse url_for(:host_factory_create_tokens, credentials, id).post(options)
  response.map do |data|
    HostFactoryToken.new data, credentials
  end
end
```

###
  
    #**tokens**  ⇒ Array<HostFactoryToken> 
  

  

  

  
    

Enumerate the tokens on the host factory.

Returns:

-

        (Array<HostFactoryToken>)

        —
        

the token or tokens.

```

66
67
68
69
70
71
72
73
```

```
# File 'lib/conjur/host_factory.rb', line 66

def tokens
  # Tokens list is not returned by +show+ if the caller doesn't have permission
  return nil unless self.attributes['tokens']

  self.attributes['tokens'].collect do |data|
    HostFactoryToken.new data, credentials
  end
end
```
