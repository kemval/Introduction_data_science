import requests
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib.dates import DateFormatter

# NASA API Endpoint for NEO
api_url = "api.nasa.gov"
api_path = "/neo/rest/v1/feed"

# Your NASA API key
api_key = "ha5zBXwbYurJy4apeQrd483YGiAGbpqnd2WbSt2j"

# Set up parameters for the initial API request
start_date = "2023-01-01"
end_date = "2023-01-07"

# Maximum number of redirects to follow
max_redirects = 10
redirect_count = 0

while redirect_count < max_redirects:
    # Build the request URL
    url = f"https://{api_url}{api_path}?start_date={start_date}&end_date={end_date}&api_key={api_key}"

    # Make the request with SSL certificate verification disabled
    response = requests.get(url, verify=False)

    # Check for successful response
    if response.status_code == 200:
        break
    elif response.status_code == 302:
        if response.headers.get('Location'):
            # If there's a redirect, update the URL and increment the redirect count
            api_url, api_path = response.headers['Location'].split(api_url, 1)
            redirect_count += 1
        else:
            print("Redirect received but no 'Location' header found.")
            break
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        break

# Check if the loop was terminated due to too many redirects
if redirect_count >= max_redirects:
    print("Exceeded maximum number of redirects.")
else:
    # Decode the response and process the data
    neo_data = response.json()

    # Extracting NEO counts and dates
    dates = [datetime.strptime(date, "%Y-%m-%d") for date in neo_data["near_earth_objects"].keys()]
    neo_counts = [len(neos) for neos in neo_data["near_earth_objects"].values()]

    # Plotting the line chart
    fig, ax = plt.subplots()
    ax.plot(dates, neo_counts, label="Number of NEOs")
    ax.xaxis.set_major_formatter(DateFormatter("%Y-%m-%d"))
    plt.title("NEO Monitoring Over Time")
    plt.xlabel("Date")
    plt.ylabel("Number of NEOs")
    plt.legend()
    plt.show()
