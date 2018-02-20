from django.apps import AppConfig
from django.utils.translation import ugettext_lazy


class PluginApp(AppConfig):
    name = 'pretix_cpanalytics'
    verbose_name = 'Chris's Pretix Analytics plugin'

    class PretixPluginMeta:
        name = ugettext_lazy('Chris's Pretix Analytics plugin')
        author = 'Christopher P Yarger'
        description = ugettext_lazy('Analytics plugin for pretix')
        visible = True
        version = '1.0.0'

    def ready(self):
        from . import signals  # NOQA


default_app_config = 'pretix_cpanalytics.PluginApp'
