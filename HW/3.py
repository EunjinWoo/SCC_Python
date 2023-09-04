import hashlib

m = hashlib.sha256() #SHA256 방식으로 해싱

class Member:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        m.update(password.encode('utf-8')) # password hashing
        self.password = m.digest() # put hashed password str into self.passowrd
    
    def display(self):
        print(self.name, self.username)

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

members = []

for i in range(3):
    mem_info = input("name, username, password: ").split(", ")
    members.append(Member(mem_info[0], mem_info[1], mem_info[2]))
# Mem1 = Member("woo", "@esthrelar", "1234")
# Mem2 = Member("boo", "@pledis_boos", "1234")
# Mem3 = Member("han", "@yoon", "1234")

posts = []
for mem in members:
    for i in range(3):
        post_info = input("title, content, author(your username): ").split(", ")
        print(post_info)
        posts.append(Post(post_info[0], post_info[1], post_info[2]))

# for 문을 돌면서 특정유저가 작성한 게시글의 제목을 모두 프린트 해주세요
print("# for 문을 돌면서 특정유저가 작성한 게시글의 제목을 모두 프린트 해주세요")
for post in posts:
    if post.author == members[0].username:
        print(post.title)

# for문을 돌면서 ‘특정 단어’가 content에 포함된 게시글의 제목을 모두 프린트 해주세요
print("# for문을 돌면서 ‘hello’가 content에 포함된 게시글의 제목을 모두 프린트 해주세요")
for post in posts:
    if "hello" in post.content:
        print(post.title)