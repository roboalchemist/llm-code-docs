# Class: Conjur::HostFactoryToken
  
    Inherits:
    
      Object
      
        

          
- Object

- Conjur::HostFactoryToken

        show all
      

    Defined in:
    lib/conjur/host_factory_token.rb
  
##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**==**(other)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**cidr**  ⇒ String 
    

    
  
  
  
  
  
  
  
  

  
    

Gets the CIDR restriction.

-
  
      #**expiration**  ⇒ DateTime 

Gets the expiration.

-
  
      #**initialize**(data, credentials)  ⇒ HostFactoryToken 

    constructor
  
  
  
  
  
  

  
    

A new instance of HostFactoryToken.

-
  
      #**revoke**  ⇒ Object 

Revokes the token, after which it cannot be used any more.

-
  
      #**to_json**(options = {})  ⇒ Object 

Convert the object to JSON.

-
  
      #**to_s**  ⇒ Object 

Format the token as a string, using JSON format.

-
  
      #**token**  ⇒ String 

Gets the token string.

## Constructor Details

###
  
    #**initialize**(data, credentials)  ⇒ HostFactoryToken 
  

  

  

  
    

Returns a new instance of HostFactoryToken.

```

23
24
25
26
```

```
# File 'lib/conjur/host_factory_token.rb', line 23

def initialize data, credentials
  @data = data
  @credentials = credentials
end
```

## Instance Method Details

###
  
    #**==**(other)  ⇒ Object 
  

  

  

  
    
      

```

70
71
72
73
74
75
```

```
# File 'lib/conjur/host_factory_token.rb', line 70

def ==(other)
  other.class == self.class &&
    other.token == self.token &&
    other.expiration == self.expiration &&
    other.cidr == self.cidr
end
```

###
  
    #**cidr**  ⇒ String 
  

  

  

  
    

Gets the CIDR restriction.

Returns:

-

        (String)

```

61
62
63
```

```
# File 'lib/conjur/host_factory_token.rb', line 61

def cidr
  @data['cidr']
end
```

###
  
    #**expiration**  ⇒ DateTime 
  

  

  

  
    

Gets the expiration.

Returns:

-

        (DateTime)

```

54
55
56
```

```
# File 'lib/conjur/host_factory_token.rb', line 54

def expiration
  DateTime.iso8601(@data['expiration'])
end
```

###
  
    #**revoke**  ⇒ Object 
  

  

  

  
    

Revokes the token, after which it cannot be used any more.

```

66
67
68
```

```
# File 'lib/conjur/host_factory_token.rb', line 66

def revoke
  Conjur::API.revoke_host_factory_token @credentials, token
end
```

###
  
    #**to_json**(options = {})  ⇒ Object 
  

  

  

  
    

Convert the object to JSON.

Fields:

- token

- expiration

- cidr

```

35
36
37
```

```
# File 'lib/conjur/host_factory_token.rb', line 35

def to_json(options = {})
  { token: token, expiration: expiration, cidr: cidr }
end
```

###
  
    #**to_s**  ⇒ Object 
  

  

  

  
    

Format the token as a string, using JSON format.

```

40
41
42
```

```
# File 'lib/conjur/host_factory_token.rb', line 40

def to_s
  to_json.to_s
end
```

###
  
    #**token**  ⇒ String 
  

  

  

  
    

Gets the token string.

Returns:

-

        (String)

```

47
48
49
```

```
# File 'lib/conjur/host_factory_token.rb', line 47

def token
  @data['token']
end
```
