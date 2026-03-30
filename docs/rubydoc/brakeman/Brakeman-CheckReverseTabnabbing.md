# Class: Brakeman::CheckReverseTabnabbing
  
  
  

  
  
    Inherits:
    
      BaseCheck
      
        

          
- Object
          
            
- SexpProcessor
          
            
- BaseCheck
          
            
- Brakeman::CheckReverseTabnabbing
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/brakeman/checks/check_reverse_tabnabbing.rb
  
  

  
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
  
    
      #**process_result**(result)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
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
  
    #**process_result**(result)  ⇒ Object 
  

  

  

  
    
      

```

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
50
51
52
53
54
55
56
57
58
```

    
    
      

```
# File 'lib/brakeman/checks/check_reverse_tabnabbing.rb', line 15

def process_result result
  return unless original? result and result[:call].last_arg

  html_opts = result[:call].last_arg
  return unless hash? html_opts

  target = hash_access html_opts, :target
  unless target &&
        (string?(target) && target.value == "_blank" ||
        symbol?(target) && target.value == :_blank)
    return
  end

  target_url = result[:block] ? result[:call].first_arg : result[:call].second_arg

  # `url_for` and `_path` calls lead to urls on to the same origin.
  # That means that an adversary would need to run javascript on
  # the victim application's domain. If that is the case, the adversary
  # already has the ability to redirect the victim user anywhere.
  # Also statically provided URLs (interpolated or otherwise) are also
  # ignored as they produce many false positives.
  return if !call?(target_url) || target_url.method.match(/^url_for$|_path$/)

  rel = hash_access html_opts, :rel
  confidence = :medium

  if rel && string?(rel) then
    rel_opt = rel.value
    return if rel_opt.include?("noopener") && rel_opt.include?("noreferrer")

    if rel_opt.include?("noopener") ^ rel_opt.include?("noreferrer") then
      confidence = :weak
    end
  end

  warn :result => result,
    :warning_type => "Reverse Tabnabbing",
    :warning_code => :reverse_tabnabbing,
    :message => msg("When opening a link in a new tab without setting ", msg_code('rel: "noopener noreferrer"'),
                    ", the new tab can control the parent tab's location. For example, an attacker could redirect to a phishing page."),
    :confidence => confidence,
    :user_input => rel,
    :cwe_id => [1022]
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
```

    
    
      

```
# File 'lib/brakeman/checks/check_reverse_tabnabbing.rb', line 8

def run_check
  calls = tracker.find_call :methods => :link_to
  calls.each do |call|
    process_result call
  end
end
```