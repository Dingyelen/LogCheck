from func.transdoc import TransDoc
from conf.map_detail import PROJECT
class CreateSQL:
    def __init__(self, appname: str, event_name: str, start_date: str, end_date: str):
        self.appname = appname
        self.event_name = event_name
        self.start_date = start_date
        self.end_date = end_date

    def __repr__(self):
        return f'{self.appname} CreateSQL'
    
    def get_projectmodel(self):
        target_pro = PROJECT.get(self.appname)
        if target_pro is None:
            raise KeyError(f'plese complete {self.appname} projectmodel and PROJECT at conf/map_detail.py')
        
        return target_pro 
    
    def get_event_attr(self):
        target_pro = self.get_projectmodel()
        target_transdoc = TransDoc(appname=target_pro.appname, transdoc=target_pro.transdoc) 
        event_attr = target_transdoc.event_attr

        return event_attr 
    
    def all_event_sql(self):
        pass


    @property
    def total_sql(self):
        target_pro = self.get_projectmodel()
        target_event = target_pro.map_dict.get(self.event_name)
        if target_event is None:
            raise KeyError(f'plese complete {self.event_name} MAP at conf/map_detail.py')
        target_dbname = target_pro.tadb_name

        sql = f'''
        select a.{target_event[1]}, b."{target_event[2]}"
        from {target_dbname} a
        left join {target_event[0]} b
        on a.{target_event[1]} = b."{target_event[2]}"
        where "$part_event" = '{self.event_name}'
        and "$part_date" >= '{self.start_date}'
        and "$part_date" <= '{self.end_date}'
        group by 1, 2
        order by 1
        '''
        return sql
    
    @property
    def null_sql(self):
        target_pro = self.get_projectmodel()
        target_event = target_pro.map_dict.get(self.event_name)
        if target_event is None:
            raise KeyError(f'plese complete {self.event_name} MAP at conf/map_detail.py')
        target_dbname = target_pro.tadb_name
        
        sql = f'''
        select a.{target_event[1]}, b."{target_event[2]}"
        from {target_dbname} a
        left join {target_event[0]} b
        on a.{target_event[1]} = b."{target_event[2]}"
        where "$part_event" = '{self.event_name}'
        and "$part_date" >= '{self.start_date}'
        and "$part_date" <= '{self.end_date}'
        and b."{target_event[2]}" is null
        group by 1, 2
        order by 1
        '''
        return sql