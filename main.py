from pyscript import document, display

def skugen(e):
    # Get the values
    cat_elem = document.getElementById("category")
    prod_elem = document.getElementById("product")
    qty_elem = document.getElementById("quantity")

    if not cat_elem or not prod_elem or not qty_elem:
        return

    category = cat_elem.value
    product_name = prod_elem.value
    quantity = qty_elem.value

    # Make sure all the values have been filled up
    if not category or not product_name or not quantity:
        document.getElementById("skugen").innerHTML = "<p style='color: #ff71a3; text-align: center; font-weight: bold;'>Please fill out all fields properly.</p>"
        return

    categ0ry = category[0:3].upper()
    product = product_name[0:3].upper()
    quvntity = quantity

    generated_sku = f"{categ0ry}-{product}-{quvntity}"

    document.getElementById("skugen").innerHTML = f"<h2 style='color: #ff71a3; text-align: center; margin-top: 15px;'>Your SKU code is {generated_sku}</h2>"


def Total(e):
    result_elem = document.getElementById("result")
    if not result_elem:
        return

    result_elem.innerHTML = ""
    
    items = [
        document.getElementById("slime1"),
        document.getElementById("slime2"),
        document.getElementById("slime3"),
        document.getElementById("squishy1"),
        document.getElementById("squishy2"),
        document.getElementById("squishy3")
    ]

    subtotal = 0.0
    for item in items:
        if item and item.checked:
            subtotal += float(item.value)

    tax = subtotal * 0.12
    total = subtotal + tax

    display(f"Subtotal: ₱{subtotal:.2f}", target="result")
    display(f"Tax: ₱{tax:.2f}", target="result")
    display(f"Total: ₱{total:.2f}", target="result")


def Reset(e):
    items = ["slime1", "slime2", "slime3", "squishy1", "squishy2", "squishy3"]
    for item_id in items:
        elem = document.getElementById(item_id)
        if elem:
            elem.checked = False
            
    result_elem = document.getElementById("result")
    if result_elem:
        result_elem.innerHTML = "<p><b>Subtotal:</b> ₱0.00</p><p><b>Tax:</b> ₱0.00</p><p><b>Total:</b> ₱0.00</p>"
