PRE_PROCESSED_DATA_PATH = "./datasets/custom_dataset"
OUTPUT_PATH = "./datasets/custom_dataset/inputs"

NUM_PROCESS = 10


python3 colmap_input_para.py --input_folder $PRE_PROCESSED_DATA_PATH output_folder $OUTPUT_PATH --num_process $NUM_PROCESS