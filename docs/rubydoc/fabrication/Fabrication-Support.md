# Module: Fabrication::Support
  
  
  

  

  
  
  
      Extended by:
      Support
  
  
  
  
  

  
  
    Included in:
    Support
  
  

  
  
    Defined in:
    lib/fabrication/support.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**class_for**(class_or_to_s)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**constantize**(camel_cased_word)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**extract_options!**(args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**fabricatable?**(name)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**find_definitions**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**hash_class**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**log_deprecation**(message)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**singularize**(string)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**underscore**(string)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**variable_name_to_class_name**(name)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**class_for**(class_or_to_s)  ⇒ Object 
  

  

  

  
    
      

```

13
14
15
16
17
```

    
    
      

```
# File 'lib/fabrication/support.rb', line 13

def class_for(class_or_to_s)
  constantize(variable_name_to_class_name(class_or_to_s))
rescue NameError => e
  raise Fabrication::UnfabricatableError.new(class_or_to_s, e)
end
```

    
  

    
      
  
### 
  
    #**constantize**(camel_cased_word)  ⇒ Object 
  

  

  

  
    
      

```

19
20
21
22
23
24
25
```

    
    
      

```
# File 'lib/fabrication/support.rb', line 19

def constantize(camel_cased_word)
  return camel_cased_word if camel_cased_word.is_a?(Class)

  camel_cased_word.to_s.split('::').reduce(Object) do |resolved_class, class_part|
    resolved_class.const_get(class_part)
  end
end
```

    
  

    
      
  
### 
  
    #**extract_options!**(args)  ⇒ Object 
  

  

  

  
    
      

```

27
28
29
```

    
    
      

```
# File 'lib/fabrication/support.rb', line 27

def extract_options!(args)
  args.last.is_a?(::Hash) ? args.pop : {}
end
```

    
  

    
      
  
### 
  
    #**fabricatable?**(name)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

5
6
7
```

    
    
      

```
# File 'lib/fabrication/support.rb', line 5

def fabricatable?(name)
  Fabrication.manager[name] || class_for(name)
end
```

    
  

    
      
  
### 
  
    #**find_definitions**  ⇒ Object 
  

  

  

  
    
      

```

43
44
45
46
47
48
```

    
    
      

```
# File 'lib/fabrication/support.rb', line 43

def find_definitions
  log_deprecation('Fabrication::Support.find_definitions has been replaced by ' \
                  'Fabrication.manager.load_definitions and will be removed in 3.0.0.')

  Fabrication.manager.load_definitions
end
```

    
  

    
      
  
### 
  
    #**hash_class**  ⇒ Object 
  

  

  

  
    
      

```

50
51
52
```

    
    
      

```
# File 'lib/fabrication/support.rb', line 50

def hash_class
  @hash_class ||= defined?(HashWithIndifferentAccess) ? HashWithIndifferentAccess : Hash
end
```

    
  

    
      
  
### 
  
    #**log_deprecation**(message)  ⇒ Object 
  

  

  

  
    
      

```

9
10
11
```

    
    
      

```
# File 'lib/fabrication/support.rb', line 9

def log_deprecation(message)
  Config.logger.warn("[DEPRECATION][fabrication] #{message}")
end
```

    
  

    
      
  
### 
  
    #**singularize**(string)  ⇒ Object 
  

  

  

  
    
      

```

54
55
56
57
58
```

    
    
      

```
# File 'lib/fabrication/support.rb', line 54

def singularize(string)
  string.singularize
rescue StandardError
  string.end_with?('s') ? string[0..-2] : string
end
```

    
  

    
      
  
### 
  
    #**underscore**(string)  ⇒ Object 
  

  

  

  
    
      

```

60
61
62
63
64
65
66
```

    
    
      

```
# File 'lib/fabrication/support.rb', line 60

def underscore(string)
  string.gsub('::', '/')
        .gsub(/([A-Z]+)([A-Z][a-z])/, '\1_\2')
        .gsub(/([a-z\d])([A-Z])/, '\1_\2')
        .tr('-', '_')
        .downcase
end
```

    
  

    
      
  
### 
  
    #**variable_name_to_class_name**(name)  ⇒ Object 
  

  

  

  
    
      

```

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
# File 'lib/fabrication/support.rb', line 31

def variable_name_to_class_name(name)
  name_string = name.to_s

  if name_string.respond_to?(:camelize)
    name_string.camelize
  else
    name_string
      .gsub(%r{/(.?)}) { "::#{Regexp.last_match(1).upcase}" }
      .gsub(/(?:^|_)(.)/) { Regexp.last_match(1).upcase }
  end
end
```