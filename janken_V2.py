import sys
# ランダム選択のためにchoiceをインポート
from random import choice  

# jyanken_tはループ外で一度だけ定義
jyanken_t = ("グー", "チョキ", "パー")

# get_player_handの関数化
def get_player_hand():
    # プレイヤーの手を入力して取得する
    while True:
        int_player_hand = input("プレイヤーの手をルールに従い入力してください>>")
        try:
            int_player_hand = int(int_player_hand)
            if int_player_hand < 0 or int_player_hand > 2:
                print("0, 1, 2 のいずれかを入力してください")
                continue  # 範囲外なら再入力
            player_hand = jyanken_t[int_player_hand]
            return player_hand  # グーチョキパーで返す
        except ValueError:
            print("整数ではない文字が入力されました")
            continue  # 無効な入力の場合、再入力

# get_pc_handの関数化
def get_pc_hand():
    # PCの手をランダムに取得する
    pc_hand = choice(jyanken_t)
    return pc_hand

# judgeの関数化
def judge(player_hand, pc_hand):
    # じゃんけんの勝敗を判定する
    if player_hand == pc_hand:
        print("あいこでしょ")
        return False
    elif (player_hand == "グー" and pc_hand == "チョキ") or \
         (player_hand == "チョキ" and pc_hand == "パー") or \
         (player_hand == "パー" and pc_hand == "グー"):
        print("あなたの勝ちです")
    else:
        print("あなたの負けです")
    return True

# じゃんけんゲームのメイン処理
print("じゃんけんゲームを始めます")
print("0:グー 1:チョキ 2:パー")

while True:
    player_hand = get_player_hand()
    pc_hand = get_pc_hand()
    print(f"あなたの手は{player_hand}です")
    print(f"PCの手は{pc_hand}です")

    if judge(player_hand, pc_hand):
        break  # 勝敗が決まったら終了
