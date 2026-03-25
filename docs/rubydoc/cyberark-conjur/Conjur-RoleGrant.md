# Class: Conjur::RoleGrant
  
    Inherits:
    
      Object
      
        

          
- Object

- Conjur::RoleGrant

        show all
      
    
  
  

  
  
  
      Extended by:
      BuildObject::ClassMethods
  
    Defined in:
    lib/conjur/role_grant.rb
  
## Overview

Represents the membership of a role. `RoleGrant`s are returned
by ActsAsRole#members and represent members of the role on which the method was invoked.

#### Examples

```
alice.members.map{|grant| grant.member}.include? admin_role # => true
admin_role.members.map{|grant| grant.member}.include? alice # => true

```

## Instance Attribute Summary collapse

-
  
      #**admin_option**  ⇒ Boolean 

      readonly
    
    
  
  
  
  
  

  
    

When true, the role #member is allowed to give this grant to other roles.

-
  
      #**member**  ⇒ Conjur::Role 

      readonly
    
    
  
  
  
  
  

  
    

The member role in the relationship.

-
  
      #**role**  ⇒ Conjur::Role 

      readonly
    
    
  
  
  
  
  

  
    

The role which was granted.

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**as_json**(options = {})  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**to_h**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Representation of the role grant as a hash.

-
  
      #**to_s**  ⇒ Object 

### Methods included from BuildObject::ClassMethods

build_object, find_class

## Instance Attribute Details

###
  
    #**admin_option**  ⇒ Boolean  (readonly)
  

  

  

  
    

When true, the role #member is allowed to give this grant to other roles

Returns:

-

        (Boolean)

```

39
40
41
```

```
# File 'lib/conjur/role_grant.rb', line 39

def admin_option
  @admin_option
end

```

###
  
    #**member**  ⇒ Conjur::Role  (readonly)
  

  

  

  
    

The member role in the relationship

Returns:

-

        (Conjur::Role)

```

34
35
36
```

```
# File 'lib/conjur/role_grant.rb', line 34

def member
  @member
end

```

###
  
    #**role**  ⇒ Conjur::Role  (readonly)
  

  

  

  
    

The role which was granted.

Returns:

-

        (Conjur::Role)

```

30
31
32
```

```
# File 'lib/conjur/role_grant.rb', line 30

def role
  @role
end

```

## Instance Method Details

###
  
    #**as_json**(options = {})  ⇒ Object 
  

  

  

  
    
      

```

66
67
68
```

```
# File 'lib/conjur/role_grant.rb', line 66

def as_json options = {}
  to_h.as_json(options)
end

```

###
  
    #**to_h**  ⇒ Object 
  

  

  

  
    

Representation of the role grant as a hash.

```

54
55
56
57
58
59
60
```

```
# File 'lib/conjur/role_grant.rb', line 54

def to_h
  {
    role: role.id,
    member: member.id,
    admin_option: admin_option
  }
end

```

###
  
    #**to_s**  ⇒ Object 
  

  

  

  
    
      

```

62
63
64
```

```
# File 'lib/conjur/role_grant.rb', line 62

def to_s
  to_h.to_s
end

```
