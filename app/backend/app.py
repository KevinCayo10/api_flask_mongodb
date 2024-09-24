from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route("/")
def index():
  return "Hello World!"

# @app.route("/artefacta",methods=["POST"])
# def scrape():
#   params = request.json
#   process = subprocess.Popen(['python', 'mi_script_de_scraping.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

#     # Retorna inmediatamente una respuesta sin esperar a que el scraping termine
#   return jsonify({"status": "Scraping iniciado en segundo plano", "pid": process.pid})

  

if __name__=='__main__':
  app.run(debug=True)
  