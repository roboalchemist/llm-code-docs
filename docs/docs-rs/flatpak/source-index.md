flatpak
# Module source 
Source 
## Structs§
CODE_TYPESFlatpakDataCheckerConfigSee https://github.com/flathub/flatpak-external-data-checker#changes-to-flatpak-manifests
for the specificationFlatpakSourceThese contain a pointer to the source that will be extracted into the
source directory before the build starts. They can be of several types,
distinguished by the type property.VCS_TYPES
## Enums§
FlatpakSourceItemThe sources are a list pointer to the source code that needs to be extracted into
the build directory before the build starts.
They can be of several types, distinguished by the type property.FlatpakSourceTypeThe Flatpak sources can be of multiple different types, determined
by the `type` field. The type of the Flatpak source will determine which
other fields should be populated.
## Constants§
ARCHIVEBAZAARDIREXTRA_DATAFILEGITPATCHSCRIPTSHELLSVN