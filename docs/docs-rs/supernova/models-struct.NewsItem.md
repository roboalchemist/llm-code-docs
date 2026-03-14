supernova::models
# Struct NewsItem 
Source 

```
pub struct NewsItem {
    pub id: NewsItemKey,
    pub title: String,
    pub summary: String,
    pub datetime: DateTime<Utc>,
    pub thumb: Option<String>,
    pub url: String,
    /* private fields */
}
```

## Fields§
§`id: NewsItemKey`§`title: String`§`summary: String`§`datetime: DateTime<Utc>`§`thumb: Option<String>`§`url: String`
## Implementations§