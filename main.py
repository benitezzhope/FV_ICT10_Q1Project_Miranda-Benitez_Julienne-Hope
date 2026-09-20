# Project
from pyscript import display, document

def Total(e):
    document.getElementById("result").innerHTML = ""
    item1 = document.getElementById("slime1")
    item2 = document.getElementById("slime2")
    item3 = document.getElementById("slime3")
    item4 = document.getElementById("squishy1")
    item5 = document.getElementById("squishy2")
    item6 = document.getElementById("squishy3")

    # Calculate the subtotal using the selected values
    subtotal = float(item1.value) * item1.checked

    # Add the current value of the items to the subtotal
    # .checked adds the selected item only
    subtotal += float(item2.value) * item2.checked
    subtotal += float(item3.value) * item3.checked
    subtotal += float(item4.value) * item4.checked
    subtotal += float(item5.value) * item5.checked
    subtotal += float(item6.value) * item6.checked

    # Calculate tax and total
    tax = subtotal * 0.12
    total = subtotal + tax

    # Display receipt
    display(f"Subtotal: ₱{subtotal:.2f}", target="result")
    display(f"Tax: ₱{tax:.2f}", target="result")
    display(f"Total: ₱{total:.2f}", target="result")

def Reset(e): #hides the receipt details and unchecks the boxes
    document.getElementById("slime1").checked = False 
    document.getElementById("slime2").checked = False
    document.getElementById("slime3").checked = False
    document.getElementById("squishy1").checked = False
    document.getElementById("squishy2").checked = False
    document.getElementById("squishy3").checked = False
    
    document.getElementById("result").innerHTML = ""