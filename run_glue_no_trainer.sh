#!/bin/bash
#SBATCH --job-name=gpt2-yl          
#SBATCH --output=logs/gpt2-yl-%j.out          
#SBATCH --nodes=1                 
#SBATCH --ntasks=1
#SBATCH --ntasks-per-node=1
#SBATCH --mem=100G
#SBATCH --cpus-per-task=20   
#SBATCH --partition=gpujl
#SBATCH --gres=gpu:4

export CUDA_VISIBLE_DEVICES=1
source /home/fuyali/miniconda3/bin/activate gpt2
cd /home/fuyali/emotionClassification

python run_glue_no_trainer.py \
  --model_name_or_path /home/fuyali/emotionClassification/checkpoints \
  --train_file /home/fuyali/emotionClassification/emotion/train.csv \
  --validation_file /home/fuyali/emotionClassification/emotion/val.csv \
  --max_length 128 \
  --per_device_train_batch_size 32 \
  --learning_rate 2e-5 \
  --num_train_epochs 1 \
  --report_to wandb \
  --output_dir /home/fuyali/emotionClassification/checkpoints

