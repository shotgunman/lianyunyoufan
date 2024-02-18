from flask import Flask, request, jsonify
from flask_cors import CORS
import route
app = Flask(__name__)
CORS(app)

# @app.route('/process', methods=['POST'])
# def process_data():
#     data = request.json
#     address = data.get('address', '')
#     city = data.get('city', '')
#     processed_data = f"Address: {address}, City: {city}"
#     return jsonify({'result': processed_data})


# 转换为导航格式
def process_list(original_list):
    # 至少要有两个元素
    if len(original_list) < 2:
        raise ValueError("原始列表至少需要两个元素")

    sted = [original_list[0], original_list[-1]]
    waypoints = original_list[1:-1] if len(original_list) > 2 else []
    opts = {'waypoints': waypoints}

    return sted, opts


@app.route('/get_data', methods=['GET'])
def get_new_points():
    # 或许可以新增一个可选参数已有的geocode，减少地理编码api使用。(用户修改destination时存储本地地理编码)
    # 传入points

    # points = [
    # {'address': '北京市朝阳区阜通东大街6号', 'city': '北京'},
    # {'address': '东方明珠', 'city': '上海'},
    # ]
    # geolist = geocode.get_geo_list(points)
    # shortest_path, min_distance = route.find_shortest_path(geolist)
    # sted, opts = process_list(shortest_path)

    # test case
    shortest_path, min_distance = route.find_shortest_path([[116.4074, 39.9042], [116.232633, 40.051922], [116.266965, 39.623799], [116.717405, 39.841358]])
    # shortest_path = [[116.4074, 39.9042], [116.232633,40.051922], [116.266965,39.623799], [116.717405,39.841358],
    # [115.864591,40.10026], [116.532364,38.858118], [118.509903,36.06821], [120.004044,36.387255], [120.597306,
    # 32.02812]]

    # print(shortest_path)
    sted, opts = process_list(shortest_path)

    # print("sted:", sted)
    # print("opts:", opts)
    # print(geolist)

    return jsonify({"sted": sted, "opts": opts})

@app.route('/receive_data', methods=['POST'])
def receive_data():
    data = request.json
    print(data)

    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)
