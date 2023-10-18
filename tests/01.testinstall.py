import unittest

class TestingClass(unittest.TestCase):

    # Multi-Task Testing
    def test_mutil_task(self):
        import hanlp
        HanLP = hanlp.load(hanlp.pretrained.mtl.CLOSE_TOK_POS_NER_SRL_DEP_SDP_CON_ELECTRA_SMALL_ZH) # 世界最大中文语料库
        r = HanLP(['hanlp测试语句'])
        self.assertEqual(str(type(r)),"<class 'hanlp_common.document.Document'>")

    #Single-Task Testing
    def test_single_task(self):
        import hanlp
        HanLP = hanlp.pipeline() \
            .append(hanlp.utils.rules.split_sentence, output_key='sentences') \
            .append(hanlp.load('FINE_ELECTRA_SMALL_ZH'), output_key='tok') \
            .append(hanlp.load('CTB9_POS_ELECTRA_SMALL'), output_key='pos') \
            .append(hanlp.load('MSRA_NER_ELECTRA_SMALL_ZH'), output_key='ner', input_key='tok') \
            .append(hanlp.load('CTB9_DEP_ELECTRA_SMALL', conll=0), output_key='dep', input_key='tok')\
            .append(hanlp.load('CTB9_CON_ELECTRA_SMALL'), output_key='con', input_key='tok')
        r = HanLP('作为一个测试case。我应该保持每一个测试用例的唯一性。') 
        self.assertEqual(str(type(r)),"<class 'hanlp_common.document.Document'>")

    #Segment-Words Testing
    def test_segment_words(self):

        import hanlp
        tokenizer = hanlp.load('PKU_NAME_MERGED_SIX_MONTHS_CONVSEG')
        r = tokenizer("我是分词测试用例。")
        self.assertEqual("我",r[0])
        self.assertEqual("是",r[1])
        self.assertEqual("分词",r[2])
        self.assertEqual("测试",r[3])
        self.assertEqual("用例",r[4])
        self.assertEqual("。",r[5])

unittest.main()