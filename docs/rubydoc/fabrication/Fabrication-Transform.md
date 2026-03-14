# Class: Fabrication::Transform
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Fabrication::Transform
          
        

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      Singleton
  
  
  

  

  
  
    Defined in:
    lib/fabrication/transform.rb
  
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**apply_to**(schematic, attributes_hash)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**clear_all**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**define**(attribute, transform)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**only_for**(schematic, attribute, transform)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**apply_transform**(schematic, attribute, value)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**overrides**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**transforms**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  

  
    
## Class Method Details

    
      
  
### 
  
    .**apply_to**(schematic, attributes_hash)  ⇒ Object 
  

  

  

  
    
      

```

8
9
10
11
```

    
    
      

```
# File 'lib/fabrication/transform.rb', line 8

def apply_to(schematic, attributes_hash)
  Fabrication.manager.load_definitions if Fabrication.manager.empty?
  attributes_hash.inject({}) { |h, (k, v)| h.update(k => instance.apply_transform(schematic, k, v)) }
end
```

    
  

    
      
  
### 
  
    .**clear_all**  ⇒ Object 
  

  

  

  
    
      

```

13
14
15
16
```

    
    
      

```
# File 'lib/fabrication/transform.rb', line 13

def clear_all
  instance.transforms.clear
  instance.overrides.clear
end
```

    
  

    
      
  
### 
  
    .**define**(attribute, transform)  ⇒ Object 
  

  

  

  
    
      

```

18
19
20
```

    
    
      

```
# File 'lib/fabrication/transform.rb', line 18

def define(attribute, transform)
  instance.transforms[attribute] = transform
end
```

    
  

    
      
  
### 
  
    .**only_for**(schematic, attribute, transform)  ⇒ Object 
  

  

  

  
    
      

```

22
23
24
```

    
    
      

```
# File 'lib/fabrication/transform.rb', line 22

def only_for(schematic, attribute, transform)
  instance.overrides[schematic] = (instance.overrides[schematic] || {}).merge!(attribute => transform)
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**apply_transform**(schematic, attribute, value)  ⇒ Object 
  

  

  

  
    
      

```

31
32
33
```

    
    
      

```
# File 'lib/fabrication/transform.rb', line 31

def apply_transform(schematic, attribute, value)
  overrides.fetch(schematic, transforms)[attribute].call(value)
end
```

    
  

    
      
  
### 
  
    #**overrides**  ⇒ Object 
  

  

  

  
    
      

```

27
28
29
```

    
    
      

```
# File 'lib/fabrication/transform.rb', line 27

def overrides
  @overrides ||= {}
end
```

    
  

    
      
  
### 
  
    #**transforms**  ⇒ Object 
  

  

  

  
    
      

```

35
36
37
```

    
    
      

```
# File 'lib/fabrication/transform.rb', line 35

def transforms
  @transforms ||= Hash.new(->(value) { value })
end
```