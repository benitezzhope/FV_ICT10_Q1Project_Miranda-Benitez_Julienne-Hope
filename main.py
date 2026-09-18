from pyscript import document

def skugen(e):
    # Get the values
    category = document.getElementById("category").value
    product_name = document.getElementById("product").value
    quantity = document.getElementById("quantity").value

    # Make sure all the values have been filled up
    if not category or not product_name or not quantity:
        document.getElementById("skugen").innerHTML = "<p style='color: #ff71a3; text-align: center; font-weight: bold;'>Please fill out all fields properly.</p>"
        return

    # Getting the elements for the SKU Code by getting the first three letters for each

    categ0ry = category[0:3].upper() # Using uppercase

    product = product_name[0:3].upper() # Using uppercase

    quvntity = quantity # Getting the numerical value

    generated_sku = f"{categ0ry}-{product}-{quvntity}" # Getting the generated sku

    # display
    document.getElementById("skugen").innerHTML = f"<h2 style='color: #ff71a3; text-align: center; margin-top: 15px;'>Your SKU code is {generated_sku}</h2>"
