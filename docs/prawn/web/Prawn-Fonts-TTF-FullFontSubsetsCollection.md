# Class: Prawn::Fonts::TTF::FullFontSubsetsCollection
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Prawn::Fonts::TTF::FullFontSubsetsCollection
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/prawn/fonts/ttf.rb
  
  

## Overview

  
    

An adapter for subset collection to represent a full font.

  

  

  
    
## 
      Constant Summary
      collapse
    

    
      
        FULL_FONT =
          
        
        

```
Object.new.tap do |obj|
  obj.singleton_class.define_method(:inspect) do
    super().insert(-2, ' FULL_FONT')
  end
end.freeze

```

      
    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**encode**(characters)  ⇒ Array<Array(FULL_FONT, String)> 
    

    
  
  
  
  
  
  
  
  

  
    

Encode characters.

  

      
        
- 
  
    
      #**initialize**(original)  ⇒ FullFontSubsetsCollection 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of FullFontSubsetsCollection.

  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(original)  ⇒ FullFontSubsetsCollection 
  

  

  

  
    

Returns a new instance of FullFontSubsetsCollection.

  

  

  
    
      

```

77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
```

    
    
      

```
# File 'lib/prawn/fonts/ttf.rb', line 77

def initialize(original)
  @original = original

  (@cmap ||= original.cmap.unicode.first) || raise(NoUnicodeCMap.new(font: name))

  @code_space_size =
    case cmap.code_map.keys.max
    when 0..0xff then 1
    when 0x100..0xffff then 2
    when 0x10000..0xffffff then 3
    else
      4
    end

  # Codespaces are not sequentional, they're ranges in
  # a multi-dimentional space. Each byte is considered separately. So we
  # have to maximally extend the lower two bytes in order to allow for
  # continuos Unicode mapping.
  # We only keep the highest byte because Unicode only goes to 1FFFFF
  # and fonts usually cover even less of the space. We don't want to
  # list all those unmapped charac codes here.
  @code_space_max = cmap.code_map.keys.max | ('ff' * (code_space_size - 1)).to_i(16)
end

```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**encode**(characters)  ⇒ Array<Array(FULL_FONT, String)> 
  

  

  

  
    

Encode characters.

  

  

Returns:

  
    
- 
      
      
        (Array<Array(FULL_FONT, String)>)
      
      
      
    
  

  
    
      

```

104
105
106
107
108
109
110
111
112
113
114
```

    
    
      

```
# File 'lib/prawn/fonts/ttf.rb', line 104

def encode(characters)
  [
    [
      FULL_FONT,
      characters.map { |c|
        check_bounds!(c)
        [cmap[c]].pack('n')
      }.join(''),
    ],
  ]
end

```