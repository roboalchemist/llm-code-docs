# Package jakarta.faces.view.facelets

---

package jakarta.faces.view.facelets

-

Related Packages

Package
Description
jakarta.faces.view

-

Class
Description
AttributeHandler

 An interface that allows other code to identify FaceletHandlers that correspond to component attributes.

BehaviorConfig

 Convey the id of a behavior declared in a view.

BehaviorHandler

 The `FaceletHandler` that corresponds to attached objects that represent an instance of
 `ClientBehavior` that must be added to the parent component, which must
 implement `ClientBehaviorHolder`, with a call to
 `ClientBehaviorHolder.addClientBehavior(java.lang.String, jakarta.faces.component.behavior.ClientBehavior)`.

ComponentConfig

 Passed to the constructor of `ComponentHandler`.

ComponentHandler

 Public base class for markup element instances that map to
 `UIComponent` instances in the view.

CompositeFaceletHandler

 A FaceletHandler that is derived of 1 or more, inner FaceletHandlers.

ConverterConfig

 A Facelet version of the Jakarta Server Pages `ConverterTag`.

ConverterHandler

 Handles setting a `Converter` instance on a `ValueHolder`
 parent.

DelegatingMetaTagHandler

 Enable the Jakarta Faces implementation to provide the
 appropriate behavior for the kind of `MetaTagHandler` subclass for each kind of element in the view, while
 providing a base-class from which those wanting to make a Java language custom tag handler can inherit.

Facelet

 The parent or root object in a FaceletHandler composition.

FaceletCache<V>

 This API defines the facility by which the Facelets
 `ViewDeclarationLanguage` creates and caches instances of Facelets.

FaceletCache.MemberFactory<V>

 Factory interface for creating Facelet or View Metadata Facelet instances.

FaceletCacheFactory

 Allows customization of the implementation of `FaceletCache`.

FaceletContext

 Context representative of a single request from a Facelet.

FaceletException

 An Exception from the Facelet implementation

FaceletHandler

 This is the root class for markup elements in Facelets VDL.

FaceletsAttachedObjectHandler

 Root class for all tag handlers that represent attached objetcts in a Facelets page.

FacetHandler

 An interface that allows other code to identify FaceletHandlers that correspond to component facets.

Metadata

 There are concrete subclasses within the implementation that map concepts in the Facelet VDL page to Jakarta Server
 Faces Java API calls the appropriate instances.

MetadataTarget

 Information used with `MetaRule` for determining how and what `Metadata` should be wired.

MetaRule

 The root class of the abstraction that dictates how attributes on a markup element in a Facelets VDL page are wired
 to the Jakarta Faces API object instance associated with that element.

MetaRuleset

 A mutable set of rules to be used in auto-wiring state to a particular object instance.

MetaTagHandler

 Every kind of markup element in Facelets VDL that has attributes that need to take action on a Jakarta Faces
 Java API artifact is associated with an instance of this class.

Tag

 The runtime must create an instance of this class for each element in the Facelets XHTML view.

TagAttribute

 Representation of an XML attribute name=value pair on an XML element in a
 Facelet file.

TagAttributeException

 An Exception caused by a `TagAttribute`

TagAttributes

 A set of TagAttributes, usually representing all attributes on a Tag.

TagConfig

 Passed to the constructor of `TagHandler` subclass, it defines the document definition of the handler we are
 instantiating.

TagDecorator

 Provides the ability to completely change the Tag
 before it's processed for compiling with the associated `TagHandler`.

TagException

 An Exception caused by a `Tag`

TagHandler

 Foundation class for `FaceletHandler`s associated with a
 markup element in a Facelet document.

TagHandlerDelegate

 Abstract class that defines methods relating to helping tag handler
 instances.

TagHandlerDelegateFactory

 Abstract factory for creating instances of
 `TagHandlerDelegate`.

TextHandler

 An interface that allows other code to identify FaceletHandlers that may provide text (String) content.

ValidatorConfig

 Used in creating `ValidatorHandler` and all implementations.

ValidatorHandler

 Handles setting a `Validator` instance on an
 `EditableValueHolder` parent.
