# Module: Conjur::API::Router
  
      Extended by:
      Router, Escape::ClassMethods
  
  
  
  
  

  
  
    Included in:
    Router
  
  

  
  
    Defined in:
    lib/conjur/api/router.rb
  
## Overview

Router translates method arguments to rest-ful API request parameters.
because of this, most of the methods suffer from :reek:LongParameterList:
and :reek:UtilityFunction:

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**authentication_providers**(account, authenticator, credentials)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**authenticator**(account, authenticator, service_id, credentials)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**authenticator_authenticate**(account, service_id, authenticator, options)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**authenticators**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**authn_authenticate**(account, username)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**authn_authenticate_local**(username, account, expiration, cidr, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

The authn-local message is a JSON string with account, sub, and optional fields.

-
  
      #**authn_login**(account, username, password)  ⇒ Object 

-
  
      #**authn_rotate_api_key**(credentials, account, id)  ⇒ Object 

-
  
      #**authn_rotate_own_api_key**(account, username, password)  ⇒ Object 

-
  
      #**authn_update_password**(account, username, password)  ⇒ Object 

-
  
      #**group_attributes**(credentials, resource, id)  ⇒ Object 

-
  
      #**host_factory_create_host**(token)  ⇒ Object 

-
  
      #**host_factory_create_tokens**(credentials, id)  ⇒ Object 

-
  
      #**host_factory_revoke_token**(credentials, token)  ⇒ Object 

-
  
      #**ldap_sync_policy**(credentials, config_name)  ⇒ Object 

-
  
      #**parse_group_gidnumber**(attributes)  ⇒ Object 

-
  
      #**parse_members**(credentials, result)  ⇒ Object 

-
  
      #**parse_user_uidnumber**(attributes)  ⇒ Object 

-
  
      #**parse_variable_kind**(attributes)  ⇒ Object 

-
  
      #**parse_variable_mime_type**(attributes)  ⇒ Object 

-
  
      #**policies_load_policy**(credentials, account, id)  ⇒ Object 

-
  
      #**public_keys_for_user**(account, username)  ⇒ Object 

-
  
      #**resources**(credentials, account, kind, options)  ⇒ Object 

-
  
      #**resources_check**(credentials, id, privilege, role)  ⇒ Object 

-
  
      #**resources_permitted_roles**(credentials, id, privilege)  ⇒ Object 

-
  
      #**resources_resource**(credentials, id)  ⇒ Object 

-
  
      #**roles_role**(credentials, id)  ⇒ Object 

-
  
      #**secrets_add**(credentials, id)  ⇒ Object 

-
  
      #**secrets_value**(credentials, id, options)  ⇒ Object 

-
  
      #**secrets_values**(credentials, variable_ids)  ⇒ Object 

-
  
      #**user_attributes**(credentials, resource, id)  ⇒ Object 

-
  
      #**variable_attributes**(credentials, resource, id)  ⇒ Object 

-
  
      #**whoami**(credentials)  ⇒ Object 

### Methods included from Escape::ClassMethods

fully_escape, path_escape, path_or_query_escape, query_escape

## Instance Method Details

###
  
    #**authentication_providers**(account, authenticator, credentials)  ⇒ Object 
  

  

  

  
    
      

```

66
67
68
69
70
71
```

```
# File 'lib/conjur/api/router.rb', line 66

def authentication_providers(account, authenticator, credentials)
  RestClient::Resource.new(
    Conjur.configuration.core_url,
    Conjur.configuration.create_rest_client_options(credentials)
  )[fully_escape authenticator][fully_escape account]['providers']
end
```

###
  
    #**authenticator**(account, authenticator, service_id, credentials)  ⇒ Object 
  

  

  

  
    
      

```

52
53
54
55
56
57
```

```
# File 'lib/conjur/api/router.rb', line 52

def authenticator account, authenticator, service_id, credentials
  RestClient::Resource.new(
    Conjur.configuration.core_url,
    Conjur.configuration.create_rest_client_options(credentials)
  )[fully_escape authenticator][fully_escape service_id][fully_escape account]
end
```

###
  
    #**authenticator_authenticate**(account, service_id, authenticator, options)  ⇒ Object 
  

  

  

  
    
      

```

45
46
47
48
49
50
```

```
# File 'lib/conjur/api/router.rb', line 45

def authenticator_authenticate(account, service_id, authenticator, options)
  RestClient::Resource.new(
    Conjur.configuration.core_url,
    Conjur.configuration.rest_client_options
  )[fully_escape authenticator][fully_escape service_id][fully_escape account]['authenticate'][options_querystring options]
end
```

###
  
    #**authenticators**  ⇒ Object 
  

  

  

  
    
      

```

59
60
61
62
63
64
```

```
# File 'lib/conjur/api/router.rb', line 59

def authenticators
  RestClient::Resource.new(
    Conjur.configuration.core_url,
    Conjur.configuration.rest_client_options
  )['authenticators']
end
```

###
  
    #**authn_authenticate**(account, username)  ⇒ Object 
  

  

  

  
    
      

```

38
39
40
41
42
43
```

```
# File 'lib/conjur/api/router.rb', line 38

def authn_authenticate account, username
  RestClient::Resource.new(
    Conjur.configuration.authn_url,
    Conjur.configuration.rest_client_options
  )[fully_escape account][fully_escape username]['authenticate']
end
```

###
  
    #**authn_authenticate_local**(username, account, expiration, cidr, &block)  ⇒ Object 
  

  

  

  
    

The authn-local message is a JSON string with account, sub, and optional fields.

```

74
75
76
77
78
79
```

```
# File 'lib/conjur/api/router.rb', line 74

def authn_authenticate_local username, account, expiration, cidr, &block
  { account: account, sub: username }.tap do |params|
    params[:exp] = expiration if expiration
    params[:cidr] = cidr if cidr
  end.to_json
end
```

###
  
    #**authn_login**(account, username, password)  ⇒ Object 
  

  

  

  
    
      

```

28
29
30
31
32
33
34
35
36
```

```
# File 'lib/conjur/api/router.rb', line 28

def authn_login account, username, password
  RestClient::Resource.new(
    Conjur.configuration.authn_url,
    Conjur.configuration.create_rest_client_options(
      user: username,
      password: password
    )
  )[fully_escape account]['login']
end
```

###
  
    #**authn_rotate_api_key**(credentials, account, id)  ⇒ Object 
  

  

  

  
    
      

```

91
92
93
94
95
96
```

```
# File 'lib/conjur/api/router.rb', line 91

def authn_rotate_api_key credentials, account, id
  RestClient::Resource.new(
    Conjur.configuration.core_url,
    Conjur.configuration.create_rest_client_options(credentials)
  )['authn'][fully_escape account]["api_key?role=#{id}"]
end
```

###
  
    #**authn_rotate_own_api_key**(account, username, password)  ⇒ Object 
  

  

  

  
    
      

```

98
99
100
101
102
103
104
105
106
```

```
# File 'lib/conjur/api/router.rb', line 98

def authn_rotate_own_api_key account, username, password
  RestClient::Resource.new(
    Conjur.configuration.authn_url,
    Conjur.configuration.create_rest_client_options(
      user: username,
      password: password
    )
  )[fully_escape account]['api_key']
end
```

###
  
    #**authn_update_password**(account, username, password)  ⇒ Object 
  

  

  

  
    
      

```

81
82
83
84
85
86
87
88
89
```

```
# File 'lib/conjur/api/router.rb', line 81

def authn_update_password account, username, password
  RestClient::Resource.new(
    Conjur.configuration.authn_url,
    Conjur.configuration.create_rest_client_options(
      user: username,
      password: password
    )
  )[fully_escape account]['password']
end
```

###
  
    #**group_attributes**(credentials, resource, id)  ⇒ Object 
  

  

  

  
    
      

```

211
212
213
```

```
# File 'lib/conjur/api/router.rb', line 211

def group_attributes credentials, resource, id
  resource_annotations resource
end
```

###
  
    #**host_factory_create_host**(token)  ⇒ Object 
  

  

  

  
    
      

```

108
109
110
111
112
113
114
115
116
```

```
# File 'lib/conjur/api/router.rb', line 108

def host_factory_create_host token
  http_options = {
    headers: { authorization: %Q(Token token="#{token}") }
  }
  RestClient::Resource.new(
    Conjur.configuration.core_url,
    Conjur.configuration.create_rest_client_options(http_options)
  )["host_factories"]["hosts"]
end
```

###
  
    #**host_factory_create_tokens**(credentials, id)  ⇒ Object 
  

  

  

  
    
      

```

118
119
120
121
122
123
```

```
# File 'lib/conjur/api/router.rb', line 118

def host_factory_create_tokens credentials, id
  RestClient::Resource.new(
    Conjur.configuration.core_url,
    Conjur.configuration.create_rest_client_options(credentials)
  )['host_factory_tokens']
end
```

###
  
    #**host_factory_revoke_token**(credentials, token)  ⇒ Object 
  

  

  

  
    
      

```

125
126
127
128
129
130
```

```
# File 'lib/conjur/api/router.rb', line 125

def host_factory_revoke_token credentials, token
  RestClient::Resource.new(
    Conjur.configuration.core_url,
    Conjur.configuration.create_rest_client_options(credentials)
  )['host_factory_tokens'][token]
end
```

###
  
    #**ldap_sync_policy**(credentials, config_name)  ⇒ Object 
  

  

  

  
    
      

```

245
246
247
248
249
250
```

```
# File 'lib/conjur/api/router.rb', line 245

def ldap_sync_policy(credentials, config_name)
  RestClient::Resource.new(
    Conjur.configuration.core_url,
    Conjur.configuration.create_rest_client_options(credentials)
  )['ldap-sync']["policy?config_name=#{fully_escape(config_name)}"]
end
```

###
  
    #**parse_group_gidnumber**(attributes)  ⇒ Object 
  

  

  

  
    
      

```

223
224
225
```

```
# File 'lib/conjur/api/router.rb', line 223

def parse_group_gidnumber attributes
  HasAttributes.annotation_value attributes, 'conjur/gidnumber'
end
```

###
  
    #**parse_members**(credentials, result)  ⇒ Object 
  

  

  

  
    
      

```

239
240
241
242
243
```

```
# File 'lib/conjur/api/router.rb', line 239

def parse_members credentials, result
  result.map do |json|
    RoleGrant.parse_from_json(json, credentials)
  end
end
```

###
  
    #**parse_user_uidnumber**(attributes)  ⇒ Object 
  

  

  

  
    
      

```

227
228
229
```

```
# File 'lib/conjur/api/router.rb', line 227

def parse_user_uidnumber attributes
  HasAttributes.annotation_value attributes, 'conjur/uidnumber'
end
```

###
  
    #**parse_variable_kind**(attributes)  ⇒ Object 
  

  

  

  
    
      

```

231
232
233
```

```
# File 'lib/conjur/api/router.rb', line 231

def parse_variable_kind attributes
  HasAttributes.annotation_value attributes, 'conjur/kind'
end
```

###
  
    #**parse_variable_mime_type**(attributes)  ⇒ Object 
  

  

  

  
    
      

```

235
236
237
```

```
# File 'lib/conjur/api/router.rb', line 235

def parse_variable_mime_type attributes
  HasAttributes.annotation_value attributes, 'conjur/mime_type'
end
```

###
  
    #**policies_load_policy**(credentials, account, id)  ⇒ Object 
  

  

  

  
    
      

```

132
133
134
135
136
137
```

```
# File 'lib/conjur/api/router.rb', line 132

def policies_load_policy credentials, account, id
  RestClient::Resource.new(
    Conjur.configuration.core_url,
    Conjur.configuration.create_rest_client_options(credentials)
  )['policies'][fully_escape account]['policy'][fully_escape id]
end
```

###
  
    #**public_keys_for_user**(account, username)  ⇒ Object 
  

  

  

  
    
      

```

139
140
141
142
143
144
```

```
# File 'lib/conjur/api/router.rb', line 139

def public_keys_for_user account, username
  RestClient::Resource.new(
    Conjur.configuration.core_url,
    Conjur.configuration.rest_client_options
  )['public_keys'][fully_escape account]['user'][fully_escape username]
end
```

###
  
    #**resources**(credentials, account, kind, options)  ⇒ Object 
  

  

  

  
    
      

```

146
147
148
149
150
151
152
153
154
155
156
```

```
# File 'lib/conjur/api/router.rb', line 146

def resources credentials, account, kind, options
  credentials ||= {}

  path = "/resources/#{fully_escape account}"
  path += "/#{fully_escape kind}" if kind

  RestClient::Resource.new(
    Conjur.configuration.core_url,
    Conjur.configuration.create_rest_client_options(credentials)
  )[path][options_querystring options]
end
```

###
  
    #**resources_check**(credentials, id, privilege, role)  ⇒ Object 
  

  

  

  
    
      

```

172
173
174
175
176
177
178
```

```
# File 'lib/conjur/api/router.rb', line 172

def resources_check credentials, id, privilege, role
  options = {}
  options[:check] = true
  options[:privilege] = privilege
  options[:role] = query_escape(Id.new(role)) if role
  resources_resource(credentials, id)[options_querystring options].get
end
```

###
  
    #**resources_permitted_roles**(credentials, id, privilege)  ⇒ Object 
  

  

  

  
    
      

```

165
166
167
168
169
170
```

```
# File 'lib/conjur/api/router.rb', line 165

def resources_permitted_roles credentials, id, privilege
  options = {}
  options[:permitted_roles] = true
  options[:privilege] = privilege
  resources_resource(credentials, id)[options_querystring options]
end
```

###
  
    #**resources_resource**(credentials, id)  ⇒ Object 
  

  

  

  
    
      

```

158
159
160
161
162
163
```

```
# File 'lib/conjur/api/router.rb', line 158

def resources_resource credentials, id
  RestClient::Resource.new(
    Conjur.configuration.core_url,
    Conjur.configuration.create_rest_client_options(credentials)
  )['resources'][id.to_url_path]
end
```

###
  
    #**roles_role**(credentials, id)  ⇒ Object 
  

  

  

  
    
      

```

180
181
182
183
184
185
```

```
# File 'lib/conjur/api/router.rb', line 180

def roles_role credentials, id
  RestClient::Resource.new(
    Conjur.configuration.core_url,
    Conjur.configuration.create_rest_client_options(credentials)
  )['roles'][id.to_url_path]
end
```

###
  
    #**secrets_add**(credentials, id)  ⇒ Object 
  

  

  

  
    
      

```

187
188
189
190
191
192
```

```
# File 'lib/conjur/api/router.rb', line 187

def secrets_add credentials, id
  RestClient::Resource.new(
    Conjur.configuration.core_url,
    Conjur.configuration.create_rest_client_options(credentials)
  )['secrets'][id.to_url_path]
end
```

###
  
    #**secrets_value**(credentials, id, options)  ⇒ Object 
  

  

  

  
    
      

```

194
195
196
197
198
199
```

```
# File 'lib/conjur/api/router.rb', line 194

def secrets_value credentials, id, options
  RestClient::Resource.new(
    Conjur.configuration.core_url,
    Conjur.configuration.create_rest_client_options(credentials)
  )['secrets'][id.to_url_path][options_querystring options]
end
```

###
  
    #**secrets_values**(credentials, variable_ids)  ⇒ Object 
  

  

  

  
    
      

```

201
202
203
204
205
206
207
208
209
```

```
# File 'lib/conjur/api/router.rb', line 201

def secrets_values credentials, variable_ids
  options = {
    variable_ids: Array(variable_ids).join(',')
  }
  RestClient::Resource.new(
    Conjur.configuration.core_url,
    Conjur.configuration.create_rest_client_options(credentials)
  )['secrets'][options_querystring(options).gsub("%2C", ',')]
end
```

###
  
    #**user_attributes**(credentials, resource, id)  ⇒ Object 
  

  

  

  
    
      

```

219
220
221
```

```
# File 'lib/conjur/api/router.rb', line 219

def user_attributes credentials, resource, id
  resource_annotations resource
end
```

###
  
    #**variable_attributes**(credentials, resource, id)  ⇒ Object 
  

  

  

  
    
      

```

215
216
217
```

```
# File 'lib/conjur/api/router.rb', line 215

def variable_attributes credentials, resource, id
  resource_annotations resource
end
```

###
  
    #**whoami**(credentials)  ⇒ Object 
  

  

  

  
    
      

```

252
253
254
255
256
257
```

```
# File 'lib/conjur/api/router.rb', line 252

def whoami(credentials)
  RestClient::Resource.new(
    Conjur.configuration.core_url,
    Conjur.configuration.create_rest_client_options(credentials)
  )['whoami']
end
```
