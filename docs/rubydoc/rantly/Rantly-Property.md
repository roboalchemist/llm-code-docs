# Class: Rantly::Property
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Rantly::Property
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/rantly/property.rb
  
  

  
    
## 
      Constant Summary
      collapse
    

    
      
        VERBOSITY =
          
        
        

```
ENV.fetch('RANTLY_VERBOSE', 1).to_i

```

      
        RANTLY_COUNT =
          
        
        

```
ENV.fetch('RANTLY_COUNT', 100).to_i

```

      
    
  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**failed_data**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute failed_data.

  

    
      
- 
  
    
      #**shrunk_failed_data**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute shrunk_failed_data.

  

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**check**(n = RANTLY_COUNT, limit = 10, &assertion)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**(property)  ⇒ Property 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Property.

  

      
        
- 
  
    
      #**io**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**pretty_print**(object)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**shrinkify**(assertion, data, depth = 0, iteration = 0)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Explore the failures tree.

  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(property)  ⇒ Property 
  

  

  

  
    

Returns a new instance of Property.

  

  

  
    
      

```

23
24
25
```

    
    
      

```
# File 'lib/rantly/property.rb', line 23

def initialize(property)
  @property = property
end

```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**failed_data**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute failed_data.

  

  

  
    
      

```

6
7
8
```

    
    
      

```
# File 'lib/rantly/property.rb', line 6

def failed_data
  @failed_data
end

```

    
  

    
      
      
      
  
### 
  
    #**shrunk_failed_data**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute shrunk_failed_data.

  

  

  
    
      

```

6
7
8
```

    
    
      

```
# File 'lib/rantly/property.rb', line 6

def shrunk_failed_data
  @shrunk_failed_data
end

```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**check**(n = RANTLY_COUNT, limit = 10, &assertion)  ⇒ Object 
  

  

  

  
    
      

```

27
28
29
30
31
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
```

    
    
      

```
# File 'lib/rantly/property.rb', line 27

def check(n = RANTLY_COUNT, limit = 10, &assertion)
  i = 0
  test_data = nil
  begin
    Rantly.singleton.generate(n, limit, @property) do |val|
      test_data = val
      yield(val) if assertion
      io.puts '' if (i % 100).zero?
      io.print '.' if (i % 10).zero?
      i += 1
    end
    io.puts
    io.puts "SUCCESS - #{i} successful tests"
  rescue Rantly::TooManyTries => e
    io.puts
    io.puts "FAILURE - #{i} successful tests, too many tries: #{e.tries}"
    raise e.exception("#{i} successful tests, too many tries: #{e.tries} (limit: #{e.limit})")
  rescue Exception => e
    io.puts
    io.puts "FAILURE - #{i} successful tests, failed on:"
    pretty_print test_data
    @failed_data = test_data
    if @failed_data.respond_to?(:shrink)
      @shrunk_failed_data, @depth = shrinkify(assertion, @failed_data)
      io.puts "Minimal failed data (depth #{@depth}) is:"
      pretty_print @shrunk_failed_data
    end
    raise e.exception("#{i} successful tests, failed on:\n#{test_data}\n\n#{e}\n")
  end
end

```

    
  

    
      
  
### 
  
    #**io**  ⇒ Object 
  

  

  

  
    
      

```

11
12
13
14
15
16
17
```

    
    
      

```
# File 'lib/rantly/property.rb', line 11

def io
  @io ||= if VERBOSITY >= 1
            $stdout
          else
            StringIO.new
          end
end

```

    
  

    
      
  
### 
  
    #**pretty_print**(object)  ⇒ Object 
  

  

  

  
    
      

```

19
20
21
```

    
    
      

```
# File 'lib/rantly/property.rb', line 19

def pretty_print(object)
  PP.pp(object, io)
end

```

    
  

    
      
  
### 
  
    #**shrinkify**(assertion, data, depth = 0, iteration = 0)  ⇒ Object 
  

  

  

  
    

Explore the failures tree

  

  

  
    
      

```

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
70
71
72
73
74
75
76
77
78
79
80
```

    
    
      

```
# File 'lib/rantly/property.rb', line 59

def shrinkify(assertion, data, depth = 0, iteration = 0)
  min_data = data
  max_depth = depth
  if data.shrinkable?
    while iteration < 1024
      # We assume that data.shrink is non-destructive
      shrunk_data = data.shrink
      begin
        assertion.call(shrunk_data)
      rescue Exception
        # If the assertion was verified, recursively shrink failure case
        branch_data, branch_depth, iteration = shrinkify(assertion, shrunk_data, depth + 1, iteration + 1)
        if branch_depth > max_depth
          min_data = branch_data
          max_depth = branch_depth
        end
      end
      break unless data.retry?
    end
  end
  [min_data, max_depth, iteration]
end

```