# Source: https://docs.augmentcode.com/context-services/sdk/api-reference.md

# API Reference

> Complete API documentation for the Context Engine SDK

<Warning>
  **Experimental API** - Context Engine SDK is experimental and subject to breaking changes.
</Warning>

## DirectContext

This class provides explicit file indexing via API calls with the ability to import and export state to avoid re-indexing between sessions.

***

## Examples

### Example 1: Simple Usage

Upload files and ask questions immediately:

<CodeGroup>
  ```typescript TypeScript theme={null}
  import { DirectContext } from '@augmentcode/auggie-sdk';

  async function simpleExample() {
    // Create context (authentication is automatic)
    const context = await DirectContext.create();

    // Add files and wait for indexing (default behavior)
    const result = await context.addToIndex([
      { path: 'src/auth.ts', contents: 'export function login(user, pass) { ... }' },
      { path: 'src/user.ts', contents: 'export class User { constructor(id) { ... } }' },
      { path: 'README.md', contents: '# My Project\nAuthentication system' }
    ]);

    console.log(`Newly uploaded: ${result.newlyUploaded.length}`);

    // Ask questions about the code - files are already indexed
    const answer = await context.searchAndAsk(
      'How does the login system work?'
    );
    console.log('Answer:', answer);
  }

  simpleExample().catch(console.error);
  ```

  ```python Python theme={null}
  from auggie_sdk.context import DirectContext, File

  def simple_example():
      # Create context (authentication is automatic)
      context = DirectContext.create()

      # Add files and wait for indexing (default behavior)
      result = context.add_to_index([
          File(path='src/auth.py', contents='def login(user, password): ...'),
          File(path='src/user.py', contents='class User:\n    def __init__(self, id): ...'),
          File(path='README.md', contents='# My Project\nAuthentication system')
      ])

      print(f"Newly uploaded: {len(result.newly_uploaded)}")

      # Ask questions about the code - files are already indexed
      answer = context.search_and_ask(
          'How does the login system work?'
      )
      print('Answer:', answer)

  if __name__ == '__main__':
      simple_example()
  ```
</CodeGroup>

### Example 2: Persistent Index

Persist state between sessions to avoid re-indexing. This is useful when you want to save the index state to disk and reload it later without having to re-upload and re-index all files. The saved state file contains metadata about which files are indexed, allowing you to resume from where you left off:

<CodeGroup>
  ```typescript TypeScript theme={null}
  import { DirectContext } from '@augmentcode/auggie-sdk';

  // First session: Upload and save
  async function uploadAndSave() {
    const context = await DirectContext.create();

    // Upload files
    await context.addToIndex([
      { path: 'src/auth.ts', contents: 'export function login() { ... }' },
      { path: 'src/user.ts', contents: 'export class User { ... }' },
      { path: 'src/database.ts', contents: 'export function connect() { ... }' }
    ]);

    // Save state for later use - this creates a JSON file containing the index metadata
    // so you can reload it later without re-indexing all files
    await context.exportToFile('./my-project-context.json');
    console.log('Context saved!');
    console.log('You can now reload this state in a future session using importFromFile()');
  }

  // Second session: Load, update incrementally, and save again
  async function updateAndSave() {
    // Load previous state - this restores the index without re-uploading files
    const context = await DirectContext.importFromFile('./my-project-context.json');
    console.log('Context loaded from previous session - no re-indexing needed!');

    // Make incremental changes - remove old file and add new one
    await context.removeFromIndex(['src/user.ts']);
    await context.addToIndex([
      { path: 'src/profile.ts', contents: 'export class Profile { /* profile logic */ }' },
      { path: 'src/settings.ts', contents: 'export function updateSettings() { /* settings */ }' }
    ]);
    console.log('Index updated incrementally');

    // Save updated state
    await context.exportToFile('./my-project-context.json');
    console.log('Updated context saved!');
  }

  // Third session: Load and search
  async function loadAndSearch() {
    // Load the updated state
    const context = await DirectContext.importFromFile('./my-project-context.json');
    console.log('Updated context loaded');

    // Search immediately - files are already indexed
    const answer = await context.searchAndAsk(
      'What user management features are implemented?'
    );
    console.log('Answer:', answer);
  }

  // Run the complete workflow: upload → update → search
  uploadAndSave()
    .then(() => updateAndSave())
    .then(() => loadAndSearch())
    .catch(console.error);
  ```

  ```python Python theme={null}
  from auggie_sdk.context import DirectContext, File

  # First session: Upload and save
  def upload_and_save():
      context = DirectContext.create()

      # Upload files
      context.add_to_index([
          File(path='src/auth.py', contents='def login(): ...'),
          File(path='src/user.py', contents='class User: ...'),
          File(path='src/database.py', contents='def connect(): ...')
      ])

      # Save state for later use - this creates a JSON file containing the index metadata
      # so you can reload it later without re-indexing all files
      context.export_to_file('./my-project-context.json')
      print('Context saved!')
      print('You can now reload this state in a future session using import_from_file()')

  # Second session: Load, update incrementally, and save again
  def update_and_save():
      # Load previous state - this restores the index without re-uploading files
      context = DirectContext.import_from_file('./my-project-context.json')
      print('Context loaded from previous session - no re-indexing needed!')

      # Make incremental changes - remove old file and add new one
      context.remove_from_index(['src/user.py'])
      context.add_to_index([
          File(path='src/profile.py', contents='class Profile: # profile logic'),
          File(path='src/settings.py', contents='def update_settings(): # settings')
      ])
      print('Index updated incrementally')

      # Save updated state
      context.export_to_file('./my-project-context.json')
      print('Updated context saved!')

  # Third session: Load and search
  def load_and_search():
      # Load the updated state
      context = DirectContext.import_from_file('./my-project-context.json')
      print('Updated context loaded')

      # Search immediately - files are already indexed
      answer = context.search_and_ask(
          'What user management features are implemented?'
      )
      print('Answer:', answer)

  # Run the complete workflow: upload → update → search
  if __name__ == '__main__':
      upload_and_save()
      update_and_save()
      load_and_search()
  ```
