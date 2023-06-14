## CKB Test

### prepare 
download ckb 
```shell
pip install -r requirements.txt
python -m download
```
### run 
run single test 
```shell
python -m pytest test_cases/framework/test_01_node.py
```

### add new test 
- test_cases/example/test_01_demo.py
- test_cases/example/test_02_fixture_demo.py


## todo 
- ckb-cli support 
- test with ckb build 
- ckb rpc support
- ckb contract support 
- etc..
