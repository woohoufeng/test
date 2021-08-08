from dialog import ListMDDialog

class LocationPopupMenu(ListMDDialog):
    def __init__(self, market_data):
        super().__init__()
        #Set all of the fields of market data
        headers = "Open_Hours,Name,Street,City,State"
        headers = headers.split(',')
        for i in range(len(headers)):
            attribute_name = headers[i]
            attribute_value = market_data[i]
            setattr(self, attribute_name, attribute_value)
