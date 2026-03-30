# Class: Jekyll::Profiler
  
    Inherits:
    
      Object
      
        

          
- Object

- Jekyll::Profiler

        show all
      

    Defined in:
    lib/jekyll/profiler.rb
  
##

      Class Method Summary
      collapse
    

    

      
        
-
  
      .**tabulate**(table_rows)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  
    
##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**initialize**(site)  ⇒ Profiler 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Profiler.

-
  
      #**profile_process**  ⇒ Object 

## Constructor Details

###
  
    #**initialize**(site)  ⇒ Profiler 
  

  

  

  
    

Returns a new instance of Profiler.

```

30
31
32
```

```
# File 'lib/jekyll/profiler.rb', line 30

def initialize(site)
  @site = site
end
```

## Class Method Details

###
  
    .**tabulate**(table_rows)  ⇒ Object 
  

  

  

  
    
      

```

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
```

```
# File 'lib/jekyll/profiler.rb', line 12

def self.tabulate(table_rows)
  require "terminal-table"

  rows   = table_rows.dup
  header = rows.shift
  output = +"\n"

  table = Terminal::Table.new do |t|
    t << header
    t << :separator
    rows.each { |row| t << row }
    t.style = TERMINAL_TABLE_STYLES
    t.align_column(0, :left)
  end

  output << table.to_s << "\n"
end
```

## Instance Method Details

###
  
    #**profile_process**  ⇒ Object 
  

  

  

  
    
      

```

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
```

```
# File 'lib/jekyll/profiler.rb', line 34

def profile_process
  profile_data = { "PHASE" => "TIME" }

  [:reset, :read, :generate, :render, :cleanup, :write].each do |method|
    start_time = Time.now
    @site.send(method)
    end_time = (Time.now - start_time).round(4)
    profile_data[method.to_s.upcase] = format("%.4f", end_time)
  end

  Jekyll.logger.info "\nBuild Process Summary:"
  Jekyll.logger.info Profiler.tabulate(Array(profile_data))

  Jekyll.logger.info "\nSite Render Stats:"
  @site.print_stats
end
```
