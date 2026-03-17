# Class: Prawn::Outline
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Prawn::Outline
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/prawn/outline.rb
  
  

## Overview

  
    

The Outline class organizes the outline tree items for the document. Note that the #prev and #parent are adjusted while navigating through the nested blocks. These attributes along with the presence or absence of blocks are the primary means by which the relations for the various ‘PDF::Core::OutlineItem`s and the `PDF::Core::OutlineRoot` are set.

Some ideas for the organization of this class were gleaned from `name_tree`. In particular the way in which the ‘PDF::Core::OutlineItem`s are finally rendered into document objects through a hash.

  

  

  
## Stable API collapse

  

    
      
- 
  
    
      #**document**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    
  

    
      
- 
  
    
      #**items**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    
  

    
      
- 
  
    
      #**parent**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    
  

    
      
- 
  
    
      #**prev**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    
  

    
  

  
    
## 
      Stable API
      collapse
    

    

      
        
- 
  
    
      #**add_subsection_to**(title, position = :last) { ... } ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Inserts an outline section to the outline tree (see #define).

  

      
        
- 
  
    
      #**define** { ... } ⇒ void 
    

    
      (also: #update)
    
  
  
  
  
  
  
  
  

  
    

Defines/Updates an outline for the document.

  

      
        
- 
  
    
      #**initialize**(document)  ⇒ Outline 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Outline.

  

      
        
- 
  
    
      #**insert_section_after**(title) { ... } ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Inserts an outline section to the outline tree (see #define).

  

      
        
- 
  
    
      #**page**(options = {})  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Adds a page to the outline.

  

      
        
- 
  
    
      #**page_number**  ⇒ Integer 
    

    
  
  
  
  
  
  
  
  

  
    

Returns the current page number of the document.

  

      
        
- 
  
    
      #**section**(title, options = {}) { ... } ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Adds an outline section to the outline tree.

  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(document)  ⇒ Outline 
  

  

  

  
    

Returns a new instance of Outline.

  

  

Parameters:

  
    
- 
      
        document
      
      
        (Prawn::Document)
      
      
      
    
  

  
    
      

```

31
32
33
34
35
36
```

    
    
      

```
# File 'lib/prawn/outline.rb', line 31

def initialize(document)
  @document = document
  @parent = root
  @prev = nil
  @items = {}
end

```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**document**  ⇒ Object 
  

  

  

  
    
      

```

28
29
30
```

    
    
      

```
# File 'lib/prawn/outline.rb', line 28

def document
  @document
end

```

    
  

    
      
      
      
  
### 
  
    #**items**  ⇒ Object 
  

  

  

  
    
      

```

28
29
30
```

    
    
      

```
# File 'lib/prawn/outline.rb', line 28

def items
  @items
end

```

    
  

    
      
      
      
  
### 
  
    #**parent**  ⇒ Object 
  

  

  

  
    
      

```

28
29
30
```

    
    
      

```
# File 'lib/prawn/outline.rb', line 28

def parent
  @parent
end

```

    
  

    
      
      
      
  
### 
  
    #**prev**  ⇒ Object 
  

  

  

  
    
      

```

28
29
30
```

    
    
      

```
# File 'lib/prawn/outline.rb', line 28

def prev
  @prev
end

```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**add_subsection_to**(title, position = :last) { ... } ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Inserts an outline section to the outline tree (see #define).

Although you will probably choose to exclusively use #define so that your outline tree is contained and easy to manage, this method gives you the option to insert sections to the outline tree at any point during document generation. This method allows you to add a child subsection to any other item at any level in the outline tree. Currently the only way to locate the place of entry is with the title for the item. If your title names are not unique consider using #define.

Consider using this method instead of #update if you want to have the outline object to be scoped as self (see #insert_section_after example).

“‘ruby go_to_page 2 start_new_page text “Inserted Page” outline.add_subsection_to title: ’Page 2’, :first do

```
outline.page destination: page_number, title: "Inserted Page"

