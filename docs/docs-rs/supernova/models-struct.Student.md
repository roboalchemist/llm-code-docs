supernova::models
# Struct Student 
Source 

```
pub struct Student {
    pub id: StudentKey,
    pub name: String,
    pub abbreviation: Option<String>,
    pub number: u32,
    pub first_year: Option<u32>,
    pub last_year: Option<u32>,
    pub avg_grade: Option<u32>,
    pub url: String,
    /* private fields */
}
```

## Fields§
§`id: StudentKey`§`name: String`§`abbreviation: Option<String>`§`number: u32`§`first_year: Option<u32>`§`last_year: Option<u32>`§`avg_grade: Option<u32>`§`url: String`
## Implementations§