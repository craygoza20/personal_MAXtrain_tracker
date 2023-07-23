import os

app_id = os.environ.get("TRANSIT_TRACKER_API_KEY")

if __name__ == '__main__':
    if app_id != None:
        # Use the API key in your script
        print("Your secret API key is:", app_id)
    else:
        print("API key not found. Make sure you set the SECRET_API_KEY environment variable.")
