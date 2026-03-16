# Module: Capybara::RSpecMatchers::CountSugar
  
  
  

  

  
  
  
  
  

  
  
    Included in:
    Matchers::CountableWrappedElementMatcher
  
  

  
  
    Defined in:
    lib/capybara/rspec/matchers/count_sugar.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**at_least**(number)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**at_most**(number)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**exactly**(number)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**once**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**thrice**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**times**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**twice**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**at_least**(number)  ⇒ Object 
  

  

  

  
    
      

```

20
21
22
23
```

    
    
      

```
# File 'lib/capybara/rspec/matchers/count_sugar.rb', line 20

def at_least(number)
  options[:minimum] = number
  self
end

```

    
  

    
      
  
### 
  
    #**at_most**(number)  ⇒ Object 
  

  

  

  
    
      

```

15
16
17
18
```

    
    
      

```
# File 'lib/capybara/rspec/matchers/count_sugar.rb', line 15

def at_most(number)
  options[:maximum] = number
  self
end

```

    
  

    
      
  
### 
  
    #**exactly**(number)  ⇒ Object 
  

  

  

  
    
      

```

10
11
12
13
```

    
    
      

```
# File 'lib/capybara/rspec/matchers/count_sugar.rb', line 10

def exactly(number)
  options[:count] = number
  self
end

```

    
  

    
      
  
### 
  
    #**once**  ⇒ Object 
  

  

  

  
    
      

```

6
```

    
    
      

```
# File 'lib/capybara/rspec/matchers/count_sugar.rb', line 6

def once; exactly(1); end

```

    
  

    
      
  
### 
  
    #**thrice**  ⇒ Object 
  

  

  

  
    
      

```

8
```

    
    
      

```
# File 'lib/capybara/rspec/matchers/count_sugar.rb', line 8

def thrice; exactly(3); end

```

    
  

    
      
  
### 
  
    #**times**  ⇒ Object 
  

  

  

  
    
      

```

25
26
27
```

    
    
      

```
# File 'lib/capybara/rspec/matchers/count_sugar.rb', line 25

def times
  self
end

```

    
  

    
      
  
### 
  
    #**twice**  ⇒ Object 
  

  

  

  
    
      

```

7
```

    
    
      

```
# File 'lib/capybara/rspec/matchers/count_sugar.rb', line 7

def twice; exactly(2); end

```