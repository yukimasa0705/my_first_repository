from janken_v3_Player import Player
# MyPlayerのクラス化（プレイヤークラス作成の布石として名前を変更しました)       
class MyPlayer(Player):
    def __init__(self):
        # スーパークラス（親クラス）のコンストラクタを呼び出す
        super().__init__("あなた")
    # get_player_handの関数化
    def get_hand(self):
        # プレイヤーの手を入力して取得する
        while True:
            int_player_hand = input("プレイヤーの手をルールに従い入力してください>>")
            try:
                int_player_hand = int(int_player_hand)
                if int_player_hand < 0 or int_player_hand > 2:
                    print("0, 1, 2 のいずれかを入力してください")
                    continue  # 範囲外なら再入力
                # 親クラスの変数を継承
                return self.jyanken_t[int_player_hand] # グーチョキパーで返す
            except ValueError:
                print("整数ではない文字が入力されました")
                continue  # 無効な入力の場合、再入力
