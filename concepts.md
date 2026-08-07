-- This file contains the main concepts when working with backend development

# HTTP - protocolo de la capa de aplicación
protocolo de comunicación fundamental para la WWW, estandariza la comunicación entre clientes y servidores para intercambiar datos. 
1. El cliente inicia la comunicación y el servidor responde
2. funciona sobre protocolos de transporte como TCP (HTTP/1.1 - conexiones persistentes y HTTP/2 - multiplex) o QUIC/UDP (HTTP/3 - menor latencia)

# API (Aplication Programming Interface)
Capa de comunicación que permite mecanismos de interacción con el backend, sigue estándares para mejorar su desarrollo y uso

# FastAPI
Funciona con el servidor *uvicorn* que permite ejecutar el backend de forma local. En /docs se presenta la documentación con Swagger UI para conocer cada endpoint.

# Postman
Aunque podamos probar peticiones GET en el navegador, cuando queremos hacer otro tipo de peticiones (como POST) surgen otras herramientas que son de utilidad. Postman es un cliente que permite realizar peticiones a una API. Estas pruebas también se pueden realizar, como se mencionó, con /docs.