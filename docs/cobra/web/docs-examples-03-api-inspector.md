# Source: https://cobra.dev/docs/examples/03-api-inspector/

Title: API Inspector CLI

URL Source: https://cobra.dev/docs/examples/03-api-inspector/

Markdown Content:
```
package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"os"
	"path/filepath"
	"strings"
	"time"

	"github.com/spf13/cobra"
	"github.com/spf13/viper"
	"gopkg.in/yaml.v2"
)

type RequestConfig struct {
	Method      string            `json:"method"`
	URL         string            `json:"url"`
	Headers     map[string]string `json:"headers"`
	Body        string            `json:"body,omitempty"`
	Timeout     int               `json:"timeout"`
	OutputFormat string           `json:"output_format"`
}

type ResponseData struct {
	Status     string                 `json:"status"`
	StatusCode int                    `json:"status_code"`  
	Headers    map[string][]string    `json:"headers"`
	Body       interface{}            `json:"body"`
	Timestamp  time.Time             `json:"timestamp"`
	Duration   time.Duration         `json:"duration"`
}

var (
	method       string
	headers      []string
	body         string
	timeout      int
	outputFormat string
	saveResponse string
	configFile   string
	client       *http.Client
)

var rootCmd = &cobra.Command{
	Use:   "apispy [url]",
	Short: "A modern API inspection tool",
	Long: `apispy is a CLI tool for inspecting APIs and HTTP services.

