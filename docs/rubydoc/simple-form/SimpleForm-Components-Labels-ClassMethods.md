# Module: SimpleForm::Components::Labels::ClassMethods
  
  
  

  

  
  
  
  
  

  

  
  
    Defined in:
    lib/simple_form/components/labels.rb
  
  

## Overview

  
    

:nodoc:

  

  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**translate_required_html**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**translate_required_mark**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**translate_required_text**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**translate_required_html**  ⇒ Object 
  

  

  

  
    
      

```

8
9
10
11
12
```

    
    
      

```
# File 'lib/simple_form/components/labels.rb', line 8

def translate_required_html
  I18n.t(:"required.html", scope: i18n_scope, default:
    %(<abbr title="#{translate_required_text}">#{translate_required_mark}</abbr>)
  )
end
```

    
  

    
      
  
### 
  
    #**translate_required_mark**  ⇒ Object 
  

  

  

  
    
      

```

18
19
20
```

    
    
      

```
# File 'lib/simple_form/components/labels.rb', line 18

def translate_required_mark
  I18n.t(:"required.mark", scope: i18n_scope, default: '*')
end
```

    
  

    
      
  
### 
  
    #**translate_required_text**  ⇒ Object 
  

  

  

  
    
      

```

14
15
16
```

    
    
      

```
# File 'lib/simple_form/components/labels.rb', line 14

def translate_required_text
  I18n.t(:"required.text", scope: i18n_scope, default: 'required')
end
```