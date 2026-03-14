# Module: Formtastic::Inputs::Base::Timeish
  
  
  

  

  
  
  
  
  

  
  
    Included in:
    DateSelectInput, DatetimeSelectInput, TimeSelectInput
  
  

  
  
    Defined in:
    lib/formtastic/inputs/base/timeish.rb
  
  

## Overview

  
    
  
    **TODO:**
    

Document i18n

  

  
    **TODO:**
    

Check what other Rails options are supported (`start_year`, `end_year`, `use_month_numbers`, `use_short_month`, `add_month_numbers`, `prompt`), write tests for them, and otherwise support them

  

  
    **TODO:**
    

Could we take the rendering from Rails' helpers and inject better HTML in and around it rather than re-inventing the whee?

  

Timeish inputs (`:date_select`, `:datetime_select`, `:time_select`) are similar to the Rails date and time 
helpers (`date_select`, `datetime_select`, `time_select`), rendering a series of `<select>`
tags for each fragment (year, month, day, hour, minute, seconds). The fragments are then 
re-combined to a date by ActiveRecord through multi-parameter assignment.

The mark-up produced by Rails is simple but far from ideal, with no way to label the 
individual fragments for accessibility, no fieldset to group the related fields, and no
legend describing the group. Formtastic addresses this within the standard `<li>` wrapper 
with a `<fieldset>` with a `<legend>` as a label, followed by an ordered list (`<ol>`) of 
list items (`<li>`), one for each fragment (year, month, ...). Each `<li>` fragment contains
a `<label>` (eg "Year") for the fragment, and a `<select>` containing `<option>`s (eg a 
range of years).

In the supplied formtastic.css file, the resulting mark-up is styled to appear a lot like a
standard Rails date time select by:

- styling the legend to look like the other labels (to the left hand side of the selects)

- floating the `<li>` fragments against each other as a single line

- hiding the `<label>` of each fragment with `display:none`

  

  
  
    
#### Examples:

    
      
        
##### 

`:date_select` input with full form context and sample HTMl output

      
      

```

<%= semantic_form_for(@post) do |f| %>
  <%= f.inputs do %>
    ...
    <%= f.input :publish_at, :as => :date_select %>
  <% end %>
<% end %>

<form...>
  <fieldset class="inputs">
    <ol>
      <li class="date">
        <fieldset class="fragments">
          <ol class="fragments-group">
            <li class="fragment">
              <label for="post_publish_at_1i">Year</label>
              <select id="post_publish_at_1i" name="post[publish_at_1i]">...</select>
            </li>
            <li class="fragment">
              <label for="post_publish_at_2i">Month</label>
              <select id="post_publish_at_2i" name="post[publish_at_2i]">...</select>
            </li>
            <li class="fragment">
              <label for="post_publish_at_3i">Day</label>
              <select id="post_publish_at_3i" name="post[publish_at_3i]">...</select>
            </li>
          </ol>
        </fieldset>
      </li>
    </ol>
  </fieldset>
</form>
```

    
      
        
##### 

`:time_select` input

      
      

```
<%= f.input :publish_at, :as => :time_select %>
```

    
      
        
##### 

`:datetime_select` input

      
      

```
<%= f.input :publish_at, :as => :datetime_select %>
```

    
      
        
##### 

Change the labels for each fragment

      
      

```
<%= f.input :publish_at, :as => :date_select, :labels => { :year => "Y", :month => "M", :day => "D" }  %>
```

    
      
        
##### 

Suppress the labels for all fragments

      
      

```
<%= f.input :publish_at, :as => :date_select, :labels => false  %>
```

    
      
        
##### 

Skip a fragment (defaults to 1, skips all following fragments)

      
      

```
<%= f.input :publish_at, :as => :datetime_select, :discard_minute => true  %>
<%= f.input :publish_at, :as => :datetime_select, :discard_hour => true  %>
<%= f.input :publish_at, :as => :datetime_select, :discard_day => true  %>
<%= f.input :publish_at, :as => :datetime_select, :discard_month => true  %>
<%= f.input :publish_at, :as => :datetime_select, :discard_year => true  %>
```

    
      
        
##### 

Change the order

      
      

```
<%= f.input :publish_at, :as => :date_select, :order => [:month, :day, :year]  %>
```

    
      
        
##### 

Include seconds with times (excluded by default)

      
      

```
<%= f.input :publish_at, :as => :time_select, :include_seconds => true %>
```

    
      
        
##### 

Specify if there should be a blank option at the start of each select or not. Note that, unlike select inputs, :include_blank does not accept a string value.

      
      

```
<%= f.input :publish_at, :as => :time_select, :include_blank => true %>
<%= f.input :publish_at, :as => :time_select, :include_blank => false %>
```

    
      
        
##### 

Provide a value for the field via selected

      
      

