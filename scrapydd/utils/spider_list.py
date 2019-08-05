import os
import pkg_resources
from scrapy.spiderloader import SpiderLoader
from scrapy.settings import Settings
import sys

def activate_egg(eggpath):
    """Activate a Scrapy egg file. This is meant to be used from egg runners
    to activate a Scrapy egg file. Don't use it from other code as it may
    leave unwanted side effects.
    """
    try:
        d = pkg_resources.find_distributions(eggpath).next()
    except StopIteration:
        raise ValueError("Unknown or corrupt egg")
    d.activate()
    settings_module = d.get_entry_info('scrapy', 'settings').module_name
    os.environ.setdefault('SCRAPY_SETTINGS_MODULE', settings_module)
    return settings_module

def main(egg_path=None):
    settings_module = activate_egg(egg_path)

    settings = Settings()
    settings.setmodule(settings_module)
    loader = SpiderLoader(settings)
    print(loader.list())

if __name__ == '__main__':
    print(sys.argv)
    main(sys.argv[1])
