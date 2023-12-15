## Preprocessing
Data preprocessing
```
python3 preprocessing.py --data_dir /path/to/data.jsonl --output_dir_for_training /path/to/processed-data.json
```
Do the following to process the training and testing data
```
python3 preprocessing.py  \
    --data_dir data/train.json \
    --output_dir data/processed_train.json
python3 preprocessing.py  \
    --data_dir data/public_test.json \
    --output_dir data/processed_public_test.json
python3 preprocessing.py  \
    --data_dir data/private_test.json \
    --output_dir data/processed_private_test.json
```

## Training
Model training for summarization
prepare the training config file qlora.yml and simply run accelerate launch -m axolotl.cli.train examples/llama-2/qlora.yml
```
accelerate launch -m axolotl.cli.train examples/llama-2/qlora.yml
```
## Inference
After data preprocessing and model training, prepare the testing config file test.yml and simply run python3 -m axolotl.cli.inference examples/llama-2/test.yml --lora_model_dir="./qlora-out"
```
python3 -m axolotl.cli.inference examples/llama-2/test.yml --lora_model_dir="./qlora-out"
```
