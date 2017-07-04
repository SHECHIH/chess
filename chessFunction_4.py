def noPutEnemyChess(chess,bout):             #用來判斷是否按到已方的棋子，會回傳結果
	if chess["text"][0]==bout["text"][0] :
		return(1)
	else :
		print("非己方棋子")                  #印出提醒訊息
		return(0)
"""
def noMoveOwnChess(chess,holdchess):
	if chess==holdchess :
		print("不能食用自己")
		return(0)
	elif chess["text"][0]==holdchess["text"][0] :
		print("不能食用己方棋子")
		return(0)
	else :
		return(1)
"""
#===================================================================================================
#函式，用來判斷是什麼棋子並呼叫相應的函式
def checkChess(chess,table,bout,rt=0):
	if chess["text"]=="白兵" :
		whitePawnWalk(chess,table,bout,rt)
	elif chess["text"]=="黑兵" :
		blackPawnWalk(chess,table,bout,rt)
	elif chess["text"][-2:]=="騎士" :
		knightWalk(chess,table,bout)
	elif chess["text"][-2:]=="主教" :
		bishopWalk(chess,table,bout)
	elif chess["text"][-2:]=="城堡" :
		rookWalk(chess,table,bout)
	elif chess["text"][-2:]=="皇后" :
		queenWalk(chess,table,bout)
	elif chess["text"][-2:]=="國王" :
		kingWalk(chess,table,bout)
	else :
		print("88")
#如果是白兵的話，會呼叫這個函式
def whitePawnWalk(chess,table,bout,rt):
	i,j=checkChessWhere(chess,table)
	if (i+1<8) and (j-1>-1) :
		if table[i+1][j-1]["text"][0]=="黑" :
			table[i+1][j-1]["bg"]="red"
	if (i-1>-1) and (j-1>-1) :
		if table[i-1][j-1]["text"][0]=="黑" :
			table[i-1][j-1]["bg"]="red"
	if j-1>-1 :
		if table[i][j-1]["text"]=="空白" :
			table[i][j-1]["bg"]="green"
	if j==6 :
		if (table[i][j-2]["text"]=="空白") and (table[i][j-1]["text"]=="空白"):
			table[i][j-2]["bg"]="green"
	if rt!=0 :
		if j==3 :
			if (i==rt["width"]+1) or (i==rt["width"]-1) :
				table[rt["width"]][3]["bg"]="orange"
				table[rt["width"]][3-1]["bg"]="red"
				rt["width"]+=10
#如果是黑兵的話，會呼叫這個函式
def blackPawnWalk(chess,table,bout,rt):
	i,j=checkChessWhere(chess,table)
	if (i+1<8) and (j+1<8) :
		if table[i+1][j+1]["text"][0]=="白" :
			table[i+1][j+1]["bg"]="red"
	if (i-1>-1) and (j+1<8) :
		if table[i-1][j+1]["text"][0]=="白" :
			table[i-1][j+1]["bg"]="red"
	if j+1<8 :
		if table[i][j+1]["text"]=="空白" :
			table[i][j+1]["bg"]="green"
	if j==1 :
		if (table[i][j+2]["text"])=="空白" and (table[i][j+1]["text"]=="空白"):
			table[i][j+2]["bg"]="green"
	if rt!=0 :
		if j==4 :
			if (i==rt["width"]+1) or (i==rt["width"]-1) :
				table[rt["width"]][4]["bg"]="orange"
				table[rt["width"]][4+1]["bg"]="red"
				rt["width"]+=10
#如果是騎士的話，會呼叫這個函式
def knightWalk(chess,table,bout):
	i,j=checkChessWhere(chess,table)
	if i+2<8 :
		if j+1<8 :
			draw(table[i+2][j+1],bout)
		if j-1>-1 :
			draw(table[i+2][j-1],bout)
	if i+1<8 :
		if j+2<8 :
			draw(table[i+1][j+2],bout)
		if j-2>-1 :
			draw(table[i+1][j-2],bout)
	if i-1>-1 :
		if j+2<8 :
			draw(table[i-1][j+2],bout)
		if j-2>-1 :
			draw(table[i-1][j-2],bout)
	if i-2>-1 :
		if j+1<8 :
			draw(table[i-2][j+1],bout)
		if j-1>-1 :
			draw(table[i-2][j-1],bout)
#如果是主教的話，會呼叫這個函式
def bishopWalk(chess,table,bout):
	i,j=checkChessWhere(chess,table)
	k=1
	while (i+k<8) and (j+k<8) :
		draw(table[i+k][j+k],bout)
		if table[i+k][j+k]["bg"]!="green" :
			break
		k+=1
	k=1
	while (i+k<8) and (j-k>-1) :
		draw(table[i+k][j-k],bout)
		if table[i+k][j-k]["bg"]!="green" :
			break
		k+=1
	k=1
	while (i-k>-1) and (j-k>-1) :
		draw(table[i-k][j-k],bout)
		if table[i-k][j-k]["bg"]!="green" :
			break
		k+=1
	k=1
	while (i-k>-1) and (j+k<8) :
		draw(table[i-k][j+k],bout)
		if table[i-k][j+k]["bg"]!="green" :
			break
		k+=1
