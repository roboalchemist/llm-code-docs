# Module: Formtastic::Inputs::Base::Validations
  
  
  

  

  
  
  
  
  

  
  
    Included in:
    Formtastic::Inputs::Base
  
  

  
  
    Defined in:
    lib/formtastic/inputs/base/validations.rb
  
  

## Defined Under Namespace

  
    
  
    
      **Classes:** IndeterminableMaximumAttributeError, IndeterminableMinimumAttributeError
    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**autofocus?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**column_limit**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**limit**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**not_required_through_negated_validation!**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**not_required_through_negated_validation?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**optional?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**readonly?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**readonly_attribute?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**readonly_from_options?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**required?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**required_attribute?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**responds_to_global_required?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**validation_integer_only?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**validation_limit**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**validation_max**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Prefer :less_than_or_equal_to over :less_than, for no particular reason.

  

      
        
- 
  
    
      #**validation_min**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Prefer :greater_than_or_equal_to over :greater_than, for no particular reason.

  

      
        
- 
  
    
      #**validation_step**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**validations**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**validations?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**validator_relevant?**(validator)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**autofocus?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

180
181
182
183
184
```

    
    
      

```
# File 'lib/formtastic/inputs/base/validations.rb', line 180

def autofocus?
  opt_autofocus = options[:input_html] && options[:input_html][:autofocus]

  !!opt_autofocus
end
```

    
  

    
      
  
### 
  
    #**column_limit**  ⇒ Object 
  

  

  

  
    
      

```

186
187
188
189
190
191
192
193
194
195
196
197
198
199
200
201
202
203
```

    
    
      

```
# File 'lib/formtastic/inputs/base/validations.rb', line 186

def column_limit
  return unless column?
  return unless column.respond_to?(:limit)

  limit = column.limit # already in characters for string, text, etc

  if column.type == :integer && column.limit.is_a?(Integer)
    return {
      1 => 3, # 8 bit
      2 => 5, # 16 bit
      3 => 7, # 24 bit
      4 => 10, # 32 bit
      8 => 19, # 64 bit
    }[limit] || nil
  end

  return limit
end
```

    
  

    
      
  
### 
  
    #**limit**  ⇒ Object 
  

  

  

  
    
      

```

205
206
207
```

    
    
      

```
# File 'lib/formtastic/inputs/base/validations.rb', line 205

def limit
  validation_limit || column_limit
end
```

    
  

    
      
  
### 
  
    #**not_required_through_negated_validation!**  ⇒ Object 
  

  

  

  
    
      

```

168
169
170
```

    
    
      

```
# File 'lib/formtastic/inputs/base/validations.rb', line 168

def not_required_through_negated_validation!
  @not_required_through_negated_validation = true
end
```

    
  

    
      
  
### 
  
    #**not_required_through_negated_validation?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

164
165
166
```

    
    
      

```
# File 'lib/formtastic/inputs/base/validations.rb', line 164

def not_required_through_negated_validation?
  @not_required_through_negated_validation
end
```

    
  

    
      
  
### 
  
    #**optional?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

176
177
178
```

    
    
      

```
# File 'lib/formtastic/inputs/base/validations.rb', line 176

def optional?
  !required?
end
```

    
  

    
      
  
### 
  
    #**readonly?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

209
210
211
```

    
    
      

```
# File 'lib/formtastic/inputs/base/validations.rb', line 209

def readonly?
  readonly_from_options? || readonly_attribute?
end
```

    
  

    
      
  
### 
  
    #**readonly_attribute?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

213
214
215
216
217
218
219
```

    
    
      

```
# File 'lib/formtastic/inputs/base/validations.rb', line 213

def readonly_attribute?
  object_class = self.object.class
  object_class.respond_to?(:readonly_attributes) &&
    self.object.persisted? &&
    column.respond_to?(:name) &&
    object_class.readonly_attributes.include?(column.name.to_s)
end
```

    
  

    
      
  
### 
  
    #**readonly_from_options?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

221
222
223
```

    
    
      

```
# File 'lib/formtastic/inputs/base/validations.rb', line 221

def readonly_from_options?
  options[:input_html] && options[:input_html][:readonly]
end
```

    
  

    
      
  
### 
  
    #**required?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

132
133
134
135
136
137
138
139
140
141
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
153
154
155
156
157
158
```

    
    
      

```
# File 'lib/formtastic/inputs/base/validations.rb', line 132

def required?
  return false if options[:required] == false
  return true if options[:required] == true
  return false if not_required_through_negated_validation?
  if validations?
    validations.any? { |validator|
      if validator.options.key?(:on)
        validator_on = Array(validator.options[:on])
        next false if (validator_on.exclude?(:save)) && ((object.new_record? && validator_on.exclude?(:create)) || (!object.new_record? && validator_on.exclude?(:update)))
      end
      case validator.kind
      when :presence
        true
      when :inclusion
        validator.options[:allow_blank] != true
      when :length
        validator.options[:allow_blank] != true &&
        option_value(validator.options[:minimum], object).to_i > 0 ||
        option_value(validator.options[:within], object).try(:first).to_i > 0
      else
        false
      end
    }
  else
    return responds_to_global_required? && !!builder.all_fields_required_by_default
  end
