iced::widget::selector
# Function find 
Source 

```
pub fn find<S>(selector: S) -> Task<Option<<S as Selector>::Output>>where
    S: Selector + Send + 'static,
    <S as Selector>::Output: Send + Clone + 'static,
```
Available on **crate feature `selector`** only.