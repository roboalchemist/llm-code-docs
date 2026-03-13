# Module: Jekyll::Utils::Ansi
  
      Extended by:
      Ansi
  
  
  
  
  

  
  
    Included in:
    Ansi
  
  

  
  
    Defined in:
    lib/jekyll/utils/ansi.rb
  
  

  
    
##

      Constant Summary
      collapse
    

    
      
        ESCAPE =
          
        
        

```
format("%c", 27)
```

        MATCH =
          
        
        

```
%r!#{ESCAPE}\[(?:\d+)(?:;\d+)*(j|k|m|s|u|A|B|G)|\e\(B\e\[m!ix.freeze
```

        COLORS =
          
        
        

```
{
  :red     => 31,
  :green   => 32,
  :black   => 30,
  :magenta => 35,
  :yellow  => 33,
  :white   => 37,
  :blue    => 34,
  :cyan    => 36,
}.freeze
```

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**has?**(str)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**reset**(str = "")  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Reset the color back to the default color so that you do not leak any colors when you move onto the next line.

-
  
      #**strip**(str)  ⇒ Object 

Strip ANSI from the current string.

## Instance Method Details

###
  
    #**has?**(str)  ⇒ Boolean 
  

  

  

  
    

Returns:

-

        (Boolean)

```

31
32
33
```

```
# File 'lib/jekyll/utils/ansi.rb', line 31

def has?(str)
  !!(str =~ MATCH)
end
```

###
  
    #**reset**(str = "")  ⇒ Object 
  

  

  

  
    

Reset the color back to the default color so that you do not leak any colors when you move onto the next line. This is probably normally used as part of a wrapper so that we don’t leak colors.

```

39
40
41
42
```

```
# File 'lib/jekyll/utils/ansi.rb', line 39

def reset(str = "")
  @ansi_reset ||= format("%c[0m", 27)
  "#{@ansi_reset}#{str}"
end
```

###
  
    #**strip**(str)  ⇒ Object 
  

  

  

  
    

Strip ANSI from the current string.  It also strips cursor stuff, well some of it, and it also strips some other stuff that a lot of the other ANSI strippers don’t.

```

25
26
27
```

```
# File 'lib/jekyll/utils/ansi.rb', line 25

def strip(str)
  str.gsub MATCH, ""
end
```
