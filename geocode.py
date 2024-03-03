import requests

def get_geocode(data):
    url = "https://restapi.amap.com/v3/geocode/geo"
    key = ("0975e803904c4538ede7c07e7c9acf02")
    address = data.get('address')
    city = data.get('city')

    params = {
        'key': key,
        'address': address,
        'city': city,
        'output': 'JSON'
    }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        if data['status'] == '1' and data['count'] != '0':
            # 提取第一个结果的经纬度，并以列表形式返回
            location_str = data['geocodes'][0]['location']
            location = [float(coord) for coord in location_str.split(',')]
            return location
        else:
            return None
    else:
        return None


def get_geo_list(data_list):
    geocode_results = []

    for data in data_list:
        location = get_geocode(data)
        geocode_results.append(location)
        if not location:
            geocode_results.append(data)
            geocode_results.append("地理编码获取失败")

    return geocode_results


# data_list = [
#     {'address': '北京市朝阳区阜通东大街6号', 'city': '北京'},
#     {'address': '东方明珠', 'city': '上海'},
# ]
#
# results = get_geo_list(data_list)
# print("所有地理编码结果：", results)
