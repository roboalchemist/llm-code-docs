# Class: Brakeman::CheckSelectTag
  
  
  

  
  
    Inherits:
    
      BaseCheck
      
        

          
- Object
          
            
- SexpProcessor
          
            
- BaseCheck
          
            
- Brakeman::CheckSelectTag
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/brakeman/checks/check_select_tag.rb
  
  

## Overview

  
    

Checks for CVE-2012-3463, unescaped input in :prompt option of select_tag: groups.google.com/d/topic/rubyonrails-security/fV3QUToSMSw/discussion

  

  

  
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
    

    
  
  
  
  
  
  
  
  

  
    

Check if select_tag is called with user input in :prompt option.

  

      
        
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
  

  

  

  
    

Check if select_tag is called with user input in :prompt option

  

  

  
    
      

```

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
59
```

    
    
      

```
# File 'lib/brakeman/checks/check_select_tag.rb', line 36

def process_result result
  return unless original? result

  #Only concerned if user input is supplied for :prompt option
  last_arg = result[:call].last_arg

  if hash? last_arg
    prompt_option = hash_access last_arg, :prompt

    if call? prompt_option and @ignore_methods.include? prompt_option.method
      return
    elsif sexp? prompt_option and input = include_user_input?(prompt_option)

      warn :warning_type => "Cross-Site Scripting",
        :warning_code => :CVE_2012_3463,
        :result => result,
        :message => @message,
        :confidence => :high,
        :user_input => input,
        :link_path => "https://groups.google.com/d/topic/rubyonrails-security/fV3QUToSMSw/discussion",
        :cwe_id => [79]
    end
  end
end
```

    
  

    
      
  
### 
  
    #**run_check**  ⇒ Object 
  

  

  

  
    
      

```

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
27
28
29
30
31
32
33
```

    
    
      

```
# File 'lib/brakeman/checks/check_select_tag.rb', line 10

def run_check

  if version_between? "3.0.0", "3.0.16"
    suggested_version = "3.0.17"
  elsif version_between? "3.1.0", "3.1.7"
    suggested_version = "3.1.8"
  elsif version_between? "3.2.0", "3.2.7"
    suggested_version = "3.2.8"
  else
    return
  end

  @ignore_methods = Set[:escapeHTML, :escape_once, :h].merge tracker.options[:safe_methods]

  @message = msg("Upgrade to ", msg_version(suggested_version), ". In ", msg_version(rails_version), " ", msg_code("select_tag"), " is vulnerable ", msg_cve("CVE-2012-3463"))

  calls = tracker.find_call(:target => nil, :method => :select_tag).select do |result|
    result[:location][:type] == :template
  end

  calls.each do |result|
    process_result result
  end
end
```