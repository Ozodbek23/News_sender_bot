class NewsDaryoDto:
    def __init__(self,
                 id : int = None,
                 title : str = None,
                 created_at : str = None,
                 img_name : str = None):
        self.id = id
        self.title = title
        self.created_at = created_at
        self.img_name = img_name

class NewsQalampirDto:
    def __init__(self,
                 id : int = None,
                 title : str = None,
                 created_at : str = None,
                 img_name : str = None):
        self.id = id
        self.title = title
        self.created_at = created_at
        self.img_name = img_name