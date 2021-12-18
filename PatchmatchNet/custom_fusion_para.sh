CUSTOM_TESTING = "./datasets/dtu-test/inputs"
CHECKPOINT_FILE = "./checkpoints/params_000007.ckpt"
OUTPUT_PATH = "./datasets/dtu-test/outputs"

python eval_para.py --input_folder=$CUSTOM_TESTING --output_folder=$OUTPUT_PATH --checkpoint_path $CHECKPOINT_FILE \
   --batch_size 4 --num_views 7 --output_type fusion --image_max_dim 2688 --geo_mask_thres 2 --geo_pixel_thres 0.7 --num_process 10 --photo_thres 0.8 "$@"
