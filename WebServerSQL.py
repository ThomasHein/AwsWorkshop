#!/usr/bin/bash
import mysql.connector
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT_NUMBER = 8888

host = '12.0.2.134'
database = "awsomedatabase"
successfulDBConnection = False;


def createDBConnection():
    print("DB Connection is tried to establish");
    successfulDBConnection = False;
    try:
        connection = mysql.connector.connect(host=host,database=database,user='root', password='notsecure',connection_timeout=1);
        db_Info = connection.get_server_info()
        print("Connected to MySQL database... MySQL Server version on ",db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print ("Your connected to - ", record)
        successfulDBConnection = True
    except mysql.connector.Error as e:
        print ("Error while connecting to MySQL",e)
        successfulDBConnection = False;
    return successfulDBConnection;

#This class will handles any incoming request from
#the browser
class serverUserRequest(BaseHTTPRequestHandler):
    successfulDBConnection = False;

    #Handler for the GET requests
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        # Send the html message
        # Send message back to client
        message = "DB Connection Successful: " +str(successfulDBConnection);
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return

try:
    #Create a web server and define the handler to manage the
    #incoming request
    print("Application starts")
    successfulDBConnection = createDBConnection();
    print(successfulDBConnection);
    server = HTTPServer(('', PORT_NUMBER),serverUserRequest)
    print ("Started httpserver on port ", PORT_NUMBER)

    #Wait forever for incoming htto requests
    server.serve_forever()

except KeyboardInterrupt:
    print ("^C received, shutting down the web server")
    server.socket.close()
    #closing database connection.