from random import choice
from janken_v3_Player import Player
# PCPlayerのクラス化
class PCPlayer(Player): 
    NICKNAMES = ["タロウ", "ジロー"]
    def __init__(self,index):
        # PCプレイヤーに名前を付け
        name=self.NICKNAMES[index]
        # スーパークラス（親クラス）のコンストラクタを呼び出す
        super().__init__(name)

    # get_pc_handの関数化
    def get_hand(self):
        # PCの手をランダムに取得する
        # 親クラスの変数を継承
        return choice(self.jyanken_t)
