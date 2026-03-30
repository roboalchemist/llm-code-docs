Module org.easymock
Package org.easymock

## Annotation Type TestSubject

- 

---

```
@Target(FIELD)
@Retention(RUNTIME)
@Documented
public @interface TestSubject
```

Annotation to set on a field so that `EasyMockRunner`, `EasyMockRule` or `EasyMockSupport.injectMocks(Object)`
 will inject mocks created with `Mock` on its fields.
 

 See `EasyMockSupport.injectMocks(Object)` for the injection rules.

Since:
3.2
Author:
Henri Tremblay