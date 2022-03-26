"""
CURRENCY EXCHANGE APP
- Currency exchange app is able to convert an arbitrary currencies, which are supported by ISO 4217. 
- This app was made by me, Tomas Hajek as a small creative project.
- Its main aim was to exercise with Python, API calls and TKinter GUI.
- You can find all my mini projects in github portfolio: https://github.com/TomHajek.
"""

import requests
import tkinter as tk
from tkinter import *
import tkinter.messagebox
import datetime

# =========================================================================================== Functional part of APP
"""This part of the code is responsible for API call, retrieving informations and functionalities of all widgets."""

## ISO 4217
supported_currencies = ['USD', 'AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG', 'AZN', 
                        'BAM', 'BBD', 'BDT', 'BGN', 'BHD','BIF', 'BMD', 'BND', 'BOB', 'BRL', 'BSD', 
                        'BTN', 'BWP', 'BYN', 'BZD', 'CAD', 'CDF', 'CHF', 'CLP', 'CNY', 'COP','CRC', 
                        'CUC', 'CUP', 'CVE', 'CZK', 'DJF', 'DKK', 'DOP', 'DZD', 'EGP', 'ERN', 'ETB', 
                        'EUR', 'FJD', 'FKP', 'FOK','GBP', 'GEL', 'GGP', 'GHS', 'GIP', 'GMD', 'GNF', 
                        'GTQ', 'GYD', 'HKD', 'HNL', 'HRK', 'HTG', 'HUF', 'IDR', 'ILS','IMP', 'INR', 
                        'IQD', 'IRR', 'ISK', 'JMD', 'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KID', 'KMF', 
                        'KRW', 'KWD', 'KYD','KZT', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL', 'LYD', 'MAD', 
                        'MDL', 'MGA', 'MKD', 'MMK', 'MNT', 'MOP', 'MRU', 'MUR','MVR', 'MWK', 'MXN', 
                        'MYR', 'MZN', 'NAD', 'NGN', 'NIO', 'NOK', 'NPR', 'NZD', 'OMR', 'PAB', 'PEN', 
                        'PGK', 'PHP','PKR', 'PLN', 'PYG', 'QAR', 'RON', 'RSD', 'RUB', 'RWF', 'SAR', 
                        'SBD', 'SCR', 'SDG', 'SEK', 'SGD', 'SHP', 'SLL','SOS', 'SRD', 'SSP', 'STN', 
                        'SYP', 'SZL', 'THB', 'TJS', 'TMT', 'TND', 'TOP', 'TRY', 'TTD', 'TVD', 'TWD', 
                        'TZS','UAH', 'UGX', 'UYU', 'UZS', 'VES', 'VND', 'VUV', 'WST', 'XAF', 'XCD', 
                        'XDR', 'XOF', 'XPF', 'YER', 'ZAR', 'ZMW']

## Getting data from API
def get_exchange(base, target, amount):
    if base not in supported_currencies:
        #raise ValueError("Incorrect input. Please insert relevant currency code according to ISO 4217.")
        clear()
        
    if target not in supported_currencies:
        #raise ValueError("Incorrect input. Please insert relevant currency code according to ISO 4217.")
        clear()      
        
    api_key = "7dee9b50e76f9344fa89acbc"
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{base}/{target}/{amount}"    
    
    response = requests.get(url)
    exchange = response.json()
    #print(exchange)
    
    #print(format_result(exchange))
    #print(format_status(exchange))
    
    result_label['text'] = format_result(exchange)
    status_label['text'] = format_status(exchange)

## Formating result   
def format_result(exchange):
    try:    
        result = exchange["conversion_result"]
        result_str = f"{result}"
    except:
        result_str = ""
    return result_str

## Formating status(rate and update dates)  
def format_status(exchange):
    try:   
        rate = exchange["conversion_rate"]
        last_update = exchange["time_last_update_utc"]
        next_update = exchange["time_next_update_utc"]
        status_str = f"rate: {rate}, last update: {last_update}, next update: {next_update}"
    except:
        status_str = "Incorrect input. Please insert relevant currency codes according to ISO 4217."
    return status_str

## Drop down menu - clear all inputs/outputs
def clear():
    entry_base.delete(0, "end")
    entry_target.delete(0, "end")
    entry_amount.delete(0, "end")
    result_label.config(text = "")
    status_label.config(text = "")
    
## Drop down menu - save exchange into exchange.txt file
def save():
    with open("exchange.txt", "a") as f:
        f.write(f"\nLOG:{datetime.datetime.now()},"
                f"\n - To exchange: {entry_amount.get()} {entry_base.get()},"
                f"\n - To get:      {result_label['text']} {entry_target.get()},"
                f"\n - {status_label['text']}\n") 

