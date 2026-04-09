# Package jakarta.faces.annotation

---

package jakarta.faces.annotation

-

Related Packages

Package
Description
jakarta.faces

-

Class
Description
ApplicationMap

 The presence of this annotation (along with `@Inject`) on a field of type `Map<String,
 Object>` causes the map returned from `ExternalContext.getApplicationMap()` to be
 injected as the value of that field.

ApplicationMap.Literal

 Supports inline instantiation of the `ApplicationMap` qualifier.

FacesConfig

 The presence of this annotation on a class deployed within an application
 guarantees activation of Jakarta Faces and its CDI specific features, even when
 `/WEB-INF/faces-config.xml` is absent and `FacesServlet` is not explicitly registered.

FacesConfig.Literal

 Supports inline instantiation of the `FacesConfig` qualifier.

FlowMap

 The presence of this annotation (along with `@Inject`) on a field of type `Map<Object,
 Object>` causes the map returned from `FlowHandler.getCurrentFlowScope()` to be
 injected as the value of that field.

FlowMap.Literal

 Supports inline instantiation of the `ApplicationMap` qualifier.

HeaderMap

 The presence of this annotation (along with `@Inject`) on a field of type `Map<String,
 String>` causes the map returned from `ExternalContext.getRequestHeaderMap()` to
 be injected as the value of that field.

HeaderMap.Literal

 Supports inline instantiation of the `HeaderMap` qualifier.

HeaderValuesMap

 The presence of this annotation (along with `@Inject`) on a field of type `Map<String,
 String[]>` causes the map returned from
 `ExternalContext.getRequestHeaderValuesMap()` to be injected as the value of that field.

HeaderValuesMap.Literal

 Supports inline instantiation of the `HeaderValuesMap` qualifier.

InitParameterMap

 The presence of this annotation (along with `@Inject`) on a field of type `Map<String,
 String>` causes the map returned from `ExternalContext.getInitParameterMap()` to
 be injected as the value of that field.

InitParameterMap.Literal

 Supports inline instantiation of the `InitParameterMap` qualifier.

ManagedProperty

 The presence of this annotation (along with `@Inject`) on a field of any type causes the value returned from
 evaluating an expression language expression to be injected as the value of that field.

ManagedProperty.Literal

 Supports inline instantiation of the `ManagedProperty` qualifier.

RequestCookieMap

 The presence of this annotation (along with `@Inject`) on a field of type `Map<String,
 Object>` causes the map returned from `ExternalContext.getRequestCookieMap()` to
 be injected as the value of that field.

RequestCookieMap.Literal

 Supports inline instantiation of the `RequestCookieMap` qualifier.

RequestMap

 The presence of this annotation (along with `@Inject`) on a field of type `Map<String,
 Object>` causes the map returned from `ExternalContext.getRequestMap()` to be
 injected as the value of that field.

RequestMap.Literal

 Supports inline instantiation of the `RequestMap` qualifier.

RequestParameterMap

 The presence of this annotation (along with `@Inject`) on a field of type `Map<String,
 String>` causes the map returned from `ExternalContext.getRequestParameterMap()`
 to be injected as the value of that field.

RequestParameterMap.Literal

 Supports inline instantiation of the `RequestParameterMap` qualifier.

RequestParameterValuesMap

 The presence of this annotation (along with `@Inject`) on a field of type `Map<String,
 String []>` causes the map returned from
 `ExternalContext.getRequestParameterValuesMap()` to be injected as the value of that field.

RequestParameterValuesMap.Literal

 Supports inline instantiation of the `RequestParameterValuesMap` qualifier.

SessionMap

 The presence of this annotation (along with `@Inject`) on a field of type `Map<String,
 Object>` causes the map returned from `ExternalContext.getSessionMap()` to be
 injected as the value of that field.

SessionMap.Literal

 Supports inline instantiation of the `SessionMap` qualifier.

View

 The presence of this annotation on a target (type, method, parameter or field) within an application is used to indicate that
 this target is somehow handling a Faces View Id or Ids.

View.Literal

Supports inline instantiation of the `View` annotation.

ViewMap

 The presence of this annotation (along with `@Inject`) on a field of type `Map<String,
 Object>` causes the map returned from `UIViewRoot.getViewMap()` to be injected
 as the value of that field.

ViewMap.Literal

 Supports inline instantiation of the `ViewMap` qualifier.
