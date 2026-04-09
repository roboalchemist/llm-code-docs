Module org.glassfish.tyrus.core
Package org.glassfish.tyrus.core

# Annotation Interface Beta

---

@Retention(CLASS)
@Documented
@Target({ANNOTATION_TYPE,TYPE,CONSTRUCTOR,METHOD,FIELD,PACKAGE})
public @interface Beta
Marker of a public Tyrus API that is still in "beta" non-final version.

 This annotation signals that the annotated public Tyrus API (package, class, method or field)
 has not been fully stabilized yet. As such, the API is subject to backward-incompatible changes
 (or even removal) in a future Tyrus release. Tyrus development team does not make any guarantees
 to retain backward compatibility of a `@Beta`-annotated Tyrus API.

 This annotation does not indicate inferior quality or performance of the API, just informs that the
 API may still evolve in the future in a backward-incompatible ways. Tyrus users may use beta APIs
 in their applications keeping in mind potential cost of extra work associated with an upgrade
 to a newer Tyrus version.

 Once a `@Beta`-annotated Tyrus API reaches the desired maturity, the `@Beta` annotation
 will be removed from such API and the API will become part of a stable public Tyrus API.

Author:
Marek Potociar
