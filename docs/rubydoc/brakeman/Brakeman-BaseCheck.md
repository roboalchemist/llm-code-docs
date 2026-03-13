# Class: Brakeman::BaseCheck
  
  
  

  
  
    Inherits:
    
      SexpProcessor
      
        

          
- Object
          
            
- SexpProcessor
          
            
- Brakeman::BaseCheck
          
        

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      Messages, ProcessorHelper, SafeCallHelper, Util
  
  
  

  

  
  
    Defined in:
    lib/brakeman/checks/base_check.rb
  
  

## Overview

  
    

Basis of vulnerability checks.

  

  

  
## Direct Known Subclasses

  

CheckBasicAuth, CheckBasicAuthTimingAttack, CheckCSRFTokenForgeryCVE, CheckCookieSerialization, CheckCreateWith, CheckCrossSiteScripting, CheckDefaultRoutes, CheckDeserialize, CheckDetailedExceptions, CheckDigestDoS, CheckDivideByZero, CheckDynamicFinders, CheckEscapeFunction, CheckEvaluation, CheckExecute, CheckFileAccess, CheckFileDisclosure, CheckFilterSkipping, CheckForceSSL, CheckForgerySetting, CheckHeaderDoS, CheckI18nXSS, CheckJRubyXML, CheckJSONEncoding, CheckJSONEntityEscape, CheckJSONParsing, CheckMailTo, CheckMassAssignment, CheckMimeTypeDoS, CheckModelAttrAccessible, CheckModelAttributes, CheckModelSerialize, CheckNestedAttributes, CheckNestedAttributesBypass, CheckNumberToCurrency, CheckPageCachingCVE, CheckPathname, CheckPermitAttributes, CheckQuoteTableName, CheckRansack, CheckRedirect, CheckRegexDoS, CheckRender, CheckRenderDoS, CheckResponseSplitting, CheckReverseTabnabbing, CheckRouteDoS, CheckSQL, CheckSQLCVEs, CheckSSLVerify, CheckSafeBufferManipulation, CheckSanitizeConfigCve, CheckSanitizeMethods, CheckSecrets, CheckSelectTag, CheckSelectVulnerability, CheckSend, CheckSessionManipulation, CheckSessionSettings, CheckSingleQuotes, CheckSkipBeforeFilter, CheckSprocketsPathTraversal, CheckStripTags, CheckSymbolDoS, CheckSymbolDoSCVE, CheckTemplateInjection, CheckTranslateBug, CheckUnsafeReflection, CheckUnsafeReflectionMethods, CheckUnscopedFind, CheckValidationRegex, CheckVerbConfusion, CheckWeakHash, CheckWeakRSAKey, CheckWithoutProtection, CheckXMLDoS, CheckYAMLParsing, EOLCheck

## Defined Under Namespace

  
    
  
    
      **Classes:** Match
    
  

  
    
## 
      Constant Summary
      collapse
    

    
      
        CONFIDENCE =
          
  
    

This is for legacy support. Use :high, :medium, or :low instead when creating warnings.

  

  

        
        

```
Brakeman::Warning::CONFIDENCE
```

      
    
  

  
  
  
### Constants included
     from Util

  

Util::ALL_COOKIES, Util::ALL_PARAMETERS, Util::COOKIES, Util::COOKIES_SEXP, Util::DIR_CONST, Util::LITERALS, Util::PARAMETERS, Util::PARAMS_SEXP, Util::PATH_PARAMETERS, Util::QUERY_PARAMETERS, Util::REQUEST_COOKIES, Util::REQUEST_ENV, Util::REQUEST_PARAMETERS, Util::REQUEST_PARAMS, Util::REQUEST_REQUEST_PARAMETERS, Util::SAFE_LITERAL, Util::SESSION, Util::SESSION_SEXP, Util::SIMPLE_LITERALS

  
  
  
### Constants inherited
     from SexpProcessor

  

SexpProcessor::VERSION

  
## Class Attribute Summary collapse

  

    
      
- 
  
    
      .**name**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute name.

  

    
  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**tracker**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute tracker.

  

    
      
- 
  
    
      #**warnings**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute warnings.

  

    
  

  
  
  
### Attributes inherited from SexpProcessor

  

#context, #env, #expected

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**description**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**inherited**(subclass)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**add_result**(result)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Add result to result list, which is used to check for duplicates.

  

      
        
- 
  
    
      #**initialize**(tracker)  ⇒ BaseCheck 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

Initialize Check with Checks.

  

      
        
- 
  
    
      #**process_array**(exp)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**process_call**(exp)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Process calls and check if they include user input.

  

      
        
- 
  
    
      #**process_cookies**(exp)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Note that cookies are included in current expression.

  

      
        
- 
  
    
      #**process_default**(exp)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Default Sexp processing.

  

      
        
- 
  
    
      #**process_dstr**(exp)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Does not actually process string interpolation, but notes that it occurred.

  

      
        
- 
  
    
      #**process_if**(exp)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**process_params**(exp)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Note that params are included in current expression.

  

      
    

  

  
  
  
  
  
  
  
  
  
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
  
    #**initialize**(tracker)  ⇒ BaseCheck 
  

  

  

  
    

Initialize Check with Checks.

  

  

  
    
      

