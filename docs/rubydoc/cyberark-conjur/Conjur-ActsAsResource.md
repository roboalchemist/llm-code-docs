# Module: Conjur::ActsAsResource
  
    Included in:
    Resource, Variable, Webservice
  
  

  
  
    Defined in:
    lib/conjur/acts_as_resource.rb
  
## Overview

This module is included in object classes that have resource behavior.

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**exists?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Check whether this object exists by performing a HEAD request to its URL.

-
  
      #**owner**  ⇒ String 

The full role id of the role that owns this resource.

-
  
      #**permitted?**(privilege, role: nil)  ⇒ Boolean 

True if the logged-in role, or a role specified using the :role option, has the specified +privilege+ on this resource.

-
  
      #**permitted_roles**(privilege)  ⇒ Array<String> 

Lists roles that have a specified privilege on the resource.

## Instance Method Details

###
  
    #**exists?**  ⇒ Boolean 
  

  

  

  
    

Check whether this object exists by performing a HEAD request to its URL.

This method will return false if the object doesn't exist.

#### Examples

```
does_not_exist = api.user 'does-not-exist' # This returns without error.

# this is wrong!
owner = does_not_exist.owner # raises RestClient::ResourceNotFound

# this is right!
owner = if does_not_exist.exists?
  does_not_exist.owner
else
  nil # or some sensible default
end
```

Returns:

-

        (Boolean)

        —
        

does it exist?

```

62
63
64
65
66
67
68
69
70
71
```

```
# File 'lib/conjur/acts_as_resource.rb', line 62

def exists?
  begin
    url_for(:resources_resource, credentials, id).head
    true
  rescue RestClient::Forbidden
    true
  rescue RestClient::ResourceNotFound
    false
  end
end
```

###
  
    #**owner**  ⇒ String 
  

  

  

  
    

The full role id of the role that owns this resource.

#### Examples

```
api.current_role # => 'conjur:user:jon'
resource = api.create_resource 'conjur:example:resource-owner'
resource.owner # => 'conjur:user:jon'
```

Returns:

-

        (String)

        —
        

the full role id of this resource's owner.

```

40
41
42
```

```
# File 'lib/conjur/acts_as_resource.rb', line 40

def owner
  build_object attributes['owner'], default_class: Role
end
```

###
  
    #**permitted?**(privilege, role: nil)  ⇒ Boolean 
  

  

  

  
    

True if the logged-in role, or a role specified using the :role option, has the
specified +privilege+ on this resource.

#### Examples

```
api.current_role # => 'conjur:cat:mouse'
resource.permitted_roles 'execute' # => ['conjur:user:admin', 'conjur:cat:mouse']
resource.permitted_roles 'update', # => ['conjur:user:admin', 'conjur:cat:gino']

resource.permitted? 'update' # => false, `mouse` can't update this resource
resource.permitted? 'execute' # => true, `mouse` can execute it.
resource.permitted? 'update', role: 'conjur:cat:gino' # => true, `gino` can update it.
```

Parameters:

-

        privilege

        (String)
      
      
      
        —
        

the privilege to check

-

        role

        (String, nil)
      
      
        *(defaults to: nil)*
      
      
        —
        

:role check whether the role given by this full role id is permitted
instead of checking +api.current_role+.

Returns:

-

        (Boolean)

```

114
115
116
117
118
119
120
121
```

```
# File 'lib/conjur/acts_as_resource.rb', line 114

def permitted? privilege, role: nil
  url_for(:resources_check, credentials, id, privilege, role)
  true
rescue RestClient::Forbidden
  false
rescue RestClient::ResourceNotFound
  false
end
```

###
  
    #**permitted_roles**(privilege)  ⇒ Array<String> 
  

  

  

  
    

Lists roles that have a specified privilege on the resource.

This will return only roles of which api.current_user is a member.

Options:

- **offset** Zero-based offset into the result set.

- **limit**  Total number of records returned.

#### Examples

```
resource = api.resource 'conjur:variable:example'
resource.permitted_roles 'execute' # => ['conjur:user:admin']
# After permitting 'execute' to user 'jon'
resource.permitted_roles 'execute' # => ['conjur:user:admin', 'conjur:user:jon']
```

Parameters:

-

        privilege

        (String)
      
      
      
        —
        

the privilege

Returns:

-

        (Array<String>)

        —
        

the ids of roles that have `privilege` on this resource.

```

90
91
92
93
94
95
96
97
```

```
# File 'lib/conjur/acts_as_resource.rb', line 90

def permitted_roles privilege
  result = JSON.parse url_for(:resources_permitted_roles, credentials, id, privilege).get
  if result.is_a?(Hash) && ( count = result['count'] )
    count
  else
    result
  end
end
```
