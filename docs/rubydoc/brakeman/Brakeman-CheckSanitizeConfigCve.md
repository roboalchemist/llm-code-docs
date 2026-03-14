# Class: Brakeman::CheckSanitizeConfigCve
  
  
  

  
  
    Inherits:
    
      BaseCheck
      
        

          
- Object
          
            
- SexpProcessor
          
            
- BaseCheck
          
            
- Brakeman::CheckSanitizeConfigCve
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/brakeman/checks/check_sanitize_config_cve.rb
  
  

  
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
  
    
      #**check_config**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Look for   config.action_view.sanitized_allowed_tags = [“select”, “style”].

  

      
        
- 
  
    
      #**check_safe_list_allowed_tags**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Look for   Rails::Html::SafeListSanitizer.allowed_tags = [“select”, “style”].

  

      
        
- 
  
    
      #**check_sanitize_calls**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Look for   sanitize …, tags: [“select”, “style”] and   Rails::Html::SafeListSanitizer.new.sanitize(…, tags: [“select”, “style”]).

  

      
        
- 
  
    
      #**cve_warning**(confidence: :weak, result: nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
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
  
    #**check_config**  ⇒ Object 
  

  

  

  
    

Look for

```
config.action_view.sanitized_allowed_tags = ["select", "style"]

```

  

  

  
    
      

```

52
53
54
55
56
57
58
59
```

    
    
      

```
# File 'lib/brakeman/checks/check_sanitize_config_cve.rb', line 52

def check_config
  sanitizer_config = tracker.config.rails.dig(:action_view, :sanitized_allowed_tags)

  if sanitizer_config and include_both_tags? sanitizer_config
    @specific_warning = true
    cve_warning confidence: :high
  end
end
```

    
  

    
      
  
### 
  
    #**check_safe_list_allowed_tags**  ⇒ Object 
  

  

  

  
    

Look for

```
Rails::Html::SafeListSanitizer.allowed_tags = ["select", "style"]

```

  

  

  
    
      

```

77
78
79
80
81
```

    
    
      

```
# File 'lib/brakeman/checks/check_sanitize_config_cve.rb', line 77

def check_safe_list_allowed_tags
  tracker.find_call(target: :'Rails::Html::SafeListSanitizer', method: :allowed_tags=).each do |result|
    check_result result, result[:call].first_arg
  end
end
```

    
  

    
      
  
### 
  
    #**check_sanitize_calls**  ⇒ Object 
  

  

  

  
    

Look for

```
sanitize ..., tags: ["select", "style"]

```

and

```
Rails::Html::SafeListSanitizer.new.sanitize(..., tags: ["select", "style"])

```

  

  

  
    
      

```

65
66
67
68
69
70
71
72
73
```

    
    
      

```
# File 'lib/brakeman/checks/check_sanitize_config_cve.rb', line 65

def check_sanitize_calls
  tracker.find_call(method: :sanitize, target: nil).each do |result|
    check_tags_option result
  end

  tracker.find_call(method: :sanitize, target: :'Rails::Html::SafeListSanitizer.new').each do |result|
    check_tags_option result
  end
end
```

    
  

    
      
  
### 
  
    #**cve_warning**(confidence: :weak, result: nil)  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/brakeman/checks/check_sanitize_config_cve.rb', line 24

def cve_warning confidence: :weak, result: nil
  return if result and not original? result

  message = msg(msg_version(@gem_version, 'rails-html-sanitizer'),
                " is vulnerable to cross-site scripting when ",
                msg_code('select'),
                " and ",
                msg_code("style"),
                " tags are allowed ",
                msg_cve("CVE-2022-32209")
               )

  unless result
    message << ". Upgrade to 1.4.3 or newer"
  end

  warn :warning_type => "Cross-Site Scripting",
    :warning_code => :CVE_2022_32209,
    :message => message,
    :confidence => confidence,
    :gem_info => gemfile_or_environment(:'rails-html-sanitizer'),
    :link_path => "https://groups.google.com/g/rubyonrails-security/c/ce9PhUANQ6s/m/S0fJfnkmBAAJ",
    :cwe_id => [79],
    :result => result
end
```

    
  

    
      
  
### 
  
    #**run_check**  ⇒ Object 
  

  

  

  
    
      

```

8
9
10
11
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
```

    
    
      

```
# File 'lib/brakeman/checks/check_sanitize_config_cve.rb', line 8

def run_check
  @specific_warning = false

  @gem_version = tracker.config.gem_version :'rails-html-sanitizer'
  if version_between? "0.0.0", "1.4.2", @gem_version
    check_config
    check_sanitize_calls
    check_safe_list_allowed_tags

    unless @specific_warning
      # General warning about the vulnerable version
      cve_warning
    end
  end
end
```