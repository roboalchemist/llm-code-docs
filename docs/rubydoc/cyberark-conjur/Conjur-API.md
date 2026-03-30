# Class: Conjur::API
  
    Inherits:
    
      Object
      
        

          
- Object

- Conjur::API

        show all
      
    
  
  

  
  
  
      Extended by:
      Routing
  
  
  
  
  
      Includes:
      BuildObject, Escape, LogSource, Routing
  
    Defined in:
    lib/conjur/base.rb,

  lib/conjur/api/authn.rb,
 lib/conjur/api/roles.rb,
 lib/conjur/api/router.rb,
 lib/conjur-api/version.rb,
 lib/conjur/api/pubkeys.rb,
 lib/conjur/api/policies.rb,
 lib/conjur/api/ldap_sync.rb,
 lib/conjur/api/resources.rb,
 lib/conjur/api/variables.rb,
 lib/conjur/api/authenticators.rb,
 lib/conjur/api/host_factories.rb

## Overview

API contains each of the methods for access the Conjur API endpoints
-- :reek:DataClump for authenticator identifier fields (name, id, account)

## Defined Under Namespace

      **Modules:** Router, TokenExpiration
    
  
    
      **Classes:** APIKeyAuthenticator, LocalAuthenticator, TokenFileAuthenticator, UnableAuthenticator
    
  

  
    
##

      Policy management
      collapse
    

    
      
        POLICY_METHOD_POST =
          
  
    

Append only.

```
:post
```

        POLICY_METHOD_PATCH =
          
  
    

Allow explicit deletion statements, but don't delete implicitly delete data.

```
:patch
```

        POLICY_METHOD_PUT =
          
  
    

Replace the policy entirely, deleting any existing data that is not declared in the new policy.

```
:put
```

##

      Constant Summary
      collapse
    

    
      
        VERSION =
          
        
        

```
File.read(File.expand_path('../../VERSION', __dir__))
```

## Instance Attribute Summary collapse

-
  
      #**api_key**  ⇒ String 

      readonly
    
    
  
  
  
  
  

  
    

The api key used to create this instance.

-
  
      #**authenticator**  ⇒ Object 

      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute authenticator.

-
  
      #**remote_ip**  ⇒ Object 

      readonly
    
    
  
  
  
  
  

  
    

An optional IP address to be recorded in the audit record for any actions performed by this API instance.

##

      Authentication
      collapse
    

    

      
        
-
  
      .**authenticate**(username, api_key, account: Conjur.configuration.account)  ⇒ String 
    

    
  
  
  
  
  
  
  
  

  
    

Exchanges Conjur the API key (refresh token) for an access token.

-
  
      .**authenticate_local**(username, account: Conjur.configuration.account, expiration: nil, cidr: nil)  ⇒ String 

Obtains an access token from the +authn_local+ service.

-
  
      .**authenticator_authenticate**(authenticator, service_id, account: Conjur.configuration.account, options: {})  ⇒ String 

Authenticates using a third party authenticator like authn-oidc.

-
  
      .**authenticator_authenticate_get**(authenticator, service_id, account: Conjur.configuration.account, options: {})  ⇒ RestClient::Response 

Authenticates using a third party authenticator like authn-oidc via GET request.

-
  
      .**login**(username, password, account: Conjur.configuration.account)  ⇒ String 

Exchanges a username and a password for an api key.

-
  
      .**update_password**(username, password, new_password, account: Conjur.configuration.account)  

Change a user's password.

##

      Password and API key management
      collapse
    

    

      
        
-
  
      .**rotate_api_key**(username, password, account: Conjur.configuration.account)  ⇒ String 
    

    
  
  
  
  
  
  
  
  

  
    

Rotate the currently authenticated user or host API key by generating and returning a new one.

##

      Roles
      collapse
    

    

      
        
-
  
      #**current_role**(account)  ⇒ Conjur::Role 
    

    
  
  
  
  
  
  
  
  

  
    

Return a Role object representing the role (typically a user or host) that this API instance is authenticated as.

-
  
      #**role**(id)  ⇒ Conjur::Role 

Return a Role representing a role with the given id.

##

      Public Keys
      collapse
    

    

      
        
-
  
      .**public_keys**(username, account: Conjur.configuration.account)  ⇒ String 
    

    
  
  
  
  
  
  
  
  

  
    

Fetch *all*  public keys for the user.

##

      Policy management
      collapse
    

    

      
        
-
  
      #**load_policy**(id, policy, account: Conjur.configuration.account, method: POLICY_METHOD_POST)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Load a policy document into the server.

##

      Resources
      collapse
    

    

      
        
-
  
      #**resource**(id)  ⇒ Conjur::Resource 
    

    
  
  
  
  
  
  
  
  

  
    

Find a resource by its id.

-
  
      #**resources**(options = {})  ⇒ Array<Conjur::Resource> 

Find all resources visible to the current role that match the given search criteria.

##

      Variables
      collapse
    

    

      
        
-
  
      #**variable_values**(variable_ids)  ⇒ Array<String> 
    

    
  
  
  
  
  
  
  
  

  
    

Fetch the values of a list of variables.

##

      Authenticators
      collapse
    

    

      
        
