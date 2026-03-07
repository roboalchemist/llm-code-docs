# Source: https://project-chip.github.io/connectedhomeip-doc/testing/yaml_schema.html

# YAML Schema

# YAML Schema

YAML schema

key | type | supports variables  
---|---|---  
name | str |
PICS | str,list |
config |  |
nodeId | int |
cluster | str |
endpoint | int |
_variableName_ |  |
type | type |
defaultValue | Any |
tests |  |
label | str |
identity | str |
nodeId | int | Y  
runIf | str |
groupId | int | Y  
endpoint | int | Y  
cluster | str |
attribute | str |
command | str |
event | str |
eventNumber | int | Y  
disabled | bool |
fabricFiltered | bool |
verification | str |
PICS | str |
arguments |  |
values |  |
value | NoneType,bool,int,float,dict,list | Y  
name | str |
value | NoneType,bool,int,float,dict,list | Y  
response |  | Y  
value | NoneType,bool,int,float,dict,list | Y  
name | str |
error | str |
clusterError | int |
constraints |  |
hasValue | bool |
type | str |
minLength | int |
maxLength | int |
isHexString | bool |
startsWith | str |
endsWith | str |
isUpperCase | bool |
isLowerCase | bool |
isSetOfValues | list |
minValue | int,float | Y  
maxValue | int,float | Y  
contains | list |
excludes | list |
hasMasksSet | list |
hasMasksClear | list |
notValue | NoneType,bool,int,float,list,dict | Y  
anyOf | list |
python | str | Y  
saveAs | str |
saveDataVersschemaionAs | str |
saveResponseAs | str |
minInterval | int |
maxInterval | int |
keepSubscriptions | bool |
timeout | int |
timedInteractionTimeoutMs | int |
dataVersion | list,int | Y  
busyWaitMs | int |
wait | str |
minRevision | int | Y  
maxRevision | int | Y
