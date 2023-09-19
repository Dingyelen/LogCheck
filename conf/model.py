class ProjectModel:
    def __init__(self, appname: str, transdoc: str, map_dict: dict, tadb_name: str, ta_url: str, ta_password: str):
        self.appname = appname
        self.transdoc = transdoc
        self.map_dict = map_dict
        self.tadb_name = tadb_name
        self.ta_url = ta_url
        self.ta_password = ta_password

    def __repr__(self):
        return f'{self.appname}_Model'