from kivy_garden.mapview import MapView
from kivy.clock import Clock
from kivy.app import App
from marketmarker import MarketMarker

class FarmersMapView(MapView):
    getting_markets_timer = None
    market_names = []

    def start_getting_markets_in_fov(self):
        # After one second, get the markets in the field of view
        try:
            self.getting_markets_timer.cancel()
        except:
            pass

        self.getting_markets_timer = Clock.schedule_once(self.get_markets_in_fov, 1)

    def get_markets_in_fov(self, *args):
        # Get reference to main app and the database cursor
        min_lat, min_lon, max_lat, max_lon = self.get_bbox()
        app = App.get_running_app()
        sql_statement = "SELECT * FROM lang WHERE x > %s AND x < %s AND y > %s AND y < %s" % (min_lat,max_lat, min_lon, max_lon)
        app.cursor.execute(sql_statement)
        markets = app.cursor.fetchall()
        print(markets)
        for market in markets:
            name = market[1]
            if name in self.market_names:
                continue
            else:
                self.add_market(market)

    def add_market(self, market):
        # Create the MarketMarker
        lat, lon = market[5], market[6]
        marker = MarketMarker(lat=lat, lon=lon, source='marker.png')
        marker.market_data = market
        # Add the MarketMarker to the map
        self.add_widget(marker)
        # Keep track of the marker's name
        name = market[1]
        self.market_names.append(name)
