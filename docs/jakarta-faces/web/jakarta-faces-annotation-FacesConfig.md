Package jakarta.faces.annotation

# Annotation Interface FacesConfig

---

@Qualifier
@Target(TYPE)
@Retention(RUNTIME)
public @interface FacesConfig

 The presence of this annotation on a class deployed within an application
 guarantees activation of Jakarta Faces and its CDI specific features, even when
 `/WEB-INF/faces-config.xml` is absent and `FacesServlet` is not explicitly registered.

-

## Nested Class Summary

Nested Classes

Modifier and Type
Class
Description
`static final class`
`FacesConfig.Literal`

 Supports inline instantiation of the `FacesConfig` qualifier.
