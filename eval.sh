#!/bin/bash

#SBATCH --job-name="bash"
#SBATCH --partition=v100-32g
#SBATCH --ntasks=4
#SBATCH --gres=gpu:1
#SBATCH --time=0-24:0
#SBATCH --chdir=.
#SBATCH --output=cout_eval.txt
#SBATCH --error=cerr_eval.txt


module load opt gcc python/3.9.13-gpu
sbatch_pre.sh
python3 -m ppl \
    --base_model_path Taiwan-LLM-7B-v2.0-chat/ \
    --peft_path axolotl/qlora-out/ \
    --test_data_path data/processed_public_test_without_id.json
sbatch_post.sh