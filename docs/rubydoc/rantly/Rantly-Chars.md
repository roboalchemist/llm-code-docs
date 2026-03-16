# Module: Rantly::Chars
  
  
  

  

  
  
  
  
  

  

  
  
    Defined in:
    lib/rantly/generator.rb
  
  

  
    
## 
      Constant Summary
      collapse
    

    
      
        ASCII =
          
        
        

```
Chars.of(/./)

```

      
        ALNUM =
          
        
        

```
Chars.of(/[[:alnum:]]/)

```

      
        ALPHA =
          
        
        

```
Chars.of(/[[:alpha:]]/)

```

      
        BLANK =
          
        
        

```
Chars.of(/[[:blank:]]/)

```

      
        CNTRL =
          
        
        

```
Chars.of(/[[:cntrl:]]/)

```

      
        DIGIT =
          
        
        

```
Chars.of(/[[:digit:]]/)

```

      
        GRAPH =
          
        
        

```
Chars.of(/[[:graph:]]/)

```

      
        LOWER =
          
        
        

```
Chars.of(/[[:lower:]]/)

```

      
        PRINT =
          
        
        

```
Chars.of(/[[:print:]]/)

```

      
        PUNCT =
          
        
        

```
Chars.of(/[[:punct:]]/)

```

      
        SPACE =
          
        
        

```
Chars.of(/[[:space:]]/)

```

      
        UPPER =
          
        
        

```
Chars.of(/[[:upper:]]/)

```

      
        XDIGIT =
          
        
        

```
Chars.of(/[[:xdigit:]]/)

```

      
        CLASSES =
          
        
        

```
{
  alnum: ALNUM,
  alpha: ALPHA,
  blank: BLANK,
  cntrl: CNTRL,
  digit: DIGIT,
  graph: GRAPH,
  lower: LOWER,
  print: PRINT,
  punct: PUNCT,
  space: SPACE,
  upper: UPPER,
  xdigit: XDIGIT,
  ascii: ASCII
}.freeze

```

      
    
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**of**(regexp)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Class Method Details

    
      
  
### 
  
    .**of**(regexp)  ⇒ Object 
  

  

  

  
    
      

```

237
238
239
```

    
    
      

```
# File 'lib/rantly/generator.rb', line 237

def of(regexp)
  ASCII.scan(regexp).to_a.map! { |char| char[0].ord }
end

```