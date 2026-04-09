# Class: Fabricate
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Fabricate
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/fabricate.rb
  
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**attributes_for**(name, overrides = {})  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**attributes_for_times**(count, name, overrides = {})  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**build**(name, overrides = {})  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**build_times**(count, name, overrides = {})  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**create**(name, overrides = {})  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**fail_if_initializing**(name)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**schematic**(name)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**sequence**(name = Fabrication::Sequencer::DEFAULT, start = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**times**(count, name, overrides = {})  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**to_params**(name, overrides = {})  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Class Method Details

    
      
  
### 
  
    .**attributes_for**(name, overrides = {})  ⇒ Object 
  

  

  

  
    
      

```

14
15
16
17
```

    
    
      

```
# File 'lib/fabricate.rb', line 14

def self.attributes_for(name, overrides = {}, &)
  fail_if_initializing(name)
  schematic(name).to_attributes(overrides, &)
end
```

    
  

    
      
  
### 
  
    .**attributes_for_times**(count, name, overrides = {})  ⇒ Object 
  

  

  

  
    
      

```

10
11
12
```

    
    
      

```
# File 'lib/fabricate.rb', line 10

def self.attributes_for_times(count, name, overrides = {}, &)
  Array.new(count).map { Fabricate.attributes_for(name, overrides, &) }
end
```

    
  

    
      
  
### 
  
    .**build**(name, overrides = {})  ⇒ Object 
  

  

  

  
    
      

```

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
# File 'lib/fabricate.rb', line 24

def self.build(name, overrides = {}, &)
  fail_if_initializing(name)
  schematic(name).build(overrides, &).tap do |object|
    Fabrication::Config.notifiers.each do |notifier|
      notifier.call(name, object)
    end
  end
end
```

    
  

    
      
  
### 
  
    .**build_times**(count, name, overrides = {})  ⇒ Object 
  

  

  

  
    
      

```

6
7
8
```

    
    
      

```
# File 'lib/fabricate.rb', line 6

def self.build_times(count, name, overrides = {}, &)
  Array.new(count).map { Fabricate.build(name, overrides, &) }
end
```

    
  

    
      
  
### 
  
    .**create**(name, overrides = {})  ⇒ Object 
  

  

  

  
    
      

```

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
# File 'lib/fabricate.rb', line 33

def self.create(name, overrides = {}, &)
  fail_if_initializing(name)
  schematic(name).fabricate(overrides, &).tap do |object|
    Fabrication::Config.notifiers.each do |notifier|
      notifier.call(name, object)
    end
  end
end
```

    
  

    
      
  
### 
  
    .**fail_if_initializing**(name)  ⇒ Object 
  

  

  

  
    

  

  

Raises:

  
    
- 
      
      
        (Fabrication::MisplacedFabricateError)
      
      
      
    
  

  
    
      

```

51
52
53
```

    
    
      

```
# File 'lib/fabricate.rb', line 51

def self.fail_if_initializing(name)
  raise Fabrication::MisplacedFabricateError, name if Fabrication.manager.initializing?
end
```

    
  

    
      
  
### 
  
    .**schematic**(name)  ⇒ Object 
  

  

  

  
    
      

```

46
47
48
49
```

    
    
      

```
# File 'lib/fabricate.rb', line 46

def self.schematic(name)
  Fabrication.manager.load_definitions if Fabrication.manager.empty?
  Fabrication.manager[name] || raise(Fabrication::UnknownFabricatorError, name)
end
```

    
  

    
      
  
### 
  
    .**sequence**(name = Fabrication::Sequencer::DEFAULT, start = nil)  ⇒ Object 
  

  

  

  
    
      

```

42
43
44
```

    
    
      

```
# File 'lib/fabricate.rb', line 42

def self.sequence(name = Fabrication::Sequencer::DEFAULT, start = nil, &)
  Fabrication::Sequencer.sequence(name, start, &)
end
```

    
  

    
      
  
### 
  
    .**times**(count, name, overrides = {})  ⇒ Object 
  

  

  

  
    
      

```

2
3
4
```

    
    
      

```
# File 'lib/fabricate.rb', line 2

def self.times(count, name, overrides = {}, &)
  Array.new(count).map { Fabricate(name, overrides, &) }
end
```

    
  

    
      
  
### 
  
    .**to_params**(name, overrides = {})  ⇒ Object 
  

  

  

  
    
      

```

19
20
21
22
```

    
    
      

```
# File 'lib/fabricate.rb', line 19

def self.to_params(name, overrides = {}, &)
  fail_if_initializing(name)
  schematic(name).to_params(overrides, &)
end
```