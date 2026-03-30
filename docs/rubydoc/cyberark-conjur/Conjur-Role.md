# Class: Conjur::Role
  
    Inherits:
    
      BaseObject
      
        

          
- Object

- BaseObject

- Conjur::Role

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      ActsAsRole
  
    Defined in:
    lib/conjur/role.rb
  
## Overview

A Conjur custom Role. This object is used for roles whose `kind` is not
any of the pre-defined common types such as Group, Host, Layer, etc.

## Instance Attribute Summary

### Attributes inherited from BaseObject

# credentials, #id

## Method Summary

### Methods included from ActsAsRole

# exists?, #login, #members, #memberships

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