#如果是城堡的話，會呼叫這個函式
def rookWalk(chess,table,bout):
	i,j=checkChessWhere(chess,table)
	k=1
	while i+k<8 :
		draw(table[i+k][j],bout)
		if table[i+k][j]["bg"]!="green" :
			break
		k+=1
	k=1
	while i-k>-1 :
		draw(table[i-k][j],bout)
		if table[i-k][j]["bg"]!="green" :
			break
		k+=1
	k=1
	while j+k<8 :
		draw(table[i][j+k],bout)
		if table[i][j+k]["bg"]!="green" :
			break
		k+=1
	k=1
	while j-k>-1 :
		draw(table[i][j-k],bout)
		if table[i][j-k]["bg"]!="green" :
			break
		k+=1
#如果是皇后的話，會呼叫這個函式
def queenWalk(chess,table,bout):
	i,j=checkChessWhere(chess,table)
	k=1
	while (i+k<8) and (j+k<8) :
		draw(table[i+k][j+k],bout)
		if table[i+k][j+k]["bg"]!="green" :
			break
		k+=1
	k=1
	while (i+k<8) and (j-k>-1) :
		draw(table[i+k][j-k],bout)
		if table[i+k][j-k]["bg"]!="green" :
			break
		k+=1
	k=1
	while (i-k>-1) and (j-k>-1) :
		draw(table[i-k][j-k],bout)
		if table[i-k][j-k]["bg"]!="green" :
			break
		k+=1
	k=1
	while (i-k>-1) and (j+k<8) :
		draw(table[i-k][j+k],bout)
		if table[i-k][j+k]["bg"]!="green" :
			break
		k+=1
	k=1
	while i+k<8 :
		draw(table[i+k][j],bout)
		if table[i+k][j]["bg"]!="green" :
			break
		k+=1
	k=1
	while i-k>-1 :
		draw(table[i-k][j],bout)
		if table[i-k][j]["bg"]!="green" :
			break
		k+=1
	k=1
	while j+k<8 :
		draw(table[i][j+k],bout)
		if table[i][j+k]["bg"]!="green" :
			break
		k+=1
	k=1
	while j-k>-1 :
		draw(table[i][j-k],bout)
		if table[i][j-k]["bg"]!="green" :
			break
		k+=1
#如果是國王的話，會呼叫這個函式
def kingWalk(chess,table,bout):
	i,j=checkChessWhere(chess,table)
	if (i+1<8) and (j+1<8) :
		draw(table[i+1][j+1],bout)
	if (i+1<8) and (j-1>-1) :
		draw(table[i+1][j-1],bout)
	if (i-1>-1) and (j-1>-1) :
		draw(table[i-1][j-1],bout)
	if (i-1>-1) and (j+1<8) :
		draw(table[i-1][j+1],bout)
	if i+1<8 :
		draw(table[i+1][j],bout)
	if i-1>-1 :
		draw(table[i-1][j],bout)
	if j+1<8 :
		draw(table[i][j+1],bout)
	if j-1>-1 :
		draw(table[i][j-1],bout)
#用來檢查棋子在哪一格
def checkChessWhere(chess,table):
	for x in range(8):
		for y in range(8):
			if chess==table[x][y] :
				return x,y
#用來畫上格子的顏色，有判斷是空白或敵方或己方
def draw(square,bout):
	if square["text"]=="空白" :
		square["bg"]="green"
	elif square["text"][0]==bout["text"][0] :
		pass
	else :
		square["bg"]="red"
#回復棋盤的顏色
def returncolor(table):
	for i in range(8):
		for j in range(8):
			if (i+j)%2==0 :
				table[i][j]["bg"]="white"
			else :
				table[i][j]["bg"]="silver"
#檢查是不是沒有可以移動的格子，會回傳值
def checkNoDraw(table):
	n=0
	for i in range(8):
		for j in range(8):
			if (i+j)%2==0 :
				if table[i][j]["bg"]!="white" :
					n=1
			else :
				if table[i][j]["bg"]!="silver" :
					n=1
	return n
#檢查有沒有可以升變士兵，會升變並回傳值
def upupup(table,whiteQueen,blackQueen):
	for i in range(8):
		if table[i][0]["text"]=="白兵" :
			table[i][0]["text"]="白皇后"
			table[i][0]["image"]=whiteQueen
			print("士兵成功升變!!")
			return 1
	i=0
	for i in range(8):
		if table[i][7]["text"]=="黑兵" :
			table[i][7]["text"]="黑皇后"
			table[i][7]["image"]=blackQueen
			print("士兵成功升變!!")
			return 2
	return 0