import include.xml_to_csv as xml_to_csv
import include.generate_pbtxt as generate_pbtxt
import include.generate_tfrecord as generate_tfrecord
from include.common import common


common('r2d2')
print(common.model_name)
generate_pbtxt.main()
xml_to_csv.main()
# generate_tfrecord.main('data/train_labels.csv', 'data/train.record')
# generate_tfrecord.main('data/eval_labels.csv', 'data/eval.record')
