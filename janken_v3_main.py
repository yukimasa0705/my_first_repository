from janken_v3_MyPlayer import  MyPlayer 
from janken_v3_PCPlayer import  PCPlayer
from janken_v3_Judge import Judge
# じゃんけんゲームのメイン処理
print("じゃんけんゲームを始めます")
print("0:グー 1:チョキ 2:パー")
# プレイヤーの作成
myPlayer = MyPlayer()
pcPlayer1 = PCPlayer()
pcPlayer2 = PCPlayer()
judge = Judge()

# プレイヤーの手を決定
players = [myPlayer, pcPlayer1, pcPlayer2]

while True:
    # それぞれの手を決定
    for p in players:
        p.hand=p.get_hand() # ここで手を決める
        p.show_hand() # 手を表示

    # 勝者を判定
    winners = Judge.judge(players)
    # 引き分けでもう一度繰り返す
    if winners:
        break
    else:
        continue