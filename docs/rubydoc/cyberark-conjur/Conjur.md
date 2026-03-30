# Module: Conjur
  
    Defined in:
    lib/conjur/host.rb,

  lib/conjur/id.rb,
 lib/conjur/log.rb,
 lib/conjur/base.rb,
 lib/conjur/cidr.rb,
 lib/conjur/role.rb,
 lib/conjur/user.rb,
 lib/conjur/cache.rb,
 lib/conjur/group.rb,
 lib/conjur/layer.rb,
 lib/conjur/config.rb,
 lib/conjur/escape.rb,
 lib/conjur/policy.rb,
 lib/conjur/routing.rb,
 lib/conjur/resource.rb,
 lib/conjur/variable.rb,
 lib/conjur/api/authn.rb,
 lib/conjur/api/roles.rb,
 lib/conjur/api/router.rb,
 lib/conjur/cert_utils.rb,
 lib/conjur/exceptions.rb,
 lib/conjur/log_source.rb,
 lib/conjur/role_grant.rb,
 lib/conjur/webservice.rb,
 lib/conjur-api/version.rb,
 lib/conjur/api/pubkeys.rb,
 lib/conjur/base_object.rb,
 lib/conjur/acts_as_role.rb,
 lib/conjur/acts_as_user.rb,
 lib/conjur/api/policies.rb,
 lib/conjur/build_object.rb,
 lib/conjur/host_factory.rb,
 lib/conjur/api/ldap_sync.rb,
 lib/conjur/api/resources.rb,
 lib/conjur/api/variables.rb,
 lib/conjur/configuration.rb,
 lib/conjur/has_attributes.rb,
 lib/conjur/acts_as_resource.rb,
 lib/conjur/acts_as_rolsource.rb,
 lib/conjur/api/authenticators.rb,
 lib/conjur/api/host_factories.rb,
 lib/conjur/host_factory_token.rb,
 lib/conjur/policy_load_result.rb

## Overview

Copyright 2013-2017 Conjur Inc

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Defined Under Namespace

      **Modules:** ActsAsResource, ActsAsRole, ActsAsRolsource, ActsAsUser, BuildObject, CIDR, CertUtils, Escape, HasAttributes, LogSource, Routing
    
  
    
      **Classes:** API, BaseCache, BaseObject, Config, Configuration, FeatureNotAvailable, Group, Host, HostFactory, HostFactoryToken, Id, Layer, Policy, PolicyLoadResult, Resource, Role, RoleGrant, User, Variable, Webservice
    
  

  
    
##

      Constant Summary
      collapse
    

    
      
        @@env_log =
          
        
        

```
create_log ENV['CONJURAPI_LOG']
```

        @@log =
          
        
        

```
nil
```

        @@cache =
          
        
        

```
BaseCache.new
```

##

      Class Method Summary
      collapse
    

    

      
        
-
  
      .**cache**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Gets the global cache.

-
  
      .**cache=**(cache)  ⇒ Object 

Sets the global cache.

-
  
      .**cache_key**(username, url, path = nil)  ⇒ Object 

Builds a cache key from a +username+, +url+ and optional +path+.

-
  
      .**configuration**  ⇒ Conjur::Configuration 

      (also: config)
    
  
  
  
  
  
  
  
  

  
    

Gets the current thread-local or global configuration.

-
  
      .**configuration=**(config)  ⇒ Conjur::Configuration 

      (also: config=)
    
  
  
  
  
  
  
  
  

  
    

Sets the global configuration.

-
  
      .**configure** {|c| ... } ⇒ Object 

Configure Conjur with a block.

-
  
      .**log=**(log)  

Assign a Logger for use by Conjur API methods.

-
  
      .**with_configuration**(config)  

Saves the current thread local Configuration, sets the thread local Configuration to `config`, yields to the block, and ensures that the original thread local configuration is restored.

## Class Method Details

###
  
    .**cache**  ⇒ Object 
  

  

  

  
    

Gets the global cache.

```

19
```

```
# File 'lib/conjur/cache.rb', line 19

def cache; @@cache; end
```

###
  
    .**cache=**(cache)  ⇒ Object 
  

  

  

  
    

Sets the global cache. It should implement +fetch_:method+ methods.
The easy way to accomplish this is to extend BaseCache.

```

14
15
16
```

```
# File 'lib/conjur/cache.rb', line 14

def cache= cache
  @@cache = cache
end
```

