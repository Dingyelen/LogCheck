from func.transdoc import TransDoc
from func.createsql import CreateSQL
from conf.map_detail import PROJECT
from func.ta import TaDB
import sys
import re

def parse_shellparams(shellinputs):
    params = shellinputs[1:]
    kwargs = dict(param[2:].split('=') for param in params if re.match('--[a-zA-Z]+', param) and param.count('=') == 1)
    others = [param for param in params if param[2:].split('=')[0] not in kwargs]
    if others:
        fit_param_ = [f'--{param}=value' for param in others]
        fit_param = '  '.join(fit_param_)
        raise SyntaxError(f'please check your shellparams 【{others}】, example: 【python mytest.py {fit_param}】')
    return kwargs

if __name__ == '__main__':
    kwargs = parse_shellparams(sys.argv)
    appname = kwargs.get('appname')
    if appname is None:
        raise TypeError(f'appname is necessary argument')
    event_name = kwargs.get('event_name')
    start_date = kwargs.get('start_date')
    end_date = kwargs.get('end_date')
    res_type = kwargs.get('res_type') if 'res_type' in kwargs else 'null'

    target = CreateSQL(appname=appname, event_name=event_name, start_date=start_date, end_date=end_date)
    target_pro, target_event = target.get_projectmodel()
    if res_type == 'total':
        sql = target.total_sql
    else:
        sql = target.null_sql
    tadb = TaDB(target_pro.ta_url, target_pro.ta_url)
    rows, action, results = tadb.execute(sql)

    print(rows, action, results)
