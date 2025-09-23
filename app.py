from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import os
from receiptCheckingAI import mainFunction

app = Flask(__name__)
CORS(app)

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["myfile"]
    filename = file.filename
    file_bytes = file.read()
    print(mainFunction(file_bytes),flush=True)
    # save_path = os.path.join("uploads", filename)
    # file.save(save_path)
    
    name, ext = os.path.splitext(filename)
    
    return send_file(
        "receipt.xlsx",
        as_attachment=True,
        download_name=name+".xlsx"
    )

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
