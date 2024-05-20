import tkinter as tk
from tkinter import ttk, messagebox

class Event:
    def __init__(self, name, total_seats, pricing_tiers):
        self.name = name
        self.total_seats = total_seats
        self.pricing_tiers = pricing_tiers
        self.booked_seats = {}

    def book_seat(self, seat_number, tier):
        if seat_number in self.booked_seats:
            return f"Error: Seat {seat_number} is already booked."
        if tier not in self.pricing_tiers:
            return f"Error: Invalid pricing tier. Available tiers: {list(self.pricing_tiers.keys())}."
        if seat_number < 1 or seat_number > self.total_seats:
            return "Error: Seat number is out of range."

        self.booked_seats[seat_number] = tier
        return f"Seat {seat_number} booked under {tier} tier for {self.name}, Price: ${self.pricing_tiers[tier]}."

    def available_seats(self):
        return self.total_seats - len(self.booked_seats)

class TicketBookingSystemGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Ticket Booking System")
        self.events = {
            "Concert": Event("Concert", 100, {"Standard": 50, "Premium": 100}),
            "Bus Trip": Event("Bus Trip", 30, {"Standard": 25, "Luxury": 40})
        }
        
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.root, text="Select Event:").grid(row=0, column=0)
        self.event_name = ttk.Combobox(self.root, values=list(self.events.keys()), state='readonly')
        self.event_name.grid(row=0, column=1)
        
        ttk.Label(self.root, text="Seat Number:").grid(row=1, column=0)
        self.seat_number = ttk.Entry(self.root)
        self.seat_number.grid(row=1, column=1)
        
        ttk.Label(self.root, text="Tier:").grid(row=2, column=0)
        self.tier = ttk.Combobox(self.root, values=["Standard", "Premium", "Luxury"], state='readonly')
        self.tier.grid(row=2, column=1)
        
        book_btn = ttk.Button(self.root, text="Book Ticket", command=self.book_ticket)
        book_btn.grid(row=3, column=0, columnspan=2)
        
        self.result = ttk.Label(self.root, text="")
        self.result.grid(row=4, column=0, columnspan=2)

    def book_ticket(self):
        event_name = self.event_name.get()
        try:
            seat_number = int(self.seat_number.get())
        except ValueError:
            messagebox.showerror("Error", "Invalid seat number")
            return
        
        tier = self.tier.get()
        result = self.events[event_name].book_seat(seat_number, tier)
        if "Error" in result:
            messagebox.showerror("Error", result)
        else:
            messagebox.showinfo("Success", result)
            self.result.config(text=f"{event_name}: {self.events[event_name].available_seats()} seats available")

def main():
    root = tk.Tk()
    app = TicketBookingSystemGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
