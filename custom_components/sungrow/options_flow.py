import voluptuous as vol
from homeassistant.config_entries import OptionsFlow, ConfigEntry


class SungrowInverterOptionsFlow(OptionsFlow):
    def __init__(self, config_entry: ConfigEntry):
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        options_schema = vol.Schema({
            vol.Optional("scan_interval", default=self.config_entry.options.get("scan_interval", 30)): int,
            vol.Optional("use_local_time", default=self.config_entry.options.get("use_local_time", False)): bool,
        })

        return self.async_show_form(
            step_id="init",
            data_schema=options_schema,
        )
