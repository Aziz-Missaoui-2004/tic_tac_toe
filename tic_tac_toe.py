import sys
import os


def print_empty_line():
    print("   ---","+","-","+","---",)
    
def print_header():
    print("     a   b   c")
    
def print_line(grille, i):
    print(i,'  ',
              grille['a'][i],
              '|',
              grille['b'][i],
              '|',
              grille['c'][i],
              )

class Board:
    
    def __init__(self):
        self.grille = {
            'a' :  [' ', ' ', ' '],
            'b' :  [' ', ' ', ' '],
            'c' :  [' ', ' ', ' '],
            }
        self.columns = ['a', 'b', 'c']
        
        self.boxes = ["a0", "b0", "c0",
                      "a1", "b1", "c1",
                      "a2", "b2", "c2"]
        self.empty_boxes = ["a0", "b0", "c0",
                      "a1", "b1", "c1",
                      "a2", "b2", "c2"]
        self.filled_boxes = []

    
    def print_board(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        sys.stdout.flush()
        print_header()
        print_line(self.grille, 0)
        print_empty_line()
        print_line(self.grille, 1)
        print_empty_line()
        print_line(self.grille, 2)
    
    def fill_box(self, box, flag):
        if box in self.boxes and flag in ['x', 'o']:
            colonne, ligne = box[0], int(box[1])
            self.grille[colonne][ligne] = flag
            self.empty_boxes.remove(box)
            self.filled_boxes.append(box)
        else:
            pass 
    
    def empty_grid(self):
        self.grille = {
            'a' :  [' ', ' ', ' '],
            'b' :  [' ', ' ', ' '],
            'c' :  [' ', ' ', ' '],
            }
 
    def still_can_play(self):
        return len(self.empty_boxes) > 0
    
                   
    
    def check_win(self):
        boxes_to_check = [
            self.grille['a'],
            self.grille['b'],
            self.grille['c'],
            [self.grille[col][0] for col in self.columns],
            [self.grille[col][1] for col in self.columns],
            [self.grille[col][2] for col in self.columns],
            [self.grille['a'][0], self.grille['b'][1], self.grille['c'][2]],
            [self.grille['a'][2], self.grille['b'][1], self.grille['c'][0]],
            ]
        check = False
        i = 0
        while i < len(boxes_to_check) and not check:
            check = (len(set(boxes_to_check[i])) == 1) and (boxes_to_check[i][0] in ['x', 'o'])
            i+=1
        return check
                
def get_box(board):
    box = input("Enter box: ")
    while box not in board.empty_boxes:
        box = input("Enter a valid box: ")
    return box


def run_game():
    board = Board()
    flags = ['x', 'o']
    player_names = [input("Enter player 1 name: "),
                    input("Enter player 2 name: ")]
    board.print_board()
    player = 1
    while board.still_can_play() and not board.check_win():
        player = 1 - player
        print("\n>>>", player_names[player])
        box = get_box(board)
        board.fill_box(box, flags[player])
        board.print_board()
        
        
    if board.check_win():
        print("Congrats ", player_names[0])
    else:
        print("It's a tie!")
        
    pass

run_game()
 








