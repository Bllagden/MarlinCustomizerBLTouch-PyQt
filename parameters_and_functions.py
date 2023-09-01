convert_to_limit_switch = {  # параметры для датчика концевика
    0: ("uncomm", "#define PROBE_MANUALLY"),
    1: ("uncomm", "#define MANUAL_PROBE_START_Z"),
    2: ("comm", "#define BLTOUCH"),

    3: ("edit", "#define X_PROBE_OFFSET_FROM_EXTRUDER"),
    4: ("edit", "#define Y_PROBE_OFFSET_FROM_EXTRUDER"),

    5: ("comm", "#define MULTIPLE_PROBING 2"),

    6: ("comm", "#define AUTO_BED_LEVELING_3POINT"),
    7: ("comm", "#define AUTO_BED_LEVELING_LINEAR"),
    8: ("comm", "#define AUTO_BED_LEVELING_BILINEAR"),
    9: ("comm", "#define AUTO_BED_LEVELING_UBL"),
    10: ("uncomm", "#define MESH_BED_LEVELING"),

    11: ("uncomm", "#define GRID_MAX_POINTS_X 3"),
    12: ("comm", "#define GRID_MAX_POINTS_X 4"),

    13: ("comm", "#define LEFT_PROBE_BED_POSITION"),
    14: ("comm", "#define RIGHT_PROBE_BED_POSITION"),
    15: ("comm", "#define FRONT_PROBE_BED_POSITION"),
    16: ("comm", "#define BACK_PROBE_BED_POSITION")
}
"""Расшифровка типов операций с настройками

"comm": закомментировать
"uncomm": раскомментировать
"edit": изменить параметры в конце строки статически

"""

convert_to_bltouch = {  # параметры для датчика BLTouch
    0: ("comm", "#define PROBE_MANUALLY"),
    1: ("comm", "#define MANUAL_PROBE_START_Z"),
    2: ("uncomm", "#define BLTOUCH"),

    3: ("edit", "#define X_PROBE_OFFSET_FROM_EXTRUDER"),
    4: ("edit", "#define Y_PROBE_OFFSET_FROM_EXTRUDER"),

    5: ("selection", "#define MULTIPLE_PROBING 2"),

    6: ("selection", "#define AUTO_BED_LEVELING_3POINT"),
    7: ("selection", "#define AUTO_BED_LEVELING_LINEAR"),
    8: ("selection", "#define AUTO_BED_LEVELING_BILINEAR"),
    9: ("selection", "#define AUTO_BED_LEVELING_UBL"),
    10: ("comm", "#define MESH_BED_LEVELING"),

    11: ("selection", "#define GRID_MAX_POINTS_X 3"),
    12: ("selection", "#define GRID_MAX_POINTS_X 4"),

    13: ("uncomm + edit", "#define LEFT_PROBE_BED_POSITION"),
    14: ("uncomm + edit", "#define RIGHT_PROBE_BED_POSITION"),
    15: ("uncomm + edit", "#define FRONT_PROBE_BED_POSITION"),
    16: ("uncomm + edit", "#define BACK_PROBE_BED_POSITION")
}
"""Расшифровка типов операций с настройками

"comm": закомментировать
"uncomm": раскомментировать
"edit": изменить параметры в конце строки динамически
"uncomm + edit": раскомментировать и изменить параметры в конце строки динамически
"selection": считать значение нажатой кнопки (в блоке кнопок может быть нажата только одна) или введенного значения

"""


def comm(string):
    """функция закомментирования строки"""
    n_space = len(string) - len(string.lstrip(" "))
    head, sep, tail = string.partition("#define")
    string = (" " * n_space) + "//" + sep + tail
    return string


def uncomm(string):
    """функция раскомментирования строки"""
    n_space = len(string) - len(string.lstrip(" "))
    head, sep, tail = string.partition("#define")
    string = (" " * n_space) + sep + tail
    return string


def clear_parameters(string, separator):
    """функция удаления параметров в конце строки"""
    head, sep, tail = string.partition(separator)
    return head + sep
