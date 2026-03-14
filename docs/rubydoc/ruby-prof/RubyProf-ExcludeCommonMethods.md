# Module: RubyProf::ExcludeCommonMethods
  
  
  

  

  
  
  
  
  

  

  
  
    Defined in:
    lib/ruby-prof/exclude_common_methods.rb
  
  

  
    
## 
      Constant Summary
      collapse
    

    
      
        ENUMERABLE_NAMES =
          
        
        

```
Enumerable.instance_methods(false)
```

      
    
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**apply!**(profile)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**exclude_enumerable**(profile, mod, *method_or_methods)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**exclude_methods**(profile, mod, *method_or_methods)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**exclude_singleton_methods**(profile, mod, *method_or_methods)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Class Method Details

    
      
  
### 
  
    .**apply!**(profile)  ⇒ Object 
  

  

  

  
    
      

```

8
9
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
100
101
102
103
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
115
116
117
118
119
120
121
122
123
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
140
141
142
143
144
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
159
160
161
162
163
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
178
179
180
181
182
183
184
185
186
187
```

    
    
      

```
# File 'lib/ruby-prof/exclude_common_methods.rb', line 8

def self.apply!(profile)
  ##
  #  Kernel Methods
  ##

  exclude_methods(profile, Kernel, [
    :dup,
    :initialize_dup,
    :tap,
    :send,
    :public_send,
  ])

  ##
  #  Fundamental Types
  ##

  exclude_methods(profile, BasicObject,  :!=)
  exclude_methods(profile, Kernel,       :"block_given?")
  exclude_methods(profile, Method,       :[])
  exclude_methods(profile, Module,       :new)
  exclude_methods(profile, Class,        :new)
  exclude_methods(profile, Proc,         :call, :yield)
  exclude_methods(profile, Range,        :each)

  ##
  #  Value Types
  ##

  exclude_methods(profile, Integer, [
    :times,
    :succ,
    :<
  ])

  exclude_methods(profile, String, [
    :sub,
    :sub!,
    :gsub,
    :gsub!,
  ])

  ##
  #  Emumerables
  ##

  exclude_enumerable(profile, Enumerable)
  exclude_enumerable(profile, Enumerator)

  ##
  #  Collections
  ##

  exclude_enumerable(profile, Array, [
    :each_index,
    :map!,
    :select!,
    :reject!,
    :collect!,
    :sort!,
    :sort_by!,
    :index,
    :delete_if,
    :keep_if,
    :drop_while,
    :uniq,
    :uniq!,
    :"==",
    :eql?,
    :hash,
    :to_json,
    :as_json,
    :encode_json,
  ])

  exclude_enumerable(profile, Hash, [
    :dup,
    :initialize_dup,
    :fetch,
    :"[]",
    :"[]=",
    :each_key,
    :each_value,
    :each_pair,
    :map!,
    :select!,
    :reject!,
    :collect!,
    :delete_if,
    :keep_if,
    :slice,
    :slice!,
    :except,
    :except!,
    :"==",
    :eql?,
    :hash,
    :to_json,
    :as_json,
    :encode_json,
  ])

  exclude_enumerable(profile, Set, [
    :map!,
    :select!,
    :reject!,
    :collect!,
    :classify,
    :delete_if,
    :keep_if,
    :divide,
    :"==",
    :eql?,
    :hash,
    :to_json,
    :as_json,
    :encode_json,
  ])

  ##
  #  Garbage Collection
  ##

  exclude_singleton_methods(profile, GC, [
    :start
  ])

  ##
  #  Unicorn
  ##

  if defined?(Unicorn)
    exclude_methods(profile, Unicorn::HttpServer, :process_client)
  end

  if defined?(Unicorn::OobGC)
    exclude_methods(profile, Unicorn::OobGC, :process_client)
  end

  ##
  #  New Relic
  ##

  if defined?(NewRelic::Agent)
    if defined?(NewRelic::Agent::Instrumentation::MiddlewareTracing)
      exclude_methods(profile, NewRelic::Agent::Instrumentation::MiddlewareTracing, [
        :call
      ])
    end

    if defined?(NewRelic::Agent::MethodTracerHelpers)
      exclude_methods(profile, NewRelic::Agent::MethodTracerHelpers, [
        :trace_execution_scoped,
        :log_errors,
      ])

      exclude_singleton_methods(profile, NewRelic::Agent::MethodTracerHelpers, [
        :trace_execution_scoped,
        :log_errors,
      ])
    end

    if defined?(NewRelic::Agent::MethodTracer)
      exclude_methods(profile, NewRelic::Agent::MethodTracer, [
        :trace_execution_scoped,
        :trace_execution_unscoped,
      ])
    end
  end

    ##
    #  Miscellaneous Methods
    ##

  if defined?(Mustache)
    exclude_methods(profile, Mustache::Context, [
      :fetch
    ])
  end
end
```

    
  

    
      
  
### 
  
    .**exclude_enumerable**(profile, mod, *method_or_methods)  ⇒ Object 
  

  

  

  
    
      

```

191
192
193
194
```

    
    
      

```
# File 'lib/ruby-prof/exclude_common_methods.rb', line 191

def self.exclude_enumerable(profile, mod, *method_or_methods)
  exclude_methods(profile, mod, [:each, *method_or_methods])
  exclude_methods(profile, mod, ENUMERABLE_NAMES)
end
```

    
  

    
      
  
### 
  
    .**exclude_methods**(profile, mod, *method_or_methods)  ⇒ Object 
  

  

  

  
    
      

```

196
197
198
```

    
    
      

```
# File 'lib/ruby-prof/exclude_common_methods.rb', line 196

def self.exclude_methods(profile, mod, *method_or_methods)
  profile.exclude_methods!(mod, method_or_methods)
end
```

    
  

    
      
  
### 
  
    .**exclude_singleton_methods**(profile, mod, *method_or_methods)  ⇒ Object 
  

  

  

  
    
      

```

200
201
202
```

    
    
      

```
# File 'lib/ruby-prof/exclude_common_methods.rb', line 200

def self.exclude_singleton_methods(profile, mod, *method_or_methods)
  profile.exclude_singleton_methods!(mod, method_or_methods)
end
```