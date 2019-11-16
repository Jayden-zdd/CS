
from collections import Counter
content = '''Based on this preliminary study, we show that BERT can be adapted to relation extraction andsemantic role labeling without syntactic features
and human-designed constraints. While we concede that our model is quite simple, we argue this
is a feature, as the power of 'BERT' is able to simplify neural architectures tailored to specific tasks.
Nevertheless, these results provide strong baselines and foundations for future research. Many
natural follow-up questions emerge: Can syntactic features be re-introduced to further improve results? Can multitask learning be used to simultaneously benefit relation extraction and semantic
role labeling? We are actively working on answering these and additional questions.'''

content = content.replace('\n',' ').replace('\'',' ').replace(',',' ').replace('.',' ').replace('?',' ')
con_list = content.split()
con_count = Counter(con_list)
print('word and count:',con_count)
print('----------------------------')
print('count_10:',con_count.most_common(10))