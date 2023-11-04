import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.current_player = 'X'
        self.buttons = [[None, None, None], [None, None, None], [None, None, None]]

        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(root, text='', width=10, height=3, command=lambda i=i, j=j: self.make_move(i, j))
                self.buttons[i][j].grid(row=i, column=j)

    def make_move(self, row, col):
        if not self.buttons[row][col]['text']:
            self.buttons[row][col]['text'] = self.current_player
            self.buttons[row][col]['state'] = 'disabled'
            if self.check_win(row, col):
                messagebox.showinfo("Tic-Tac-Toe", f"Player {self.current_player} wins!")
                self.reset_board()
            elif self.check_tie():
                messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
                self.reset_board()
            self.current_player = 'X' if self.current_player == 'O' else 'O'

    def check_win(self, row, col):
        return self.check_row(row) or self.check_col(col) or self.check_diag(row, col)

    def check_row(self, row):
        return all(self.buttons[row][col]['text'] == self.current_player for col in range(3))

    def check_col(self, col):
        return all(self.buttons[row][col]['text'] == self.current_player for row in range(3))

    def check_diag(self, row, col):
        if row == col:
            return all(self.buttons[i][i]['text'] == self.current_player for i in range(3))
        if row + col == 2:
            return all(self.buttons[i][2 - i]['text'] == self.current_player for i in range(3))
        return False

    def check_tie(self):
        return all(self.buttons[i][j]['text'] for i in range(3) for j in range(3))

    def reset_board(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]['text'] = ''
                self.buttons[i][j]['state'] = 'active'

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
