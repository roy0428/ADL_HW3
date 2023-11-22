from argparse import ArgumentParser
from pathlib import Path
import json

def parse_args():
    parser = ArgumentParser()
    parser.add_argument("--data_dir",
                        default='HW3/hw3/data/private_test.json',
                        type=str)
    parser.add_argument("--output_dir",
                        default='HW3/hw3/data/processed_private_test.json',
                        type=str)

    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_args()

    with open(args.data_dir, 'r') as json_file:
        data_list = json.load(json_file)

    result = []
    for data in data_list:
        data["instruction"] = f'你是人工智慧助理，以下是用戶和人工智能助理之間的對話。你要對用戶的問題提供有用、安全、詳細和禮貌的回答。USER: {data["instruction"]} ASSISTANT:'
        # data.pop("id")
        result.append(data)

    # data_json = {"data": result}
    data_json = result
    json.dump(data_json, open(args.output_dir, 'w'), indent=2, ensure_ascii=False)