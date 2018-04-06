import json

def load_error_desc(filename):
    error_dict = {}

    #载入主网合约abi
    with open(filename) as server_error_file:
        error_dict = json.load(server_error_file)
    return error_dict

def build_error_result(error_dict, error_tag):
    if not error_dict.__contains__(error_tag):
        print(error_dict)
        print(error_dict["SERVER_INTERNAL_ERR"], error_tag)

        code = error_dict["SERVER_INTERNAL_ERR"]["code"]
        desc = error_dict["SERVER_INTERNAL_ERR"]["desc"]
    else:
        print(error_dict[error_tag], error_tag)

        code = error_dict[error_tag]["code"]
        desc = error_dict[error_tag]["desc"]
    return { "retcode": code, "message" : desc }
