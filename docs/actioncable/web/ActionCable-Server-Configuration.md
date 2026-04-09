# Class: ActionCable::Server::Configuration
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- ActionCable::Server::Configuration
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/action_cable/server/configuration.rb
  
  

## Overview

  
    

# Action Cable Server Configuration

An instance of this configuration object is available via ActionCable.server.config, which allows you to tweak Action Cable configuration in a Rails config initializer.

  

  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**allow_same_origin_as_host**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute allow_same_origin_as_host.

  

    
      
- 
  
    
      #**allowed_request_origins**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute allowed_request_origins.

  

    
      
- 
  
    
      #**cable**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute cable.

  

    
      
- 
  
    
      #**connection_class**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute connection_class.

  

    
      
- 
  
    
      #**disable_request_forgery_protection**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute disable_request_forgery_protection.

  

    
      
- 
  
    
      #**filter_parameters**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute filter_parameters.

  

    
      
- 
  
    
      #**health_check_application**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute health_check_application.

  

    
      
- 
  
    
      #**health_check_path**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute health_check_path.

  

    
      
- 
  
    
      #**log_tags**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute log_tags.

  

    
      
- 
  
    
      #**logger**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute logger.

  

    
      
- 
  
    
      #**mount_path**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute mount_path.

  

    
      
- 
  
    
      #**precompile_assets**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute precompile_assets.

  

    
      
- 
  
    
      #**url**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute url.

  

    
      
- 
  
    
      #**worker_pool_size**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute worker_pool_size.

  

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**initialize**  ⇒ Configuration 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Configuration.

  

      
        
- 
  
    
      #**pubsub_adapter**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Returns constant of subscription adapter specified in config/cable.yml.

  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**  ⇒ Configuration 
  

  

  

  
    

Returns a new instance of Configuration.

  

  

  
    
      

```

22
23
24
25
26
27
28
29
30
31
32
33
34
35
```

    
    
      

```
# File 'lib/action_cable/server/configuration.rb', line 22

def initialize
  @log_tags = []

  @connection_class = -> { ActionCable::Connection::Base }
  @worker_pool_size = 4

  @disable_request_forgery_protection = false
  @allow_same_origin_as_host = true
  @filter_parameters = []

  @health_check_application = ->(env) {
    [200, { Rack::CONTENT_TYPE => "text/html", "date" => Time.now.httpdate }, []]
  }
end
```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**allow_same_origin_as_host**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute allow_same_origin_as_host.

  

  

  
    
      

```

17
18
19
```

    
    
      

```
# File 'lib/action_cable/server/configuration.rb', line 17

def allow_same_origin_as_host
  @allow_same_origin_as_host
end
```

    
  

    
      
      
      
  
### 
  
    #**allowed_request_origins**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute allowed_request_origins.

  

  

  
    
      

```

17
18
19
```

    
    
      

```
# File 'lib/action_cable/server/configuration.rb', line 17

def allowed_request_origins
  @allowed_request_origins
end
```

    
  

    
      
      
      
  
### 
  
    #**cable**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute cable.

  

  

  
    
      

```

18
19
20
```

    
    
      

```
# File 'lib/action_cable/server/configuration.rb', line 18

def cable
  @cable
end
```

    
  

    
      
      
      
  
### 
  
    #**connection_class**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute connection_class.

  

  

  
    
      

```

16
17
18
```

    
    
      

```
# File 'lib/action_cable/server/configuration.rb', line 16

def connection_class
  @connection_class
end
```

    
  

    
      
      
      
  
### 
  
    #**disable_request_forgery_protection**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute disable_request_forgery_protection.

  

  

  
    
      

```

17
18
19
```

    
    
      

```
# File 'lib/action_cable/server/configuration.rb', line 17

def disable_request_forgery_protection
  @disable_request_forgery_protection
end
```

    
  

    
      
      
      
  
### 
  
    #**filter_parameters**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute filter_parameters.

  

  

  
    
      

