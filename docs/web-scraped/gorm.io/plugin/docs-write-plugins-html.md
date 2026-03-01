# Source: https://gorm.io/docs/write_plugins.html

Title: Write Plugins

URL Source: https://gorm.io/docs/write_plugins.html

Published Time: 2026-01-31T07:58:03.919Z

Markdown Content:
[](https://github.com/go-gorm/gorm.io/edit/master/pages/docs/write_plugins.md "Improve this page")

[](https://gorm.io/docs/write_plugins.html#Callbacks "Callbacks")Callbacks
--------------------------------------------------------------------------

GORM leverages `Callbacks` to power its core functionalities. These callbacks provide hooks for various database operations like `Create`, `Query`, `Update`, `Delete`, `Row`, and `Raw`, allowing for extensive customization of GORM’s behavior.

Callbacks are registered at the global `*gorm.DB` level, not on a session basis. This means if you need different callback behaviors, you should initialize a separate `*gorm.DB` instance.

### [](https://gorm.io/docs/write_plugins.html#Registering-a-Callback "Registering a Callback")Registering a Callback

You can register a callback for specific operations. For example, to add a custom image cropping functionality:

func cropImage(db *gorm.DB) {

 if db.Statement.Schema != nil {

 

 for _, field := range db.Statement.Schema.Fields {

 switch db.Statement.ReflectValue.Kind() {

 case reflect.Slice, reflect.Array:

 for i := 0; i < db.Statement.ReflectValue.Len(); i++ {

 

 if fieldValue, isZero := field.ValueOf(db.Statement.Context, db.Statement.ReflectValue.Index(i)); !isZero {

 if crop, ok := fieldValue.(CropInterface); ok {

 crop.Crop()

 }

 }

 }

 case reflect.Struct:

 

 if fieldValue, isZero := field.ValueOf(db.Statement.Context, db.Statement.ReflectValue); !isZero {

 if crop, ok := fieldValue.(CropInterface); ok {

 crop.Crop()

 }

 }

 

 err := field.Set(db.Statement.Context, db.Statement.ReflectValue, "newValue")

 }

 }

 

 db.Statement.Schema.Fields

 

 db.Statement.Schema.PrimaryFields

 

 db.Statement.Schema.PrioritizedPrimaryField

 

 db.Statement.Schema.Relationships

 

 field := db.Statement.Schema.LookUpField("Name")

 

 }

}

db.Callback().Create().Register("crop_image", cropImage)

### [](https://gorm.io/docs/write_plugins.html#Deleting-a-Callback "Deleting a Callback")Deleting a Callback

If a callback is no longer needed, it can be removed:

db.Callback().Create().Remove("gorm:create")

### [](https://gorm.io/docs/write_plugins.html#Replacing-a-Callback "Replacing a Callback")Replacing a Callback

Callbacks with the same name can be replaced with a new function:

db.Callback().Create().Replace("gorm:create", newCreateFunction)

### [](https://gorm.io/docs/write_plugins.html#Ordering-Callbacks "Ordering Callbacks")Ordering Callbacks

Callbacks can be registered with specific orders to ensure they execute at the right time in the operation lifecycle.

db.Callback().Create().Before("gorm:create").Register("update_created_at", updateCreated)

db.Callback().Create().After("gorm:create").Register("update_created_at", updateCreated)

db.Callback().Query().After("gorm:query").Register("my_plugin:after_query", afterQuery)

db.Callback().Delete().After("gorm:delete").Register("my_plugin:after_delete", afterDelete)

db.Callback().Update().Before("gorm:update").Register("my_plugin:before_update", beforeUpdate)

db.Callback().Create().Before("gorm:create").After("gorm:before_create").Register("my_plugin:before_create", beforeCreate)

db.Callback().Create().Before("*").Register("update_created_at", updateCreated)

db.Callback().Create().After("*").Register("update_created_at", updateCreated)

### [](https://gorm.io/docs/write_plugins.html#Predefined-Callbacks "Predefined Callbacks")Predefined Callbacks

GORM comes with a set of predefined callbacks that drive its standard features. It’s recommended to review these [defined callbacks](https://github.com/go-gorm/gorm/blob/master/callbacks/callbacks.go) before creating custom plugins or additional callback functions.

[](https://gorm.io/docs/write_plugins.html#Plugins "Plugins")Plugins
--------------------------------------------------------------------

GORM’s plugin system allows for easy extensibility and customization of its core functionalities, enhancing your application’s capabilities while maintaining a modular architecture.

### [](https://gorm.io/docs/write_plugins.html#The-Plugin-Interface "The Plugin Interface")The `Plugin` Interface

To create a plugin for GORM, you need to define a struct that implements the `Plugin` interface:

type Plugin interface {

 Name() string

 Initialize(*gorm.DB) error

}

*   **`Name` Method**: Returns a unique string identifier for the plugin.
*   **`Initialize` Method**: Contains the logic to set up the plugin. This method is called when the plugin is registered with GORM for the first time.

### [](https://gorm.io/docs/write_plugins.html#Registering-a-Plugin "Registering a Plugin")Registering a Plugin

Once your plugin conforms to the `Plugin` interface, you can register it with a GORM instance:

db.Use(MyCustomPlugin{})

### [](https://gorm.io/docs/write_plugins.html#Accessing-Registered-Plugins "Accessing Registered Plugins")Accessing Registered Plugins

After a plugin is registered, it is stored in GORM’s configuration. You can access registered plugins via the `Plugins` map:

plugin := db.Config.Plugins[pluginName]

### [](https://gorm.io/docs/write_plugins.html#Practical-Example "Practical Example")Practical Example

An example of a GORM plugin is the Prometheus plugin, which integrates Prometheus monitoring with GORM:

db.Use(prometheus.New(prometheus.Config{

 

}))

[Prometheus plugin documentation](https://gorm.io/docs/prometheus.html) provides detailed information on its implementation and usage.

[![Image 1: GitHub tag (latest SemVer)](https://img.shields.io/github/v/tag/go-gorm/gorm?label=Latest%20GORM%20Release&color=red&&style=for-the-badge&logo=go&logoColor=red)](https://gorm.io/docs/v2_release_note.html)
