# Source: https://novita.ai/docs/api-reference/reference-unified-video-generation.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Unified Video Generation API

export const UnifiedAPI = () => {
  if (typeof document === "undefined") {
    return null;
  }
  const [config, setConfig] = useState(window.novitaRemoteData?.videoUnifyAPIConfig?.data || null);
  const [chosenIndex, setChosenIndex] = useState(0);
  const [isOpen, setIsOpen] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const [searchTerm, setSearchTerm] = useState("");
  useEffect(() => {
    if (!window.novitaRemoteData?.videoUnifyAPIConfig?.data) {
      setIsLoading(true);
      fetch('https://api.novita.ai/v3/admin/video-unify-api/config').then(response => {
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        return response.json();
      }).then(data => {
        setConfig(data.configs);
      }).catch(error => {
        console.error('Failed to fetch config:', error);
      }).finally(() => {
        setIsLoading(false);
      });
    }
  }, []);
  const data = useMemo(() => {
    return config?.[chosenIndex];
  }, [config, chosenIndex]);
  useEffect(() => {
    const handleClickOutside = event => {
      if (isOpen && !event.target.closest(".unified-api-selector-container")) {
        setIsOpen(false);
        setSearchTerm("");
      }
    };
    document.addEventListener("mousedown", handleClickOutside);
    return () => {
      document.removeEventListener("mousedown", handleClickOutside);
    };
  }, [isOpen]);
  const filteredConfig = useMemo(() => {
    if (!config || !searchTerm.trim()) {
      return config || [];
    }
    const term = searchTerm.toLowerCase();
    return config.filter(item => {
      const model = (item.model || '').toLowerCase();
      const description = (item.description || '').toLowerCase();
      return model.includes(term) || description.includes(term);
    });
  }, [config, searchTerm]);
  const modelSelector = useMemo(() => {
    if (!config || config.length <= 1) {
      return null;
    }
    const selectedModel = config[chosenIndex]?.model || '-';
    return <div className="unified-api-selector-container">
        <label className="unified-api-selector-label">Model</label>
        <div className="unified-api-selector-wrapper">
          <button type="button" onClick={() => setIsOpen(!isOpen)} className="unified-api-selector-button">
            <span>{selectedModel}</span>
            <svg width="16" height="16" viewBox="0 0 20 20" fill="none" className={`unified-api-selector-arrow ${isOpen ? "open" : ""}`}>
              <path stroke="#6b7280" strokeLinecap="round" strokeLinejoin="round" strokeWidth="1.5" d="m6 8 4 4 4-4" />
            </svg>
          </button>
          {isOpen && <div className="unified-api-selector-dropdown">
              <div className="unified-api-search-container">
                <input type="text" placeholder="Search model..." value={searchTerm} onChange={e => setSearchTerm(e.target.value)} className="unified-api-search-input" onClick={e => e.stopPropagation()} />
              </div>
              <div className="unified-api-options-container">
                {filteredConfig.length > 0 ? filteredConfig.map((item, filteredIndex) => {
      const originalIndex = config.findIndex(configItem => configItem === item);
      return <div key={originalIndex} onClick={() => {
        setChosenIndex(originalIndex);
        setIsOpen(false);
        setSearchTerm("");
      }} className={`unified-api-selector-option ${originalIndex === chosenIndex ? "selected" : ""}`}>
                        {item.model || '-'}
                      </div>;
    }) : <div className="unified-api-no-results">
                    No matching model found
                  </div>}
              </div>
            </div>}
        </div>
      </div>;
  }, [config, chosenIndex, isOpen, searchTerm, filteredConfig]);
  const headerFields = useMemo(() => {
    return <>
        <h2>Request Headers</h2>
        <ParamField header="Content-Type" type="string" required={true}>
          Enum: <span className="unified-api-inline-label">application/json</span>
        </ParamField>
        <ParamField header="Authorization" type="string" required={true}>
          Bearer authentication format: Bearer {`{{API Key}}`}.
        </ParamField>
      </>;
  }, []);
  const requestBodyFields = useMemo(() => {
    if (!data?.json_schema) {
      return null;
    }
    const schema = JSON.parse(data.json_schema);
    const getFields = () => {
      return Object.entries(schema.properties).filter(([key, value]) => key !== "model").map(([key, value]) => ({
        name: key,
        ...value
      }));
    };
    const getFieldInfo = fieldName => {
      const field = schema.properties[fieldName];
      if (!field) return {
        type: "string",
        required: false
      };
      return {
        type: field.type || "string",
        required: schema.required?.includes(fieldName) || false,
        description: field.description,
        enum: field.enum,
        default: field.default,
        minLength: field.minLength,
        maxLength: field.maxLength,
        minimum: field.minimum,
        maximum: field.maximum,
        maxItems: field.maxItems,
        items: field.items
      };
    };
    const renderFieldConstraints = fieldInfo => {
      return <>
          {fieldInfo.maxItems !== undefined && <p>
              Max items:{" "}
              <span className="unified-api-inline-label">
                {fieldInfo.maxItems}
              </span>
            </p>}
          {(fieldInfo.minLength || fieldInfo.maxLength) && <p>
              {fieldInfo.minLength !== undefined && <>
                  Min length:{" "}
                  <span className="unified-api-inline-label">
                    {fieldInfo.minLength}
                  </span>
                </>}
              {fieldInfo.minLength !== undefined && fieldInfo.maxLength && ", "}
              {fieldInfo.maxLength && <>
                  Max length:{" "}
                  <span className="unified-api-inline-label">
                    {fieldInfo.maxLength}
                  </span>
                </>}
              .
            </p>}
          {(fieldInfo.minimum !== undefined || fieldInfo.maximum !== undefined) && <p>
              {fieldInfo.minimum !== undefined && <>
                  Min value:{" "}
                  <span className="unified-api-inline-label">
                    {fieldInfo.minimum}
                  </span>
                </>}
              {fieldInfo.minimum !== undefined && fieldInfo.maximum !== undefined && ", "}
              {fieldInfo.maximum !== undefined && <>
                  Max value:{" "}
                  <span className="unified-api-inline-label">
                    {fieldInfo.maximum}
                  </span>
                </>}
              .
            </p>}
          {(fieldInfo.enum || fieldInfo.default !== undefined) && <p>
              {fieldInfo.enum && <>
                  Enum values:{" "}
                  {fieldInfo.enum.map((value, index) => <span key={index}>
                      <span className="unified-api-inline-label">
                        {value}
                      </span>
                      {index < fieldInfo.enum.length - 1 && ", "}
                    </span>)}
                </>}
              {fieldInfo.enum && fieldInfo.default !== undefined && ". "}
              {fieldInfo.default !== undefined && <>
                  Default:{" "}
                  <span className="unified-api-inline-label">
                    {typeof fieldInfo.default === 'boolean' ? fieldInfo.default ? 'true' : 'false' : fieldInfo.default}
                  </span>
                </>}
              .
            </p>}
        </>;
    };
    return <>
        {data?.model && <ParamField body="model" type="string" required={true}>
            Supported model:
            <span className="unified-api-inline-label">{data.model}</span>
          </ParamField>}
        {getFields().map(field => {
      const fieldInfo = getFieldInfo(field.name);
      return <ParamField key={field.name} body={field.name} type={fieldInfo.type} required={fieldInfo.required} default={fieldInfo.default}>
              <p>{fieldInfo.description}</p>
              {renderFieldConstraints(fieldInfo)}
              {fieldInfo.items && fieldInfo.items.properties && <Expandable title="properties" defaultOpen={false}>
                  {Object.entries(fieldInfo.items.properties).map(([propName, propInfo]) => <ParamField key={propName} body={propName} type={propInfo.type} required={fieldInfo.items.required?.includes(propName) || false}>
                      <p>{propInfo.description}</p>
                      {renderFieldConstraints(propInfo)}
                    </ParamField>)}
                </Expandable>}
            </ParamField>;
    })}
      </>;
  }, [data]);
  const LoadingSpinner = useMemo(() => <div className="unified-api-loading-container">
      <div className="unified-api-loading-spinner"></div>
      <p className="unified-api-loading-text">Loading...</p>
    </div>, []);
  return <div className="unified-api-container">
      <p>
        This API provides a unified interface for video generation across multiple vendors, extracting common request and response fields, standardizing parameters and data formats, simplifying the invocation process, and improving integration and usage efficiency.
      </p>
      {modelSelector}
      {data?.description && <>
          <p>Model description:</p>
          <p className="unified-api-description">{data.description}</p>
        </>}
      {headerFields}
      <h2>Request Body</h2>
      {!isLoading && <ParamField body="callback_url" type="string">
          Webhook callback URL. When video generation is completed, the system will send a POST request to this URL with the callback data format shown below:

          <p className="unified-api-code">{`{
              event_type: "ASYNC_TASK_RESULT",
              payload: TaskResultResponse
             }`}
          </p>

          See <a href="/api-reference/model-apis-task-result">Task Result Query API</a> for details on the <code>TaskResultResponse</code> object.<br /><br />
          Example: https://your-callback-url.com/callback
        </ParamField>}
      {isLoading ? LoadingSpinner : requestBodyFields}
      <h2>Response</h2>
      <ResponseField name="task_id" type="string" required={true}>
        The asynchronous task <code>task_id</code>. You should use this <code>task_id</code> to call{" "}
        <a href="/api-reference/model-apis-task-result">
          the task result query API
        </a>{" "}
        to obtain the generation result.
      </ResponseField>
    </div>;
};

<UnifiedAPI />


Built with [Mintlify](https://mintlify.com).