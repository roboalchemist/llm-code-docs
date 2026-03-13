# Class: Jekyll::Drops::Drop
  
    Inherits:
    
      Liquid::Drop
      
        

          
- Object

- Liquid::Drop

- Jekyll::Drops::Drop

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      Enumerable
  
    Defined in:
    lib/jekyll/drops/drop.rb
  
## Direct Known Subclasses

CollectionDrop, DocumentDrop, SiteDrop, StaticFileDrop, ThemeDrop, UnifiedPayloadDrop, UrlDrop

##

      Constant Summary
      collapse
    

    
      
        NON_CONTENT_METHODS =
          
        
        

```
[:fallback_data, :collapse_document].freeze

```

##

      Class Method Summary
      collapse
    

    

      
        
-
  
      .**data_delegator**(key)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Generate public Drop instance_methods for given string `key`.

-
  
      .**data_delegators**(*strings)  ⇒ Object 

Generate public Drop instance_methods for each string entry in the given list.

-
  
      .**delegate_method**(symbol)  ⇒ Object 

Generate public Drop instance_method for given symbol that calls ‘@obj.<sym>`.

-
  
      .**delegate_method_as**(original, delegate)  ⇒ Object 

Generate public Drop instance_method named `delegate` that calls ‘@obj.<original>`.

-
  
      .**delegate_methods**(*symbols)  ⇒ Object 

Generate public Drop instance_methods for each symbol in the given list.

-
  
      .**getter_method_names**  ⇒ Object 

Array of stringified instance methods that do not end with the assignment operator.

-
  
      .**mutable**(is_mutable = nil)  ⇒ Object 

Get or set whether the drop class is mutable.

-
  
      .**mutable?**  ⇒ Boolean 

-
  
      .**private_delegate_methods**(*symbols)  ⇒ Object 

