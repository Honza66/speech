from gtts import gTTS
import os
from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Konvertot textu na řeč')
root.geometry('300x300')
root.resizable(False, False)

def translate_text(entry, language, audio_file):
    try:
        text_to_audio = entry
        output = gTTS(text=text_to_audio, lang= language,  slow=False)
        output.save(f'{audio_file}.mp3')
        os.system(f'{audio_file}.mp3')
    except Exception as e:
        print(f'Nastala chyba {e}')

main_label = Label(text='Konvertor')
main_label.grid(row=0, column=1)

language_label = Label(text='Vyberte jazyk:')
language_label.grid(row=1, column=0)

language_dropdown = ttk.Combobox(
    state='readonly',
    values=('cs','en', 'de'),
    width=27
)
language_dropdown.grid(row=1, column=1)

text_label = Label(text='Vložte text:')
text_label.grid(row=2,column=0)
text_entry = Entry(width=30)
text_entry.grid(row=2, column=1)

audio_label = Label(text='Název souboru')
audio_label.grid(row=3, column=0)
audio_entry = Entry(width=30)
audio_entry.grid(row=3, column=1)

translate_button = Button(text='Přelož', command=lambda: translate_text(text_entry.get(), language_dropdown.get(), audio_entry.get()))
translate_button.grid(row=4, column=1)



root.mainloop()

