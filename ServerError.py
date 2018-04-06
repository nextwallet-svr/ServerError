import json

server_error_dict = {}

def load_error_desc():
	#载入主网合约abi
    with open("serverError.json") as server_error_file:
        server_error_dict = json.load(server_error_file)

def build_error_result(error_tag):
	if not server_error_dict.__contains__(error_tag):
		code = server_error_dict["SERVER_INTERNAL_ERR"]["code"]
		desc = server_error_dict["SERVER_INTERNAL_ERR"]["desc"]
	else:
		code = server_error_dict[error_tag]["code"]
		desc = server_error_dict[error_tag]["desc"]
	return { "retcode": code, "message" : desc }


