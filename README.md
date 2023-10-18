# learn_hanlp

## 环境设置
1. Python基础环境搭建
```shell
Python: 3.10.9
PyTorch: 2.1.0

```
2. 安装hanlp模块
```shell
pip install hanlp[full]
```

3. 修改环境变量（非必须）

临时修改,用于用户指定存储hanlp模块数据和模型文件
命令行知行如下代码
```shell
export HANLP_HOME=/data/code/python/hanlp_home
```

用户永久修改
```shell
vim ~/.bashrc
#文件末尾插入 #/data/hanlp_home修改为你想使用的存储目录
export HANLP_HOME=/data/hanlp_home
#然后:x (保存退出)
source ~/.bashrc
```

4. 测试安装结果

执行如下命令（注意/data/learn_hanlp根据自身实际情况修改）：
```python
python3 /data/learn_hanlp/tests/01.testinstall.py
```

控制台输出如下语句则表示安装成功,否则安装失败

```
 Ran 3 tests in 7.825s
 
 OK
```
