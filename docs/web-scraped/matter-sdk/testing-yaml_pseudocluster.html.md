# Source: https://project-chip.github.io/connectedhomeip-doc/testing/yaml_pseudocluster.html

# YAML Pseudo-clusters

# YAML Pseudo-clusters

CommissionerCommands

command | args | arg type | arg optional  
---|---|---|---  
PairWithCode | nodeId  
payload  
discoverOnce | node_id  
char_string  
boolean | false  
false  
true  
Unpair | nodeId | node_id | false  
GetCommissionerNodeId |  |  |
GetCommissionerNodeIdResponse | nodeId | node_id | false  
GetCommissionerRootCertificate |  |  |
GetCommissionerRootCertificateResponse | RCAC | OCTET_STRING | false  
IssueNocChain | Elements  
nodeId | octet_string  
node_id | false  
false  
IssueNocChainResponse | NOC  
ICAC  
RCAC  
IPK | octet_string  
octet_string  
octet_string  
octet_string | false  
false  
false  
false  
  
DelayCommands

command | args | arg type | arg optional  
---|---|---|---  
WaitForCommissioning |  |  |
WaitForCommissionee | nodeId  
expireExistingSession | node_id  
bool | false  
true  
WaitForMs | ms | int16u | false  
WaitForMessage | registerKey  
message | char_string  
char_string | false  
false  
  
DiscoveryCommands

command | args | arg type | arg optional  
---|---|---|---  
FindCommissionable |  |  |
FindCommissionableByShortDiscriminator | value | int16u | false  
FindCommissionableByLongDiscriminator | value | int16u | false  
FindCommissionableByCommissioningMode |  |  |
FindCommissionableByVendorId | value | vendor_id | false  
FindCommissionableByDeviceType | value | devtype_id | false  
FindCommissioner |  |  |
FindCommissionerByVendorId | value | vendor_id | false  
FindCommissionerByDeviceType | value | devtype_id | false  
FindResponse | hostName  
instanceName  
longDiscriminator  
shortDiscriminator  
vendorId  
productId  
commissioningMode  
deviceType  
deviceName  
rotatingId  
rotatingIdLen  
pairingHint  
pairingInstruction  
supportsTcp  
numIPs  
port  
mrpRetryIntervalIdle  
mrpRetryIntervalActive  
mrpRetryActiveThreshold  
isICDOperatingAsLIT | char_string  
char_string  
int16u  
int16u  
vendor_id  
int16u  
int8u  
devtype_id  
char_string  
octet_string  
int64u  
int16u  
char_string  
boolean  
int8u  
int16u  
int32u  
int32u  
int16u  
boolean | false  
false  
false  
false  
false  
false  
false  
false  
false  
false  
false  
false  
false  
false  
false  
false  
true  
true  
true  
true  
  
EqualityCommands

command | args | arg type | arg optional  
---|---|---|---  
BooleanEquals | Value1  
Value2 | boolean  
boolean | false  
false  
SignedNumberEquals | Value1  
Value2 | int64s  
int64s | false  
false  
UnsignedNumberEquals | Value1  
Value2 | int64u  
int64u | false  
false  
EqualityResponse | Equals | bool | false  
  
LogCommands

command | args | arg type | arg optional  
---|---|---|---  
Log | message | char_string | false  
UserPrompt | message  
expectedValue | char_string  
char_string | false  
true  
  
SystemCommands

command | args | arg type | arg optional  
---|---|---|---  
Start | registerKey  
discriminator  
port  
minCommissioningTimeout  
kvs  
filepath  
otaDownloadPath  
endUserSupportLogPath  
networkDiagnosticsLogPath  
crashLogPath | char_string  
int16u  
int16u  
int16u  
char_string  
char_string  
char_string  
char_string  
char_string  
char_string | true  
true  
true  
true  
true  
true  
true  
true  
true  
true  
Stop | registerKey | char_string | true  
Reboot | registerKey | char_string | true  
FactoryReset | registerKey | char_string | true  
CreateOtaImage | otaImageFilePath  
rawImageFilePath  
rawImageContent | char_string  
char_string  
char_string | false  
false  
false  
CompareFiles | file1  
file2 | char_string  
char_string | false  
false  
CreateFile | filePath  
fileContent | char_string  
char_string | false  
false  
DeleteFile | filePath | char_string | false
