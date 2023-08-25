import os
from itertools import combinations
import subprocess

games = ["tictactoe", "nim", "splix"]

for game in games:
    algos = os.listdir("approved/" + game)
    matchups = list(combinations(algos, 2))
    matchups.extend([[b, a] for a, b in matchups])
    wins = {algo: 0 for algo in algos}
    
    for algoOne, algoTwo in matchups:
        gameProcess = subprocess.Popen(["python", "games/"+game+".py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        playerOne = subprocess.Popen(["python", "approved/"+game+"/"+algoOne], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        playerTwo = subprocess.Popen(["python", "approved/"+game+"/"+algoTwo], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        turn = "one"
        playing = True
        while playing:
            gameData = gameProcess.stdout.readline() 
            
            if turn == "one":
                playerOne.stdin.write(gameData)
                playerOne.stdin.flush()
                move = playerOne.stdout.readline()
                gameProcess.stdin.write(move)
                gameProcess.stdin.flush()
            if turn == "two":
                playerTwo.stdin.write(gameData)
                playerTwo.stdin.flush()
                move = playerTwo.stdout.readline()
                gameProcess.stdin.write(move)
                gameProcess.stdin.flush()
            
            checkwin = gameProcess.stdout.readline()

            if "win" in checkwin:
                winner = turn
                playing = False
            elif "draw" in checkwin:
                winner = "draw"
                playing = False
            
            turn = "two" if turn == "one" else "one"
        
        if winner == "one":
            wins[algoOne] += 1
        elif winner == "two":
            wins[algoTwo] += 1
        elif winner == "draw":
            wins[algoOne] += 0.5
            wins[algoTwo] += 0.5
        
        gameProcess.stdin.close()
        gameProcess.stdout.close()
        gameProcess.wait()
        
        playerOne.stdin.close()
        playerOne.stdout.close()
        playerOne.wait()
        
        playerTwo.stdin.close()
        playerTwo.stdout.close()
        playerTwo.wait()
        
    print(wins)