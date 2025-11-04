import voluptuous as vol
from homeassistant.config_entries import OptionsFlow, ConfigEntry
from homeassistant.const import CONF_SCAN_INTERVAL

class SungrowInverterOptionsFlow(OptionsFlow):
    def __init__(self, config_entry: ConfigEntry):
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        options_schema = vol.Schema({
            vol.Optional(CONF_SCAN_INTERVAL, default=self.config_entry.options.get(CONF_SCAN_INTERVAL, 30)): int,
        })

        return self.async_show_form(
            step_id="init",
            data_schema=options_schema,
        )
