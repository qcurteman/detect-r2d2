# detect-r2d2
Repo for detecting r2d2 with Google's TensorFlow


To run it:

from "/models/research/"
python object_detection/model_main.py --pipeline_config_path="C:\tensorflow1\models\research\object_detection\detect-r2d2\models\model\embedded_ssd_mobilenet_v1_coco.config" --model_dir="C:\tensorflow1\models\research\object_detection\detect-r2d2\models\model\training" --num_train_steps=200 --sample_1_of_n_eval_examples=1 --alsologtostderr


To view it: 

from "/models/research/"
tensorboard --logdir="C:\tensorflow1\models\research\object_detection\detect-r2d2\models\model\training" --host localhost --port 8088

Then go to http://localhost:8088
