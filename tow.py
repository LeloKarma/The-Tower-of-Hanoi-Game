import tkinter as tk
from tkinter import messagebox
import time

class TowerOfHanoiWelcomeScreen:
    def __init__(self, master):
        self.master = master
        self.master.title("Tower of Hanoi - Welcome")
        self.master.geometry("400x300")
        self.master.configure(bg="lightblue")  # Set background color
        
        title_label = tk.Label(master, text="Welcome to Tower of Hanoi!", font=("Helvetica", 18), bg="lightblue", fg="navy")
        title_label.pack(pady=20)

        rules_text = """
        Rules:
        1. Only one disk may be moved at a time.
        2. Each move consists of taking the upper disk from one of the stacks 
           and placing it on top of another stack or on an empty rod.
        3. No disk may be placed on top of a disk that is smaller than it.
        """
        rules_label = tk.Label(master, text=rules_text, font=("Helvetica", 12), justify=tk.LEFT, bg="lightblue", fg="navy")
        rules_label.pack(pady=10)

        num_disks_label = tk.Label(master, text="Enter the number of disks (minimum 2):", font=("Helvetica", 12), bg="lightblue", fg="navy")
        num_disks_label.pack()

        self.num_disks_entry = tk.Entry(master)
        self.num_disks_entry.pack()

        start_button = tk.Button(master, text="Start", font=("Helvetica", 12), command=self.start_game, bg="navy", fg="white")
        start_button.pack(pady=20)

        

    def start_game(self):
        try:
            num_disks = int(self.num_disks_entry.get())
            if num_disks < 2:
                raise ValueError
            self.master.destroy()
            root = tk.Tk()
            game = TowerOfHanoiGame(root, num_disks)
            root.mainloop()
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number of disks (minimum 2).")

class TowerOfHanoiGame:
    def __init__(self, master, num_disks):
        self.master = master
        self.num_disks = num_disks
        self.max_moves = 2**num_disks - 1  # Maximum number of moves for the Tower of Hanoi puzzle
        self.remaining_moves = self.max_moves
        self.towers = [[i for i in range(num_disks, 0, -1)], [], []]
        self.selected_disk = None
        self.move_counter = 0
        self.start_time = time.time()

        self.canvas = tk.Canvas(master, width=600, height=400)
        self.canvas.pack()

        self.message_var = tk.StringVar()
        self.message_label = tk.Label(master, textvariable=self.message_var, fg="red")
        self.message_label.pack()

        self.num_moves_var = tk.StringVar()
        self.num_moves_label = tk.Label(master, textvariable=self.num_moves_var)
        self.num_moves_label.pack()

        self.move_timer_var = tk.StringVar()
        self.move_timer_label = tk.Label(master, textvariable=self.move_timer_var)
        self.move_timer_label.pack()

        self.reset_button = tk.Button(master, text="Reset", command=self.reset_game)
        self.reset_button.pack()

        self.draw_towers()
        self.draw_disks()
        self.update_moves_label()
        self.update_timer()

        self.canvas.bind("<Button-1>", self.handle_click)

    def draw_towers(self):
        for i in range(3):
            self.canvas.create_rectangle(i * 200 + 50, 50, i * 200 + 150, 350, fill="gray")
        # Shade the last tower as the destination tower
        self.canvas.create_rectangle(450, 50, 550, 350, fill="lightgreen")

    def draw_disks(self):
        self.canvas.delete("disk")  # Clear all existing disks
        colors = ["red", "green", "blue", "orange", "purple", "yellow", "cyan"]  # Define colors for disks
        for i in range(3):
            for j, disk in enumerate(self.towers[i]):
                width = 20 + disk * 20
                x0 = i * 200 + (100 - width // 2)
                y0 = 350 - (j * 20)
                x1 = x0 + width
                y1 = y0 - 20
                color_index = min(disk - 1, len(colors) - 1)  # Ensure color index is within range
                disk_color = colors[color_index]
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=disk_color, tags="disk")

    def handle_click(self, event):
        if self.remaining_moves > 0:
            x, y = event.x, event.y
            tower = x // 200
            if self.selected_disk is None and self.towers[tower]:
                self.selected_disk = self.towers[tower].pop()
                self.draw_disks()
                self.message_var.set("Disk selected. Click on destination tower.")
            elif self.selected_disk is not None:
                destination = x // 200
                if not self.towers[destination] or self.selected_disk < self.towers[destination][-1]:
                    self.towers[destination].append(self.selected_disk)
                    self.selected_disk = None
                    self.draw_disks()
                    self.remaining_moves -= 1
                    self.move_counter += 1
                    self.update_moves_label()
                    if self.remaining_moves == 0 and not self.towers[0] and not self.towers[1]:
                        self.message_var.set("You win!")
                        elapsed_time = time.time() - self.start_time
                        self.move_timer_var.set(f"Time taken: {elapsed_time:.2f} seconds")
                    elif self.remaining_moves == 0:
                        self.message_var.set("You've used all your moves. Click Reset to try again.")
                else:
                    self.message_var.set("Invalid move: Cannot place a larger disk on top of a smaller one.")
        else:
            self.message_var.set("You've used all your moves. Click Reset to try again.")

    def reset_game(self):
        self.remaining_moves = self.max_moves
        self.move_counter = 0
        self.start_time = time.time()
        self.towers = [[i for i in range(self.num_disks, 0, -1)], [], []]
        self.selected_disk = None
        self.draw_disks()
        self.message_var.set("")
        self.update_moves_label()
        self.update_timer()

    def update_moves_label(self):
        self.num_moves_var.set(f"Moves: {self.move_counter}/{self.max_moves}")

    def update_timer(self):
        if self.remaining_moves > 0:
            elapsed_time = time.time() - self.start_time
            self.move_timer_var.set(f"Time elapsed: {elapsed_time:.2f} seconds")
            self.master.after(1000, self.update_timer)
        else:
            self.move_timer_var.set("")

def main():
    root = tk.Tk()
    welcome_screen = TowerOfHanoiWelcomeScreen(root)
    root.mainloop()

if __name__ == "__main__":
    main()
