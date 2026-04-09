# Class: Conjur::Variable
  
    Inherits:
    
      BaseObject
      
        

          
- Object

- BaseObject

- Conjur::Variable

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      ActsAsResource
  
    Defined in:
    lib/conjur/variable.rb
  
## Overview

#### Examples

#####

Variables are versioned

```
variable = api.resource 'myorg:variable:example'
# Unless you set a variables value when you create it, the variable starts out without a value and version_count
# is 0.
var.version_count # => 0
var.value # raises RestClient::ResourceNotFound (404)

# Add a value
var.add_value 'value 1'
var.version_count # => 1
var.value # => 'value 1'

# Add another value
var.add_value 'value 2'
var.version_count # => 2

# 'value' with no argument returns the most recent value
var.value # => 'value 2'

# We can access older versions by their 1 based index:
var.value 1 # => 'value 1'
var.value 2 # => 'value 2'
# Notice that version 0 of a variable is always the most recent:
var.value 0 # => 'value 2'

```

## Instance Attribute Summary

### Attributes inherited from BaseObject

# credentials, #id

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**add_value**(value)  
    

    
  
  
  
  
  
  
  
  

  
    

Add a new value to the variable.

-
  
      #**as_json**(options = {})  ⇒ Object 

-
  
      #**kind**  ⇒ String 

The kind of secret represented by this variable,  for example, `'postgres-url'` or `'aws-secret-access-key'`.

-
  
      #**mime_type**  ⇒ String 

The MIME Type of the variable's value.

-
  
      #**value**(version = nil, options = {})  ⇒ String 

Return the version of a variable.

-
  
      #**version_count**  ⇒ Integer 

Return the number of versions of the variable.

### Methods included from ActsAsResource

# exists?, #owner, #permitted?, #permitted_roles

### Methods inherited from BaseObject

# account, #identifier, #initialize, #inspect, #username

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
  
    #**add_value**(value)  
  

  

  

  
    

This method returns an undefined value.

Add a new value to the variable.

You must have the **`'update'`** permission on a variable to call this method.

#### Examples

#####

Add a value to a variable

```
var = api.variable 'my-secret'
puts var.version_count     #  1
puts var.value             #  'supersecret'
var.add_value "new_secret"
puts var.version_count     # 2
puts var.value             # 'new_secret'

```

Parameters:

-

        value

        (String)
      
      
      
        —
        

the new value to add

```

128
129
130
131
132
133
134
135
136
```

```
# File 'lib/conjur/variable.rb', line 128

def add_value value
  log do |logger|
    logger << "Adding a value to variable #{id}"
  end
  invalidate do
    route = url_for(:secrets_add, credentials, id)
    route.post value
  end
end

```

###
  
    #**as_json**(options = {})  ⇒ Object 
  

  

  

  
    
      

```

80
81
82
83
84
85
```

```
# File 'lib/conjur/variable.rb', line 80

def as_json options={}
  result = super(options)
  result["mime_type"] = mime_type
  result["kind"] = kind
  result
end

```

###
  
    #**kind**  ⇒ String 
  

  

  

  
    
  
    **Note:**
    

this is **not** the same as the `kind` part of a qualified Conjur id.

The kind of secret represented by this variable,  for example, `'postgres-url'` or
`'aws-secret-access-key'`.

You must have the **`'read'`** permission on a variable to call this method.

This attribute is only for human consumption, and does not take part in the Conjur permissions
model.

Returns:

-

        (String)

        —
        

a string representing the kind of secret.

```

97
98
99
```

```
# File 'lib/conjur/variable.rb', line 97

def kind
  parser_for(:variable_kind, variable_attributes) || "secret"
end

```

###
  
    #**mime_type**  ⇒ String 
  

  

  

  
    

The MIME Type of the variable's value.

You must have the **`'read'`** permission on a variable to call this method.

This attribute is used by the Conjur services to set a response `Content-Type` header when
returning the value of a variable.  Conjur applies the same MIME Type to all versions of a variable,
so if you plan on accessing the variable in a way that depends on a correct `Content-Type` header
you should make sure to store appropriate data for the mime type in all versions.

Returns:

-

        (String)

        —
        

a MIME type, such as `'text/plain'` or `'application/octet-stream'`.

```

111
112
113
```

```
# File 'lib/conjur/variable.rb', line 111

def mime_type
  parser_for(:variable_mime_type, variable_attributes) || "text/plain"
end

```

###
  
    #**value**(version = nil, options = {})  ⇒ String 
  

  

  

  
    

Return the version of a variable.

You must have the **`'execute'`** permission on a variable to call this method.

When no argument is given, the most recent version is returned.

When a `version` argument is given, the method returns a version according to the following rules:

- If `version` is 0, the *most recent* version is returned.

- If `version` is less than 0 or greater than #version_count, a `RestClient::ResourceNotFound` exception
will be raised.

- If #version_count is 0, a `RestClient::ResourceNotFound` exception will be raised.

- If `version` is >= 1 and `version` <= #version_count, the version at the **1 based** index given by `version`
will be returned.

#### Examples

#####

Fetch all versions of a variable

```
versions = (1..var.version_count).map do |version|
  var.value version
end

```

#####

Get the current version of a variable

```
# All of these return the same thing:
var.value
var.value 0
var.value var.version_count

```

#####

Get the value of an expired variable

```
var.value nil, show_expired: true

```

Parameters:

-

        version

        (Integer)
      
      
        *(defaults to: nil)*
      
      
        —
        

the **1 based** version.

-

        options

        (Hash)
      
      
        *(defaults to: {})*
      
      
    
  

  
    
    
    
    
    

Options Hash (options):

-
          :show_expired
          (Boolean, false)
          
            
          
          
            — 

show value even if variable has expired

Returns:

-

        (String)

        —
        

the value of the variable

```

189
190
191
192
```

```
# File 'lib/conjur/variable.rb', line 189

def value version = nil, options = {}
  options['version'] = version if version
  url_for(:secrets_value, credentials, id, options).get.body
end

```

###
  
    #**version_count**  ⇒ Integer 
  

  

  

  
    

Return the number of versions of the variable.

You must have the **`'read'`** permission on a variable to call this method.

#### Examples

```
var.version_count # => 4
var.add_value "something new"
var.version_count # => 5

```

Returns:

-

        (Integer)

        —
        

the number of versions

```

148
149
150
151
152
153
154
155
```

```
# File 'lib/conjur/variable.rb', line 148

def version_count
  secrets = attributes['secrets']
  if secrets.empty?
    0
  else
    secrets.last['version']
  end
end

```