-
  
      #**authentication_providers**(authenticator, account: Conjur.configuration.account)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Fetches the available authentication providers for the authenticator and account.

-
  
      #**authenticator_disable**(authenticator, id, account: Conjur.configuration.account)  ⇒ Object 

Disables an authenticator in Conjur.

-
  
      #**authenticator_enable**(authenticator, id, account: Conjur.configuration.account)  ⇒ Object 

Enables an authenticator in Conjur.

-
  
      #**authenticator_list**  ⇒ Object 

List all configured authenticators.

##

      Class Method Summary
      collapse
    

    

      
        
-
  
      .**host_factory_create_host**(token, id, options = {})  ⇒ Host 
    

    
  
  
  
  
  
  
  
  

  
    

Use a host factory token to create a new host.

-
  
      .**new_from_authn_local**(username, account: Conjur.configuration.account, remote_ip: nil, expiration: nil, cidr: nil)  ⇒ Conjur::API 

Create a new API instance which authenticates using +authn-local+ using the specified username.

-
  
      .**new_from_key**(username, api_key, account: Conjur.configuration.account, remote_ip: nil)  ⇒ Conjur::API 

Create a new API instance from a username and a password or api key.

-
  
      .**new_from_token**(token, remote_ip: nil)  ⇒ Conjur::API 

Create a new API instance from an access token.

-
  
      .**new_from_token_file**(token_file, remote_ip: nil)  ⇒ Conjur::API 

Create a new API instance from a file containing a token issued by the Conjur authentication service.

-
  
      .**revoke_host_factory_token**(credentials, token)  ⇒ Object 

Revokes a host factory token.

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**credentials**  ⇒ Hash 
    

    
  
  
  
  
  
  
  
  

  
    

Credentials that can be merged with options to be passed to `RestClient::Resource` HTTP request methods.

-
  
      #**init_from_authn_local**(username, account: Conjur.configuration.account, remote_ip: nil, expiration: nil, cidr: nil)  ⇒ Object 

-
  
      #**init_from_key**(username, api_key, account: Conjur.configuration.account, remote_ip: nil)  ⇒ Object 

-
  
      #**init_from_token**(token, remote_ip: nil)  ⇒ Object 

-
  
      #**init_from_token_file**(token_file, remote_ip: nil)  ⇒ Object 

-
  
      #**ldap_sync_policy**(config_name: 'default')  ⇒ Object 

Retrieve the policy for the given LDAP sync configuration.

-
  
      #**revoke_host_factory_token**(token)  ⇒ Object 

Revokes a host factory token.

-
  
      #**token**  ⇒ Hash 

The token used to authenticate requests made with the api.

-
  
      #**username**  ⇒ String 

The name of the user as which this api instance is authenticated.

-
  
      #**whoami**  ⇒ Object 

### Methods included from Routing

parser_for, url_for

### Methods included from BuildObject

# build_object

### Methods included from LogSource

# log

### Methods included from Escape

# fully_escape, #path_escape, #query_escape

## Instance Attribute Details

###
  
    #**api_key**  ⇒ String  (readonly)
  

  

  

  
    

The api key used to create this instance.  This is only present when you created the api with new_from_key.#

Returns:

-

        (String)

        —
        

the api key, or nil if this instance was created from a token.

```

125
126
127
```

```
# File 'lib/conjur/base.rb', line 125

def api_key
  @api_key
end
```

###
  
    #**authenticator**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute authenticator.

```

324
325
326
```

```
# File 'lib/conjur/base.rb', line 324

def authenticator
  @authenticator
end
```

###
  
    #**remote_ip**  ⇒ Object  (readonly)
  

  

  

  
    

An optional IP address to be recorded in the audit record for any actions performed by this API instance.

```

129
130
131
```

```
# File 'lib/conjur/base.rb', line 129

def remote_ip
  @remote_ip
end
```

## Class Method Details

###
  
    .**authenticate**(username, api_key, account: Conjur.configuration.account)  ⇒ String 
  

  

  

  
    

Exchanges Conjur the API key (refresh token) for an access token.  The access token can
then be used to authenticate further API calls.

Parameters:

-

        username

        (String)
      
      
      
        —
        

The username or host id for which we want a token

-

        api_key

        (String)
      
      
      
        —
        

The api key

-

        account

        (String)
      
      
        *(defaults to: Conjur.configuration.account)*
      
      
        —
        

The organization account.

Returns:

-

        (String)

        —
        

A JSON formatted authentication token.

```

91
92
93
94
95
96
97
```

```
# File 'lib/conjur/api/authn.rb', line 91

def authenticate username, api_key, account: Conjur.configuration.account
  account ||= Conjur.configuration.account
  if Conjur.log
    Conjur.log << "Authenticating #{username} to account #{account}\n"
  end
  JSON.parse url_for(:authn_authenticate, account, username).post(api_key, content_type: 'text/plain')
end
```

###
  
    .**authenticate_local**(username, account: Conjur.configuration.account, expiration: nil, cidr: nil)  ⇒ String 
  

  

  

  
    

Obtains an access token from the +authn_local+ service. The access token can
then be used to authenticate further API calls.

Parameters:

