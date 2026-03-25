redshift::writer
# Struct ColumnDefinition 
Source 

```
pub struct ColumnDefinition<'a, T> {
    pub name: &'a str,
    pub extract_column: Box<dyn Fn(&T) -> String>,
}
```

## Fields§
§`name: &'a str`

Column name
§`extract_column: Box<dyn Fn(&T) -> String>`

Method to extract the column value from item `T`

## Auto Trait Implementations§
§
### impl<'a, T> Freeze for ColumnDefinition<'a, T>