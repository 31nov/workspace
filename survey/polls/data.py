class Poll:
    def __init__(self, id, name, choice_list):
        self.id = id
        self.name = name
        self.choice_list = choice_list
        
class Choice:
    def __init__(self,name,votes):
        self.name = name
        self.votes = votes
        
def get_all():
    return polls

def get(index):
    try:
        index = int(index)
    except(e):
        return None
    else:
        return polls[index]
    

polls = [
    Poll(0, "오늘 점심은 뭐 먹을까", [Choice("맥도날드", 3), Choice("카레돈까스", 2), Choice("라면", 6), Choice("다이어트", 14)]),
    Poll(1, "좋아하는 커피숍", [Choice("별다방", 8), Choice("콩다방", 5), Choice("천사다방", 2)]),
    Poll(2, "선호하는 재테크 방법", [Choice("예/적금", 12), Choice("주식/선물거래", 9), Choice("부동산", 2)])
]