```

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
# File 'lib/brakeman/checks/base_check.rb', line 30

def initialize(tracker)
  super()
  @app_tree = tracker.app_tree
  @results = [] #only to check for duplicates
  @warnings = []
  @tracker = tracker
  @string_interp = false
  @current_set = nil
  @current_template = @current_module = @current_class = @current_method = nil
  @active_record_models = nil
  @mass_assign_disabled = nil
  @has_user_input = nil
  @in_array = false
  @safe_input_attributes = Set[:to_i, :to_f, :arel_table, :id, :uuid]
  @comparison_ops  = Set[:==, :!=, :>, :<, :>=, :<=]
end
```

    
  

  

  
    
## Class Attribute Details

    
      
      
      
  
### 
  
    .**name**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute name.

  

  

  
    
      

```

22
23
24
```

    
    
      

```
# File 'lib/brakeman/checks/base_check.rb', line 22

def name
  @name
end
```

    
  

    
  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**tracker**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute tracker.

  

  

  
    
      

```

13
14
15
```

    
    
      

```
# File 'lib/brakeman/checks/base_check.rb', line 13

def tracker
  @tracker
end
```

    
  

    
      
      
      
  
### 
  
    #**warnings**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute warnings.

  

  

  
    
      

```

13
14
15
```

    
    
      

```
# File 'lib/brakeman/checks/base_check.rb', line 13

def warnings
  @warnings
end
```

    
  

    
  

  
    
## Class Method Details

    
      
  
### 
  
    .**description**  ⇒ Object 
  

  

  

  
    
      

```

489
490
491
```

    
    
      

```
# File 'lib/brakeman/checks/base_check.rb', line 489

def self.description
  @description
end
```

    
  

    
      
  
### 
  
    .**inherited**(subclass)  ⇒ Object 
  

  

  

  
    
      

```

24
25
26
```

    
    
      

```
# File 'lib/brakeman/checks/base_check.rb', line 24

def inherited(subclass)
  subclass.name = subclass.to_s.match(/^Brakeman::(.*)$/)[1]
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**add_result**(result)  ⇒ Object 
  

  

  

  
    

Add result to result list, which is used to check for duplicates

  

  

  
    
      

```

48
49
50
51
52
53
```

    
    
      

```
# File 'lib/brakeman/checks/base_check.rb', line 48

def add_result result
  location = get_location result
  location, line = get_location result

  @results << [line, location, result]
end
```

    
  

    
      
  
### 
  
    #**process_array**(exp)  ⇒ Object 
  

  

  

  
    
      

```

113
114
115
116
117
118
```

    
    
      

```
# File 'lib/brakeman/checks/base_check.rb', line 113

def process_array exp
  @in_array = true
  process_default exp
ensure
  @in_array = false
end
```

    
  

    
      
  
### 
  
    #**process_call**(exp)  ⇒ Object 
  

  

  

  
    

Process calls and check if they include user input

  

  

  
    
      

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
```

    
    
      

```
# File 'lib/brakeman/checks/base_check.rb', line 66

def process_call exp
  unless @comparison_ops.include? exp.method
    process exp.target if sexp? exp.target
    process_call_args exp
  end

  target = exp.target

  unless always_safe_method? exp.method
    if params? target
      @has_user_input = Match.new(:params, exp)
    elsif cookies? target
      @has_user_input = Match.new(:cookies, exp)
    elsif request_headers? target
      @has_user_input = Match.new(:request, exp)
    elsif sexp? target and model_name? target[1] #TODO: Can this be target.target?
      @has_user_input = Match.new(:model, exp)
    end
  end

  exp
end
```

    
  

    
      
  
### 
  
    #**process_cookies**(exp)  ⇒ Object 
  

  

  

  
    

Note that cookies are included in current expression

  

  

  
    
      

```

108
109
110
111
```

    
    
      

```
# File 'lib/brakeman/checks/base_check.rb', line 108

def process_cookies exp
  @has_user_input = Match.new(:cookies, exp)
  exp
end
```

    
  

    
      
  
### 
  
    #**process_default**(exp)  ⇒ Object 
  

  

  

  
    

Default Sexp processing. Iterates over each value in the Sexp and processes them if they are also Sexps.

  

  

  
    
      

```

57
58
59
60
61
62
63
```

    
    
      

```
# File 'lib/brakeman/checks/base_check.rb', line 57

def process_default exp
  exp.each do |e|
    process e if sexp? e
  end

  exp
end
```

    
  

    
      
  
### 
  
    #**process_dstr**(exp)  ⇒ Object 
  

  

  

  
    

Does not actually process string interpolation, but notes that it occurred.

  

  

  
    
      

```

121
122
123
124
125
126
127
```

    
    
      

```
# File 'lib/brakeman/checks/base_check.rb', line 121

def process_dstr exp
  unless array_interp? exp or @string_interp # don't overwrite existing value
    @string_interp = Match.new(:interp, exp)
  end

  process_default exp
end
```

    
  

    
      
  
### 
  
    #**process_if**(exp)  ⇒ Object 
  

  

  

  
    
      

```

89
90
91
92
93
94
95
96
97
98
99
```

    
    
      

```
# File 'lib/brakeman/checks/base_check.rb', line 89

def process_if exp
  #This is to ignore user input in condition
  current_user_input = @has_user_input
  process exp.condition
  @has_user_input = current_user_input

  process exp.then_clause if sexp? exp.then_clause
  process exp.else_clause if sexp? exp.else_clause

  exp
end
```

    
  

    
      
  
### 
  
    #**process_params**(exp)  ⇒ Object 
  

  

  

  
    

Note that params are included in current expression

  

  

  
    
      

```

102
103
104
105
```

    
    
      

```
# File 'lib/brakeman/checks/base_check.rb', line 102

def process_params exp
  @has_user_input = Match.new(:params, exp)
  exp
end
```