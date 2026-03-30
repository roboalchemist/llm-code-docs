# Class: Brakeman::BasicProcessor
  
  
  

  
  
    Inherits:
    
      SexpProcessor
      
        

          
- Object
          
            
- SexpProcessor
          
            
- Brakeman::BasicProcessor
          
        

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      ProcessorHelper, SafeCallHelper, Util
  
  
  

  

  
  
    Defined in:
    lib/brakeman/processors/lib/basic_processor.rb
  
  

  
## Direct Known Subclasses

  

FindAllCalls, FindCall, GemProcessor, Rails2ConfigProcessor, Rails2RoutesProcessor, Rails3ConfigProcessor, Rails3RoutesProcessor

  
## Constant Summary

  
  
### Constants included
     from Util

  

Util::ALL_COOKIES, Util::ALL_PARAMETERS, Util::COOKIES, Util::COOKIES_SEXP, Util::DIR_CONST, Util::LITERALS, Util::PARAMETERS, Util::PARAMS_SEXP, Util::PATH_PARAMETERS, Util::QUERY_PARAMETERS, Util::REQUEST_COOKIES, Util::REQUEST_ENV, Util::REQUEST_PARAMETERS, Util::REQUEST_PARAMS, Util::REQUEST_REQUEST_PARAMETERS, Util::SAFE_LITERAL, Util::SESSION, Util::SESSION_SEXP, Util::SIMPLE_LITERALS

  
  
  
### Constants inherited
     from SexpProcessor

  

SexpProcessor::VERSION

  
## Instance Attribute Summary

  
  
### Attributes inherited from SexpProcessor

  

#context, #env, #expected

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**initialize**(tracker)  ⇒ BasicProcessor 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of BasicProcessor.

  

      
        
- 
  
    
      #**process_default**(exp)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**process_if**(exp)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods included from Util

  

#all_literals?, #array?, #block?, #call?, #camelize, #class_name, #constant?, #contains_class?, #cookies?, #dir_glob?, #false?, #hash?, #hash_access, #hash_insert, #hash_iterate, #hash_values, #integer?, #kwsplat?, #literal?, #make_call, #node_type?, #number?, #params?, #pluralize, #rails_version, #recurse_check?, #regexp?, #remove_kwsplat, #request_headers?, #request_value?, #result?, #safe_literal, #safe_literal?, #safe_literal_target?, #set_env_defaults, #sexp?, #simple_literal?, #string?, #string_interp?, #symbol?, #template_path_to_name, #true?, #underscore

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
### Methods included from ProcessorHelper

  

#current_file, #process_all, #process_all!, #process_call_args, #process_call_defn?, #process_class, #process_module

  
  
  
  
  
  
  
  
  
### Methods inherited from SexpProcessor

  

#in_context, #process, processors, #scope

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(tracker)  ⇒ BasicProcessor 
  

  

  

  
    

Returns a new instance of BasicProcessor.

  

  

  
    
      

```

10
11
12
13
14
```

    
    
      

```
# File 'lib/brakeman/processors/lib/basic_processor.rb', line 10

def initialize tracker
  super()
  @tracker = tracker
  @current_template = @current_module = @current_class = @current_method = nil
end
```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**process_default**(exp)  ⇒ Object 
  

  

  

  
    
      

```

16
17
18
```

    
    
      

```
# File 'lib/brakeman/processors/lib/basic_processor.rb', line 16

def process_default exp
  process_all exp
end
```

    
  

    
      
  
### 
  
    #**process_if**(exp)  ⇒ Object 
  

  

  

  
    
      

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
31
32
33
34
35
36
```

    
    
      

```
# File 'lib/brakeman/processors/lib/basic_processor.rb', line 20

def process_if exp
  condition = exp.condition

  process condition

  if true? condition
    process exp.then_clause
  elsif false? condition
    process exp.else_clause
  else
    [exp.then_clause, exp.else_clause].compact.map do |e|
      process e
    end
  end

  exp
end
```