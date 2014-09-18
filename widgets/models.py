import widgy

from widgy.contrib.page_builder.models import Layout, DefaultLayout

widgy.unregister(DefaultLayout)


@widgy.register
class HomepageLayout(Layout):
    pass


@widgy.register
class WhateverpageLayout(Layout):
    pass
