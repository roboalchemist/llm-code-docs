### Index ¶

- Constants

- 
        func MainHelpTemplate() string

- 
        func MainUsageTemplate() string

- 
          type CommandGroup

- 

  - 
            func CreateCmdGroup(msg string, cmds ...*cobra.Command) CommandGroup

- 
          type CommandGroups

- 

  - 
            func AddAdditionalCommands(g CommandGroups, message string, cmds []*cobra.Command) CommandGroups

- 

  - 
            func (g CommandGroups) Add(c *cobra.Command)

  - 
            func (g CommandGroups) Has(c *cobra.Command) bool

- 
          type FlagExposer

- 

  - 
            func ActsAsRootCommand(cmd *cobra.Command, filters []string, groups ...CommandGroup) FlagExposer

### Constants ¶

  
    
      View Source
      

```
const (
	// SectionVars is the help template section that declares variables to be used in the template.
	SectionVars = `{{$isRootCmd := isRootCmd .}}` +
		`{{$rootCmd := rootCmd .}}` +
		`{{$visibleFlags := visibleFlags (flagsNotIntersected .LocalFlags .PersistentFlags)}}` +
		`{{$explicitlyExposedFlags := exposed .}}` +
		`{{$usageLine := usageLine .}}`

	// SectionAliases is the help template section that displays command aliases.
	SectionAliases = `{{if gt .Aliases 0}}Aliases:
  {{.NameAndAliases}}

{{end}}`

	// SectionExamples is the help template section that displays command examples.
	SectionExamples = `{{if .HasExample}}Examples:
  {{trimRight .Example}}

{{end}}`

	// SectionSubcommands is the help template section that displays the command's subcommands.
	SectionSubcommands = `{{if .HasAvailableSubCommands}}{{cmdGroupsString .}}

{{end}}`

	// SectionFlags is the help template section that displays the command's flags.
	SectionFlags = `{{ if $visibleFlags.HasFlags}}Options:
{{trimRight (flagsUsages $visibleFlags)}}

{{end}}`

	// SectionGlobalFlags is the help template section that displays the command's global flags.
	SectionGlobalFlags = `` /* 174-byte string literal not displayed */

	// SectionUsage is the help template section that displays the command's usage.
	SectionUsage = `{{if and .Runnable (ne .UseLine "") (ne .UseLine $rootCmd)}}Usage:
  {{$usageLine}}
{{end}}`

	// SectionTipsHelp is the help template section that displays the '--help' hint.
	SectionTipsHelp = `{{if .HasSubCommands}}Use "{{$rootCmd}} <command> --help" for more information about a given command.
{{end}}`
)
```

    
  

    
      View Source
      

```
const AliasSeparator = " |:|: "
```

    
  

  
### Variables ¶

  

This section is empty.

  
### Functions ¶

  
	  
  
  
    
#### 
      func MainHelpTemplate ¶
  
    
  

    
    
      

```
func MainHelpTemplate() string
```

    
  

MainHelpTemplate if the template for 'help' used by most commands.

  

        
	  
  
  
    
#### 
      func MainUsageTemplate ¶
  
    
  

    
    
      

```
func MainUsageTemplate() string
```

    
  

MainUsageTemplate if the template for 'usage' used by most commands.

  

        

  
### Types ¶

  
      
  
  
    
#### 
      type CommandGroup ¶
  
    
  

    
    
      

```
type CommandGroup struct {
	Message  string
	Commands []*cobra.Command
}
```

    
  

    
  
  
    
#### 
      func CreateCmdGroup ¶
  
    
  

    
    
      

```
func CreateCmdGroup(msg string, cmds ...*cobra.Command) CommandGroup
```