# Class: Fabrication::Cucumber::StepFabricator
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Fabrication::Cucumber::StepFabricator
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/fabrication/cucumber/step_fabricator.rb
  
  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**model**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute model.

  

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**from_table**(table, extra = {})  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**has_many**(children)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

rubocop:disable Naming/PredicateName.

  

      
        
- 
  
    
      #**initialize**(model_name, opts = {})  ⇒ StepFabricator 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of StepFabricator.

  

      
        
- 
  
    
      #**klass**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**n**(count, attrs = {})  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**parent**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

rubocop:enable Naming/PredicateName.

  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(model_name, opts = {})  ⇒ StepFabricator 
  

  

  

  
    

Returns a new instance of StepFabricator.

  

  

  
    
      

```

8
9
10
11
12
```

    
    
      

```
# File 'lib/fabrication/cucumber/step_fabricator.rb', line 8

def initialize(model_name, opts = {})
  @model = dehumanize(model_name)
  @fabricator = Fabrication::Support.singularize(@model).to_sym
  @parent_name = opts.delete(:parent)
end
```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**model**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute model.

  

  

  
    
      

```

6
7
8
```

    
    
      

```
# File 'lib/fabrication/cucumber/step_fabricator.rb', line 6

def model
  @model
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**from_table**(table, extra = {})  ⇒ Object 
  

  

  

  
    
      

```

14
15
16
17
18
19
20
21
22
```

    
    
      

```
# File 'lib/fabrication/cucumber/step_fabricator.rb', line 14

def from_table(table, extra = {})
  hashes = singular? ? [table.rows_hash] : table.hashes
  transformed_hashes = hashes.map do |hash|
    transformed_hash = Fabrication::Transform.apply_to(@model, parameterize_hash(hash))
    make(transformed_hash.merge(extra))
  end
  remember(transformed_hashes)
  transformed_hashes
end
```

    
  

    
      
  
### 
  
    #**has_many**(children)  ⇒ Object 
  

  

  

  
    

rubocop:disable Naming/PredicateName

  

  

  
    
      

```

29
30
31
32
33
34
35
36
```

    
    
      

```
# File 'lib/fabrication/cucumber/step_fabricator.rb', line 29

def has_many(children)
  instance = Fabrications[@fabricator]
  children = dehumanize(children)
  [Fabrications[children]].flatten.each do |child|
    child.send(:"#{klass.to_s.underscore.downcase}=", instance)
    child.respond_to?(:save!) && child.save!
  end
end
```

    
  

    
      
  
### 
  
    #**klass**  ⇒ Object 
  

  

  

  
    
      

```

45
46
47
```

    
    
      

```
# File 'lib/fabrication/cucumber/step_fabricator.rb', line 45

def klass
  Fabricate.schematic(@fabricator).send(:klass)
end
```

    
  

    
      
  
### 
  
    #**n**(count, attrs = {})  ⇒ Object 
  

  

  

  
    
      

```

24
25
26
```

    
    
      

```
# File 'lib/fabrication/cucumber/step_fabricator.rb', line 24

def n(count, attrs = {})
  Array.new(count).map { make(attrs) }.tap { |o| remember(o) }
end
```

    
  

    
      
  
### 
  
    #**parent**  ⇒ Object 
  

  

  

  
    

rubocop:enable Naming/PredicateName

  

  

  
    
      

```

39
40
41
42
43
```

    
    
      

```
# File 'lib/fabrication/cucumber/step_fabricator.rb', line 39

def parent
  return unless @parent_name

  Fabrications[dehumanize(@parent_name)]
end
```