from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
<head>
<title>Top Software Companies</title>
</head>
<body align="center">
<caption>Top 5 software companies</caption>
<table>
<table border="1" cellspacing="2" cellpadding="2" align="center">
            <tr>
                <th>Rank</th>
                <th>Company Name</th>
                <th>Revenue(billion dollars)</th>
            </tr>
            <tr>
                <td>1</td>
                <td>Microsoft</td>
                <td>203.08</td>
            </tr>
            <tr>
                <td>2</td>
                <td>Oracle</td>
                <td>46.07</td>
            </tr>
            <tr>
                <td>3</td>
                <td>SAP SE</td>
                <td>32.97</td>
            </tr>
            <tr>
                <td>4</td>
                <td>Salesforce</td>
                <td>30.29</td>
            </tr>
            <tr>
                <td>5</td>
                <td>Adobe</td>
                <td>17.61</td>
</table>
</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()