-

        username

        (String)
      
      
      
        —
        

The username or host id for which we want a token

-

        account

        (String)
      
      
        *(defaults to: Conjur.configuration.account)*
      
      
        —
        

The organization account.

Returns:

-

        (String)

        —
        

A JSON formatted authentication token.

```

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
# File 'lib/conjur/api/authn.rb', line 105

def authenticate_local username, account: Conjur.configuration.account, expiration: nil, cidr: nil
  account ||= Conjur.configuration.account
  if Conjur.log
    Conjur.log << "Authenticating #{username} to account #{account} using authn_local\n"
  end

  require 'json'
  require 'socket'
  message = url_for(:authn_authenticate_local, username, account, expiration, cidr)
  JSON.parse(UNIXSocket.open(Conjur.configuration.authn_local_socket) {|s| s.puts message; s.gets })
end
```

###
  
    .**authenticator_authenticate**(authenticator, service_id, account: Conjur.configuration.account, options: {})  ⇒ String 
  

  

  

  
    

Authenticates using a third party authenticator like authn-oidc.  It will return an
access token to be used to authenticate further API calls.

Parameters:

-

        authenticator

        (String)
      
      
      
    
  
    
-

        service_id
      
      
        (String)
      
      
      
    
  
    
-

        account
      
      
        (String)
      
      
        *(defaults to: Conjur.configuration.account)*
      
      
        —
        

The organization account.

-

        params

        (Hash)
      
      
      
        —
        

Additional params to send to authenticator

Returns:

-

        (String)

        —
        

A JSON formatted authentication token.

```

65
66
67
```

```
# File 'lib/conjur/api/authn.rb', line 65

def authenticator_authenticate authenticator, service_id, account: Conjur.configuration.account, options: {}
  JSON.parse authenticator_authenticate_get authenticator, service_id, account: account, options: options
end
```

###
  
    .**authenticator_authenticate_get**(authenticator, service_id, account: Conjur.configuration.account, options: {})  ⇒ RestClient::Response 
  

  

  

  
    

Authenticates using a third party authenticator like authn-oidc via GET request.
It will return an response object containing access/refresh token data.

Parameters:

-

        authenticator

        (String)
      
      
      
    
  
    
-

        service_id
      
      
        (String)
      
      
      
    
  
    
-

        account
      
      
        (String)
      
      
        *(defaults to: Conjur.configuration.account)*
      
      
        —
        

The organization account.

-

        params

        (Hash)
      
      
      
        —
        

Additional params to send to authenticator

Returns:

-

        (RestClient::Response)

        —
        

Response object

```

77
78
79
80
81
82
```

```
# File 'lib/conjur/api/authn.rb', line 77

def authenticator_authenticate_get authenticator, service_id, account: Conjur.configuration.account, options: {}
  if Conjur.log
    Conjur.log << "Authenticating to account #{account} using #{authenticator}/#{service_id}\n"
  end
  url_for(:authenticator_authenticate, account, service_id, authenticator, options).get
end
```

###
  
    .**host_factory_create_host**(token, id, options = {})  ⇒ Host 
  

  

  

  
    

Use a host factory token to create a new host. Unlike most other methods, this
method does not require a Conjur access token. The host factory token is the
authentication and authorization to create the host.

The token must be valid. The host id can be a new host, or an existing host.
If the host already exists, the server verifies that its layer memberships
match the host factory exactly. Then, its API key is rotated and returned with
the response.

Parameters:

-

        token

        (String)
      
      
      
        —
        

the host factory token.

-

        id

        (String)
      
      
      
        —
        

the id of a new or existing host.

-

        options

        (Hash)
      
      
        *(defaults to: {})*
      
      
        —
        

additional host creation options.

Returns:

-

        (Host)

```

37
38
39
40
41
42
43
44
45
46
47
48
49
```

```
# File 'lib/conjur/api/host_factories.rb', line 37

def host_factory_create_host token, id, options = {}
  token = token.token if token.is_a?(HostFactoryToken)
  response = url_for(:host_factory_create_host, token)
    .post(options.merge(id: id)).body

  attributes = JSON.parse(response)
  # in v4 'id' is just the identifier
  host_id = attributes['roleid'] || attributes['id']

  Host.new(host_id, {}).tap do |host|
    host.attributes = attributes
  end
end
```

###
  
    .**login**(username, password, account: Conjur.configuration.account)  ⇒ String 
  

  

  

  
    

Exchanges a username and a password for an api key.  The api key
  is preferable for storage and use in code, as it can be rotated and has far greater entropy than
  a user memorizable password.

- Note that this method works only for Users. While
Hosts are roles, they do not have passwords.

- If you pass an api key to this method instead of a password, it will verify and return the API key.

- This method uses HTTP Basic Authentication to send the credentials.

#### Examples

```
bob_api_key = Conjur::API.login('bob', 'bob_password')
bob_api_key == Conjur::API.login('bob', bob_api_key)  # => true
```

Parameters:

-

        username

        (String)
      
      
      
        —
        

The `username` or `login` for the
Conjur User.

-

        password

        (String)
      
      
      
        —
        

The `password` or `api key` to authenticate with.