</CodeGroup>

### Example 3: Batch Upload Then Wait

When you need to upload many files in multiple batches, you can optimize performance by uploading all files first without waiting for indexing, then waiting once at the end. This approach is faster than waiting for indexing after each batch:

<CodeGroup>
  ```typescript TypeScript theme={null}
  import { DirectContext } from '@augmentcode/auggie-sdk';

  async function batchExample() {
    const context = await DirectContext.create();

    // Upload multiple batches without waiting for indexing
    await context.addToIndex([
      { path: 'src/auth.ts', contents: 'export function login() { ... }' },
      { path: 'src/user.ts', contents: 'export class User { ... }' }
    ], { waitForIndexing: false });

    await context.addToIndex([
      { path: 'src/database.ts', contents: 'export function connect() { ... }' },
      { path: 'src/api.ts', contents: 'export function createServer() { ... }' }
    ], { waitForIndexing: false });

    // Wait for all files to be indexed
    console.log('Waiting for indexing to complete...');
    await context.waitForIndexing();
    console.log('All files indexed!');

    // Now search - all files are guaranteed to be indexed
    const answer = await context.searchAndAsk(
      'How do the database and auth systems work together?'
    );
    console.log('Answer:', answer);
  }

  batchExample().catch(console.error);
  ```

  ```python Python theme={null}
  from auggie_sdk.context import DirectContext, File

  def batch_example():
      context = DirectContext.create()

      # Upload multiple batches without waiting for indexing
      context.add_to_index([
          File(path='src/auth.py', contents='def login(): ...'),
          File(path='src/user.py', contents='class User: ...')
      ], wait_for_indexing=False)

      context.add_to_index([
          File(path='src/database.py', contents='def connect(): ...'),
          File(path='src/api.py', contents='def create_server(): ...')
      ], wait_for_indexing=False)

      # Wait for all files to be indexed
      print('Waiting for indexing to complete...')
      context.wait_for_indexing()
      print('All files indexed!')

      # Now search - all files are guaranteed to be indexed
      answer = context.search_and_ask(
          'How do the database and auth systems work together?'
      )
      print('Answer:', answer)

  if __name__ == '__main__':
      batch_example()
  ```
</CodeGroup>

### Example 4: Custom Prompts

Use searchAndAsk with custom prompts for diverse tasks:

