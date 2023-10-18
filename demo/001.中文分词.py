import hanlp
#https://hanlp.hankcs.com/docs/api/hanlp/pretrained/tok.html
#打印出所有分词模型
print(hanlp.pretrained.tok.ALL)

#加载分词模型
tok = hanlp.load(hanlp.pretrained.tok.COARSE_ELECTRA_SMALL_ZH)
r = tok("飞行器及其动力装置")

#打印分词结果
print(r)