-

        account

        (String)
      
      
        *(defaults to: Conjur.configuration.account)*
      
      
        —
        

The organization account.

Returns:

-

        (String)

        —
        

the API key.

```

50
51
52
53
54
55
```

```
# File 'lib/conjur/api/authn.rb', line 50

def login username, password, account: Conjur.configuration.account
  if Conjur.log
    Conjur.log << "Logging in #{username} to account #{account} via Basic authentication\n"
  end
  url_for(:authn_login, account, username, password).get
end
```

###
  
    .**new_from_authn_local**(username, account: Conjur.configuration.account, remote_ip: nil, expiration: nil, cidr: nil)  ⇒ Conjur::API 
  

  

  

  
    

Create a new Conjur::API instance which authenticates using +authn-local+
using the specified username.

Parameters:

-

        username

        (String)
      
      
      
        —
        

the username to use when making authenticated requests.

-

        account

        (String)
      
      
        *(defaults to: Conjur.configuration.account)*
      
      
        —
        

The organization account.

-

        remote_ip

        (String)
      
      
        *(defaults to: nil)*
      
      
        —
        

the optional IP address to be recorded in the audit record.

-

        expiration

        (String)
      
      
        *(defaults to: nil)*
      
      
        —
        

the optional expiration time of the token.

-

        cidr

        (String)
      
      
        *(defaults to: nil)*
      
      
        —
        

the optional CIDR restriction on the token.

Returns:

-

        (Conjur::API)

        —
        

an api that will authenticate with the given username.

```

116
117
118
```

```
# File 'lib/conjur/base.rb', line 116

def new_from_authn_local username, account: Conjur.configuration.account, remote_ip: nil, expiration: nil, cidr: nil
  self.new.init_from_authn_local username, account: account, remote_ip: remote_ip, expiration: expiration, cidr: cidr
end
```

###
  
    .**new_from_key**(username, api_key, account: Conjur.configuration.account, remote_ip: nil)  ⇒ Conjur::API 
  

  

  

  
    

Create a new Conjur::API instance from a username and a password or api key.

#### Examples

#####

Create an API with valid credentials

```
api = Conjur::API.new_from_key 'admin', '<admin password>'
api.current_role # => 'conjur:user:admin'
api.token['data'] # => 'admin'
```

#####

Authentication is lazy

```
api = Conjur::API.new_from_key 'admin', 'wrongpassword'   # succeeds
api.user 'foo' # raises a 401 error
```

Parameters:

-

        username

        (String)
      
      
      
        —
        

the username to use when making authenticated requests.

-

        api_key

        (String)
      
      
      
        —
        

the api key or password for `username`

-

        remote_ip

        (String)
      
      
        *(defaults to: nil)*
      
      
        —
        

the optional IP address to be recorded in the audit record.

-

        account

        (String)
      
      
        *(defaults to: Conjur.configuration.account)*
      
      
        —
        

The organization account.

Returns:

-

        (Conjur::API)

        —
        

an api that will authenticate with the given username and api key.

```

60
61
62
```

```
# File 'lib/conjur/base.rb', line 60

def new_from_key username, api_key, account: Conjur.configuration.account, remote_ip: nil
  self.new.init_from_key username, api_key, remote_ip: remote_ip, account: account
end
```

###
  
    .**new_from_token**(token, remote_ip: nil)  ⇒ Conjur::API 
  

  

  

  
    

Create a new Conjur::API instance from an access token.

Generally, you will have a Conjur identitiy (username and API key), and create an Conjur::API instance
for the identity using new_from_key.  This method is useful when you are performing authorization checks
given a token.  For example, a Conjur gateway that requires you to prove that you can 'read' a resource named
'super-secret' might get the token from a request header, create an Conjur::API instance with this method,
and use Resource#permitted? to decide whether to accept and forward the request.

#### Examples

#####

A simple gatekeeper

```
RESOURCE_NAME = 'protected-service'

def handle_request request
  token_header = request.header 'X-Conjur-Token'
  token = JSON.parse Base64.b64decode(token_header)

  api = Conjur::API.new_from_token token
  raise Forbidden unless api.resource(RESOURCE_NAME).permitted? 'read'

  proxy_to_service request
end
```

Parameters:

-

        token

        (Hash)
      
      
      
        —
        

the authentication token as parsed JSON to use when making authenticated requests

-

        remote_ip

        (String)
      
      
        *(defaults to: nil)*
      
      
        —
        

the optional IP address to be recorded in the audit record.

Returns:

-

        (Conjur::API)

        —
        

an api that will authenticate with the token

```

88
89
90
```

```
# File 'lib/conjur/base.rb', line 88

def new_from_token token, remote_ip: nil
  self.new.init_from_token token, remote_ip: remote_ip
end
```

###
  
    .**new_from_token_file**(token_file, remote_ip: nil)  ⇒ Conjur::API 
  

  

  

  
    

Create a new Conjur::API instance from a file containing a token issued by the
Conjur authentication service.
The file is read the first time that a token is required. It is also re-read
whenever the API decides that the token it already has is getting close to expiration.

This method is useful when an external process, such as a sidecar container, is continuously
obtaining fresh tokens and writing them to a known file.