```
<%= f.input :publish_at, :as => :datetime_select, :selected => DateTime.new(2018, 10, 4, 12, 00)
```

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**date_fragments**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**default_date_fragments**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**fragment_id**(fragment)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**fragment_input_html**(fragment)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**fragment_label**(fragment)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**fragment_label_html**(fragment)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**fragment_name**(fragment)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**fragment_prefix**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**fragment_wrapping**(&block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**fragment_wrapping_html_options**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**fragments**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**fragments_inner_wrapping**(&block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**fragments_label**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**fragments_wrapping**(&block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**fragments_wrapping_html_options**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**hidden_field_name**(fragment)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**hidden_fragments**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**i18n_date_fragments**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**include_blank?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

TODO extract to BlankOptions or similar -- Select uses similar code.

  

      
        
- 
  
    
      #**position**(fragment)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**positions**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**time_fragments**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**to_html**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**value**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**date_fragments**  ⇒ Object 
  

  

  

  
    
      

```

123
124
125
```

    
    
      

```
# File 'lib/formtastic/inputs/base/timeish.rb', line 123

def date_fragments
  options[:order] || i18n_date_fragments || default_date_fragments
end
```

    
  

    
      
  
### 
  
    #**default_date_fragments**  ⇒ Object 
  

  

  

  
    
      

```

127
128
129
```

    
    
      

```
# File 'lib/formtastic/inputs/base/timeish.rb', line 127

def default_date_fragments
  [:year, :month, :day]
end
```

    
  

    
      
  
### 
  
    #**fragment_id**(fragment)  ⇒ Object 
  

  

  

  
    
      

```

150
151
152
```

    
    
      

```
# File 'lib/formtastic/inputs/base/timeish.rb', line 150

def fragment_id(fragment)
  "#{input_html_options[:id]}_#{position(fragment)}i"
end
```

    
  

    
      
  
### 
  
    #**fragment_input_html**(fragment)  ⇒ Object 
  

  

  

  
    
      

```

168
169
170
171
```

    
    
      

```
# File 'lib/formtastic/inputs/base/timeish.rb', line 168

def fragment_input_html(fragment)
  opts = input_options.merge(:prefix => fragment_prefix, :field_name => fragment_name(fragment), :default => value, :include_blank => include_blank?)
  template.send(:"select_#{fragment}", value, opts, input_html_options.merge(:id => fragment_id(fragment)))
end
```

    
  

    
      
  
### 
  
    #**fragment_label**(fragment)  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/formtastic/inputs/base/timeish.rb', line 139

def fragment_label(fragment)
  labels_from_options = options.key?(:labels) ? options[:labels] : {}
  if !labels_from_options
    ''
  elsif labels_from_options.key?(fragment)
    labels_from_options[fragment]
  else
    ::I18n.t(fragment.to_s, :default => fragment.to_s.humanize, :scope => [:datetime, :prompts])
  end
end
```

    
  

    
      
  
### 
  
    #**fragment_label_html**(fragment)  ⇒ Object 
  

  

  

  
    
      

```

158
159
160
161
```

    
    
      

```
# File 'lib/formtastic/inputs/base/timeish.rb', line 158

def fragment_label_html(fragment)
  text = fragment_label(fragment)
  text.blank? ? +"".html_safe : template.content_tag(:label, text, :for => fragment_id(fragment))
end
```

    
  

    
      
  
### 
  
    #**fragment_name**(fragment)  ⇒ Object 
  

  

  

  
    
      

```

154
155
156
```

    
    
      

```
# File 'lib/formtastic/inputs/base/timeish.rb', line 154

def fragment_name(fragment)
  "#{method}(#{position(fragment)}i)"
end
```

    
  

    
      
  
### 
  
    #**fragment_prefix**  ⇒ Object 
  

  

  

  
    
      

```

173
174
175
176
177
178
179
```

    
    
      

```
# File 'lib/formtastic/inputs/base/timeish.rb', line 173

def fragment_prefix
  if builder.options.key?(:index)
    object_name + "[#{builder.options[:index]}]"
  else
    object_name
  end
end
```

    
  

    
      
  
### 
  
    #**fragment_wrapping**(&block)  ⇒ Object 
  

  

  

  
    
      

```

131
132
133
```

    
    
      

```
# File 'lib/formtastic/inputs/base/timeish.rb', line 131

def fragment_wrapping(&block)
  template.content_tag(:li, template.capture(&block), fragment_wrapping_html_options)
end
```

    
  

    
      
  
### 
  
    #**fragment_wrapping_html_options**  ⇒ Object 
  

  

  

  
    
      

```

135
136
137
```

    
    
      

```
# File 'lib/formtastic/inputs/base/timeish.rb', line 135

def fragment_wrapping_html_options
  { :class => 'fragment' }
end
```

    
  

    
      
  
### 
  
    #**fragments**  ⇒ Object 
  

  

  

  
    
      

```

115
116
117
```

    
    
      

```
# File 'lib/formtastic/inputs/base/timeish.rb', line 115

def fragments
  date_fragments + time_fragments
end
```

    
  

    
      
  
### 
  
    #**fragments_inner_wrapping**(&block)  ⇒ Object 
  

  

  

  
    
      

```

225
226
227
228
229
```

    
    
      

```
# File 'lib/formtastic/inputs/base/timeish.rb', line 225

def fragments_inner_wrapping(&block)
  template.content_tag(:ol,
    template.capture(&block)
  )
end
```

    
  

    
      
  
### 
  
    #**fragments_label**  ⇒ Object 
  

  

  

  
    
      

```

214
215
216
217
218
219
220
221
222
223
```

    
    
      

```
# File 'lib/formtastic/inputs/base/timeish.rb', line 214

def fragments_label
  if render_label?
    template.content_tag(:legend, 
      builder.label(method, label_text, :for => fragment_id(fragments.first)), 
      :class => "label"
    )
  else
    +"".html_safe
  end
end
```

    
  

    
      
  
### 
  
    #**fragments_wrapping**(&block)  ⇒ Object 
  

  

  

  
    
      

```

203
204
205
206
207
208
```

    
    
      

```
# File 'lib/formtastic/inputs/base/timeish.rb', line 203

def fragments_wrapping(&block)
  template.content_tag(:fieldset,
    template.capture(&block).html_safe, 
    fragments_wrapping_html_options
  )
end
```

    
  

    
      
  
### 
  
    #**fragments_wrapping_html_options**  ⇒ Object 
  

  

  

  
    
      

```

210
211
212
```

    
    
      

```
# File 'lib/formtastic/inputs/base/timeish.rb', line 210

def fragments_wrapping_html_options
  { :class => "fragments" }
end
```

    
  

    
      
  
### 
  
    #**hidden_field_name**(fragment)  ⇒ Object 
  

  

  

  
    
      

```

235
236
237
238
239
240
241
```

    
    
      

```
# File 'lib/formtastic/inputs/base/timeish.rb', line 235

def hidden_field_name(fragment)
  if builder.options.key?(:index)
    "#{object_name}[#{builder.options[:index]}][#{fragment_name(fragment)}]"
  else
    "#{object_name}[#{fragment_name(fragment)}]"
  end
end
```

    
  

    
      
  
### 
  
    #**hidden_fragments**  ⇒ Object 
  

  

  

  
    
      

```

231
232
233
```

    
    
      

```
# File 'lib/formtastic/inputs/base/timeish.rb', line 231

def hidden_fragments
  +"".html_safe
end
```

    
  

    
      
  
### 
  
    #**i18n_date_fragments**  ⇒ Object 
  

  

  

  
    
      

```

194
195
196
197
198
199
200
201
```

    
    
      

```
# File 'lib/formtastic/inputs/base/timeish.rb', line 194

def i18n_date_fragments
  order = ::I18n.t(:order, :scope => [:date])
  if order.is_a?(Array)
    order.map &:to_sym
  else
    nil
  end
end
```

    
  

    
      
  
### 
  
    #**include_blank?**  ⇒ Boolean 
  

  

  

  
    

TODO extract to BlankOptions or similar -- Select uses similar code

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

182
183
184
```

    
    
      

```
# File 'lib/formtastic/inputs/base/timeish.rb', line 182

def include_blank?
  options.key?(:include_blank) ? options[:include_blank] : builder.include_blank_for_select_by_default
end
```

    
  

    
      
  
### 
  
    #**position**(fragment)  ⇒ Object 
  

  

  

  
    
      

```

190
191
192
```

    
    
      

```
# File 'lib/formtastic/inputs/base/timeish.rb', line 190

def position(fragment)
  positions[fragment]
end
```

    
  

    
      
  
### 
  
    #**positions**  ⇒ Object 
  

  

  

  
    
      

```

186
187
188
```

    
    
      

```
# File 'lib/formtastic/inputs/base/timeish.rb', line 186

def positions
  { :year => 1, :month => 2, :day => 3, :hour => 4, :minute => 5, :second => 6 }
end
```

    
  

    
      
  
### 
  
    #**time_fragments**  ⇒ Object 
  

  

  

  
    
      

```

119
120
121
```

    
    
      

```
# File 'lib/formtastic/inputs/base/timeish.rb', line 119

def time_fragments
  options[:include_seconds] ? [:hour, :minute, :second] : [:hour, :minute]
end
```

    
  

    
      
  
### 
  
    #**to_html**  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/formtastic/inputs/base/timeish.rb', line 97

def to_html
  input_wrapping do
    fragments_wrapping do
      hidden_fragments <<
      fragments_label <<
      template.content_tag(:ol,
        fragments.map do |fragment|
          fragment_wrapping do
            fragment_label_html(fragment) <<
            fragment_input_html(fragment)
          end
        end.join.html_safe, # TODO is this safe?
        { :class => 'fragments-group' } # TODO refactor to fragments_group_wrapping
      )
    end
  end
end
```

    
  

    
      
  
### 
  
    #**value**  ⇒ Object 
  

  

  

  
    
      

```

163
164
165
166
```

    
    
      

```
# File 'lib/formtastic/inputs/base/timeish.rb', line 163

def value
  return input_options[:selected] if options.key?(:selected)
  object.send(method) if object && object.respond_to?(method)
end
```