inquire::formatter
# Type Alias DateFormatter 
Source 

```
pub type DateFormatter<'a> = &'a dyn Fn(NaiveDate) -> String;
```
Available on **crate feature `date`** only.