Parameters:

-

        token_file

        (String)
      
      
      
        —
        

the file path containing an authentication token as parsed JSON.

-

        remote_ip

        (String)
      
      
        *(defaults to: nil)*
      
      
        —
        

the optional IP address to be recorded in the audit record.

Returns:

-

        (Conjur::API)

        —
        

an api that will authenticate with the tokens provided in the file.

```

103
104
105
```

```
# File 'lib/conjur/base.rb', line 103

def new_from_token_file token_file, remote_ip: nil
  self.new.init_from_token_file token_file, remote_ip: remote_ip
end
```

###
  
    .**public_keys**(username, account: Conjur.configuration.account)  ⇒ String 
  

  

  

  
    

Fetch *all*  public keys for the user.  This method returns a newline delimited
String for compatibility with the authorized_keys SSH format.

If the given user does not exist, an empty String will be returned.  This is to prevent attackers from determining whether
a user exists.

## Permissions

You do not need any special permissions to call this method, since public keys are, well, public.

#### Examples

```
puts api.public_keys('jon')
# ssh-rsa [big long string] jon@albert
# ssh-rsa [big long string] jon@conjurops
```

Parameters:

-

        username

        (String)
      
      
      
        —
        

the *unqualified* Conjur username

Returns:

-

        (String)

        —
        

newline delimited public keys

```

46
47
48
```

```
# File 'lib/conjur/api/pubkeys.rb', line 46

def public_keys username, account: Conjur.configuration.account
  url_for(:public_keys_for_user, account, username).get
end
```

###
  
    .**revoke_host_factory_token**(credentials, token)  ⇒ Object 
  

  

  

  
    

Revokes a host factory token. After revocation, the token can no longer be used to
create hosts.

Parameters:

-

        credentials

        (Hash)
      
      
      
        —
        

authentication credentials of the current user.

-

        token

        (String)
      
      
      
        —
        

the host factory token.

```

56
57
58
```

```
# File 'lib/conjur/api/host_factories.rb', line 56

def revoke_host_factory_token credentials, token
  url_for(:host_factory_revoke_token, credentials, token).delete
end
```

###
  
    .**rotate_api_key**(username, password, account: Conjur.configuration.account)  ⇒ String 
  

  

  

  
    

Rotate the currently authenticated user or host API key by generating and returning a new one.
The old API key is no longer valid after calling this method.  You must have the current
API key or password to perform this operation.  This method *does not* affect a user's password.

Parameters:

-

        username

        (String)
      
      
      
        —
        

the name of the user or host whose API key we want to change

-

        password

        (String)
      
      
      
        —
        

the user's current api key

-

        account

        (String)
      
      
        *(defaults to: Conjur.configuration.account)*
      
      
        —
        

The organization account.

Returns:

-

        (String)

        —
        

the new API key

```

145
146
147
148
149
150
151
```

```
# File 'lib/conjur/api/authn.rb', line 145

def rotate_api_key username, password, account: Conjur.configuration.account
  if Conjur.log
    Conjur.log << "Rotating API key for self (#{username} in account #{account})\n"
  end

  url_for(:authn_rotate_own_api_key, account, username, password).put('').body
end
```

###
  
    .**update_password**(username, password, new_password, account: Conjur.configuration.account)  
  

  

  

  
    

This method returns an undefined value.

Change a user's password.  To do this, you must have the user's current password.  This does not change or rotate
  api keys. However, you *can* use the user's api key as the *current* password, if the user was not created
  with a password.

Parameters:

-

        username

        (String)
      
      
      
        —
        

the name of the user whose password we want to change.

-

        password

        (String)
      
      
      
        —
        

the user's *current* password *or* api key.

-

        new_password

        (String)
      
      
      
        —
        

the new password for the user.

-

        account

        (String)
      
      
        *(defaults to: Conjur.configuration.account)*
      
      
        —
        

The organization account.

```

126
127
128
129
130
131
```

```
# File 'lib/conjur/api/authn.rb', line 126

def update_password username, password, new_password, account: Conjur.configuration.account
  if Conjur.log
    Conjur.log << "Updating password for #{username} in account #{account}\n"
  end
  url_for(:authn_update_password, account, username, password).put new_password
end
```

## Instance Method Details

###
  
    #**authentication_providers**(authenticator, account: Conjur.configuration.account)  ⇒ Object 
  

  

  

  
    

Fetches the available authentication providers for the authenticator and account.
The authenticators must be loaded in Conjur policy prior to fetching.

Parameters:

-

        authenticator

        (String)
      
      
      
        —
        

the authenticator type to retrieve providers for

```

20
21
22
```

```
# File 'lib/conjur/api/authenticators.rb', line 20

def authentication_providers authenticator, account: Conjur.configuration.account
  JSON.parse(url_for(:authentication_providers, account, authenticator, credentials).get)
end
```

###
  
    #**authenticator_disable**(authenticator, id, account: Conjur.configuration.account)  ⇒ Object 
  

  

  

  
    

Disables an authenticator in Conjur.

Parameters:

-

        authenticator

        (String)
      
      
      
        —
        

the authenticator type to disable (e.g. authn-k8s)