<CodeGroup>
  ```typescript TypeScript theme={null}
  import { DirectContext } from '@augmentcode/auggie-sdk';

  async function creativeExample() {
    const context = await DirectContext.create();

    // Upload some code
    await context.addToIndex([
      { path: 'src/auth.ts', contents: 'export function login(user, pass) { /* auth logic */ }' },
      { path: 'src/database.ts', contents: 'export function connect() { /* db connection */ }' },
      { path: 'README.md', contents: '# My App\nA secure authentication system' }
    ]);

    // Creative prompts with searchAndAsk
    const poem = await context.searchAndAsk(
      'authentication system',
      'Write a haiku about this authentication code'
    );
    console.log('Haiku:', poem);

    // Generate documentation
    const docs = await context.searchAndAsk(
      'database authentication flow',
      'Write a brief user guide explaining how to use the database authentication flow'
    );
    console.log('Documentation:', docs);

    // Code review style analysis
    const review = await context.searchAndAsk(
      'authentication logic',
      'Provide a code review focusing on security best practices'
    );
    console.log('Code Review:', review);
  }

  creativeExample().catch(console.error);
  ```

  ```python Python theme={null}
  from auggie_sdk.context import DirectContext, File

  def creative_example():
      context = DirectContext.create()

      # Upload some code
      context.add_to_index([
          File(path='src/auth.py', contents='def login(user, password): # auth logic'),
          File(path='src/database.py', contents='def connect(): # db connection'),
          File(path='README.md', contents='# My App\nA secure authentication system')
      ])

      # Creative prompts with search_and_ask
      poem = context.search_and_ask(
          'authentication system',
          'Write a haiku about this authentication code'
      )
      print('Haiku:', poem)

      # Generate documentation
      docs = context.search_and_ask(
          'database authentication flow',
          'Write a brief user guide explaining how to use the database authentication flow'
      )
      print('Documentation:', docs)

      # Code review style analysis
      review = context.search_and_ask(
          'authentication logic',
          'Provide a code review focusing on security best practices'
      )
      print('Code Review:', review)

  if __name__ == '__main__':
      creative_example()
  ```
</CodeGroup>

### Example 5: External LLM Integration

Use search() results with external LLM APIs:

<CodeGroup>
  ```typescript TypeScript theme={null}
  import { DirectContext } from '@augmentcode/auggie-sdk';
  // import { Anthropic } from '@anthropic-ai/sdk';
  // import OpenAI from 'openai';

  async function externalLLMExample() {
    const context = await DirectContext.create();

    // Upload code
    await context.addToIndex([
      { path: 'src/api.ts', contents: 'export function handleRequest() { /* API logic */ }' },
      { path: 'src/auth.ts', contents: 'export function authenticate() { /* auth */ }' },
      { path: 'src/database.ts', contents: 'export function query() { /* db query */ }' }
    ]);

    // Get formatted search results for external LLMs
    const codeContext = await context.search('API request handling');

    // codeContext is a formatted string ready to embed in prompts for
    // Anthropic, OpenAI, or other LLM APIs
    console.log('Code context for LLM:', codeContext);

    // Example: Use with Anthropic Claude (uncomment to use)
    // const anthropic = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });
    // const response = await anthropic.messages.create({
    //   model: 'claude-sonnet-4-5-20250929',
    //   max_tokens: 1000,
    //   messages: [{
    //     role: 'user',
    //     content: `Based on this code:\n\n${codeContext}\n\nHow can I improve the error handling in the API?`
    //   }]
    // });
    // console.log('Claude response:', response.content[0].text);

    // Example: Use with OpenAI GPT-5.1 (uncomment to use)
    // const openai = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });
    // const completion = await openai.chat.completions.create({
    //   model: 'gpt-5.1',
    //   messages: [{
    //     role: 'user',
    //     content: `Based on this code:\n\n${codeContext}\n\nSuggest performance optimizations for this API.`
    //   }]
    // });
    // console.log('GPT-5.1 response:', completion.choices[0].message.content);


  }

  externalLLMExample().catch(console.error);
  ```

  ```python Python theme={null}
  from auggie_sdk.context import DirectContext, File
  # import anthropic
  # import openai

  def external_llm_example():
      context = DirectContext.create()

      # Upload code
      context.add_to_index([
          File(path='src/api.py', contents='def handle_request(): # API logic'),
          File(path='src/auth.py', contents='def authenticate(): # auth'),
          File(path='src/database.py', contents='def query(): # db query')
      ])

      # Get formatted search results for external LLMs
      code_context = context.search('API request handling')

      # code_context is a formatted string ready to embed in prompts for
      # Anthropic, OpenAI, or other LLM APIs
      print('Code context for LLM:', code_context)

      # Example: Use with Anthropic Claude (uncomment to use)
      # client = anthropic.Anthropic(api_key=os.environ['ANTHROPIC_API_KEY'])
      # response = client.messages.create(
      #     model='claude-sonnet-4-5-20250929',
      #     max_tokens=1000,
      #     messages=[{
      #         'role': 'user',
      #         'content': f'Based on this code:\n\n{code_context}\n\nHow can I improve the error handling?'
      #     }]
      # )
      # print('Claude response:', response.content[0].text)

      # Example: Use with OpenAI GPT-5.1 (uncomment to use)
      # client = openai.OpenAI(api_key=os.environ['OPENAI_API_KEY'])
      # completion = client.chat.completions.create(
      #     model='gpt-5.1',
      #     messages=[{
      #         'role': 'user',
      #         'content': f'Based on this code:\n\n{code_context}\n\nSuggest performance optimizations.'
      #     }]
      # )
      # print('GPT-5.1 response:', completion.choices[0].message.content)

  if __name__ == '__main__':
      external_llm_example()
  ```
