#สร้างเครื่องคิดเลข
from flask import Flask, request, jsonify 
app = Flask(__name__)
@app.route('/add', methods=['GET'])
def add():
    try:
        # รับค่าจาก query string
        a = request.args.get('a', type=float)
        b = request.args.get('b', type=float)
        
        # ตรวจสอบว่าค่าที่รับมามีหรือไม่
        if a is None or b is None:
            return jsonify({"error": "Missing parameters"}), 400
        
        # คำนวณผลลัพธ์
        result = a + b
        
        # ส่งผลลัพธ์กลับ
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500