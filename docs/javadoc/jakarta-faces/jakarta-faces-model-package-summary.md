# Package jakarta.faces.model

---

package jakarta.faces.model

-

Related Packages

Package
Description
jakarta.faces

-

Class
Description
ArrayDataModel<E>

 **ArrayDataModel** is a convenience implementation of `DataModel` that wraps an array of Java
 objects.

CollectionDataModel<E>

 **CollectionDataModel** is a convenience implementation of `DataModel` that wraps an
 `Collection` of Java objects.

DataModel<E>

 **DataModel** is an abstraction around arbitrary data binding
 technologies that can be used to adapt a variety of data sources for use by Jakarta Faces components that
 support per-row processing for their child components (such as `UIData`.

DataModelEvent

 **DataModelEvent** represents an event of interest to registered listeners that occurred on the
 specified `DataModel`.

DataModelListener

 **DataModelListener** represents an event listener that wishes to be notified of `DataModelEvent`s
 occurring on a particular `DataModel` instance.

FacesDataModel

FacesDataModel.Literal

 Supports inline instantiation of the `FacesDataModel` qualifier.

IterableDataModel<E>

 **IterableDataModel** is an implementation of `DataModel` that wraps an `Iterable`.

ListDataModel<E>

 **ListDataModel** is a convenience implementation of `DataModel` that wraps an `List`
 of Java objects.

ResultSetDataModel

 **ResultSetDataModel** is a convenience implementation of `DataModel` that wraps a
 `ResultSet` of Java objects.

ScalarDataModel<E>

 **ScalarDataModel** is a convenience implementation of `DataModel` that wraps an individual Java
 object.

SelectItem

 **SelectItem** represents a single *item*
 in the list of supported *items* associated with a `UISelectMany` or `UISelectOne` component.

SelectItemGroup

 **SelectItemGroup** is a subclass of `SelectItem` that identifies a set of options that will be
 made available as a subordinate "submenu" or "options list", depending upon the requirements of the
 `UISelectMany` or `UISelectOne` renderer that is actually used.
