from tensorboard.backend.event_processing import event_accumulator
import argparse
import pandas as pd
from tqdm import tqdm


def main():
    # load log data
    parser = argparse.ArgumentParser(description='Export tensorboard data')
    parser.add_argument('--in-path', type=str, required=False, help='Tensorboard event files or a single tensorboard '
                                                                    'file location', default=".")
    parser.add_argument('--ex-path', type=str, required=False, help='location to save the exported data',
                        default="out.csv")

    args = parser.parse_args()
    event_data = event_accumulator.EventAccumulator(args.in_path)  # a python interface for loading Event data
    event_data.Reload()  # synchronously loads all of the data written so far b
    # print(event_data.Tags())  # print all tags
    keys = event_data.scalars.Keys()  # get all tags,save in a list
    keys = ["Average_mAP", "loss_total"]
    # print(keys)
    # 这里也可以选择想要的keys
    df = pd.DataFrame(columns=keys)
    for key in tqdm(keys):
        # print(key)
        # 可以写你筛选的类，这里我全都要所以注释掉下面
        # if key != 'train/total_loss_iter':
        #     df[key] = pd.DataFrame(event_data.Scalars(key)).value
        df[key] = pd.DataFrame(event_data.Scalars(key)).value
    df.to_csv(args.ex_path)

    print("Tensorboard data exported successfully")


if __name__ == '__main__':
    main()
