from mcp.server.fastmcp import FastMCP
import httpx

mcp = FastMCP("Weather Server")

NWS_API_BASE = "https://api.weather.gov"
USER_AGENT = "weather-mcp-demo/1.0"

async def make_nws_request(url: str) -> dict:
    """Helper to make NWS API requests"""
    headers = {"User-Agent": USER_AGENT}
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers, timeout=30.0)
        response.raise_for_status()
        return response.json()

@mcp.tool()
async def get_forecast(latitude: float, longitude: float) -> str:
    """
    Get weather forecast for a location.

    Args:
        latitude: Latitude of the location
        longitude: Longitude of the location
    """
    # Get forecast URL
    points_url = f"{NWS_API_BASE}/points/{latitude},{longitude}"
    points_data = await make_nws_request(points_url)

    # Get detailed forecast
    forecast_url = points_data["properties"]["forecast"]
    forecast_data = await make_nws_request(forecast_url)

    # Format response
    periods = forecast_data["properties"]["periods"]
    forecasts = []
    for period in periods[:5]:  # Next 5 periods
        forecast = f"""{period['name']}:
Temperature: {period['temperature']}°{period['temperatureUnit']}
Wind: {period['windSpeed']} {period['windDirection']}
Forecast: {period['detailedForecast']}"""
        forecasts.append(forecast)

    return "\n---\n".join(forecasts)

@mcp.tool()
async def get_alerts(state: str) -> str:
    """
    Get weather alerts for a US state.

    Args:
        state: Two-letter US state code (e.g. CA, NY)
    """
    url = f"{NWS_API_BASE}/alerts/active/area/{state}"
    data = await make_nws_request(url)

    if not data.get("features"):
        return "No active alerts for this state."

    alerts = []
    for feature in data["features"]:
        props = feature["properties"]
        alert = f"""Event: {props['event']}
Area: {props['areaDesc']}
Severity: {props['severity']}
Description: {props['description'][:200]}..."""
        alerts.append(alert)

    return "\n---\n".join(alerts[:3])  # Limit to 3 alerts

@mcp.resource("config://settings")
def get_config() -> str:
    """Get server configuration"""
    return "Weather API v1.0 - National Weather Service"

if __name__ == "__main__":
    mcp.run()
