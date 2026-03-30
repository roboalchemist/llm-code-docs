# Module: Formtastic::Inputs::Base::Collections
  
  
  

  

  
  
  
  
  

  
  
    Included in:
    CheckBoxesInput, DatalistInput, RadioInput, SelectInput
  
  

  
  
    Defined in:
    lib/formtastic/inputs/base/collections.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**collection**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**collection_for_boolean**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**collection_from_association**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**collection_from_enum**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Assuming the following model:.

  

      
        
- 
  
    
      #**collection_from_enum?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**collection_from_options**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**label_and_value_method**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**label_and_value_method_from_collection**(_collection)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**label_method**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**label_method_from_options**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**raw_collection**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**send_or_call**(duck, object)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**send_or_call_or_object**(duck, object)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Avoids an issue where `send_or_call` can be a String and duck can be something simple like `:first`, which obviously String responds to.

  

      
        
- 
  
    
      #**value_method**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**value_method_from_options**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**collection**  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/formtastic/inputs/base/collections.rb', line 50

def collection
  # Return if we have a plain string
  return raw_collection if raw_collection.is_a?(String)

  # Return if we have an Array of strings, integers or arrays
  return raw_collection if (raw_collection.instance_of?(Array) || raw_collection.instance_of?(Range)) &&
                       ([Array, String, Symbol].include?(raw_collection.first.class) || raw_collection.first.is_a?(Integer)) &&
                       !(options.include?(:member_label) || options.include?(:member_value))

  raw_collection.map { |o| [send_or_call(label_method, o), send_or_call(value_method, o)] }
end
```

    
  

    
      
  
### 
  
    #**collection_for_boolean**  ⇒ Object 
  

  

  

  
    
      

```

131
132
133
134
135
136
137
138
```

    
    
      

```
# File 'lib/formtastic/inputs/base/collections.rb', line 131

def collection_for_boolean
  true_text = options[:true] || Formtastic::I18n.t(:yes)
  false_text = options[:false] || Formtastic::I18n.t(:no)

  # TODO options[:value_as_class] = true unless options.key?(:value_as_class)

  [ [true_text, true], [false_text, false] ]
end
```

    
  

    
      
  
### 
  
    #**collection_from_association**  ⇒ Object 
  

  

  

  
    
      

```

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
88
89
90
91
92
```

    
    
      

```
# File 'lib/formtastic/inputs/base/collections.rb', line 74

def collection_from_association
  if reflection
    if reflection.respond_to?(:options)
      raise PolymorphicInputWithoutCollectionError.new(
                "A collection must be supplied for #{method} input. Collections cannot be guessed for polymorphic associations."
            ) if reflection.options[:polymorphic] == true
    end

    return reflection.klass.merge(reflection.scope) if reflection.scope

    conditions_from_reflection = (reflection.respond_to?(:options) && reflection.options[:conditions]) || {}
    conditions_from_reflection = conditions_from_reflection.call if conditions_from_reflection.is_a?(Proc)

    scope_conditions = conditions_from_reflection.empty? ? nil : {:conditions => conditions_from_reflection}
    where_conditions = (scope_conditions && scope_conditions[:conditions]) || {}

    reflection.klass.where(where_conditions)
  end
end
```

    
  

    
      
  
### 
  
    #**collection_from_enum**  ⇒ Object 
  

  

  

  
    

Assuming the following model:

class Post < ActiveRecord::Base
  enum :status => [ :active, :archived ]
end

We would end up with a collection like this:

[["Active", "active"], ["Archived", "archived"]

The first element in each array uses String#humanize, but I18n
translations are available too. Set them with the following structure.

en:
  activerecord:
    attributes:
      post:
        statuses:
          active: Custom Active Label Here
          archived: Custom Archived Label Here

  

  

  
    
      

```

114
115
116
117
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
# File 'lib/formtastic/inputs/base/collections.rb', line 114

def collection_from_enum
  if collection_from_enum?
    method_name = method.to_s

    enum_options_hash = object.defined_enums[method_name]
    enum_options_hash.map do |name, value|
      key = "activerecord.attributes.#{object.model_name.i18n_key}.#{method_name.pluralize}.#{name}"
      label = ::I18n.translate(key, :default => name.humanize)
      [label, name]
    end
  end
end
```

    
  

    
      
  
### 
  
    #**collection_from_enum?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

127
128
129
```

    
    
      

