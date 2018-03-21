#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import pygal
import json

from country_codes import get_country_code 

filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)
    
# 创建一个包含人口数量的字典
cc_population ={}
for pop_dict in pop_data:
    if pop_dict['Year'] == 2010 :
        country = pop_dict['Country_name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country)
        if code:
            cc_population[code] = population

wm = pygal.maps.world.World()
wm.title= 'World population in 2010, by country'
wm.add('2010', cc_population)

wm.render_to_file('World population.svg')  
