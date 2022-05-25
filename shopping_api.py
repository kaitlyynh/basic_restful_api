from fastapi import FastAPI, Path, Query, HTTPException
app = FastAPI()
local_data = {}
#Case handling if no information is passed in
@app.get('/')
def case_handling():
    raise HTTPException(status_code=404, detail="Provide a valid request.")
@app.get('/display-my-shopping-cart')
def display_tasks():
    if len(local_data) == 0:
        raise HTTPException(status_code=299, detail="Cart is empty.")
    return local_data
@app.post('/add-to-cart/{item_name}')
def add_item(
    item_name: str = Path(None, description="Provide an item name"), 
    quality: str = Query('Low', description="Provide a level of quality"),
    price: float = Query(0.99, description="Enter item price here")
    ):
    if item_name is None:
        raise HTTPException(status_code=404, detail="Item not found")
    if item_name in local_data:
        return local_data[item_name]
    else:
        quality = quality.lower()
        qualities = ['low', 'medium', 'high']
        if quality in qualities:
            if quality == 'low':
                q_to_add = 'Low'
            elif quality == 'medium':
                q_to_add = 'Medium'
            elif quality == 'high':
                q_to_add = 'High'
        item_obj = {
            'item_quality': q_to_add,
            'item_price': price
        }
        local_data[item_name] = item_obj
        return local_data[item_name]
@app.get('/select-item/{item_name}')
def select_item(item_name: str = Path(None, description="Enter item in your cart")):
    if item_name in local_data:
        return local_data[item_name]
    else:
        return {"Item": "Not in cart"}

