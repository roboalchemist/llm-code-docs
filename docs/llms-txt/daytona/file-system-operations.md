# Source: https://www.daytona.io/docs/en/file-system-operations.md

The Daytona SDK provides comprehensive file system operations through the `fs` module in Sandboxes. This guide covers all available file system operations and best practices.

## Basic Operations

Daytona SDK provides an option to interact with the file system in Sandboxes using Python, TypeScript, and Ruby. You can perform various operations like listing files, creating directories, reading and writing files, and more.

File operations assume you are operating in the Sandbox user's home directory (e.g. `workspace` implies `/home/[username]/workspace`). Use a leading `/` when providing absolute paths.

### Listing Files and Directories

Daytona SDK provides an option to list files and directories in a Sandbox using Python, TypeScript, and Ruby.

```python
# List files in a directory
files = sandbox.fs.list_files("workspace")

for file in files:
    print(f"Name: {file.name}")
    print(f"Is directory: {file.is_dir}")
    print(f"Size: {file.size}")
    print(f"Modified: {file.mod_time}")

```
```typescript
// List files in a directory
const files = await sandbox.fs.listFiles("workspace")

files.forEach(file => {
    console.log(`Name: ${file.name}`)
    console.log(`Is directory: ${file.isDir}`)
    console.log(`Size: ${file.size}`)
    console.log(`Modified: ${file.modTime}`)
})
```

```ruby
# List files in a directory
files = sandbox.fs.list_files('workspace')

files.each do |file|
  puts "Name: #{file.name}"
  puts "Is directory: #{file.is_dir}"
  puts "Size: #{file.size}"
  puts "Modified: #{file.mod_time}"
end
```