</CodeGroup>

***

## API Reference

### DirectContext.create()

Create and initialize a new DirectContext instance.

<CodeGroup>
  ```typescript TypeScript theme={null}
  static async create(options?: DirectContextOptions): Promise<DirectContext>

  interface DirectContextOptions {
    apiKey?: string;      // Optional - falls back to env vars or session.json
    apiUrl?: string;      // Optional - falls back to env vars or session.json
    debug?: boolean;      // Enable debug logging (default: false)
  }
  ```

  ```python Python theme={null}
  @classmethod
  def create(
      cls,
      *,
      api_key: Optional[str] = None,
      api_url: Optional[str] = None,
      debug: bool = False,
  ) -> DirectContext
  ```
</CodeGroup>

**Parameters:**

* `options` - Optional configuration object
  * `apiKey` - API key for authentication (optional)
  * `apiUrl` - API URL for your tenant (optional)
  * `debug` - Enable debug logging (optional, default: false)

**Authentication Priority:**

1. `options.apiKey` / `options.apiUrl` (passed to create())
2. `AUGMENT_API_TOKEN` / `AUGMENT_API_URL` environment variables
3. `~/.augment/session.json` (created by `auggie login`)

**Usage:** See complete examples above for full implementation details.

**Notes:**

* The SDK is **source-agnostic** - you provide files as `{path, contents}` objects
* Files larger than 1MB are rejected during indexing
* All indexing operations are serialized to ensure consistency
* State can be saved and loaded to avoid re-indexing

***

### DirectContext.importFromFile() / import\_from\_file()

Create a DirectContext instance from a saved state file.

<CodeGroup>
  ```typescript TypeScript theme={null}
  static async importFromFile(
    filePath: string,
    options?: DirectContextOptions
  ): Promise<DirectContext>
  ```

  ```python Python theme={null}
  @classmethod
  def import_from_file(
      cls,
      file_path: str,
      *,
      api_key: Optional[str] = None,
      api_url: Optional[str] = None,
      debug: bool = False,
  ) -> DirectContext
  ```
</CodeGroup>

**Parameters:**

* `filePath` / `file_path` - Path to the saved state file
* `options` - Optional configuration object (same as `create()`)

**Returns:** A DirectContext instance with restored state

**Usage:**

<CodeGroup>
  ```typescript TypeScript theme={null}
  // Load context from saved state
  const context = await DirectContext.importFromFile('./my-context.json');
  // Files are already indexed, ready to search
  ```

  ```python Python theme={null}
  # Load context from saved state
  context = DirectContext.import_from_file('./my-context.json')
  # Files are already indexed, ready to search
  ```
</CodeGroup>

***

### DirectContext.import() / import\_state()

Create a DirectContext instance from a saved state object.

<CodeGroup>
  ```typescript TypeScript theme={null}
  static async import(
    state: DirectContextState,
    options?: DirectContextOptions
  ): Promise<DirectContext>
  ```

  ```python Python theme={null}
  @classmethod
  def import_state(
      cls,
      state: DirectContextState,
      *,
      api_key: Optional[str] = None,
      api_url: Optional[str] = None,
      debug: bool = False,
  ) -> DirectContext
  ```
</CodeGroup>

**Parameters:**

* `state` - The state object to restore from
* `options` - Optional configuration object (same as `create()`)

**Returns:** A DirectContext instance with restored state

**Usage:**

<CodeGroup>
  ```typescript TypeScript theme={null}
  // Load context from state object
  const savedState = JSON.parse(stateJson);
  const context = await DirectContext.import(savedState);
  ```

  ```python Python theme={null}
  import json
  # Load context from state object
  with open('state.json') as f:
      saved_state = DirectContextState.from_dict(json.load(f))
  context = DirectContext.import_state(saved_state)
  ```
