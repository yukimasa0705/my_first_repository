from janken_v3_MyPlayer import  MyPlayer 
from janken_v3_PCPlayer import  PCPlayer
from janken_v3_Judge import Judge
# じゃんけんゲームのメイン処理
print("じゃんけんゲームを始めます")
num_computers = int(input("コンピュータの人数を入力してください: "))

# プレイヤーの手を決定
players = [MyPlayer()] + [PCPlayer(i) for i in range(num_computers)]

while len(players) > 1:
    while True:
        print("0:グー 1:チョキ 2:パー")
    # それぞれの手を決定
        for p in players:
            p.hand=p.get_hand() # ここで手を決める
            p.show_hand() # 手を表示

        # 勝者を判定
        winners = Judge.judge(players)
        # 引き分けでもう一度繰り返す
        if winners:
            players = winners
            break
        else:
            continue
print(f"最終勝者は {players[0].name} です！")