# Including a Software License

**Source:** [https://developer.wordpress.org/plugins/plugin-basics/including-a-software-license/](https://developer.wordpress.org/plugins/plugin-basics/including-a-software-license/)



# Including a Software License



↑Back to top



Most WordPress plugins are released under theGPL, which is the same license thatWordPress itself uses. However, there are other compatible options available. It is always best to clearly indicate the license your plugin uses.


In theHeader Requirementssection, we briefly mentioned how you can indicate your plugin’s license within the plugin header comment. Another common, and encouraged, practice is to place a license block comment near the top of your main plugin file (the same one that has the plugin header comment).


This license block comment usually looks something like this:


```
/*
{Plugin Name} is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 2 of the License, or
any later version.

{Plugin Name} is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with {Plugin Name}. If not, see {URI to Plugin License}.
*/
```





First published


September 16, 2014


Last updated


February 20, 2024



[PreviousDetermining Plugin and Content DirectoriesPrevious: Determining Plugin and Content Directories](https://developer.wordpress.org/plugins/plugin-basics/determining-plugin-and-content-directories/)
[NextUninstall MethodsNext: Uninstall Methods](https://developer.wordpress.org/plugins/plugin-basics/uninstall-methods/)


