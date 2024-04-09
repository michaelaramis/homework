import flet as ft
import random

def main(page: ft.Page):
    def button_clicked(e):
        roll = random.randint(1, 6)
        img.height=190
        img.width=190
        number.value=roll
        if roll == 1: 
            img.src = "https://static.thenounproject.com/png/1194685-200.png"
        elif roll == 2: 
            img.src = "https://upload.wikimedia.org/wikipedia/commons/5/5f/Dice-2-b.svg"
        elif roll == 3: 
            img.src = "https://www.svgrepo.com/show/320121/inverted-dice-3.svg"
        elif roll == 4: 
            img.src = "https://www.svgrepo.com/show/320121/inverted-dice-3.svg"
        elif roll == 5: 
            img.src = "https://cdn2.iconfinder.com/data/icons/dice-roll/100/dice_5-512.png"
        elif roll == 6: 
            img.src = "https://www.svgrepo.com/show/344728/dice-6.svg"
        page.update()
        
    page.title = "Dice Dynasty"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    img = ft.Image(src="firstface.png", height=190, width=190)
    number = ft.Text(" ")

    page.add(
        img,number, 
        ft.FilledTonalButton(text="Press this button to roll",on_click=button_clicked)), 
ft.app(target=main)