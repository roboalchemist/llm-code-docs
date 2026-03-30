# Class: Brakeman::CheckDefaultRoutes
  
  
  

  
  
    Inherits:
    
      BaseCheck
      
        

          
- Object
          
            
- SexpProcessor
          
            
- BaseCheck
          
            
- Brakeman::CheckDefaultRoutes
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/brakeman/checks/check_default_routes.rb
  
  

## Overview

  
    

Checks if default routes are allowed in routes.rb

  

  

  
## Constant Summary

  
  
### Constants inherited
     from BaseCheck

  

BaseCheck::CONFIDENCE

  
  
  
### Constants included
     from Util

  

Util::ALL_COOKIES, Util::ALL_PARAMETERS, Util::COOKIES, Util::COOKIES_SEXP, Util::DIR_CONST, Util::LITERALS, Util::PARAMETERS, Util::PARAMS_SEXP, Util::PATH_PARAMETERS, Util::QUERY_PARAMETERS, Util::REQUEST_COOKIES, Util::REQUEST_ENV, Util::REQUEST_PARAMETERS, Util::REQUEST_PARAMS, Util::REQUEST_REQUEST_PARAMETERS, Util::SAFE_LITERAL, Util::SESSION, Util::SESSION_SEXP, Util::SIMPLE_LITERALS

  
  
  
### Constants inherited
     from SexpProcessor

  

SexpProcessor::VERSION

  
## Instance Attribute Summary

  
  
### Attributes inherited from BaseCheck

  

#tracker, #warnings

  
  
  
### Attributes inherited from SexpProcessor

  

#context, #env, #expected

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**allow_all_actions?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**check_for_action_globs**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**check_for_cve_2014_0130**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**check_for_default_routes**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**(*args)  ⇒ CheckDefaultRoutes 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of CheckDefaultRoutes.

  

      
        
- 
  
    
      #**run_check**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Checks for :allow_all_actions globally and for individual routes if it is not enabled globally.

  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from BaseCheck

  

#add_result, description, inherited, #process_array, #process_call, #process_cookies, #process_default, #process_dstr, #process_if, #process_params

  
  
  
  
  
  
  
  
  
### Methods included from Messages

  

#msg, #msg_code, #msg_cve, #msg_file, #msg_input, #msg_lit, #msg_plain, #msg_version

  
  
  
  
  
  
  
  
  
### Methods included from Util

  

#all_literals?, #array?, #block?, #call?, #camelize, #class_name, #constant?, #contains_class?, #cookies?, #dir_glob?, #false?, #hash?, #hash_access, #hash_insert, #hash_iterate, #hash_values, #integer?, #kwsplat?, #literal?, #make_call, #node_type?, #number?, #params?, #pluralize, #rails_version, #recurse_check?, #regexp?, #remove_kwsplat, #request_headers?, #request_value?, #result?, #safe_literal, #safe_literal?, #safe_literal_target?, #set_env_defaults, #sexp?, #simple_literal?, #string?, #string_interp?, #symbol?, #template_path_to_name, #true?, #underscore

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
### Methods included from ProcessorHelper

  

#current_file, #process_all, #process_all!, #process_call_args, #process_call_defn?, #process_class, #process_module

  
  
  
  
  
  
  
  
  
### Methods inherited from SexpProcessor

  

#in_context, #process, processors, #scope

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(*args)  ⇒ CheckDefaultRoutes 
  

  

  

  
    

Returns a new instance of CheckDefaultRoutes.

  

  

  
    
      

```

9
10
11
12
```

    
    
      

```
# File 'lib/brakeman/checks/check_default_routes.rb', line 9

def initialize *args
  super
  @actions_allowed_on_controller = nil
end
```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**allow_all_actions?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

91
92
93
```

    
    
      

```
# File 'lib/brakeman/checks/check_default_routes.rb', line 91

def allow_all_actions?
  tracker.routes[:allow_all_actions]
end
```

    
  

    
      
  
### 
  
    #**check_for_action_globs**  ⇒ Object 
  

  

  

  
    
      

```

35
36
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
50
51
52
53
54
55
56
57
```

    
    
      

```
# File 'lib/brakeman/checks/check_default_routes.rb', line 35

def check_for_action_globs
  return if allow_all_actions?
  Brakeman.debug "Checking each controller for default routes"

  tracker.routes.each do |name, actions|
    if actions.is_a? Array and actions[0] == :allow_all_actions
      @actions_allowed_on_controller = true
      if actions[1].is_a? Hash and actions[1][:allow_verb]
        verb = actions[1][:allow_verb]
      else
        verb = "any"
      end
      warn :controller => name,
        :warning_type => "Default Routes",
        :warning_code => :controller_default_routes,
        :message => msg("Any public method in ", msg_code(name), " can be used as an action for ", msg_code(verb), " requests."),
        :line => actions[2],
        :confidence => :medium,
        :file => "#{tracker.app_path}/config/routes.rb",
        :cwe_id => [22]
    end
  end
end
```

    
  

    
      
  
### 
  
    #**check_for_cve_2014_0130**  ⇒ Object 
  

  

  

  
    
      

```

59
60
61
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
72
73
74
75
76
77
78
79
80
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
# File 'lib/brakeman/checks/check_default_routes.rb', line 59

def check_for_cve_2014_0130
  case
  when lts_version?("2.3.18.9")
    #TODO: Should support LTS 3.0.20 too
    return
  when version_between?("2.0.0", "2.3.18")
    upgrade = "3.2.18"
  when version_between?("3.0.0", "3.2.17")
    upgrade = "3.2.18"
  when version_between?("4.0.0", "4.0.4")
    upgrade = "4.0.5"
  when version_between?("4.1.0", "4.1.0")
    upgrade = "4.1.1"
  else
    return
  end

  if allow_all_actions? or @actions_allowed_on_controller
    confidence = :high
  else
    confidence = :medium
  end

  warn :warning_type => "Remote Code Execution",
    :warning_code => :CVE_2014_0130,
    :message => msg(msg_version(rails_version), " with globbing routes is vulnerable to directory traversal and remote code execution. Patch or upgrade to ", msg_version(upgrade)),
    :confidence => confidence,
    :file => "#{tracker.app_path}/config/routes.rb",
    :link => "http://matasano.com/research/AnatomyOfRailsVuln-CVE-2014-0130.pdf",
    :cwe_id => [22]
end
```

    
  

    
      
  
### 
  
    #**check_for_default_routes**  ⇒ Object 
  

  

  

  
    
      

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
```

    
    
      

```
# File 'lib/brakeman/checks/check_default_routes.rb', line 22

def check_for_default_routes
  if allow_all_actions?
    #Default routes are enabled globally
    warn :warning_type => "Default Routes",
      :warning_code => :all_default_routes,
      :message => msg("All public methods in controllers are available as actions in ", msg_file("routes.rb")),
      :line => tracker.routes[:allow_all_actions].line,
      :confidence => :high,
      :file => "#{tracker.app_path}/config/routes.rb",
      :cwe_id => [22]
  end
end
```

    
  

    
      
  
### 
  
    #**run_check**  ⇒ Object 
  

  

  

  
    

Checks for :allow_all_actions globally and for individual routes if it is not enabled globally.

  

  

  
    
      

```

16
17
18
19
20
```

    
    
      

```
# File 'lib/brakeman/checks/check_default_routes.rb', line 16

def run_check
  check_for_default_routes
  check_for_action_globs
  check_for_cve_2014_0130
end
```