-

        id

        (String)
      
      
      
        —
        

the service ID of the authenticator to disable

```

37
38
39
```

```
# File 'lib/conjur/api/authenticators.rb', line 37

def authenticator_disable authenticator, id, account: Conjur.configuration.account
  url_for(:authenticator, account, authenticator, id, credentials).patch(enabled: false)
end
```

###
  
    #**authenticator_enable**(authenticator, id, account: Conjur.configuration.account)  ⇒ Object 
  

  

  

  
    

Enables an authenticator in Conjur. The authenticator must be defined and
loaded in Conjur policy prior to enabling it.

Parameters:

-

        authenticator

        (String)
      
      
      
        —
        

the authenticator type to enable (e.g. authn-k8s)

-

        id

        (String)
      
      
      
        —
        

the service ID of the authenticator to enable

```

29
30
31
```

```
# File 'lib/conjur/api/authenticators.rb', line 29

def authenticator_enable authenticator, id, account: Conjur.configuration.account
  url_for(:authenticator, account, authenticator, id, credentials).patch(enabled: true)
end
```

###
  
    #**authenticator_list**  ⇒ Object 
  

  

  

  
    

List all configured authenticators

```

12
13
14
```

```
# File 'lib/conjur/api/authenticators.rb', line 12

def authenticator_list
  JSON.parse(url_for(:authenticators).get)
end
```

###
  
    #**credentials**  ⇒ Hash 
  

  

  

  
    

Credentials that can be merged with options to be passed to `RestClient::Resource` HTTP request methods.
These include a username and an Authorization header containing the authentication token.

Returns:

-

        (Hash)

        —
        

the options.

Raises:

-

        (RestClient::Unauthorized)

        —
        

if fetching the token fails.

```

170
171
172
173
174
175
176
```

```
# File 'lib/conjur/base.rb', line 170

def credentials
  headers = {}.tap do |h|
    h[:authorization] = "Token token=\"#{Base64.strict_encode64 token.to_json}\""
    h[:x_forwarded_for] = @remote_ip if @remote_ip
  end
  { headers: headers, username: username }
end
```

###
  
    #**current_role**(account)  ⇒ Conjur::Role 
  

  

  

  
    

Return a Role object representing the role (typically a user or host) that this API instance is authenticated
as.  This is derived either from the `login` argument to new_from_key or from the contents of the
`token` given to new_from_token or new_from_token_file.

#### Examples

#####

Current role for a user

```
api = Conjur::API.new_from_key 'jon', 'somepassword'
api.current_role.id # => 'conjur:user:jon'
```

#####

Current role for a host

```
host = api.create_host id: 'exapmle-host'

# Host and User have an `api` method that returns an api with their credentials.  Note
# that this only works with a newly created host or user, which has an `api_key` attribute.
host.api.current_role.id # => 'conjur:host:example-host'
```

Parameters:

-

        account

        (String)
      
      
      
        —
        

the organization account

Returns:

-

        (Conjur::Role)

        —
        

the authenticated role for this API instance

```

75
76
77
```

```
# File 'lib/conjur/api/roles.rb', line 75

def current_role account
  self.class.role_from_username self, username, account
end
```

###
  
    #**init_from_authn_local**(username, account: Conjur.configuration.account, remote_ip: nil, expiration: nil, cidr: nil)  ⇒ Object 
  

  

  

  
    
      

```

316
317
318
319
320
321
322
```

```
# File 'lib/conjur/base.rb', line 316

def init_from_authn_local username, account: Conjur.configuration.account, remote_ip: nil, expiration: nil, cidr: nil
  @username = username
  @api_key = api_key
  @remote_ip = remote_ip
  @authenticator = LocalAuthenticator.new(account, username, expiration, cidr)
  self
end
```

###
  
    #**init_from_key**(username, api_key, account: Conjur.configuration.account, remote_ip: nil)  ⇒ Object 
  

  

  

  
    
      

```

295
296
297
298
299
300
301
```

```
# File 'lib/conjur/base.rb', line 295

def init_from_key username, api_key, account: Conjur.configuration.account, remote_ip: nil
  @username = username
  @api_key = api_key
  @remote_ip = remote_ip
  @authenticator = APIKeyAuthenticator.new(account, username, api_key)
  self
end
```

###
  
    #**init_from_token**(token, remote_ip: nil)  ⇒ Object 
  

  

  

  
    
      

```

303
304
305
306
307
308
```

```
# File 'lib/conjur/base.rb', line 303

def init_from_token token, remote_ip: nil
  @token = token
  @remote_ip = remote_ip
  @authenticator = UnableAuthenticator.new
  self
end
```

###
  
    #**init_from_token_file**(token_file, remote_ip: nil)  ⇒ Object 
  

  

  

  
    
      

```

310
311
312
313
314
```

```
# File 'lib/conjur/base.rb', line 310

def init_from_token_file token_file, remote_ip: nil
  @remote_ip = remote_ip
  @authenticator = TokenFileAuthenticator.new(token_file)
  self
end
```

###
  
    #**ldap_sync_policy**(config_name: 'default')  ⇒ Object 
  

  

  

  
    

