# Class: Fabrication::Schematic::Definition
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Fabrication::Schematic::Definition
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/fabrication/schematic/definition.rb
  
  

  
    
## 
      Constant Summary
      collapse
    

    
      
        GENERATORS =
          
        
        

```
[
  Fabrication::Generator::ActiveRecord,
  Fabrication::Generator::Sequel,
  Fabrication::Generator::Mongoid,
  Fabrication::Generator::Base
].freeze
```

      
    
  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**attributes**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    
  

    
      
- 
  
    
      #**block**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute block.

  

    
      
- 
  
    
      #**callbacks**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    
  

    
      
- 
  
    
      #**name**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute name.

  

    
      
- 
  
    
      #**options**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute options.

  

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**append_or_update_attribute**(attribute_name, value, params = {})  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**attribute**(name)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**build**(overrides = {})  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**fabricate**(overrides = {})  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**generate_value**(name, params)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**generator**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**(name, options = {}, &block)  ⇒ Definition 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Definition.

  

      
        
- 
  
    
      #**initialize_copy**(original)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**klass**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**merge**(overrides = {})  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**process_block**(&block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**sorted_attributes**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**to_attributes**(overrides = {})  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**to_params**(overrides = {})  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(name, options = {}, &block)  ⇒ Definition 
  

  

  

  
    

Returns a new instance of Definition.

  

  

  
    
      

```

13
14
15
16
17
```

    
    
      

```
# File 'lib/fabrication/schematic/definition.rb', line 13

def initialize(name, options = {}, &block)
  self.name = name
  self.options = options
  self.block = block
end
```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**attributes**  ⇒ Object 
  

  

  

  
    
      

```

41
42
43
44
```

    
    
      

```
# File 'lib/fabrication/schematic/definition.rb', line 41

def attributes
  load_body
  @attributes ||= []
end
```

    
  

    
      
      
      
  
### 
  
    #**block**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute block.

  

  

  
    
      

```

11
12
13
```

    
    
      

```
# File 'lib/fabrication/schematic/definition.rb', line 11

def block
  @block
end
```

    
  

    
      
      
      
  
### 
  
    #**callbacks**  ⇒ Object 
  

  

  

  
    
      

```

46
47
48
49
```

    
    
      

```
# File 'lib/fabrication/schematic/definition.rb', line 46

def callbacks
  load_body
  @callbacks ||= {}
end
```

    
  

    
      
      
      
  
### 
  
    #**name**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute name.

  

  

  
    
      

```

11
12
13
```

    
    
      

```
# File 'lib/fabrication/schematic/definition.rb', line 11

def name
  @name
end
```

    
  

    
      
      
      
  
### 
  
    #**options**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute options.

  

  

  
    
      

```

11
12
13
```

    
    
      

```
# File 'lib/fabrication/schematic/definition.rb', line 11

def options
  @options
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**append_or_update_attribute**(attribute_name, value, params = {})  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/fabrication/schematic/definition.rb', line 27

def append_or_update_attribute(attribute_name, value, params = {}, &)
  attribute = Fabrication::Schematic::Attribute.new(klass, attribute_name, value, params, &)
  index = attributes.index { |a| a.name == attribute.name }

  if index
    attribute.transient! if attributes[index].transient?
    attributes[index] = attribute
  else
    attributes << attribute
  end
end
```

    
  

    
      
  
### 
  
    #**attribute**(name)  ⇒ Object 
  

  

  

  
    
      

```

23
24
25
```

    
    
      

```
# File 'lib/fabrication/schematic/definition.rb', line 23

def attribute(name)
  attributes.detect { |a| a.name == name }
end
```

    
  

    
      
  
### 
  
    #**build**(overrides = {})  ⇒ Object 
  

  

  

  
    
      

```

59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
```

    
    
      

```
# File 'lib/fabrication/schematic/definition.rb', line 59

def build(overrides = {}, &)
  Fabrication.manager.prevent_recursion!
  if Fabrication.manager.to_params_stack.any?
    to_params(overrides, &)
  else
    begin
      Fabrication.manager.build_stack << name
      merge(overrides, &).instance_eval do
        generator.new(klass).build(sorted_attributes, callbacks)
      end
    ensure
      Fabrication.manager.build_stack.pop
    end
  end
end
```

    
  

    
      
  
### 
  
    #**fabricate**(overrides = {})  ⇒ Object 
  

  

  

  
    
      

