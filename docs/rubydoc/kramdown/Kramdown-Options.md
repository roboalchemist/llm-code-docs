# Module: Kramdown::Options
  
  
  

  

  
  
  
  
  

  

  
  
    Defined in:
    lib/kramdown/options.rb
  
  

## Overview

  
    

This module defines all options that are used by parsers and/or converters as well as providing methods to deal with the options.

  

  

## Defined Under Namespace

  
    
  
    
      **Classes:** Boolean, Definition
    
  

  
    
## 
      Constant Summary
      collapse
    

    
      
        ALLOWED_TYPES =
          
  
    

Allowed option types.

  

  

        
        

```
[String, Integer, Float, Symbol, Boolean, Object]

```

      
    
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**defaults**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Return a Hash with the default values for all options.

  

      
        
- 
  
    
      .**define**(name, type, default, desc, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Define a new option called `name` (a Symbol) with the given `type` (String, Integer, Float, Symbol, Boolean, Object), default value `default` and the description `desc`.

  

      
        
- 
  
    
      .**defined?**(name)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Return `true` if an option called `name` is defined.

  

      
        
- 
  
    
      .**definitions**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Return all option definitions.

  

      
        
- 
  
    
      .**merge**(hash)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Merge the #defaults Hash with the **parsed** options from the given Hash, i.e.

  

      
        
- 
  
    
      .**parse**(name, data)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Parse the given value `data` as if it was a value for the option `name` and return the parsed value with the correct type.

  

      
        
- 
  
    
      .**simple_array_validator**(val, name, size = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Ensures that the option value `val` for the option called `name` is a valid array.

  

      
        
- 
  
    
      .**simple_hash_validator**(val, name)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Ensures that the option value `val` for the option called `name` is a valid hash.

  

      
        
- 
  
    
      .**str_to_sym**(data)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Converts the given String `data` into a Symbol or `nil` with the following provisions:.

  

      
    

  

  
    
## Class Method Details

    
      
  
### 
  
    .**defaults**  ⇒ Object 
  

  

  

  
    

Return a Hash with the default values for all options.

  

  

  
    
      

```

72
73
74
75
76
77
78
79
```

    
    
      

```
# File 'lib/kramdown/options.rb', line 72

def self.defaults
  @defaults ||=
    begin
      temp = {}
      @options.each {|_n, o| temp[o.name] = o.default }
      temp.freeze
    end
end

```

    
  

    
      
  
### 
  
    .**define**(name, type, default, desc, &block)  ⇒ Object 
  

  

  

  
    

Define a new option called `name` (a Symbol) with the given `type` (String, Integer, Float, Symbol, Boolean, Object), default value `default` and the description `desc`. If a block is specified, it should validate the value and either raise an error or return a valid value.

The type ‘Object’ should only be used for complex types for which none of the other types suffices. A block needs to be specified when using type ‘Object’ and it has to cope with a value given as string and as the opaque type.

  

  

Raises:

  
    
- 
      
      
      
      
    
  

  
    
      

```

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
# File 'lib/kramdown/options.rb', line 51

def self.define(name, type, default, desc, &block)
  name = name.to_sym
  raise ArgumentError, "Option name #{name} is already used" if @options.key?(name)
  raise ArgumentError, "Invalid option type #{type} specified" unless ALLOWED_TYPES.include?(type)
  raise ArgumentError, "Invalid type for default value" if !(type === default) && !default.nil?
  raise ArgumentError, "Missing validator block" if type == Object && block.nil?
  @options[name] = Definition.new(name, type, default, desc, block)
  @defaults = nil
end

```

    
  

    
      
  
### 
  
    .**defined?**(name)  ⇒ Boolean 
  

  

  

  
    

Return `true` if an option called `name` is defined.

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

67
68
69
```

    
    
      

```
# File 'lib/kramdown/options.rb', line 67

def self.defined?(name)
  @options.key?(name.to_sym)
end

```

    
  

    
      
  
### 
  
    .**definitions**  ⇒ Object 
  

  

  

  
    

Return all option definitions.

  

  

  
    
      

```

62
63
64
```

    
    
      

```
# File 'lib/kramdown/options.rb', line 62

def self.definitions
  @options
end

```

    
  

    
      
  
### 
  
    .**merge**(hash)  ⇒ Object 
  

  

  

  
    

Merge the #defaults Hash with the **parsed** options from the given Hash, i.e. only valid option names are considered and their value is run through the #parse method.

  

  

  
    
      

```

83
84
85
86
87
88
89
90
```

    
    
      

```
# File 'lib/kramdown/options.rb', line 83

def self.merge(hash)
  temp = defaults.dup
  hash.each do |k, v|
    k = k.to_sym
    temp[k] = @options.key?(k) ? parse(k, v) : v
  end
  temp
end

```

    
  

    
      
  
### 
  
    .**parse**(name, data)  ⇒ Object 
  

  

  

  
    

Parse the given value `data` as if it was a value for the option `name` and return the parsed value with the correct type.

If `data` already has the correct type, it is just returned. Otherwise it is converted to a String and then to the correct type.

  

  

Raises:

  
    
- 
      
      
      
      
    
  

  
    
      

```

97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
```

    
    
      

```
# File 'lib/kramdown/options.rb', line 97

def self.parse(name, data)
  name = name.to_sym
  raise ArgumentError, "No option named #{name} defined" unless @options.key?(name)
  unless @options[name].type === data
    data = data.to_s
    data = if @options[name].type == String
             data
           elsif @options[name].type == Integer
             Integer(data) rescue raise Kramdown::Error, "Invalid integer value for option '#{name}': '#{data}'"
           elsif @options[name].type == Float
             Float(data) rescue raise Kramdown::Error, "Invalid float value for option '#{name}': '#{data}'"
           elsif @options[name].type == Symbol
             str_to_sym(data)
           elsif @options[name].type == Boolean
             data.downcase.strip != 'false' && !data.empty?
           end
  end
  data = @options[name].validator[data] if @options[name].validator
  data
end

```

    
  

    
      
  
### 
  
    .**simple_array_validator**(val, name, size = nil)  ⇒ Object 
  

  

  

  
    

Ensures that the option value `val` for the option called `name` is a valid array. The parameter `val` can be

- 

a comma separated string which is split into an array of values

- 

or an array.

Optionally, the array is checked for the correct size.

  

  

  
    
      

```

142
143
144
145
146
147
148
149
150
151
152
```

    
    
      

```
# File 'lib/kramdown/options.rb', line 142

def self.simple_array_validator(val, name, size = nil)
  if String === val
    val = val.split(",")
  elsif !(Array === val)
    raise Kramdown::Error, "Invalid type #{val.class} for option #{name}"
  end
  if size && val.size != size
    raise Kramdown::Error, "Option #{name} needs exactly #{size} values"
  end
  val
end

```

    
  

    
      
  
### 
  
    .**simple_hash_validator**(val, name)  ⇒ Object 
  

  

  

  
    

Ensures that the option value `val` for the option called `name` is a valid hash. The parameter `val` can be

- 

a hash in YAML format

- 

or a Ruby Hash object.

  

  

Raises:

  
    
- 
      
      
      
      
    
  

  
    
      

```

159
160
161
162
163
164
165
166
167
168
169
```

    
    
      

```
# File 'lib/kramdown/options.rb', line 159

def self.simple_hash_validator(val, name)
  if String === val
    begin
      val = YAML.safe_load(val)
    rescue RuntimeError, ArgumentError, SyntaxError
      raise Kramdown::Error, "Invalid YAML value for option #{name}"
    end
  end
  raise Kramdown::Error, "Invalid type #{val.class} for option #{name}" unless Hash === val
  val
end

```

    
  

    
      
  
### 
  
    .**str_to_sym**(data)  ⇒ Object 
  

  

  

  
    

Converts the given String `data` into a Symbol or `nil` with the following provisions:

- 

A leading colon is stripped from the string.

- 

An empty value or a value equal to “nil” results in `nil`.

  

  

  
    
      

```

123
124
125
126
127
```

    
    
      

```
# File 'lib/kramdown/options.rb', line 123

def self.str_to_sym(data)
  data = data.strip
  data = data[1..-1] if data[0] == ':'
  (data.empty? || data == 'nil' ? nil : data.to_sym)
end

```