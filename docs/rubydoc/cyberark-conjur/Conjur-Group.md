# Class: Conjur::Group
  
    Inherits:
    
      BaseObject
      
        

          
- Object

- BaseObject

- Conjur::Group

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      ActsAsRolsource
  
    Defined in:
    lib/conjur/group.rb
  
## Overview

A Conjur Group represents a collection of Conjur Users, Groups and Layers.

## Instance Attribute Summary

### Attributes inherited from BaseObject

# credentials, #id

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**gidnumber**  ⇒ Fixnum 
    

    
  
  
  
  
  
  
  
  

  
    

Get the group's gidnumber, which can be used by LDAP and SSH login, among other things.

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
  
    #**gidnumber**  ⇒ Fixnum 
  

  

  

  
    

Get the group's gidnumber, which can be used by LDAP and SSH login, among other things.

Returns:

-

        (Fixnum)

        —
        

the gidnumber

Raises:

-

        (RestClient::Forbidden)

        —
        

if you don't have permission to `show` the group.

```

31
32
33
```

```
# File 'lib/conjur/group.rb', line 31

def gidnumber
  parser_for(:group_gidnumber, group_attributes)
end

```
