from conf.model import ProjectModel

# map_dict
DOW2_MAP = {'PayFunel': ['ta_dim.dim_38_0_130723', 'icon_id', 'icon_id@icon_id'], 
            'GoldChage': ['ta_dim.dim_38_0_130727', 'gold_reason', 'gold_reason@gold_reason'], 
            'ItemChange': ['ta_dim.dim_38_0_130879', 'item_id', 'item_id@item_id'], 
            'Summon': ['ta_dim.dim_38_0_131028', 'summon_id', 'summon_id@summon_id'], 
            'Payment': ['ta_dim.dim_38_0_131279', 'payment_itemid', 'payment_itemid@goods_id']
            }


# tadb_name
DOW2_DB = 'ta.v_event_38'

# ta_url
DOW2_URL = 'http://106.52.105.118:8992/querySql'

# ta_password
DOW2_PASSWORD = '260aXXAfe1LdM3fGKqFFstRlF7p69YhSYRxyQ3MWCSBzBdonFS9TXT4W9KDo5Bg1'

# MODEL
DOW2 = ProjectModel(appname='dow2', transdoc='DOW2', map_dict=DOW2_MAP, tadb_name=DOW2_DB, ta_url=DOW2_URL, ta_password=DOW2_PASSWORD)

