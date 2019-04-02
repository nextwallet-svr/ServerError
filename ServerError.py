import json
import os
import re


def load_error_desc(filename):
    error_dict = {}

    with open(filename) as server_error_file:
        error_dict = json.load(server_error_file)
    return error_dict


def build_error_result(error_dict, error_tag, *extra_info, **kwargs):
    code = 0
    desc = ''
    try:
        if error_tag not in error_dict:
            code = 1
            desc = error_tag
        else:
            code = error_dict[error_tag]["code"]
            desc = error_dict[error_tag]["desc"]
    except (Exception) as e:
        print(e, error_tag)
        code = error_dict["SERVER_INTERNAL_ERR"]["code"]
        desc = error_dict["SERVER_INTERNAL_ERR"]["desc"]
    finally:
        final = {"retcode": code, "message": desc}
        if extra_info:
            final['extra'] = extra_info
        if kwargs:
            final['extra'] = kwargs
            if re.findall('\{\w+\}', desc):
                try:
                    final['message'] = desc.format(**kwargs)
                except KeyError as e:
                    pass
        return final


server_error_dict = load_error_desc(os.path.abspath(
    os.path.dirname(__file__)) + "/serverError.json")


def ErrorRsp(err_tag, *extra_info, **kwargs):
    return build_error_result(server_error_dict, err_tag, *extra_info, **kwargs)


SUCCESS = ErrorRsp('SUCC')
FAIL = ErrorRsp('SERVER_INTERNAL_ERR')
