flatpak
# Module module 
Source 
## Structs§
FlatpakBuildOptionsBuild options specify the build environment of a module,
and can be specified globally as well as per-module.
Options can also be specified on a per-architecture basis using the arch property.FlatpakModuleEach module specifies a source that has to be separately built and installed.
It contains the build options and a list of sources to download and extract before
building.
## Enums§
FlatpakBuildOptionsEnvThis is a dictionary defining environment variables to be set during the build.
Elements in this override the properties that set the environment, like
cflags and ldflags. Keys with a null value unset the corresponding variable.
FIXME the doc says this should be an object, but when defined in the modules,
it is actually an array with values like PPC_CONFIG_PATH=/app/etc.FlatpakModuleItemItems in a module list can be either paths to external module manifests, or inline descriptions
of flatpak modules.