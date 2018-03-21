#!/usr/bin/env python
# -*- coding: utf-8 -*-
#


import pygal

from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
    """根据指定国家，返回pygal使用的两个字母的国别码"""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
        return None