```

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
88
89
90
91
```

    
    
      

```
# File 'lib/fabrication/schematic/definition.rb', line 75

def fabricate(overrides = {}, &)
  Fabrication.manager.prevent_recursion!
  if Fabrication.manager.build_stack.any?
    build(overrides, &)
  elsif Fabrication.manager.to_params_stack.any?
    to_params(overrides, &)
  else
    begin
      Fabrication.manager.create_stack << name
      merge(overrides, &).instance_eval do
        generator.new(klass).create(sorted_attributes, callbacks)
      end
    ensure
      Fabrication.manager.create_stack.pop
    end
  end
end
```

    
  

    
      
  
### 
  
    #**generate_value**(name, params)  ⇒ Object 
  

  

  

  
    
      

```

118
119
120
121
122
123
124
125
```

    
    
      

```
# File 'lib/fabrication/schematic/definition.rb', line 118

def generate_value(name, params)
  if params[:count] || params[:rand]
    name = Fabrication::Support.singularize(name.to_s)
    proc { Fabricate.build(params[:fabricator] || name) }
  else
    proc { Fabricate(params[:fabricator] || name) }
  end
end
```

    
  

    
      
  
### 
  
    #**generator**  ⇒ Object 
  

  

  

  
    
      

```

51
52
53
```

    
    
      

```
# File 'lib/fabrication/schematic/definition.rb', line 51

def generator
  @generator ||= Fabrication::Config.generator_for(GENERATORS, klass)
end
```

    
  

    
      
  
### 
  
    #**initialize_copy**(original)  ⇒ Object 
  

  

  

  
    
      

```

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
# File 'lib/fabrication/schematic/definition.rb', line 109

def initialize_copy(original)
  self.callbacks = {}
  original.callbacks.each do |type, callbacks|
    self.callbacks[type] = callbacks.clone
  end

  self.attributes = original.attributes.clone
end
```

    
  

    
      
  
### 
  
    #**klass**  ⇒ Object 
  

  

  

  
    
      

```

136
137
138
139
140
141
142
143
```

    
    
      

```
# File 'lib/fabrication/schematic/definition.rb', line 136

def klass
  @klass ||= Fabrication::Support.class_for(
    options[:class_name] ||
      parent&.klass ||
      options[:from] ||
      name
  )
end
```

    
  

    
      
  
### 
  
    #**merge**(overrides = {})  ⇒ Object 
  

  

  

  
    
      

```

127
128
129
130
131
132
133
134
```

    
    
      

```
# File 'lib/fabrication/schematic/definition.rb', line 127

def merge(overrides = {}, &)
  clone.tap do |definition|
    definition.process_block(&)
    overrides.each do |name, value|
      definition.append_or_update_attribute(name.to_sym, value)
    end
  end
end
```

    
  

    
      
  
### 
  
    #**process_block**(&block)  ⇒ Object 
  

  

  

  
    
      

```

19
20
21
```

    
    
      

```
# File 'lib/fabrication/schematic/definition.rb', line 19

def process_block(&block)
  Fabrication::Schematic::Evaluator.new.process(self, &block) if block
end
```

    
  

    
      
  
### 
  
    #**sorted_attributes**  ⇒ Object 
  

  

  

  
    
      

```

55
56
57
```

    
    
      

```
# File 'lib/fabrication/schematic/definition.rb', line 55

def sorted_attributes
  attributes.select(&:value_static?) + attributes.select(&:value_proc?)
end
```

    
  

    
      
  
### 
  
    #**to_attributes**(overrides = {})  ⇒ Object 
  

  

  

  
    
      

```

103
104
105
106
107
```

    
    
      

```
# File 'lib/fabrication/schematic/definition.rb', line 103

def to_attributes(overrides = {}, &)
  merge(overrides, &).instance_eval do
    generator.new(klass).to_hash(sorted_attributes, callbacks)
  end
end
```

    
  

    
      
  
### 
  
    #**to_params**(overrides = {})  ⇒ Object 
  

  

  

  
    
      

```

93
94
95
96
97
98
99
100
101
```

    
    
      

```
# File 'lib/fabrication/schematic/definition.rb', line 93

def to_params(overrides = {}, &)
  Fabrication.manager.prevent_recursion!
  Fabrication.manager.to_params_stack << name
  merge(overrides, &).instance_eval do
    generator.new(klass).to_params(sorted_attributes)
  end
ensure
  Fabrication.manager.to_params_stack.pop
end
```