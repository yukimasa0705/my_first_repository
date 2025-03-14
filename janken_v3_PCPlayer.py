# PCPlayerのクラス化
class PCPlayer(Player): 
    def __init__(self):
        # スーパークラス（親クラス）のコンストラクタを呼び出す
        super().__init__("PC")

    # get_pc_handの関数化
    def get_hand(self):
        # PCの手をランダムに取得する
        # 親クラスの変数を継承
        return choice(self.jyanken_t)