Generate private Drop instance_methods for each symbol in the given list.

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**[]**(key)  ⇒ Object 
    

    
      (also: #invoke_drop)
    
  
  
  
  
  
  
  
  

  
    

Access a method in the Drop or a field in the underlying hash data.

-
  
      #**[]=**(key, val)  ⇒ Object 

Set a field in the Drop.

-
  
      #**content_methods**  ⇒ Object 

Generates a list of strings which correspond to content getter methods.

-
  
      #**each**  ⇒ Object 

-
  
      #**each_key**(&block)  ⇒ Object 

Collects all the keys and passes each to the block in turn.

-
  
      #**fetch**(key, default = nil, &block)  ⇒ Object 

Imitate Hash.fetch method in Drop.

-
  
      #**hash_for_json**  ⇒ Object 

Generate a Hash for use in generating JSON.

-
  
      #**initialize**(obj)  ⇒ Drop 

    constructor
  
  
  
  
  
  

  
    

Create a new Drop.

-
  
      #**inspect**  ⇒ Object 

Inspect the drop’s keys and values through a JSON representation of its keys and values.

-
  
      #**key?**(key)  ⇒ Boolean 

Check if key exists in Drop.

-
  
      #**keys**  ⇒ Object 

Generates a list of keys with user content as their values.

-
  
      #**merge**(other, &block)  ⇒ Object 

-
  
      #**merge!**(other)  ⇒ Object 

-
  
      #**to_h**  ⇒ Object 

      (also: #to_hash)
    
  
  
  
  
  
  
  
  

  
    

Generate a Hash representation of the Drop by resolving each key’s value.

-
  
      #**to_json**(state = nil)  ⇒ Object 

Generate a JSON representation of the Drop.

## Constructor Details

###
  
    #**initialize**(obj)  ⇒ Drop 
  

  

  

  
    

Create a new Drop

obj - the Jekyll Site, Collection, or Document required by the drop.

Returns nothing

```

112
113
114
```

```
# File 'lib/jekyll/drops/drop.rb', line 112

def initialize(obj)
  @obj = obj
end

```

## Class Method Details

###
  
    .**data_delegator**(key)  ⇒ Object 
  

  

  

  
    

Generate public Drop instance_methods for given string `key`. The generated method access(es) ‘@obj`’s data hash.

Returns method symbol.

```

90
91
92
```

```
# File 'lib/jekyll/drops/drop.rb', line 90

def data_delegator(key)
  define_method(key.to_sym) { @obj.data[key] }
end

```

###
  
    .**data_delegators**(*strings)  ⇒ Object 
  

  

  

  
    

Generate public Drop instance_methods for each string entry in the given list. The generated method(s) access(es) ‘@obj`’s data hash.

Returns nothing.

```

79
80
81
82
83
84
```

```
# File 'lib/jekyll/drops/drop.rb', line 79

def data_delegators(*strings)
  strings.each do |key|
    data_delegator(key) if key.is_a?(String)
  end
  nil
end

```

###
  
    .**delegate_method**(symbol)  ⇒ Object 
  

  

  

  
    

Generate public Drop instance_method for given symbol that calls ‘@obj.<sym>`.

Returns delegated method symbol.

```

64
65
66
```

```
# File 'lib/jekyll/drops/drop.rb', line 64

def delegate_method(symbol)
  define_method(symbol) { @obj.send(symbol) }
end

```

###
  
    .**delegate_method_as**(original, delegate)  ⇒ Object 
  

  

  

  
    

Generate public Drop instance_method named `delegate` that calls ‘@obj.<original>`.

Returns delegated method symbol.

```

71
72
73
```

```
# File 'lib/jekyll/drops/drop.rb', line 71

def delegate_method_as(original, delegate)
  define_method(delegate) { @obj.send(original) }
end

```

###
  
    .**delegate_methods**(*symbols)  ⇒ Object 
  

  

  

  
    

Generate public Drop instance_methods for each symbol in the given list.

Returns nothing.

```

56
57
58
59
```

```
# File 'lib/jekyll/drops/drop.rb', line 56

def delegate_methods(*symbols)
  symbols.each { |symbol| delegate_method(symbol) }
  nil
end

```

###
  
    .**getter_method_names**  ⇒ Object 
  

  

  

  
    

Array of stringified instance methods that do not end with the assignment operator.

(<klass>.instance_methods always generates a new Array object so it can be mutated)

Returns array of strings.

```

99
100
101
102
103
```

```
# File 'lib/jekyll/drops/drop.rb', line 99

def getter_method_names
  @getter_method_names ||= instance_methods.map!(&:to_s).tap do |list|
    list.reject! { |item| item.end_with?("=") }
  end
end

```

###
  
    .**mutable**(is_mutable = nil)  ⇒ Object 
  

  

  

  
    

Get or set whether the drop class is mutable. Mutability determines whether or not pre-defined fields may be overwritten.

is_mutable - Boolean set mutability of the class (default: nil)

Returns the mutability of the class

```

34
35
36
```

```
# File 'lib/jekyll/drops/drop.rb', line 34

def mutable(is_mutable = nil)
  @is_mutable = is_mutable || false
end

```

###
  
    .**mutable?**  ⇒ Boolean 
  

  

  

  
    

Returns:

-

        (Boolean)

```

38
39
40
```

```
# File 'lib/jekyll/drops/drop.rb', line 38

def mutable?
  @is_mutable
end

```

###
  
    .**private_delegate_methods**(*symbols)  ⇒ Object 
  

  

  

  
    

Generate private Drop instance_methods for each symbol in the given list.

Returns nothing.

```

48
49
50
51
```

```
# File 'lib/jekyll/drops/drop.rb', line 48

def private_delegate_methods(*symbols)
  symbols.each { |symbol| private delegate_method(symbol) }
  nil
end

```

## Instance Method Details

###
  
    #**[]**(key)  ⇒ Object 
  

  
    Also known as:
    invoke_drop
    
  

  

  
    

Access a method in the Drop or a field in the underlying hash data. If mutable, checks the mutations first. Then checks the methods, and finally check the underlying hash (e.g. document front matter) if all the previous places didn’t match.

key - the string key whose value to fetch

Returns the value for the given key, or nil if none exists

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
```

```
# File 'lib/jekyll/drops/drop.rb', line 124

def [](key)
  if self.class.mutable? && mutations.key?(key)
    mutations[key]
  elsif self.class.invokable? key
    public_send key
  else
    fallback_data[key]
  end
end

```

###
  
    #**[]=**(key, val)  ⇒ Object 
  

  

  

  
    

Set a field in the Drop. If mutable, sets in the mutations and returns. If not mutable, checks first if it’s trying to override a Drop method and raises a DropMutationException if so. If not mutable and the key is not a method on the Drop, then it sets the key to the value in the underlying hash (e.g. document front matter)

key - the String key whose value to set val - the Object to set the key’s value to

Returns the value the key was set to unless the Drop is not mutable and the key matches a method in which case it raises a DropMutationException.

```

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
159
160
161
```

```
# File 'lib/jekyll/drops/drop.rb', line 148

def []=(key, val)
  setter = SETTER_KEYS_STASH[key] || "#{key}="
  if respond_to?(setter)
    public_send(setter, val)
  elsif respond_to?(key.to_s)
    if self.class.mutable?
      mutations[key] = val
    else
      raise Errors::DropMutationException, "Key #{key} cannot be set in the drop."
    end
  else
    fallback_data[key] = val
  end
end

```

###
  
    #**content_methods**  ⇒ Object 
  

  

  

  
    

Generates a list of strings which correspond to content getter methods.

Returns an Array of strings which represent method-specific keys.

```

167
168
169
170
171
172
```

```
# File 'lib/jekyll/drops/drop.rb', line 167

def content_methods
  @content_methods ||= \
    self.class.getter_method_names \
      - Jekyll::Drops::Drop.getter_method_names \
      - NON_CONTENT_METHOD_NAMES
end

```

###
  
    #**each**  ⇒ Object 
  

  

  

  
    
      

```

244
245
246
247
248
```

```
# File 'lib/jekyll/drops/drop.rb', line 244

def each
  each_key.each do |key|
    yield key, self[key]
  end
end

```

###
  
    #**each_key**(&block)  ⇒ Object 
  

  

  

  
    

Collects all the keys and passes each to the block in turn.

block - a block which accepts one argument, the key

Returns nothing.

```

240
241
242
```

```
# File 'lib/jekyll/drops/drop.rb', line 240

def each_key(&block)
  keys.each(&block)
end

```

###
  
    #**fetch**(key, default = nil, &block)  ⇒ Object 
  

  

  

  
    

Imitate Hash.fetch method in Drop

Returns value if key is present in Drop, otherwise returns default value KeyError is raised if key is not present and no default value given

Raises:

-

        (KeyError)

```

279
280
281
282
283
284
285
```

```
# File 'lib/jekyll/drops/drop.rb', line 279

def fetch(key, default = nil, &block)
  return self[key] if key?(key)
  raise KeyError, %(key not found: "#{key}") if default.nil? && block.nil?
  return yield(key) unless block.nil?

  default unless default.nil?
end

```

###
  
    #**hash_for_json**  ⇒ Object 
  

  

  

  
    

Generate a Hash for use in generating JSON. This is useful if fields need to be cleared before the JSON can generate.

Returns a Hash ready for JSON generation.

```

222
223
224
```

```
# File 'lib/jekyll/drops/drop.rb', line 222

def hash_for_json(*)
  to_h
end

```

###
  
    #**inspect**  ⇒ Object 
  

  

  

  
    

Inspect the drop’s keys and values through a JSON representation of its keys and values.

Returns a pretty generation of the hash representation of the Drop.

```

214
215
216
```

```
# File 'lib/jekyll/drops/drop.rb', line 214

def inspect
  JSON.pretty_generate to_h
end

```

###
  
    #**key?**(key)  ⇒ Boolean 
  

  

  

  
    

Check if key exists in Drop

key - the string key whose value to fetch

Returns true if the given key is present

Returns:

-

        (Boolean)

```

179
180
181
182
183
184
```

```
# File 'lib/jekyll/drops/drop.rb', line 179

def key?(key)
  return false if key.nil?
  return true if self.class.mutable? && mutations.key?(key)

  respond_to?(key) || fallback_data.key?(key)
end

```

###
  
    #**keys**  ⇒ Object 
  

  

  

  
    

Generates a list of keys with user content as their values. This gathers up the Drop methods and keys of the mutations and underlying data hashes and performs a set union to ensure a list of unique keys for the Drop.

Returns an Array of unique keys for content for the Drop.

```

192
193
194
195
196
```

```
# File 'lib/jekyll/drops/drop.rb', line 192

def keys
  (content_methods |
    mutations.keys |
    fallback_data.keys).flatten
end

```

###
  
    #**merge**(other, &block)  ⇒ Object 
  

  

  

  
    
      

```

250
251
252
253
254
255
256
257
258
```

```
# File 'lib/jekyll/drops/drop.rb', line 250

def merge(other, &block)
  dup.tap do |me|
    if block.nil?
      me.merge!(other)
    else
      me.merge!(other, block)
    end
  end
end

```

###
  
    #**merge!**(other)  ⇒ Object 
  

  

  

  
    
      

```

260
261
262
263
264
265
266
267
268
269
270
271
272
273
```

```
# File 'lib/jekyll/drops/drop.rb', line 260

def merge!(other)
  other.each_key do |key|
    if block_given?
      self[key] = yield key, self[key], other[key]
    else
      if Utils.mergable?(self[key]) && Utils.mergable?(other[key])
        self[key] = Utils.deep_merge_hashes(self[key], other[key])
        next
      end

      self[key] = other[key] unless other[key].nil?
    end
  end
end

```

###
  
    #**to_h**  ⇒ Object 
  

  
    Also known as:
    to_hash
    
  

  

  
    

Generate a Hash representation of the Drop by resolving each key’s value. It includes Drop methods, mutations, and the underlying object’s data. See the documentation for Drop#keys for more.

Returns a Hash with all the keys and values resolved.

```

203
204
205
206
207
```

```
# File 'lib/jekyll/drops/drop.rb', line 203

def to_h
  keys.each_with_object({}) do |(key, _), result|
    result[key] = self[key]
  end
end

```

###
  
    #**to_json**(state = nil)  ⇒ Object 
  

  

  

  
    

Generate a JSON representation of the Drop.

state - the JSON::State object which determines the state of current processing.

Returns a JSON representation of the Drop in a String.

```

231
232
233
```

```
# File 'lib/jekyll/drops/drop.rb', line 231

def to_json(state = nil)
  JSON.generate(hash_for_json(state), state)
end

```
