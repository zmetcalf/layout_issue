import widgy

from django.db import models

from widgy.db.fields import VersionedWidgyField
from widgy.models import links

from widgy_blog.models import AbstractBlog, AbstractBlogLayout
from widgy_blog.site import site


@links.register
class News(AbstractBlog):
    content = VersionedWidgyField(
        null=False,
        on_delete=models.PROTECT,
        site=site,
        verbose_name='News Content',
        root_choices=[
            'NewsLayout',
        ],
    )


@widgy.register
class NewsLayout(AbstractBlogLayout):
    owner_class = News
