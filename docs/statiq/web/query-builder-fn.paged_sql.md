statiq::query::builder
# Function paged_sql 
Source 

```
pub fn paged_sql(
    select_sql: &str,
    pk_col: &str,
    page: i64,
    page_size: i64,
) -> String
```