```

17
18
19
```

    
    
      

```
# File 'lib/action_cable/server/configuration.rb', line 17

def filter_parameters
  @filter_parameters
end
```

    
  

    
      
      
      
  
### 
  
    #**health_check_application**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute health_check_application.

  

  

  
    
      

```

20
21
22
```

    
    
      

```
# File 'lib/action_cable/server/configuration.rb', line 20

def health_check_application
  @health_check_application
end
```

    
  

    
      
      
      
  
### 
  
    #**health_check_path**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute health_check_path.

  

  

  
    
      

```

20
21
22
```

    
    
      

```
# File 'lib/action_cable/server/configuration.rb', line 20

def health_check_path
  @health_check_path
end
```

    
  

    
      
      
      
  
### 
  
    #**log_tags**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute log_tags.

  

  

  
    
      

```

15
16
17
```

    
    
      

```
# File 'lib/action_cable/server/configuration.rb', line 15

def log_tags
  @log_tags
end
```

    
  

    
      
      
      
  
### 
  
    #**logger**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute logger.

  

  

  
    
      

```

15
16
17
```

    
    
      

```
# File 'lib/action_cable/server/configuration.rb', line 15

def logger
  @logger
end
```

    
  

    
      
      
      
  
### 
  
    #**mount_path**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute mount_path.

  

  

  
    
      

```

18
19
20
```

    
    
      

```
# File 'lib/action_cable/server/configuration.rb', line 18

def mount_path
  @mount_path
end
```

    
  

    
      
      
      
  
### 
  
    #**precompile_assets**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute precompile_assets.

  

  

  
    
      

```

19
20
21
```

    
    
      

```
# File 'lib/action_cable/server/configuration.rb', line 19

def precompile_assets
  @precompile_assets
end
```

    
  

    
      
      
      
  
### 
  
    #**url**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute url.

  

  

  
    
      

```

18
19
20
```

    
    
      

```
# File 'lib/action_cable/server/configuration.rb', line 18

def url
  @url
end
```

    
  

    
      
      
      
  
### 
  
    #**worker_pool_size**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute worker_pool_size.

  

  

  
    
      

```

16
17
18
```

    
    
      

```
# File 'lib/action_cable/server/configuration.rb', line 16

def worker_pool_size
  @worker_pool_size
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**pubsub_adapter**  ⇒ Object 
  

  

  

  
    

Returns constant of subscription adapter specified in config/cable.yml. If the adapter cannot be found, this will default to the Redis adapter. Also makes sure proper dependencies are required.

  

  

  
    
      

```

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
50
51
52
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
63
64
65
66
67
```

    
    
      

```
# File 'lib/action_cable/server/configuration.rb', line 40

def pubsub_adapter
  adapter = (cable.fetch("adapter") { "redis" })

  # Require the adapter itself and give useful feedback about
  #     1. Missing adapter gems and
  #     2. Adapter gems' missing dependencies.
  path_to_adapter = "action_cable/subscription_adapter/#{adapter}"
  begin
    require path_to_adapter
  rescue LoadError => e
    # We couldn't require the adapter itself. Raise an exception that points out
    # config typos and missing gems.
    if e.path == path_to_adapter
      # We can assume that a non-builtin adapter was specified, so it's either
      # misspelled or missing from Gemfile.
      raise e.class, "Could not load the '#{adapter}' Action Cable pubsub adapter. Ensure that the adapter is spelled correctly in config/cable.yml and that you've added the necessary adapter gem to your Gemfile.", e.backtrace

    # Bubbled up from the adapter require. Prefix the exception message with some
    # guidance about how to address it and reraise.
    else
      raise e.class, "Error loading the '#{adapter}' Action Cable pubsub adapter. Missing a gem it depends on? #{e.message}", e.backtrace
    end
  end

  adapter = adapter.camelize
  adapter = "PostgreSQL" if adapter == "Postgresql"
  "ActionCable::SubscriptionAdapter::#{adapter}".constantize
end
```