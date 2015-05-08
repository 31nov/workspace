class Main:
    def __init__(self, userNumber, userId, userPic, userName,userPW):
        self.userNumber = userNumber
        self.userId = userId
        self.userPic = userPic
        self.userName = userName
        self.userPW = userPW

def user_all():
    return userList

userList = [
    Main(0, 're@1', './image/user0.png','홍길동',1234),
    Main(1, 're@2', './image/user1.png','홍길서',1234),
    Main(2, 're@3', './image/user2.png','홍길남',1234),
    Main(3, 're@4', './image/user3.png','홍길북',1234),
    Main(4, 're@5', './image/user4.png','김길동',1234),
    Main(5, 're@6', './image/user5.png','박길동',1234),
    Main(6, 're@7', './image/user6.png','정길동',1234),
    Main(7, 're@8', './image/user7.png','이길동',1234)
]