## Drop down menu - brief comment about application
def about():
    tk.messagebox.showinfo("about", 
                           "This app was made by me, Tomas Hajek as a small creative project. " 
                           "Its main aim was to exercise with Python, API calls and GUI.")


# =========================================================================================== TKinter GUI
"""This part of the code is responsible for graphical user interface."""

## WINDOW
root = tk.Tk()
root.title("Currency Exchange App")

### window - properties
canvas = tk.Canvas(root, height = 300, width = 610)
canvas.pack()

### background
background_image = tk.PhotoImage(file = "coins.png")
background_label = tk.Label(root, image = background_image)
background_label.place(relwidth = 1, relheight = 1)

## TOP FRAME - properties
top_frame = tk.Frame(root, bg = "#4f423b", bd = 6, relief = "flat")
top_frame.place(relx = 0.4, rely = 0.15, relwidth = 0.5, relheight = 0.25, anchor = "n")

### BASE CURRENCY - label
input_label = tk.Label(top_frame, text = "ENTER VALUE AND CURRENCY TO EXCHANGE", font = ("Arial", 10), fg = "white", 
                       bg = "#4f423b", anchor = "n", justify = "center")
input_label.place(relwidth = 1, relheight = 0.5)

### BASE AMOUNT - input window
entry_amount = tk.Entry(top_frame, font = ("Arial", 12), fg = "#4f423b", justify = "right")
entry_amount.insert(0, "1000")
entry_amount.place(relx = 0.58, rely = 0.5, relwidth = 0.4, relheight = 0.4, anchor = "n") 

### BASE CURRENCY - input window
entry_base = tk.Entry(top_frame, font = ("Arial", 12), fg = "#4f423b", justify = "left")
entry_base.insert(0, "CZK")
entry_base.place(relx = 0.9, rely = 0.5, relwidth = 0.15, relheight = 0.4, anchor = "n") 

## BOT FRAME - properties
bot_frame = tk.Frame(root, bg = "#4f423b", bd = 6, relief = "flat")
bot_frame.place(relx = 0.4, rely = 0.55, relwidth = 0.5, relheight = 0.25, anchor = "n")

### TARGET CURRENCY - label
output_label = tk.Label(bot_frame, text = "ENTER THE DESIRED CURRENCY", font = ("Arial", 12), fg = "white", 
                        bg = "#4f423b", anchor = "n", justify = "center")
output_label.place(relwidth = 1, relheight = 0.5)

### TARGET VALUE - result window
result_label = tk.Label(bot_frame, text = "", font = ("Arial", 12), fg = "#4f423b", justify = "right", anchor = "n", 
                       bg = "#c0dfac",relief = "flat")
result_label.place(relx = 0.58, rely = 0.5, relwidth = 0.4, relheight = 0.4, anchor = "n")

### TARGET CURRENCY - input window
entry_target = tk.Entry(bot_frame, font = ("Arial", 12), fg = "#4f423b", justify = "left")
entry_target.insert(0, "EUR")
entry_target.place(relx = 0.9, rely = 0.5, relwidth = 0.15, relheight = 0.4, anchor = "n")  

## MID FRAME
mid_frame = tk.Frame(root, bg = "#4f423b", bd = 6, relief = "flat")
mid_frame.place(relx = 0.83, rely = 0.315, relwidth = 0.2, relheight = 0.3, anchor = "n")

### CONVERT BUTTON - clicking on the button executes the API call based on user inputs
background_button = tk.PhotoImage(file = "arrow.png")
button_image = background_button.subsample(17, 17)

button = tk.Button(mid_frame, text = "CONVERT!", fg = "#4f423b", bg = "#c0dfac", image = button_image, compound = "left", 
                   command = lambda: get_exchange(entry_base.get().upper(), entry_target.get().upper(), entry_amount.get().upper()))
button.place(relx = 0.03, rely = 0.03, relheight = 0.94, relwidth = 0.94)

## STATUS BAR
status_label = tk.Label(root, text = "rate:      , last update:     ", font = ("Arial", 9), 
                        fg = "#4f423b", bg = "white", anchor = "s", justify = "left", relief = "flat")
status_label.place(rely = 0.93, relwidth = 1, relheight = 0.07)

## DROP DOWN MENU
menubar = Menu(root)                                           # main menu bar
root.config(menu = menubar)

### File
filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label = "New", command = clear)            ## New
filemenu.add_command(label = "save", command = save)            ## save
filemenu.add_separator()                                        ## _____
filemenu.add_command(label = "Exit", command = root.quit)       ## Exit

menubar.add_cascade(label = "File", menu = filemenu)            # adding File(tab) to main menu bar

### about
helpmenu = Menu(menubar, tearoff = 0)
helpmenu.add_command(label = "about", command = about)          # about
menubar.add_cascade(label = "about", menu = helpmenu)           # adding about(tab) to main menu bar



root.mainloop()