</CodeGroup>

***

## DirectContext Methods

### addToIndex() / add\_to\_index()

Add files to the index. Files can come from any source - memory, disk, API, database, etc.

<CodeGroup>
  ```typescript TypeScript theme={null}
  async addToIndex(
    files: File[],
    options?: { waitForIndexing?: boolean }
  ): Promise<IndexingResult>

  interface File {
    path: string;      // Relative path (e.g., "src/main.ts")
    contents: string;  // File contents as string
  }

  interface IndexingResult {
    newlyUploaded: string[];     // Paths that were uploaded and indexed
    alreadyUploaded: string[];   // Paths that were skipped (already on server)
  }
  ```

  ```python Python theme={null}
  def add_to_index(
      self,
      files: List[File],
      wait_for_indexing: bool = True
  ) -> IndexingResult

  @dataclass
  class File:
      path: str       # Relative path (e.g., "src/main.py")
      contents: str   # File contents as string

  @dataclass
  class IndexingResult:
      newly_uploaded: List[str]     # Paths that were uploaded and indexed
      already_uploaded: List[str]   # Paths that were skipped (already on server)
  ```
</CodeGroup>

**Parameters:**

* `files` - Array/list of file objects with `path` and `contents`
* `options` / `wait_for_indexing` - Optional configuration
  * `waitForIndexing` / `wait_for_indexing` - If true (default), waits for the newly added files to be indexed before returning

**Returns:** `IndexingResult` object with details about what was indexed

**Notes:**

* Files larger than 1MB will throw an error
* By default, waits for backend indexing to complete before returning (set `waitForIndexing: false` / `wait_for_indexing=False` to return immediately after upload)
* If a file with the same path already exists, it will be updated
* All operations are serialized to ensure consistency
* The SDK optimizes uploads by checking which blobs the server already has and only uploading missing ones

***

### removeFromIndex() / remove\_from\_index()

Remove files from the index by path.

<CodeGroup>
  ```typescript TypeScript theme={null}
  async removeFromIndex(paths: string[]): Promise<void>
  ```

  ```python Python theme={null}
  def remove_from_index(self, paths: List[str]) -> None
  ```
</CodeGroup>

**Parameters:**

* `paths` - Array/list of file paths to remove

***

### clearIndex() / clear\_index()

Clear the entire index, removing all files.

<CodeGroup>
  ```typescript TypeScript theme={null}
  async clearIndex(): Promise<void>
  ```

  ```python Python theme={null}
  def clear_index(self) -> None
  ```
</CodeGroup>

***

### getIndexedPaths() / get\_indexed\_paths()

Get the list of currently indexed file paths.

<CodeGroup>
  ```typescript TypeScript theme={null}
  getIndexedPaths(): string[]
  ```

  ```python Python theme={null}
  def get_indexed_paths(self) -> List[str]
  ```
</CodeGroup>

**Returns:** Array/list of relative file paths that are currently indexed

**Use Cases:**

* Display indexed files to users
* Verify which files are included in the index
* Filter files for targeted searches

***

### search()

Search the codebase and return formatted results as a string.

<CodeGroup>
  ```typescript TypeScript theme={null}
  async search(
    query: string,
    options?: { maxOutputLength?: number }
  ): Promise<string>
  ```

  ```python Python theme={null}
  def search(
      self,
      query: str,
      max_output_length: Optional[int] = None
  ) -> str
  ```
</CodeGroup>

**Parameters:**

* `query` - Natural language search query
* `options` / `max_output_length` - Optional search options
  * `maxOutputLength` / `max_output_length` - Maximum character length of the formatted output (default: 20000, max: 80000)

**Returns:** Formatted string containing the search results, ready for LLM consumption

**Notes:**

* Returns a formatted string designed for use in LLM prompts
* The format includes file paths, line numbers, and code content
* Does NOT wait for indexing - ensure files are indexed before searching by either:
  * Using `addToIndex()` / `add_to_index()` with `waitForIndexing: true` / `wait_for_indexing=True` (default)
  * Calling `waitForIndexing()` / `wait_for_indexing()` explicitly before searching
* Throws an error if the index is empty

***

### searchAndAsk() / search\_and\_ask()

Search the indexed codebase and ask an LLM a question about the results.

