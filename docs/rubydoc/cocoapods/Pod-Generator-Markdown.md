# Class: Pod::Generator::Markdown
  
  
  

  
  
    Inherits:
    
      Acknowledgements
      
        

          
- Object
          
            
- Acknowledgements
          
            
- Pod::Generator::Markdown
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/cocoapods/generator/acknowledgements/markdown.rb
  
  

  
## Instance Attribute Summary

  
  
### Attributes inherited from Acknowledgements

  

#file_accessors

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**path_from_basepath**(path)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**generate**  ⇒ String 
    

    
  
  
  
  
  
  
  
  

  
    

The contents of the acknowledgements in Markdown format.

  

      
        
- 
  
    
      #**licenses**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**save_as**(path)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**string_for_spec**(spec)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**title_from_string**(string, level)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from Acknowledgements

  

#footnote_text, #footnote_title, generators, #header_text, #header_title, #initialize

  
## Constructor Details

  
    

This class inherits a constructor from Pod::Generator::Acknowledgements
  

  
    
## Class Method Details

    
      
  
### 
  
    .**path_from_basepath**(path)  ⇒ Object 
  

  

  

  
    
      

```

4
5
6
```

    
    
      

```
# File 'lib/cocoapods/generator/acknowledgements/markdown.rb', line 4

def self.path_from_basepath(path)
  Pathname.new(path.dirname + "#{path.basename}.markdown")
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**generate**  ⇒ String 
  

  

  

  
    

Returns The contents of the acknowledgements in Markdown format.

  

  

Returns:

  
    
- 
      
      
        (String)
      
      
      
        —
        

The contents of the acknowledgements in Markdown format.

      
    
  

  
    
      

```

16
17
18
```

    
    
      

```
# File 'lib/cocoapods/generator/acknowledgements/markdown.rb', line 16

def generate
  licenses
end
```

    
  

    
      
  
### 
  
    #**licenses**  ⇒ Object 
  

  

  

  
    
      

```

32
33
34
35
36
37
38
39
40
41
```

    
    
      

```
# File 'lib/cocoapods/generator/acknowledgements/markdown.rb', line 32

def licenses
  licenses_string = "#{title_from_string(header_title, 1)}\n#{header_text}\n"
  specs.each do |spec|
    if (license = string_for_spec(spec))
      license = license.force_encoding('UTF-8') if license.respond_to?(:force_encoding)
      licenses_string += license
    end
  end
  licenses_string += "#{title_from_string(footnote_title, 2)}#{footnote_text}\n"
end
```

    
  

    
      
  
### 
  
    #**save_as**(path)  ⇒ Object 
  

  

  

  
    
      

```

8
9
10
11
12
```

    
    
      

```
# File 'lib/cocoapods/generator/acknowledgements/markdown.rb', line 8

def save_as(path)
  file = File.new(path, 'w')
  file.write(licenses)
  file.close
end
```

    
  

    
      
  
### 
  
    #**string_for_spec**(spec)  ⇒ Object 
  

  

  

  
    
      

```

26
27
28
29
30
```

    
    
      

```
# File 'lib/cocoapods/generator/acknowledgements/markdown.rb', line 26

def string_for_spec(spec)
  if (license_text = license_text(spec))
    "\n" << title_from_string(spec.name, 2) << "\n\n" << license_text << "\n"
  end
end
```

    
  

    
      
  
### 
  
    #**title_from_string**(string, level)  ⇒ Object 
  

  

  

  
    
      

```

20
21
22
23
24
```

    
    
      

```
# File 'lib/cocoapods/generator/acknowledgements/markdown.rb', line 20

def title_from_string(string, level)
  unless string.empty?
    '#' * level << " #{string}"
  end
end
```