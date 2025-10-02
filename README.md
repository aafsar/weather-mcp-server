# Weather MCP Server

A Model Context Protocol (MCP) server that provides real-time weather forecasts and alerts for the United States using the National Weather Service API.

## Features

- **Weather Forecasts**: Get detailed 5-period weather forecasts for any US location using latitude/longitude coordinates
- **Weather Alerts**: Retrieve active weather alerts for any US state
- **No API Key Required**: Uses the free National Weather Service API
- **Fast & Reliable**: Built with FastMCP and deployed on FastMCP Cloud
- **Easy Integration**: Works with any MCP-compatible client (Claude Desktop, ChatGPT, etc.)

## Live Demo

**Server URL**: `https://weather-mcp-server.fastmcp.app/mcp`

## Tools

### `get_forecast`

Get weather forecast for a specific location.

**Parameters:**
- `latitude` (float): Latitude of the location
- `longitude` (float): Longitude of the location

**Example:**
```
latitude: 40.7128
longitude: -74.0060
```
Returns a detailed 5-period forecast including temperature, wind conditions, and detailed descriptions.

### `get_alerts`

Get active weather alerts for a US state.

**Parameters:**
- `state` (string): Two-letter US state code (e.g., "CA", "NY", "TX")

**Example:**
```
state: CA
```
Returns up to 3 active weather alerts with event type, affected areas, severity, and descriptions.

## Resources

### `config://settings`

Returns server configuration information.

## Usage

### With Claude Desktop

1. Add to your Claude Desktop config file:
   - **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "weather": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://weather-mcp-server.fastmcp.app/mcp"
      ]
    }
  }
}
```

2. Restart Claude Desktop (Command+R on Mac, Ctrl+R on Windows)

3. Look for the hammer icon in the input box to verify the server is connected

4. Try asking: *"What's the weather forecast for New York City?"*

### Example Queries

- "Get the weather forecast for Los Angeles?"
- "Are there any weather alerts for California?"
- "What's the forecast for coordinates 41.8781, -87.6298?" (Chicago)
- "Check weather alerts for Texas"

## Development

### Prerequisites

- Python 3.8+
- [uv](https://github.com/astral-sh/uv) package manager

### Local Setup

1. Clone the repository:
```bash
git clone https://github.com/aafsar/weather-mcp-server.git
cd weather-mcp-server
```

2. Initialize environment:
```bash
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
uv add "mcp[cli]"
uv add httpx
```

4. Run the server locally:
```bash
uv run mcp dev server.py
```

The MCP Inspector will open in your browser for testing.

### Project Structure

```
weather-mcp-server/
├── server.py           # Main MCP server implementation
├── requirements.txt    # Python dependencies
├── pyproject.toml      # uv project configuration
└── README.md          # This file
```

### Technologies Used

- **[FastMCP](https://github.com/jlowin/fastmcp)**: Lightweight framework for building MCP servers
- **[httpx](https://www.python-httpx.org/)**: Modern async HTTP client
- **[National Weather Service API](https://www.weather.gov/documentation/services-web-api)**: Free weather data source

## API Credits

Weather data provided by the [National Weather Service](https://www.weather.gov/), a service of the National Oceanic and Atmospheric Administration (NOAA).

## License

MIT License - feel free to use this server in your own projects!

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## Links

- **Live Server**: https://weather-mcp-server.fastmcp.app/mcp
- **GitHub Repository**: https://github.com/aafsar/weather-mcp-server
- **MCP Documentation**: https://modelcontextprotocol.io/
- **FastMCP**: https://github.com/jlowin/fastmcp

---

Built with the Model Context Protocol
