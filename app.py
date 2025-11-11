from flask import Flask, jsonify
import platform
import psutil
import os
import json

app = Flask (__name__)

nome = "Alana Queiroz"

@app.route('/info')
def info():
    return f"Nome: {nome}"

@app.route('/metricas')
def metricas():
    pid = os.getpid()
    memoria_mb = psutil.virtual_memory().used // 1024 ** 2
    cpu = psutil.cpu_percent()
    so = platform.platform()

    dados = {
        'Nome': nome,
        'PID': pid, 
        'Memoria vsada(MB)': memoria_mb,
        'Uso CPU': cpu,
        'Sistema Operacional': so
    }

    return jsonify(dados)

if __name__ == '__main__':
    app.run(host= '0.0.0.0', port= int(os.environ.get("PORT", 500)))
# Obtém versão do S.O. subjacente
#print(platform.platform())

# Obtém PID
#print(os.getpid())

# Obtém uso de CPU (%)
#print(psutil.cpu_percent())

# Obtém uso de memória (MB)
#print(psutil.virtual_memory().used // 1024 ** 2)


#metricas = {
#    'so': platform.platform(),
#    'pid': os.getpid(),
#    'uso_cpu': psutil.cpu_percent(),
#    'memoria_mb': psutil.virtual_memory().used // 1024 ** 2
#}

#print(json.dumps(metricas, ensure_ascii=False))