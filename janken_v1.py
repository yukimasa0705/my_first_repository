import sys
from random import choice  # ランダム選択のためにchoiceをインポート

# ゲームの開始宣言をします
print("じゃんけんゲームを始めます")
# ルールの説明をします
print("0:グー 1:チョキ 2:パー")

# jyanken_tはループ外で一度だけ定義
jyanken_t = ("グー", "チョキ", "パー")

# あいこの時、再度手の入力がされるためのループ処理
while True:
    # プレイヤーの手を入力
    player_hand=input("プレイヤーの手をルールに従い入力してください>>")
    
    # プレイヤーの手の入力が例外処理となった場合のループ処理
    try:      
        #　整数に変換
        player_hand=int(player_hand)
        
         # 範囲チェック
        if player_hand < 0 or player_hand > 2:
            print("0, 1, 2 のいずれかを入力してください")
            continue  # 範囲外なら再入力
            
        #　プレイヤーの手を表示
        print(f"あなたの手は{jyanken_t[player_hand]}です")
    except ValueError:
        print("整数ではない文字が入力されました")
        continue
    except IndexError:
        # この部分は不要ですが、念のため入れておく
        print("無効な入力がありました")
        continue # 範囲外の値が入った場合
        
    # PCの手をランダムに決定
    PC_hand = choice(jyanken_t)  # jyanken_tからランダムに選ぶ
    print(f"PCの手は{PC_hand}です")
    
    # 判定
    if jyanken_t[player_hand] == PC_hand:
        print("あいこでしょ")
        continue # あいこの時、再度手を入力させる
    elif (jyanken_t[player_hand] == "グー" and PC_hand == "チョキ") or \
         (jyanken_t[player_hand] == "チョキ" and PC_hand == "パー") or \
         (jyanken_t[player_hand] == "パー" and PC_hand == "グー"):
        print("あなたの勝ちです")
    else:
        print("あなたの負けです")
    
    # 勝敗が決まったらループを終了
    break
