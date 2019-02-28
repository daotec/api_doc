# RESTful API for Dao-Tec    


## 建立连接    

REST访问的根URL：`https://www.dao-tec.com/api/v1`     
所有请求基于Https协议，请求头中contentType设置为：`application/x-www-form-urlencoded`    
	
建立连接说明    
1. 请求参数：根据接口请求参数规定进行参数封装。    
2. 发送参数：将封装好的参数通过GET、POST、PUT或DELETE方式提交。  
3. 服务器响应：服务器首先对用户请求数据进行校验，通过校验后将响应数据以JSON格式返回给用户。   

## API参考  

### 信息 API 

获取dao-tec的一些基本信息

1. GET /api/v1/exchanges 获取支持交易所信息

URL `https://www.dao-tec.com/api/v1/exchanges`	访问频率 20次/2秒

示例	

```
# Request
GET http://127.0.0.1:8000/api/v1/exchanges?exchange_type=spot
# Response
{
    "status": 1, 
    "data": [
        {"id": "okex", "terrace_name": "OKEX"}, 
        {"id": "huobi", "terrace_name": "Huobi"}, 
        {"id": "binance", "terrace_name": "Binance"}
    ]
}
```

返回值说明	

```
status: 请求成功或失败
id: 交易所代号
terrace_name: 交易所名称
```

请求参数	

|参数名|	参数类型|	必填|	描述|
| :-----    | :-----   | :-----    | :-----   |
|exchange_type|String|是|标的类型如: 现货交易spot, 合约交易future, 所有all|

2. GET /api/v1/symbols 获取交易的标的

URL `https://www.dao-tec.com/api/v1/symbols`	访问频率 20次/2秒

示例	

```
# Request
GET http://www.dao-tec.com/api/v1/symbols?exchange=okex
# Response
{
    "status": 1, 
    "data": [
        {"symbol_id": "btc_usdt", "symbol_name": "btc_usdt"},
        {"symbol_id": "eos_usdt", "symbol_name": "eos_usdt"}, 
        {"symbol_id": "ltc_usdt", "symbol_name": "ltc_usdt"}, 
        {"symbol_id": "eth_usdt", "symbol_name": "eth_usdt"}, 
        {"symbol_id": "xrp_usdt", "symbol_name": "xrp_usdt"}
    ]
}
```

返回值说明	

```
status: 请求成功或失败
symbol_id: 标的代号
symbol_name: 标的名称
```

请求参数	

|参数名|	参数类型|	必填|	描述|
| :-----    | :-----   | :-----    | :-----   |
|exchange|String|是|交易所: okex, huobi, binance, okexf(okex合约)|


### 行情 API 

获取dao-tec行情数据  

1. GET /api/v1/tickers    获取OKEx币币行情

URL `https://www.dao-tec.com/api/v1/tickers`	访问频率 20次/2秒

示例	

```
# Request
GET https://www.dao-tec.com/api/v1/tickers?exchange=okex&symbol=btc_usdt
# Response
{
    "status": 1, 
    "data": {
        "date": 1550686758.307304, 
        "bid": "3954.5009"
        "high": "3984.6497", 
        "last": "3954.6499", 
        "low": "3881.2552", 
        "ask": "3955.3995",
        "vol": "45584.746610545",   
    }
}
```

返回值说明	

```
date: 返回数据时服务器时间
bid: 买一价
high: 最高价
last: 最新成交价
low: 最低价
ask: 卖一价
vol: 成交量(最近24小时)
```

请求参数	

|参数名|	参数类型|	必填|	描述|
| :-----    | :-----   | :-----    | :-----   |
|exchange|String|是|交易所, 如okex|
|symbol|String|是|标的, 如btc_usdt|

2. GET /api/v1/depths   获取dao-tec市场深度

URL `https://www.dao-tec.com/api/v1/depths`	访问频率 20次/2秒

示例	

