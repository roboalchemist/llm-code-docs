# Source: https://docs.pentaho.com/pba-ctools/pentaho-cdf-api/dashboard/sprintf.md

# Sprintf

## cdf.dashboard. Sprintf

Static

Sprintf implementation for javascript. The class returns a function that can be called to format a string according to the Sprintf specs.

```
require(["cdf/dashboard/Sprintf"], function(Sprintf) {
  var firstName ="John";
  var info = Sprintf("%s %s is %d years old!", firstName,"Doe", 42);
  //info =="John Doe is 42 years old!"});
```

**AMD Module**

```
require(["cdf/dashboard/Sprintf"], function(Sprintf) { /* code goes here */ });
```

\*\*Source:\*\*dashboard/Sprintf.js, line 21

\*\*See also:\*\*<http://www.webtoolkit.info/javascript\\_sprintf.html>