This is a convenience method that combines `search()` with an LLM call to answer questions about your codebase.

<CodeGroup>
  ```typescript TypeScript theme={null}
  async searchAndAsk(
    searchQuery: string,
    prompt?: string
  ): Promise<string>
  ```

  ```python Python theme={null}
  def search_and_ask(
      self,
      search_query: str,
      prompt: Optional[str] = None
  ) -> str
  ```
</CodeGroup>

**Parameters:**

* `searchQuery` / `search_query` - The semantic search query to find relevant code (also used as the prompt if no separate prompt is provided)
* `prompt` - Optional prompt to ask the LLM about the search results. If not provided, searchQuery is used as the prompt.

**Returns:** The LLM's answer to your question

**Notes:**

* Does NOT wait for indexing - ensure files are indexed before searching by either:
  * Using `addToIndex()` / `add_to_index()` with `waitForIndexing: true` / `wait_for_indexing=True` (default)
  * Calling `waitForIndexing()` / `wait_for_indexing()` explicitly before searching
* Requires `AUGMENT_API_TOKEN` and `AUGMENT_API_URL` environment variables for LLM access

**Use Cases:**

* Quick Q\&A about your codebase
* Building conversational interfaces
* Automated code analysis and documentation

***

### waitForIndexing() / wait\_for\_indexing()

Wait for all indexed files to be fully indexed on the backend.

This method polls the backend until all files that have been added to the index are confirmed to be indexed and searchable.

<CodeGroup>
  ```typescript TypeScript theme={null}
  async waitForIndexing(): Promise<void>
  ```

  ```python Python theme={null}
  def wait_for_indexing(self) -> None
  ```
</CodeGroup>

**Returns:** Promise that resolves when all files are indexed

**Notes:**

* Throws an error if indexing times out (default: 10 minutes)
* Only waits for files that have been added to the index
* Useful when you want to control when to wait for indexing completion

**Use Cases:**

* Batch upload multiple files quickly, then wait for all to be indexed
* Ensure search results include all recently added files
* Control timing of indexing waits in complex workflows

***

### exportToFile() / export\_to\_file()

Export the current state to a file.

<CodeGroup>
  ```typescript TypeScript theme={null}
  async exportToFile(filePath: string): Promise<void>
  ```

  ```python Python theme={null}
  def export_to_file(self, file_path: str) -> None
  ```
</CodeGroup>

**Parameters:**

* `filePath` / `file_path` - Path to save the state file

**Use Cases:**

* Persist indexing state between sessions
* Avoid re-indexing large codebases
* Share indexing state across different processes

***

### export()

Export the current state as an object (in-memory).

<CodeGroup>
  ```typescript TypeScript theme={null}
  export(): DirectContextState

  interface DirectContextState {
    checkpointId?: string;
    addedBlobs: string[];
    deletedBlobs: string[];
    blobs: BlobEntry[];  // Array of [blobName, path] tuples
  }
  ```

  ```python Python theme={null}
  def export(self) -> DirectContextState

  @dataclass
  class DirectContextState:
      checkpoint_id: Optional[str]
      added_blobs: List[str]
      deleted_blobs: List[str]
      blobs: List[Tuple[str, str]]  # List of (blob_name, path) tuples
  ```
</CodeGroup>

**Returns:** State object that can be serialized and stored

***

## FileSystemContext

This class provides automatic indexing and search capabilities for a local directory.

### FileSystemContext.create()

Create and initialize a new FileSystemContext instance.

<CodeGroup>
  ```typescript TypeScript theme={null}
  static async create(options: FileSystemContextOptions): Promise<FileSystemContext>

  interface FileSystemContextOptions {
    directory: string;      // Path to the workspace directory to index
    auggiePath?: string;    // Path to auggie executable (default: "auggie")
    debug?: boolean;        // Enable debug logging (default: false)
  }
  ```

  ```python Python theme={null}
  @classmethod
  def create(
      cls,
      directory: str,
      *,
      auggie_path: str = "auggie",
      debug: bool = False,
  ) -> FileSystemContext
  ```
</CodeGroup>

**Parameters:**

* `options` / positional args - Configuration
  * `directory` - Path to the workspace directory to index (required)
  * `auggiePath` / `auggie_path` - Path to auggie executable (optional, default: "auggie")
  * `debug` - Enable debug logging (optional, default: false)

**Usage:** See DirectContext examples above for similar patterns.

**Notes:**

* Automatically indexes the directory on startup
* Requires `auggie` CLI to be installed and accessible
* Python supports context manager (`with` statement) for automatic cleanup