```
# Request
GET https://www.dao-tec.com/api/v1/depths?exchange=okex&symbol=btc_usdt
# Response
{
    "status": 1, 
    "data": {
        "date": 1550690368.872222, 
        "asks": [
            [3956, 0.007], 
            [3955.9995, 0.06], 
            [3955.7995, 0.06], 
            [3955.7868, 0.998], 
            [3955.7, 0.006], 
            [3955.5995, 0.06], 
            [3955.5331, 0.104], 
            [3955.2508, 0.40415165], 
            [3955.2505, 0.03074834]
        ], 
        "bids": [
            [3954.9833, 0.001], 
            [3954.9706, 0.01940527], 
            [3954.8793, 1.06], 
            [3954.8792, 4.17441423], 
            [3954.6474, 0.014], 
            [3954.6368, 0.04534968], 
            [3954.6134, 0.03024269], 
            [3954.6005, 0.06], 
            [3954.4598, 0.03024396]
        ]
    }
}
```

返回值说明	

```
asks :卖方深度
bids :买方深度
```

请求参数	

|参数名|	参数类型|	必填|	描述|
| :-----    | :-----   | :-----    | :-----   |
|exchange|String|是|交易所, 如okex|
|symbol|String|是|标的, 如btc_usdt|

3. Get /api/v1/klines    获取dao-tec K线数据(1min)

URL `https://www.dao-tec.com/api/v1/klines`	访问频率 20次/2秒

示例	

```
# Request
GET https://www.dao-tec.com/api/v1/klines?exchange=okex&symbol=btc_usdt
# Response
{
    "status": 1, 
    "data": [
        [
            1550675160000, 
            "3952.0538", 
            "3952.6724", 
            "3950.6132", 
            "3950.6259", 
            "18.87557114"
        ], 
        [
            1550675220000, 
            "3950.6386", 
            "3950.706", 
            "3947.8935", 
            "3947.8936", 
            "22.30932163"
        ], 
        [
            1550675280000, 
            "3947.8936", 
            "3947.8937", 
            "3945.5003", 
            "3945.739", 
            "15.84687589"
        ]
    ]
}
```

返回值说明	

```
[
	1550675160000,	时间戳
	"3952.0538",	开
	"3952.6724",	高
	"3950.6132",	低
	"3950.6259",	收
	"18.87557114"	交易量
]
```

请求参数	

|参数名|	参数类型|	必填|	描述|
| :-----    | :-----   | :-----    | :-----   |
|exchange|String|是|交易所, 如okex|
|symbol|String|是|标的, 如btc_usdt|

### 币币交易 API 

用于dao-tec币币交易  

1. GET /api/v1/balances    获取用户信息

URL `https://www.dao-tec.com/api/v1/balances`	访问频率 6次/2秒    

示例	

```
# Request
GET https://www.dao-tec.com/api/v1/balances?api_key=apiKey&exchange=okex&account_type=api_bind&symbol=btc_usdt&strategy_name=manual_trading&signature=sig
# Response
{
    "status": 1, 
    "data": {
        "coin": {
            "coin": "btc", 
            "free": 1.0753766, 
            "balance": 1.0753766
        }, 
        "basecoin": {
            "basecoin": "usdt", 
            "free": 5.0862397, 
            "balance": 5.0862397
        }
    }
}
```

返回值说明	

```
coin:交易币名
basecoin:基础货币名
free:账户可用余额
balance:账户余额
```

请求参数	

|参数名|	参数类型|	必填|	描述|
| :-----    | :-----   | :-----    | :-----   |
|api_key|String|是|用户申请的apiKey|
|exchange|String|是|交易所名字|
|account_type|String|是|交易账户类型|
|symbol|String|是|标的|
|strategy_name|String|是|策略名字|
|signature|String|是|请求参数的签名|

2. POST /api/v1/orders    下单交易

URL `https://www.dao-tec.com/api/v1/orders`	访问频率 20次/2秒	

示例	

```
# Request
POST https://www.dao-tec.com/api/v1/orders
# Response
{"status": 1, "data": "\\u4e0b\\u5355\\u6210\\u529f, \\u4ea4\\u6613\\u6240: okex, \\u6807\\u7684: eos_usdt, \\u4ef7\\u683c: 5.1, \\u6570\\u91cf: 0.3", "order_id": 2364535153626112}
```

