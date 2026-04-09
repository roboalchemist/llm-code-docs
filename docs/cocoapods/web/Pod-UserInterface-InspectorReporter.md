# Class: Pod::UserInterface::InspectorReporter
  
    Inherits:
    
      Object
      
        

          
- Object

- Pod::UserInterface::InspectorReporter

        show all
      

    Defined in:
    lib/cocoapods/user_interface/inspector_reporter.rb
  
## Overview

Redirects GH-issues delegate callbacks to CocoaPods UI methods.

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**inspector_could_not_create_report**(error, query, inspector)  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Called when there have been networking issues in creating the report.

-
  
      #**inspector_received_empty_report**(_, inspector)  ⇒ void 

Called once the report has been received, but when there are no issues found.

-
  
      #**inspector_started_query**(_, inspector)  ⇒ void 

Called just as the investigation has begun.

-
  
      #**inspector_successfully_received_report**(report, _)  ⇒ void 

Called once the inspector has received a report with more than one issue, showing the top 3 issues, and offering a link to see more.

## Instance Method Details

###
  
    #**inspector_could_not_create_report**(error, query, inspector)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Called when there have been networking issues in creating the report.

Parameters:

-

        error

        (Error)
      
      
      
        —
        

The error returned during networking

-

        query

        (String)
      
      
      
        —
        

The original search query

-

        inspector

        (GhInspector::Inspector)
      
      
      
        —
        

The current inspector

```

63
64
65
66
67
68
```

```
# File 'lib/cocoapods/user_interface/inspector_reporter.rb', line 63

def inspector_could_not_create_report(error, query, inspector)
  safe_query = Addressable::URI.escape query
  UI.puts 'Could not access the GitHub API, you may have better luck via the website.'
  UI.puts "https://github.com/#{inspector.repo_owner}/#{inspector.repo_name}/search?q=#{safe_query}&type=Issues&utf8=✓"
  UI.puts "Error: #{error.name}"
end
```

###
  
    #**inspector_received_empty_report**(_, inspector)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Called once the report has been received, but when there are no issues found.

Parameters:

-

        inspector

        (GhInspector::Inspector)
      
      
      
        —
        

The current inspector

```

45
46
47
48
```

```
# File 'lib/cocoapods/user_interface/inspector_reporter.rb', line 45

def inspector_received_empty_report(_, inspector)
  UI.puts 'Found no similar issues. To create a new issue, please visit:'
  UI.puts "https://github.com/#{inspector.repo_owner}/#{inspector.repo_name}/issues/new"
end
```

###
  
    #**inspector_started_query**(_, inspector)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Called just as the investigation has begun. Lets the user know that it’s looking for an issue.

Parameters:

-

        inspector

        (GhInspector::Inspector)
      
      
      
        —
        

The current inspector

```

17
18
19
```

```
# File 'lib/cocoapods/user_interface/inspector_reporter.rb', line 17

def inspector_started_query(_, inspector)
  UI.puts "Looking for related issues on #{inspector.repo_owner}/#{inspector.repo_name}..."
end
```

###
  
    #**inspector_successfully_received_report**(report, _)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Called once the inspector has received a report with more than one issue, showing the top 3 issues, and offering a link to see more.

Parameters:

-

        report

        (GhInspector::InspectionReport)
      
      
      
        —
        

Report a list of the issues

```

29
30
31
32
33
34
35
36
```

```
# File 'lib/cocoapods/user_interface/inspector_reporter.rb', line 29

def inspector_successfully_received_report(report, _)
  report.issues[0..2].each { |issue| print_issue_full(issue) }

  if report.issues.count > 3
    UI.puts "and #{report.total_results - 3} more at:"
    UI.puts report.url
  end
end
```
