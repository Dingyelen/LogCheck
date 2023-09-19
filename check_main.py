from func.transdoc import TransDoc
from conf.map_detail import *
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

print(DOW2.appname)
