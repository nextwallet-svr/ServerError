import json

def load_error_desc(filename):
    error_dict = {}

    with open(filename) as server_error_file:
        error_dict = json.load(server_error_file)
    return error_dict

def build_error_result(error_dict, error_tag):
    code = 0
    desc = ''
    try:
        if not error_dict.__contains__(error_tag):
            raise Exception('not support error_tag')
        else:
            # print(error_dict[error_tag], error_tag)
            code = error_dict[error_tag]["code"]
            desc = error_dict[error_tag]["desc"]
    except (Exception) as e:
        print(e, error_tag)
        code = error_dict["SERVER_INTERNAL_ERR"]["code"]
        desc = error_dict["SERVER_INTERNAL_ERR"]["desc"]
    finally:
        return { "retcode": code, "message" : desc }