返回值说明	

```
status:1代表成功返回
order_id:订单ID
```

请求参数	

|参数名|	参数类型|	必填|	描述|
| :-----    | :-----   | :-----    | :-----   |
|api_key|String|是|用户申请的apiKey|
|exchange|String|是|用户要交易的交易所|
|account_type|String|是|用户交易的账户类型|
|symbol|String|是|币对如btc_usdt|
|strategy_name|String|是|用户交易的策略名|
|order_type|String|是|买卖类型：限价单(buy_limit/sell_limit) 市价单(buy_market/sell_market)|
|price|Double|是|下单价格|
|amount|Double|是|交易数量|
|money_num|Double|是|目前填0|
|signature|String|是|请求参数的签名|

3. GET /api/v1/orders    获取用户的订单信息

URL `https://www.dao-tec.com/api/v1/orders`	访问频率 20次/2秒(未成交)

示例	

```
# Request
GET https://www.dao-tec.com/api/v1/orders
# Response
{
    'status': 1, 
    'data': {
        'page_num': 1, 
        'page_num_list': [1, 2, 3, 4, 5], 
        'order_list': [
            {
                'order_timestamp': 1550815943.341732, 
                'user_name': '15530290099', 
                'phone_num': '15530290099', 
                'exchange': 'okex', 
                'account_type': 'api_bind', 
                'strategy_name': 'manual_trading', 
                'symbol': 'eos_usdt', 
                'order_type': 'sell_limit', 
                'order_id': '2364535153626112', 
                'price': '5.1', 
                'avg_price': 0.0, 
                'quantity': '0.3', 
                'quantity_treaded': 0.0, 
                'quantity_frozen': 0.0, 
                'quantity_canceled': 0.3, 
                'order_cancel_timestamp': 1550887379.142241, 
                'order_deal_timestamp': 0.0, 
                'order_status': 'cancelled'
            }
        ]
    }
}
```

返回值说明	

```
order_timestamp:委托时间
exchange:交易所
account_type:账户类型
strategy_name:策略名
symbol:标的
order_type:订单类型
order_id:订单ID
price:委托价格
avg_price:平均成交价
quantity:委托数量
quantity_treaded:成交数量
quantity_frozen:冻结数量
quantity_canceled:撤销数量
order_cancel_timestamp:订单撤销时间
order_deal_timestamp:订单成交时间
order_status:订单状态
```

请求参数	

|参数名|	参数类型|	必填|	描述|
| :-----    | :-----   | :-----    | :-----   |
|api_key|String|是|用户申请的apiKey|
|exchange|String|是|用户要交易的交易所|
|account_type|String|是|用户交易的账户类型|
|symbol|String|是|币对如btc_usdt|
|strategy_name|String|是|用户交易的策略名|
|order_id|String|是|订单ID|
|signature|String|是|请求参数的签名|

4. DELETE /api/v1/orders    撤销订单

URL `https://www.dao-tec.com/api/v1/orders`	访问频率 20次/2秒

示例	

```
# Request
DELETE https://www.dao-tec.com/api/v1/orders
# Response
{"success":"123456,123457","error":"123458,123459"}
```

返回值说明	

```
result:true撤单请求成功，等待系统执行撤单；false撤单失败(用于单笔订单)
order_id:订单ID(用于单笔订单)
success:撤单请求成功的订单ID，等待系统执行撤单(用于多笔订单)
error:撤单请求失败的订单ID(用户多笔订单)
```

请求参数	

|参数名|	参数类型|	必填|	描述|
| :-----    | :-----   | :-----    | :-----   |
|api_key|String|是|用户申请的apiKey|
|exchange|String|是|用户要交易的交易所|
|account_type|String|是|用户要交易的账户类型|
|symbol|String|是|币对如btc_usdt|
|strategy_name|String|是|用户交易的策略名|
|order_id|String|是|订单ID|
|signature|String|是|请求参数的签名|