Retrieve the policy for the given LDAP sync
configuration. Configurations created through the Conjur UI are
named +default+, so the default value of +config_name+ can be
used.

For details on the use of LDAP sync, see
https://developer.conjur.net/reference/services/ldap_sync/ .

Parameters:

-

        config_name

        (String)
      
      
        *(defaults to: 'default')*
      
      
        —
        

the name of the LDAP sync configuration.

```

34
35
36
```

```
# File 'lib/conjur/api/ldap_sync.rb', line 34

def ldap_sync_policy config_name: 'default'
  JSON.parse(url_for(:ldap_sync_policy, credentials, config_name).get)
end
```

###
  
    #**load_policy**(id, policy, account: Conjur.configuration.account, method: POLICY_METHOD_POST)  ⇒ Object 
  

  

  

  
    

Load a policy document into the server.

The modes are support for policy loading:

- POLICY_METHOD_POST Policy data will be added to the named policy. Deletions are not allowed.

- POLICY_METHOD_PATCH Policy data can be added to or deleted from the named policy. Deletions
are performed by an explicit `!delete` statement.

- POLICY_METHOD_PUT The policy completely replaces the name policy. Policy data which is present
in the server, but not present in the new policy definition, is deleted.

Parameters:

-

        id

        (String)
      
      
      
        —
        

id of the policy to load.

-

        policy

        (String)
      
      
      
        —
        

YAML-formatted policy definition.

-

        account

        (String)
      
      
        *(defaults to: Conjur.configuration.account)*
      
      
        —
        

Conjur organization account

-

        method

        (Symbol)
      
      
        *(defaults to: POLICY_METHOD_POST)*
      
      
        —
        

Policy load method to use: POLICY_METHOD_POST (default), POLICY_METHOD_PATCH, or POLICY_METHOD_PUT.

```

49
50
51
52
```

```
# File 'lib/conjur/api/policies.rb', line 49

def load_policy id, policy, account: Conjur.configuration.account, method: POLICY_METHOD_POST
  request = url_for(:policies_load_policy, credentials, account, id)
  PolicyLoadResult.new JSON.parse(request.send(method, policy))
end
```

###
  
    #**resource**(id)  ⇒ Conjur::Resource 
  

  

  

  
    
  
    **Note:**
    

The id given to this method must be fully qualified.

Find a resource by its id.

### Permissions

The resource **must** be visible to the current role.  This is the case if the current role is the owner of
the resource, or has any privilege on it.

Parameters:

-

        id

        (String)
      
      
      
        —
        

a fully qualified resource identifier

Returns:

-

        (Conjur::Resource)

        —
        

the resource, which may or may not exist

```

36
37
38
```

```
# File 'lib/conjur/api/resources.rb', line 36

def resource id
  build_object id
end
```

###
  
    #**resources**(options = {})  ⇒ Array<Conjur::Resource> 
  

  

  

  
    

Find all resources visible to the current role that match the given search criteria.

## Full Text Search

Conjur supports full text search over the identifiers and annotation *values*
of resources.  For example, if `opts[:search]` is `"pubkeys"`, any resource with
an id containing `"pubkeys"` or an annotation whose value contains `"pubkeys"` will match.

**Notes**

- Annotation *keys* are *not* indexed for full text search.

- Conjur indexes the content of ids and annotation values by word.

- Only resources visible to the current role (either owned by that role or
  having a privilege on it) are returned.

- If you do not provide `:offset` or `:limit`, all records will be returned. For systems
  with a huge number of resources, you may want to paginate as shown in the example below.

- If `:offset` is provided and `:limit` is not, 10 records starting at `:offset` will be
  returned.  You may choose an arbitrarily large number for `:limit`, but the same performance
  considerations apply as when omitting `:offset` and `:limit`.

#### Examples

#####

Search for resources annotated with the text "WebService Route"

```
webservice_routes = api.resources search: "WebService Route"
```

#####

Restrict the search to 'group' resources

```
groups = api.resources kind: 'group'

# Correct behavior:
expect(groups.all?{|g| g.kind == 'group'}).to be_true
```

#####

Get every single resource in a performant way

```
resources = []
limit = 25
offset = 0
until (batch = api.resources limit: limit, offset: offset).empty?
  offset += batch.length
  resources.concat results
end
# do something with your resources
```

Parameters:

-

        options

        (Hash)
      
      
        *(defaults to: {})*
      
      
        —
        

search criteria

Options Hash (options):

-
          :search
          (String)
          
            
          
          
            — 

find resources whose ids or annotations contain this string

-
          :kind
          (String)
          
            
          
          
            — 

find resources whose `kind` matches this string

-
          :limit
          (Integer)
          
            
          
          
            — 

the maximum number of records to return (Conjur may return fewer)

-
          :offset
          (Integer)
          
            
          
          
            — 

offset of the first record to return

-
          :count
          (Boolean)
          
            
          
          
            — 

return a count of records instead of the records themselves when set to true

Returns:

-

        (Array<Conjur::Resource>)

        —
        

the resources matching the criteria given

```

84
85
86
87
88
89
90
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
```

