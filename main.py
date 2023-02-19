from flask import Flask, request, jsonify
from marketdata import item_data, get_hashname

app = Flask(__name__)

@app.route('/api/weapon', methods=['POST'])
def get_item_data():
  gun = request.json['gun']
  skin = request.json['skin']
  wear = request.json['wear']
  stat = request.json['stat']
  hashname = get_hashname(gun, skin, wear, stat)
  try:
      data = item_data(hashname)
      return jsonify(data)
  except:
      return jsonify({"error": "Item data not available"})

@app.route('/api/case', methods=['POST'])
def get_case_data():
  case = request.json['case']
  hashname = case.replace(' ', '%20')
  try:
      data = item_data(hashname)
      return jsonify(data)
  except:
      return jsonify({"error": "Item data not available"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
