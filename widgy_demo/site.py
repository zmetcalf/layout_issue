from widgy.site import WidgySite

from widgets.models import HomepageLayout, WhateverpageLayout


class WidgySite(WidgySite):
    def valid_root_of(self, owner_class, root_class, root_choices):
        return issubclass(root_class, (HomepageLayout, WhateverpageLayout,))


site = WidgySite()
