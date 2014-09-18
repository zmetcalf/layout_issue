from widgy.site import WidgySite

from widgets.models import HomepageLayout, WhateverpageLayout


class WidgySite(WidgySite):
    def valid_root_of(self, owner_class, root_class, root_choices):
        from widgy.contrib.widgy_mezzanine.models import WidgyPage
        if issubclass(owner_class, WidgyPage):
            return issubclass(root_class, (HomepageLayout, WhateverpageLayout,))
        else:
            return super(WidgySite, self).valid_root_of(owner_class, root_class, root_choices)


site = WidgySite()
