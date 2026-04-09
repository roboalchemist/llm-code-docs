# Class: Brakeman::CheckNumberToCurrency
  
  
  

  
  
    Inherits:
    
      BaseCheck
      
        

          
- Object
          
            
- SexpProcessor
          
            
- BaseCheck
          
            
- Brakeman::CheckNumberToCurrency
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/brakeman/checks/check_number_to_currency.rb
  
  

  
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
  
    
      #**check_helper_option**(result, exp)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**check_number_helper_usage**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**generic_warning**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**  ⇒ CheckNumberToCurrency 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of CheckNumberToCurrency.

  

      
        
- 
  
    
      #**run_check**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**warn_on_number_helper**(result, match)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
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
  
    #**initialize**  ⇒ CheckNumberToCurrency 
  

  

  

  
    

Returns a new instance of CheckNumberToCurrency.

  

  

  
    
      

```

8
9
10
11
```

    
    
      

```
# File 'lib/brakeman/checks/check_number_to_currency.rb', line 8

def initialize(*)
  super
  @found_any = false
end
```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**check_helper_option**(result, exp)  ⇒ Object 
  

  

  

  
    
      

```

57
58
59
60
61
62
63
64
```

    
    
      

```
# File 'lib/brakeman/checks/check_number_to_currency.rb', line 57

def check_helper_option result, exp
  if match = (has_immediate_user_input? exp or has_immediate_model? exp)
    warn_on_number_helper result, match
    @found_any = true
  else
    false
  end
end
```

    
  

    
      
  
### 
  
    #**check_number_helper_usage**  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/brakeman/checks/check_number_to_currency.rb', line 43

def check_number_helper_usage
  number_methods = [:number_to_currency, :number_to_percentage, :number_to_human]
  tracker.find_call(:target => false, :methods => number_methods).each do |result|
    arg = result[:call].second_arg
    next unless arg

    if not check_helper_option(result, arg) and hash? arg
      hash_iterate(arg) do |_key, value|
        break if check_helper_option(result, value)
      end
    end
  end
end
```

    
  

    
      
  
### 
  
    #**generic_warning**  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/brakeman/checks/check_number_to_currency.rb', line 25

def generic_warning
  message = msg(msg_version(rails_version), " has a vulnerability in number helpers ", msg_cve("CVE-2014-0081"), ". Upgrade to ")

  if version_between? "2.3.0", "3.2.16"
    message << msg_version("3.2.17")
  else
    message << msg_version("4.0.3")
  end

  warn :warning_type => "Cross-Site Scripting",
    :warning_code => :CVE_2014_0081,
    :message => message,
    :confidence => :medium,
    :gem_info => gemfile_or_environment,
    :link_path => "https://groups.google.com/d/msg/ruby-security-ann/9WiRn2nhfq0/2K2KRB4LwCMJ",
    :cwe_id => [79]
end
```

    
  

    
      
  
### 
  
    #**run_check**  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/brakeman/checks/check_number_to_currency.rb', line 13

def run_check
  if version_between? "2.0.0", "2.3.18" or
    version_between? "3.0.0", "3.2.16" or
    version_between? "4.0.0", "4.0.2"

    return if lts_version? "2.3.18.8"

    check_number_helper_usage
    generic_warning unless @found_any
  end
end
```

    
  

    
      
  
### 
  
    #**warn_on_number_helper**(result, match)  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/brakeman/checks/check_number_to_currency.rb', line 66

def warn_on_number_helper result, match
  warn :result => result,
    :warning_type => "Cross-Site Scripting",
    :warning_code => :CVE_2014_0081_call,
    :message => msg("Format options in ", msg_code(result[:call].method), " are not safe in ", msg_version(rails_version)),
    :confidence => :high,
    :link_path => "https://groups.google.com/d/msg/ruby-security-ann/9WiRn2nhfq0/2K2KRB4LwCMJ",
    :user_input => match,
    :cwe_id => [79]
end
```