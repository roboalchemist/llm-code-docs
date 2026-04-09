# Class: Capybara::Selector::CSSBuilder
  
  
  Private

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Capybara::Selector::CSSBuilder
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/capybara/selector/builders/css_builder.rb
  
  

  
    

  **This class is part of a private API.**
  You should avoid using this class if possible, as it may be removed or be changed in the future.

  

  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**expression**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  private

  
    
  

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**add_attribute_conditions**(**attributes)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  private

  
    
  

      
        
- 
  
    
      #**initialize**(expression)  ⇒ CSSBuilder 
    

    
  
  
  
    constructor
  
  
  
  
  
  private

  
    

A new instance of CSSBuilder.

  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(expression)  ⇒ CSSBuilder 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Returns a new instance of CSSBuilder.

  

  

  
    
      

```

9
10
11
```

    
    
      

```
# File 'lib/capybara/selector/builders/css_builder.rb', line 9

def initialize(expression)
  @expression = expression || ''
end
```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**expression**  ⇒ Object  (readonly)
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

  

  

  
    
      

```

13
14
15
```

    
    
      

```
# File 'lib/capybara/selector/builders/css_builder.rb', line 13

def expression
  @expression
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**add_attribute_conditions**(**attributes)  ⇒ Object 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/capybara/selector/builders/css_builder.rb', line 15

def add_attribute_conditions(**attributes)
  @expression = attributes.inject(expression) do |css, (name, value)|
    conditions = if name == :class
      class_conditions(value)
    elsif value.is_a? Regexp
      regexp_conditions(name, value)
    else
      [attribute_conditions(name => value)]
    end

    ::Capybara::Selector::CSS.split(css).map do |sel|
      next sel if conditions.empty?

      conditions.map { |cond| sel + cond }.join(', ')
    end.join(', ')
  end
end
```