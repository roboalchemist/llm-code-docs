# Module: Nokogiri::XML::PP::Node
  
  
  

  

  
  
  
  
  

  
  
    Included in:
    ElementContent, Namespace, Node
  
  

  
  
    Defined in:
    lib/nokogiri/xml/pp/node.rb
  
  

  
    
## 
      Constant Summary
      collapse
    

    
      
        COLLECTIONS =
          
        
        

```
[:attribute_nodes, :children]
```

      
    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**inspect**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**pretty_print**(pp)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**inspect**  ⇒ Object 
  

  

  

  
    
      

```

10
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
30
```

    
    
      

```
# File 'lib/nokogiri/xml/pp/node.rb', line 10

def inspect
  # handle the case where an exception is thrown during object construction
  if respond_to?(:data_ptr?) && !data_ptr?
    return "#<#{self.class}:#{format("0x%x", object_id)} (no data)>"
  end

  attributes = inspect_attributes.reject do |x|
    attribute = send(x)
    !attribute || (attribute.respond_to?(:empty?) && attribute.empty?)
  rescue NoMethodError
    true
  end
  attributes = if inspect_attributes.length == 1
    send(attributes.first).inspect
  else
    attributes.map do |attribute|
      "#{attribute}=#{send(attribute).inspect}"
    end.join(" ")
  end
  "#<#{self.class}:#{format("0x%x", object_id)} #{attributes}>"
end
```

    
  

    
      
  
### 
  
    #**pretty_print**(pp)  ⇒ Object 
  

  

  

  
    
      

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
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
```

    
    
      

```
# File 'lib/nokogiri/xml/pp/node.rb', line 32

def pretty_print(pp)
  nice_name = self.class.name.split("::").last
  pp.group(2, "#(#{nice_name}:#{format("0x%x", object_id)} {", "})") do
    pp.breakable

    attrs = inspect_attributes.filter_map do |t|
      [t, send(t)] if respond_to?(t)
    end.find_all do |x|
      if x.last
        if COLLECTIONS.include?(x.first)
          !x.last.empty?
        else
          true
        end
      end
    end

    if inspect_attributes.length == 1
      pp.pp(attrs.first.last)
    else
      pp.seplist(attrs) do |v|
        if COLLECTIONS.include?(v.first)
          pp.group(2, "#{v.first} = [", "]") do
            pp.breakable
            pp.seplist(v.last) do |item|
              pp.pp(item)
            end
          end
        else
          pp.text("#{v.first} = ")
          pp.pp(v.last)
        end
      end
    end

    pp.breakable
  end
end
```