from db.config import DB


class News_Daryo(DB):
    def __init__(self , *fields):
        self.fields = fields

class News_Qalampir(DB):
    def __init__(self , *fields):
        self.fields = fields