Make requests, format responses, and save data for analysis.
Supports multiple output formats and extensive configuration.`,
	Args: cobra.MaximumNArgs(1),
	Run:  makeRequest,
	PersistentPreRun: setupClient,
}

var getCmd = &cobra.Command{
	Use:   "get [url]",
	Short: "Make a GET request",
	Args:  cobra.ExactArgs(1), 
	Run:   func(cmd *cobra.Command, args []string) {
		method = "GET"
		makeRequest(cmd, args)
	},
}

var postCmd = &cobra.Command{
	Use:   "post [url]",
	Short: "Make a POST request",
	Args:  cobra.ExactArgs(1),
	Run:   func(cmd *cobra.Command, args []string) {
		method = "POST"
		makeRequest(cmd, args)
	},
}

var saveCmd = &cobra.Command{
	Use:   "save [name] [url]",
	Short: "Save a request configuration",
	Args:  cobra.ExactArgs(2),
	Run:   saveRequestConfig,
}

var loadCmd = &cobra.Command{
	Use:   "load [name]", 
	Short: "Load and execute a saved request",
	Args:  cobra.ExactArgs(1),
	Run:   loadRequestConfig,
}

func init() {
	// Global flags
	rootCmd.PersistentFlags().StringVarP(&method, "method", "X", "GET", "HTTP method")
	rootCmd.PersistentFlags().StringSliceVarP(&headers, "header", "H", []string{}, "HTTP headers (key:value)")
	rootCmd.PersistentFlags().StringVarP(&body, "data", "d", "", "Request body data")
	rootCmd.PersistentFlags().IntVar(&timeout, "timeout", 30, "Request timeout in seconds")
	rootCmd.PersistentFlags().StringVarP(&outputFormat, "output", "o", "json", "Output format (json, yaml, table)")
	rootCmd.PersistentFlags().StringVar(&saveResponse, "save", "", "Save response to file")
	rootCmd.PersistentFlags().StringVar(&configFile, "config", "", "Config file (default is $HOME/.apispy.yaml)")

	// POST-specific flags
	postCmd.Flags().StringVarP(&body, "data", "d", "", "POST body data")

	// Add subcommands
	rootCmd.AddCommand(getCmd, postCmd, saveCmd, loadCmd)
	
	// Setup configuration
	setupConfig()
}

func setupConfig() {
	if configFile != "" {
		viper.SetConfigFile(configFile)
	} else {
		home, _ := os.UserHomeDir()
		viper.AddConfigPath(home)
		viper.SetConfigName(".apispy")
		viper.SetConfigType("yaml")
	}
	
	// Set defaults
	viper.SetDefault("timeout", 30)
	viper.SetDefault("output_format", "json")
	viper.SetDefault("headers", map[string]string{
		"User-Agent": "apispy/1.0",
	})
	
	// Environment variables
	viper.SetEnvPrefix("APISPY")
	viper.AutomaticEnv()
	
	// Read config file
	viper.ReadInConfig()
}

func setupClient(cmd *cobra.Command, args []string) {
	timeoutDuration := time.Duration(viper.GetInt("timeout")) * time.Second
	client = &http.Client{
		Timeout: timeoutDuration,
	}
}

func parseHeaders(headerSlice []string) map[string]string {
	headers := make(map[string]string)
	
	// Add default headers from config
	defaultHeaders := viper.GetStringMapString("headers")
	for k, v := range defaultHeaders {
		headers[k] = v
	}
	
	// Add command-line headers (override defaults)
	for _, header := range headerSlice {
		parts := strings.SplitN(header, ":", 2)
		if len(parts) == 2 {
			key := strings.TrimSpace(parts[0])
			value := strings.TrimSpace(parts[1])
			headers[key] = value
		}
	}
	
	return headers
}

func makeRequest(cmd *cobra.Command, args []string) {
	if len(args) == 0 {
		fmt.Println("URL required")
		os.Exit(1)
	}
	
	url := args[0]
	
	// Create request
	var bodyReader io.Reader
	if body != "" {
		bodyReader = strings.NewReader(body)
	}
	
	req, err := http.NewRequest(method, url, bodyReader)
	if err != nil {
		fmt.Printf("Error creating request: %v\n", err)
		os.Exit(1)
	}
	
	// Set headers
	requestHeaders := parseHeaders(headers)
	for key, value := range requestHeaders {
		req.Header.Set(key, value)
	}
	
	// Make request with timing
	start := time.Now()
	resp, err := client.Do(req)
	duration := time.Since(start)
	
	if err != nil {
		fmt.Printf("Error making request: %v\n", err)
		os.Exit(1)
	}
	defer resp.Body.Close()
	
	// Read response body
	respBody, err := io.ReadAll(resp.Body)
	if err != nil {
		fmt.Printf("Error reading response: %v\n", err)
		os.Exit(1)
	}
	
	// Parse JSON if possible
	var bodyData interface{}
	if err := json.Unmarshal(respBody, &bodyData); err != nil {
		// If not JSON, store as string
		bodyData = string(respBody)
	}
	
	// Create response data
	responseData := ResponseData{
		Status:     resp.Status,
		StatusCode: resp.StatusCode,
		Headers:    resp.Header,
		Body:       bodyData,
		Timestamp:  time.Now(),
		Duration:   duration,
	}
	
	// Output response
	outputResponse(responseData)
	
	// Save response if requested
	if saveResponse != "" {
		saveResponseToFile(responseData, saveResponse)
	}
}

func outputResponse(response ResponseData) {
	switch strings.ToLower(outputFormat) {
	case "json":
		outputJSON(response)
	case "yaml":
		outputYAML(response)
	case "table":
		outputTable(response)
	default:
		fmt.Printf("Unsupported output format: %s\n", outputFormat)
		os.Exit(1)
	}
}

func outputJSON(response ResponseData) {
	jsonData, err := json.MarshalIndent(response, "", "  ")
	if err != nil {
		fmt.Printf("Error formatting JSON: %v\n", err)
		os.Exit(1)
	}
	fmt.Println(string(jsonData))
}

func outputYAML(response ResponseData) {
	yamlData, err := yaml.Marshal(response)
	if err != nil {
		fmt.Printf("Error formatting YAML: %v\n", err)
		os.Exit(1)
	}
	fmt.Print(string(yamlData))
}

func outputTable(response ResponseData) {
	fmt.Printf("Status: %s (%d)\n", response.Status, response.StatusCode)
	fmt.Printf("Duration: %v\n", response.Duration)
	fmt.Printf("Timestamp: %s\n", response.Timestamp.Format(time.RFC3339))
	fmt.Println("\nHeaders:")
	for key, values := range response.Headers {
		for _, value := range values {
			fmt.Printf("  %s: %s\n", key, value)
		}
	}
	fmt.Println("\nBody:")
	if jsonStr, err := json.MarshalIndent(response.Body, "", "  "); err == nil {
		fmt.Println(string(jsonStr))
	} else {
		fmt.Printf("%v\n", response.Body)
	}
}

func saveResponseToFile(response ResponseData, filename string) {
	jsonData, err := json.MarshalIndent(response, "", "  ")
	if err != nil {
		fmt.Printf("Error formatting response for save: %v\n", err)
		return
	}
	
	err = os.WriteFile(filename, jsonData, 0644)
	if err != nil {
		fmt.Printf("Error saving response: %v\n", err)
		return
	}
	
	fmt.Printf("Response saved to %s\n", filename)
}

func saveRequestConfig(cmd *cobra.Command, args []string) {
	name := args[0]
	url := args[1]
	
	config := RequestConfig{
		Method:       method,
		URL:          url,
		Headers:      parseHeaders(headers),
		Body:         body,
		Timeout:      timeout,
		OutputFormat: outputFormat,
	}
	
	configDir := filepath.Join(os.Getenv("HOME"), ".apispy", "requests")
	os.MkdirAll(configDir, 0755)
	
	configPath := filepath.Join(configDir, name+".json")
	jsonData, err := json.MarshalIndent(config, "", "  ")
	if err != nil {
		fmt.Printf("Error formatting config: %v\n", err)
		os.Exit(1)
	}
	
	err = os.WriteFile(configPath, jsonData, 0644)
	if err != nil {
		fmt.Printf("Error saving config: %v\n", err)
		os.Exit(1)
	}
	
	fmt.Printf("Request configuration saved as '%s'\n", name)
}

func loadRequestConfig(cmd *cobra.Command, args []string) {
	name := args[0]
	configPath := filepath.Join(os.Getenv("HOME"), ".apispy", "requests", name+".json")
	
	data, err := os.ReadFile(configPath)
	if err != nil {
		fmt.Printf("Error loading config '%s': %v\n", name, err)
		os.Exit(1)
	}
	
	var config RequestConfig
	err = json.Unmarshal(data, &config)
	if err != nil {
		fmt.Printf("Error parsing config: %v\n", err)
		os.Exit(1)
	}
	
	// Apply loaded configuration
	method = config.Method
	body = config.Body
	timeout = config.Timeout
	outputFormat = config.OutputFormat
	
	// Convert headers to slice format
	headers = []string{}
	for key, value := range config.Headers {
		headers = append(headers, fmt.Sprintf("%s: %s", key, value))
	}
	
	// Make the request
	makeRequest(cmd, []string{config.URL})
}

func main() {
	if err := rootCmd.Execute(); err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
}
```