See: [list_files (Python SDK)](https://www.daytona.io/docs/python-sdk/sync/file-system.md#filesystemlist_files), [listFiles (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/file-system.md#listfiles), [list_files (Ruby SDK)](https://www.daytona.io/docs/ruby-sdk/file-system.md#list_files)

### Creating Directories

Daytona SDK provides an option to create directories with specific permissions using Python, TypeScript, and Ruby.

```python
# Create with specific permissions
sandbox.fs.create_folder("workspace/new-dir", "755")
```
```typescript
// Create with specific permissions
await sandbox.fs.createFolder("workspace/new-dir", "755")
```

```ruby
# Create with specific permissions
sandbox.fs.create_folder('workspace/new-dir', '755')
```


See: [create_folder (Python SDK)](https://www.daytona.io/docs/python-sdk/sync/file-system.md#filesystemcreate_folder), [createFolder (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/file-system.md#createfolder), [create_folder (Ruby SDK)](https://www.daytona.io/docs/ruby-sdk/file-system.md#create_folder)

### Uploading Files

Daytona SDK provides options to read, write, upload, download, and delete files in Sandboxes using Python, TypeScript, and Ruby.

#### Uploading a Single File

The following example shows how to upload a single file:

```python
# Upload a single file
with open("local_file.txt", "rb") as f:
    content = f.read()
sandbox.fs.upload_file(content, "remote_file.txt")
```
```typescript
// Upload a single file
const fileContent = Buffer.from('Hello, World!')
await sandbox.fs.uploadFile(fileContent, "data.txt")
```

```ruby
# Upload a single file
content = 'Hello, World!'
sandbox.fs.upload_file(content, 'data.txt')
```


See: [upload_file (Python SDK)](https://www.daytona.io/docs/python-sdk/sync/file-system.md#filesystemupload_file), [uploadFile (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/file-system.md#uploadfile), [upload_file (Ruby SDK)](https://www.daytona.io/docs/ruby-sdk/file-system.md#upload_file)

#### Uploading Multiple Files

The following example shows how to efficiently upload multiple files with a single method call.

```python
# Upload multiple files at once
files_to_upload = []

with open("file1.txt", "rb") as f1:
    files_to_upload.append(FileUpload(
        source=f1.read(),
        destination="data/file1.txt",
    ))

with open("file2.txt", "rb") as f2:
    files_to_upload.append(FileUpload(
        source=f2.read(),
        destination="data/file2.txt",
    ))

with open("settings.json", "rb") as f3:
    files_to_upload.append(FileUpload(
        source=f3.read(),
        destination="config/settings.json",
    ))

sandbox.fs.upload_files(files_to_upload)

```
```typescript
// Upload multiple files at once
const files = [
    {
        source: Buffer.from('Content of file 1'),
        destination: 'data/file1.txt',
    },
    {
        source: Buffer.from('Content of file 2'),
        destination: 'data/file2.txt',
    },
    {
        source: Buffer.from('{"key": "value"}'),
        destination: 'config/settings.json',
    }
]

await sandbox.fs.uploadFiles(files)
```


```ruby
# Upload multiple files at once
files = [
  Daytona::FileUpload.new('Content of file 1', 'data/file1.txt'),
  Daytona::FileUpload.new('Content of file 2', 'data/file2.txt'),
  Daytona::FileUpload.new('{"key": "value"}', 'config/settings.json')
]

sandbox.fs.upload_files(files)
```


See: [upload_files (Python SDK)](https://www.daytona.io/docs/python-sdk/sync/file-system.md#filesystemupload_files), [uploadFiles (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/file-system.md#uploadfiles), [upload_files (Ruby SDK)](https://www.daytona.io/docs/ruby-sdk/file-system.md#upload_files)

### Downloading Files

#### Downloading a Single File

The following commands downloads a single file `file1.txt` from the Sandbox working directory and prints out the content:

```python

content = sandbox.fs.download_file("file1.txt")

with open("local_file.txt", "wb") as f:
    f.write(content)

print(content.decode('utf-8'))

```
```typescript

const downloadedFile = await sandbox.fs.downloadFile("file1.txt")

console.log('File content:', downloadedFile.toString())

```


```ruby

# Download file and get a Tempfile reference
file = sandbox.fs.download_file('file1.txt')

# Read the content
puts "File content: #{file.open.read}"

# Or download and save to a specific path
sandbox.fs.download_file('file1.txt', 'local_file.txt')

```


See: [download_file (Python SDK)](https://www.daytona.io/docs/python-sdk/sync/file-system.md#filesystemdownload_file), [downloadFile (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/file-system.md#downloadfile), [download_file (Ruby SDK)](https://www.daytona.io/docs/ruby-sdk/file-system.md#download_file)

#### Downloading Multiple Files

The following example shows how to efficiently download multiple files with a single method call.

```python
# Download multiple files at once
files_to_download = [
    FileDownloadRequest(source="data/file1.txt"), # No destination - download to memory
    FileDownloadRequest(source="data/file2.txt", destination="local_file2.txt"), # Download to local file
]

results = sandbox.fs.download_files(files_to_download)

for result in results:
    if result.error:
        print(f"Error downloading {result.source}: {result.error}")
    elif result.result:
        print(f"Downloaded {result.source} to {result.result}")

```
```typescript
// Download multiple files at once
const files = [
    { source: "data/file1.txt" }, // No destination - download to memory
    { source: "data/file2.txt", destination: "local_file2.txt" }, // Download to local file
]

const results = await sandbox.fs.downloadFiles(files)

results.forEach(result => {
    if (result.error) {
        console.error(`Error downloading ${result.source}: ${result.error}`)
    } else if (result.result) {
        console.log(`Downloaded ${result.source} to ${result.result}`)
    }
})
```

```ruby
# Download multiple files at once
files = [
  Daytona::FileDownloadRequest.new(source: 'data/file1.txt'), # No destination - download to memory
  Daytona::FileDownloadRequest.new(source: 'data/file2.txt', destination: 'local_file2.txt') # Download to local file
]

results = sandbox.fs.download_files(files)

results.each do |result|
  if result.error
    puts "Error downloading #{result.source}: #{result.error}"
  elsif result.result
    puts "Downloaded #{result.source} to #{result.result}"
  end
end
```

See: [download_files (Python SDK)](https://www.daytona.io/docs/python-sdk/sync/file-system.md#filesystemdownload_files), [downloadFiles (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/file-system.md#downloadfiles), [download_files (Ruby SDK)](https://www.daytona.io/docs/ruby-sdk/file-system.md#download_files)

### Deleting files

The following example shows how to delete a file:

```python

sandbox.fs.delete_file("workspace/file.txt")

```
```typescript

await sandbox.fs.deleteFile("workspace/file.txt")
```


```ruby

sandbox.fs.delete_file('workspace/file.txt')

```


See: [delete_file (Python SDK)](https://www.daytona.io/docs/python-sdk/sync/file-system.md#filesystemdelete_file), [deleteFile (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/file-system.md#deletefile), [delete_file (Ruby SDK)](https://www.daytona.io/docs/ruby-sdk/file-system.md#delete_file)

## Advanced Operations

Daytona SDK provides advanced file system operations like file permissions, search and replace, and more.

### File Permissions

Daytona SDK provides an option to set file permissions, get file permissions, and set directory permissions recursively using Python, TypeScript, and Ruby.

```python
# Set file permissions
sandbox.fs.set_file_permissions("workspace/file.txt", "644")

# Get file permissions

file_info = sandbox.fs.get_file_info("workspace/file.txt")
print(f"Permissions: {file_info.permissions}")

```
```typescript
// Set file permissions
await sandbox.fs.setFilePermissions("workspace/file.txt", { mode: "644" })

// Get file permissions
const fileInfo = await sandbox.fs.getFileDetails("workspace/file.txt")
console.log(`Permissions: ${fileInfo.permissions}`)
```


```ruby
# Set file permissions
sandbox.fs.set_file_permissions('workspace/file.txt', '644')

# Get file permissions
file_info = sandbox.fs.get_file_info('workspace/file.txt')
puts "Permissions: #{file_info.permissions}"
```


See: [set_file_permissions (Python SDK)](https://www.daytona.io/docs/python-sdk/sync/file-system.md#filesystemset_file_permissions), [setFilePermissions (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/file-system.md#setfilepermissions), [set_file_permissions (Ruby SDK)](https://www.daytona.io/docs/ruby-sdk/file-system.md#set_file_permissions)

### File Search and Replace

Daytona SDK provides an option to search for text in files and replace text in files using Python, TypeScript, and Ruby.

```python
# Search for text in files; if a folder is specified, the search is recursive
results = sandbox.fs.find_files(
    path="workspace/src",
    pattern="text-of-interest"
)
for match in results:
    print(f"Absolute file path: {match.file}")
    print(f"Line number: {match.line}")
    print(f"Line content: {match.content}")
    print("\n")

# Replace text in files

sandbox.fs.replace_in_files(
    files=["workspace/file1.txt", "workspace/file2.txt"],
    pattern="old_text",
    new_value="new_text"
)

```
```typescript
// Search for text in files; if a folder is specified, the search is recursive
const results = await sandbox.fs.findFiles({
    path="workspace/src",
    pattern: "text-of-interest"
})
results.forEach(match => {
    console.log('Absolute file path:', match.file)
    console.log('Line number:', match.line)
    console.log('Line content:', match.content)
})

// Replace text in files
await sandbox.fs.replaceInFiles(
    ["workspace/file1.txt", "workspace/file2.txt"],
    "old_text",
    "new_text"
)
```


```ruby
# Search for text in files; if a folder is specified, the search is recursive
results = sandbox.fs.find_files('workspace/src', 'text-of-interest')
results.each do |match|
  puts "Absolute file path: #{match.file}"
  puts "Line number: #{match.line}"
  puts "Line content: #{match.content}"
end

# Replace text in files
sandbox.fs.replace_in_files(
  files: ['workspace/file1.txt', 'workspace/file2.txt'],
  pattern: 'old_text',
  new_value: 'new_text'
)
```


See: [find_files (Python SDK)](https://www.daytona.io/docs/python-sdk/sync/file-system.md#filesystemfind_files), [replace_in_files (Python SDK)](https://www.daytona.io/docs/python-sdk/sync/file-system.md#filesystemreplace_in_files), [findFiles (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/file-system.md#findfiles), [replaceInFiles (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/file-system.md#replaceinfiles), [find_files (Ruby SDK)](https://www.daytona.io/docs/ruby-sdk/file-system.md#find_files), [replace_in_files (Ruby SDK)](https://www.daytona.io/docs/ruby-sdk/file-system.md#replace_in_files)