```
# File 'lib/formtastic/inputs/base/collections.rb', line 127

def collection_from_enum?
  object.respond_to?(:defined_enums) && object.defined_enums.has_key?(method.to_s)
end
```

    
  

    
      
  
### 
  
    #**collection_from_options**  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/formtastic/inputs/base/collections.rb', line 62

def collection_from_options
  items = options[:collection]
  case items
  when Hash
    items.to_a
  when Range
    items.to_a.collect{ |c| [c.to_s, c] }
  else
    items
  end
end
```

    
  

    
      
  
### 
  
    #**label_and_value_method**  ⇒ Object 
  

  

  

  
    
      

```

23
24
25
```

    
    
      

```
# File 'lib/formtastic/inputs/base/collections.rb', line 23

def label_and_value_method
  @label_and_value_method ||= label_and_value_method_from_collection(raw_collection)
end
```

    
  

    
      
  
### 
  
    #**label_and_value_method_from_collection**(_collection)  ⇒ Object 
  

  

  

  
    
      

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
38
39
40
41
42
43
44
```

    
    
      

```
# File 'lib/formtastic/inputs/base/collections.rb', line 27

def label_and_value_method_from_collection(_collection)
  sample = _collection.first || _collection[-1]

  case sample
  when Array
    label, value = :first, :last
  when Integer
    label, value = :to_s, :to_i
  when Symbol, String, NilClass
    label, value = :to_s, :to_s
  end

  # Order of preference: user supplied method, class defaults, auto-detect
  label ||= builder.collection_label_methods.find { |m| sample.respond_to?(m) }
  value ||= builder.collection_value_methods.find { |m| sample.respond_to?(m) }

  [label, value]
end
```

    
  

    
      
  
### 
  
    #**label_method**  ⇒ Object 
  

  

  

  
    
      

```

7
8
9
```

    
    
      

```
# File 'lib/formtastic/inputs/base/collections.rb', line 7

def label_method
  @label_method ||= (label_method_from_options || label_and_value_method.first)
end
```

    
  

    
      
  
### 
  
    #**label_method_from_options**  ⇒ Object 
  

  

  

  
    
      

```

11
12
13
```

    
    
      

```
# File 'lib/formtastic/inputs/base/collections.rb', line 11

def label_method_from_options
  options[:member_label]
end
```

    
  

    
      
  
### 
  
    #**raw_collection**  ⇒ Object 
  

  

  

  
    
      

```

46
47
48
```

    
    
      

```
# File 'lib/formtastic/inputs/base/collections.rb', line 46

def raw_collection
  @raw_collection ||= (collection_from_options || collection_from_enum || collection_from_association || collection_for_boolean)
end
```

    
  

    
      
  
### 
  
    #**send_or_call**(duck, object)  ⇒ Object 
  

  

  

  
    
      

```

140
141
142
143
144
145
146
```

    
    
      

```
# File 'lib/formtastic/inputs/base/collections.rb', line 140

def send_or_call(duck, object)
  if duck.respond_to?(:call)
    duck.call(object)
  elsif object.respond_to? duck.to_sym
    object.send(duck)
  end
end
```

    
  

    
      
  
### 
  
    #**send_or_call_or_object**(duck, object)  ⇒ Object 
  

  

  

  
    

Avoids an issue where `send_or_call` can be a String and duck can be something simple like
`:first`, which obviously String responds to.

  

  

  
    
      

```

150
151
152
153
```

    
    
      

```
# File 'lib/formtastic/inputs/base/collections.rb', line 150

def send_or_call_or_object(duck, object)
  return object if object.is_a?(String) || object.is_a?(Integer) || object.is_a?(Symbol) # TODO what about other classes etc?
  send_or_call(duck, object)
end
```

    
  

    
      
  
### 
  
    #**value_method**  ⇒ Object 
  

  

  

  
    
      

```

15
16
17
```

    
    
      

```
# File 'lib/formtastic/inputs/base/collections.rb', line 15

def value_method
  @value_method ||= (value_method_from_options || label_and_value_method[-1])
end
```

    
  

    
      
  
### 
  
    #**value_method_from_options**  ⇒ Object 
  

  

  

  
    
      

```

19
20
21
```

    
    
      

```
# File 'lib/formtastic/inputs/base/collections.rb', line 19

def value_method_from_options
  options[:member_value]
end
```