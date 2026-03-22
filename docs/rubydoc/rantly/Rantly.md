# Class: Rantly
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Rantly
          
        

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      Data
  
  
  

  

  
  
    Defined in:
    lib/rantly.rb,

  lib/rantly/data.rb,
 lib/rantly/generator.rb

  
  

## Defined Under Namespace

  
    
      **Modules:** Chars, Check, Data, Silly
    
  
    
      **Classes:** GuardFailure, Property, TooManyTries
    
  

  
    
## 
      Constant Summary
      collapse
    

    
      
        INTEGER_MAX =
          
  
    

wanna avoid going into Bignum when calling range with these.

  

  

        
        

```
(2**(0.size * 8 - 2) - 1) / 2

```

      
        INTEGER_MIN =
          
        
        

```
-INTEGER_MAX

```

      
    
  

  
## Class Attribute Summary collapse

  

    
      
- 
  
    
      .**default_size**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    
  

    
  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**classifiers**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute classifiers.

  

    
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**each**(n, limit = 10, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**gen**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**map**(n, limit = 10, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**singleton**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**value**(limit = 10, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**array**(n = size, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**boolean**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**branch**(*gens)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**call**(gen, *args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**choose**(*vals)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**classify**(classifier)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**dict**(n = size, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**each**(n, limit = 10, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

limit attempts to 10 times of how many things we want to generate.

  

      
        
- 
  
    
      #**float**(distribution = nil, params = {})  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**freq**(*pairs)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**generate**(n, limit_arg, gen_block, &handler)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**guard**(test)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**  ⇒ Rantly 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Rantly.

  

      
        
- 
  
    
      #**integer**(limit = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**literal**(value)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**map**(n, limit = 10, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**positive_integer**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**range**(lo = INTEGER_MIN, hi = INTEGER_MAX)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**reset**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**size**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**sized**(n, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**string**(char_class = :print)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**value**(limit = 10, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods included from Data

  

#email, #password

  
## Constructor Details

  
    
  
### 
  
    #**initialize**  ⇒ Rantly 
  

  

  

  
    

Returns a new instance of Rantly.

  

  

  
    
      

```

88
89
90
```

    
    
      

```
# File 'lib/rantly/generator.rb', line 88

def initialize
  reset
end

```

    
  

  

  
    
## Class Attribute Details

    
      
      
      
  
### 
  
    .**default_size**  ⇒ Object 
  

  

  

  
    
      

```

10
11
12
```

    
    
      

```
# File 'lib/rantly/generator.rb', line 10

def default_size
  @default_size || 6
end

```

    
  

    
  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**classifiers**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute classifiers.

  

  

  
    
      

```

86
87
88
```

    
    
      

```
# File 'lib/rantly/generator.rb', line 86

def classifiers
  @classifiers
end

```

    
  

    
  

  
    
## Class Method Details

    
      
  
### 
  
    .**each**(n, limit = 10, &block)  ⇒ Object 
  

  

  

  
    
      

```

14
15
16
```

    
    
      

```
# File 'lib/rantly/generator.rb', line 14

def each(n, limit = 10, &block)
  gen.each(n, limit, &block)
end

```

    
  

    
      
  
### 
  
    .**gen**  ⇒ Object 
  

  

  

  
    
      

```

26
27
28
```

    
    
      

```
# File 'lib/rantly/generator.rb', line 26

def gen
  singleton
end

```

    
  

    
      
  
### 
  
    .**map**(n, limit = 10, &block)  ⇒ Object 
  

  

  

  
    
      

```

18
19
20
```

    
    
      

```
# File 'lib/rantly/generator.rb', line 18

def map(n, limit = 10, &block)
  gen.map(n, limit, &block)
end

```

    
  

    
      
  
### 
  
    .**singleton**  ⇒ Object 
  

  

  

  
    
      

```

5
6
7
8
```

    
    
      

```
# File 'lib/rantly/generator.rb', line 5

def singleton
  @singleton ||= Rantly.new
  @singleton
end

```

    
  

    
      
  
### 
  
    .**value**(limit = 10, &block)  ⇒ Object 
  

  

  

  
    
      

```

22
23
24
```

    
    
      

```
# File 'lib/rantly/generator.rb', line 22

def value(limit = 10, &block)
  gen.value(limit, &block)
end

```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**array**(n = size, &block)  ⇒ Object 
  

  

  

  
    
      

```

220
221
222
```

    
    
      

```
# File 'lib/rantly/generator.rb', line 220

def array(n = size, &block)
  n.times.map { instance_eval(&block) }
end

```

    
  

    
      
  
### 
  
    #**boolean**  ⇒ Object 
  

  

  

  
    
      

```

191
192
193
```

    
    
      

```
# File 'lib/rantly/generator.rb', line 191

def boolean
  range(0, 1).zero?
end

```

    
  

    
      
  
### 
  
    #**branch**(*gens)  ⇒ Object 
  

  

  

  
    
      

```

179
180
181
```

    
    
      

```
# File 'lib/rantly/generator.rb', line 179

def branch(*gens)
  call(choose(*gens))
end

```

    
  

    
      
  
### 
  
    #**call**(gen, *args)  ⇒ Object 
  

  

  

  
    
      

```

164
165
166
167
168
169
170
171
172
173
174
175
176
177
```

    
    
      

```
# File 'lib/rantly/generator.rb', line 164

def call(gen, *args)
  case gen
  when Symbol
    send(gen, *args)
  when Array
    raise 'empty array' if gen.empty?

    send(gen[0], *gen[1..-1])
  when Proc
    instance_eval(&gen)
  else
    raise "don't know how to call type: #{gen}"
  end
end

```

    
  

    
      
  
### 
  
    #**choose**(*vals)  ⇒ Object 
  

  

  

  
    
      

```

183
184
185
```

    
    
      

```
# File 'lib/rantly/generator.rb', line 183

def choose(*vals)
  vals[range(0, vals.length - 1)] if vals.length.positive?
end

```

    
  

    
      
  
### 
  
    #**classify**(classifier)  ⇒ Object 
  

  

  

  
    
      

```

97
98
99
```

    
    
      

```
# File 'lib/rantly/generator.rb', line 97

def classify(classifier)
  @classifiers[classifier] += 1
end

```

    
  

    
      
  
### 
  
    #**dict**(n = size, &block)  ⇒ Object 
  

  

  

  
    
      

```

224
225
226
227
228
229
230
231
```

    
    
      

```
# File 'lib/rantly/generator.rb', line 224

def dict(n = size, &block)
  h = {}
  each(n) do
    k, v = instance_eval(&block)
    h[k] = v if guard(!h.key?(k))
  end
  h
end

```

    
  

    
      
  
### 
  
    #**each**(n, limit = 10, &block)  ⇒ Object 
  

  

  

  
    

limit attempts to 10 times of how many things we want to generate

  

  

  
    
      

```

48
49
50
```

    
    
      

```
# File 'lib/rantly/generator.rb', line 48

def each(n, limit = 10, &block)
  generate(n, limit, block)
end

```

    
  

    
      
  
### 
  
    #**float**(distribution = nil, params = {})  ⇒ Object 
  

  

  

  
    
      

```

145
146
147
148
149
150
151
152
153
154
155
156
157
158
```

    
    
      

```
# File 'lib/rantly/generator.rb', line 145

def float(distribution = nil, params = {})
  case distribution
  when :normal
    params[:center] ||= 0
    params[:scale] ||= 1
    raise 'The distribution scale should be greater than zero' if params[:scale].negative?

    # Sum of 6 draws from a uniform distribution give as a draw of a normal
    # distribution centered in 3 (central limit theorem).
    ([rand, rand, rand, rand, rand, rand].sum - 3) * params[:scale] + params[:center]
  else
    rand
  end
end

```

    
  

    
      
  
### 
  
    #**freq**(*pairs)  ⇒ Object 
  

  

  

  
    
      

```

195
196
197
198
199
200
201
202
203
204
205
206
207
208
209
210
211
212
213
214
215
216
217
218
```

    
    
      

```
# File 'lib/rantly/generator.rb', line 195

def freq(*pairs)
  pairs = pairs.map do |pair|
    case pair
    when Symbol, String, Proc
      [1, pair]
    when Array
      if pair.first.is_a?(Integer)
        pair
      else
        [1] + pair
      end
    end
  end
  total = pairs.inject(0) { |sum, p| sum + p.first }
  raise("Illegal frequency:#{pairs.inspect}") if total.zero?

  pos = range(1, total)
  pairs.each do |p|
    weight, gen, *args = p
    return call(gen, *args) if pos <= p[0]

    pos -= weight
  end
end

```

    
  

    
      
  
### 
  
    #**generate**(n, limit_arg, gen_block, &handler)  ⇒ Object 
  

  

  

  
    
      

```

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
81
82
83
84
```

    
    
      

```
# File 'lib/rantly/generator.rb', line 66

def generate(n, limit_arg, gen_block, &handler)
  limit = n * limit_arg
  nfailed = 0
  nsuccess = 0
  while nsuccess < n
    raise TooManyTries.new(limit_arg * n, nfailed) if limit.zero?

    begin
      val = instance_eval(&gen_block)
    rescue GuardFailure
      nfailed += 1
      limit -= 1
      next
    end
    nsuccess += 1
    limit -= 1
    yield(val) if handler
  end
end

```

    
  

    
      
  
### 
  
    #**guard**(test)  ⇒ Object 
  

  

  

  
    

  

  

Raises:

  
    
- 
      
      
        (GuardFailure)
      
      
      
    
  

  
    
      

```

101
102
103
104
105
```

    
    
      

```
# File 'lib/rantly/generator.rb', line 101

def guard(test)
  return true if test

  raise GuardFailure
end

```

    
  

    
      
  
### 
  
    #**integer**(limit = nil)  ⇒ Object 
  

  

  

  
    
      

```

124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
```

    
    
      

```
# File 'lib/rantly/generator.rb', line 124

def integer(limit = nil)
  case limit
  when Range
    hi = limit.end
    lo = limit.begin
  when Integer
    raise 'n should be greater than zero' if limit.negative?

    hi = limit
    lo = -limit
  else
    hi = INTEGER_MAX
    lo = INTEGER_MIN
  end
  range(lo, hi)
end

```

    
  

    
      
  
### 
  
    #**literal**(value)  ⇒ Object 
  

  

  

  
    
      

```

187
188
189
```

    
    
      

```
# File 'lib/rantly/generator.rb', line 187

def literal(value)
  value
end

```

    
  

    
      
  
### 
  
    #**map**(n, limit = 10, &block)  ⇒ Object 
  

  

  

  
    
      

```

52
53
54
55
56
57
58
```

    
    
      

```
# File 'lib/rantly/generator.rb', line 52

def map(n, limit = 10, &block)
  acc = []
  generate(n, limit, block) do |val|
    acc << val
  end
  acc
end

```

    
  

    
      
  
### 
  
    #**positive_integer**  ⇒ Object 
  

  

  

  
    
      

```

141
142
143
```

    
    
      

```
# File 'lib/rantly/generator.rb', line 141

def positive_integer
  range(0)
end

```

    
  

    
      
  
### 
  
    #**range**(lo = INTEGER_MIN, hi = INTEGER_MAX)  ⇒ Object 
  

  

  

  
    
      

```

160
161
162
```

    
    
      

```
# File 'lib/rantly/generator.rb', line 160

def range(lo = INTEGER_MIN, hi = INTEGER_MAX)
  rand(lo..hi)
end

```

    
  

    
      
  
### 
  
    #**reset**  ⇒ Object 
  

  

  

  
    
      

```

92
93
94
95
```

    
    
      

```
# File 'lib/rantly/generator.rb', line 92

def reset
  @size = nil
  @classifiers = Hash.new(0)
end

```

    
  

    
      
  
### 
  
    #**size**  ⇒ Object 
  

  

  

  
    
      

```

107
108
109
```

    
    
      

```
# File 'lib/rantly/generator.rb', line 107

def size
  @size || Rantly.default_size
end

```

    
  

    
      
  
### 
  
    #**sized**(n, &block)  ⇒ Object 
  

  

  

  
    
      

```

111
112
113
114
115
116
117
118
119
```

    
    
      

```
# File 'lib/rantly/generator.rb', line 111

def sized(n, &block)
  raise 'size needs to be greater than zero' if n.negative?

  old_size = @size
  @size = n
  r = instance_eval(&block)
  @size = old_size
  r
end

```

    
  

    
      
  
### 
  
    #**string**(char_class = :print)  ⇒ Object 
  

  

  

  
    
      

```

273
274
275
276
277
278
279
280
281
282
283
284
285
286
```

    
    
      

```
# File 'lib/rantly/generator.rb', line 273

def string(char_class = :print)
  chars = case char_class
          when Regexp
            Chars.of(char_class)
          when Symbol
            Chars::CLASSES[char_class]
          end
  raise 'bad arg' unless chars

  char_strings = chars.map(&:chr)
  str = Array.new(size)
  size.times { |i| str[i] = char_strings.sample }
  str.join
end

```

    
  

    
      
  
### 
  
    #**value**(limit = 10, &block)  ⇒ Object 
  

  

  

  
    
      

```

60
61
62
63
64
```

    
    
      

```
# File 'lib/rantly/generator.rb', line 60

def value(limit = 10, &block)
  generate(1, limit, block) do |val|
    return val
  end
end

```