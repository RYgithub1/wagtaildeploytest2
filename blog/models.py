from django.conf import settings
from django.db import models
from django.utils import timezone

''' WAGTAIL '''
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.search import index



''' WAGTAIL '''
class BlogPage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]
    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('intro'),
        FieldPanel('body', classname="full"),
    ]



class BlogIndexPage(Page):
    intro = RichTextField(blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]



# class GenericPage(Page):
#     banner_title = models.CharField(
#       max_length=100,
#       default='GENERIC here',
#     )
#     content_panels = Page.content_panels + [
#         FieldPanel('banner_title'),
#     ]



class HomePage(Page):
    body = RichTextField(blank=True)
    # banner_title = models.CharField(
    #   max_length=100,
    #   default='Welcome Home',
    # )
    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        # FieldPanel('banner_title'),
    ]






''' APP '''
class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

