import requests

def get_nearby_hospitals(lat, lng):

    query = f"""
    [out:json];
    (
        node["amenity"="hospital"](around:5000,{lat},{lng})
    );
    out body;
    """

    response = requests.post(
        "https://overpass-api.de/api/interpreter",
        data=query,
        headers={
            "Content-Type": "text/plain"
        }
    )
    
    # data = response.json()
    print("STATUS:", response.status_code)
    data = response.json()
    hospitals = []
    
    for item in data.get("elements", [])[:5]:

        hospitals.append({
            "name": item.get("tags", {}).get(
                "name",
                "Unknown Hospital"
            ),
            "latitude": item.get("lat"),
            "longitude": item.get("lon")
        })

    return hospitals