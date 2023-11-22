python3 preprocessing.py \
    --data_dir ${3} \
    --output_dir processed_data.json

python3 -m axolotl.cli.inference examples/llama-2/test.yml \
    --base_model ${1} \
    --lora_model_dir ${2} \
    --datasets_path processed_data.json \
    --output_file ${4} 