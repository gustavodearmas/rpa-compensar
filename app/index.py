import requests
from bs4 import BeautifulSoup
import urllib3
urllib3.disable_warnings()

class SesionActive():
    SESSION = requests.Session()
    SESSION.verify = False
    data_login = {
        "usuario": "jmfialloch", 
        "password": "Juan060997."}
    dias = {
        "lun": "Lunes",
        "mar": "Martes",
        "mié": "Miércoles",
        "jue": "Jueves",
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

    def login(self):
        url_login = "https://sistemamotricidad.deportescompensar.com/sistema.php/login"
        login = self.SESSION.post(url = url_login,  json = {"usuario": "jmfialloch", "password": "Juan060997."}, headers=self.headers, verify=False)
        soup = BeautifulSoup(login.content, "html.parser")
        print(soup)

    def Av68_CicloII_FinSemana_CalendarioA(self):
        data_principal = []
        data_secundaria = []
        url = "https://sistemamotricidad.deportescompensar.com/sistema.php/v1/pruebacampeonato/json"
        code = {"idDeporte": "544","idCiclo": "26554","idSede": "476","start": "0","limit": "100"}
        respuesta = self.SESSION.post(url, code, verify=False)
        dia = ""
        for i in respuesta.json()["pruebas"]:
            data_principal.append({
                "sede":i["sede"],
                "ciclo": i["ciclo"],
                "nivel":i["prueba"].rstrip(i["prueba"][-1]),
                "de":i["horario"][0:5]+":00",
                "a":i["horario"][6:11]+":00",
                "dias":i["dias"]
            })
            dia = self.dias[data_principal[len(data_principal) - 1]['dias']]
            data_principal[len(data_principal) - 1]['dias'] = dia

        for i in respuesta.json()["pruebas"]:
            data_secundaria.append({
                "inscritos":i["num_participantes"],
                "SKU":i["id"],
            })
        return [data_principal, data_secundaria]

obj = SesionActive()