adjust::database::util
# Function get_identifier_filter 
Source 

```
pub fn get_identifier_filter<T, U>(
    id_column: T,
    username_column: U,
    identifier: String,
) -> Or<Eq<T, i32>, Eq<U, String>>where
    T: Expression<SqlType = Integer> + Copy,
    U: Expression<SqlType = Text> + Copy,
```