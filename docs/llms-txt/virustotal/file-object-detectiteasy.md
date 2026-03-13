# Source: https://virustotal.readme.io/reference/file-object-detectiteasy.md

# detectiteasy

File type identification tool.

`detectiteasy`: [Detect It Easy](https://github.com/horsicq/Detect-It-Easy), or abbreviated "DIE" is a program for determining types of\
files. The program defines the types MSDOS, PE, ELF, MACH and Binary.

* `filetype`: <*string*> "PE32", "PE64", "ELF32", "ELF64", "Mach-O64".
* `values`: list of artifacts detected in the file.
  * `info`: <*string*> context of the artifact (i.e. "Native", "GUI32", "NRV", etc).
  * `version`: <*string*>.
  * `type`: <*string*> general type of detection ("Linker", "Compiler", "Packer", etc).
  * `name`: <*string*> item specific name ("UPX", "Microsoft Linker", "gcc(GNU)", etc).

```json
{
	"data": {
		...
		"attributes": {
			...
			"detectiteasy": {
				"filetype": "<string>",
				"values": [{
					"info": "<string>",
					"version": "<string>",
					"type": "<string>",
					"name": "<string>"
				}, ...]
			}
		}
	}
}
```
```json Example
{
	"data": {
		"attributes": {
			"detectiteasy": {
				"filetype": "PE32",
				"values": [{
						"version": "2.12-2.42",
						"type": "Packer",
						"name": "ASPack"
					},
					{
						"type": "Compiler",
						"name": "Borland Delphi"
					},
					{
						"info": "GUI32",
						"version": "2.25*,Delphi",
						"type": "Linker",
						"name": "Turbo Linker"
					}
				]
			}
		}
	}
}
```