# Class: Conjur::Policy
  
    Inherits:
    
      BaseObject
      
        

          
- Object

- BaseObject

- Conjur::Policy

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      ActsAsRolsource
  
    Defined in:
    lib/conjur/policy.rb
  
## Overview

Defines an set of objects, permission grants and role grants. All objects in a policy
share a common naming prefix, which is the id of the policy. (Exception: the root
policy does not add a naming prefix to each of its objects).

Policies are defined using a YAML syntax, which is extensively documented on the Conjur
web site. To load a policy, define it using YAML and then use API#load_policy.

See Also:
  
- API#load_policy

## Instance Attribute Summary

### Attributes inherited from BaseObject

# credentials, #id

## Method Summary

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
