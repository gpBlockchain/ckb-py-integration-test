from framework.util import get_project_root

TMP_PATH = "tmp"

# private key 98400f6a67af07025f5959af35ed653d649f745b8f54bf3f07bef9bd605ee946
#   key: "98400f6a67af07025f5959af35ed653d649f745b8f54bf3f07bef9bd605ee946"
#   code_hash: "0x9bd7e06f3ecf4be0f2fcd2188b23f1b9fcc88e5d4b65a8637b17723bbda3cce8"
#   args: "0x8883a512ee2383c01574a328f60eeccbb4d78240"
#   hash_type: "type"
#   message: "0x"
## template/ckb.toml.j2
CKB_DEFAULT_CONFIG = {
    # 'ckb_chain_spec': '{ bundled = "specs/mainnet.toml" }',
    'ckb_chain_spec': '{ file = "dev.toml" }',
    'ckb_network_listen_addresses': ["/ip4/0.0.0.0/tcp/8115"],
    'ckb_rpc_listen_address': '127.0.0.1:8114',
    'ckb_rpc_modules': ["Net", "Pool", "Miner", "Chain", "Stats", "Subscription", "Experiment", "Debug"],
    'ckb_block_assembler_code_hash': '0x9bd7e06f3ecf4be0f2fcd2188b23f1b9fcc88e5d4b65a8637b17723bbda3cce8',
    'ckb_block_assembler_args': '0x8883a512ee2383c01574a328f60eeccbb4d78240',
    'ckb_block_assembler_hash_type': 'type',
    'ckb_block_assembler_message': '0x'
}

CKB_MINER_CONFIG = {
    'ckb_miner_rpc_url': '127.0.0.1:8114',
    'ckb_chain_spec': '{ file = "dev.toml" }',
}


def get_tmp_path():
    return "{path}/{tmp}".format(path=get_project_root(), tmp=TMP_PATH)
