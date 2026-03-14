Package com.beust.jcommander

## Annotation Type ParametersDelegate







- 

---


```
@Retention(RUNTIME)
@Target(FIELD)
public @interface ParametersDelegate
```


When applied to a field all of its child fields annotated
 with `Parameter` will be included during arguments
 parsing.

 

Mainly useful when creating complex command based CLI interfaces,
 where several commands can share a set of arguments, but using
 object inheritance is not enough, due to no-multiple-inheritance
 restriction. Using `ParametersDelegate` any number of
 command sets can be shared by using composition pattern.

 

Delegations can be chained (nested).