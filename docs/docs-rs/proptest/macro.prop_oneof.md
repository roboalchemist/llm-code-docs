proptest
# Macro prop_oneof 
Source 

```
macro_rules! prop_oneof {
    ($($item:expr),+ $(,)?) => { ... };
    ($_weight0:expr => $item0:expr $(,)?) => { ... };
    ($weight0:expr => $item0:expr,
     $weight1:expr => $item1:expr $(,)?) => { ... };
    ($weight0:expr => $item0:expr,
     $weight1:expr => $item1:expr,
     $weight2:expr => $item2:expr $(,)?) => { ... };
    ($weight0:expr => $item0:expr,
     $weight1:expr => $item1:expr,
     $weight2:expr => $item2:expr,
     $weight3:expr => $item3:expr $(,)?) => { ... };
    ($weight0:expr => $item0:expr,
     $weight1:expr => $item1:expr,
     $weight2:expr => $item2:expr,
     $weight3:expr => $item3:expr,
     $weight4:expr => $item4:expr $(,)?) => { ... };
    ($weight0:expr => $item0:expr,
     $weight1:expr => $item1:expr,
     $weight2:expr => $item2:expr,
     $weight3:expr => $item3:expr,
     $weight4:expr => $item4:expr,
     $weight5:expr => $item5:expr $(,)?) => { ... };
    ($weight0:expr => $item0:expr,
     $weight1:expr => $item1:expr,
     $weight2:expr => $item2:expr,
     $weight3:expr => $item3:expr,
     $weight4:expr => $item4:expr,
     $weight5:expr => $item5:expr,
     $weight6:expr => $item6:expr $(,)?) => { ... };
    ($weight0:expr => $item0:expr,
     $weight1:expr => $item1:expr,
     $weight2:expr => $item2:expr,
     $weight3:expr => $item3:expr,
     $weight4:expr => $item4:expr,
     $weight5:expr => $item5:expr,
     $weight6:expr => $item6:expr,
     $weight7:expr => $item7:expr $(,)?) => { ... };
    ($weight0:expr => $item0:expr,
     $weight1:expr => $item1:expr,
     $weight2:expr => $item2:expr,
     $weight3:expr => $item3:expr,
     $weight4:expr => $item4:expr,
     $weight5:expr => $item5:expr,
     $weight6:expr => $item6:expr,
     $weight7:expr => $item7:expr,
     $weight8:expr => $item8:expr $(,)?) => { ... };
    ($weight0:expr => $item0:expr,
     $weight1:expr => $item1:expr,
     $weight2:expr => $item2:expr,
     $weight3:expr => $item3:expr,
     $weight4:expr => $item4:expr,
     $weight5:expr => $item5:expr,
     $weight6:expr => $item6:expr,
     $weight7:expr => $item7:expr,
     $weight8:expr => $item8:expr,
     $weight9:expr => $item9:expr $(,)?) => { ... };
    ($($weight:expr => $item:expr),+ $(,)?) => { ... };
}
```