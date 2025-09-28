import requests
import json
import csv

# Overview: This script is used to query the MITRE STIX endpoint for the latest threats and IOCs to enterprises.
    # The output after being sorted is written to a CSV in the current working directory. 
    # This data can be used to upload to Splunk (or any SIEM solution) for dashboard enhancement.

# The MITRE STIX endpoint is queried and the JSON data is returned to continue the method
def fetch_stix_data(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        returned_data = response.json()
        return returned_data
    except requests.RequestException as e:
        print (f"Error fetching data {e}")

# The queried data is validated to not be NONE and parsed to only return the values from the keys type, name, and description
def extract_keys(stix_stuff):
    # print(f"--- STIX STUFF --- {stix_stuff}")
    if not stix_stuff:
        print("No valid STIX info")
        return None
    else:
        # print(f"stix stuff = {stix_stuff}")
        results = []
        for object in stix_stuff.get("objects", []):
            # print("Working before type")
            if object.get("type"):
                # print("working after type")
                result = {
                    "type": object.get("type", "N/A"),
                    "name": object.get("name", "N/A"),
                    "description": object.get("description", "N/A")
                }
                results.append(result)
        return results

# The parsed data is validated to not be NONE and written to a CSV
def write_to_csv(filtered_stix_data, filename="stix_output.csv"):
    if not filtered_stix_data:
        print("No filtered data found")
        return
    try:
        with open(filename, "w", newline="", encoding="utf-8") as f:
            # print("success")
            writer = csv.DictWriter(f, fieldnames=["type", "name", "description"])
            writer.writeheader()
            # print("wrote headers")
            writer.writerows(filtered_stix_data)
            # print("wrote rows")
            print(f"Done writing data to {filename}")
    except PermissionError:
        print(f"Permission error writing to {filename}")
    except Exception as e:
        print(f"Exception error writing to {filename}")
        print(f"Error code: {e}")

def main():
    # fetch_stix_data --> runs a requests for STIX JSON. If results isn't NONE then the extract_keys function runs with the returned data as an argument.
    # extract_keys --> checks if the data is valid. If so it parses it to place into a CSV file. Then returns the parsed data to continue the method.
    # write_to_csv --> parsed data is validated and written to a CSV in the current working directory
    url = "https://raw.githubusercontent.com/mitre/cti/master/enterprise-attack/enterprise-attack.json"
    fetch_stix_data(url)

    stix_data = fetch_stix_data(url)
    if stix_data:
        extract = extract_keys(stix_data)
        if extract:
            written_to_csv = write_to_csv(extract)

if __name__ == "__main__":
    main()


# Example stix_data content
stix_data = {
    "type": "bundle",
    "id": "bundle--123",
    "objects": [
        {"type": "indicator", "name": "Malicious IP", "description": "C2 server IP"},
        {"type": "attack-pattern", "name": "Phishing", "description": "Spearphishing attack"}
    ]
}