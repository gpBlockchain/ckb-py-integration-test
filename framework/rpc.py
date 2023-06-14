import requests

import json


class RPCClient:
    def __init__(self, url):
        self.url = url

    def get_tip_block_number(self):
        return int(self.call("get_tip_block_number", []),16)

    def local_node_info(self):
        return self.call("local_node_info", [])

    # //"QmUsZHPbjjzU627UZFt4k8j6ycEcNvXRnVGxCPKqwbAfQS",
    # "/ip4/192.168.2.100/tcp/8114"
    def add_node(self, peer_id, peer_address):
        return self.call("add_node", [peer_id, peer_address])

    def call(self, method, params):
        headers = {'content-type': 'application/json'}
        data = {
            "id": 1,
            "jsonrpc": "2.0",
            "method": method,
            "params": params
        }
        response = requests.post(self.url, data=json.dumps(data), headers=headers).json()
        print("request:url:{url},data:{data}".format(url = self.url,data= json.dumps(data)))
        print("response:{response}".format(response= response))
        return response.get('result', None)


if __name__ == '__main__':
    client = RPCClient("https://testnet.ckb.dev/")
    number = client.get_tip_block_number()
    print(number)
