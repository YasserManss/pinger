from pythonping import ping
import yaml

def load_hosts():
    with open('hosts.yaml', 'r') as file:
        hosts = yaml.safe_load(file)
    return hosts

def ping_hosts(hosts):
    for host in hosts:
        p = ping(target=host['IP'], timeout=0.2, count=3)
        if not p.success():
            print(f"host {host['description']} not pingable!")

if __name__ == "__main__":
    hosts = load_hosts()
    while True:
        ping_hosts(hosts)
