# Package jakarta.faces.view

---

package jakarta.faces.view

-

Related Packages

Package
Description
jakarta.faces

jakarta.faces.view.facelets

-

Class
Description
ActionSource2AttachedObjectHandler
Deprecated, for removal: This API element is subject to removal in a future version.
Use `ActionSourceAttachedObjectHandler` instead.

ActionSource2AttachedObjectTarget
Deprecated, for removal: This API element is subject to removal in a future version.
Use `ActionSourceAttachedObjectTarget` instead.

ActionSourceAttachedObjectHandler

 A VDL handler that exposes `ActionListener` to a *page author*.

ActionSourceAttachedObjectTarget

 A marker interface for VDL tags that represent `<composite:actionSource/>` for use by the
 *composite component page author*.

AttachedObjectHandler

 The abstract base interface for a handler representing an *attached object* in a VDL page.

AttachedObjectTarget

 Within the declaration of a *composite component*, an `AttachedObjectTarget` allows the
 *composite component author* to expose the semantics of an inner component to the *page author* without
 exposing the rendering or implementation details of the *inner component*.

BehaviorHolderAttachedObjectHandler

 Represent an attached object that is a `BehaviorHolder` in a VDL page.

BehaviorHolderAttachedObjectTarget

 Represent a `BehaviorHolder` attached object target in a VDL page.

EditableValueHolderAttachedObjectHandler

 A VDL handler that exposes `Validator` or
 `ValueChangeListener` to a *page author*.

EditableValueHolderAttachedObjectTarget

 A marker interface for VDL tags that represent `<composite:editableValueHolder/>` for use by the
 *composite component page author*.

Location

 An object that represents the Location of a tag or attribute of a tag in a View Declaration Language file.

StateManagementStrategy

 Encapsulate the saving and restoring of the view to enable the VDL to take
 over the responsibility for handling this feature.

ValueHolderAttachedObjectHandler

 A VDL handler that exposes `Converter` to a *page author*.

ValueHolderAttachedObjectTarget

 A marker interface for VDL tags that represent `<composite:valueHolder/>` for use by the
 *composite component page author*.

ViewDeclarationLanguage

 The contract that a view
 declaration language must implement to interact with the Jakarta Faces runtime.

ViewDeclarationLanguageFactory

 **ViewDeclarationLanguageFactory** is a factory object
 that creates (if needed) and returns a new `ViewDeclarationLanguage` instance based on the VDL found in a
 specific view.

ViewDeclarationLanguageWrapper

 Provides a simple implementation of `ViewDeclarationLanguage` that
 can be subclassed by developers wishing to provide specialized behavior to an existing
 `ViewDeclarationLanguage` instance.

ViewMetadata

 `ViewMetadata` is reponsible for extracting and providing view parameter metadata from VDL views.

ViewScoped

 When this annotation, along with `
jakarta.inject.Named` is found on a class, the runtime must place the bean in a CDI scope such that it remains active
 as long as `NavigationHandler.handleNavigation(jakarta.faces.context.FacesContext, java.lang.String, java.lang.String)` does not cause a navigation to a view
 with a viewId that is different than the viewId of the current view.
