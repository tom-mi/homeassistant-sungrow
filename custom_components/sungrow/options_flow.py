import voluptuous as vol
from homeassistant.config_entries import OptionsFlow
from homeassistant.const import CONF_SCAN_INTERVAL
from homeassistant.helpers import config_validation as cv

# Constants for host, port, and slave
CONF_HOST = "host"
CONF_PORT = "port"
CONF_SLAVE = "slave"

class SungrowInverterOptionsFlow(OptionsFlow):

    async def async_step_init(self, user_input=None):
        # hack to adapt config instead of options, see https://community.home-assistant.io/t/configflowhandler-and-optionsflowhandler-managing-the-same-parameter/365582/4
        if user_input is not None:
            self.hass.config_entries.async_update_entry(
                self.config_entry,
                data={**self.config_entry.data, **user_input},
            )
            return self.async_create_entry(title="", data={})

        options_schema = vol.Schema({
            vol.Optional(CONF_HOST, default=self.config_entry.data.get(CONF_HOST, "")): cv.string,
            vol.Optional(CONF_PORT, default=self.config_entry.data.get(CONF_PORT, 502)): cv.port,
            vol.Optional(CONF_SLAVE, default=self.config_entry.data.get(CONF_SLAVE, 1)): int,
            vol.Optional(CONF_SCAN_INTERVAL, default=self.config_entry.data.get(CONF_SCAN_INTERVAL, 60)): int,
        })

        return self.async_show_form(
            step_id="init",
            data_schema=options_schema,
        )
