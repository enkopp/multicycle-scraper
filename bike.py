import xml.etree.ElementTree as ET
import requests

def get_branch_availability(sku):
    url = 'https://multicycle.de/wp-admin/admin-ajax.php'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Origin': 'https://multicycle.de'    
    }

    data = {
        'action': 'get_branch_availability',
        'product_sku': sku,
        'nonce': '3ad3c02a28'
    }

    response = requests.post(url, headers=headers, data=data)
    result = response.json()
    
    # Wrap HTML content in a root element to make it XML-compliant
    xml_content = f"<root>{result['data'].replace('<br>', '')}</root>"

    # Parse the content 
    root = ET.fromstring(xml_content)

    # Extract city names 
    city_names = [a.text for a in root.findall(".//span[@class='branch-name']/a")]

    return city_names  

bikes = {
    "900002945": "S white", 
    "900002944": "M white",
    "900002949": "S blue",
    "900002948": "M blue"
}

for (sku, name) in bikes.items():
    print(f"{name}: {', '.join(get_branch_availability(sku))}")
