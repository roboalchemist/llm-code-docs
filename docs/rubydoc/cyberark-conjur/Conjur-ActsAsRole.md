# Module: Conjur::ActsAsRole
  
    Included in:
    Role
  
  

  
  
    Defined in:
    lib/conjur/acts_as_role.rb
  
## Overview

This module provides methods for things that have an associated Role.

All high level Conjur assets (groups and users, for example) are composed of both a role and a resource.  This allows
these assets to have permissions on other assets, and for other assets to have permission
on them.

The ActsAsRole module itself should be considered private, but it's methods are
public when added to a Conjur asset class.

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**exists?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Check whether this object exists by performing a HEAD request to its URL.

-
  
      #**login**  ⇒ Object 

Login name of the role.

-
  
      #**members**(options = {})  ⇒ Array<Conjur::RoleGrant> 

Fetch the direct members of this role.

-
  
      #**memberships**(options = {})  ⇒ Array<Conjur::Role> 

Find all roles of which this role is a member.

## Instance Method Details

###
  
    #**exists?**  ⇒ Boolean 
  

  

  

  
    

Check whether this object exists by performing a HEAD request to its URL.

This method will return false if the object doesn't exist.

#### Examples

```
does_not_exist = api.user 'does-not-exist' # This returns without error.

# this is wrong!
owner = does_not_exist.members # raises RestClient::ResourceNotFound

# this is right!
owner = if does_not_exist.exists?
  does_not_exist.members
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

53
54
55
56
57
58
59
60
61
62
```

```
# File 'lib/conjur/acts_as_role.rb', line 53

def exists?
  begin
    rbac_role_resource.head
    true
  rescue RestClient::Forbidden
    true
  rescue RestClient::ResourceNotFound
    false
  end
end

```

###
  
    #**login**  ⇒ Object 
  

  

  

  
    

Login name of the role. This is formed from the role kind and role id.
For users, the role kind can be omitted.

```

31
32
33
```

```
# File 'lib/conjur/acts_as_role.rb', line 31

def login
  [ kind, identifier ].delete_if{|t| t == "user"}.join('/')
end

```

###
  
    #**members**(options = {})  ⇒ Array<Conjur::RoleGrant> 
  

  

  

  
    

Fetch the direct members of this role. The results are *not* recursively expanded).

### Permissions

You must be a member of the role to call this method.

Parameters:

-

        options

        (Hash, nil)
      
      
        *(defaults to: {})*
      
      
        —
        

extra parameters to pass to the webservice method.

Returns:

-

        (Array<Conjur::RoleGrant>)

        —
        

the role memberships

Raises:

-

        (RestClient::Forbidden)

        —
        

if you don't have permission to perform this operation

```

125
126
127
128
129
130
131
132
133
```

```
# File 'lib/conjur/acts_as_role.rb', line 125

def members options = {}
  options["members"] = true
  result = JSON.parse(rbac_role_resource[options_querystring options].get)
  if result.is_a?(Hash) && ( count = result['count'] )
    count
  else
    parser_for(:members, credentials, result)
  end
end

```

###
  
    #**memberships**(options = {})  ⇒ Array<Conjur::Role> 
  

  

  

  
    

Find all roles of which this role is a member.  By default, role relationships are recursively expanded,
so if `a` is a member of `b`, and `b` is a member of `c`, `a.all` will include `c`.

### Permissions

You must be a member of the role to call this method.

You can restrict the roles returned to one or more role ids.  This feature is mainly useful
for checking whether this role is a member of any of a set of roles.

### Options

- **recursive** Defaults to +true+, performs recursive expansion of the memberships.

#### Examples

#####

Show all roles of which `"conjur:group:pubkeys-1.0/key-managers"` is a member

```
# Add alice to the group, so we see something interesting
key_managers = api.group('pubkeys-1.0/key-managers')
key_managers.add_member api.user('alice')

# Show the memberships, mapped to the member ids.
key_managers.role.all.map(&:id)
# => ["conjur:group:pubkeys-1.0/admin", "conjur:user:alice"]

```

#####

See if role `"conjur:user:alice"` is a member of either `"conjur:groups:developers"` or `"conjur:group:ops"`

```
is_member = api.role('conjur:user:alice').all(filter: ['conjur:group:developers', 'conjur:group:ops']).any?

```

Parameters:

-

        options

        (Hash)
      
      
        *(defaults to: {})*
      
      
        —
        

options for the request

Returns:

-

        (Array<Conjur::Role>)

        —
        

Roles of which this role is a member

```

91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
```

```
# File 'lib/conjur/acts_as_role.rb', line 91

def memberships options = {}
  request = if options.delete(:recursive) == false
    options["memberships"] = true
  else
    options["all"] = true
  end
  if filter = options.delete(:filter)
    filter = [filter] unless filter.is_a?(Array)
    options["filter"] = filter.map(&Id.method(:new))
  end

  result = JSON.parse(rbac_role_resource[options_querystring options].get)
  if result.is_a?(Hash) && ( count = result['count'] )
    count
  else
    host = Conjur.configuration.core_url
    result.collect do |item|
      if item.is_a?(String)
        build_object(item, default_class: Role)
      else
        RoleGrant.parse_from_json(item, self.credentials)
      end
    end
  end
end

```
