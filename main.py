import kivy
from kivymd.app import MDApp
from farmersmapview import FarmersMapView
import sqlite3
import mysql.connector
from searchpopupmenu import SearchPopupMenu
from kivy.core.window import Window

# Window.size = (375, 750)
import certifi
import os

os.environ['SSL_CERT_FILE'] = certifi.where()


class MainApp(MDApp):
    connection = None
    cursor = None
    search_menu = None

    def on_start(self):
        # Initialize GPS

        # Connect to database
        self.connection = sqlite3.connect(":memory:")
        self.cursor = self.connection.cursor()
        self.cursor.execute("create table lang (Open_Hours,Name,Street,City,State,x,y)")
        lang_list = [
            ("Open 24 Hours", "Petron Sungai Buloh", "Lot PT 7234 Bandar Baru Sungai Buloh 47000 Sungai Buloh",
             "Sungai Buloh", " Selangor", 3.20901, 101.567),
            ("Open 24 Hours", "Caltex", "Caltex Jalan Kuala Selangor U 19 40160 Shah Alam", "Shah Alam", "Selangor",
             3.20092, 101.556),
            (
                "Open 24 Hours", "Shell", "Jalan Kuala Selangor Lot Pt4087 Bdr Baru Sg Buloh, 47000 Shah Alam",
                "Shah Alam",
                "Selangor", 3.2059, 101.562),
            ("Open 24 Hours", "Petron Rahman", "LOT 33935, Jalan BRP 1/6, Bukit Rahman Putra, 47000 Sungai Buloh",
             "Sungai Buloh", "Selangor", 3.21133, 101.562)
        ]
        self.cursor.executemany("insert into lang values (?, ?, ?, ?, ?, ?, ?)", lang_list)

        # Instantiate SearchPopupMenu
        self.search_menu = SearchPopupMenu()


MainApp().run()
