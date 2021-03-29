from common.po_base import El
from common.po_base import Page


class EventPage(Page):
    work_bench = El("点击工作台", x='//*[@id="app"]/div[2]/div/div[1]/a[2]')

