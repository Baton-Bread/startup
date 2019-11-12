#TCP альтернатива ему UDP
    #ipv4 255.255.255.255
    #ipv6 2001:0db8:11a3:09d7:1f34:8a2e:07a0:765d

import socket

class WebServer:
    def __init__(self, port):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET = ipv4 SOCK_STREAM = TCP
        self.websocket = ("127.0.0.1", port)
        self.urls = {
            "/": "main page",
            "/news": "news page"
        }

    def get_url(self, request):
        url = request.split(" ")[1]
        return url

    def get_response(self, url):
        link = self.urls.get(url)
        if link is None:
            return "HTTP/1.1 200 OK\n\n" + "Page not found"
        else:
            return "HTTP/1.1 200 OK\n\n" + self.urls[url]


    def start(self):
        self.server_socket.bind(self.websocket)
        self.server_socket.listen()

        while True:
            client_socket, adress = self.server_socket.accept()
            request = client_socket.recv(2048)

            url = self.get_url(request.decode())


            response = self.get_response(url)
            
            print(adress)
            print(request)

            client_socket.sendall(response.encode())
            client_socket.close()


WebServer(2121).start()
