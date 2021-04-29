from __future__ import print_function
try:
    input = raw_input
except NameError:
    pass
from pc_lib_api import pc_api
import pc_lib_general

# --Configuration-- #

parser = pc_lib_general.pc_arg_parser_defaults()
# INSERT SCRIPT-SPECIFIC ARGUMENTS HERE
args = parser.parse_args()

# --Initialize-- #

pc_lib_general.prompt_for_verification_to_continue(args.yes)
pc_settings = pc_lib_general.pc_settings_get(args.username, args.password, args.uiurl, args.config_file)
pc_api.configure(pc_settings['apiBase'], pc_settings['username'], pc_settings['password'])

# --Main-- #

# INSERT SCRIPT CODE HERE
result = pc_api.current_user()
print(result)