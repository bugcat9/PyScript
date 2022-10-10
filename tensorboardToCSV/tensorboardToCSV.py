from tensorboard.backend.event_processing import event_accumulator
import pandas as pd
from tqdm import tqdm


def tensorboardToCSV(in_path, ex_path):
    '''
    将 tensorboard log 文件转化为 CSV
    in_path: tensorboard 文件路径
    ex_path: excel导出路径
    '''
    # 加载 log data
    event_data = event_accumulator.EventAccumulator(in_path)
    event_data.Reload()
    tags = event_data.Tags()
    for tag in tags:
        print(tag)
    print("---------------------------------------")
    keys = event_data.scalars.Keys()
    for key in keys:
        print(key)

    # 这里也可以选择想要的keys
    df = pd.DataFrame(columns=keys)
    for key in tqdm(keys):
        # print(key)
        # 可以写你筛选的类，这里我全都要所以注释掉下面
        # if key != 'train/total_loss_iter':
        #     df[key] = pd.DataFrame(event_data.Scalars(key)).value
        df[key] = pd.DataFrame(event_data.Scalars(key)).value
    df.to_csv(ex_path)

    print("Tensorboard data exported to csv successfully")


if __name__ == '__main__':
    in_path = "tensorboardToCSV\events.out.tfevents.1619248452.ubun"
    ex_path = "tensorboardToCSV\out.csv"
    tensorboardToCSV(in_path, ex_path)
