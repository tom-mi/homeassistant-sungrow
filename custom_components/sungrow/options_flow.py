import voluptuous as vol
from homeassistant.config_entries import OptionsFlow, ConfigEntry
from homeassistant.const import CONF_SCAN_INTERVAL

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
            vol.Optional(CONF_SCAN_INTERVAL, default=self.config_entry.data.get(CONF_SCAN_INTERVAL, 60)): int,
        })

        return self.async_show_form(
            step_id="init",
            data_schema=options_schema,
        )
