
import tkinter as tk
from PIL import ImageTk, Image
from model import sentiment_classification

def prediction():
  input_emotion = text_entry.get()
  sentiment = sentiment_classification(input_emotion)
  display_label["text"] = sentiment
  if sentiment == "positive":
    display_label["text"] = "positive"
    img_result_label["image"] = happy_img
  elif sentiment == "negative":
    display_label["text"] = "negative"
    img_result_label["image"] = sad_img
  else:
    img_result_label["image"] = question_img

    
screen = tk.Tk()

screen.title("Make me happy or make me sad")

screen.resizable(width = False, height = False)

sad_img = ImageTk.PhotoImage(Image.open('img/sad.jpg'))

happy_img = ImageTk.PhotoImage(Image.open('img/happy.jpg'))

question_img = ImageTk.PhotoImage(Image.open('img/question.jpg'))

frame_result = tk.Frame(master = screen)
frame_entry = tk.Frame(master = screen)


display_label = tk.Label(master = frame_result, text = "This should be displayed", font = ("Arial", 20), width = 20)
display_label.grid(row = 1, column = 0)

img_result_label = tk.Label(master = frame_result, image = question_img)
img_result_label.grid(row = 2, column = 0)

entry_label = tk.Label(master = frame_entry, text= "Enter text below: ", font = ("Arial",10), width = 15)
entry_label.grid(row = 0, column = 0)

text_entry = tk.Entry(master = frame_entry, width = 15)
text_entry.grid(row =1, column = 0)

submit_button = tk.Button(master = frame_entry, text = "Submit", font = ("Arial", 15), command = prediction)
submit_button.grid(row =3, column = 0)

frame_result.grid(row = 0, column = 0)
frame_entry.grid(row =1, column =0)


screen.geometry('400x450')
screen.mainloop()