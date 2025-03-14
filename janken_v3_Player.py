class Player(ABC):
    # constructer
    def __init__(self,name):
        # property
        self.name=name #my or PC
        self.hand=None
        self.jyanken_t = ("グー", "チョキ", "パー")
    # 手を決める関数の共通化
    @abstractmethod
    def get_hand(self):
        pass
    # 手の表示の共通化
    def show_hand(self):
        print(f"{self.name}の手は{self.hand}です")
        return self.hand