***

## FileSystemContext Methods

### search()

Search the codebase and return formatted results as a string.

<CodeGroup>
  ```typescript TypeScript theme={null}
  async search(query: string): Promise<string>
  ```

  ```python Python theme={null}
  def search(self, query: str) -> str
  ```
</CodeGroup>

**Parameters:**

* `query` - Natural language search query

**Returns:** Formatted string containing the search results, ready for LLM consumption

***

### searchAndAsk() / search\_and\_ask()

Search the indexed codebase and ask an LLM a question about the results.

<CodeGroup>
  ```typescript TypeScript theme={null}
  async searchAndAsk(
    searchQuery: string,
    prompt?: string
  ): Promise<string>
  ```

  ```python Python theme={null}
  def search_and_ask(
      self,
      search_query: str,
      prompt: Optional[str] = None
  ) -> str
  ```
</CodeGroup>

**Parameters:**

* `searchQuery` / `search_query` - The semantic search query to find relevant code (also used as the prompt if no separate prompt is provided)
* `prompt` - Optional prompt to ask the LLM about the search results. If not provided, searchQuery is used as the prompt.

**Returns:** The LLM's answer to your question

**Notes:**

* Requires `AUGMENT_API_TOKEN` and `AUGMENT_API_URL` environment variables for LLM access

***

### close()

Close the connection and cleanup resources.

<CodeGroup>
  ```typescript TypeScript theme={null}
  async close(): Promise<void>
  ```

  ```python Python theme={null}
  def close(self) -> None
  ```
</CodeGroup>

**Notes:**

* Always call `close()` when done to cleanup resources
* Python: Use context manager (`with` statement) for automatic cleanup

***

## Types

### File

Represents a file to be indexed (input type for `addToIndex()` / `add_to_index()`).

<CodeGroup>
  ```typescript TypeScript theme={null}
  interface File {
    path: string;      // Relative path (e.g., "src/main.ts")
    contents: string;  // File contents as string
  }
  ```

  ```python Python theme={null}
  @dataclass
  class File:
      path: str       # Relative path (e.g., "src/main.py")
      contents: str   # File contents as string
  ```
</CodeGroup>

### IndexingResult

Result from `addToIndex()` / `add_to_index()` operation showing what was indexed.

<CodeGroup>
  ```typescript TypeScript theme={null}
  interface IndexingResult {
    newlyUploaded: string[];     // Paths that were uploaded and indexed
    alreadyUploaded: string[];   // Paths that were skipped (already on server)
  }
  ```

  ```python Python theme={null}
  @dataclass
  class IndexingResult:
      newly_uploaded: List[str]     # Paths that were uploaded and indexed
      already_uploaded: List[str]   # Paths that were skipped (already on server)
  ```
</CodeGroup>

**Notes:**

* `newlyUploaded` / `newly_uploaded`: Files that were uploaded to the server and indexed
* `alreadyUploaded` / `already_uploaded`: Files that were skipped because:
  * They were already in the local cache with the same content, OR
  * The server already had the blob (detected via `find-missing` API)

### DirectContextOptions (TypeScript) / Keyword Arguments (Python)

Options for configuring DirectContext.

<CodeGroup>
  ```typescript TypeScript theme={null}
  interface DirectContextOptions {
    apiKey?: string;      // API key for authentication
    apiUrl?: string;      // API URL for your Augment tenant
    debug?: boolean;      // Enable debug logging (default: false)
  }
  ```

  ```python Python theme={null}
  # In Python, these are passed as keyword arguments to create():
  DirectContext.create(
      api_key: Optional[str] = None,  # API key for authentication
      api_url: Optional[str] = None,  # API URL for your Augment tenant
      debug: bool = False,            # Enable debug logging (default: False)
  )
  ```
</CodeGroup>

### DirectContextState

State for DirectContext that can be saved/loaded.

