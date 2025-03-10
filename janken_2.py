import sys
from random import randint
# ゲームの開始宣言をします
print("じゃんけんゲームを始めます")
# ルールの説明をします
print("0:グー 1:チョキ 2:パー")
# あいこの時、再度手の入力がされるためのループ処理
while True:
    # プレイヤーの手を入力
    player_hand=input("プレイヤーの手をルールに従い入力してください>>")
    jyanken_t="グー","チョキ","パー"
    # プレイヤーの手の入力が例外処理となった場合のループ処理
    try:      
        #　整数に変換
        player_hand=int(player_hand)
         # 範囲チェック
        if player_hand < 0 or player_hand > 2:
            print("0, 1, 2 のいずれかを入力してください")
            continue
        #　プレイヤーの手を表示
        print(f"あなたの手は{jyanken_t[player_hand]}です")
    except ValueError:
        print("整数ではない文字が入力されました")
        continue
    except IndexError:
        print("3以上の入力がされました")
        continue
    # PCの手を決定
    PC_hand=randint(0,2)
    # PCの手を表示
    print(f"PCの手は{jyanken_t[PC_hand]}です")
    # 判定
    result=(player_hand-PC_hand+3)%3
    # 結果の表示
    judgement="あいこでしょ","あなたの負けです","あなたの勝ちです"
    print(judgement[result])
    if judgement[result]=="あいこでしょ":
        continue
    break
