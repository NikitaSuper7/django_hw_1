from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import time

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    """Спец. класс, который отвечает
    за обработку входящих запросов от клиентов."""

    def __get_html_content(self):
        with open('webapp.html', encoding='utf-8') as file:
            web_data = file.read()
        return web_data
    def do_GET(self):
        """Метод для обработки входящих GET-запросов"""
        query_comp = parse_qs(urlparse(self.path).query)
        print(query_comp)
        page_content = self.__get_html_content()
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(page_content, "utf-8"))
if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    # Корректная остановка веб-сервера, чтобы он освободил адрес и порт в сети, которые занимал
    webServer.server_close()
    print("Server stopped.")