# Class: Conjur::Resource
  
    Inherits:
    
      BaseObject
      
        

          
- Object

- BaseObject

- Conjur::Resource

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      ActsAsResource
  
    Defined in:
    lib/conjur/resource.rb
  
## Overview

A Conjur custom Resource. This object is used for resources whose `kind` is not
any of the pre-defined common types such as Group, Host, Variable, etc.

## Instance Attribute Summary

### Attributes inherited from BaseObject

# credentials, #id

## Method Summary

### Methods included from ActsAsResource

# exists?, #owner, #permitted?, #permitted_roles

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
