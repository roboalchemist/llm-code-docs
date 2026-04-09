# Class: Brakeman::CheckQuoteTableName
  
  
  

  
  
    Inherits:
    
      BaseCheck
      
        

          
- Object
          
            
- SexpProcessor
          
            
- BaseCheck
          
            
- Brakeman::CheckQuoteTableName
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/brakeman/checks/check_quote_table_name.rb
  
  

## Overview

  
    

Check for uses of quote_table_name in Rails versions before 2.3.13 and 3.0.10 groups.google.com/group/rubyonrails-security/browse_thread/thread/6a1e473744bc389b

  

  

  
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
  
    
      #**run_check**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**uses_quote_table_name?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
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
34
```

    
    
      

```
# File 'lib/brakeman/checks/check_quote_table_name.rb', line 10

def run_check
  if (version_between?('2.0.0', '2.3.13') or 
      version_between?('3.0.0', '3.0.9'))

    if uses_quote_table_name?
      confidence = :high
    else
      confidence = :medium
    end

    if rails_version =~ /^3/
      message = msg("Rails versions before 3.0.10 have a vulnerability in ", msg_code("quote_table_name"), " ", msg_cve("CVE-2011-2930"))
    else
      message = msg("Rails versions before 2.3.14 have a vulnerability in ", msg_code("quote_table_name"), " ", msg_cve("CVE-2011-2930"))
    end

    warn :warning_type => "SQL Injection",
      :warning_code => :CVE_2011_2930,
      :message => message,
      :confidence => confidence,
      :gem_info => gemfile_or_environment,
      :link_path => "https://groups.google.com/d/topic/rubyonrails-security/ah5HN0S8OJs/discussion",
      :cwe_id => [89]
  end
end
```

    
  

    
      
  
### 
  
    #**uses_quote_table_name?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

36
37
38
39
40
```

    
    
      

```
# File 'lib/brakeman/checks/check_quote_table_name.rb', line 36

def uses_quote_table_name?
  Brakeman.debug "Finding calls to quote_table_name()"

  not tracker.find_call(:target => false, :method => :quote_table_name).empty?
end
```