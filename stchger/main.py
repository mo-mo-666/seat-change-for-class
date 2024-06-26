from .setting_io import read_setting, write_setting
from .initializer import RandomInitializer, RandomGlassesInitializer
from .loss import WeightedHopeLoss, GlassesLoss
from .changer import SeatChanger

import os
from typing import Sequence


def solve(
    seat_places: Sequence[tuple[int, int]], members: Sequence[dict]
) -> tuple[tuple[tuple[int, int]], list[float]]:
    """
    Solve pipeline

    Parameters
    ----------
    seat_places : Sequence[tuple[int, int]]
        Seat places.
    members : Sequence[dict]
        Members' directories

    Returns
    -------
    tuple[tuple[tuple[int, int]], list[float]]
        mem_places, loss_log
        Places of members and loss_logs.
    """

    hope_loss = WeightedHopeLoss(metric="euclid", power=2)
    glasses_loss = GlassesLoss(weight=1000000)
    seat_chger = SeatChanger(
        losses=[hope_loss, glasses_loss],
        initializer=RandomInitializer(),
        iter_num=100000,
        ch_step_range=(2, 5),
    )
    mem_places = seat_chger.solve(seat_places, members)
    loss_log = seat_chger.loss_log
    return mem_places, loss_log


def pipeline(setting_path: str, write_path: str):
    """
    Whole pipeline

    Parameters
    ----------
    setting_path : str
        Path to setting file.
    write_path : str
        Path to writing file.
    """
    # read data
    datas = read_setting(setting_path)
    members = datas["members"]
    seat_places = datas["seat_places"]
    # solve
    mem_places, loss_log = solve(seat_places, members)
    # write data
    datas["mem_places"] = mem_places
    datas["loss_log"] = loss_log

    for m, s in zip(members, mem_places):
        m["mem_place"] = s
    datas["members"] = members
    datas["member_keys"].append("mem_place")
    write_setting(write_path, datas)


def read_args() -> tuple[str, str]:
    """
    Read argument.

    Returns
    -------
    tuple[str, str]
        setting_path, write_path
    """
    while True:
        setting_path = input("設定ファイルのパスを指定してください：")
        if not setting_path or not os.path.exists(setting_path):
            print("そのようなファイルは存在しません")
        else:
            break

    # while True:
    #     write_path = input("結果を出力するファイルのパスを指定してください：")
    #     if not write_path:
    #         print("この項目は必須です")
    #     elif os.path.exists(write_path):
    #         yn = input("既にファイルが存在します．上書きしてもよろしいですか(y/n)：")
    #         if yn == "y":
    #             break
    #     else:
    #         break
    write_path = setting_path

    return setting_path, write_path


def main():
    setting_path, write_path = read_args()
    pipeline(setting_path, write_path)


if __name__ == "__main__":
    main()
