# Class: Fabrication::Schematic::Attribute
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Fabrication::Schematic::Attribute
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/fabrication/schematic/attribute.rb
  
  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**klass**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute klass.

  

    
      
- 
  
    
      #**name**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute name.

  

    
      
- 
  
    
      #**params**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    
  

    
      
- 
  
    
      #**value**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute value.

  

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**initialize**(klass, name, value, params = {}, &block)  ⇒ Attribute 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Attribute.

  

      
        
- 
  
    
      #**processed_value**(processed_attributes)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**transient!**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**transient?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**value_proc?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**value_static?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(klass, name, value, params = {}, &block)  ⇒ Attribute 
  

  

  

  
    

Returns a new instance of Attribute.

  

  

  
    
      

```

7
8
9
10
11
12
```

    
    
      

```
# File 'lib/fabrication/schematic/attribute.rb', line 7

def initialize(klass, name, value, params = {}, &block)
  self.klass = klass
  self.name = name
  self.params = params
  self.value = value.nil? ? block : value
end
```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**klass**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute klass.

  

  

  
    
      

```

4
5
6
```

    
    
      

```
# File 'lib/fabrication/schematic/attribute.rb', line 4

def klass
  @klass
end
```

    
  

    
      
      
      
  
### 
  
    #**name**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute name.

  

  

  
    
      

```

4
5
6
```

    
    
      

```
# File 'lib/fabrication/schematic/attribute.rb', line 4

def name
  @name
end
```

    
  

    
      
      
      
  
### 
  
    #**params**  ⇒ Object 
  

  

  

  
    
      

```

14
15
16
```

    
    
      

```
# File 'lib/fabrication/schematic/attribute.rb', line 14

def params
  @params ||= {}
end
```

    
  

    
      
      
      
  
### 
  
    #**value**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute value.

  

  

  
    
      

```

4
5
6
```

    
    
      

```
# File 'lib/fabrication/schematic/attribute.rb', line 4

def value
  @value
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**processed_value**(processed_attributes)  ⇒ Object 
  

  

  

  
    
      

```

26
27
28
29
30
31
32
33
34
```

    
    
      

```
# File 'lib/fabrication/schematic/attribute.rb', line 26

def processed_value(processed_attributes)
  if process_count
    (1..process_count).map { |i| execute(processed_attributes, i, &value) }
  elsif value_proc?
    execute(processed_attributes, &value)
  else
    value
  end
end
```

    
  

    
      
  
### 
  
    #**transient!**  ⇒ Object 
  

  

  

  
    
      

```

18
19
20
```

    
    
      

```
# File 'lib/fabrication/schematic/attribute.rb', line 18

def transient!
  params[:transient] = true
end
```

    
  

    
      
  
### 
  
    #**transient?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

22
23
24
```

    
    
      

```
# File 'lib/fabrication/schematic/attribute.rb', line 22

def transient?
  params[:transient]
end
```

    
  

    
      
  
### 
  
    #**value_proc?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

40
41
42
```

    
    
      

```
# File 'lib/fabrication/schematic/attribute.rb', line 40

def value_proc?
  value.is_a?(Proc)
end
```

    
  

    
      
  
### 
  
    #**value_static?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

36
37
38
```

    
    
      

```
# File 'lib/fabrication/schematic/attribute.rb', line 36

def value_static?
  !value_proc?
end
```