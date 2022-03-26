import requests
import tkinter as tk

# ================================================================================= request API
# http://api.openweathermap.org/data/2.5/weather?q={city},cz&APPID={api_key}

## Getting data from API
def get_weather(city):
    url = "https://api.openweathermap.org/data/2.5/weather"
    api_key = "135b2dcf7cd502de0f1076c40c8b98ca"
    params = {"q": city, "APPID": api_key, "units": "metric"}
    
    response = requests.get(url, params = params)
    weather = response.json()
    
    label['text'] = format_response(weather)

## Formating recieved data
def format_response(weather):
    try:
        name = weather["name"]
        temp = weather["main"]["temp"]
        description = weather["weather"][0]['description']
        
        format_str = f"City: {name} \nTemperature: {temp} °C \nConditions: {description}"
        
    except:
        format_str = "An error occurred while retrieving the information."
        
    return format_str

# ================================================================================ tkinter GUI
root = tk.Tk()

## Setting window dimensions
HEIGHT = 400
WIDTH = 500

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

## Setting app background
background_image = tk.PhotoImage(file = "landscape.png")
background_label = tk.Label(root, image = background_image)
background_label.place(relwidth = 1, relheight = 1)

## Setting app frames
upper_frame = tk.Frame(root, bg = "#20B2AA", bd = 5)
upper_frame.place(relx = 0.5, rely = 0.1, relwidth = 0.8, relheight = 0.1, anchor = "n")

lower_frame = tk.Frame(root, bg = "#20B2AA", bd = 6)
lower_frame.place(relx = 0.5, rely = 0.3, relwidth = 0.8, relheight = 0.6, anchor = "n")

## Setting app BUTTON
### clicking on the button executes the API call based on user input 
button = tk.Button(upper_frame, text = "Get Weather", font = 40, command = lambda: get_weather(entry.get()))
button.place(relx = 0.7, relheight = 1, relwidth = 0.3)

## Setting app INPUT window
entry = tk.Entry(upper_frame, font = 40, fg = "black")
entry.insert(0, "Type here your city name...")
entry.place(relwidth = 0.65, relheight = 1)

## Setting app OUTPUT window
label = tk.Label(lower_frame, font =("Arial", 18), justify = "left", anchor = "n", relief = "groove")
label.place(relwidth = 1, relheight = 1)


root.mainloop()