from bs4 import BeautifulSoup
import json

with open("/Users/abhilash/Documents/Workshop/Output/SERVERS.JSON") as servers_json_file:

    data_servers = json.load(servers_json_file)

    with open('/Users/abhilash/Documents/Workshop/HTML/servers_ip.html', 'r') as file_1:
        soup = BeautifulSoup(file_1, features="html.parser")

    for server in data_servers["SERVERS"]:
        if server["SERVER_OUTPUT"] == 0:
            x = soup.find(id=server["ID"])
            x.attrs["class"][1] = "server-down"

        print(soup.prettify())

        file = open("/Users/abhilash/Documents/Workshop/HTML/servers_op.html", "w")
        file.write(soup.prettify())
        file.close()