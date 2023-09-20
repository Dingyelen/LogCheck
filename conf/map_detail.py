from conf.model import ProjectModel

# map_dict
DOW2_MAP = {'PayFunel': ['ta_dim.dim_38_0_130723', 'icon_id', 'icon_id@icon_id'], 
            'GoldChage': ['ta_dim.dim_38_0_130727', 'gold_reason', 'gold_reason@gold_reason'], 
            'ItemChange': ['ta_dim.dim_38_0_130879', 'item_id', 'item_id@item_id'], 
            'Summon': ['ta_dim.dim_38_0_131028', 'summon_id', 'summon_id@summon_id'], 
            'Payment': ['ta_dim.dim_38_0_131279', 'payment_itemid', 'payment_itemid@goods_id']
            }

DOW_MAP = {'AddGold': ['ta_dim.dim_9_0_95031', 'itemid', 'itemid@id'], 
           'CostGold': ['ta_dim.dim_9_0_95031', 'itemid', 'itemid@id'],
           'AddItem': ['ta_dim.dim_9_0_124717', 'itemid',  'item_id_detail.item_id@id'], 
           'CostItem': ['ta_dim.dim_9_0_124717', 'itemid',  'item_id_detail.item_id@id'], 
           'RecruitCard': ['ta_dim.dim_9_0_100730', 'recruitid', 'recruitid@id'], 
           'Payment': ['ta_dim.dim_9_0_95498', 'payment_itemid', 'payment_itemid@goodsid']
           }

SEAEMPIRE_MAP = {'PayFunel': ['ta_dim.dim_38_0_130723', 'icon_id', 'icon_id@icon_id'], 
                 'CurrencyChange': ['ta_dim.dim_36_0_127730', 'currency_reason', 'item_reason@reason'], 
                 'ItemChange': ['ta_dim.dim_36_0_127718', 'item_id', 'item_id@item_id'], 
                 'Summon': ['ta_dim.dim_36_0_128199', 'summon_id', 'summon_id@summon_id'], 
                 'Payment': ['ta_dim.dim_36_0_128493', 'payment_itemid', 'payment_itemid@goods_id']
            }

# tadb_name
DOW2_DB = 'ta.v_event_38'
DOW_DB = 'ta.v_event_9'
SEAEMPIRE_DB = 'ta.v_event_36'

# ta_url
URL = 'http://106.52.105.118:8992/querySql'
DOW2_URL = URL
DOW_URL = URL
SEAEMPIRE_URL = URL



# ta_password
DOW2_PASSWORD = '260aXXAfe1LdM3fGKqFFstRlF7p69YhSYRxyQ3MWCSBzBdonFS9TXT4W9KDo5Bg1'
DOW_PASSWORD = 'QCHTSdWhHlg286d41qKq7TP54TvFsfVLdGx4BXNvdSl4N8hymmMnmx1nwt0A0Tnm'
SEAEMPIRE_PASSWORD = '07F9GuaBxkWQM26k1wsrITat3dwC551RxfxO12syQAL43Ll0NzvJVmBn0yFwMBOj'

# MODEL
DOW2 = ProjectModel(appname='dow2', transdoc='DOW2', map_dict=DOW2_MAP, tadb_name=DOW2_DB, ta_url=DOW2_URL, ta_password=DOW2_PASSWORD)
DOW = ProjectModel(appname='dow', transdoc='DOW', map_dict=DOW_MAP, tadb_name=DOW_DB, ta_url=DOW_URL, ta_password=DOW_PASSWORD)
SEAEMPIRE = ProjectModel(appname='seaempire', transdoc='SEAEMPIRE', map_dict=SEAEMPIRE_MAP, tadb_name=SEAEMPIRE_DB, ta_url=SEAEMPIRE_URL, ta_password=SEAEMPIRE_PASSWORD)


PROJECT = {DOW2.appname: DOW2, 
           DOW.appname: DOW, 
           SEAEMPIRE.appname: SEAEMPIRE
           }