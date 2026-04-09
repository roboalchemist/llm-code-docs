mozjpeg
# Trait CompInfoExt 
Source 

```
pub trait CompInfoExt {
    // Required methods
    fn row_stride(&self) -> usize;
    fn col_stride(&self) -> usize;
    fn sampling(&self) -> (u8, u8);
    fn qtable(&self) -> Option<QTable>;
    fn width_in_blocks(&self) -> usize;
    fn height_in_blocks(&self) -> usize;
}
```

## Required Methods§