# Class: Nokogiri::HTML4::EntityLookup
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Nokogiri::HTML4::EntityLookup
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/nokogiri/html4/entity_lookup.rb,

  ext/nokogiri/html4_entity_lookup.c

  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**[]**(name)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Look up entity with `name`.

  

      
        
- 
  
    
      #**get**(key)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Get the HTML4::EntityDescription for `key`.

  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**[]**(name)  ⇒ Object 
  

  

  

  
    

Look up entity with `name`

  

  

  
    
      

```

10
11
12
```

    
    
      

```
# File 'lib/nokogiri/html4/entity_lookup.rb', line 10

def [](name)
  (val = get(name)) && val.value
end

```

    
  

    
      
  
### 
  
    #**get**(key)  ⇒ Object 
  

  

  

  
    

Get the HTML4::EntityDescription for `key`

  

  
  

  
    
      

```

11
12
13
14
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
```

    
    
      

```
# File 'ext/nokogiri/html4_entity_lookup.c', line 11

static VALUE
get(VALUE _, VALUE rb_entity_name)
{
  VALUE cNokogiriHtml4EntityDescription;
  const htmlEntityDesc *c_entity_desc;
  VALUE rb_constructor_args[3];

  c_entity_desc = htmlEntityLookup((const xmlChar *)StringValueCStr(rb_entity_name));
  if (NULL == c_entity_desc) {
    return Qnil;
  }

  rb_constructor_args[0] = UINT2NUM(c_entity_desc->value);
  rb_constructor_args[1] = NOKOGIRI_STR_NEW2(c_entity_desc->name);
  rb_constructor_args[2] = NOKOGIRI_STR_NEW2(c_entity_desc->desc);

  cNokogiriHtml4EntityDescription = rb_const_get_at(mNokogiriHtml4, rb_intern("EntityDescription"));
  return rb_class_new_instance(3, rb_constructor_args, cNokogiriHtml4EntityDescription);
}

```