```
# File 'lib/conjur/api/resources.rb', line 84

def resources options = {}
  options = { host: Conjur.configuration.core_url, credentials: credentials }.merge options
  options[:account] ||= Conjur.configuration.account

  host, credentials, account, kind = options.values_at(*[:host, :credentials, :account, :kind])
  fail ArgumentError, "host and account are required" unless [host, account].all?
  %w(host credentials account kind).each do |name|
    options.delete(name.to_sym)
  end

  result = JSON.parse(url_for(:resources, credentials, account, kind, options).get)

  result = result['count'] if result.is_a?(Hash)

  if result.is_a?(Numeric)
    result
  else
    result.map do |result|
      resource(result['id']).tap do |r|
        r.attributes = result
      end
    end
  end
end
```

###
  
    #**revoke_host_factory_token**(token)  ⇒ Object 
  

  

  

  
    

Revokes a host factory token. After revocation, the token can no longer be used to
create hosts.

Parameters:

-

        token

        (String)
      
      
      
        —
        

the host factory token.

```

65
66
67
```

```
# File 'lib/conjur/api/host_factories.rb', line 65

def revoke_host_factory_token token
  self.class.revoke_host_factory_token credentials, token
end
```

###
  
    #**role**(id)  ⇒ Conjur::Role 
  

  

  

  
    

Return a Role representing a role with the given id.  Note that the Role may or
may not exist (see Exists#exists?).

### Permissions

Because this method returns roles that may or may not exist, it doesn't require any permissions to call it:
in fact, it does not perform an HTTP request (except for authentication if necessary).

#### Examples

#####

Create and show a role

```
iggy = api.role 'cat:iggy'
iggy.exists? # true
iggy.members.map(&:member).map(&:id) # => ['conjur:user:admin']
api.current_role.id # => 'conjur:user:admin' # creator role is a member of created role.
```

#####

No permissions are required to call this method

```
api.current_role # => "user:no-access"

# current role is only a member of itself, so it can't see other roles.
api.current_role.memberships.count # => 1
admin = api.role 'user:admin' # OK
admin.exists? # => true
admin.members # => RestClient::Forbidden: 403 Forbidden
```

Parameters:

-

        id

        (String)
      
      
      
        —
        

a fully qualified role identifier

Returns:

-

        (Conjur::Role)

        —
        

an object representing the role

```

54
55
56
```

```
# File 'lib/conjur/api/roles.rb', line 54

def role id
  build_object id, default_class: Role
end
```

###
  
    #**token**  ⇒ Hash 
  

  

  

  
    

The token used to authenticate requests made with the api.  The token will be fetched,
if possible, when not present or about to expire.  Accordingly, this
method may raise a RestClient::Unauthorized exception if the credentials are invalid.

Returns:

-

        (Hash)

        —
        

the authentication token as a Hash

Raises:

-

        (RestClient::Unauthorized)

        —
        

if the username and api key are invalid.

```

154
155
156
157
```

```
# File 'lib/conjur/base.rb', line 154

def token
  refresh_token if needs_token_refresh?
  return @token
end
```

###
  
    #**username**  ⇒ String 
  

  

  

  
    

The name of the user as which this api instance is authenticated.  This is available whether the api
instance was created from credentials or an authentication token. If the instance was created from
credentials, we will use that value directly otherwise we will attempt to extract the username from
the token (either the old-style data field or the new-style JWT `sub` field).

Returns:

-

        (String)

        —
        

the login of the current user.

```

137
138
139
```

```
# File 'lib/conjur/base.rb', line 137

def username
  @username || token['data'] || jwt_username(token)
end
```

###
  
    #**variable_values**(variable_ids)  ⇒ Array<String> 
  

  

  

  
    

Fetch the values of a list of variables.  This operation is more efficient than fetching the
values one by one.

This method will fail unless:

- All of the variables exist

- You have permission to `'execute'` all of the variables

This method is used to implement the `conjur env`
commands.  You may consider using that instead to run your program in an environment with the necessary secrets.

#### Examples

#####

Fetch multiple variable values

```
values = variable_values ['myorg:variable:postgres_uri', 'myorg:variable:aws_secret_access_key', 'myorg:variable:aws_access_key_id']
values # =>
{
   "postgres://...",
   "the-secret-key",
   "the-access-key-id"
}
```

Parameters:

-

        variable_ids

        (Array<String>)
      
      
      
        —
        

list of variable ids to fetch

Returns:

-

        (Array<String>)

        —
        

a list of variable values corresponding to the variable ids.

Raises:

-

        (RestClient::Forbidden, RestClient::ResourceNotFound)

        —
        

if any of the variables don't exist or aren't accessible.

```

50
51
52
53
54
55
```

```
# File 'lib/conjur/api/variables.rb', line 50

def variable_values variable_ids
  raise ArgumentError, "Variables list must be an array" unless variable_ids.kind_of? Array 
  raise ArgumentError, "Variables list is empty" if variable_ids.empty?

  JSON.parse(url_for(:secrets_values, credentials, variable_ids).get.body)
end
```

###
  
    #**whoami**  ⇒ Object 
  

  

  

  
    
      

```

25
26
27
```

```
# File 'lib/conjur/api/authn.rb', line 25

def whoami
  JSON.parse(url_for(:whoami, credentials).get)
end
```
