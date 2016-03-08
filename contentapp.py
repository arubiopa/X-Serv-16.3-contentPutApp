#!/usr/bin/python

"""
 contentApp class
 Simple web application for managing content

 Copyright Jesus M. Gonzalez-Barahona, Gregorio Robles 2009-2015
 jgb, grex @ gsyc.es
 TSAI, SAT and SARO subjects (Universidad Rey Juan Carlos)
 October 2009 - March 2015
"""
#importamos de webapp
import webapp

#webapp.webApp = para que no haya colision de nombres modulo.clase
class contentApp (webapp.webApp):
    """Simple web application for managing content.

    Content is stored in a dictionary, which is intialized
    with the web content."""

    # Declare and initialize content
    content = {'/': 'Root page',
               '/page': 'A page',
               '/pepe': 'Hola,pepe',
               '/nueva': 'nueva'
               }

    def parse(self, request):
        """Return the resource name (including /)"""
        #tendremos que diferenciar entre put y get
        metodo = request.split(' ', 2)[0]
        recurso = request.split(' ', 2)[1]
        try:
            cuerpo = request.split('\r\n\r\n ')[1]
        except IndexError:
            cuerpo = ""
        
        return metodo, recurso,cuerpo

    def process(self, peticion):
        """Process the relevant elements of the request.

        Finds the HTML text corresponding to the resource name,
        ignoring requests for resources not in the dictionary.
        """
        metodo, recurso, cuerpo = peticion
        if metodo == "GET":
            if recurso in self.content.keys():
                httpCode = "200 OK"
                htmlBody = "<html><body>" + self.content[recurso] \
                    + '<form method="POST" action "/page">'\
                    + 'Name :<input type="text" name="firstname"><br>'\
                    + 'Surname:<input type="text" name="lastname"><br>'\
                    + '<input type="submit" value="enviar">'\
                    + '</form>'\
                    + "</body></html>"
            else:
                httpCode = "404 Not Found"
                htmlBody = "Not Found"
            
        elif metodo == "PUT" or metodo =="POST":
            self.content[recurso] = cuerpo
            httpCode = "200 OK"
            htmlBody = "Todo ha ido bien"
        else:
            httpCode = "450 Method  not Allowed"
            htmlBody = "Go away"
        return (httpCode, htmlBody)


if __name__ == "__main__":
    testWebApp = contentApp("localhost", 1235)

