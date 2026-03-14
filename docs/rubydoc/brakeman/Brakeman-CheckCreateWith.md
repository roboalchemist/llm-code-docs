# Class: Brakeman::CheckCreateWith
  
  
  

  
  
    Inherits:
    
      BaseCheck
      
        

          
- Object
          
            
- SexpProcessor
          
            
- BaseCheck
          
            
- Brakeman::CheckCreateWith
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/brakeman/checks/check_create_with.rb
  
  

  
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
  
    
      #**danger_level**(exp)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

For a given create_with call, set confidence level.

  

      
        
- 
  
    
      #**generic_warning**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
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
  
    #**danger_level**(exp)  ⇒ Object 
  

  

  

  
    

For a given create_with call, set confidence level. Ignore calls that use permit()

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/brakeman/checks/check_create_with.rb', line 49

def danger_level exp
  return unless sexp? exp

  if call? exp and exp.method == :permit
    nil
  elsif request_value? exp
    :high
  elsif hash? exp
    nil
  elsif has_immediate_user_input?(exp)
    :high
  elsif include_user_input? exp
    :medium
  else
    :weak
  end
end
```

    
  

    
      
  
### 
  
    #**generic_warning**  ⇒ Object 
  

  

  

  
    
      

```

67
68
69
70
71
72
73
74
75
```

    
    
      

```
# File 'lib/brakeman/checks/check_create_with.rb', line 67

def generic_warning
    warn :warning_type => "Mass Assignment",
      :warning_code => :CVE_2014_3514,
      :message => @message,
      :gem_info => gemfile_or_environment,
      :confidence => :medium,
      :link_path => "https://groups.google.com/d/msg/rubyonrails-security/M4chq5Sb540/CC1Fh0Y_NWwJ",
      :cwe_id => [915]
end
```

    
  

    
      
  
### 
  
    #**process_result**(result)  ⇒ Object 
  

  

  

  
    
      

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
37
38
39
40
41
42
43
44
45
```

    
    
      

```
# File 'lib/brakeman/checks/check_create_with.rb', line 28

def process_result result
  return unless original? result
  arg = result[:call].first_arg

  confidence = danger_level arg

  if confidence
    @warned = true

    warn :warning_type => "Mass Assignment",
      :warning_code => :CVE_2014_3514_call,
      :result => result,
      :message => @message,
      :confidence => confidence,
      :link_path => "https://groups.google.com/d/msg/rubyonrails-security/M4chq5Sb540/CC1Fh0Y_NWwJ",
      :cwe_id => [915]
  end
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
23
24
25
26
```

    
    
      

```
# File 'lib/brakeman/checks/check_create_with.rb', line 8

def run_check
  @warned = false

  if version_between? "4.0.0", "4.0.8"
    suggested_version = "4.0.9"
  elsif version_between? "4.1.0", "4.1.4"
    suggested_version = "4.1.5"
  else
    return
  end

  @message = msg(msg_code("create_with"), " is vulnerable to strong params bypass. Upgrade to ", msg_version(suggested_version), " or patch")

  tracker.find_call(:method => :create_with, :nested => true).each do |result|
    process_result result
  end

  generic_warning unless @warned
end
```