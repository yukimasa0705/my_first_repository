from janken_v3_MyPlayer import  MyPlayer 
from janken_v3_PCPlayer import  PCPlayer
from janken_v3_Judge import Judge
# じゃんけんゲームのメイン処理
print("じゃんけんゲームを始めます")
print("0:グー 1:チョキ 2:パー")
myPlayer = MyPlayer()
pcPlayer = PCPlayer()
judge = Judge()

while True:
    player_hand = myPlayer.get_hand()
    pc_hand = pcPlayer.get_hand()
    print(f"あなたの手は{player_hand}です")
    print(f"PCの手は{pc_hand}です")

    if Judge.judge(player_hand, pc_hand):
        break  # 勝敗が決まったら終了
