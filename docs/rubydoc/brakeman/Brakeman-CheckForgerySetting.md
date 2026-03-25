# Class: Brakeman::CheckForgerySetting
  
  
  

  
  
    Inherits:
    
      BaseCheck
      
        

          
- Object
          
            
- SexpProcessor
          
            
- BaseCheck
          
            
- Brakeman::CheckForgerySetting
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/brakeman/checks/check_forgery_setting.rb
  
  

## Overview

  
    

Checks that `protect_from_forgery` is set in the ApplicationController.

Also warns for CSRF weakness in certain versions of Rails: groups.google.com/group/rubyonrails-security/browse_thread/thread/2d95a3cc23e03665

  

  

  
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
  
    
      #**check_cve_2011_0447**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**csrf_warning**(opts)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**run_check**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from BaseCheck

  

#add_result, description, inherited, #initialize, #process_array, #process_call, #process_cookies, #process_default, #process_dstr, #process_if, #process_params

  
  
  
  
  
  
  
  
  
### Methods included from Messages

  

#msg, #msg_code, #msg_cve, #msg_file, #msg_input, #msg_lit, #msg_plain, #msg_version

  
  
  
  
  
  
  
  
  
### Methods included from Util

  

#all_literals?, #array?, #block?, #call?, #camelize, #class_name, #constant?, #contains_class?, #cookies?, #dir_glob?, #false?, #hash?, #hash_access, #hash_insert, #hash_iterate, #hash_values, #integer?, #kwsplat?, #literal?, #make_call, #node_type?, #number?, #params?, #pluralize, #rails_version, #recurse_check?, #regexp?, #remove_kwsplat, #request_headers?, #request_value?, #result?, #safe_literal, #safe_literal?, #safe_literal_target?, #set_env_defaults, #sexp?, #simple_literal?, #string?, #string_interp?, #symbol?, #template_path_to_name, #true?, #underscore

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
### Methods included from ProcessorHelper

  

#current_file, #process_all, #process_all!, #process_call_args, #process_call_defn?, #process_class, #process_module

  
  
  
  
  
  
  
  
  
### Methods inherited from SexpProcessor

  

#in_context, #initialize, #process, processors, #scope

  
## Constructor Details

  
    

This class inherits a constructor from Brakeman::BaseCheck
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**check_cve_2011_0447**  ⇒ Object 
  

  

  

  
    
      

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
```

    
    
      

```
# File 'lib/brakeman/checks/check_forgery_setting.rb', line 62

def check_cve_2011_0447
  @warned_cve_2011_0447 ||= false
  return if @warned_cve_2011_0447

  if version_between? "2.1.0", "2.3.10"
    new_version = "2.3.11"
  elsif version_between? "3.0.0", "3.0.3"
    new_version = "3.0.4"
  else
    return
  end

  @warned_cve_2011_0447 = true # only warn once

  csrf_warning :warning_code => :CVE_2011_0447,
    :message => msg("CSRF protection is flawed in unpatched versions of ", msg_version(rails_version), " ", msg_cve("CVE-2011-0447"), ". Upgrade to ", msg_version(new_version), " or apply patches as needed"),
    :gem_info => gemfile_or_environment,
    :file => nil,
    :link_path => "https://groups.google.com/d/topic/rubyonrails-security/LZWjzCPgNmU/discussion",
    :cwe_id => [352]
end
```

    
  

    
      
  
### 
  
    #**csrf_warning**(opts)  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/brakeman/checks/check_forgery_setting.rb', line 51

def csrf_warning opts
  opts = {
    :controller => :ApplicationController,
    :warning_type => "Cross-Site Request Forgery",
    :confidence => :high,
    :cwe_id => [352]
  }.merge opts

  warn opts
end
```

    
  

    
      
  
### 
  
    #**run_check**  ⇒ Object 
  

  

  

  
    
      

```

12
13
14
15
16
17
18
19
20
21
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
```

    
    
      

```
# File 'lib/brakeman/checks/check_forgery_setting.rb', line 12

def run_check
  return if tracker.config.default_protect_from_forgery?

  tracker.controllers
  .select { |_, controller| controller.parent == :"ActionController::Base" }
  .each do |name, controller|
    if controller and not controller.protect_from_forgery?
      csrf_warning :controller => name,
        :warning_code => :csrf_protection_missing,
        :message => msg(msg_code("protect_from_forgery"), " should be called in ", msg_code(name)),
        :file => controller.file,
        :line => controller.top_line
    elsif version_between? "4.0.0", "100.0.0" and forgery_opts = controller.options[:protect_from_forgery]
      unless forgery_opts.is_a?(Array) and sexp?(forgery_opts.first) and
        access_arg = hash_access(forgery_opts.first.first_arg, :with) and symbol? access_arg and
        access_arg.value == :exception

        args = {
          :controller => name,
          :warning_type => "Cross-Site Request Forgery",
          :warning_code => :csrf_not_protected_by_raising_exception,
          :message => msg(msg_code("protect_from_forgery"), " should be configured with ", msg_code("with: :exception")),
          :confidence => :medium,
          :file => controller.file
        }

        args.merge!(:code => forgery_opts.first) if forgery_opts.is_a?(Array)

        csrf_warning args
      end

    end

    if controller.options[:protect_from_forgery]
      check_cve_2011_0447
    end
  end
end
```