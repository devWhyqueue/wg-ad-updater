import logging.config
from pathlib import Path
from time import sleep

import click
import pkg_resources
from click import command, option, argument
from selenium.common.exceptions import WebDriverException

from wgrequestupdater.webdriver import chrome_driver

logging_config = pkg_resources.resource_filename(__name__, str(Path('config/logging.ini')))
logging.config.fileConfig(logging_config, disable_existing_loggers=False)
log = logging.getLogger("wgrequestupdater.main")


@command()
@argument('username')
@argument('password')
@option('--chromium-path', type=click.Path())
def cli(username, password, chromium_path):
    from wgrequestupdater.updater import WgRequestUpdater
    log.info("WG Request updater successfully started.")
    while True:
        webdriver = chrome_driver(chromium_path)
        req = WgRequestUpdater(webdriver)
        try:
            req.update(username, password)
        except WebDriverException:
            log.error(f"A WebDriver exception occurred!")
            log.debug("Following exception was thrown:", exc_info=True)
        finally:
            webdriver.quit()
            sleep(3600)


if __name__ == '__main__':
    cli()
