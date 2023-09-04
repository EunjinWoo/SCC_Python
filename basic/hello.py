class Monster():
    hp = 100
    alive = True

    def damage(self, attack):
        self.hp = self.hp - attack
        if self.hp < 0:
            self.alive = False

    def status_check(self):
        if self.alive: # self.alive == True 인 것과 동일
            print('살았다')
        else :
            print('죽었다')

m1 = Monster() # m1이라는 변수에다가 몬스터를 이렇게 만든 것.and
m1.damage(150)
m1.status_check() # 죽었다

m2 = Monster()
m2.damage(90)
m2.status_check() # 살았다

# m1, m2 = 인스턴스