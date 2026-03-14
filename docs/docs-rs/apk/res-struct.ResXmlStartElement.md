apk::res

# Struct ResXmlStartElement

Source

```
pub struct ResXmlStartElement {
    pub namespace: i32,
    pub name: i32,
    pub attribute_start: u16,
    pub attribute_size: u16,
    pub attribute_count: u16,
    pub id_index: u16,
    pub class_index: u16,
    pub style_index: u16,
}
```

## Fields§

§`namespace: i32`

String of the full namespace of this element.
§`name: i32`

String name of this node if it is an ELEMENT; the raw
character data if this is a CDATA node.
§`attribute_start: u16`

Byte offset from the start of this structure to where
the attributes start.
§`attribute_size: u16`

Size of the attribute structures that follow.
§`attribute_count: u16`

Number of attributes associated with an ELEMENT. These are
available as an array of ResXmlAttribute structures
immediately following this node.
§`id_index: u16`

Index (1-based) of the “id” attribute. 0 if none.
§`class_index: u16`

Index (1-based) of the “class” attribute. 0 if none.
§`style_index: u16`

Index (1-based) of the “style” attribute. 0 if none.

## Implementations§