```

end “‘

  

  

Parameters:

  
    
- 
      
        title
      
      
        (String)
      
      
      
        —
        

An outline title to add the subsection to.

      
    
  
    
- 
      
        position
      
      
        (:first, :last)
      
      
        *(defaults to: :last)*
      
      
        —
        

(:last) Where the subsection will be placed relative to other child elements. If you need to position your subsection in between other elements then consider using #insert_section_after.

      
    
  

Yields:

  
    
- 
      
      
        
      
      
      
        
        

Uses the same DSL syntax as #define

      
    
  

  
    
      

```

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
```

    
    
      

```
# File 'lib/prawn/outline.rb', line 115

def add_subsection_to(title, position = :last, &block)
  @parent = items[title]
  unless @parent
    raise Prawn::Errors::UnknownOutlineTitle,
      "\n No outline item with title: '#{title}' exists in the outline tree"
  end
  @prev = position == :first ? nil : @parent.data.last
  nxt = position == :first ? @parent.data.first : nil
  insert_section(nxt, &block)
end

```

    
  

    
      
  
### 
  
    #**define** { ... } ⇒ void 
  

  
    Also known as:
    update
    
  

  

  
    

This method returns an undefined value.

Defines/Updates an outline for the document.

The outline is an optional nested index that appears on the side of a PDF document usually with direct links to pages. The outline DSL is defined by nested blocks involving two methods: #section and #page. Note that one can also use #update to add more sections to the end of the outline tree using the same syntax and scope.

The syntax is best illustrated with an example:

“‘ruby Prawn::Document.generate(’outlined_document.pdf’) do

```
text "Page 1. This is the first Chapter. "
start_new_page
text "Page 2. More in the first Chapter. "
start_new_page
outline.define do
  section 'Chapter 1', destination: 1, closed: true do
    page destination: 1, title: 'Page 1'
    page destination: 2, title: 'Page 2'
  end
end
start_new_page do
outline.update do
  section 'Chapter 2', destination: 2, do
    page destination: 3, title: 'Page 3'
  end
end

```

end “‘

  

  

Yields:

  
    
- 
      
      
        
      
      
      
    
  

  
    
      

```

80
81
82
```

    
    
      

```
# File 'lib/prawn/outline.rb', line 80

def define(&block)
  instance_eval(&block) if block
end

```

    
  

    
      
  
### 
  
    #**insert_section_after**(title) { ... } ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Inserts an outline section to the outline tree (see #define).

Although you will probably choose to exclusively use #define so that your outline tree is contained and easy to manage, this method gives you the option to insert sections to the outline tree at any point during document generation. Unlike #add_subsection_to, this method allows you to enter a section after any other item at any level in the outline tree. Currently the only way to locate the place of entry is with the title for the item. If your title names are not unique consider using #define.

  

  
  
    
#### Examples:

    
      
      

```
go_to_page 2
start_new_page
text "Inserted Page"
update_outline do
  insert_section_after :title => 'Page 2' do
    page :destination => page_number, :title => "Inserted Page"
  end
end

```

    
  

Parameters:

  
    
- 
      
        title
      
      
        (String)
      
      
      
        —
        

The title of other section or page to insert new section after.

      
    
  

Yields:

  
    
- 
      
      
        
      
      
      
        
        

Uses the same DSL syntax as #define.

      
    
  

  
    
      

```

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
```

    
    
      

```
# File 'lib/prawn/outline.rb', line 151

def insert_section_after(title, &block)
  @prev = items[title]
  unless @prev
    raise Prawn::Errors::UnknownOutlineTitle,
      "\n No outline item with title: '#{title}' exists in the outline tree"
  end
  @parent = @prev.data.parent
  nxt = @prev.data.next
  insert_section(nxt, &block)
end

