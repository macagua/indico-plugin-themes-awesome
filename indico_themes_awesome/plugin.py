#from __future__ import unicode_literals

import os

from flask.helpers import get_root_path

from indico.core.signals.plugin import get_event_themes_files
from indico.core.plugins import IndicoPlugin, IndicoPluginBlueprint

class AwesomeThemesPlugin(IndicoPlugin):
    """Awesome Themes
    Provides event themes for Awesome Events.
    """

    def init(self):
        super(AwesomeThemesPlugin, self).init()
        self.connect(get_event_themes_files, self._get_themes_yaml)

    def get_blueprints(self):
        return IndicoPluginBlueprint(self.name, __name__)

    def _get_themes_yaml(self, sender, **kwargs):
        return os.path.join(get_root_path('indico_themes_awesome'), 'themes.yaml')

