import time
import logging

from chitools.kernel.combination_generator import gen_data, label_encode_data
from chitools.utils.time_utils.time_recoder import TimeRecoder, time_recorder

logger = logging.getLogger(__name__)

@time_recorder
def prepare_data():
    df_data = gen_data(part_num=20, ret_num=20, tool_num=20, pre1tool_num=20, pre2tool_num=20, chuck_num=2)
    lst_feat = df_data.columns
    df_data_le, _ = label_encode_data(df_data, lst_feat)
    logger.info(f'Gen Data Shape: {df_data.shape}')
    logger.info(f'Feature: {lst_feat}')
    logger.info(f'df_data_le Shape: {df_data_le.shape}')

@time_recorder
def app2():
    time.sleep(0.5)

@time_recorder
def app3():
    time.sleep(0.5)

def main():
    # prepare_data()
    app2()
    app3()
    logger.info("Chi Tools Done")
    TimeRecoder().record_exec_time().to_csv("./exec_time.csv", index=False)


if __name__ == "__main__":
    main()