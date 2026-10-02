import random
import string
import tkinter as tk

is_running= False
guess = ""
att = 0
def secure():
    global guess,att, is_running
    
    a = entry.get() 
    chars = string.ascii_letters + string.digits + string.punctuation
    
    is_running = True
    att = 0
    guess = ""
    


    output_label.config(text="Trying to guess...")

    while guess != a and is_running:
        guess = "".join(random.choice(chars) for i in range(len(a)))
        att += 1
        output_label.config(text=f"Attempt {att}: {guess}")
        window.update() # refresh screen
        # if att > 5000: # safety break so it doesn't hang
        #     break
        
    if not is_running:
            output_label.config(text=f"Stopped! Last guess was '{guess}' after {att} attempts")
    else:
            output_label.config(text=f"Found! '{guess}' in {att} attempts")
        
    
def stop():
    global is_running
    is_running=False
    
# --- GUI STRUCTURE ---

window = tk.Tk()
window.title("Password Tracker By SMI")
window.geometry("500x300") # width x height

title = tk.Label(window, text="-------------Password Tracker By SMI----------", font=("Arial", 12, "bold"))
title.pack(pady=10) # pady = space from top

tk.Label(window, text="Enter Your Password:").pack()
entry = tk.Entry(window, width=40)
entry.pack(pady=5)

btn = tk.Button(window, text="Start Guessing", command=secure, bg="black", fg="white", width=20)
btn.pack(pady=10)
reset= tk.Button(window, text="Stop",command=stop ,bg="red", fg="white", width=15)
reset.pack(pady=10)

output_label = tk.Label(window, text="", font=("Courier", 10))
output_label.pack(pady=10)

window.mainloop()