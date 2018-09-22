import include.xml_to_csv as xml_to_csv
import include.generate_pbtxt as generate_pbtxt
from include.common import common


common('r2d2')
print(common.model_name)

generate_pbtxt.main()


#xml_to_csv.main()