###
  
    .**cache_key**(username, url, path = nil)  ⇒ Object 
  

  

  

  
    

Builds a cache key from a +username+, +url+ and optional +path+.

```

22
23
24
```

```
# File 'lib/conjur/cache.rb', line 22

def cache_key username, url, path = nil
  [ username, [ url, path ].compact.join ].join(".")
end
```

###
  
    .**configuration**  ⇒ Conjur::Configuration 
  

  
    Also known as:
    config
    
  

  

  
    

Gets the current thread-local or global configuration.

The thread-local Conjur configuration can only be set using the with_configuration
method.  This method will try to return that value first, then the global configuration as
set with configuration= (which is lazily initialized if not set).

Returns:

-

        (Conjur::Configuration)

        —
        

the thread-local or global Conjur configuration.

```

80
81
82
```

```
# File 'lib/conjur/configuration.rb', line 80

def configuration
  Thread.current[:conjur_configuration] || (@config ||= Configuration.new)
end
```

###
  
    .**configuration=**(config)  ⇒ Conjur::Configuration 
  

  
    Also known as:
    config=
    
  

  

  
    

Sets the global configuration.

This method *has no effect* on the thread local configuration.  Use with_configuration instead if
that's what you want.

Parameters:

-

        config

        (Conjur::Configuration)
      
      
      
        —
        

the new configuration

Returns:

-

        (Conjur::Configuration)

        —
        

the new value of the configuration

```

91
92
93
```

```
# File 'lib/conjur/configuration.rb', line 91

def configuration=(config)
  @config = config
end
```

###
  
    .**configure** {|c| ... } ⇒ Object 
  

  

  

  
    

Configure Conjur with a block.

#### Examples

```
Conjur.configure do |c|
  c.account = 'some-account'
  c.appliance_url = 'https://conjur.companyname.com/api'
end
```

Yield Parameters:

-

        c

        (Conjur::Configuration)
      
      
      
        —
        

the configuration instance to modify.

```

107
108
109
```

```
# File 'lib/conjur/configuration.rb', line 107

def configure
  yield configuration
end
```

###
  
    .**log=**(log)  
  

  

  

  
    

This method returns an undefined value.

Assign a Logger for use by Conjur API methods.  This method accepts
several argument forms:

- The strings 'stdout' and 'stderr' cause log messages to be sent to the corresponding stream.

- Other stings are treated as paths and will cause log messages to be sent to those files.

- A `Logger` instance will be used as is.

Note that the logger specified by the `CONJURAPI_LOG` environment variable will override
the value set here.

Parameters:

-

        log

        (String, Logger, nil)
      
      
      
        —
        

the new logger to use

```

35
36
37
```

```
# File 'lib/conjur/log.rb', line 35

def self.log= log
  @@log = create_log log
end
```

###
  
    .**with_configuration**(config)  
  

  

  

  
    

This method returns an undefined value.

Saves the current thread local Configuration,
sets the thread local Configuration to `config`, yields to the block, and ensures that
the original thread local configuration is restored.

Because Conjur configuration is accessed from the 'global' configuration method by all Conjur
API methods, this method provides the ability to set a thread local value for use within the current,
or within a block in a single threaded application.

Note that the configuration= method sets the *global* Configuration, not the thread-local
value.

#### Examples

#####

Override Configuration in a Thread

```
# in this rather contrived example, we'll override the {Conjur::Configuration#appliance_url} parameter
# used by calls within a thread.

# Set up the configuration in the main thread
Conjur.configure do |c|
  # ...
  c.appliance_url = 'https://conjur.main-url.com/api'
end

# Start a new thread that will perform requests to another server.  In practice, you might
# have a web server that uses a Conjur endpoint specified by a request header.
Thread.new do
   Conjur.with_configuration Conjur.config.clone(appliance_url: 'https://conjur.local-url.com/api') do
      sleep 2
      puts "Thread local url is #{Conjur.config.appliance_url}"
   end
end
puts "Global url is #{Conjur.config.appliance_url}"
# Outputs:
Global url is https://conjur.main-url.com/api
Thread local url is https://conjur.local-url.com/api
```

```

65
66
67
68
69
70
71
```

```
# File 'lib/conjur/configuration.rb', line 65

def with_configuration(config)
  oldvalue = Thread.current[:conjur_configuration]
  Thread.current[:conjur_configuration] = config
  yield
ensure
  Thread.current[:conjur_configuration] = oldvalue
end
```
