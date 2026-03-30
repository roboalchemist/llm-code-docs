druid::lens

# Trait LensExt

Source

```
pub trait LensExt<A: ?Sized, B: ?Sized>: Lens<A, B> {
    // Provided methods
    fn get(&self, data: &A) -> B
       where B: Clone { ... }
    fn put(&self, data: &mut A, value: B)
       where B: Sized { ... }
    fn then<Other, C>(self, other: Other) -> Then<Self, Other, B>
       where Other: Lens<B, C> + Sized,
             C: ?Sized,
             Self: Sized { ... }
    fn map<Get, Put, C>(
        self,
        get: Get,
        put: Put,
    ) -> Then<Self, Map<Get, Put>, B>
       where Get: Fn(&B) -> C,
             Put: Fn(&mut B, C),
             Self: Sized { ... }
    fn deref(self) -> Then<Self, Deref, B>
       where B: Deref + DerefMut,
             Self: Sized { ... }
    fn as_ref<T: ?Sized>(self) -> Then<Self, Ref, B>
       where B: AsRef<T> + AsMut<T>,
             Self: Sized { ... }
    fn index<I>(self, index: I) -> Then<Self, Index<I>, B>
       where I: Clone,
             B: Index<I> + IndexMut<I>,
             Self: Sized { ... }
    fn in_arc(self) -> InArc<Self>
       where A: Clone,
             B: Data,
             Self: Sized { ... }
    fn not(self) -> Then<Self, Not, B>
       where Self: Sized,
             B: Sized + Into<bool> + Copy,
             bool: Into<B> { ... }
}
```

## Provided Methods§
