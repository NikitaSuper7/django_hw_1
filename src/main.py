from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from config import operations_path

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    """Спец. класс, который отвечает
    за обработку входящих запросов от клиентов."""


    def __get_index(self):
        with open('main_page.html', encoding='utf-8') as file:
            web_data = file.read()
        return web_data
    def __get_html_content(self, page_address):
        if page_address == 'catalog':
            with open('catalog.html', encoding='utf-8') as file:
                web_data = file.read()
            return web_data
        elif page_address == 'category':
            with open('category_page.html', encoding='utf-8') as file:
                web_data = file.read()
            return web_data
        elif page_address == 'main':
            with open('main_page.html', encoding='utf-8') as file:
                web_data = file.read()
            return web_data
        elif page_address == 'contacts':
            with open('contacts.html', encoding='utf-8') as file:
                web_data = file.read()
            return web_data
        else:
            "page Not found 404"

    def __get_blog_article(self, page_address):
        return self.__get_html_content(page_address)


    def do_GET(self):
        query_components = parse_qs(urlparse(self.path).query)
        page_address = query_components.get('page')
        page_content = self.__get_index()
        if page_address:
            page_content = self.__get_blog_article(page_address[0])
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(page_content, "utf-8"))
    # def do_GET(self):
    #     """Метод для обработки входящих GET-запросов"""
    #     query_comp = parse_qs(urlparse(self.path).query)
    #     print(query_comp)
    #     page_content = self.__get_html_content()
    #     self.send_response(200)
    #     self.send_header("Content-type", "text/html")
    #     self.end_headers()
    #     self.file.write(bytes(page_content, "utf-8"))
if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")