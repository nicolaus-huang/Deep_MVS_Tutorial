CUSTOM_TESTING="/mnt/PatchmatchNet/original/outputs_2"
CHECKPOINT_FILE="./checkpoints/params_000007.ckpt"
python eval_para.py --input_folder=$CUSTOM_TESTING --output_folder=./outputs_para_5 --checkpoint_path $CHECKPOINT_FILE \
   --batch_size 5 --num_views 10 --image_max_dim 2048 --geo_mask_thres 5 --num_process 10 --photo_thres 0.5 "$@"


#CUSTOM_TESTING="/home/custom/"
#python eval.py --input_folder=$CUSTOM_TESTING --output_folder=$CUSTOM_TESTING --checkpoint_path $CHECKPOINT_FILE \
#--parallel --num_views 10 --image_max_dim 2048 --geo_mask_thres 5 --photo_thres 0.5 "$@"