```

    
  

    
      
  
### 
  
    #**page**(options = {})  ⇒ void 
  

  

  

  
    
  
    **Note:**
    

This method is almost identical to #section except that it does not accept a block thereby defining the outline item as a leaf on the outline tree structure.

  

This method returns an undefined value.

Adds a page to the outline.

Although you will probably choose to exclusively use #define so that your outline tree is contained and easy to manage, this method also gives you the option to add pages to the root of outline tree at any point during document generation. Note that the page will be added at the top level after the other root outline elements. For more flexible placement try using #insert_section_after and/or #add_subsection_to.

  

  
  
    
#### Examples:

    
      
      

```
outline.page title: "Very Last Page"

```

    
  

Parameters:

  
    
- 
      
        options
      
      
        (Hash{Symbol => any})
      
      
        *(defaults to: {})*
      
      
    
  

  
    
    
    

Options Hash (options):
    

      
        
- 
          :title
          (String)
          
            
          
          
            — 

REQUIRED. The outline text that appears for the page.

          
        
      
        
- 
          :destination
          (Integer, Array)
          
            
          
          
            — 

  - 

The page number for a destination link to the top of the page (using a `:FIT` destination).

  - 

An array with a custom destination (see the `#dest_*` methods of the `PDF::Core::Destination` module).

          
        
      
        
- 
          :closed
          (Boolean)
          
            
              — default:
              false
            
          
          
            — 

Whether the section should show its nested outline elements.

          
        
      
    

  

  
    
      

```

219
220
221
222
223
224
225
226
227
```

    
    
      

```
# File 'lib/prawn/outline.rb', line 219

def page(options = {})
  if options[:title]
    title = options[:title]
  else
    raise Prawn::Errors::RequiredOption,
      "\nTitle is a required option for page"
  end
  add_outline_item(title, options)
end

```

    
  

    
      
  
### 
  
    #**page_number**  ⇒ Integer 
  

  

  

  
    

Returns the current page number of the document.

  

  

Returns:

  
    
- 
      
      
        (Integer)
      
      
      
    
  

  
    
      

```

43
44
45
```

    
    
      

```
# File 'lib/prawn/outline.rb', line 43

def page_number
  @document.page_number
end

```

    
  

    
      
  
### 
  
    #**section**(title, options = {}) { ... } ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Adds an outline section to the outline tree.

Although you will probably choose to exclusively use #define so that your outline tree is contained and easy to manage, this method gives you the option to add sections to the outline tree at any point during document generation. When not being called from within another #section block the section will be added at the top level after the other root elements of the outline. For more flexible placement try using #insert_section_after and/or #add_subsection_to.

  

  
  
    
#### Examples:

    
      
      

```
outline.section 'Added Section', destination: 3 do
  outline.page destionation: 3, title: 'Page 3'
end

```

    
  

Parameters:

  
    
- 
      
        title
      
      
        (String)
      
      
      
        —
        

The outline text that appears for the section.

      
    
  
    
- 
      
        options
      
      
        (Hash{Symbol => any})
      
      
        *(defaults to: {})*
      
      
    
  

  
    
    
    
    
    

Options Hash (options):
    

      
        
- 
          :destination
          (Integer, Array)
          
            
          
          
            — 

  - 

Optional page number for a destination link to the top of the page (using a `:FIT` destination).

  - 

An array with a custom destination (see the `#dest_*` methods of the `PDF::Core::Destination` module).

          
        
      
        
- 
          :closed
          (Boolean)
          
            
              — default:
              false
            
          
          
            — 

Whether the section should show its nested outline elements.

          
        
      
    

  

Yields:

  
    
- 
      
      
        
      
      
      
        
        

More nested subsections and/or page blocks.

      
    
  

  
    
      

```

188
189
190
```

    
    
      

```
# File 'lib/prawn/outline.rb', line 188

def section(title, options = {}, &block)
  add_outline_item(title, options, &block)
end

```