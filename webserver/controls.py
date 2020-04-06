def webserver_specialized(server,connection,data):
    server.send_file_headers(connection,contenttype="text/plain")
