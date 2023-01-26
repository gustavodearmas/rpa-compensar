import requests
from bs4 import BeautifulSoup
import urllib3
urllib3.disable_warnings()

class SesionActive():
    SESSION = requests.Session()
    sedes_input_api = {
        "fin_semana_calenadarioA_av68": {"idDeporte": "544","idCiclo": "26554","idSede": "476","start": "0","limit": "100"},
        "fin_semana_calenadarioA_cajica": {"idDeporte": "544", "idCiclo": "26554", "idSede": "4", "start": "0", "limit": "100"},
        "fin_semana_calenadarioA_220": {'idDeporte': '544', 'idCiclo': '26554', 'idSede': '2', 'start': '0', 'limit': '100'},
        "fin_semana_calenadarioA_cll94": {'idDeporte': '544', 'idCiclo': '26554', 'idSede': '5', 'start': '0', 'limit': '100'},
        "fin_semana_calenadarioA_cbi_americas": {'idDeporte': '544', 'idCiclo': '26554', 'idSede': '588', 'start': '0', 'limit': '100'},
        "fin_semana_calenadarioA_cbi_autosur": {'idDeporte': '544', 'idCiclo': '26554', 'idSede': '606', 'start': '0', 'limit': '100'},
        "fin_semana_calenadarioA_cbi_142": {'idDeporte': '544', 'idCiclo': '26554', 'idSede': '610', 'start': '0', 'limit': '100'},
        "fin_semana_calenadarioA_cbi_centro_mayor": {'idDeporte': '544', 'idCiclo': '26554', 'idSede': '689', 'start': '0', 'limit': '100'},
        "fin_semana_calenadarioA_cbi_soacha": {'idDeporte': '544', 'idCiclo': '26554', 'idSede': '607', 'start': '0', 'limit': '100'},
        "fin_semana_calenadarioA_cbi_zona_franca": {'idDeporte': '544', 'idCiclo': '26554', 'idSede': '609', 'start': '0', 'limit': '100'},
        "fin_semana_calenadarioA_cef": {'idDeporte': '544', 'idCiclo': '26554', 'idSede': '573', 'start': '0', 'limit': '100'},
        "fin_semana_calenadarioA_cur": {'idDeporte': '544', 'idCiclo': '26554', 'idSede': '3', 'start': '0', 'limit': '100'},
        "fin_semana_calenadarioA_online": {'idDeporte': '544', 'idCiclo': '26554', 'idSede': '584', 'start': '0', 'limit': '100'},
        "fin_semana_calenadarioA_suba": {'idDeporte': '544', 'idCiclo': '26554', 'idSede': '584', 'start': '0', 'limit': '100'},
        "fin_semana_calenadarioB_av68": {"idDeporte": "544","idCiclo": "26555","idSede": "476","start": "0","limit": "100"},
        "fin_semana_calenadarioB_cbi_soacha": {'idDeporte': '544', 'idCiclo': '26555', 'idSede': '607', 'start': '0', 'limit': '100'},
        "entre_semana_calenadarioB_av68": {"idDeporte": "544","idCiclo": "26556","idSede": "476","start": "0","limit": "100"},
        "entre_semana_calenadarioB_call94": {"idDeporte": "5","idCiclo": "26556","idSede": "476","start": "0","limit": "100"},
        "entre_semana_calenadarioB_cbi_americas": {"idDeporte": "588","idCiclo": "26556","idSede": "476","start": "0","limit": "100"},
        "entre_semana_calenadarioB_cbi_cll142": {"idDeporte": "610","idCiclo": "26556","idSede": "476","start": "0","limit": "100"},
        "entre_semana_calenadarioB_cbi_centro_mayor": {"idDeporte": "689","idCiclo": "26556","idSede": "476","start": "0","limit": "100"},
        "entre_semana_calenadarioB_cbi_pasus_veraguas": {"idDeporte": "618","idCiclo": "26556","idSede": "476","start": "0","limit": "100"},
        "entre_semana_calenadarioB_cbi_soacha": {"idDeporte": "607","idCiclo": "26556","idSede": "476","start": "0","limit": "100"},
        "entre_semana_calenadarioB_cur": {"idDeporte": "3","idCiclo": "26556","idSede": "476","start": "0","limit": "100"},
        "entre_semana_calenadarioB_online": {"idDeporte": "620","idCiclo": "26556","idSede": "476","start": "0","limit": "100"},
        "entre_semana_calenadarioB_suba": {"idDeporte": "584","idCiclo": "26556","idSede": "476","start": "0","limit": "100"},
        }
    SESSION.verify = False
    data_login = {
        "usuario": "jmfialloch", 
        "password": "Juan060997."}
    dias = {
        "lun": "Lunes",
        "mar": "Martes",
        "mié": "Miércoles",
        "jue": "Jueves",
        "viernes": "Viernes",
        "sáb": "Sábados",
        "dom": "Domingos",
        "sáb y dom": "Sábados y Domingos"
        }
    headers = {
    'authority': 'sistemamotricidad.deportescompensar.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'es-419,es;q=0.9,es-ES;q=0.8,en;q=0.7,en-GB;q=0.6,en-US;q=0.5',
    'cache-control': 'no-cache',
    'content-type': 'application/json;charset=UTF-8',
    # 'cookie': '_ga=GA1.2.1015349931.1649043978; _gid=GA1.2.143685208.1674574066; sistema=1ttpt51iai985lng117f5eju5alk8uur',
    'origin': 'https://sistemamotricidad.deportescompensar.com',
    'pragma': 'no-cache',
    'referer': 'https://sistemamotricidad.deportescompensar.com/sistema.php/login',
    'sec-ch-ua': '"Not_A Brand";v="99", "Microsoft Edge";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.61',
}
    DATA_1 = []
    DATA_2 = []

    def login(self):
        url_login = "https://sistemamotricidad.deportescompensar.com/sistema.php/login"
        login = self.SESSION.post(url = url_login,  json = {"usuario": "jmfialloch", "password": "Juan060997."}, headers=self.headers, verify=False)
        print(login)

    def extract_data_api(self, code_):
        code = code_
        url = "https://sistemamotricidad.deportescompensar.com/sistema.php/v1/pruebacampeonato/json"
        respuesta = self.SESSION.post(url, code, verify=False)
        dia = ""
        for i in respuesta.json()["pruebas"]:
            self.DATA_1.append({
                "sede":i["sede"],
                "ciclo": i["ciclo"],
                "nivel":i["prueba"].rstrip(i["prueba"][-1]),
                "de":i["horario"][0:5]+":00",
                "a":i["horario"][6:11]+":00",
                "dias":i["dias"]
            })
            dia = self.dias[self.DATA_1[len(self.DATA_1) - 1]['dias']]
            self.DATA_1[len(self.DATA_1) - 1]['dias'] = dia

        for i in respuesta.json()["pruebas"]:
            self.DATA_2.append({
                "inscritos":i["num_participantes"],
                "SKU":i["id"],
            })
        print(self.DATA_1)
        print(self.DATA_2)
    
        return [self.DATA_1, self.DATA_2]
    
    def loop_api(self):
        for i, c in zip(self.sedes_input_api, range(0,3)):
            if c <= 2:
                self.extract_data_api(self.sedes_input_api[i])
                print("s")
            else: 
                break

obj = SesionActive()
obj.login()
obj.loop_api()