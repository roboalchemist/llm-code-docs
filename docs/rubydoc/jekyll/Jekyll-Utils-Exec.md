# Module: Jekyll::Utils::Exec
  
      Extended by:
      Exec
  
  
  
  
  

  
  
    Included in:
    Exec
  
  

  
  
    Defined in:
    lib/jekyll/utils/exec.rb
  
  

  
    
##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**run**(*args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Runs a program in a sub-shell.

## Instance Method Details

###
  
    #**run**(*args)  ⇒ Object 
  

  

  

  
    

Runs a program in a sub-shell.

*args - a list of strings containing the program name and arguments

Returns a Process::Status and a String of output in an array in that order.

```

16
17
18
19
20
21
22
23
```

```
# File 'lib/jekyll/utils/exec.rb', line 16

def run(*args)
  stdin, stdout, stderr, process = Open3.popen3(*args)
  out = stdout.read.strip
  err = stderr.read.strip

  [stdin, stdout, stderr].each(&:close)
  [process.value, out + err]
end
```
