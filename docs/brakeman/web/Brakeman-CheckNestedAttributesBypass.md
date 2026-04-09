# Class: Brakeman::CheckNestedAttributesBypass
  
  
  

  
  
    Inherits:
    
      BaseCheck
      
        

          
- Object
          
            
- SexpProcessor
          
            
- BaseCheck
          
            
- Brakeman::CheckNestedAttributesBypass
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/brakeman/checks/check_nested_attributes_bypass.rb
  
  

## Overview

  
    

groups.google.com/d/msg/rubyonrails-security/cawsWcQ6c8g/tegZtYdbFQAJ

  

  

  
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
  
    
      #**allow_destroy?**(arg)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**check_nested_attributes**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**reject_if?**(arg)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**run_check**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**warn_about_nested_attributes**(model, args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**workaround?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
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
  
    #**allow_destroy?**(arg)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

46
47
48
49
```

    
    
      

```
# File 'lib/brakeman/checks/check_nested_attributes_bypass.rb', line 46

def allow_destroy? arg
  hash? arg and
    false? hash_access(arg, :allow_destroy)
end
```

    
  

    
      
  
### 
  
    #**check_nested_attributes**  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/brakeman/checks/check_nested_attributes_bypass.rb', line 20

def check_nested_attributes
  active_record_models.each do |name, model|
    if opts = model.options[:accepts_nested_attributes_for]
      opts.each do |args|
        if args.any? { |a| allow_destroy? a } and args.any? { |a| reject_if? a }
          warn_about_nested_attributes model, args
        end
      end
    end
  end
end
```

    
  

    
      
  
### 
  
    #**reject_if?**(arg)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

51
52
53
54
```

    
    
      

```
# File 'lib/brakeman/checks/check_nested_attributes_bypass.rb', line 51

def reject_if? arg
  hash? arg and
    hash_access(arg, :reject_if)
end
```

    
  

    
      
  
### 
  
    #**run_check**  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/brakeman/checks/check_nested_attributes_bypass.rb', line 9

def run_check
  if version_between? "3.1.0", "3.2.22" or
     version_between? "4.0.0", "4.1.14" or
     version_between? "4.2.0", "4.2.5"

    unless workaround?
      check_nested_attributes
    end
  end
end
```

    
  

    
      
  
### 
  
    #**warn_about_nested_attributes**(model, args)  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/brakeman/checks/check_nested_attributes_bypass.rb', line 32

def warn_about_nested_attributes model, args
  message = msg(msg_version(rails_version), " does not call ", msg_code(":reject_if"), " option when ", msg_code(":allow_destroy"), " is ", msg_code("false"), " ", msg_cve("CVE-2015-7577"))

  warn :model => model,
    :warning_type => "Nested Attributes",
    :warning_code => :CVE_2015_7577,
    :message => message,
    :file => model.file,
    :line => args.line,
    :confidence => :medium,
    :link_path => "https://groups.google.com/d/msg/rubyonrails-security/cawsWcQ6c8g/tegZtYdbFQAJ",
    :cwe_id => [284]
end
```

    
  

    
      
  
### 
  
    #**workaround?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

56
57
58
```

    
    
      

```
# File 'lib/brakeman/checks/check_nested_attributes_bypass.rb', line 56

def workaround?
  tracker.find_call(method: :will_be_destroyed?).any?
end
```