<CodeGroup>
  ```typescript TypeScript theme={null}
  interface DirectContextState {
    checkpointId?: string;      // Current checkpoint ID
    addedBlobs: string[];       // Blob names added (pending checkpoint)
    deletedBlobs: string[];     // Blob names deleted (pending checkpoint)
    blobs: BlobEntry[];         // List of blobs as [blobName, path] tuples
  }

  type BlobEntry = [blobName: string, path: string];
  ```

  ```python Python theme={null}
  @dataclass
  class DirectContextState:
      checkpoint_id: Optional[str]       # Current checkpoint ID
      added_blobs: List[str]             # Blob names added (pending checkpoint)
      deleted_blobs: List[str]           # Blob names deleted (pending checkpoint)
      blobs: List[Tuple[str, str]]       # List of (blob_name, path) tuples

      def to_dict(self) -> Dict[str, Any]:
          """Convert to JSON-serializable dict."""
          ...

      @classmethod
      def from_dict(cls, data: Dict[str, Any]) -> DirectContextState:
          """Create from JSON dict (e.g., from imported state file)."""
          ...
  ```
</CodeGroup>

**Serialization Example:**

<CodeGroup>
  ```typescript TypeScript theme={null}
  // DirectContextState is a plain object, use JSON.parse/stringify
  const stateJson = JSON.stringify(context.export());
  const restoredState = JSON.parse(stateJson);
  const newContext = await DirectContext.import(restoredState);
  ```

  ```python Python theme={null}
  import json

  # Export state and serialize to JSON
  state = context.export()
  state_json = json.dumps(state.to_dict())

  # Later: deserialize and import
  data = json.loads(state_json)
  restored_state = DirectContextState.from_dict(data)
  new_context = DirectContext.import_state(restored_state)
  ```
</CodeGroup>

### FileSystemContextOptions (TypeScript) / Keyword Arguments (Python)

Options for FileSystem Context.

<CodeGroup>
  ```typescript TypeScript theme={null}
  interface FileSystemContextOptions {
    directory: string;      // Path to the workspace directory to index
    auggiePath?: string;    // Path to auggie executable (default: "auggie")
    debug?: boolean;        // Enable debug logging (default: false)
  }
  ```

  ```python Python theme={null}
  # In Python, these are passed as arguments to create():
  FileSystemContext.create(
      directory: str,                    # Path to the workspace directory to index
      auggie_path: str = "auggie",       # Path to auggie executable (default: "auggie")
      debug: bool = False,               # Enable debug logging (default: False)
  )
  ```
</CodeGroup>

***

## Authentication

The SDK automatically loads credentials from multiple sources in this priority order:

1. **Options/keyword arguments**: `apiKey`/`api_key` and `apiUrl`/`api_url` passed to `DirectContext.create()`
2. **Environment variables**: `AUGMENT_API_TOKEN` and `AUGMENT_API_URL`
3. **Session file**: `~/.augment/session.json` (created by `auggie login`)

**To get credentials:**

1. Sign in to Augment using the CLI: `auggie login`
2. Your credentials will be stored in `~/.augment/session.json`
3. The SDK will automatically use them

***

## Error Handling

The SDK exports specific error classes for better error handling:

| Error Class         | Description                                                    |
| ------------------- | -------------------------------------------------------------- |
| `BlobTooLargeError` | File exceeds 1MB limit. Includes `path` and `size` properties. |
| `APIError`          | Network or API request failures. Includes `status` property.   |

<CodeGroup>
  ```typescript TypeScript theme={null}
  import { DirectContext, APIError, BlobTooLargeError } from '@augmentcode/auggie-sdk';

  try {
    const context = await DirectContext.create();
    await context.addToIndex([
      { path: 'test.ts', contents: '...' }
    ]);
    const results = await context.search('query');
  } catch (error) {
    if (error instanceof BlobTooLargeError) {
      console.error('File too large (max 1MB):', error.path);
    } else if (error instanceof APIError) {
      console.error('API request failed:', error.message);
      console.error('Status code:', error.status);
    } else if (error.message.includes('API key is required')) {
      console.error('Missing credentials');
    } else if (error.message.includes('Index not initialized')) {
      console.error('No files indexed yet');
    } else {
      console.error('Operation failed:', error);
    }
  }
  ```

  ```python Python theme={null}
  from auggie_sdk.context import DirectContext, File, APIError, BlobTooLargeError

  try:
      context = DirectContext.create()
      context.add_to_index([
          File(path='test.py', contents='...')
      ])
      results = context.search('query')
  except BlobTooLargeError as error:
      print('File too large (max 1MB):', error)
  except APIError as error:
      print('API request failed:', error)
  except ValueError as error:
      if 'API key is required' in str(error):
          print('Missing credentials')
      elif 'Index not initialized' in str(error):
          print('No files indexed yet')
      else:
          print('Operation failed:', error)
  except Exception as error:
      print('Operation failed:', error)
  ```
</CodeGroup>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.augmentcode.com/llms.txt