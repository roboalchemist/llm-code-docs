# Class: Conjur::Layer
  
    Inherits:
    
      BaseObject
      
        

          
- Object

- BaseObject

- Conjur::Layer

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      ActsAsRolsource
  
    Defined in:
    lib/conjur/layer.rb
  
## Overview

A Conjur Layer is a type of role whose members are Conjur Hosts. The hosts inherit
permissions from the layer. Automatic roles on the layer can also be used to manage
SSH permissions to the hosts.

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
