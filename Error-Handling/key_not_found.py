server = { 'name': "server-01", 'os': "Linux"}

server_cpu = server.get('cpu',"")

print(f"cpu of the server {server_cpu}")

try:
 
    server_cpu = server['cpu']

except KeyError as err:

    print(f"Required key is missing : {err}")

