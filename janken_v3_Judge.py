# judgeのクラス化
class Judge:
# judgeの関数化
    def judge(players):
        while True:
            hands = set(player.hand for player in players)
            # じゃんけんの勝敗を判定する
            if len(hands) == 2: # 勝敗が決まった場合
                winner_hand = Judge.winning_hand(hands)
                winners = [p for p in players if p.hand == winner_hand]
                print("勝者: " + ", ".join(p.name for p in winners))
                return winners # 勝者を返す
            else:
                print("あいこでしょ")
                return None # あいこだった場合はNoneを返す

    @staticmethod
    def winning_hand(hands):
        if "グー" in hands and "チョキ" in hands:
            return "グー"
        elif "チョキ" in hands and "パー" in hands:
            return "チョキ"
        else:
            return "パー"