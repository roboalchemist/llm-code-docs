# Class: Capybara::Selector::FilterSet
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Capybara::Selector::FilterSet
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/capybara/selector/filter_set.rb
  
  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**expression_filters**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute expression_filters.

  

    
      
- 
  
    
      #**node_filters**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute node_filters.

  

    
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**[]**(name)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**add**(name, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**all**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**remove**(name)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**describe**(what = nil, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**description**(node_filters: true, expression_filters: true, **options)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**descriptions**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**expression_filter**(name, *types, **options, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**import**(name, filters = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**(name, &block)  ⇒ FilterSet 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of FilterSet.

  

      
        
- 
  
    
      #**node_filter**(names, *types, **options, &block)  ⇒ Object 
    

    
      (also: #filter)
    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(name, &block)  ⇒ FilterSet 
  

  

  

  
    

Returns a new instance of FilterSet.

  

  

  
    
      

```

10
11
12
13
14
15
16
```

    
    
      

```
# File 'lib/capybara/selector/filter_set.rb', line 10

def initialize(name, &block)
  @name = name
  @node_filters = {}
  @expression_filters = {}
  @descriptions = Hash.new { |hsh, key| hsh[key] = [] }
  instance_eval(&block) if block
end

```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**expression_filters**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute expression_filters.

  

  

  
    
      

```

8
9
10
```

    
    
      

```
# File 'lib/capybara/selector/filter_set.rb', line 8

def expression_filters
  @expression_filters
end

```

    
  

    
      
      
      
  
### 
  
    #**node_filters**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute node_filters.

  

  

  
    
      

```

8
9
10
```

    
    
      

```
# File 'lib/capybara/selector/filter_set.rb', line 8

def node_filters
  @node_filters
end

```

    
  

    
  

  
    
## Class Method Details

    
      
  
### 
  
    .**[]**(name)  ⇒ Object 
  

  

  

  
    
      

```

74
75
76
```

    
    
      

```
# File 'lib/capybara/selector/filter_set.rb', line 74

def [](name)
  all.fetch(name.to_sym) { |set_name| raise ArgumentError, "Unknown filter set (:#{set_name})" }
end

```

    
  

    
      
  
### 
  
    .**add**(name, &block)  ⇒ Object 
  

  

  

  
    
      

```

78
79
80
```

    
    
      

```
# File 'lib/capybara/selector/filter_set.rb', line 78

def add(name, &block)
  all[name.to_sym] = FilterSet.new(name.to_sym, &block)
end

```

    
  

    
      
  
### 
  
    .**all**  ⇒ Object 
  

  

  

  
    
      

```

70
71
72
```

    
    
      

```
# File 'lib/capybara/selector/filter_set.rb', line 70

def all
  @filter_sets ||= {} # rubocop:disable Naming/MemoizedInstanceVariableName
end

```

    
  

    
      
  
### 
  
    .**remove**(name)  ⇒ Object 
  

  

  

  
    
      

```

82
83
84
```

    
    
      

```
# File 'lib/capybara/selector/filter_set.rb', line 82

def remove(name)
  all.delete(name.to_sym)
end

```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**describe**(what = nil, &block)  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/capybara/selector/filter_set.rb', line 29

def describe(what = nil, &block)
  case what
  when nil
    undeclared_descriptions.push block
  when :node_filters
    node_filter_descriptions.push block
  when :expression_filters
    expression_filter_descriptions.push block
  else
    raise ArgumentError, 'Unknown description type'
  end
end

```

    
  

    
      
  
### 
  
    #**description**(node_filters: true, expression_filters: true, **options)  ⇒ Object 
  

  

  

  
    
      

```

42
43
44
45
46
47
48
49
```

    
    
      

```
# File 'lib/capybara/selector/filter_set.rb', line 42

def description(node_filters: true, expression_filters: true, **options)
  opts = options_with_defaults(options)
  description = +''
  description << undeclared_descriptions.map { |desc| desc.call(**opts).to_s }.join
  description << expression_filter_descriptions.map { |desc| desc.call(**opts).to_s }.join if expression_filters
  description << node_filter_descriptions.map { |desc| desc.call(**opts).to_s }.join if node_filters
  description
end

```

    
  

    
      
  
### 
  
    #**descriptions**  ⇒ Object 
  

  

  

  
    
      

```

51
52
53
54
```

    
    
      

```
# File 'lib/capybara/selector/filter_set.rb', line 51

def descriptions
  Capybara::Helpers.warn 'DEPRECATED: FilterSet#descriptions is deprecated without replacement'
  [undeclared_descriptions, node_filter_descriptions, expression_filter_descriptions].flatten
end

```

    
  

    
      
  
### 
  
    #**expression_filter**(name, *types, **options, &block)  ⇒ Object 
  

  

  

  
    
      

```

25
26
27
```

    
    
      

```
# File 'lib/capybara/selector/filter_set.rb', line 25

def expression_filter(name, *types, **options, &block)
  add_filter(name, Filters::ExpressionFilter, *types, **options, &block)
end

```

    
  

    
      
  
### 
  
    #**import**(name, filters = nil)  ⇒ Object 
  

  

  

  
    
      

```

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
66
67
```

    
    
      

```
# File 'lib/capybara/selector/filter_set.rb', line 56

def import(name, filters = nil)
  filter_selector = filters.nil? ? ->(*) { true } : ->(filter_name, _) { filters.include? filter_name }

  self.class[name].tap do |f_set|
    expression_filters.merge!(f_set.expression_filters.select(&filter_selector))
    node_filters.merge!(f_set.node_filters.select(&filter_selector))
    f_set.undeclared_descriptions.each { |desc| describe(&desc) }
    f_set.expression_filter_descriptions.each { |desc| describe(:expression_filters, &desc) }
    f_set.node_filter_descriptions.each { |desc| describe(:node_filters, &desc) }
  end
  self
end

```

    
  

    
      
  
### 
  
    #**node_filter**(names, *types, **options, &block)  ⇒ Object 
  

  
    Also known as:
    filter
    
  

  

  
    
      

```

18
19
20
21
22
```

    
    
      

```
# File 'lib/capybara/selector/filter_set.rb', line 18

def node_filter(names, *types, **options, &block)
  Array(names).each do |name|
    add_filter(name, Filters::NodeFilter, *types, **options, &block)
  end
end

```