# Module: Rantly::Silly::Love
  
  
  

  

  
  
  
  
  

  

  
  
    Defined in:
    lib/rantly/silly.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**address**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**caused_by**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**double_plus_good**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**extremifier**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**fantasy**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**fragment**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**groveler**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**how_i_feel**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**humbleizer**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**i_am_stalking_you**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**letter**(n = 3)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**paragraph**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**pedestal_label**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**post_script**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**sentence**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**sign**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**stalk_action**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**time_duration**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**whoami**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**address**  ⇒ Object 
  

  

  

  
    
      

```

24
25
26
```

    
    
      

```
# File 'lib/rantly/silly.rb', line 24

def address
  "my #{extremifier} #{pedestal_label}"
end

```

    
  

    
      
  
### 
  
    #**caused_by**  ⇒ Object 
  

  

  

  
    
      

```

64
```

    
    
      

```
# File 'lib/rantly/silly.rb', line 64

def caused_by; end

```

    
  

    
      
  
### 
  
    #**double_plus_good**  ⇒ Object 
  

  

  

  
    
      

```

36
37
38
```

    
    
      

```
# File 'lib/rantly/silly.rb', line 36

def double_plus_good
  choose 'holy', 'shiny', 'glittering', 'joyous', 'delicious'
end

```

    
  

    
      
  
### 
  
    #**extremifier**  ⇒ Object 
  

  

  

  
    
      

```

28
29
30
```

    
    
      

```
# File 'lib/rantly/silly.rb', line 28

def extremifier
  choose 'most', 'ultimate', 'unbelievable', 'incredible', 'burning'
end

```

    
  

    
      
  
### 
  
    #**fantasy**  ⇒ Object 
  

  

  

  
    
      

```

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
100
101
102
103
104
105
106
107
```

    
    
      

```
# File 'lib/rantly/silly.rb', line 90

def fantasy
  freq \
    proc {
      make = choose 'raise', 'nurture', 'bring into the world'
      babies = choose 'brood of babies', "#{double_plus_good} angels"
      good = double_plus_good
      effect = choose "the world becomes all the more #{good}",
                      "we may at the end of our lives rest in #{good} peace.",
                      "you, my #{pedestal_label}, would continue to live."
      "we would #{make} #{babies}, so #{effect}."
    },
    proc {
      do_thing = choose('kiss', 'hug', 'read poetry to each other', 'massage', "whisper empty nothings into each others' ears",
                        'be with each other, and oblivious to the entire world')
      affect = choose 'joy', 'mindfulness', 'calm', 'sanctity'
      "we would #{do_thing} with #{double_plus_good} #{affect}"
    }
end

```

    
  

    
      
  
### 
  
    #**fragment**  ⇒ Object 
  

  

  

  
    
      

```

59
60
61
62
```

    
    
      

```
# File 'lib/rantly/silly.rb', line 59

def fragment
  fun = fantasy
  choose "i hope to god #{fun}", "i believe #{fun}", "i will that #{fun}"
end

```

    
  

    
      
  
### 
  
    #**groveler**  ⇒ Object 
  

  

  

  
    
      

```

78
79
80
```

    
    
      

```
# File 'lib/rantly/silly.rb', line 78

def groveler
  choose 'slave', 'servant', 'captive', 'lapdog'
end

```

    
  

    
      
  
### 
  
    #**how_i_feel**  ⇒ Object 
  

  

  

  
    
      

```

40
41
42
```

    
    
      

```
# File 'lib/rantly/silly.rb', line 40

def how_i_feel
  choose 'my heart aches', 'my spine pines', 'my spirit wanders and wonders', 'my soul is awed', 'my loin burns'
end

```

    
  

    
      
  
### 
  
    #**humbleizer**  ⇒ Object 
  

  

  

  
    
      

```

74
75
76
```

    
    
      

```
# File 'lib/rantly/silly.rb', line 74

def humbleizer
  choose 'undeserving', 'insignificant', 'unremarkable', 'fearful', 'menial'
end

```

    
  

    
      
  
### 
  
    #**i_am_stalking_you**  ⇒ Object 
  

  

  

  
    
      

```

86
87
88
```

    
    
      

```
# File 'lib/rantly/silly.rb', line 86

def i_am_stalking_you
  "every #{time_duration} i #{stalk_action}"
end

```

    
  

    
      
  
### 
  
    #**letter**(n = 3)  ⇒ Object 
  

  

  

  
    
      

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
```

    
    
      

```
# File 'lib/rantly/silly.rb', line 11

def letter(n = 3)
  body = array(n) { paragraph }.join "\n\n"
  "    \#{address}:\n\n    \#{body}\n\n    \#{sign}\n\n    \#{post_script}\n  EOS\nend\n"

```

    
  

    
      
  
### 
  
    #**paragraph**  ⇒ Object 
  

  

  

  
    
      

```

44
45
46
```

    
    
      

```
# File 'lib/rantly/silly.rb', line 44

def paragraph
  array(range(2, 4)) { sentence }.join ' '
end

```

    
  

    
      
  
### 
  
    #**pedestal_label**  ⇒ Object 
  

  

  

  
    
      

```

32
33
34
```

    
    
      

```
# File 'lib/rantly/silly.rb', line 32

def pedestal_label
  choose 'beloved', 'desire', 'dove', 'virgin goddess', 'existential solution', 'lighthouse', 'beacon', 'holy mother', 'queen', 'mistress'
end

```

    
  

    
      
  
### 
  
    #**post_script**  ⇒ Object 
  

  

  

  
    
      

```

82
83
84
```

    
    
      

```
# File 'lib/rantly/silly.rb', line 82

def post_script
  "ps: #{i_am_stalking_you}, and hope that #{fantasy}"
end

```

    
  

    
      
  
### 
  
    #**sentence**  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/rantly/silly.rb', line 48

def sentence
  freq \
    proc {
      "when #{how_i_feel}, my #{pedestal_label}, i feel the need to #{stalk_action},"\
           "but this is not because #{how_i_feel}, but rather a symptom of my being your #{whoami}."
    },
    proc { "because you are my #{pedestal_label}, and i am your #{whoami}, no, rather your #{whoami}, #{fragment}." },
    proc { "do not think that saying '#{how_i_feel}' suffices to show the depth of how #{how_i_feel}, because more than that, #{fantasy}" },
    proc { "as a #{whoami}, that #{how_i_feel} is never quite enough for you, my #{double_plus_good} #{pedestal_label}." }
end

```

    
  

    
      
  
### 
  
    #**sign**  ⇒ Object 
  

  

  

  
    
      

```

70
71
72
```

    
    
      

```
# File 'lib/rantly/silly.rb', line 70

def sign
  "your #{whoami}"
end

```

    
  

    
      
  
### 
  
    #**stalk_action**  ⇒ Object 
  

  

  

  
    
      

```

109
110
111
```

    
    
      

```
# File 'lib/rantly/silly.rb', line 109

def stalk_action
  choose 'think of you', 'dream of us together', 'look at your picture and sigh'
end

```

    
  

    
      
  
### 
  
    #**time_duration**  ⇒ Object 
  

  

  

  
    
      

```

113
114
115
```

    
    
      

```
# File 'lib/rantly/silly.rb', line 113

def time_duration
  choose 'once in a while', 'night', 'day', 'hour', 'minute'
end

```

    
  

    
      
  
### 
  
    #**whoami**  ⇒ Object 
  

  

  

  
    
      

```

66
67
68
```

    
    
      

```
# File 'lib/rantly/silly.rb', line 66

def whoami
  "#{extremifier} #{humbleizer} #{groveler}"
end

```