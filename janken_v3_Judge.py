# judgeのクラス化
class Judge:
    @staticmethod
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
