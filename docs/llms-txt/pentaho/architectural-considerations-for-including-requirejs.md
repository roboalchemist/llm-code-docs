# Source: https://docs.pentaho.com/pba-ctools/cde-advanced-solutions/architectural-considerations-for-including-requirejs.md

# Source: https://docs.pentaho.com/pba-ctools/9.3-ctools/cde-advanced-solutions/architectural-considerations-for-including-requirejs.md

# Source: https://docs.pentaho.com/pba-ctools/10.2-ctools/cde-advanced-solutions/architectural-considerations-for-including-requirejs.md

# Architectural considerations for including RequireJS

Including RequireJS in CTools required several architectural changes, such as using Asynchronous Module Definition (AMD) for JavaScript modules.

Specifically, the following changes were made:

## The Dashboards singleton no longer exists.

Most of the methods called in `Dashboards` are available elsewhere. If you are running code in the component context (meaning that this refers to a component), like in `preExecution`, `postExecution` and `postFetch`, most methods will be available in the `this.dashboard`. Some exceptions exist:

* The logging methods were migrated to a separate AMD module with ID `cdf/Logger`, so `Dashboards.log` has been replaced with `Logger.log`.
* Some static methods were migrated to a separate AMD module with ID `cdf/dashboard/Utils`, such that
  * `Dashboards.escapeHtml` is now `Utils.escapeHtml`.
  * `Dashboards.getQueryParameter` is now `Utils.getQueryParameter`.
  * `Dashboards.objectToPropertiesArray` is now `Utils.objectToPropertiesArray`.
  * `Dashboards.propertiesArrayToObject` is now `Utils.propertiesArrayToObject`.

## Parameters and components no longer create objects in the global scope.

Instead, components and parameters are internal to the dashboard. If you want to get to a component, you need to use the `getComponent` method in the `dashboardobject`. For parameters, always use the `getParameter` method.

When debugging during dashboard development, follow the same guideline. If you have a component called `foo`, then the object `render_foo` is no longer accessible from the console. Instead, call `dashboard.getComponent ("render_foo")` to get to that component. When CDE renders, it creates a `dashboard` object in the global scope. It is recommended that you use the dashboard object to access the dashboard internals you need. You can view further information on [RequireJS in CTools Dashboards](https://community.hitachivantara.com/s/article/requirejs-in-ctools-dashboards).
