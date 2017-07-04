from tkinter import *
from chessFunction_4 import *
import random


checkerboard = Tk()                          #建立一個視窗
checkerboard.title("西洋棋")                 #視窗標題
checkerboard.geometry("605x320")             #視窗大小

"""
some = Label(checkerboard, text="Tk's job!!", width="30", height="5")
some.pack()
"""

grid=[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
holdchess=0                  #正拿著的棋子

#建立變數，將圖片宣告上
blackKing = PhotoImage(file=r"D:\pythonwork\blackKing.png")
blackQueen = PhotoImage(file=r"D:\pythonwork\blackQueen.png")
blackRook = PhotoImage(file=r"D:\pythonwork\blackRook.png")
blackBishop = PhotoImage(file=r"D:\pythonwork\blackBishop.png")
blackKnight = PhotoImage(file=r"D:\pythonwork\blackKnight.png")
blackPawn = PhotoImage(file=r"D:\pythonwork\blackPawn.png")
whiteKing = PhotoImage(file="D:\pythonwork\whiteKing.png")
whiteQueen = PhotoImage(file="D:\pythonwork\whiteQueen.png")
whiteRook = PhotoImage(file="D:\pythonwork\whiteRook.png")
whiteBishop = PhotoImage(file="D:\pythonwork\whiteBishop.png")
whiteKnight = PhotoImage(file="D:\pythonwork\whiteKnight.png")
whitePawn = PhotoImage(file="D:\pythonwork\whitePawn.png")
space = PhotoImage(file="D:\pythonwork\space.png")
miniblackKing = PhotoImage(file=r"D:\pythonwork\miniblackKing.png")
miniblackQueen = PhotoImage(file=r"D:\pythonwork\miniblackQueen.png")
miniblackRook = PhotoImage(file=r"D:\pythonwork\miniblackRook.png")
miniblackBishop = PhotoImage(file=r"D:\pythonwork\miniblackBishop.png")
miniblackKnight = PhotoImage(file=r"D:\pythonwork\miniblackKnight.png")
miniblackPawn = PhotoImage(file=r"D:\pythonwork\miniblackPawn.png")
miniwhiteKing = PhotoImage(file="D:\pythonwork\miniwhiteKing.png")
miniwhiteQueen = PhotoImage(file="D:\pythonwork\miniwhiteQueen.png")
miniwhiteRook = PhotoImage(file="D:\pythonwork\miniwhiteRook.png")
miniwhiteBishop = PhotoImage(file="D:\pythonwork\miniwhiteBishop.png")
miniwhiteKnight = PhotoImage(file="D:\pythonwork\miniwhiteKnight.png")
miniwhitePawn = PhotoImage(file="D:\pythonwork\miniwhitePawn.png")
blackKingWin = PhotoImage(file=r"D:\pythonwork\blackKingWin.png")
whiteKingWin = PhotoImage(file="D:\pythonwork\whiteKingWin.png")

#用列表建立格子和初始棋盤
grid[0][0] = Button(checkerboard,width="35", height="35",text="黑城堡",bg="white",image=blackRook)
grid[0][0].place(x = 0, y = 0)
grid[1][0] = Button(checkerboard,width="35", height="35",text="黑騎士",bg="silver",image=blackKnight)
grid[1][0].place(x = 40, y = 0)
grid[2][0] = Button(checkerboard,width="35", height="35",text="黑主教",bg="white",image=blackBishop)
grid[2][0].place(x = 80, y = 0)
grid[3][0] = Button(checkerboard,width="35", height="35",text="黑皇后",bg="silver",image=blackQueen)
grid[3][0].place(x = 120, y = 0)
grid[4][0] = Button(checkerboard,width="35", height="35",text="黑國王",bg="white",image=blackKing)
grid[4][0].place(x = 160, y = 0)
grid[5][0] = Button(checkerboard,width="35", height="35",text="黑主教",bg="silver",image=blackBishop)
grid[5][0].place(x = 200, y = 0)
grid[6][0] = Button(checkerboard,width="35", height="35",text="黑騎士",bg="white",image=blackKnight)
grid[6][0].place(x = 240, y = 0)
grid[7][0] = Button(checkerboard,width="35", height="35",text="黑城堡",bg="silver",image=blackRook)
grid[7][0].place(x = 280, y = 0)

grid[0][1] = Button(checkerboard,width="35", height="35",text="黑兵",bg="silver",image=blackPawn)
grid[0][1].place(x = 0, y = 40)
grid[1][1] = Button(checkerboard,width="35", height="35",text="黑兵",bg="white",image=blackPawn)
grid[1][1].place(x = 40, y = 40)
grid[2][1] = Button(checkerboard,width="35", height="35",text="黑兵",bg="silver",image=blackPawn)
grid[2][1].place(x = 80, y = 40)
grid[3][1] = Button(checkerboard,width="35", height="35",text="黑兵",bg="white",image=blackPawn)
grid[3][1].place(x = 120, y = 40)
grid[4][1] = Button(checkerboard,width="35", height="35",text="黑兵",bg="silver",image=blackPawn)
grid[4][1].place(x = 160, y = 40)
grid[5][1] = Button(checkerboard,width="35", height="35",text="黑兵",bg="white",image=blackPawn)
grid[5][1].place(x = 200, y = 40)
grid[6][1] = Button(checkerboard,width="35", height="35",text="黑兵",bg="silver",image=blackPawn)
grid[6][1].place(x = 240, y = 40)
grid[7][1] = Button(checkerboard,width="35", height="35",text="黑兵",bg="white",image=blackPawn)
grid[7][1].place(x = 280, y = 40)

grid[0][2] = Button(checkerboard,width="35", height="35",text="空白",bg="white",image=space)
grid[0][2].place(x = 0, y = 80)
grid[1][2] = Button(checkerboard,width="35", height="35",text="空白",bg="silver",image=space)
grid[1][2].place(x = 40, y = 80)
grid[2][2] = Button(checkerboard,width="35", height="35",text="空白",bg="white",image=space)
grid[2][2].place(x = 80, y = 80)
grid[3][2] = Button(checkerboard,width="35", height="35",text="空白",bg="silver",image=space)
grid[3][2].place(x = 120, y = 80)
grid[4][2] = Button(checkerboard,width="35", height="35",text="空白",bg="white",image=space)
grid[4][2].place(x = 160, y = 80)
grid[5][2] = Button(checkerboard,width="35", height="35",text="空白",bg="silver",image=space)
grid[5][2].place(x = 200, y = 80)
grid[6][2] = Button(checkerboard,width="35", height="35",text="空白",bg="white",image=space)
grid[6][2].place(x = 240, y = 80)
grid[7][2] = Button(checkerboard,width="35", height="35",text="空白",bg="silver",image=space)
grid[7][2].place(x = 280, y = 80)

grid[0][3] = Button(checkerboard,width="35", height="35",text="空白",bg="silver",image=space)
grid[0][3].place(x = 0, y = 120)
grid[1][3] = Button(checkerboard,width="35", height="35",text="空白",bg="white",image=space)
grid[1][3].place(x = 40, y = 120)
grid[2][3] = Button(checkerboard,width="35", height="35",text="空白",bg="silver",image=space)
grid[2][3].place(x = 80, y = 120)
grid[3][3] = Button(checkerboard,width="35", height="35",text="空白",bg="white",image=space)
grid[3][3].place(x = 120, y = 120)
grid[4][3] = Button(checkerboard,width="35", height="35",text="空白",bg="silver",image=space)
grid[4][3].place(x = 160, y = 120)
grid[5][3] = Button(checkerboard,width="35", height="35",text="空白",bg="white",image=space)
grid[5][3].place(x = 200, y = 120)
grid[6][3] = Button(checkerboard,width="35", height="35",text="空白",bg="silver",image=space)
grid[6][3].place(x = 240, y = 120)
grid[7][3] = Button(checkerboard,width="35", height="35",text="空白",bg="white",image=space)
grid[7][3].place(x = 280, y = 120)

grid[0][4] = Button(checkerboard,width="35", height="35",text="空白",bg="white",image=space)
grid[0][4].place(x = 0, y = 160)
grid[1][4] = Button(checkerboard,width="35", height="35",text="空白",bg="silver",image=space)
grid[1][4].place(x = 40, y = 160)
grid[2][4] = Button(checkerboard,width="35", height="35",text="空白",bg="white",image=space)
grid[2][4].place(x = 80, y = 160)
grid[3][4] = Button(checkerboard,width="35", height="35",text="空白",bg="silver",image=space)
grid[3][4].place(x = 120, y = 160)
grid[4][4] = Button(checkerboard,width="35", height="35",text="空白",bg="white",image=space)
grid[4][4].place(x = 160, y = 160)
grid[5][4] = Button(checkerboard,width="35", height="35",text="空白",bg="silver",image=space)
grid[5][4].place(x = 200, y = 160)
grid[6][4] = Button(checkerboard,width="35", height="35",text="空白",bg="white",image=space)
grid[6][4].place(x = 240, y = 160)
grid[7][4] = Button(checkerboard,width="35", height="35",text="空白",bg="silver",image=space)
grid[7][4].place(x = 280, y = 160)

grid[0][5] = Button(checkerboard,width="35", height="35",text="空白",bg="silver",image=space)
grid[0][5].place(x = 0, y = 200)
grid[1][5] = Button(checkerboard,width="35", height="35",text="空白",bg="white",image=space)
grid[1][5].place(x = 40, y = 200)
grid[2][5] = Button(checkerboard,width="35", height="35",text="空白",bg="silver",image=space)
grid[2][5].place(x = 80, y = 200)
grid[3][5] = Button(checkerboard,width="35", height="35",text="空白",bg="white",image=space)
grid[3][5].place(x = 120, y = 200)
grid[4][5] = Button(checkerboard,width="35", height="35",text="空白",bg="silver",image=space)
grid[4][5].place(x = 160, y = 200)
grid[5][5] = Button(checkerboard,width="35", height="35",text="空白",bg="white",image=space)
grid[5][5].place(x = 200, y = 200)
grid[6][5] = Button(checkerboard,width="35", height="35",text="空白",bg="silver",image=space)
grid[6][5].place(x = 240, y = 200)
grid[7][5] = Button(checkerboard,width="35", height="35",text="空白",bg="white",image=space)
grid[7][5].place(x = 280, y = 200)

grid[0][6] = Button(checkerboard,width="35", height="35",text="白兵",bg="white",image=whitePawn)
grid[0][6].place(x = 0, y = 240)
grid[1][6] = Button(checkerboard,width="35", height="35",text="白兵",bg="silver",image=whitePawn)
grid[1][6].place(x = 40, y = 240)
grid[2][6] = Button(checkerboard,width="35", height="35",text="白兵",bg="white",image=whitePawn)
grid[2][6].place(x = 80, y = 240)
grid[3][6] = Button(checkerboard,width="35", height="35",text="白兵",bg="silver",image=whitePawn)
grid[3][6].place(x = 120, y = 240)
grid[4][6] = Button(checkerboard,width="35", height="35",text="白兵",bg="white",image=whitePawn)
grid[4][6].place(x = 160, y = 240)
grid[5][6] = Button(checkerboard,width="35", height="35",text="白兵",bg="silver",image=whitePawn)
grid[5][6].place(x = 200, y = 240)
grid[6][6] = Button(checkerboard,width="35", height="35",text="白兵",bg="white",image=whitePawn)
grid[6][6].place(x = 240, y = 240)
grid[7][6] = Button(checkerboard,width="35", height="35",text="白兵",bg="silver",image=whitePawn)
grid[7][6].place(x = 280, y = 240)

grid[0][7] = Button(checkerboard,width="35", height="35",text="白城堡",bg="silver",image=whiteRook)
grid[0][7].place(x = 0, y = 280)
grid[1][7] = Button(checkerboard,width="35", height="35",text="白騎士",bg="white",image=whiteKnight)
grid[1][7].place(x = 40, y = 280)
grid[2][7] = Button(checkerboard,width="35", height="35",text="白主教",bg="silver",image=whiteBishop)
grid[2][7].place(x = 80, y = 280)
grid[3][7] = Button(checkerboard,width="35", height="35",text="白皇后",bg="white",image=whiteQueen)
grid[3][7].place(x = 120, y = 280)
grid[4][7] = Button(checkerboard,width="35", height="35",text="白國王",bg="silver",image=whiteKing)
grid[4][7].place(x = 160, y = 280)
grid[5][7] = Button(checkerboard,width="35", height="35",text="白主教",bg="white",image=whiteBishop)
grid[5][7].place(x = 200, y = 280)
grid[6][7] = Button(checkerboard,width="35", height="35",text="白騎士",bg="silver",image=whiteKnight)
grid[6][7].place(x = 240, y = 280)
grid[7][7] = Button(checkerboard,width="35", height="35",text="白城堡",bg="white",image=whiteRook)
grid[7][7].place(x = 280, y = 280)

#用來顯示出拿著的是什麼棋子
holdchessname = Button(checkerboard,width="8", height="2",text="",fg="black",bg="white")
holdchessname.place(x = 525, y = 220)
#"神的空白塊"用來對應是否為空白塊；"跑步的時刻"用來紀錄有關─吃過路兵─
GodSpace = Button(checkerboard,width="35", height="35",text="神的空白塊",bg="white",image=space)
GodSpace.place(x = 5000, y = 5000)
runtime = Button(checkerboard,width=0, height="35",text="跑步的時刻",bg="white",image=space)
runtime.place(x = 5000, y = 5000)
"""
def docheckerboardthing(place):
	global holdchess

	if holdchess==0 :
		if place["image"]==GodSpace["image"] :
			print("空白格")
		else :
			canput=noPutEnemyChess(place,bout)
			if canput==1 :
				holdchess=place
				holdchessname["text"]=holdchess["text"]
				if runtime["width"]!=0 :
					checkChess(place,grid,bout,runtime)
				else:
					checkChess(place,grid,bout)
				n=checkNoDraw(grid)
				if n==0 :
					print("此棋子沒有合法的移動格")
					holdchessname["text"]=""
					holdchess=0
	elif place["bg"]=="green" or place["bg"]=="red" :
		canmove=noMoveOwnChess(place,holdchess)
		if canmove==1 :
			movechess(place)
	else :
		print("不合法的移動")
"""
#用來判斷點擊按鈕(棋子)的所有事情
def docheckerboardthing(place):
	global holdchess          #用來指到全域的變數

	if holdchess==0 :         #如果沒有拿著棋子的話
		if place["image"]==GodSpace["image"] :      #如果按到的是空白的格子
			print("空白格")
		else :                                      #如果按到的不是空白的格子
			canput=noPutEnemyChess(place,bout)      #運用函式庫的函式判斷是否為己方棋子
			if canput==1 :                          #是己方棋子的話
				holdchess=place                     #拿起按到的棋子
				holdchessname["text"]=holdchess["text"]     #將右下的顯示改為拿著的棋子
				if runtime["width"]!=0 :            #如果有士兵跑兩格的話
					checkChess(place,grid,bout,runtime)     #呼叫函式庫的函式，大致是用來亮格子。多傳"跑步的時刻"按鈕
				else:                               #如果沒有士兵跑兩格的話
					checkChess(place,grid,bout)          #呼叫函式庫的函式，大致是用來亮格子
				n=checkNoDraw(grid)                 #呼叫函式庫的函式，看是否都沒有格子亮起(沒有可移動的格子)
				if n==0 :                           #如果沒有格子亮起(沒有可移動的格子)
					print("此棋子沒有合法的移動格")      #印出提醒訊息
					holdchessname["text"]=""        #將右下的顯示改回空的
					holdchess=0                     #設定為沒有拿著棋子
	elif place["text"][0]==bout["text"][0] :        #如果有拿著棋子而且又按到己方的棋子
		returncolor(grid)                           #回復棋盤顏色
		holdchess=place                             #拿起按到的棋子
		holdchessname["text"]=holdchess["text"]     #將右下的顯示改為拿著的棋子
		if runtime["width"]!=0 :                    #如果有士兵跑兩格的話
			runtime["width"]=runtime["width"]%10    #用來恢復為正確的"跑步代碼"
			checkChess(place,grid,bout,runtime)     #呼叫函式庫的函式，大致是用來亮格子。多傳"跑步的時刻"按鈕
		else:                                       #如果沒有士兵跑兩格的話
			checkChess(place,grid,bout)             #呼叫函式庫的函式，大致是用來亮格子
		n=checkNoDraw(grid)                         #呼叫函式庫的函式，看是否都沒有格子亮起(沒有可移動的格子)
		if n==0 :                                   #如果沒有格子亮起(沒有可移動的格子)
			print("此棋子沒有合法的移動格")              #印出提醒訊息
			holdchessname["text"]=""                #將右下的顯示改回空的
			holdchess=0                             #設定為沒有拿著棋子
	elif place["bg"]=="green" or place["bg"]=="red" :      #如果欲移動的位置是紅色或綠色
		movechess(place)                            #呼叫movechess()函式：用來移動
	else :                                          #如果欲移動的位置不是紅色或綠色
		print("不合法的移動")                       #印出提醒訊息，"不"呼叫movechess()函式

#一系列的按鈕(棋子)對應的函式
def putchessa8():                        #建立函式
	docheckerboardthing(grid[0][0])      #呼叫docheckerboardthing()，並傳入按鈕當變數。(也就是上面那個)
grid[0][0]["command"]=putchessa8         #把函式附著上按鈕
def putchessb8():
	docheckerboardthing(grid[1][0])
grid[1][0]["command"]=putchessb8
def putchessc8():
	docheckerboardthing(grid[2][0])
grid[2][0]["command"]=putchessc8
def putchessd8():
	docheckerboardthing(grid[3][0])
grid[3][0]["command"]=putchessd8
def putchesse8():
	docheckerboardthing(grid[4][0])
grid[4][0]["command"]=putchesse8
def putchessf8():
	docheckerboardthing(grid[5][0])
grid[5][0]["command"]=putchessf8
def putchessg8():
	docheckerboardthing(grid[6][0])
grid[6][0]["command"]=putchessg8
def putchessh8():
	docheckerboardthing(grid[7][0])
grid[7][0]["command"]=putchessh8

def putchessa7():
	docheckerboardthing(grid[0][1])
grid[0][1]["command"]=putchessa7
def putchessb7():
	docheckerboardthing(grid[1][1])
grid[1][1]["command"]=putchessb7
def putchessc7():
	docheckerboardthing(grid[2][1])
grid[2][1]["command"]=putchessc7
def putchessd7():
	docheckerboardthing(grid[3][1])
grid[3][1]["command"]=putchessd7
def putchesse7():
	docheckerboardthing(grid[4][1])
grid[4][1]["command"]=putchesse7
def putchessf7():
	docheckerboardthing(grid[5][1])
grid[5][1]["command"]=putchessf7
def putchessg7():
	docheckerboardthing(grid[6][1])
grid[6][1]["command"]=putchessg7
def putchessh7():
	docheckerboardthing(grid[7][1])
grid[7][1]["command"]=putchessh7

def putchessa6():
	docheckerboardthing(grid[0][2])
grid[0][2]["command"]=putchessa6
def putchessb6():
	docheckerboardthing(grid[1][2])
grid[1][2]["command"]=putchessb6
def putchessc6():
	docheckerboardthing(grid[2][2])
grid[2][2]["command"]=putchessc6
def putchessd6():
	docheckerboardthing(grid[3][2])
grid[3][2]["command"]=putchessd6
def putchesse6():
	docheckerboardthing(grid[4][2])
grid[4][2]["command"]=putchesse6
def putchessf6():
	docheckerboardthing(grid[5][2])
grid[5][2]["command"]=putchessf6
def putchessg6():
	docheckerboardthing(grid[6][2])
grid[6][2]["command"]=putchessg6
def putchessh6():
	docheckerboardthing(grid[7][2])
grid[7][2]["command"]=putchessh6

def putchessa5():
	docheckerboardthing(grid[0][3])
grid[0][3]["command"]=putchessa5
def putchessb5():
	docheckerboardthing(grid[1][3])
grid[1][3]["command"]=putchessb5
def putchessc5():
	docheckerboardthing(grid[2][3])
grid[2][3]["command"]=putchessc5
def putchessd5():
	docheckerboardthing(grid[3][3])
grid[3][3]["command"]=putchessd5
def putchesse5():
	docheckerboardthing(grid[4][3])
grid[4][3]["command"]=putchesse5
def putchessf5():
	docheckerboardthing(grid[5][3])
grid[5][3]["command"]=putchessf5
def putchessg5():
	docheckerboardthing(grid[6][3])
grid[6][3]["command"]=putchessg5
def putchessh5():
	docheckerboardthing(grid[7][3])
grid[7][3]["command"]=putchessh5

def putchessa4():
	docheckerboardthing(grid[0][4])
grid[0][4]["command"]=putchessa4
def putchessb4():
	docheckerboardthing(grid[1][4])
grid[1][4]["command"]=putchessb4
def putchessc4():
	docheckerboardthing(grid[2][4])
grid[2][4]["command"]=putchessc4
def putchessd4():
	docheckerboardthing(grid[3][4])
grid[3][4]["command"]=putchessd4
def putchesse4():
	docheckerboardthing(grid[4][4])
grid[4][4]["command"]=putchesse4
def putchessf4():
	docheckerboardthing(grid[5][4])
grid[5][4]["command"]=putchessf4
def putchessg4():
	docheckerboardthing(grid[6][4])
grid[6][4]["command"]=putchessg4
def putchessh4():
	docheckerboardthing(grid[7][4])
grid[7][4]["command"]=putchessh4

def putchessa3():
	docheckerboardthing(grid[0][5])
grid[0][5]["command"]=putchessa3
def putchessb3():
	docheckerboardthing(grid[1][5])
grid[1][5]["command"]=putchessb3
def putchessc3():
	docheckerboardthing(grid[2][5])
grid[2][5]["command"]=putchessc3
def putchessd3():
	docheckerboardthing(grid[3][5])
grid[3][5]["command"]=putchessd3
def putchesse3():
	docheckerboardthing(grid[4][5])
grid[4][5]["command"]=putchesse3
def putchessf3():
	docheckerboardthing(grid[5][5])
grid[5][5]["command"]=putchessf3
def putchessg3():
	docheckerboardthing(grid[6][5])
grid[6][5]["command"]=putchessg3
def putchessh3():
	docheckerboardthing(grid[7][5])
grid[7][5]["command"]=putchessh3

def putchessa2():
	docheckerboardthing(grid[0][6])
grid[0][6]["command"]=putchessa2
def putchessb2():
	docheckerboardthing(grid[1][6])
grid[1][6]["command"]=putchessb2
def putchessc2():
	docheckerboardthing(grid[2][6])
grid[2][6]["command"]=putchessc2
def putchessd2():
	docheckerboardthing(grid[3][6])
grid[3][6]["command"]=putchessd2
def putchesse2():
	docheckerboardthing(grid[4][6])
grid[4][6]["command"]=putchesse2
def putchessf2():
	docheckerboardthing(grid[5][6])
grid[5][6]["command"]=putchessf2
def putchessg2():
	docheckerboardthing(grid[6][6])
grid[6][6]["command"]=putchessg2
def putchessh2():
	docheckerboardthing(grid[7][6])
grid[7][6]["command"]=putchessh2

def putchessa1():
	docheckerboardthing(grid[0][7])
grid[0][7]["command"]=putchessa1
def putchessb1():
	docheckerboardthing(grid[1][7])
grid[1][7]["command"]=putchessb1
def putchessc1():
	docheckerboardthing(grid[2][7])
grid[2][7]["command"]=putchessc1
def putchessd1():
	docheckerboardthing(grid[3][7])
grid[3][7]["command"]=putchessd1
def putchesse1():
	docheckerboardthing(grid[4][7])
grid[4][7]["command"]=putchesse1
def putchessf1():
	docheckerboardthing(grid[5][7])
grid[5][7]["command"]=putchessf1
def putchessg1():
	docheckerboardthing(grid[6][7])
grid[6][7]["command"]=putchessg1
def putchessh1():
	docheckerboardthing(grid[7][7])
grid[7][7]["command"]=putchessh1

"""

def putchessg2():
	global holdchess
	if holdchess==0 :
		if g2["image"]==GodSpace["image"] :
			print("空白格")
			return
		else :
			holdchess=g2
	else :
		movechess(g2)
g2["command"]=putchessg2

def putchessh2():
	global holdchess
	if holdchess==0 :
		if h2["image"]==GodSpace["image"] :
			print("空白格")
			return
		else :
			holdchess=h2
	else :
		movechess(h2)
h2["command"]=putchessh2

"""

def movechess(place):              #用來移動棋子
	global holdchess               #用來指到全域的變數
	"""
	if place==holdchess :
		print(place["text"])
		print(holdchess["text"])
		print("同個")

	else :
	"""
	saveStep()                     #用來紀錄上一步
	if runtime["width"]>=10 :          #如果有士兵跑起來，和有對應的敵方士兵符合吃的資格的話
		if place["text"]=="空白" :         #如果移動的位置是空的
			x,y=checkChessWhere(place,grid)     #呼叫函式庫的函式，用來確認移動的位置
			if bout["text"]=="白色方" :               #如果現在是白色方
				if grid[x][y+1]["bg"]=="orange" :     #如果移動的格子下方一格是橘色的話
					smallchess(grid[x][y+1])          #顯示"移動的格子下方一格"的那顆棋子的小圖
					grid[x][y+1]["image"]=space       #"移動的格子下方一格"的圖改為space
					grid[x][y+1]["text"]="空白"       #"移動的格子下方一格"的資訊改為"空白"
			if bout["text"]=="黑色方" :               #如果現在是白色方
				if grid[x][y-1]["bg"]=="orange" :     #如果移動的格子上方一格是橘色的話
					smallchess(grid[x][y-1])          #顯示"移動的格子上方一格"的那顆棋子的小圖
					grid[x][y-1]["image"]=space       #"移動的格子上方一格"的圖改為space
					grid[x][y-1]["text"]="空白"       #"移動的格子上方一格"的資訊改為"空白"
	runtime["width"]=0                          #將"跑步的時刻"的資料改回0，用來赦免上一回合跑步的士兵(如果他還沒死的話...)
	if holdchess["text"][-1]=="兵" :            #如果移動的是士兵的話
		i,j=checkChessWhere(holdchess,grid)     #呼叫函式庫的函式，用來確認當前的位置
		x,y=checkChessWhere(place,grid)         #呼叫函式庫的函式，用來確認移動的位置
		if (j-y>1) or (j-y<-1) :                #如果移動的士兵跑了一格(直的)以上的話
			runtime["width"]=x                  #將棋子 ─移動的士兵─ 的"行"位置紀錄

	returncolor(grid)                     #回復棋盤顏色
	smallchess(place)                     #顯示"移動的格子"的那顆棋子的小圖
	place["image"]=holdchess["image"]     #將"移動目的地"的格子的圖片改為"移動的棋子"的圖
	holdchess["image"]=space              #"移動的棋子"的圖改為space
	place["text"]=holdchess["text"]       #將"移動目的地"的格子的"text"改為"移動的棋子"的"text"
	holdchess["text"]="空白"              #"移動的棋子"的圖改為"空白"
	holdchess=0                           #設定為沒有拿著棋子
	z=upupup(grid,whiteQueen,blackQueen)  #呼叫函式庫的函式，檢查有沒有符合升變的士兵
	if z!=0 :                             #如果有升變
		smallchessupchange(z)             #呼叫函式代入變數z
	change()                              #呼叫change()函式，主要是改回合方



player1 = Entry(checkerboard,width="10")    #可以輸入玩家名稱的文字格子
player1.place(x = 330, y = 140)             #設定文字格子的位置
player2 = Entry(checkerboard,width="10")    #可以輸入玩家名稱的文字格子
player2.place(x = 420, y = 140)             #設定文字格子的位置

first = Label(checkerboard,text="誰先手?",width="10")    #寫出"誰先手?"的文字方塊
first.place(x = 390, y = 169)               #設定文字方塊的位置

coin = Button(checkerboard,width="5", height="1",text="擲硬幣",bg="white")   #按鈕，用來按下OwO，會呼叫函式用來判斷誰先手
coin.place(x = 330, y = 165)        #按鈕位置

def throwcoin():                    #用來判斷誰先手的函式
	a=player1.get()                 #從player1取得使用者輸入
	b=player2.get()                 #從player2取得使用者輸入
	player=[a,b]                    #做player列表
	c=random.choice(player)         #從列表player中做亂數選擇
	first["text"]=c                 #"誰先手?"的文字方塊的"text"改為選出的先手的玩家
coin["command"]=throwcoin           #將函式附著上按鈕

bout = Button(checkerboard,width="10", height="2",text="白色方",fg="black",bg="white")    #顯示回合方的按鈕
bout.place(x = 518, y = 270)        #按鈕位置

def change():                         #用來變換回合方的函式
	if bout["text"]=="白色方" :       #如果現在是"白色方"
		bout["text"]="黑色方"         #改為"黑色方"
		bout["fg"]="white"            #將回合方的字體顏色改為白色
		bout["bg"]="black"            #將回合方的背景顏色改為黑色
		holdchessname["text"]=""      #將顯示拿著什麼棋子的按鈕的"text"改為空白
		holdchessname["fg"]="white"   #將顯示拿著什麼棋子的按鈕的字體顏色改為白色
		holdchessname["bg"]="black"   #將顯示拿著什麼棋子的按鈕的背景顏色改為黑色
	else :                            #如果現在不是"白色方"，也就是"黑色方"
		bout["text"]="白色方"         #改為"白色方"
		bout["fg"]="black"            #將回合方的字體顏色改為黑色
		bout["bg"]="white"            #將回合方的背景顏色改為白色
		holdchessname["text"]=""      #將顯示拿著什麼棋子的按鈕的"text"改為空白
		holdchessname["fg"]="black"   #將顯示拿著什麼棋子的按鈕的字體顏色改為黑色
		holdchessname["bg"]="white"   #將顯示拿著什麼棋子的按鈕的背景顏色改為白色
#建立變數，將圖片宣告上(這裡是死掉的棋子)
smallblackKing = Button(checkerboard,width="25", height="25",text="",bg="white",image=space,bd="0")
smallblackKing.place(x = 330, y = 5)
smallblackQueen = Button(checkerboard,width="25", height="25",text="",bg="white",image=space,bd="0")
smallblackQueen.place(x = 355, y = 5)
smallblackRook1 = Button(checkerboard,width="25", height="25",text="",bg="white",image=space,bd="0")
smallblackRook1.place(x = 380, y = 5)
smallblackRook2 = Button(checkerboard,width="25", height="25",text="",bg="white",image=space,bd="0")
smallblackRook2.place(x = 405, y = 5)
smallblackBishop1 = Button(checkerboard,width="25", height="25",text="",bg="white",image=space,bd="0")
smallblackBishop1.place(x = 330, y = 30)
smallblackBishop2 = Button(checkerboard,width="25", height="25",text="",bg="white",image=space,bd="0")
smallblackBishop2.place(x = 355, y = 30)
smallblackKnight1 = Button(checkerboard,width="25", height="25",text="",bg="white",image=space,bd="0")
smallblackKnight1.place(x = 380, y = 30)
smallblackKnight2 = Button(checkerboard,width="25", height="25",text="",bg="white",image=space,bd="0")
smallblackKnight2.place(x = 405, y = 30)
smallblackPawn1 = Button(checkerboard,width="25", height="25",text="",bg="white",image=space,bd="0")
smallblackPawn1.place(x = 330, y = 55)
smallblackPawn2 = Button(checkerboard,width="25", height="25",text="",bg="white",image=space,bd="0")
smallblackPawn2.place(x = 355, y = 55)
smallblackPawn3 = Button(checkerboard,width="25", height="25",text="",bg="white",image=space,bd="0")
smallblackPawn3.place(x = 380, y = 55)
smallblackPawn4 = Button(checkerboard,width="25", height="25",text="",bg="white",image=space,bd="0")
smallblackPawn4.place(x = 405, y = 55)
smallblackPawn5 = Button(checkerboard,width="25", height="25",text="",bg="white",image=space,bd="0")
smallblackPawn5.place(x = 330, y = 80)
smallblackPawn6 = Button(checkerboard,width="25", height="25",text="",bg="white",image=space,bd="0")
smallblackPawn6.place(x = 355, y = 80)
smallblackPawn7 = Button(checkerboard,width="25", height="25",text="",bg="white",image=space,bd="0")
smallblackPawn7.place(x = 380, y = 80)
smallblackPawn8 = Button(checkerboard,width="25", height="25",text="",bg="white",image=space,bd="0")
smallblackPawn8.place(x = 405, y = 80)

smallwhiteKing = Button(checkerboard,width="25", height="25",text="",bg="white",image=space,bd="0")
smallwhiteKing.place(x = 330, y = 290)
smallwhiteQueen = Button(checkerboard,width="25", height="25",text="",bg="white",image=space,bd="0")
smallwhiteQueen.place(x = 355, y = 290)
smallwhiteRook1 = Button(checkerboard,width="25", height="25",text="",bg="white",image=space,bd="0")
smallwhiteRook1.place(x = 380, y = 290)
smallwhiteRook2 = Button(checkerboard,width="25", height="25",text="",bg="white",image=space,bd="0")
smallwhiteRook2.place(x = 405, y = 290)
smallwhiteBishop1 = Button(checkerboard,width="25", height="25",text="",bg="white",image=space,bd="0")
smallwhiteBishop1.place(x = 330, y = 265)
smallwhiteBishop2 = Button(checkerboard,width="25", height="25",text="",bg="white",image=space,bd="0")
smallwhiteBishop2.place(x = 355, y = 265)
smallwhiteKnight1 = Button(checkerboard,width="25", height="25",text="",bg="white",image=space,bd="0")
smallwhiteKnight1.place(x = 380, y = 265)
smallwhiteKnight2 = Button(checkerboard,width="25", height="25",text="",bg="white",image=space,bd="0")
smallwhiteKnight2.place(x = 405, y = 265)
smallwhitePawn1 = Button(checkerboard,width="25", height="25",text="",bg="white",image=space,bd="0")
smallwhitePawn1.place(x = 330, y = 240)
smallwhitePawn2 = Button(checkerboard,width="25", height="25",text="",bg="white",image=space,bd="0")
smallwhitePawn2.place(x = 355, y = 240)
smallwhitePawn3 = Button(checkerboard,width="25", height="25",text="",bg="white",image=space,bd="0")
smallwhitePawn3.place(x = 380, y = 240)
smallwhitePawn4 = Button(checkerboard,width="25", height="25",text="",bg="white",image=space,bd="0")
smallwhitePawn4.place(x = 405, y = 240)
smallwhitePawn5 = Button(checkerboard,width="25", height="25",text="",bg="white",image=space,bd="0")
smallwhitePawn5.place(x = 330, y = 215)
smallwhitePawn6 = Button(checkerboard,width="25", height="25",text="",bg="white",image=space,bd="0")
smallwhitePawn6.place(x = 355, y = 215)
smallwhitePawn7 = Button(checkerboard,width="25", height="25",text="",bg="white",image=space,bd="0")
smallwhitePawn7.place(x = 380, y = 215)
smallwhitePawn8 = Button(checkerboard,width="25", height="25",text="",bg="white",image=space,bd="0")
smallwhitePawn8.place(x = 405, y = 215)
#判斷死掉的棋子，並顯示小圖
def smallchess(chess):
	if chess["text"]=="黑國王" :
		smallblackKing["image"]=miniblackKing
		smallblackKing["text"]="黑國王"
		gameFinish("白")
	if chess["text"]=="黑皇后" :
		smallblackQueen["image"]=miniblackQueen
		smallblackQueen["text"]="黑皇后"
	if chess["text"]=="黑城堡" :
		if smallblackRook1["text"]!="黑城堡" :
			smallblackRook1["image"]=miniblackRook
			smallblackRook1["text"]="黑城堡"
		else :
			smallblackRook2["image"]=miniblackRook
			smallblackRook2["text"]="黑城堡"
	if chess["text"]=="黑主教" :
		if smallblackBishop1["text"]!="黑主教" :
			smallblackBishop1["image"]=miniblackBishop
			smallblackBishop1["text"]="黑主教"
		else :
			smallblackBishop2["image"]=miniblackBishop
			smallblackBishop2["text"]="黑主教"
	if chess["text"]=="黑騎士" :
		if smallblackKnight1["text"]!="黑騎士" :
			smallblackKnight1["image"]=miniblackKnight
			smallblackKnight1["text"]="黑騎士"
		else :
			smallblackKnight2["image"]=miniblackKnight
			smallblackKnight2["text"]="黑騎士"
	if chess["text"]=="黑兵" :
		if smallblackPawn1["text"]!="黑兵" :
			smallblackPawn1["image"]=miniblackPawn
			smallblackPawn1["text"]="黑兵"
		elif smallblackPawn2["text"]!="黑兵" :
			smallblackPawn2["image"]=miniblackPawn
			smallblackPawn2["text"]="黑兵"
		elif smallblackPawn3["text"]!="黑兵" :
			smallblackPawn3["image"]=miniblackPawn
			smallblackPawn3["text"]="黑兵"
		elif smallblackPawn4["text"]!="黑兵" :
			smallblackPawn4["image"]=miniblackPawn
			smallblackPawn4["text"]="黑兵"
		elif smallblackPawn5["text"]!="黑兵" :
			smallblackPawn5["image"]=miniblackPawn
			smallblackPawn5["text"]="黑兵"
		elif smallblackPawn6["text"]!="黑兵" :
			smallblackPawn6["image"]=miniblackPawn
			smallblackPawn6["text"]="黑兵"
		elif smallblackPawn7["text"]!="黑兵" :
			smallblackPawn7["image"]=miniblackPawn
			smallblackPawn7["text"]="黑兵"
		else :
			smallblackPawn8["image"]=miniblackPawn
			smallblackPawn8["text"]="黑兵"

	if chess["text"]=="白國王" :
		smallwhiteKing["image"]=miniwhiteKing
		smallwhiteKing["text"]="白國王"
		gameFinish("黑")
	if chess["text"]=="白皇后" :
		smallwhiteQueen["image"]=miniwhiteQueen
		smallwhiteQueen["text"]="白皇后"
	if chess["text"]=="白城堡" :
		if smallwhiteRook1["text"]!="白城堡" :
			smallwhiteRook1["image"]=miniwhiteRook
			smallwhiteRook1["text"]="白城堡"
		else :
			smallwhiteRook2["image"]=miniwhiteRook
			smallwhiteRook2["text"]="白城堡"
	if chess["text"]=="白主教" :
		if smallwhiteBishop1["text"]!="白主教" :
			smallwhiteBishop1["image"]=miniwhiteBishop
			smallwhiteBishop1["text"]="白主教"
		else :
			smallwhiteBishop2["image"]=miniwhiteBishop
			smallwhiteBishop2["text"]="白主教"
	if chess["text"]=="白騎士" :
		if smallwhiteKnight1["text"]!="白騎士" :
			smallwhiteKnight1["image"]=miniwhiteKnight
			smallwhiteKnight1["text"]="白騎士"
		else :
			smallwhiteKnight2["image"]=miniwhiteKnight
			smallwhiteKnight2["text"]="白騎士"
	if chess["text"]=="白兵" :
		if smallwhitePawn1["text"]!="白兵" :
			smallwhitePawn1["image"]=miniwhitePawn
			smallwhitePawn1["text"]="白兵"
		elif smallwhitePawn2["text"]!="白兵" :
			smallwhitePawn2["image"]=miniwhitePawn
			smallwhitePawn2["text"]="白兵"
		elif smallwhitePawn3["text"]!="白兵" :
			smallwhitePawn3["image"]=miniwhitePawn
			smallwhitePawn3["text"]="白兵"
		elif smallwhitePawn4["text"]!="白兵" :
			smallwhitePawn4["image"]=miniwhitePawn
			smallwhitePawn4["text"]="白兵"
		elif smallwhitePawn5["text"]!="白兵" :
			smallwhitePawn5["image"]=miniwhitePawn
			smallwhitePawn5["text"]="白兵"
		elif smallwhitePawn6["text"]!="白兵" :
			smallwhitePawn6["image"]=miniwhitePawn
			smallwhitePawn6["text"]="白兵"
		elif smallwhitePawn7["text"]!="白兵" :
			smallwhitePawn7["image"]=miniwhitePawn
			smallwhitePawn7["text"]="白兵"
		else :
			smallwhitePawn8["image"]=miniwhitePawn
			smallwhitePawn8["text"]="白兵"
#判斷升變的士兵棋子(白或黑)，並顯示小圖
def smallchessupchange(z):
	if z==1 :
		if smallwhitePawn1["text"]!="白兵" :
			smallwhitePawn1["image"]=miniwhitePawn
			smallwhitePawn1["text"]="白兵"
		elif smallwhitePawn2["text"]!="白兵" :
			smallwhitePawn2["image"]=miniwhitePawn
			smallwhitePawn2["text"]="白兵"
		elif smallwhitePawn3["text"]!="白兵" :
			smallwhitePawn3["image"]=miniwhitePawn
			smallwhitePawn3["text"]="白兵"
		elif smallwhitePawn4["text"]!="白兵" :
			smallwhitePawn4["image"]=miniwhitePawn
			smallwhitePawn4["text"]="白兵"
		elif smallwhitePawn5["text"]!="白兵" :
			smallwhitePawn5["image"]=miniwhitePawn
			smallwhitePawn5["text"]="白兵"
		elif smallwhitePawn6["text"]!="白兵" :
			smallwhitePawn6["image"]=miniwhitePawn
			smallwhitePawn6["text"]="白兵"
		elif smallwhitePawn7["text"]!="白兵" :
			smallwhitePawn7["image"]=miniwhitePawn
			smallwhitePawn7["text"]="白兵"
		else :
			smallwhitePawn8["image"]=miniwhitePawn
			smallwhitePawn8["text"]="白兵"
	else :
		if smallblackPawn1["text"]!="黑兵" :
			smallblackPawn1["image"]=miniblackPawn
			smallblackPawn1["text"]="黑兵"
		elif smallblackPawn2["text"]!="黑兵" :
			smallblackPawn2["image"]=miniblackPawn
			smallblackPawn2["text"]="黑兵"
		elif smallblackPawn3["text"]!="黑兵" :
			smallblackPawn3["image"]=miniblackPawn
			smallblackPawn3["text"]="黑兵"
		elif smallblackPawn4["text"]!="黑兵" :
			smallblackPawn4["image"]=miniblackPawn
			smallblackPawn4["text"]="黑兵"
		elif smallblackPawn5["text"]!="黑兵" :
			smallblackPawn5["image"]=miniblackPawn
			smallblackPawn5["text"]="黑兵"
		elif smallblackPawn6["text"]!="黑兵" :
			smallblackPawn6["image"]=miniblackPawn
			smallblackPawn6["text"]="黑兵"
		elif smallblackPawn7["text"]!="黑兵" :
			smallblackPawn7["image"]=miniblackPawn
			smallblackPawn7["text"]="黑兵"
		else :
			smallblackPawn8["image"]=miniblackPawn
			smallblackPawn8["text"]="黑兵"
#勝利的圖~用按鈕來做
victory = Button(checkerboard,width="100", height="100",text="",bg="#F0F0F0",image=space,bd="0")
victory.place(x = 50000, y = 50000)    #勝利的圖的位置
def gameFinish(winner):                #結束的函式，會有勝利方的值代入
	if winner=="白" :                  #如果勝利的是白色方
		victory["image"]=whiteKingWin  #勝利的圖為白國王
	elif winner=="黑" :                #如果勝利的是黑色方
		victory["image"]=blackKingWin  #勝利的圖為黑國王
	victory.place(x = 500, y = 113)    #設定勝利的圖的位置到可以看見的位置

#存檔的函式
def saveCheckerboard():
	file=open("chessSave.csv","w")         #開一個新檔案chessSave.csv

	for i in range(8):                             #儲存所有格子
		for j in range(8):
			file.write(grid[i][j]["text"]+"\n")


	file.write(bout["fg"]+","+bout["bg"]+","+bout["text"]+"\n")

	file.write(smallblackKing["text"]+"\n")
	file.write(smallblackQueen["text"]+"\n")
	file.write(smallblackRook1["text"]+"\n")
	file.write(smallblackRook2["text"]+"\n")
	file.write(smallblackBishop1["text"]+"\n")
	file.write(smallblackBishop2["text"]+"\n")
	file.write(smallblackKnight1["text"]+"\n")
	file.write(smallblackKnight2["text"]+"\n")
	file.write(smallblackPawn1["text"]+"\n")
	file.write(smallblackPawn2["text"]+"\n")
	file.write(smallblackPawn3["text"]+"\n")
	file.write(smallblackPawn4["text"]+"\n")
	file.write(smallblackPawn5["text"]+"\n")
	file.write(smallblackPawn6["text"]+"\n")
	file.write(smallblackPawn7["text"]+"\n")
	file.write(smallblackPawn8["text"]+"\n")

	file.write(smallwhiteKing["text"]+"\n")
	file.write(smallwhiteQueen["text"]+"\n")
	file.write(smallwhiteRook1["text"]+"\n")
	file.write(smallwhiteRook2["text"]+"\n")
	file.write(smallwhiteBishop1["text"]+"\n")
	file.write(smallwhiteBishop2["text"]+"\n")
	file.write(smallwhiteKnight1["text"]+"\n")
	file.write(smallwhiteKnight2["text"]+"\n")
	file.write(smallwhitePawn1["text"]+"\n")
	file.write(smallwhitePawn2["text"]+"\n")
	file.write(smallwhitePawn3["text"]+"\n")
	file.write(smallwhitePawn4["text"]+"\n")
	file.write(smallwhitePawn5["text"]+"\n")
	file.write(smallwhitePawn6["text"]+"\n")
	file.write(smallwhitePawn7["text"]+"\n")
	file.write(smallwhitePawn8["text"]+"\n")

	rt=runtime["width"]%10
	file.write(str(rt)+"\n")

	print("儲存成功")
	file.close()
#讀檔的函式
def loadCheckerboard():
	global holdchess
	returncolor(grid)                     #回復棋盤顏色

	file=open("chessSave.csv","r")

	for i in range(8):
		for j in range(8):
			line=file.readline()                    #讀取一行
			line=line.strip()                       #去掉換行符號
			loadDoing(grid[i][j],line)              #用函式代入

	holdchess=0
	line=file.readline()
	line=line.strip()
	line=line.split(",")
	bout["fg"]=line[0]
	bout["bg"]=line[1]
	bout["text"]=line[2]
	holdchessname["fg"]=line[0]
	holdchessname["bg"]=line[1]
	holdchessname["text"]=""

	line=file.readline()
	line=line.strip()
	loadChecksmallchess(smallblackKing,line)
	line=file.readline()
	line=line.strip()
	loadChecksmallchess(smallblackQueen,line)
	line=file.readline()
	line=line.strip()
	loadChecksmallchess(smallblackRook1,line)
	line=file.readline()
	line=line.strip()
	loadChecksmallchess(smallblackRook2,line)
	line=file.readline()
	line=line.strip()
	loadChecksmallchess(smallblackBishop1,line)
	line=file.readline()
	line=line.strip()
	loadChecksmallchess(smallblackBishop2,line)
	line=file.readline()
	line=line.strip()
	loadChecksmallchess(smallblackKnight1,line)
	line=file.readline()
	line=line.strip()
	loadChecksmallchess(smallblackKnight2,line)
	line=file.readline()
	line=line.strip()
	loadChecksmallchess(smallblackPawn1,line)
	line=file.readline()
	line=line.strip()
	loadChecksmallchess(smallblackPawn2,line)
	line=file.readline()
	line=line.strip()
	loadChecksmallchess(smallblackPawn3,line)
	line=file.readline()
	line=line.strip()
	loadChecksmallchess(smallblackPawn4,line)
	line=file.readline()
	line=line.strip()
	loadChecksmallchess(smallblackPawn5,line)
	line=file.readline()
	line=line.strip()
	loadChecksmallchess(smallblackPawn6,line)
	line=file.readline()
	line=line.strip()
	loadChecksmallchess(smallblackPawn7,line)
	line=file.readline()
	line=line.strip()
	loadChecksmallchess(smallblackPawn8,line)

	line=file.readline()
	line=line.strip()
	loadChecksmallchess(smallwhiteKing,line)
	line=file.readline()
	line=line.strip()
	loadChecksmallchess(smallwhiteQueen,line)
	line=file.readline()
	line=line.strip()
	loadChecksmallchess(smallwhiteRook1,line)
	line=file.readline()
	line=line.strip()
	loadChecksmallchess(smallwhiteRook2,line)
	line=file.readline()
	line=line.strip()
	loadChecksmallchess(smallwhiteBishop1,line)
	line=file.readline()
	line=line.strip()
	loadChecksmallchess(smallwhiteBishop2,line)
	line=file.readline()
	line=line.strip()
	loadChecksmallchess(smallwhiteKnight1,line)
	line=file.readline()
	line=line.strip()
	loadChecksmallchess(smallwhiteKnight2,line)
	line=file.readline()
	line=line.strip()
	loadChecksmallchess(smallwhitePawn1,line)
	line=file.readline()
	line=line.strip()
	loadChecksmallchess(smallwhitePawn2,line)
	line=file.readline()
	line=line.strip()
	loadChecksmallchess(smallwhitePawn3,line)
	line=file.readline()
	line=line.strip()
	loadChecksmallchess(smallwhitePawn4,line)
	line=file.readline()
	line=line.strip()
	loadChecksmallchess(smallwhitePawn5,line)
	line=file.readline()
	line=line.strip()
	loadChecksmallchess(smallwhitePawn6,line)
	line=file.readline()
	line=line.strip()
	loadChecksmallchess(smallwhitePawn7,line)
	line=file.readline()
	line=line.strip()
	loadChecksmallchess(smallwhitePawn8,line)

	line=file.readline()
	line=line.strip()
	runtime["width"]=int(line)

	print("讀取成功")
	file.close()
#讀取所使用的支函式，有關棋盤上的是什麼棋子
def loadDoing(chess,line):
	chess["text"]=line
	#print(line)
	#print(chess["text"])
	if chess["text"]=="空白" :
		chess["image"]=space
	elif chess["text"]=="黑兵" :
		chess["image"]=blackPawn
	elif chess["text"]=="黑騎士" :
		chess["image"]=blackKnight
	elif chess["text"]=="黑主教" :
		chess["image"]=blackBishop
	elif chess["text"]=="黑城堡" :
		chess["image"]=blackRook
	elif chess["text"]=="黑皇后" :
		chess["image"]=blackQueen
	elif chess["text"]=="黑國王" :
		chess["image"]=blackKing
	elif chess["text"]=="白兵" :
		chess["image"]=whitePawn
	elif chess["text"]=="白騎士" :
		chess["image"]=whiteKnight
	elif chess["text"]=="白主教" :
		chess["image"]=whiteBishop
	elif chess["text"]=="白城堡" :
		chess["image"]=whiteRook
	elif chess["text"]=="白皇后" :
		chess["image"]=whiteQueen
	elif chess["text"]=="白國王" :
		chess["image"]=whiteKing
#讀取所使用的支函式，有關小圖示
def loadChecksmallchess(chess,line):
	chess["text"]=line
	if chess["text"]=="" :
		chess["image"]=space
	elif chess["text"]=="黑兵" :
		chess["image"]=miniblackPawn
	elif chess["text"]=="黑騎士" :
		chess["image"]=miniblackKnight
	elif chess["text"]=="黑主教" :
		chess["image"]=miniblackBishop
	elif chess["text"]=="黑城堡" :
		chess["image"]=miniblackRook
	elif chess["text"]=="黑皇后" :
		chess["image"]=miniblackQueen
	elif chess["text"]=="黑國王" :
		chess["image"]=miniblackKing
	elif chess["text"]=="白兵" :
		chess["image"]=miniwhitePawn
	elif chess["text"]=="白騎士" :
		chess["image"]=miniwhiteKnight
	elif chess["text"]=="白主教" :
		chess["image"]=miniwhiteBishop
	elif chess["text"]=="白城堡" :
		chess["image"]=miniwhiteRook
	elif chess["text"]=="白皇后" :
		chess["image"]=miniwhiteQueen
	elif chess["text"]=="白國王" :
		chess["image"]=miniwhiteKing
#存檔的按鈕
saveCheckerboardButton=Button(checkerboard,width="10", height="2",text="存檔",bg="white",command=saveCheckerboard)
saveCheckerboardButton.place(x = 518, y = 20)   #存檔的按鈕的位置
#讀檔的按鈕
loadCheckerboardButton=Button(checkerboard,width="10", height="2",text="載入存檔",bg="white",command=loadCheckerboard)
loadCheckerboardButton.place(x = 518, y = 70)   #讀檔的按鈕的位置

#儲存上一步的函式
def saveStep():
	file=open("chessSaveStep.csv","w")         #開一個新檔案chessSaveStep.csv

	for i in range(8):                             #儲存所有格子
		for j in range(8):
			file.write(grid[i][j]["text"]+"\n")


	file.write(bout["fg"]+","+bout["bg"]+","+bout["text"]+"\n")

	file.write(smallblackKing["text"]+"\n")
	file.write(smallblackQueen["text"]+"\n")
	file.write(smallblackRook1["text"]+"\n")
	file.write(smallblackRook2["text"]+"\n")
	file.write(smallblackBishop1["text"]+"\n")
	file.write(smallblackBishop2["text"]+"\n")
	file.write(smallblackKnight1["text"]+"\n")
	file.write(smallblackKnight2["text"]+"\n")
	file.write(smallblackPawn1["text"]+"\n")
	file.write(smallblackPawn2["text"]+"\n")
	file.write(smallblackPawn3["text"]+"\n")
	file.write(smallblackPawn4["text"]+"\n")
	file.write(smallblackPawn5["text"]+"\n")
	file.write(smallblackPawn6["text"]+"\n")
	file.write(smallblackPawn7["text"]+"\n")
	file.write(smallblackPawn8["text"]+"\n")

	file.write(smallwhiteKing["text"]+"\n")
	file.write(smallwhiteQueen["text"]+"\n")
	file.write(smallwhiteRook1["text"]+"\n")
	file.write(smallwhiteRook2["text"]+"\n")
	file.write(smallwhiteBishop1["text"]+"\n")
	file.write(smallwhiteBishop2["text"]+"\n")
	file.write(smallwhiteKnight1["text"]+"\n")
	file.write(smallwhiteKnight2["text"]+"\n")
	file.write(smallwhitePawn1["text"]+"\n")
	file.write(smallwhitePawn2["text"]+"\n")
	file.write(smallwhitePawn3["text"]+"\n")
	file.write(smallwhitePawn4["text"]+"\n")
	file.write(smallwhitePawn5["text"]+"\n")
	file.write(smallwhitePawn6["text"]+"\n")
	file.write(smallwhitePawn7["text"]+"\n")
	file.write(smallwhitePawn8["text"]+"\n")

	rt=runtime["width"]%10
	file.write(str(rt)+"\n")

	file.close()
	loadStepButton.place(x = 450, y = 200)
#讀取上一步的函式
def loadStep():
	global holdchess
	returncolor(grid)

	file=open("chessSaveStep.csv","r")

	for i in range(8):
		for j in range(8):
			line=file.readline()                    #讀取一行
			line=line.strip()                       #去掉換行符號
			loadDoing(grid[i][j],line)              #用函式代入

	holdchess=0
	line=file.readline()
	line=line.strip()
	line=line.split(",")
	bout["fg"]=line[0]
	bout["bg"]=line[1]
	bout["text"]=line[2]
	holdchessname["fg"]=line[0]
	holdchessname["bg"]=line[1]
	holdchessname["text"]=""

	line=file.readline()
	line=line.strip()
	loadChecksmallchess(smallblackKing,line)
	line=file.readline()
	line=line.strip()
	loadChecksmallchess(smallblackQueen,line)
	line=file.readline()
	line=line.strip()
	loadChecksmallchess(smallblackRook1,line)
	line=file.readline()
	line=line.strip()
	loadChecksmallchess(smallblackRook2,line)
	line=file.readline()
	line=line.strip()
	loadChecksmallchess(smallblackBishop1,line)
	line=file.readline()
	line=line.strip()
	loadChecksmallchess(smallblackBishop2,line)
	line=file.readline()
	line=line.strip()
	loadChecksmallchess(smallblackKnight1,line)
	line=file.readline()
	line=line.strip()
	loadChecksmallchess(smallblackKnight2,line)
	line=file.readline()
	line=line.strip()
	loadChecksmallchess(smallblackPawn1,line)
	line=file.readline()
	line=line.strip()
	loadChecksmallchess(smallblackPawn2,line)
	line=file.readline()
	line=line.strip()
	loadChecksmallchess(smallblackPawn3,line)
	line=file.readline()
	line=line.strip()
	loadChecksmallchess(smallblackPawn4,line)
	line=file.readline()
	line=line.strip()
	loadChecksmallchess(smallblackPawn5,line)
	line=file.readline()
	line=line.strip()
	loadChecksmallchess(smallblackPawn6,line)
	line=file.readline()
	line=line.strip()
	loadChecksmallchess(smallblackPawn7,line)
	line=file.readline()
	line=line.strip()
	loadChecksmallchess(smallblackPawn8,line)

	line=file.readline()
	line=line.strip()
	loadChecksmallchess(smallwhiteKing,line)
	line=file.readline()
	line=line.strip()
	loadChecksmallchess(smallwhiteQueen,line)
	line=file.readline()
	line=line.strip()
	loadChecksmallchess(smallwhiteRook1,line)
	line=file.readline()
	line=line.strip()
	loadChecksmallchess(smallwhiteRook2,line)
	line=file.readline()
	line=line.strip()
	loadChecksmallchess(smallwhiteBishop1,line)
	line=file.readline()
	line=line.strip()
	loadChecksmallchess(smallwhiteBishop2,line)
	line=file.readline()
	line=line.strip()
	loadChecksmallchess(smallwhiteKnight1,line)
	line=file.readline()
	line=line.strip()
	loadChecksmallchess(smallwhiteKnight2,line)
	line=file.readline()
	line=line.strip()
	loadChecksmallchess(smallwhitePawn1,line)
	line=file.readline()
	line=line.strip()
	loadChecksmallchess(smallwhitePawn2,line)
	line=file.readline()
	line=line.strip()
	loadChecksmallchess(smallwhitePawn3,line)
	line=file.readline()
	line=line.strip()
	loadChecksmallchess(smallwhitePawn4,line)
	line=file.readline()
	line=line.strip()
	loadChecksmallchess(smallwhitePawn5,line)
	line=file.readline()
	line=line.strip()
	loadChecksmallchess(smallwhitePawn6,line)
	line=file.readline()
	line=line.strip()
	loadChecksmallchess(smallwhitePawn7,line)
	line=file.readline()
	line=line.strip()
	loadChecksmallchess(smallwhitePawn8,line)

	line=file.readline()
	line=line.strip()
	runtime["width"]=int(line)

	#print("完成毀棋")
	file.close()
	loadStepButton.place(x = 50000, y = 200)
#上一步的按鈕
loadStepButton=Button(checkerboard,width="5", height=1,text="上一步",bg="white",command=loadStep)
loadStepButton.place(x = 50000, y = 200)    #上一步的按鈕位置



def special1():
	global holdchess
	bout["text"]="白色方"
	bout["fg"]="black"
	bout["bg"]="white"
	holdchessname["text"]=""
	holdchessname["fg"]="black"
	holdchessname["bg"]="white"
	holdchess=0

def special2():
	global holdchess
	bout["text"]="黑色方"
	bout["fg"]="white"
	bout["bg"]="black"
	holdchessname["text"]=""
	holdchessname["fg"]="white"
	holdchessname["bg"]="black"
	holdchess=0

specialButton1=Button(checkerboard,width="10", height="2",text="安安",bg="white",command=special1,fg="white")
specialButton1.place(x = 630, y = 70)
specialButton2=Button(checkerboard,width="10", height="2",text="安安",bg="black",command=special2)
specialButton2.place(x = 630, y = 120)

checkerboard.mainloop()


"""

def do(a):
	a=Tk()
	a=dd()

class dd:
	def __init__(self):
		self.createWidgets()
	def createWidgets(self):
		self.inputText = Label(self)
		self.inputText["text"] = "Input:"
		self.inputText.grid(row=0, column=0)
		self.inputField = Entry(self)
		self.inputField["width"] = 50
		self.inputField.grid(row=0, column=1, columnspan=6)

		self.outputText = Label(self)
		self.outputText["text"] = "Output:"
		self.outputText.grid(row=1, column=0)
		self.outputField = Entry(self)
		self.outputField["width"] = 50
		self.outputField.grid(row=1, column=1, columnspan=6)

		self.new = Button(self)
		self.new["text"] = "New"
		self.new.grid(row=2, column=0)
		self.load = Button(self)
		self.load["text"] = "Load"
		self.load.grid(row=2, column=1)
		self.save = Button(self)
		self.save["text"] = "Save"
		self.save.grid(row=2, column=2)
		self.encode = Button(self)
		self.encode["text"] = "Encode"
		self.encode.grid(row=2, column=3)
		self.decode = Button(self)
		self.decode["text"] = "Decode"
		self.decode.grid(row=2, column=4)
		self.clear = Button(self)
		self.clear["text"] = "Clear"
		self.clear.grid(row=2, column=5)
		self.copy = Button(self)
		self.copy["text"] = "Copy"
		self.copy.grid(row=2, column=6)

		self.displayText = Label(self)
		self.displayText["text"] = "something happened"
		self.displayText.grid(row=3, column=0, columnspan=7)
b="b"
do(b)
b.mainloop()

#不能用,純粹想保留Tab

"""