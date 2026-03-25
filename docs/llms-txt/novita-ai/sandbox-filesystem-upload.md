# Source: https://novita.ai/docs/guides/sandbox-filesystem-upload.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Upload data to sandbox

export const SandboxConfigHint = () => {
  if (typeof document === "undefined") {
    return null;
  } else {
    return <Note>Before running the example code in this document, please ensure you have properly configured environment variables. For details, please refer to <a href="/guides/sandbox-your-first-agent-sandbox#configure-environment-variables">Configure Environment Variables</a>.</Note>;
  }
};

You can upload data to the sandbox using the `files.write()` method.

<SandboxConfigHint />

## Upload single file

<CodeGroup>
  ```js JavaScript & TypeScript icon="js" theme={"system"}
  import fs from 'fs'
  import { Sandbox } from 'novita-sandbox/code-interpreter'

  const sandbox = await Sandbox.create()

  // Read file from local filesystem
  const localFilePath = '../local-test-file'
  const content = fs.readFileSync(localFilePath, 'utf8')

  // Upload file to sandbox
  const filePathInSandbox = '/tmp/test-file'
  const result = await sandbox.files.write(filePathInSandbox, content)
  console.log(result)

  await sandbox.kill()
  ```

  ```python Python icon="python" theme={"system"}
  from novita_sandbox.code_interpreter import Sandbox

  sandbox = Sandbox.create()

  local_file_path = '../local-test-file'
  with open(local_file_path, "rb") as file:
    file_path_in_sandbox = '/tmp/test-file'
    result = sandbox.files.write(file_path_in_sandbox, file)
    print(result)

  sandbox.kill()
  ```
</CodeGroup>

## Upload directory / multiple files

<CodeGroup>
  ```js JavaScript & TypeScript icon="js" theme={"system"}
  import fs from 'fs'
  import path from 'path'

  import { Sandbox } from 'novita-sandbox/code-interpreter'

  const sandbox = await Sandbox.create()

  const readDirectoryFiles = (directoryPath) => {
    const files = fs.readdirSync(directoryPath);

    const filesArray = files
      .filter(file => {
        const fullPath = path.join(directoryPath, file);
        return fs.statSync(fullPath).isFile();
      })
      .map(file => {
        const filePath = path.join(directoryPath, file);
      
        return {
          path: filePath,
          data: fs.readFileSync(filePath, 'utf8')
        };
      });

    return filesArray;
  };

  const localDirectoryPath = '../local-test-dir'
  const files = readDirectoryFiles(localDirectoryPath);
  console.log(files); 

  files.forEach(file => {
    file.path = file.path.replace('../local-test-dir', '/tmp')
  })

  const result = await sandbox.files.write(files)
  console.log(result)

  await sandbox.kill()
  ```

  ```python Python icon="python" theme={"system"}
  import os
  from novita_sandbox.code_interpreter import Sandbox

  sandbox = Sandbox.create()

  def read_directory_files(directory_path):
      files = []

      for filename in os.listdir(directory_path):
          file_path = os.path.join(directory_path, filename)
          
          if os.path.isfile(file_path):
              with open(file_path, "rb") as file:
                  files.append({
                      'path': file_path,
                      'data': file.read()
                  })
      return files

  local_directory_path = '../local-test-dir'
  files = read_directory_files(local_directory_path)
  print(files)

  for file in files:
      file['path'] = file['path'].replace('../local-test-dir', '/tmp')

  result = sandbox.files.write_files(files)
  print(result)

  sandbox.kill()
  ```
</CodeGroup>


Built with [Mintlify](https://mintlify.com).