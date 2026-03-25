# Class: Capybara::Selector::CSS
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Capybara::Selector::CSS
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/capybara/selector/css.rb
  
  

## Defined Under Namespace

  
    
  
    
      **Classes:** Splitter
    
  

  
    
## 
      Constant Summary
      collapse
    

    
      
        S =
          
        
        

```
'\u{80}-\u{D7FF}\u{E000}-\u{FFFD}\u{10000}-\u{10FFFF}'
```

      
        H =
          
        
        

```
/[0-9a-fA-F]/
```

      
        UNICODE =
          
        
        

```
/\\#{H}{1,6}[ \t\r\n\f]?/
```

      
        NONASCII =
          
        
        

```
/[#{S}]/
```

      
        ESCAPE =
          
        
        

```
/#{UNICODE}|\\[ -~#{S}]/
```

      
        NMSTART =
          
        
        

```
/[_a-zA-Z]|#{NONASCII}|#{ESCAPE}/
```

      
    
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**escape**(str)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**escape_char**(char)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**split**(css)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Class Method Details

    
      
  
### 
  
    .**escape**(str)  ⇒ Object 
  

  

  

  
    
      

```

8
9
10
11
12
13
14
15
```

    
    
      

```
# File 'lib/capybara/selector/css.rb', line 8

def self.escape(str)
  value = str.dup
  out = +''
  out << value.slice!(0...1) if value.match?(/^[-_]/)
  out << (value[0].match?(NMSTART) ? value.slice!(0...1) : escape_char(value.slice!(0...1)))
  out << value.gsub(/[^a-zA-Z0-9_-]/) { |char| escape_char char }
  out
end
```

    
  

    
      
  
### 
  
    .**escape_char**(char)  ⇒ Object 
  

  

  

  
    
      

```

17
18
19
```

    
    
      

```
# File 'lib/capybara/selector/css.rb', line 17

def self.escape_char(char)
  char.match?(%r{[ -/:-~]}) ? "\\#{char}" : format('\\%06<hex>x', hex: char.ord)
end
```

    
  

    
      
  
### 
  
    .**split**(css)  ⇒ Object 
  

  

  

  
    
      

```

21
22
23
```

    
    
      

```
# File 'lib/capybara/selector/css.rb', line 21

def self.split(css)
  Splitter.new.split(css)
end
```