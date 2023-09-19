class ProjectModel:
    def __init__(self, appname: str, tadb_name: str, transdoc: str):
        self.appname = appname
        self.tadb_name = tadb_name
        self.transdoc = transdoc

    def __repr__(self):
        return f'{self.appname}_Model'