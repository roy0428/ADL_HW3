#!/bin/bash

#SBATCH --job-name="bash"
#SBATCH --partition=v100-32g
#SBATCH --ntasks=4
#SBATCH --gres=gpu:1
#SBATCH --time=0-24:0
#SBATCH --chdir=.
#SBATCH --output=cout_inference.txt
#SBATCH --error=cerr_inference.txt


module load opt gcc python/3.9.13-gpu
sbatch_pre.sh
python3 -m axolotl.axolotl.cli.inference axolotl/examples/llama-2/test.yml --lora_model_dir="./qlora-out"
sbatch_post.sh