end
```

    
  

    
      
  
### 
  
    #**required_attribute?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

160
161
162
```

    
    
      

```
# File 'lib/formtastic/inputs/base/validations.rb', line 160

def required_attribute?
  required? && builder.use_required_attribute
end
```

    
  

    
      
  
### 
  
    #**responds_to_global_required?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

172
173
174
```

    
    
      

```
# File 'lib/formtastic/inputs/base/validations.rb', line 172

def responds_to_global_required?
  true
end
```

    
  

    
      
  
### 
  
    #**validation_integer_only?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

117
118
119
120
121
122
123
124
125
126
```

    
    
      

```
# File 'lib/formtastic/inputs/base/validations.rb', line 117

def validation_integer_only?
  validation = validations? && validations.find do |validation|
    validation.kind == :numericality
  end
  if validation
    validation.options[:only_integer]
  else
    false
  end
end
```

    
  

    
      
  
### 
  
    #**validation_limit**  ⇒ Object 
  

  

  

  
    
      

```

55
56
57
58
59
60
61
62
63
64
65
```

    
    
      

```
# File 'lib/formtastic/inputs/base/validations.rb', line 55

def validation_limit
  validation = validations? && validations.find do |validation|
    validation.kind == :length
  end
  if validation
    option_value(validation.options[:maximum], object) ||
      (validation.options[:within].present? ? option_value(validation.options[:within], object).max : nil)
  else
    nil
  end
end
```

    
  

    
      
  
### 
  
    #**validation_max**  ⇒ Object 
  

  

  

  
    

Prefer :less_than_or_equal_to over :less_than, for no particular reason.

  

  

  
    
      

```

88
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
100
101
102
103
104
```

    
    
      

```
# File 'lib/formtastic/inputs/base/validations.rb', line 88

def validation_max
  validation = validations? && validations.find do |validation|
    validation.kind == :numericality
  end
  if validation
    # We can't determine an appropriate value for :greater_than with a float/decimal column
    raise IndeterminableMaximumAttributeError if validation.options[:less_than] && column? && [:float, :decimal].include?(column.type)

    if validation.options[:less_than_or_equal_to]
      return option_value(validation.options[:less_than_or_equal_to], object)
    end

    if validation.options[:less_than]
      return option_value(validation.options[:less_than], object) - 1
    end
  end
end
```

    
  

    
      
  
### 
  
    #**validation_min**  ⇒ Object 
  

  

  

  
    

Prefer :greater_than_or_equal_to over :greater_than, for no particular reason.

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/formtastic/inputs/base/validations.rb', line 68

def validation_min
  validation = validations? && validations.find do |validation|
    validation.kind == :numericality
  end

  if validation
    # We can't determine an appropriate value for :greater_than with a float/decimal column
    raise IndeterminableMinimumAttributeError if validation.options[:greater_than] && column? && [:float, :decimal].include?(column.type)

    if validation.options[:greater_than_or_equal_to]
      return option_value(validation.options[:greater_than_or_equal_to], object)
    end

    if validation.options[:greater_than]
      return option_value(validation.options[:greater_than], object) + 1
    end
  end
end
```

    
  

    
      
  
### 
  
    #**validation_step**  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/formtastic/inputs/base/validations.rb', line 106

def validation_step
  validation = validations? && validations.find do |validation|
    validation.kind == :numericality
  end
  if validation
    validation.options[:step] || (1 if validation_integer_only?)
  else
    nil
  end
end
```

    
  

    
      
  
### 
  
    #**validations**  ⇒ Object 
  

  

  

  
    
      

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
```

    
    
      

```
# File 'lib/formtastic/inputs/base/validations.rb', line 25

def validations
  @validations ||= if object && object.class.respond_to?(:validators_on)
    object.class.validators_on(attributized_method_name).select do |validator|
      validator_relevant?(validator)
    end
  else
    nil
  end
end
```

    
  

    
      
  
### 
  
    #**validations?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

128
129
130
```

    
    
      

```
# File 'lib/formtastic/inputs/base/validations.rb', line 128

def validations?
  validations != nil
end
```

    
  

    
      
  
### 
  
    #**validator_relevant?**(validator)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

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
46
47
48
49
50
51
52
53
```

    
    
      

```
# File 'lib/formtastic/inputs/base/validations.rb', line 35

def validator_relevant?(validator)
  return true unless validator.options.key?(:if) || validator.options.key?(:unless)
  conditional = validator.options.key?(:if) ? validator.options[:if] : validator.options[:unless]

  result = if conditional.respond_to?(:call) && conditional.arity > 0
    conditional.call(object)
  elsif conditional.respond_to?(:call) && conditional.arity == 0
    object.instance_exec(&conditional)
  elsif conditional.is_a?(::Symbol) && object.respond_to?(conditional)
    object.send(conditional)
  else
    conditional
  end

  result = validator.options.key?(:unless) ? !result : !!result
  not_required_through_negated_validation! if !result && [:presence, :inclusion, :length].include?(validator.kind)

  result
end
```