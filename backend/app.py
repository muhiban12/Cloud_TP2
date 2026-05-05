import os
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# =====================================================================
# DILARANG MENGUBAH ATAU MENG-HARDCODE BAGIAN INI!
# =====================================================================
nama_owner = os.environ.get('NAMA_PRAKTIKAN', 'Misterius')
nim_owner = os.environ.get('NIM_PRAKTIKAN', '00000000')

# =====================================================================
# TEMA: KATALOG GADGET & TEKNOLOGI
# =====================================================================
katalog_data = {
    "judul_katalog": f"Tech Inventory - {nama_owner}",
    "pemilik": nama_owner,
    "nim": nim_owner,
    "items": [
        {"name": "MacBook Pro M3", "specs": "32GB RAM, 1TB SSD"},
        {"name": "RTX 4090 GPU", "specs": "24GB VRAM"},
        {"name": "Keychron Q1", "specs": "Custom Mechanical Keyboard"}
    ]
}

@app.route('/api/info', methods=['GET']) 
def get_info():
    return jsonify(katalog_data)

@app.route('/api/add-item', methods=['POST']) 
def add_item():
    new_item = request.json.get('item') 
    if new_item:
        katalog_data["items"].append({"name": new_item, "specs": "Added via API"})
        return jsonify({"message": "Item berhasil ditambahkan!", "items": katalog_data["items"]}), 201
    return jsonify({"error": "Data tidak valid"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)