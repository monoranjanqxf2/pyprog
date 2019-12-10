"""
It's a multiplayer number guessing game
Scope:
1.Input number of players
2.Input players name 
3.Generate a random number
4.Ask players to Guess the number
5.Ask player whether they want to countinue the game
6.If they continue then continue step 3, 4, 5 else show the result who won 
"""
import random
class pythongame:
    number_of_players=0
    player_name=[]
    winning_result=[]

#get number of player and their name
    def getplayers_name(self):
        self.number_of_players=int(input("Enter number of players : "))
        if(self.number_of_players<2):
            print("Atleast 2 players a allowed to play this game! Enter number of players again : ")
            self.getplayers_name()
        else:
            for i in range(self.number_of_players):
                player=input(f"Enter Player {i+1} name : ")
                self.player_name.append(player)
            for _ in range(self.number_of_players):
                self.winning_result.append(0)

#find the winner 
    def calculation(self):
        choice="Y"
        guessed_number=[]
        decide_win=[]
        while choice=="Y" or choice=="y":
            guessed_number.clear()
            #generating random number between 1-10
            random_num=random.randint(1,10)
            print(f"Random number is : {random_num}") #only for debugging purpose print the random number
            for i in range(self.number_of_players):#asking to guess a number
                num=int(input(f"{self.player_name[i]}, Can you guess a number between 1 to 10 : "))
                guessed_number.append(num)
            for pos, item in enumerate(guessed_number): #increasing winning list
                if(item==random_num):
                    self.winning_result[pos-1]=self.winning_result[pos]    
                else:
                    for j in guessed_number:
                        if j<random_num:
                            decide_win.append(random_num-j)
                        else:
                            decide_win.append(j-random_num)
            min_res=min(decide_win)
            pos1=decide_win.index(min_res)
            self.winning_result[pos1]=self.winning_result[pos1]+1
            decide_win.clear()
            choice=input("Press Y to continue playing or press any key to see score board : ")

#show winner name         
    def winner(self):
        max_res=max(self.winning_result)
        for pos, item in enumerate(self.winning_result):
            if(item==max_res):
                winner_name=self.player_name[pos]
        print(f"Congratulation {winner_name}, you win by {max_res} round")

#score board
    def score_board(self):
        for i in range(self.number_of_players):
            print(f"{self.player_name[i]} : {self.winning_result[i]}")
        
        

if __name__=='__main__':
    pgame=pythongame()
    pgame.getplayers_name()
    pgame.calculation()
    pgame.score_board()
    pgame.winner()
        

        
