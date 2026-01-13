# Source: https://typescript-eslint.io/packages/project-service

On this page# `@typescript-eslint/project-service`
[](https://npmjs.com/@typescript-eslint/project-service)
Standalone TypeScript project service wrapper for linting ✨
The typescript-eslint Project Service is a wrapper around TypeScript&#x27;s "project service" APIs.
These APIs are what editors such as VS Code use to programmatically "open" files and generate TypeScript programs for type information.
noteSee [Blog > Typed Linting with Project Service](/blog/project-service) for more details on how lint users interact with the Project Service.
```
import { createProjectService } from &#x27;@typescript-eslint/project-service&#x27;;
const filePathAbsolute = &#x27;/path/to/your/project/index.ts&#x27;;
const { service } = createProjectService();
service.openClientFile(filePathAbsolute);
const scriptInfo = service.getScriptInfo(filePathAbsolute)!;
const program = service
.getDefaultProjectForFile(scriptInfo.fileName, true)!
.getLanguageService(true)
.getProgram()!;
```
The following documentation is auto-generated from source code.
## Functions[​](#functions)
### createProjectService()[​](#createprojectservice)
```
function createProjectService(settings): ProjectServiceAndMetadata;
```
Defined in: [createProjectService.ts:93](https://github.com/typescript-eslint/typescript-eslint/blob/9ddd5712687140a68352978fb76428de53ab789e/packages/project-service/src/createProjectService.ts#L93)
Creates a new Project Service instance, as well as metadata on its creation.
#### Parameters[​](#parameters)
ParameterTypeDescription`settings`[`CreateProjectServiceSettings`](#createprojectservicesettings)Settings to create a new Project Service instance.
#### Returns[​](#returns)
[`ProjectServiceAndMetadata`](#projectserviceandmetadata)
A new Project Service instance, as well as metadata on its creation.
#### Example[​](#example)
```
import { createProjectService } from &#x27;@typescript-eslint/project-service&#x27;;
const { service } = createProjectService();
service.openClientFile(&#x27;index.ts&#x27;);
```
## Interfaces[​](#interfaces)
### CreateProjectServiceSettings[​](#createprojectservicesettings)
Defined in: [createProjectService.ts:63](https://github.com/typescript-eslint/typescript-eslint/blob/9ddd5712687140a68352978fb76428de53ab789e/packages/project-service/src/createProjectService.ts#L63)
Settings to create a new Project Service instance with [createProjectService](#createprojectservice).
#### Properties[​](#properties)
PropertyTypeDescriptionDefined in `jsDocParsingMode?``JSDocParsingMode`How aggressively (and slowly) to parse JSDoc comments.[createProjectService.ts:72](https://github.com/typescript-eslint/typescript-eslint/blob/9ddd5712687140a68352978fb76428de53ab789e/packages/project-service/src/createProjectService.ts#L72) `options?``ProjectServiceOptions`Granular options to configure the project service.[createProjectService.ts:67](https://github.com/typescript-eslint/typescript-eslint/blob/9ddd5712687140a68352978fb76428de53ab789e/packages/project-service/src/createProjectService.ts#L67) `tsconfigRootDir?``string`Root directory for the tsconfig.json file, if not the current directory.[createProjectService.ts:77](https://github.com/typescript-eslint/typescript-eslint/blob/9ddd5712687140a68352978fb76428de53ab789e/packages/project-service/src/createProjectService.ts#L77)
### ProjectServiceAndMetadata[​](#projectserviceandmetadata)
Defined in: [createProjectService.ts:38](https://github.com/typescript-eslint/typescript-eslint/blob/9ddd5712687140a68352978fb76428de53ab789e/packages/project-service/src/createProjectService.ts#L38)
A created Project Service instance, as well as metadata on its creation.
#### Properties[​](#properties-1)
PropertyTypeDescriptionDefined in `allowDefaultProject``string`[] | `undefined`Files allowed to be loaded from the default project, if any were specified.[createProjectService.ts:42](https://github.com/typescript-eslint/typescript-eslint/blob/9ddd5712687140a68352978fb76428de53ab789e/packages/project-service/src/createProjectService.ts#L42) `lastReloadTimestamp``number`The performance.now() timestamp of the last reload of the project service.[createProjectService.ts:47](https://github.com/typescript-eslint/typescript-eslint/blob/9ddd5712687140a68352978fb76428de53ab789e/packages/project-service/src/createProjectService.ts#L47) `maximumDefaultProjectFileMatchCount``number`The maximum number of files that can be matched by the default project.[createProjectService.ts:52](https://github.com/typescript-eslint/typescript-eslint/blob/9ddd5712687140a68352978fb76428de53ab789e/packages/project-service/src/createProjectService.ts#L52) `service``ProjectService`The created TypeScript Project Service instance.[createProjectService.ts:57](https://github.com/typescript-eslint/typescript-eslint/blob/9ddd5712687140a68352978fb76428de53ab789e/packages/project-service/src/createProjectService.ts#L57)
## Type Aliases[​](#type-aliases)
### TypeScriptProjectService[​](#typescriptprojectservice)
```
type TypeScriptProjectService = ts.server.ProjectService;
```
Defined in: [createProjectService.ts:33](https://github.com/typescript-eslint/typescript-eslint/blob/9ddd5712687140a68352978fb76428de53ab789e/packages/project-service/src/createProjectService.ts#L33)
Shortcut type to refer to TypeScript&#x27;s server ProjectService.
[Edit this page](https://github.com/typescript-eslint/typescript-eslint/edit/main/packages/website/../../docs/packages/Project_Service.mdx)- [Functions](#functions)[createProjectService()](#createprojectservice)- [Interfaces](#interfaces)[CreateProjectServiceSettings](#createprojectservicesettings)- [ProjectServiceAndMetadata](#projectserviceandmetadata)- [Type Aliases](#type-aliases)[TypeScriptProjectService](#typescriptprojectservice)