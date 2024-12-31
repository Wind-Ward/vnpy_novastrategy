APP_NAME = "NovaStrategy"


EVENT_NOVA_LOG = "eNovaLog"
EVENT_NOVA_STRATEGY = "eNovaStrategy"

STOPORDER_PREFIX = "STOP"

from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime, timedelta
from vnpy.trader.constant import Direction, Offset, Interval, Exchange
from typing import Dict

class StopOrderStatus(Enum):
    WAITING = "等待中"
    CANCELLED = "已撤销"
    TRIGGERED = "已触发"
    
    
    

@dataclass
class StopOrder:
    symbol: str
    exchange: Exchange 
    direction: Direction
    offset: Offset
    price: float
    volume: float
    stop_orderid: str
    strategy_name: str
    datetime: datetime
    vt_orderids: list = field(default_factory=list)
    status: StopOrderStatus = StopOrderStatus.WAITING
    reason: str = ""

    def __post_init__(self) -> None:
        """"""
        self.vt_symbol: str = f"{self.symbol}.{self.exchange.value}"
