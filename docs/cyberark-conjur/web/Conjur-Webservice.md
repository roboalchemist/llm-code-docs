# Class: Conjur::Webservice
  
    Inherits:
    
      BaseObject
      
        

          
- Object

- BaseObject

- Conjur::Webservice

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      ActsAsResource
  
    Defined in:
    lib/conjur/webservice.rb
  
## Overview

A Conjur Webservice, which protects access to service code.

Permissions on webservices can be granted and interpreted in a free-form way
which is appropriate to the domain. For example, for a Docker registry
which is guarded by a Webservice, the likely privileges would be `pull` and `push`.

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
