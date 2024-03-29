import requests

api_url = "https://api.spacexdata.com/v5/launches/latest"
    
try:
    response = requests.get(api_url)

    launch_info = response.json()

    name = launch_info["name"]
    date_utc = launch_info["date_utc"]
    success = launch_info["success"]
    details = launch_info["details"]
    webcast = launch_info["links"]["webcast"]

    print("\nLatest SpaceX Launch Information:")
    print(f"Mission Name: {name}")
    print(f"Launch Date (UTC): {date_utc}")
    print(f"Launch Success: {'Yes' if success else 'No'}")
    print(f"Details: {details}")
    print(f"Watch the webcast: {webcast}")

except:
    print("Failed to retrieve launch information. Please try again later.")
